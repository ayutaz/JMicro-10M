"""Prepare matched500M/2B with95percent Web and5percent stories; no GPU."""
from collections import Counter
import json
import multiprocessing as mp
import os
from pathlib import Path
import random
import numpy as np
import shutil
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.eos_pilot import TrainView, spans
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.nested_material_v2 import material_unit
from jmicro.larger_material import FourGroups
from jmicro.training import atomic_json
from phase6_performance import identity, alive
import prepare_complete_units as decode

DATA = Path("/home/aihub_ubuntu/jmicro-data/phase6/larger-material-20261006-95web")
RUN = ROOT / "reports/phase6/larger-material-20261006-95web"
SEED = 2026100621
TARGETS = dict(web=475000000, story=25000000)  # Small500M; large2B is exactly4x.
DEV = dict(web=1900000, story=100000)
BUDGET = 1800


def worker(task):
    source, batch = task
    out = []
    for a, b in batch:
        ids = decode._TRAIN[a+1:b].tolist()
        if any(i < 8 for i in ids):
            continue
        try:
            text = b"".join(decode._PIECES[i] for i in ids).decode("utf-8")
        except UnicodeDecodeError:
            continue
        unit = material_unit(text, ids, source, decode._TOK)
        if unit:
            out.append(dict(unit, source=source, source_start=a, source_end=b))
    return out


def batches(view, source, check, counts):
    previous, batch = -1, []
    lo, hi = (32, 512) if source == "story" else (64, 8192)
    for offset in range(0, len(view.tokens), 4000000):
        check()
        chunk = view.tokens[offset:offset+4000000]
        starts, ends, previous = spans(chunk, offset, previous)
        counts[source+"_scan_tokens"] = offset + len(chunk)
        sizes = ends - starts - 1
        mask = (sizes >= lo) & (sizes <= hi)
        for a, b in zip(starts[mask], ends[mask]):
            batch.append((int(a), int(b)))
            if len(batch) == 256:
                yield source, batch
                batch = []
        if batch:
            yield source, batch
            batch = []


def prepare():
    RUN.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    path = RUN / "prepare-job.json"
    base = read_json(ROOT / "configs/phase6/architecture_comparison.json")
    expansion = read_json(ROOT / "configs/phase6/dataset_expansion_1b.json")
    sources = dict(web=dict(pool=base["web_shards"], manifest_sha256=base["web_manifest_sha256"]),
                   story={k: expansion["arms"]["refined"][k] for k in ("pool", "manifest_sha256")})
    binding = dict(sources=sources, small_prepared_targets=TARGETS, dev_targets=DEV,
        exact_large_to_small_ratio=4, seed=SEED, CPU_budget_seconds=BUDGET, workers=8,
        tokenizer=base["tokenizer"], tokenizer_sha256=base["tokenizer_sha256"],
        builder_sha256=sha256(Path(__file__)), selector_sha256=sha256(ROOT / "src/jmicro/nested_material_v2.py"),
        original_selector_sha256=sha256(ROOT / "src/jmicro/nested_material.py"),
        processing_sha256={p:sha256(ROOT/p) for p in ("scripts/prepare_complete_units.py", "src/jmicro/eos_pilot.py",
            "src/jmicro/tokenizer.py", "src/jmicro/complete_units.py", "src/jmicro/coherent_units.py", "src/jmicro/evaluation.py")},
        source_ratio=dict(web=.95, story=.05), grouping_sha256=sha256(ROOT / "src/jmicro/larger_material.py"),
        scope="Five items stage5 material supply only; matched95/5 mixture in500M/2B; quantity comparison within new mixture, old80/20 separate; no GPU/adoption")
    if path.exists():
        old = read_json(path)
        assert old["binding"] == binding and not alive(old)
        if old["status"] == "complete":
            print("Completed material retained", flush=True)
            return
        raise RuntimeError("Preserved failed preparation: inspect its supply/content evidence before another version")
    start = time.monotonic()
    job = dict(status="running", **identity(), binding=binding, started_at=now())
    counts, totals = Counter(), Counter()
    def check():
        if time.monotonic() - start > BUDGET:
            raise TimeoutError("1800s CPU material supply budget exhausted; partials are not ready")
    def heartbeat(stage):
        check()
        job.update(stage=stage, heartbeat_at=now(), seconds=time.monotonic()-start,
            counts=dict(counts), prepared_tokens=dict(totals))
        atomic_json(path, job)
    seen = set()
    groups = FourGroups(SEED)
    reservoirs = {name: {s: [] for s in sources} for name in ("large", "dev")}
    sample_counts, histograms = Counter(), {name: Counter() for name in ("small", "large", "dev")}
    rng = random.Random(SEED + 1)
    streams, indexes, offsets, documents, body_bytes = {}, {}, Counter(), Counter(), Counter()
    protected = []
    for suite in ("eval/base.jsonl", "eval/japanese_semantics_v2_1.jsonl"):
        for line in (ROOT / suite).read_text().splitlines():
            r = json.loads(line)
            if r.get("split", "dev") == "dev":
                protected.extend(r[k] for k in ("prefix", "context") if isinstance(r.get(k), str) and len(r[k]) >= 12)
    try:
        assert sha256(ROOT / base["tokenizer"]) == base["tokenizer_sha256"]
        for p in (*binding["processing_sha256"], "scripts/prepare_larger_material.py", "scripts/prepare_larger_material.ps1", "src/jmicro/larger_material.py", "src/jmicro/nested_material.py", "src/jmicro/nested_material_v2.py"):
            dest = RUN / "source" / p
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / p, dest)
        for name in ("small", "large", "dev"):
            folder = DATA / name
            folder.mkdir()
            streams[name] = (folder / "train.partial.bin").open("wb")
            indexes[name] = (folder / "train.index.partial.jsonl").open("w")
        def append(name, unit, view):
            ids = np.asarray(unit["token_ids"], dtype="<u2") if "token_ids" in unit else view.tokens[unit["source_start"]:unit["source_end"]+1]
            assert ids[0] == 2 and ids[-1] == 3 and len(ids) == unit["body_tokens"] + 2
            row = {k: v for k, v in unit.items() if k not in ("text", "token_ids")}
            row.update(doc_id="nested-"+unit["canonical_sha256"][:24], offset=offsets[name],
                split="dev" if name == "dev" else "train", bytes=len(unit["text"].encode()),
                source_manifest_sha256=sources[unit["source"]]["manifest_sha256"])
            streams[name].write(ids.tobytes())
            indexes[name].write(json.dumps(row, ensure_ascii=False)+"\n")
            offsets[name] += len(ids)
            documents[name] += 1
            body_bytes[name] += row["bytes"]
            totals[name+"_"+unit["source"]] += len(ids)
            histograms[name][unit["source"]+":"+str(unit["body_tokens"])+":"+unit["unit_kind"]] += 1
            if name in reservoirs:
                key = name+"_"+unit["source"]
                sample_counts[key] += 1
                limit = 32 if name == "large" else 16
                sample = dict(row, text=unit["text"])
                selected = reservoirs[name][unit["source"]]
                if len(selected) < limit:
                    selected.append(sample)
                else:
                    slot = rng.randrange(sample_counts[key])
                    if slot < limit:
                        selected[slot] = sample

        for source, ref in sources.items():
            heartbeat("setup-"+source)
            view = TrainView(ref["pool"], ref["manifest_sha256"])
            assert view.manifest["tokenizer_sha256"] == base["tokenizer_sha256"]
            assert view.manifest["splits"]["train"]["tokens"] > 4 * TARGETS[source]
            with mp.get_context("fork").Pool(8, initializer=decode.worker_init,
                    initargs=(str(ROOT / base["tokenizer"]), str(view.directory / "train.bin"))) as workers:
                for units in workers.imap(worker, batches(view, source, check, counts), chunksize=1):
                    check()
                    for unit in units:
                        digest = unit["canonical_sha256"]
                        if digest in seen or any(p in unit["text"] for p in protected):
                            counts["local_duplicate_or_dev_prefix_excluded"] += 1
                            continue
                        seen.add(digest)
                        if unit["split"] == "dev":
                            if totals["dev_"+source] < DEV[source]:
                                append("dev", unit, view)
                        elif totals["small_"+source] < TARGETS[source]:
                            result = groups.add(unit)
                            if result:
                                all_units, small_slot = result
                                for i, member in enumerate(all_units):
                                    append("large", member, view)
                                    if i == small_slot:
                                        append("small", member, view)
                        if totals["small_"+source] >= TARGETS[source] and totals["dev_"+source] >= DEV[source]:
                            break
                    if time.monotonic() - job.get("last_report", start) > 5:
                        heartbeat("extract-"+source)
                        job["last_report"] = time.monotonic()
                        print(json.dumps(dict(source=source, seconds=job["seconds"], tokens=dict(totals))), flush=True)
                    if totals["small_"+source] >= TARGETS[source] and totals["dev_"+source] >= DEV[source]:
                        break
                workers.terminate()
            assert totals["small_"+source] >= TARGETS[source] and totals["dev_"+source] >= DEV[source], dict(totals)
        assert histograms["large"] == Counter({k: 4*v for k,v in histograms["small"].items()})
        assert offsets["large"] == 4 * offsets["small"] and documents["large"] == 4 * documents["small"]
        pools = {}
        for name in streams:
            streams[name].flush(); os.fsync(streams[name].fileno()); streams[name].close()
            indexes[name].flush(); os.fsync(indexes[name].fileno()); indexes[name].close()
            folder = DATA / name
            split = "dev" if name == "dev" else "train"
            os.replace(folder / "train.partial.bin", folder / (split+".bin"))
            os.replace(folder / "train.index.partial.jsonl", folder / (split+".index.jsonl"))
            shutil.copyfile(Path(sources["web"]["pool"]) / "token_bytes.json", folder / "token_bytes.json")
            manifest = dict(version=1, dtype="<u2", kind="web", vocab_size=4096,
                tokenizer_sha256=base["tokenizer_sha256"], binding=binding,
                token_bytes_sha256=sha256(folder / "token_bytes.json"),
                packing="Original whole bodies or intact first-four lead paragraphs; paragraph bodies retokenized without text rewriting; BOS targets masked",
                splits={split: dict(tokens=offsets[name], documents=documents[name], body_bytes=body_bytes[name],
                    stream_sha256=sha256(folder / (split+".bin")), index_sha256=sha256(folder / (split+".index.jsonl")), index_format="jsonl")})
            write_json(folder / "manifest.json", manifest)
            pools[name] = dict(pool=str(folder), manifest_sha256=sha256(folder / "manifest.json"), splits=manifest["splits"])
        sample = reservoirs["large"]["web"] + reservoirs["large"]["story"]
        dev32 = reservoirs["dev"]["web"] + reservoirs["dev"]["story"]
        assert len(sample) == 64 and len(dev32) == 32
        write_json(DATA / "sample64.json", sample)
        write_json(DATA / "dev32.json", dev32)
        ready = dict(status="prepared_pending_fixed_content_review", binding=binding, pools=pools,
            prepared_tokens=dict(totals), histograms={k: dict(v) for k,v in histograms.items()},
            nested_ratio_exact=4, small_subset_of_large=True, source_length_EOS_histograms_exact_ratio=True, editorial_unit_histograms_exact_ratio=True,
            sample_sha256=sha256(DATA / "sample64.json"), dev32_sha256=sha256(DATA / "dev32.json"),
            content_gate="Fixed64 weak<=10; manual content pending; no GPU/adoption before readiness",
            audit="Local canonical exact exclusion and normalized first-sentence-family dev split; original train source only. Global site/author/near duplicates unverified; original10B may have seen source records",
            source_history="Reuses pinned accepted Web/story train;95/5 mixture differs from old80/20; no new download; new selected corpus quantity is not guaranteed globally independent",
            CPU_seconds=time.monotonic()-start, protected_test_used=False, created_at=now())
        write_json(DATA / "ready.json", ready); write_json(RUN / "ready.json", ready)
        heartbeat("complete"); job.update(status="complete", completed_at=now())
        print(json.dumps(dict(status=ready["status"], tokens=dict(totals), CPU_seconds=ready["CPU_seconds"])), flush=True)
    except BaseException as error:
        job.update(status="failed", error=repr(error))
        raise
    finally:
        for handle in (*streams.values(), *indexes.values()):
            if not handle.closed:
                handle.close()
        job["seconds"] = time.monotonic()-start
        atomic_json(path, job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    prepare()
