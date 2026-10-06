"""Resumable, bounded native GPU Japanese Base evaluation (no training/test)."""
import argparse
from collections import Counter, defaultdict
from contextlib import nullcontext
import hashlib
import json
import math
import os
from pathlib import Path
import random
import sys
import time

import numpy as np
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from jmicro.japanese_evaluation import (NativeLikelihood, answer_metrics, classification_summary,
    clustered_ci, encode_request, repetition_metrics, tied_prediction)
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import gpu_lock
from prepare_japanese_evaluation import load_records

ACTIVE_JOB = None


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def select(rows, limit, seed):
    rows = list(rows)
    random.Random(seed).shuffle(rows)
    return rows[:limit] if limit is not None else rows


def nli_prompt(row):
    return f"前提：{row['sentence1']}\n判断する文：{row['sentence2']}\nこの文は前提だけから判断すると、\n"


def cola_prompt(row):
    return f"例文：{row['sentence']}\nこの例文の日本語の文法は、\n"


NLI_LABELS = ["entailment", "contradiction", "neutral"]
NLI_CHOICES = ["正しい。", "誤りだ。", "正しいか誤りかは不明だ。"]
COLA_CHOICES = ["不自然だ。", "自然だ。"]


def balanced_examples(rows, labels, prompt, choices):
    # First official train occurrence per class; no dev-driven selection.
    examples = [next(row for row in rows if row["label"] == label) for label in labels]
    return "\n".join(prompt(row) + choices[labels.index(row["label"])] + "\n" for row in examples)


def build_tasks(config, pilot=False):
    data = Path(config["data"])
    sources = json.loads((data / "manifest.json").read_text())["sources"]
    for source in sources.values():
        if digest(source["path"]) != source["sha256"]:
            raise ValueError("Evaluation source hash changed")
    load = lambda name: load_records(data / (name + ".json"))
    limit = config["pilot_examples"] if pilot else None
    seed = config["pilot_seed"]
    tasks, controls = {}, {}
    semantic = [row for row in load_records(config.get("semantic_suite", "eval/japanese_semantics_v2.jsonl")) if row["split"] == "dev"]
    tasks["semantics"] = semantic
    controls["semantics"] = {"chance": .5, "train_majority_label": 0,
                             "constant_candidate": "paired variants have identical candidates and opposite gold labels"}
    tasks["jblimp"] = [{"id": str(row["ID"]), "family": str(row["ID"]), "category": row["phenomenon"],
                         "context": "", "choices": [row["good_sentence"], row["bad_sentence"]], "label": 0}
                        for row in load("jblimp")]
    # Good-first storage does NOT define a meaningful first-position baseline.
    controls["jblimp"] = {"chance": .5, "train_majority_label": None,
                         "note": "minimal pair preference; labels are not a classification prior"}
    tasks["jcqa"] = [{"id": str(row["q_id"]), "category": "commonsense", "context": f"質問：{row['question']}\n答えは、\n",
                       "choices": [row[f"choice{i}"] for i in range(5)], "label": int(row["label"])}
                      for row in select(load("jcqa_dev"), limit, seed)]
    controls["jcqa"] = {"chance": .2, "train_majority_label": Counter(int(r["label"]) for r in load("jcqa_train")).most_common(1)[0][0]}
    nli_train, cola_train = load("jnli_train"), load("jcola_train")
    nli_examples = balanced_examples(nli_train, NLI_LABELS, nli_prompt, NLI_CHOICES)
    cola_examples = balanced_examples(cola_train, [0, 1], cola_prompt, COLA_CHOICES)
    for fewshot in (False, True):
        name = "jnli_3shot" if fewshot else "jnli_0shot"
        tasks[name] = [{"id": str(r["sentence_pair_id"]), "family": r["yjcaptions_id"].split("-")[0], "category": r["label"],
                        "context": (nli_examples if fewshot else "") + nli_prompt(r), "choices": NLI_CHOICES,
                        "label": NLI_LABELS.index(r["label"])} for r in select(load("jnli_dev"), limit, seed)]
        controls[name] = {"chance": 1/3, "train_majority_label": NLI_LABELS.index(Counter(r["label"] for r in nli_train).most_common(1)[0][0]),
                          "fewshot": 3 if fewshot else 0, "fixed_train_examples": nli_examples if fewshot else None}
        for domain in ("in", "out"):
            name = f"jcola_{domain}_{'2shot' if fewshot else '0shot'}"
            tasks[name] = [{"id": str(r["uid"]), "category": r["source"],
                            "context": (cola_examples if fewshot else "") + cola_prompt(r),
                            "choices": COLA_CHOICES, "label": int(r["label"])}
                           for r in select(load("jcola_" + domain), limit, seed)]
            controls[name] = {"chance": .5, "train_majority_label": Counter(int(r["label"]) for r in cola_train).most_common(1)[0][0],
                              "fewshot": 2 if fewshot else 0, "fixed_train_examples": cola_examples if fewshot else None}
    return tasks, controls


def summarize(rows, control):
    count = len(rows)
    categories = defaultdict(list)
    for row in rows:
        categories[row["category"]].append(row)
    primary, normalized, unigram = {}, {}, {}
    for name, credit, pred in (("primary", "credit", "prediction"), ("normalized", "normalized_credit", "normalized_prediction"),
                               ("unigram", "unigram_credit", "unigram_prediction")):
        mapped = [dict(row, credit=row[credit], prediction=row[pred]) for row in rows]
        score = {"accuracy": clustered_ci(mapped), **classification_summary(mapped, len(rows[0]["choices"]))} if rows else {"count": 0}
        if name == "primary": primary = score
        elif name == "normalized": normalized = score
        else: unigram = score
    majority = control.get("train_majority_label")
    return {"count": count, "primary": primary, "per_token_secondary": normalized,
            "unigram_control": unigram, "chance": control["chance"],
            "above_chance_evidence": bool(count and primary["accuracy"]["ci95"][0] > control["chance"]),
            "train_majority_accuracy": sum(row["label"] == majority for row in rows)/count if majority is not None and count else None,
            "categories": {key: clustered_ci(value) for key, value in categories.items()},
            "tie_examples": sum(row["ties"] > 1 for row in rows),
            "limitations": "single model training seed; dev diagnostic, no practical-quality acceptance"}


def evaluate_choices(scorer, cases, control, unigram, path, binding, deadline, slor=False):
    old = json.loads(path.read_text()) if path.exists() else {"binding": binding, "rows": []}
    if old["binding"] != binding:
        raise ValueError(f"Cannot reuse incompatible stage {path}")
    rows = old["rows"]
    if [r["id"] for r in rows] != [r["id"] for r in cases[:len(rows)]]:
        raise ValueError("Resume case order differs")
    excluded = old.get("excluded", [])
    if excluded:
        # No cases are silently dropped from complete official-dev tasks.
        raise ValueError("Stage with exclusions requires explicit review")
    while len(rows) < len(cases):
        if time.monotonic() > deadline:
            break
        chunk = cases[len(rows):len(rows)+32]
        pairs = [(row["context"], choice) for row in chunk for choice in row["choices"]]
        scored = scorer.score(pairs)
        offset = 0
        for case in chunk:
            choices = scored[offset:offset+len(case["choices"])]
            offset += len(choices)
            raw = [s["log_likelihood"] for s in choices]
            prior = [float(unigram[s["target_ids"]].sum()) for s in choices]
            normalized = [ll / s["target_tokens"] for ll, s in zip(raw, choices)]
            corrected = [(ll-base)/s["target_tokens"] for ll, base, s in zip(raw, prior, choices)]
            primary = corrected if slor else raw
            unigram_scores = [base/s["target_tokens"] for base, s in zip(prior, choices)] if slor else prior
            row = {**case, **tied_prediction(primary, case["label"]), "scores": primary, "raw_log_likelihood": raw,
                   "target_tokens": [s["target_tokens"] for s in choices], "token_normalized": normalized,
                   "train_sample_slor": corrected, "unigram_scores": unigram_scores}
            secondary = tied_prediction(normalized, case["label"])
            baseline = tied_prediction(unigram_scores, case["label"])
            row.update(normalized_prediction=secondary["prediction"], normalized_credit=secondary["credit"],
                       unigram_prediction=baseline["prediction"], unigram_credit=baseline["credit"])
            if slor:
                row["raw_credit"] = tied_prediction(raw, case["label"])["credit"]
            rows.append(row)
        save(path, {"binding": binding, "rows": rows, "expected": len(cases),
                    "complete": len(rows) == len(cases), "control": control})
    summary = summarize(rows, control)
    save(path, {"binding": binding, "rows": rows, "expected": len(cases),
                "complete": len(rows) == len(cases), "summary": summary, "control": control})
    return {"path": str(path), "complete": len(rows) == len(cases), "expected": len(cases), **summary,
            **({"raw_pair_accuracy": sum(r["raw_credit"] for r in rows)/len(rows)} if slor and rows else {})}


def evaluate_qa(scorer, config, output, binding, deadline):
    data = load_records(Path(config["data"]) / "jsquad_dev.json")
    cases = []
    paragraphs = []
    for article in data["data"]:
        for paragraph in article["paragraphs"]:
            paragraphs.append({"title": article["title"], "text": paragraph["context"]})
            for qa in paragraph["qas"]:
                cases.append({"id": qa["id"], "family": hashlib.sha256(paragraph["context"].encode()).hexdigest(),
                              "question": qa["question"], "context": paragraph["context"],
                              "answers": [a["text"] for a in qa["answers"]]})
    cases = select(cases, config["jsquad_examples"], config["pilot_seed"])
    path = output / "jsquad.json"
    stage = json.loads(path.read_text()) if path.exists() else {"binding": binding, "rows": []}
    if stage["binding"] != binding:
        raise ValueError("JSQuAD binding differs")
    completed = {row["id"] for row in stage["rows"]}
    for case in cases:
        if case["id"] in completed: continue
        if time.monotonic() > deadline: break
        prefix = f"文章：{case['context']}\n質問：{case['question']}\n答え：\n"
        if len(scorer.tokenizer.encode(prefix))+1+64 > scorer.maximum:
            row = {**case, "excluded": "full context plus generation budget exceeds 1024; not truncated"}
        else:
            answer = scorer.score([(prefix, case["answers"][0])])[0]
            generated = scorer.generate(prefix, 64)
            # First line or sentence as a short answer; raw continuation retained.
            prediction = generated["text"].split("\n")[0].split("。")[0]
            row = {**case, "excluded": None, "answer_log_likelihood": answer["log_likelihood"],
                   "answer_target_tokens": answer["target_tokens"], "generation": generated,
                   "prediction": prediction, **answer_metrics(prediction, case["answers"])}
        stage["rows"].append(row)
        save(path, stage)
    rows = stage["rows"]
    valid = [r for r in rows if not r["excluded"]]
    result = {"selected": len(cases), "attempted": len(rows), "excluded_context": len(rows)-len(valid), "scored": len(valid),
              "complete": len(rows) == len(cases), "normalized_em": clustered_ci(valid, "normalized_em"),
              "character_f1": clustered_ci(valid, "character_f1"),
              "official_score_reproduction": False, "score_note": "custom Japanese character F1 and punctuation-normalized EM; dev100 subset"}
    save(path, {**stage, "summary": result})
    return result, paragraphs


def evaluate_domains(scorer, paragraphs, output, binding, deadline):
    path = output / "external-body.json"
    stage = json.loads(path.read_text()) if path.exists() else {"binding": binding, "rows": []}
    if stage["binding"] != binding: raise ValueError("Domain binding differs")
    unique = {}
    for paragraph in paragraphs:
        sha = hashlib.sha256(paragraph["text"].encode()).hexdigest()
        unique.setdefault(sha, paragraph)
    selected, used_bytes = [], 0
    for sha, paragraph in list(unique.items())[:100]:
        size = len(paragraph["text"].encode())
        if used_bytes + size > 1000000: break
        selected.append((sha, paragraph, size))
        used_bytes += size
    for sha, paragraph, size in selected[len(stage["rows"]):]:
        if time.monotonic() > deadline: break
        ll = scorer.loglikelihood_rolling([(paragraph["text"],)])[0][0]
        stage["rows"].append({"doc_id": sha, "title": paragraph["title"], "body_bytes": size, "body_nll": -ll})
        save(path, stage)
    size = sum(r["body_bytes"] for r in stage["rows"])
    result = {"complete": len(stage["rows"]) == len(selected), "count": len(stage["rows"]), "bytes": size,
              "bpb": sum(r["body_nll"] for r in stage["rows"])/(math.log(2)*size) if size else None,
              "domain": "JSQuAD Wikipedia expository contexts; 100 unique paragraphs, not task answers",
              "contamination": "unknown; Wikipedia may overlap training; no claim of held-out source"}
    save(path, {**stage, "summary": result})
    return result


def evaluate_long(scorer, config, output, binding, deadline):
    path = output / "long-generation.json"
    stage = json.loads(path.read_text()) if path.exists() else {"binding": binding, "rows": []}
    if stage["binding"] != binding: raise ValueError("Generation binding differs")
    counts, cases = Counter(), []
    for case in load_records("eval/base.jsonl"):
        if case["split"] == "dev" and counts[case["category"]] < 2:
            cases.append(case)
            counts[case["category"]] += 1
    requests = [(case, maximum) for maximum in config["long_generation"]["max_new_tokens"] for case in cases]
    for case, maximum in requests[len(stage["rows"]):]:
        if time.monotonic() > deadline: break
        row = {"id": case["id"], "category": case["category"], **scorer.generate(case["prefix"], maximum)}
        row["metrics"] = repetition_metrics(row)
        # Appropriate ending is content-reviewed separately, not inferred from EOS.
        row["content_scores"] = None
        stage["rows"].append(row)
        save(path, stage)
    summary = {}
    for maximum in config["long_generation"]["max_new_tokens"]:
        rows = [r for r in stage["rows"] if r["max_new_tokens"] == maximum]
        summary[str(maximum)] = {"count": len(rows), "expected": len(cases),
                                "natural_eos": sum(r["metrics"]["natural_eos"] for r in rows),
                                "mean_char4_repeat": float(np.mean([r["metrics"]["char_4gram_repeat"] for r in rows])) if rows else None,
                                "same_sentence_repeat": sum(r["metrics"]["same_sentence_reappears"] for r in rows),
                                "raw_utf8_failure": sum(r["metrics"]["raw_utf8_failure"] for r in rows)}
    save(path, {**stage, "summary": summary, "complete": len(stage["rows"]) == len(requests)})
    return {"complete": len(stage["rows"]) == len(requests), "conditions": summary}


def main():
    global ACTIVE_JOB
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path("configs/evaluation/japanese_base_v2.json"))
    parser.add_argument("--pilot", action="store_true")
    parser.add_argument("--tasks", nargs="+", help="Explicit choice-task subset, e.g. semantics; generation requires full default run")
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    output = Path(config["output"]) / ("pilot" if args.pilot else "full")
    output.mkdir(parents=True, exist_ok=True)
    for key in ("checkpoint", "tokenizer"):
        if digest(config[key]) != config[key + "_sha256"]: raise ValueError(key + " hash differs")
    sources = {str(args.config): digest(args.config), "data_manifest": digest(Path(config["data"]) / "manifest.json")}
    for path in ("scripts/evaluate_japanese_base.py", "scripts/prepare_japanese_evaluation.py", "src/jmicro/japanese_evaluation.py",
                 "src/jmicro/model.py", "src/jmicro/tokenizer.py", "src/jmicro/training.py", "uv.lock"):
        sources[path] = digest(path)
    sources[config.get("semantic_suite", "eval/japanese_semantics_v2.jsonl")] = digest(config.get("semantic_suite", "eval/japanese_semantics_v2.jsonl"))
    binding = hashlib.sha256(json.dumps(sources, sort_keys=True).encode()).hexdigest()
    for name, expected in sources.items():
        source_path = Path(config["data"]) / "manifest.json" if name == "data_manifest" else Path(name)
        destination = output / "source" / ("data-manifest.json" if name == "data_manifest" else name)
        destination.parent.mkdir(parents=True, exist_ok=True)
        payload = source_path.read_bytes()
        if hashlib.sha256(payload).hexdigest() != expected: raise ValueError("Source changed during startup")
        if destination.exists() and destination.read_bytes() != payload: raise ValueError("Existing source snapshot differs")
        destination.write_bytes(payload)
    # Two million existing train token IDs, read once; no corpus re-tokenization.
    train = np.fromfile(config["unigram_train"], dtype="<u2", count=config["unigram_tokens"])
    counts = np.bincount(train[train >= 8], minlength=4096).astype(float)
    counts[:8] = 0
    counts[8:] += config["unigram_smoothing"]
    unigram = np.log(np.maximum(counts, 1e-300) / counts.sum())
    save(output / "unigram.json", {"train_bin": config["unigram_train"], "sample_ids_sha256": hashlib.sha256(train.tobytes()).hexdigest(),
                                  "sample_ids": len(train), "body_ids": int((train >= 8).sum()), "counts": counts.tolist(),
                                  "smoothing": config["unigram_smoothing"], "sampling": "first pinned train shard token IDs"})
    tasks, controls = build_tasks(config, args.pilot)
    if args.tasks:
        unknown = set(args.tasks) - set(tasks)
        if unknown: raise ValueError(f"Unknown task(s): {sorted(unknown)}")
        tasks = {name: rows for name, rows in tasks.items() if name in args.tasks}
    identity = {"pid": os.getpid(), "boot_id": Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
                "start_ticks": Path(f"/proc/{os.getpid()}/stat").read_text().split()[21]}
    budget = config["gpu_pilot_budget_seconds" if args.pilot else "gpu_full_budget_seconds"]
    job = {"status": "starting", **identity, "binding": binding, "source_sha256": sources, "budget_seconds": budget,
           "checkpoint": config["checkpoint"], "additional_training_tokens": 0, "protected_test_used": False}
    ACTIVE_JOB = output / "job.json"
    save(ACTIVE_JOB, job)
    with gpu_lock("cuda"), sdpa_kernel(SDPBackend.MATH):
        start = time.monotonic()
        deadline = start + budget
        torch.set_num_threads(2)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.manual_seed(42)
        saved = torch.load(config["checkpoint"], map_location="cpu", weights_only=False)
        model = JMicroModel(saved["model_config"]).to("cuda").eval()
        model.load_state_dict(saved["model"], strict=True)
        if saved["tokens"] != 10000007168 or saved["update"] != 305176: raise ValueError("Wrong checkpoint counters")
        tok = Tokenizer(config["tokenizer"])
        scorer = NativeLikelihood(model, tok, batch=config["batch"])
        job.update(status="running", checkpoint_tokens=saved["tokens"], checkpoint_update=saved["update"])
        save(output / "job.json", job)
        # Actual saved-weight validation: batched padding vs unpadded and direct manual target gather.
        examples = [("日本語の文章。\n", "今日は晴れた。"), ("\n", "猫。")]
        batch = scorer.score(examples)
        singles = [scorer.score([example])[0] for example in examples]
        deltas = [abs(a["log_likelihood"]-b["log_likelihood"]) for a, b in zip(batch, singles)]
        for example, scored in zip(examples, batch):
            encoded = encode_request(tok, *example)
            with torch.no_grad(), torch.autocast("cuda", dtype=torch.bfloat16):
                logits = model(torch.tensor([encoded["ids"][:-1]], device="cuda")).logits[0]
            positions = range(encoded["context_tokens"]-1, len(encoded["ids"])-1)
            manual = -sum(float(torch.log_softmax(logits[p].float(), -1)[encoded["ids"][p+1]]) for p in positions)
            if abs(manual + scored["log_likelihood"]) > .15: raise ValueError("GPU manual mask/shift disagrees")
        if max(deltas) > .15: raise ValueError("BF16 padded/unpadded likelihood differs excessively")
        save(output / "scorer-validation.json", {"finite": True, "padded_vs_single_absolute_nll": deltas,
              "maximum_allowed_absolute_nll": .15, "manual_target_gather_passed": True,
              "checkpoint_sha256": config["checkpoint_sha256"], "target_rows": batch})
        results = {}
        for name, cases in tasks.items():
            task_start = time.monotonic()
            print("START", name, len(cases), flush=True)
            results[name] = evaluate_choices(scorer, cases, controls[name], unigram, output / (name + ".json"), binding, deadline,
                                             slor=name == "jblimp")
            print("END", name, results[name]["count"], round(time.monotonic()-task_start, 3), flush=True)
            save(output / "result.json", {"tasks": results, "complete": False, "binding": binding})
        if not args.pilot and not args.tasks:
            results["jsquad"], paragraphs = evaluate_qa(scorer, config, output, binding, deadline)
            results["external_body"] = evaluate_domains(scorer, paragraphs, output, binding, deadline)
            results["long_generation"] = evaluate_long(scorer, config, output, binding, deadline)
        torch.cuda.synchronize()
        duration = time.monotonic()-start
        complete = all(result["complete"] for result in results.values())
        result = {"tasks": results, "complete": complete, "binding": binding, "source_sha256": sources,
                  "gpu_seconds": duration, "budget_seconds": budget, "forward_tokens": scorer.forward_tokens,
                  "checkpoint_sha256": config["checkpoint_sha256"], "parameters": sum(p.numel() for p in model.parameters()),
                  "additional_training_tokens": 0, "protected_test_used": False,
                  "human_blind_scores": "not performed", "v1_quality_criteria_unchanged": True}
        save(output / "result.json", result)
        save(output / "job.json", {**job, "status": "complete" if complete else "budget_incomplete", "gpu_seconds": duration})
        print("COMPLETE", complete, "GPU seconds", duration, flush=True)


if __name__ == "__main__":
    try:
        main()
    except BaseException as error:
        if ACTIVE_JOB is not None and ACTIVE_JOB.exists():
            job = json.loads(ACTIVE_JOB.read_text())
            save(ACTIVE_JOB, {**job, "status": "failed", "error_type": type(error).__name__, "error": str(error)})
        raise
