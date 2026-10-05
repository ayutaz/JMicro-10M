"""Pinned train-only textbook100M/400M component for a new2B mixture.

This is source material preparation, not accepted model training. The later
Web75/textbook20/story5 pools need a new fixed64 content review. Native source
provenance remains textbook, never original Web. No official dev/test download.
"""
from collections import Counter
import json
import multiprocessing as mp
import os
from pathlib import Path
import random
import shutil
import sys
import time
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "60")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download, try_to_load_from_cache
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.larger_material import FourGroups
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive, identity
from probe_textbook_supply import selected_units

DATA = Path("/home/aihub_ubuntu/jmicro-data/phase6/textbook-component-20261006")
RUN = ROOT/"reports/phase6/textbook-component-20261006"
SUPPLY = Path("/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005/supply.json")
SEED, BUDGET, WORKERS = 2026100631, 1800, 8
TARGET, DEV_TARGET = 100000000, 400000
FILES = ("scripts/prepare_textbook_component.py", "scripts/prepare_textbook_component.ps1",
    "scripts/probe_textbook_supply.py", "src/jmicro/larger_material_v3.py",
    "src/jmicro/larger_material.py", "src/jmicro/nested_material_v2.py",
    "src/jmicro/nested_material.py", "src/jmicro/complete_units.py",
    "src/jmicro/coherent_units.py", "src/jmicro/tokenizer.py")
_TOK = None


def worker_init(path):
    global _TOK
    _TOK = Tokenizer(path)


def worker(task):
    filename, rows = task
    result, native = [], 0
    for row_index, row in rows:
        units, size = selected_units(row, _TOK)
        native += size
        for unit in units:
            ids = unit.get("token_ids")
            if ids is None:
                ids = [2, *_TOK.encode(unit["text"]), 3]
            assert len(ids) == unit["body_tokens"]+2 and ids[0] == 2 and ids[-1] == 3
            assert all(i >= 8 for i in ids[1:-1])
            result.append(dict(unit, token_ids=ids, source_file=filename,
                source_row=row_index, source_revision="f928b35fde6732f7d981860d32a18ef451cd539e"))
    return result, len(rows), native


def tasks(path, filename):
    reader = pq.ParquetFile(path)
    offset = 0
    for batch in reader.iter_batches(batch_size=512,
            columns=["source_id", "url", "prompt_type", "rewrite"]):
        rows = batch.to_pylist()
        yield filename, list(enumerate(rows, offset))
        offset += len(rows)


def prepare():
    source = read_json(SUPPLY)["sources"]["KeisukeMiyamoto/SyntheticTextbook-jp"]
    assert source["revision"] == "f928b35fde6732f7d981860d32a18ef451cd539e"
    assert source["license"] == "apache-2.0" and sha256(Path(source["card_path"])) == source["card_sha256"]
    candidates = source["files"][:12]
    assert len(candidates) == 12 and [f["path"] for f in candidates] == [f"train-{i:05d}.parquet" for i in range(12)]
    previous = read_json(ROOT/"reports/phase6/textbook_supply_result.json")
    examples = ROOT/"reports/phase6/textbook_supply_sample32.json"
    inspected = read_json(examples)["examples"]
    excluded = {u["source_family"] for u in inspected}
    assert len(excluded) == 32
    tokenizer = ROOT/"artifacts/phase2/4096/tokenizer.model"
    assert sha256(tokenizer) == previous["binding"]["tokenizer_sha256"]
    binding = dict(repository=source["repository"], revision=source["revision"], license=source["license"],
        train_files_limit=candidates, official_validation_test_acquired=False,
        tokenizer_sha256=sha256(tokenizer), small_target_tokens=TARGET, large_ratio_exact=4,
        dev_target_tokens=DEV_TARGET, seed=SEED, CPU_budget_seconds=BUDGET, workers=WORKERS,
        source_sha256={p: sha256(ROOT/p) for p in FILES},
        inspected_family_exclusion_sha256=sha256(examples),
        planned_final_source_ratio=dict(web=.75, textbook=.20, story=.05),
        policy="Original whole or intact first32 paragraphs with inherited filters; same source_id family across grades/siblings; canonical exact exclusion and protected dev-prefix exclusion",
        limitations="Synthetic factual claims and cross-source/global near duplication unverified; final mixed fixed64 acceptance and three-source training accounting still required; no GPU")
    RUN.mkdir(parents=True, exist_ok=True)
    job_path = RUN/"job.json"
    if job_path.exists():
        old = read_json(job_path)
        assert old["binding"] == binding and not alive(old)
        if old["status"] == "complete":
            print("Completed textbook component retained", flush=True); return
        raise RuntimeError("Preserve failed preparation; inspect before any new version")
    DATA.mkdir(parents=True, exist_ok=True)
    assert not any(DATA.iterdir()), "Do not overwrite partial material"
    started = time.monotonic()
    job = dict(status="running", **identity(), binding=binding, started_at=now())
    counts, totals = Counter(), Counter()
    def heartbeat(stage):
        job.update(stage=stage, heartbeat_at=now(), seconds=time.monotonic()-started,
            counts=dict(counts), prepared_tokens=dict(totals))
        atomic_json(job_path, job)
        if job["seconds"] > BUDGET:
            raise TimeoutError("1800s CPU budget exhausted; partials are not ready")
    protected = []
    for suite in ("eval/base.jsonl", "eval/japanese_semantics_v2_1.jsonl"):
        for line in (ROOT/suite).read_text().splitlines():
            row = json.loads(line)
            if row.get("split", "dev") == "dev":
                protected.extend(row[k] for k in ("prefix", "context")
                    if isinstance(row.get(k), str) and len(row[k]) >= 12)
    handles, indexes = {}, {}
    offsets, documents, body_bytes = Counter(), Counter(), Counter()
    hist = {name: Counter() for name in ("small", "large", "dev")}
    rng, seen, groups = random.Random(SEED+1), set(), FourGroups(SEED)
    sample, draws, acquired = [], 0, []
    try:
        heartbeat("setup")
        write_json(RUN/"recipe.json", binding)
        for p in FILES:
            dest = RUN/"source"/p; dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/p, dest)
        for name in hist:
            folder = DATA/name; folder.mkdir()
            handles[name] = (folder/"train.partial.bin").open("wb")
            indexes[name] = (folder/"train.index.partial.jsonl").open("w")
        def append(name, unit):
            nonlocal draws
            ids = np.asarray(unit["token_ids"], dtype="<u2")
            record = {k: v for k, v in unit.items() if k not in ("text", "token_ids")}
            record.update(doc_id="textbook-"+unit["canonical_sha256"][:24], offset=offsets[name],
                split="dev" if name == "dev" else "train", bytes=len(unit["text"].encode()))
            handles[name].write(ids.tobytes())
            indexes[name].write(json.dumps(record, ensure_ascii=False)+"\n")
            offsets[name] += len(ids); totals[name] += len(ids)
            documents[name] += 1; body_bytes[name] += record["bytes"]
            hist[name][str(unit["body_tokens"])+":"+unit["unit_kind"]] += 1
            if name == "large":
                draws += 1
                entry = dict(record, text=unit["text"])
                if len(sample) < 64: sample.append(entry)
                else:
                    slot = rng.randrange(draws)
                    if slot < 64: sample[slot] = entry
        with mp.get_context("fork").Pool(WORKERS, initializer=worker_init,
                initargs=(str(tokenizer),)) as workers:
            for item in candidates:
                heartbeat("acquire-"+item["path"])
                cached = try_to_load_from_cache(source["repository"], item["path"],
                    repo_type="dataset", revision=source["revision"])
                is_cached = isinstance(cached, str) and Path(cached).is_file()
                path = Path(cached) if is_cached else Path(hf_hub_download(source["repository"], item["path"],
                    repo_type="dataset", revision=source["revision"], token=False))
                assert path.stat().st_size == item["bytes"]
                prior_verified = (item == previous["binding"]["file"] and
                    str(path) == previous["actual_cached_path"] and previous["verified_actual_sha256"] == item["sha256"])
                if not prior_verified: assert sha256(path) == item["sha256"]
                acquired.append(dict(item, cached=is_cached, path=str(path),
                    verification="prior pinned acquisition content hash/size reused" if prior_verified else "new full acquisition content SHA verified"))
                write_json(RUN/"acquired.json", acquired)
                last = time.monotonic()
                for units, rows, native in workers.imap(worker, tasks(path, item["path"]), chunksize=1):
                    counts["rows_processed"] += rows; counts["original_native_body_tokens"] += native
                    for unit in units:
                        if unit["source_family"] in excluded:
                            counts["inspected_family_excluded"] += 1; continue
                        digest = unit["canonical_sha256"]
                        if digest in seen or any(p in unit["text"] for p in protected):
                            counts["canonical_or_protected_excluded"] += 1; continue
                        seen.add(digest)
                        if unit["split"] == "dev":
                            if totals["dev"] < DEV_TARGET: append("dev", unit)
                        elif totals["small"] < TARGET:
                            group = groups.add(unit)
                            if group:
                                members, slot = group
                                for i, member in enumerate(members):
                                    append("large", member)
                                    if i == slot: append("small", member)
                    if time.monotonic()-last >= 5:
                        heartbeat("extract-"+item["path"]); last = time.monotonic()
                        print(json.dumps(dict(seconds=job["seconds"], tokens=dict(totals), rows=counts["rows_processed"])), flush=True)
                    if totals["small"] >= TARGET and totals["dev"] >= DEV_TARGET: break
                heartbeat("file-complete-"+item["path"])
                if totals["small"] >= TARGET and totals["dev"] >= DEV_TARGET: break
            workers.terminate()
        assert totals["small"] >= TARGET and totals["dev"] >= DEV_TARGET, dict(totals)
        assert offsets["large"] == 4*offsets["small"] and documents["large"] == 4*documents["small"]
        assert hist["large"] == Counter({k: 4*v for k,v in hist["small"].items()})
        token_bytes = read_json(ROOT/"configs/phase6/amount_learning_comparison.json")["pools"]["large"]["pool"]
        pools = {}
        for name in hist:
            for handle in (handles[name], indexes[name]):
                handle.flush(); os.fsync(handle.fileno()); handle.close()
            folder = DATA/name; split = "dev" if name == "dev" else "train"
            os.replace(folder/"train.partial.bin", folder/(split+".bin"))
            os.replace(folder/"train.index.partial.jsonl", folder/(split+".index.jsonl"))
            shutil.copyfile(Path(token_bytes)/"token_bytes.json", folder/"token_bytes.json")
            manifest = dict(version=1, dtype="<u2", kind="web", provenance_source="textbook", vocab_size=4096,
                tokenizer_sha256=binding["tokenizer_sha256"], token_bytes_sha256=sha256(folder/"token_bytes.json"),
                binding=binding, packing="Unchanged complete bodies/paragraphs; BOS masked; index source remains textbook",
                splits={split: dict(tokens=offsets[name], documents=documents[name], body_bytes=body_bytes[name],
                    stream_sha256=sha256(folder/(split+".bin")), index_sha256=sha256(folder/(split+".index.jsonl")), index_format="jsonl")})
            write_json(folder/"manifest.json", manifest)
            pools[name] = dict(pool=str(folder), manifest_sha256=sha256(folder/"manifest.json"), splits=manifest["splits"])
        write_json(DATA/"sample64.json", sample)
        ready = dict(status="component_prepared_pending_mixed_pool_content_review", binding=binding,
            pools=pools, prepared_tokens=dict(totals), histograms={k: dict(v) for k,v in hist.items()},
            nested_ratio_exact=4, small_subset_of_large=True, source_length_EOS_histograms_exact_ratio=True,
            sample_sha256=sha256(DATA/"sample64.json"), acquired=acquired, CPU_seconds=time.monotonic()-started,
            Base_adopted=False, GPU_teacher_tokens=0, protected_test_used=False, created_at=now())
        heartbeat("finalize")
        write_json(DATA/"ready.json", ready); write_json(RUN/"ready.json", ready)
        job.update(status="complete", completed_at=now())
        print(json.dumps(dict(status=ready["status"], tokens=dict(totals))), flush=True)
    except BaseException as error:
        job.update(status="failed", error=repr(error)); raise
    finally:
        for handle in (*handles.values(), *indexes.values()):
            if not handle.closed: handle.close()
        job["seconds"] = time.monotonic()-started; atomic_json(job_path, job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    prepare()
