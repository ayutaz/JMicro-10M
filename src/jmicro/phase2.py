"""Train and verify the two pilot tokenizers on the frozen Phase 1 sample."""
from collections import defaultdict
from pathlib import Path
import argparse
import importlib.metadata
import json
import shutil
import time
import numpy as np

import sentencepiece as spm
from sentencepiece import sentencepiece_model_pb2

from jmicro.evaluation import canonicalize_text
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer, training_spans, CODEC_VERSION


def golden_cases():
    cases = read_json(ROOT / "eval/tokenizer_golden.json")["cases"]
    return cases + [{"id": "literal-marker", "input": "▁▁ a▁b", "canonical": "▁▁ a▁b"},
                    {"id": "all-special-spellings", "input": " ".join(x["piece"] for x in
                     read_json(ROOT / "configs/tokenizer/contract.json")["special_tokens"]),
                     "canonical": " ".join(x["piece"] for x in read_json(ROOT / "configs/tokenizer/contract.json")["special_tokens"])},
                    {"id": "whitespace", "input": " \t\n\v\f\u0085\u00a0\u2028\u2029\u3000 ",
                     "canonical": " \t\n\v\f\u0085\u00a0\u2028\u2029\u3000 "}]


def check_tokenizer(tok):
    result = []
    clone = Tokenizer(tok.path)
    for case in golden_cases():
        ids = tok.encode(case["input"])
        assert tok.decode(ids) == case["canonical"], case["id"]
        assert ids == clone.encode(case["input"])
        result.append({"id": case["id"], "ids": ids, "roundtrip": True})
    assert tok.decode_bytes(tok.byte_ids) == bytes(range(256))
    for text in ["\ud800", "\udfff"]:
        try:
            tok.encode(text)
        except UnicodeEncodeError:
            pass
        else:
            raise AssertionError("Lone surrogate accepted")
    try:
        canonicalize_text(b"\xff")
    except TypeError:
        pass
    else:
        raise AssertionError("Undecoded bytes accepted")
    try:
        tok.decode([tok.byte_ids[255]])
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError("Invalid generated UTF-8 not detected")
    normal = [tok.sp.id_to_piece(i) for i in range(tok.vocab_size) if i >= 8 and not tok.sp.is_byte(i)]
    return {"vocab_size": tok.vocab_size, "special_ids": list(range(8)),
            "piece_inventory": {"special":8,"byte":256,"normal_single_character":sum(len(p)==1 for p in normal),
                                "normal_multi_character":sum(len(p)>1 for p in normal)},
            "byte_pieces": 256, "all_byte_values_recovered": True,
            "invalid_input_rejected": True, "invalid_generated_utf8_detected": True,
            "golden": result, "reload_ids_equal": True}


def run():
    contract = read_json(ROOT / "configs/tokenizer/contract.json")
    sample = ROOT / "data/phase1/processed/tokenizer_sample.jsonl"
    assert sha256(sample) == "2bd5f104d0931e883a891f64bbcd0392cabd7259d3cfc5cd8a693f7f1acf54e6"
    rows = [json.loads(line) for line in sample.read_text().splitlines()]
    assert all(row["split"] == "train" for row in rows)
    spans = [span for row in rows for span in training_spans(canonicalize_text(row["text"])) if span.strip()]
    report_dir = ROOT / "reports/phase2"
    candidates, contracts = [], {}
    for size in contract["vocab_sizes"]:
        successes = []
        for coverage in contract["character_coverage_candidates"]:
            directory = ROOT / f"artifacts/phase2/candidates/{size}/{coverage}"
            directory.mkdir(parents=True, exist_ok=True)
            prefix = directory / "tokenizer"
            started = time.monotonic()
            options = dict(model_prefix=str(prefix), vocab_size=size, model_type="unigram",
                byte_fallback=True, character_coverage=coverage, normalization_rule_name="identity",
                add_dummy_prefix=False, remove_extra_whitespaces=False, pad_id=0, unk_id=1,
                bos_id=2, eos_id=3, pad_piece="<|pad|>", unk_piece="<|unk|>", bos_piece="<|bos|>",
                eos_piece="<|eos|>", control_symbols=[x["piece"] for x in contract["special_tokens"][4:]],
                num_threads=1, shuffle_input_sentence=False, input_sentence_size=0,
                max_sentence_length=max(len(s.encode()) for s in spans) + 1,
                hard_vocab_limit=True, minloglevel=1)
            entry = {"vocab_size": size, "coverage": coverage, "options": options}
            try:
                spm.SentencePieceTrainer.train(sentence_iterator=iter(spans), **options)
                tok = Tokenizer(prefix.with_suffix(".model"))
                assert tok.vocab_size == size
                checks = check_tokenizer(tok)
                for row in rows:
                    assert tok.decode(tok.encode(row["text"])) == canonicalize_text(row["text"])
                entry.update(status="passed", model_sha256=sha256(tok.path), sample_roundtrips=len(rows))
                successes.append((coverage, directory, checks))
            except RuntimeError as error:
                entry.update(status="training_failed", error=str(error))
            entry["elapsed_seconds"] = time.monotonic() - started
            candidates.append(entry)
            write_json(report_dir / "tokenizer_training_candidates.json", candidates)
        if not successes:
            raise RuntimeError(f"No valid tokenizer at {size}")
        # Highest passing coverage; both vocabulary sizes remain research candidates.
        coverage, source, checks = successes[0]
        chosen = ROOT / f"artifacts/phase2/{size}"
        chosen.mkdir(parents=True, exist_ok=True)
        for name in ("tokenizer.model", "tokenizer.vocab"):
            shutil.copyfile(source / name, chosen / name)
        tok = Tokenizer(chosen / "tokenizer.model")
        tok.save_wrapper(chosen)
        write_json(chosen / "special_tokens.json", contract["special_tokens"])
        metadata = {"created_at": now(), "sample": str(sample.relative_to(ROOT)),
                    "sample_sha256": sha256(sample), "sample_documents": len(rows),
                    "sample_canonical_bytes": sum(len(canonicalize_text(r["text"]).encode()) for r in rows),
                    "training_view": CODEC_VERSION, "training_spans": len(spans),
                    "selected_coverage": coverage, "sentencepiece": importlib.metadata.version("sentencepiece"),
                    "model_sha256": sha256(tok.path), "lock_sha256": sha256(ROOT / "uv.lock"),
                    "retraining_reproducibility": "single CPU thread, fixed input order; no cross-version/platform guarantee"}
        # Retrain chosen candidate on the same machine and compare exact serialized model.
        options = next(x["options"] for x in candidates if x["vocab_size"] == size and x["coverage"] == coverage).copy()
        options["model_prefix"] = str(chosen / "retrained")
        spm.SentencePieceTrainer.train(sentence_iterator=iter(spans), **options)
        first = sentencepiece_model_pb2.ModelProto.FromString(tok.path.read_bytes())
        second = sentencepiece_model_pb2.ModelProto.FromString((chosen / "retrained.model").read_bytes())
        # model_prefix is recorded in trainer_spec; compare model computation rather than output filename.
        first.trainer_spec.model_prefix = second.trainer_spec.model_prefix = ""
        metadata["same_machine_retrained_model_equal_excluding_output_prefix"] = first.SerializeToString() == second.SerializeToString()
        assert metadata["same_machine_retrained_model_equal_excluding_output_prefix"]
        write_json(chosen / "training_metadata.json", metadata)
        contracts[str(size)] = {**checks, **metadata}
        write_json(report_dir / "tokenizer_contract_report.json", {"status": "passed", "tokenizers": contracts})

    measure(contract, report_dir)
    print(json.dumps({"status": "passed", "reports": str(report_dir), "candidates": len(candidates)}))


def measure(contract, report_dir):
    comparisons = {}
    for size in contract["vocab_sizes"]:
        tok = Tokenizer(ROOT / f"artifacts/phase2/{size}/tokenizer.model")
        assert sha256(tok.path) == read_json(tok.path.parent / "training_metadata.json")["model_sha256"]
        totals = defaultdict(lambda: defaultdict(int))
        lengths, compression = defaultdict(list), defaultdict(list)
        with (ROOT / "data/phase1/processed/corpus.jsonl").open() as file:
            for line in file:
                row = json.loads(line)
                text = canonicalize_text(row["text"])
                ids = tok.encode(text)
                assert tok.decode(ids) == text
                stats = totals[row["bucket"]]
                stats["documents"] += 1
                stats["chars"] += len(text)
                stats["bytes"] += len(text.encode())
                stats["tokens"] += len(ids)
                compression[row["bucket"]].append(len(text)/len(ids))
                fallback_bytes = sum(i in tok.id_bytes for i in ids)
                stats["fallback_tokens"] += fallback_bytes
                # Number of original Unicode characters represented by byte tokens.
                run = bytearray()
                for i in [*ids, 2]:
                    if i in tok.id_bytes:
                        run.extend(tok.id_bytes[i])
                    elif run:
                        stats["fallback_characters"] += len(run.decode("utf-8"))
                        run.clear()
                messages = json.loads(row["messages_json"]) if row["messages_json"] else []
                if messages:
                    dialogue_ids, labels = tok.dialogue(messages)
                    stats["dialogue_total_tokens"] += len(dialogue_ids)
                    stats["assistant_teacher_tokens"] += sum(x != -100 for x in labels[1:])
                    stats["context_1024_fit"] += len(dialogue_ids) <= 1024
                    lengths[row["bucket"]].append(len(dialogue_ids))
                    windows = list(tok.sft_windows(messages))
                    stats["sft_windows"] += len(windows)
                    stats["sft_window_tokens"] += sum(len(w["input_ids"]) for w in windows)
                    taught = sum(w["target_tokens"] for w in windows)
                    assert taught == sum(x != -100 for x in labels[1:])
                    stats["sft_window_teacher_tokens"] += taught
                else:
                    stats["context_1024_fit"] += len(ids) + 2 <= 1024
                    lengths[row["bucket"]].append(len(ids)+2)
        for bucket, stats in totals.items():
            stats["chars_per_token"] = stats["chars"] / stats["tokens"]
            stats["bytes_per_token"] = stats["bytes"] / stats["tokens"]
            stats["fallback_token_rate"] = stats["fallback_tokens"] / stats["tokens"]
            stats["fallback_character_rate"] = stats["fallback_characters"] / stats["chars"]
            stats["context_1024_fit_rate"] = stats["context_1024_fit"] / stats["documents"]
            stats["tokens_per_document_with_structure"] = {"mean":float(np.mean(lengths[bucket])),
                   "p50":float(np.percentile(lengths[bucket],50)),"p95":float(np.percentile(lengths[bucket],95)),
                   "max":max(lengths[bucket])}
            stats["document_chars_per_token"] = {"mean":float(np.mean(compression[bucket])),
                                                   "p95":float(np.percentile(compression[bucket],95))}
        comparisons[str(size)] = dict(totals)
        write_json(report_dir / "tokenizer_comparison.json", {"status": "passed", "tokenizers": comparisons,
                   "candidate_selection": "Both passed; BPB and model quality deferred to GPU experiments"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--measure-only", action="store_true", help="Measure existing selected models without retraining")
    args = parser.parse_args()
    if args.measure_only:
        measure(read_json(ROOT / "configs/tokenizer/contract.json"), ROOT / "reports/phase2")
    else:
        run()
