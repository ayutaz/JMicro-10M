"""Bounded byte-uniform supply estimate from previously verified pinned train.

This is not dataset preparation or a distinct-document/overlap audit. Sampling
the containing JSONL record by byte gives probability proportional to its byte
length; tokens/record-bytes, averaged over draws, estimates total token yield.
"""
import argparse
from collections import Counter
import hashlib
import json
import multiprocessing as mp
from pathlib import Path
import random
import shutil
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from huggingface_hub import try_to_load_from_cache
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.expanded_stories import translated_candidate
from jmicro.nested_material import whole_material
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity, alive

DATA = Path("/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005")
TOK = None
HANDLES = {}


def containing_line(stream, offset, size, window=65536):
    """Include the newline in the record's byte measure; never skip forward."""
    assert 0 <= offset < size and window > 0
    left = max(0, offset-window); right = min(size, offset+window+1)
    stream.seek(left); block = stream.read(right-left); local = offset-left
    start = block.rfind(b"\n", 0, local)+1
    end = block.find(b"\n", local)
    if start == 0 and left != 0 or end < 0 and right != size:
        raise ValueError("Sampled record exceeds the bounded containing-line window")
    end = end+1 if end >= 0 else len(block)
    return block[start:end], left+start


def initialize(tokenizer):
    global TOK
    TOK = Tokenizer(tokenizer)


def inspect(task):
    file_index, path, size, offset = task
    if path not in HANDLES: HANDLES[path] = Path(path).open("rb")
    line, position = containing_line(HANDLES[path], offset, size)
    row = json.loads(line)
    assert isinstance(row["text_ja"], str) and hashlib.sha256(row["text_en"].encode()).hexdigest() == row["text_hash"]
    candidate = translated_candidate(row["text_ja"], TOK)
    unit = whole_material(candidate["text"], len(candidate["ids"]), "story") if candidate else None
    train = bool(unit and unit["split"] == "train" and int(row["text_hash"][:8], 16)%100 != 0)
    tokens = len(candidate["ids"])+2 if train else 0
    return dict(file_index=file_index, sampled_byte=offset, record_byte_offset=position, record_bytes=len(line),
        family=row["text_hash"], translated_selector_accepted=bool(candidate), nested_train_accepted=train,
        body_tokens=len(candidate["ids"]) if candidate else None, accepted_tokens=tokens,
        tokens_per_record_byte=tokens/len(line), sample_text=candidate["text"] if train else None)


def estimate(rows, files, seed):
    rng = np.random.default_rng(seed)
    estimates = {}; bootstrap = np.zeros(2000)
    for index, item in enumerate(files):
        selected = [r for r in rows if r["file_index"] == index]
        assert selected
        rates = np.asarray([r["tokens_per_record_byte"] for r in selected])
        estimates[item["path"]] = dict(draws=len(selected), accepted_draws=sum(r["nested_train_accepted"] for r in selected),
            estimated_eligible_tokens=float(rates.mean()*item["bytes"]))
        bootstrap += rates[rng.integers(0, len(rates), (2000, len(rates)))].mean(1)*item["bytes"]
    return dict(files=estimates, estimated_eligible_tokens=sum(r["estimated_eligible_tokens"] for r in estimates.values()),
        bootstrap_ci95=np.quantile(bootstrap, [.025, .975]).tolist(), bootstrap_repetitions=2000,
        note="Monte Carlo uncertainty for byte-uniform draws in fixed files; includes possible duplicate/reused records, not distinct supply or independent family quality")


def run(args):
    assert sys.version_info[:3] == (3,12,7)
    assert 100 <= args.samples_per_file <= 2000 and 1 <= args.workers <= 12 and 0 < args.budget_seconds <= 600
    output = args.output.resolve(); assert output.is_relative_to(ROOT/"reports/phase6")
    source = read_json(DATA/"supply.json")["sources"]["shibatch/TinyStories-JA"]
    previous = read_json(DATA/"prepare-job.json")
    assert previous["status"] == "complete" and not alive(previous)
    assert previous["binding"]["source"] == {k:v for k,v in source.items() if k != "declared_notes"}
    assert source["license"] == "cdla-sharing-1.0" and len(source["files"]) == 4
    tok = ROOT/"artifacts/phase2/4096/tokenizer.model"
    assert sha256(tok) == read_json(ROOT/"configs/phase6/amount_learning_comparison.json")["tokenizer_sha256"]
    paths = []
    for item in source["files"]:
        path = try_to_load_from_cache(source["repository"], item["path"], revision=source["revision"], repo_type="dataset")
        if not isinstance(path, str): raise FileNotFoundError("Previously verified pinned train cache is required; no automatic download")
        path = Path(path).resolve()
        # Cache blob keys are not necessarily content SHA256. Reuse the
        # completed preparation's actual full-content verification and the
        # same pinned cache mapping/size, rather than rescan all5.37GB.
        assert path.stat().st_size == item["bytes"]
        paths.append(str(path))
    scripts = ("scripts/probe_larger_story_supply.py", "src/jmicro/expanded_stories.py", "src/jmicro/nested_material.py",
        "src/jmicro/complete_units.py", "src/jmicro/coherent_units.py", "src/jmicro/evaluation.py", "src/jmicro/tokenizer.py")
    binding = dict(repository=source["repository"], revision=source["revision"], source_files=source["files"],
        previous_completed_prepare_job_sha256=sha256(DATA/"prepare-job.json"), tokenizer_sha256=sha256(tok),
        reused_cached_train_paths=paths,
        source_sha256={p:sha256(ROOT/p) for p in scripts}, samples_per_file=args.samples_per_file,
        workers=args.workers, seed=args.seed, CPU_budget_seconds=args.budget_seconds,
        verification="Reuse completed full-content source hashes; same pinned revision/cache mapping/size and sampled original English hashes; cache keys are not content digests; no repeated full-file hash scans",
        scope="Cached official train only; translated and unchanged whole-story filters; no new shards/GPU/test")
    output.mkdir(parents=True, exist_ok=True); job_path = output/"job.json"
    if job_path.exists():
        old = read_json(job_path)
        assert old["binding"] == binding and not alive(old)
        if old["status"] == "complete": print("Completed supply estimate retained; no new preparation"); return
        raise RuntimeError("Preserve failed probe; inspect its evidence before changing the attempt")
    start = time.monotonic(); job = dict(status="running", **identity(), binding=binding, started_at=now())
    rng = random.Random(args.seed); rows = []; examples = []; seen_examples = set(); example_counts = Counter()
    tasks = [(i, paths[i], item["bytes"], rng.randrange(item["bytes"]))
        for i, item in enumerate(source["files"]) for _ in range(args.samples_per_file)]
    def heartbeat():
        if time.monotonic()-start > args.budget_seconds: raise TimeoutError("Bounded cached supply probe exceeded CPU budget")
        job.update(heartbeat_at=now(), completed_draws=len(rows), total_draws=len(tasks), CPU_seconds=time.monotonic()-start)
        atomic_json(job_path, job)
    try:
        heartbeat()
        for p in scripts:
            target = output/"source"/p; target.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(ROOT/p, target)
        atomic_json(output/"recipe.json", binding)
        with mp.get_context("fork").Pool(args.workers, initializer=initialize, initargs=(str(tok),)) as pool:
            for row in pool.imap(inspect, tasks, chunksize=16):
                text = row.pop("sample_text"); rows.append(row)
                if text and row["family"] not in seen_examples and example_counts[row["file_index"]] < 8:
                    seen_examples.add(row["family"]); examples.append(dict(row, text=text)); example_counts[row["file_index"]] += 1
                if len(rows)%128 == 0: heartbeat()
        heartbeat(); summary = estimate(rows, source["files"], args.seed)
        atomic_json(output/"draws.json", dict(binding=binding, rows=rows))
        atomic_json(output/"sample32.json", dict(binding=binding, examples=examples, selection="First8 distinct accepted families per source file in frozen byte-uniform order; unreviewed"))
        retained = read_json(Path(previous["binding"]["original_pool"]["pool"])/"manifest.json")["splits"]["train"]["tokens"]
        result = dict(status="bounded_supply_estimate_complete_not_prepared_or_distinct", binding=binding,
            **summary, retained_prepared_tokens=retained,
            estimated_total_with_retained=summary["estimated_eligible_tokens"]+retained,
            target_story_tokens_for2B=400000000,
            estimated_upper_with_retained_below400M=summary["bootstrap_ci95"][1]+retained < 400000000,
            duplicate_draws=len(rows)-len({(r["file_index"],r["record_byte_offset"]) for r in rows}),
            counts=dict(Counter("accepted_train" if r["nested_train_accepted"] else "rejected" for r in rows)),
            unmeasured=["exact remaining unprocessed records", "whole-source unique/family overlap", "source quality outside sample", "exact selected capacity after all exclusions"],
            existing200M_source_is_subset_not_additive=True, new_acquired_bytes=0, new_prepared_tokens=0, GPU_teacher_tokens=0,
            independent_human_blind=False, protected_test_used=False, Base_adopted=False, requested_five_steps_complete=False,
            CPU_seconds=time.monotonic()-start, completed_at=now())
        atomic_json(output/"result.json", result)
        heartbeat(); job.update(status="complete", completed_at=now()); print(json.dumps({k:v for k,v in result.items() if k != "binding"}), flush=True)
    except BaseException as error: job.update(status="failed", error=repr(error)); raise
    finally: job["CPU_seconds"] = time.monotonic()-start; atomic_json(job_path, job)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples-per-file", type=int, default=600)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--budget-seconds", type=float, default=600)
    parser.add_argument("--seed", type=int, default=20261006)
    run(parser.parse_args())
