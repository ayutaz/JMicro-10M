"""Bounded Japanese expansion, disk records, deterministic cluster splits and audit."""
from array import array
from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import argparse
import hashlib
import json
import math
import os
import sqlite3
import time
from functools import lru_cache

import numpy as np
import pyarrow.parquet as pq
from datasketch import MinHash, MinHashLSH

from jmicro.data import (contaminated, digest, evaluation_patterns, japanese_ratio,
                         normalized, overlap, shingles, url_key)
from jmicro.evaluation import canonicalize_text
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.shards import Shard, build_shards


class Union:
    def __init__(self):
        self.parent = array("q")

    def add(self):
        i = len(self.parent)
        self.parent.append(i)
        return i

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        self.parent[max(a, b)] = min(a, b)


@lru_cache(maxsize=8)
def permutations_for(seed):
    return MinHash(num_perm=128, seed=seed, scheme="legacy").permutations


def bounded_map(executor, function, tasks, pending=16):
    iterator, queue = iter(tasks), deque()
    for _ in range(pending):
        task = next(iterator, None)
        if task is None:
            break
        queue.append(executor.submit(function, task))
    while queue:
        yield queue.popleft().result()
        task = next(iterator, None)
        if task is not None:
            queue.append(executor.submit(function, task))


def signature(text, seed=42):
    """Vectorized Unicode 5-gram hash + 128 standard MinHash permutations.

    Exact Jaccard is always recomputed on actual strings for LSH candidates.
    Hash collisions/LSH can affect candidate recall, never establish a duplicate.
    """
    codes = np.frombuffer(text.encode("utf-32-le"), dtype="<u4").astype(np.uint64)
    length = len(codes)-4
    if length <= 0:
        raise ValueError("5-gram signature requires at least five characters")
    h = np.zeros(length, dtype=np.uint64)
    for i in range(5):
        h = h*np.uint64(1000003) + codes[i:i+length]+np.uint64(1)
    h ^= h >> np.uint64(33)
    h *= np.uint64(0xff51afd7ed558ccd)
    h ^= h >> np.uint64(33)
    hashes = np.unique(h & np.uint64(0xffffffff))
    permutations = permutations_for(seed)
    a, b = permutations
    result = np.full(128, np.uint64(0xffffffff))
    for start in range(0, len(hashes), 512):
        values = ((hashes[start:start+512, None]*a[None, :] + b[None, :])
                  % np.uint64((1 << 61)-1)) & np.uint64(0xffffffff)
        result = np.minimum(result, values.min(axis=0))
    return result


def analyze_batch(task):
    records, c = task
    result = []
    f, d = c["filters"], c["dedup"]
    for row in records:
        reason = None
        try:
            text = canonicalize_text(row["text"])
            if not f["web_min_chars"] <= len(text) <= f["web_max_chars"]:
                reason = "web_length"
            elif row["language"] not in ("ja", "jpn") or japanese_ratio(text) < f["min_japanese_ratio"]:
                reason = "language"
            elif not math.isfinite(float(row["language_score"])) or row["language_score"] < f["min_language_score"]:
                reason = "language_score"
            elif not math.isfinite(float(row["score"])) or row["score"] < f["min_quality_score"]:
                reason = "quality_score"
        except (TypeError, ValueError, UnicodeError, KeyError):
            text, reason = "", "invalid_record"
        clean = normalized(text)
        sketch = signature(clean, c["seed"]) if reason is None and len(clean) >= d["near_min_chars"] else None
        result.append((row, text, digest(text), digest(clean), reason, sketch))
    return result


def raw_batches(raw, c):
    receipt = read_json(raw / "acquisition.json")
    if receipt["status"] != "complete" or receipt["config_sha256"] != sha256(ROOT/"configs/phase6/preparation.json"):
        raise ValueError("Acquisition is incomplete or uses a different configuration")
    for file in receipt["files"]:
        path = raw/Path(file["path"]).name
        if sha256(path) != file["sha256"] or path.stat().st_size != file["bytes"]:
            raise ValueError("Acquired raw checksum or size differs")
        offset = 0
        for batch in pq.ParquetFile(path).iter_batches(batch_size=128):
            rows = []
            for i, row in enumerate(batch.to_pylist()):
                # Preserve the pilot's documented upstream first-10k exclusion.
                if path.name.startswith("train-00000-") and offset+i < 10000:
                    continue
                row.update(doc_id=f'{c["source"]}:{path.name}:{offset+i}',
                           source_file=path.name, source_row=offset+i, raw_sha256=file["sha256"])
                rows.append(row)
            offset += batch.num_rows
            if rows:
                yield rows, c


def pilot_rows():
    # The compact corpus omits URLs; the authoritative manifest retains them.
    path = ROOT/"data/phase1/processed/dataset_manifest.parquet"
    for batch in pq.ParquetFile(path).iter_batches(batch_size=1024):
        for row in batch.to_pylist():
            if row["kind"] == "web" and row["status"] == "kept":
                yield row


def build(raw, output, workers=8):
    c = read_json(ROOT/"configs/phase6/preparation.json")
    if sha256(ROOT/c["tokenizer"]) != c["tokenizer_sha256"]:
        raise ValueError("Pinned public tokenizer differs")
    if output.exists():
        raise ValueError("Preserve existing expansion; use a fresh output directory")
    output.mkdir(parents=True)
    process = {"status": "running", "pid": os.getpid(), "started_at": now()}
    if Path("/proc/self/stat").exists():
        process.update(boot_id=Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
                       start_ticks=Path("/proc/self/stat").read_text().split()[21])
    write_json(output/"job.json", process)
    source_hashes = {name: hashlib.sha256((ROOT/name).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
                     for name in ("src/jmicro/expanded_data.py", "src/jmicro/data.py", "src/jmicro/shards.py",
                                  "src/jmicro/evaluation.py", "src/jmicro/tokenizer.py", "uv.lock")}
    write_json(output/"source_hashes.json", source_hashes)
    started = time.perf_counter()
    db = sqlite3.connect(output/"records.sqlite")
    db.execute("CREATE TABLE records (id INTEGER PRIMARY KEY, payload TEXT, text TEXT, canonical TEXT, normalized TEXT, url TEXT, pilot INTEGER, contaminated INTEGER, reason TEXT, cluster INTEGER, split TEXT)")
    clusters, duplicates = Union(), Union()
    exact, urls, counts = {}, {}, Counter()
    lsh = MinHashLSH(num_perm=128, params=(32, 4))
    patterns = evaluation_patterns(read_json(ROOT/"configs/data/pilot.json"), ROOT)
    signature_stream = (output/"signatures.bin").open("wb")

    def text_at(i):
        return db.execute("SELECT text FROM records WHERE id=?", (i,)).fetchone()[0]

    def add(row, text, canonical, normhash, reason, sketch, pilot=False):
        i = clusters.add()
        assert duplicates.add() == i
        key = url_key(row.get("url", "")) if row.get("url") else ""
        bad = contaminated({"text": text}, patterns) if reason is None else False
        payload = dict(doc_id=row["doc_id"], kind="web", bucket=c["bucket"], canonical_sha256=canonical,
                       source=c["source"], source_subset=c["subset"], revision=c["revision"], license=c["license"],
                       url=row.get("url", ""), crawl_date=row.get("date"), quality_score=row.get("score"),
                       source_file=row.get("source_file"), source_row=row.get("source_row"), raw_sha256=row.get("raw_sha256"))
        db.execute("INSERT INTO records VALUES (?,?,?,?,?,?,?,?,?,?,?)", (i, json.dumps(payload, ensure_ascii=False),
                   text, canonical, normhash, key, int(pilot), int(bad), reason, None, None))
        signature_stream.write((sketch if sketch is not None else np.zeros(128, dtype=np.uint64)).astype("<u8").tobytes())
        counts["pilot" if pilot else "raw_records"] += 1
        if reason is not None:
            counts[reason] += 1
            return
        if key:
            previous = urls.setdefault(key, i)
            if previous != i:
                clusters.union(i, previous)
                counts["url_links"] += 1
        previous = exact.setdefault(normhash, i)
        if previous != i:
            clusters.union(i, previous)
            duplicates.union(i, previous)
            counts["normalized_exact_links"] += 1
            return  # The representative has the identical near signature.
        if sketch is not None:
            mh = MinHash(num_perm=128, seed=c["seed"], hashvalues=sketch,
                         permutations=permutations_for(c["seed"]), scheme="legacy")
            features = None
            for other in sorted(lsh.query(mh)):
                counts["lsh_candidate_pairs"] += 1
                if features is None:
                    features = shingles(normalized(text), 5)
                if overlap(features, shingles(normalized(text_at(other)), 5)) >= 0.85:
                    clusters.union(i, other)
                    duplicates.union(i, other)
                    counts["verified_near_links"] += 1
            lsh.insert(i, mh)

    for row in pilot_rows():
        clean = normalized(row["text"])
        add(row, row["text"], digest(row["text"]), digest(clean), None,
            signature(clean, c["seed"]) if len(clean) >= 64 else None, pilot=True)
    db.commit()
    # executor.map preserves input order, making cluster representatives/splits deterministic.
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for batch in bounded_map(executor, analyze_batch, raw_batches(raw, c), workers*2):
            for row, text, canonical, normhash, reason, sketch in batch:
                add(row, text, canonical, normhash, reason, sketch)
            if counts["raw_records"] % 10000 < 128:
                db.commit()
                progress = {"status": "building", "records": counts["raw_records"], "elapsed_seconds": time.perf_counter()-started}
                write_json(output/"progress.json", progress)
                print(json.dumps(progress), flush=True)
    signature_stream.close()
    db.commit()
    protected = {clusters.find(i) for (i,) in db.execute("SELECT id FROM records WHERE pilot=1 OR contaminated=1")}
    split_counts = Counter()
    with (output/"corpus.jsonl").open("w", encoding="utf-8") as stream:
        for i, payload, text, reason, pilot in db.execute("SELECT id,payload,text,reason,pilot FROM records ORDER BY id"):
            root = clusters.find(i)
            if pilot or reason:
                split = "excluded"
            elif root in protected:
                split = "excluded"
                reason = "pilot_or_fixed_evaluation_cluster"
            elif duplicates.find(i) != i:
                split = "excluded"
                reason = "normalized_exact_or_verified_near"
            else:
                value = int(digest(f'{c["seed"]}:expanded:{root}')[:16], 16) % 100
                split = "train" if value < 90 else "dev" if value < 95 else "test"
                row = json.loads(payload)
                row.update(text=text, split=split, cluster_id=root)
                stream.write(json.dumps(row, ensure_ascii=False)+"\n")
                split_counts[split] += 1
            db.execute("UPDATE records SET cluster=?,split=?,reason=? WHERE id=?", (root, split, reason, i))
            if not pilot and reason:
                counts["excluded_"+reason] += 1
    db.commit()
    db.close()
    del lsh, exact, urls
    manifest = build_shards(output/"corpus.jsonl", ROOT/c["tokenizer"], output/"shards")
    evidence = dict(status="built_not_audited", created_at=now(), config_sha256=sha256(ROOT/"configs/phase6/preparation.json"),
                    source_manifest_sha256=sha256(raw/"sources.json"), acquisition_sha256=sha256(raw/"acquisition.json"),
                    pilot_sha256=sha256(ROOT/"data/phase1/processed/corpus.jsonl"),
                    pilot_manifest_sha256=sha256(ROOT/"data/phase1/processed/dataset_manifest.parquet"),
                    fixed_suite_sha256={p:sha256(ROOT/p) for p in ("eval/base.jsonl", "eval/chat.jsonl")},
                    counts=dict(counts), split_documents=dict(split_counts), splits=manifest["splits"],
                    corpus_sha256=sha256(output/"corpus.jsonl"), records_sha256=sha256(output/"records.sqlite"),
                    signatures_sha256=sha256(output/"signatures.bin"), shard_manifest_sha256=sha256(output/"shards/manifest.json"),
                    mixture=c["mixture"], train_exposure={str(n):n/manifest["splits"]["train"]["tokens"] for n in (500000000,1000000000,10000000000)},
                    elapsed_seconds=time.perf_counter()-started, workers=workers,
                    source_sha256=source_hashes,
                    near_scope="128 permutations / 32x4 bands / Unicode rolling5 avalanche32; true 5-gram Jaccard >=0.85 verifies candidates. LSH recall is probabilistic.")
    write_json(output/"manifest.json", evidence)
    process.update(status="complete", completed_at=now())
    write_json(output/"job.json", process)
    print(json.dumps({"status":"built", "splits":{s:{k:v for k,v in x.items() if "sha256" not in k} for s,x in manifest["splits"].items()}}), flush=True)
    return evidence


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=["build"])
    p.add_argument("--raw", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--workers", type=int, default=8)
    args = p.parse_args()
    try:
        build(args.raw, args.output, args.workers)
    except Exception as exc:
        path = args.output/"job.json"
        if path.exists():
            record = read_json(path)
            if record.get("pid") == os.getpid():
                record.update(status="failed", completed_at=now(), failure=f"{type(exc).__name__}: {exc}")
                write_json(path, record)
        raise
