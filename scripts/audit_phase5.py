"""Audit finished Phase 5 artifacts independently and export compact evidence.

Run through uv in the WSL checkout. This command never trains or evaluates test.
"""
import argparse
from collections import Counter, defaultdict
import json
import math
from pathlib import Path
import sys

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.phase5 import bootstrap_bpb, equal_state
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes


def require(condition, message):
    if not condition:
        raise ValueError(message)


def audit_body(body, expected):
    rows = body["rows"]
    require(body["split"] == "dev", "Held-out evaluation must use dev")
    require(len(rows) == body["documents"] == len(expected), "Document count differs")
    require([(r["doc_id"], r["body_bytes"]) for r in rows] == expected, "Population differs")
    require(all(r["scored"] == r["body_tokens"] for r in rows), "Body not scored exactly once")
    require(body["body_bytes"] == sum(r["body_bytes"] for r in rows), "Byte sum differs")
    require(math.isclose(body["body_nll"], sum(r["body_nll"] for r in rows), rel_tol=1e-12), "NLL sum differs")
    require(math.isclose(body["bpb"], body["body_nll"] / (math.log(2) * body["body_bytes"]), rel_tol=1e-12), "BPB differs")
    require(all(math.isfinite(r["body_nll"]) and math.isfinite(r["eos_nll"]) for r in rows), "Nonfinite evaluation")


def generation_summary(generation, cases):
    expected = Counter((c["id"], c["category"], suppressed, mode, seed)
        for c in cases for suppressed, mode, seed in
        [(True, "greedy", 42), (False, "greedy", 42),
         (True, "sampling", 42), (True, "sampling", 43), (True, "sampling", 44)])
    outputs = generation["outputs"]
    actual = Counter((r["id"], r["category"], r["suppressed"], r["decoding"], r["seed"]) for r in outputs)
    require(actual == expected, "Fixed generation population/modes differ")
    require(generation["suite_sha256"] == sha256(ROOT / "eval/base.jsonl"), "Suite hash differs")
    require(generation["split"] == "dev" and all(r["split"] == "dev" for r in outputs), "Test generation detected")
    require(generation["max_new_tokens"] == 64 and generation["temperature"] == .8 and generation["top_p"] == .9,
            "Generation settings differ")
    grouped = defaultdict(list)
    for row in outputs:
        ids = row["generated_ids"]
        require(0 < len(ids) <= 64, "Invalid generation token count")
        require((row["stop_reason"] == "stop_id") == (ids[-1] == 3), "Stop reason differs from token IDs")
        require(not (3 in ids[:-1]), "Generation continued after EOS")
        key = f'{row["decoding"]}/suppressed={row["suppressed"]}'
        grouped[key].append(row)
        grouped[f'{key}/category={row["category"]}'].append(row)
    result = {}
    for key, rows in sorted(grouped.items()):
        result[key] = dict(cases=len(rows), eos=sum(r["stop_reason"] == "stop_id" for r in rows),
            unicode_failure=sum(not r["valid_utf8"] for r in rows),
            repetition=sum(r["repetition"] for r in rows), role_leak=sum(r["role_leak"] for r in rows),
            empty=sum(r["empty_response"] for r in rows),
            median_characters=float(np.median([len(r["text"]) for r in rows])))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run, output = args.run.resolve(), args.output.resolve()
    job, plan = read_json(run / "job.json"), read_json(run / "plan.json")
    require(job["status"] == "complete", "Supervisor has not completed")
    require(sha256(run / "plan.json") == job["plan_sha256"], "Frozen plan hash differs")
    require(job["implementation_sha256"] == implementation_hashes(), "Runtime source differs")
    require(not plan["selection"]["test_usage"] and not plan["selection"]["phase6_authorized"], "Scope differs")
    comparison = read_json(run / "tokenizer_model_comparison.json")
    require(comparison["status"] == "passed" and not comparison["test_used"], "Comparison not passed")
    suite = [json.loads(line) for line in (ROOT / "eval/base.jsonl").read_text().splitlines()]
    cases = [c for c in suite if c["split"] == "dev"]
    require(len(cases) == 80, "Expected 80 fixed dev cases")
    shards = {name: Shard(Path.home() / f"jmicro-data/shards/{name}-pilot", "dev") for name in ("t8k", "t4k")}
    populations = {name: [(r["doc_id"], r["bytes"]) for r in shard.index] for name, shard in shards.items()}
    require(populations["t8k"] == populations["t4k"], "Tokenizer dev populations differ")
    require(len(populations["t8k"]) == 924 and sum(b for _, b in populations["t8k"]) == 1633458, "Pinned dev population differs")
    fallback = {}
    for name, shard in shards.items():
        train = Shard(shard.directory, "train")
        require(not set(r["doc_id"] for r in train.index) & set(r["doc_id"] for r in shard.index), "Train/dev overlap")
        tok = Tokenizer(ROOT / f'artifacts/phase2/{8192 if name == "t8k" else 4096}/tokenizer.model')
        count = sum(int(np.isin(shard.tokens[r["offset"]+1:r["offset"]+1+r["body_tokens"]], tok.byte_ids).sum()) for r in shard.index)
        total = sum(r["body_tokens"] for r in shard.index)
        fallback[name] = dict(split="dev", body_tokens=total, fallback_tokens=count, fallback_token_rate=count/total,
            note="Includes protected characters encoded by the explicit byte codec; token denominators differ between vocabularies.")
    resumes = {}
    fields = ("model", "optimizer", "scheduler", "rng", "sampler", "tokens", "supervised_tokens", "body_bytes", "token_digest", "implementation_sha256")
    for name in ("t8k", "t4k", "overfit", "no-qknorm"):
        directory = run / f"resume-{name}"
        recorded = read_json(directory / "resume_report.json")
        require(recorded["status"] == "passed_exact" and all(recorded["checks"].values()), "Resume report failed")
        for filename, digest in recorded["checkpoints"].items():
            require(sha256(directory / filename) == digest, "Resume checkpoint hash differs")
        a = torch.load(directory / "continuous.pt", map_location="cpu", weights_only=False)
        b = torch.load(directory / "resumed.pt", map_location="cpu", weights_only=False)
        resumes[name] = {key: equal_state(a[key], b[key]) for key in fields}
        require(all(resumes[name].values()) and a["update"] == b["update"] == 200, "Independent resume equality failed")
        del a, b
    overfit, smoke = read_json(run / "overfit_report.json"), read_json(run / "smoke_report.json")
    thresholds, train, recall = plan["overfit"], overfit["train"], overfit["continuation"]
    require(overfit["status"] == "passed" and all(overfit["gates"].values()), "Overfit gate failed")
    require(train["split"] == "train" and train["documents"] == recall["documents"] == 100, "Overfit population differs")
    require(train["nll_per_token"] <= thresholds["max_nll_per_token"] and train["teacher_forced_accuracy"] >= thresholds["min_teacher_accuracy"], "Overfit numerical gates fail")
    require(recall["exact_rate"] >= thresholds["min_continuation_exact_rate"] and min(train["eos_argmax_accuracy"], recall["eos_generation_rate"]) >= thresholds["min_eos_argmax_accuracy"], "Overfit generation gates fail")
    train_ids = {r["doc_id"] for r in train["rows"]}
    require(train_ids == {r["doc_id"] for r in recall["outputs"]} == {r["doc_id"] for r in recall["eos_outputs"]}, "Recall population differs")
    require(math.isclose(recall["exact_rate"], sum(r["expected_ids"] == r["generated_ids"] for r in recall["outputs"]) / 100), "Recall rate differs")
    names = ["100m-t8k", "100m-t4k", "100m-no-qknorm", "100m-lr001"]
    reports, compact = {}, {}
    for name in ["smoke", *names]:
        report = smoke if name == "smoke" else read_json(run / f"{name}.json")
        reports[name] = report
        model_name = "t8k" if report["model_config"]["vocab_size"] == 8192 else "t4k"
        audit_body(report["body"], populations[model_name])
        require(report["body"]["bpb"] < read_json(run / f"initial-{model_name}.json")["body"]["bpb"], "Dev BPB did not improve")
        directory = run / ("smoke-t8k" if name == "smoke" else name)
        metrics = [json.loads(line) for line in (directory / "metrics.jsonl").read_text().splitlines()]
        updates = plan["smoke_updates"] if name == "smoke" else plan["comparison_updates"]
        require([r["update"] for r in metrics] == list(range(1, updates+1)), "Metrics missing/duplicate updates")
        require(all(math.isfinite(r[k]) and r["seconds"] > 0 for r in metrics for k in ("loss", "gradient_norm", "seconds", "tokens_per_second")), "Nonfinite training metrics")
        require(np.mean([r["loss"] for r in metrics[-100:]]) < np.mean([r["loss"] for r in metrics[:100]]), "Training loss did not decrease")
        require(sha256(Path(report["checkpoint"])) == report["checkpoint_sha256"], "Checkpoint hash differs")
        state = torch.load(report["checkpoint"], map_location="cpu", weights_only=False)
        require(state["tokens"] == updates * plan["context"] * plan["batch"] * plan["accumulation"] == report["tokens_seen"], "Consumed token budget differs")
        require(state["update"] == updates and state["implementation_sha256"] == job["implementation_sha256"], "Checkpoint source/update differs")
        require(state["model_config"] == report["model_config"] and all(torch.isfinite(w).all() for w in state["model"].values()), "Checkpoint model differs/nonfinite")
        require(all(torch.isfinite(v).all() for item in state["optimizer"]["state"].values()
            for v in item.values() if isinstance(v, torch.Tensor)), "Nonfinite optimizer state")
        if name == "smoke":
            require((directory / "checkpoint-00000600.pt").exists() and "smoke-t8k-first-half" in job["completed_stages"], "Actual smoke pause missing")
        compact[name] = dict(body={k:v for k,v in report["body"].items() if k != "rows"},
            common_windows={k:v for k,v in report["common_windows"].items() if k != "rows"},
            generation=generation_summary(report["generation"], cases),
            checkpoint=report["checkpoint"], checkpoint_sha256=report["checkpoint_sha256"], spec=state["spec"],
            raw_report=str(run / ("smoke_report.json" if name == "smoke" else f"{name}.json")),
            raw_report_sha256=sha256(run / ("smoke_report.json" if name == "smoke" else f"{name}.json")))
        del state
    require(len({reports[n]["common_windows"]["text_manifest_sha256"] for n in names}) == 1, "Common-window hash differs")
    common_population = [(r["doc_id"], r["body_bytes"]) for r in reports["100m-t8k"]["common_windows"]["rows"]]
    require(len(common_population) == 32, "Expected 32 common windows")
    for name in names:
        audit_body(reports[name]["common_windows"], common_population)
    baseline_winner = min(("100m-t8k", "100m-t4k"), key=lambda n: reports[n]["body"]["bpb"])
    require(reports["100m-no-qknorm"]["model_config"]["vocab_size"] == reports[baseline_winner]["model_config"]["vocab_size"], "Norm ablation tokenizer differs")
    require(compact["100m-no-qknorm"]["spec"] == compact[baseline_winner]["spec"], "Norm ablation training factors differ")
    left = dict(reports[baseline_winner]["model_config"]); right = dict(reports["100m-no-qknorm"]["model_config"])
    for key in ("name", "status", "expected_parameter_count", "qk_norm_type"):
        left.pop(key, None); right.pop(key, None)
    require(left == right and reports["100m-no-qknorm"]["model_config"]["qk_norm_type"] == "none", "Norm ablation architecture factors differ")
    lr_baseline = "100m-no-qknorm" if reports["100m-no-qknorm"]["body"]["bpb"] < reports[baseline_winner]["body"]["bpb"] else baseline_winner
    require(reports["100m-lr001"]["model_config"] == reports[lr_baseline]["model_config"], "LR comparison architecture differs")
    low_spec = dict(compact["100m-lr001"]["spec"]); low_spec["lr"] = plan["lr"]
    require(low_spec == compact[lr_baseline]["spec"] and compact["100m-lr001"]["spec"]["lr"] == .001, "LR comparison factors differ")
    for key, recorded in comparison["paired_comparisons"].items():
        left_name, right_name = key.split("_vs_")
        require(bootstrap_bpb(reports[left_name]["body"], reports[right_name]["body"]) == recorded, "Paired comparison differs")
    for field in ("body_bytes", "training_seconds"):
        for name in ("t8k", "t4k"):
            report = read_json(run / f"budget-{field}-{name}.json")
            audit_body(report["body"], populations[name])
            point = comparison["auxiliary_budget_matches"][field]["points"][f"100m-{name}"]
            require(report["checkpoint"] == point["path"] and report["tokens_seen"] == point["tokens"], "Auxiliary budget checkpoint differs")
            require(report["common_windows"]["text_manifest_sha256"] == reports["100m-t8k"]["common_windows"]["text_manifest_sha256"], "Auxiliary windows differ")
    require(1 <= len(comparison["selected"]) <= 2 and len(set(comparison["selected"])) == len(comparison["selected"]), "Candidate count differs")
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "evaluation_summary.json", dict(status="passed", models=compact, tokenizer_dev_fallback=fallback))
    write_json(output / "candidate_configs.json", {n: comparison["entries"][n] for n in comparison["selected"]})
    write_json(output / "independent_audit.json", dict(status="passed", created_at=now(), run=str(run),
        supervisor=job, resume_state_equality=resumes, checks=["plan/source/hash binding", "exact resume all state",
            "overfit numerical and generated-ID gates", "smoke actual pause and improvement", "finite loss and checkpoint weights",
            "four equal 100M token budgets", "single-factor norm/LR comparisons", "full common dev byte population",
            "400 fixed dev generations per model", "paired intervals recomputed", "auxiliary budgets evaluated"],
        test_used=False, phase6_started=False, comparison_sha256=sha256(run / "tokenizer_model_comparison.json"),
        evaluation_summary_sha256=sha256(output / "evaluation_summary.json")))
    print(json.dumps(dict(status="passed", selected=comparison["selected"], output=str(output))))


if __name__ == "__main__":
    main()
