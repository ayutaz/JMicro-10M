"""Restartable corpus ingestion and external-sort LSH for the local 10B corpus.

Keep the original Phase 6 builder frozen. SQLite stores source/protection records;
one sorted band at a time bounds memory instead of maintaining 32 giant hash maps.
"""
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import time

import numpy as np
import pyarrow.parquet as pq

from jmicro.data import contaminated, digest, evaluation_patterns, normalized, overlap, shingles, url_key
from jmicro.expanded_data import analyze_batch, bounded_map, pilot_rows, signature
from jmicro.experiment import ROOT, now, sha256
from jmicro.corpus_state import read_json, write_json
from jmicro.tokenizer import Tokenizer


def connect(path):
    db = sqlite3.connect(path)
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA synchronous=FULL")
    db.execute("PRAGMA cache_size=-262144")
    return db


def check_binding(db, key, value):
    encoded = json.dumps(value, sort_keys=True)
    old = db.execute("SELECT value FROM state WHERE key=?", (key,)).fetchone()
    if old is not None and old[0] != encoded:
        raise ValueError(f"Ingest binding changed: {key}")
    db.execute("INSERT OR IGNORE INTO state VALUES (?,?)", (key, encoded))
    db.commit()


def protected_rows(c):
    yield from pilot_rows()
    with Path(c["protected_corpus"]).open(encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["split"] in ("dev", "test"):
                yield row


def batches(path, source, c):
    offset = 0
    for batch in pq.ParquetFile(path).iter_batches(batch_size=128):
        rows = []
        for i, row in enumerate(batch.to_pylist()):
            if path.name.startswith("train-00000-") and offset+i < 10000:
                continue
            row.update(doc_id=f'{c["source"]}:{path.name}:{offset+i}', source_file=path.name,
                       source_row=offset+i, raw_sha256=source["sha256"])
            rows.append(row)
        offset += batch.num_rows
        if rows:
            yield rows, c


def ingest(config, raw, output, workers):
    c = read_json(config)
    if sha256(ROOT/c["tokenizer"]) != c["tokenizer_sha256"]:
        raise ValueError("Tokenizer differs")
    if sha256(Path(c["protected_corpus"])) != c["protected_corpus_sha256"]:
        raise ValueError("Previous corpus changed")
    receipt = read_json(raw/"acquisition.json")
    if receipt["status"] != "complete" or receipt["config_sha256"] != sha256(config):
        raise ValueError("Acquisition is incomplete or changed")
    output.mkdir(parents=True, exist_ok=True)
    db = connect(output/"records.sqlite")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY,value TEXT);
        CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY,payload TEXT,text TEXT,
            norm TEXT,url TEXT,reason TEXT,protected INTEGER,rep INTEGER,sketch INTEGER);
        CREATE TABLE IF NOT EXISTS exact (hash TEXT PRIMARY KEY,id INTEGER);
        CREATE TABLE IF NOT EXISTS urls (url TEXT PRIMARY KEY,id INTEGER);
        CREATE TABLE IF NOT EXISTS edges (a INTEGER,b INTEGER,duplicate INTEGER);
        CREATE TABLE IF NOT EXISTS files (name TEXT PRIMARY KEY,sha256 TEXT,rows INTEGER);
    """)
    bindings = {"config": sha256(config), "acquisition": sha256(raw/"acquisition.json"),
                "protected": c["protected_corpus_sha256"],
                "pilot": sha256(ROOT/"data/phase1/processed/dataset_manifest.parquet"),
                "evaluation": {p: sha256(ROOT/p) for p in ("eval/base.jsonl", "eval/chat.jsonl")},
                "code": {p: hashlib.sha256((ROOT/p).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
                         for p in ("src/jmicro/large_corpus.py", "src/jmicro/corpus_state.py", "src/jmicro/expanded_data.py",
                                   "src/jmicro/data.py", "src/jmicro/tokenizer.py", "uv.lock")}}
    for key, value in bindings.items():
        check_binding(db, key, value)
    patterns = evaluation_patterns(read_json(ROOT/"configs/data/pilot.json"), ROOT)
    n = db.execute("SELECT count(*) FROM records").fetchone()[0]
    sigpath = output/"signatures.u32.bin"
    stream = sigpath.open("r+b" if sigpath.exists() else "w+b")
    if stream.seek(0, 2) < n*512:
        raise ValueError("Committed signatures are truncated")
    stream.truncate(n*512)
    stream.seek(n*512)

    def add(values, protect):
        nonlocal n
        row, text, canonical, normhash, reason, sketch = values
        i = n
        n += 1
        key = url_key(row.get("url", "")) if row.get("url") else ""
        protected = protect or (reason is None and contaminated({"text": text}, patterns))
        payload = dict(doc_id=row["doc_id"], kind="web", bucket=c["bucket"],
                       canonical_sha256=canonical, source=c["source"], source_subset=c["subset"],
                       revision=c["revision"], license=c["license"], url=row.get("url", ""),
                       crawl_date=row.get("date"), quality_score=row.get("score"),
                       source_file=row.get("source_file"), source_row=row.get("source_row"),
                       raw_sha256=row.get("raw_sha256"))
        rep = i
        if reason is None:
            old = db.execute("SELECT id FROM exact WHERE hash=?", (normhash,)).fetchone()
            if old is None:
                db.execute("INSERT INTO exact VALUES (?,?)", (normhash, i))
            else:
                rep = old[0]
                db.execute("INSERT INTO edges VALUES (?,?,1)", (i, rep))
            if key:
                old = db.execute("SELECT id FROM urls WHERE url=?", (key,)).fetchone()
                if old is None:
                    db.execute("INSERT INTO urls VALUES (?,?)", (key, i))
                else:
                    db.execute("INSERT INTO edges VALUES (?,?,0)", (i, old[0]))
        eligible = reason is None and rep == i and sketch is not None
        db.execute("INSERT INTO records VALUES (?,?,?,?,?,?,?,?,?)",
                   (i, json.dumps(payload, ensure_ascii=False), text, normhash, key, reason,
                    int(protected), rep, int(eligible)))
        stream.write((sketch if sketch is not None else np.zeros(128)).astype("<u4").tobytes())

    started = time.monotonic()
    try:
        if db.execute("SELECT 1 FROM files WHERE name='__protected__'").fetchone() is None:
            db.execute("BEGIN")
            for row in protected_rows(c):
                text = row["text"]
                clean = normalized(text)
                add((row, text, digest(text), digest(clean), None,
                     signature(clean, c["seed"]) if len(clean) >= c["dedup"]["near_min_chars"] else None), True)
            stream.flush()
            os.fsync(stream.fileno())
            db.execute("INSERT INTO files VALUES ('__protected__',?,?)", (c["protected_corpus_sha256"], n))
            db.commit()
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for source in receipt["files"]:
                path = raw/Path(source["path"]).name
                done = db.execute("SELECT sha256 FROM files WHERE name=?", (path.name,)).fetchone()
                if done is not None:
                    if done[0] != source["sha256"]:
                        raise ValueError("Previously ingested file binding changed")
                    continue
                if path.stat().st_size != source["bytes"] or sha256(path) != source["sha256"]:
                    raise ValueError("Raw file size/hash changed")
                begin = n
                db.execute("BEGIN")
                for batch in bounded_map(executor, analyze_batch, batches(path, source, c), workers*2):
                    for values in batch:
                        add(values, False)
                    if (n-begin) % 10000 < 128:
                        progress = {"stage": "ingest", "file": path.name, "file_records": n-begin,
                                    "total_records": n, "seconds": time.monotonic()-started}
                        write_json(output/"progress.json", progress)
                        print(json.dumps(progress), flush=True)
                stream.flush()
                os.fsync(stream.fileno())
                db.execute("INSERT INTO files VALUES (?,?,?)", (path.name, source["sha256"], n-begin))
                db.commit()
                write_json(output/"ingest_checkpoint.json", {"records": n, "completed_file": path.name,
                                                             "completed_at": now()})
        db.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        write_json(output/"ingest_complete.json", {"records": n, "bindings": bindings,
                                                  "elapsed_seconds": time.monotonic()-started})
    finally:
        stream.close()
        db.close()
    return n


class Groups:
    def __init__(self, n, values=None):
        self.parent = np.arange(n, dtype=np.uint32) if values is None else values

    def find(self, i):
        i = int(i)
        while int(self.parent[i]) != i:
            self.parent[i] = self.parent[int(self.parent[i])]
            i = int(self.parent[i])
        return i

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        self.parent[max(a, b)] = min(a, b)


def band_order(sketches, ids, band):
    """Same 32x4 equality candidates as the frozen MinHashLSH, without hashing."""
    keys = np.asarray(sketches[ids, band*4:band*4+4])
    order = np.lexsort((ids, keys[:, 3], keys[:, 2], keys[:, 1], keys[:, 0]))
    sorted_keys = keys[order]
    equal = np.all(sorted_keys[1:] == sorted_keys[:-1], axis=1)
    boundaries = np.r_[0, np.flatnonzero(~equal)+1, len(ids)]
    return ids[order], boundaries


def deduplicate(output):
    n = read_json(output/"ingest_complete.json")["records"]
    db = connect(output/"records.sqlite")
    sketches = np.memmap(output/"signatures.u32.bin", mode="r", dtype="<u4", shape=(n,128))
    ids = np.fromiter((r[0] for r in db.execute("SELECT id FROM records WHERE sketch=1 ORDER BY id")),
                      dtype=np.uint32)
    checkpoint = output/"dedup_checkpoint.json"
    previous = read_json(checkpoint) if checkpoint.exists() else {"completed_band": -1, "verified_pairs": 0}
    if previous["completed_band"] >= 0:
        groups = Groups(n, np.load(output/f'groups-{previous["completed_band"]:02d}.npy'))
        duplicates = Groups(n, np.load(output/f'duplicates-{previous["completed_band"]:02d}.npy'))
    else:
        groups, duplicates = Groups(n), Groups(n)
        for a,b,duplicate in db.execute("SELECT a,b,duplicate FROM edges"):
            groups.union(a,b)
            if duplicate:
                duplicates.union(a,b)
    verified = previous["verified_pairs"]
    started = time.monotonic()

    @lru_cache(maxsize=4096)
    def features(i):
        return shingles(normalized(db.execute("SELECT text FROM records WHERE id=?", (int(i),)).fetchone()[0]),5)

    try:
        for band in range(previous["completed_band"]+1,32):
            ordered, bounds = band_order(sketches, ids, band)
            for start,end in zip(bounds[:-1],bounds[1:]):
                if end-start < 2:
                    continue
                members = ordered[start:end]
                for pos,a in enumerate(members):
                    for b in members[:pos]:
                        if duplicates.find(a) == duplicates.find(b):
                            continue
                        if overlap(features(int(a)),features(int(b))) >= .85:
                            groups.union(a,b)
                            duplicates.union(a,b)
                            verified += 1
            np.save(output/f"groups-{band:02d}.npy",groups.parent)
            np.save(output/f"duplicates-{band:02d}.npy",duplicates.parent)
            progress = {"stage": "external_lsh", "completed_band": band, "verified_pairs": verified,
                        "seconds": time.monotonic()-started}
            write_json(checkpoint,progress)
            write_json(output/"progress.json",progress)
            print(json.dumps(progress),flush=True)
        # Compact final parents for reproducible export and independent edge audit.
        for i in range(n):
            groups.parent[i] = groups.find(i)
            duplicates.parent[i] = duplicates.find(i)
        np.save(output/"groups.npy",groups.parent)
        np.save(output/"duplicates.npy",duplicates.parent)
        write_json(output/"dedup_complete.json", {"records": n, "verified_pairs": verified,
                                                  "groups_sha256":sha256(output/"groups.npy"),
                                                  "duplicates_sha256":sha256(output/"duplicates.npy")})
    finally:
        db.close()


@lru_cache(maxsize=1)
def worker_tokenizer(path):
    return Tokenizer(path)


def tokenize_batch(task):
    rows,path = task
    tok = worker_tokenizer(path)
    result = []
    for row in rows:
        text = row["text"]
        body = tok.encode(text)
        if tok.decode(body) != text or digest(text) != row["canonical_sha256"]:
            raise ValueError("Tokenized document is not lossless/canonical")
        result.append((row, np.asarray([2,*body,3],dtype="<u2").tobytes(),len(body)))
    return result


def export(config, output, workers):
    c = read_json(config)
    n = read_json(output/"dedup_complete.json")["records"]
    groups = np.load(output/"groups.npy",mmap_mode="r")
    duplicates = np.load(output/"duplicates.npy",mmap_mode="r")
    db = connect(output/"records.sqlite")
    protected = np.zeros(n,dtype=np.bool_)
    for (i,) in db.execute("SELECT id FROM records WHERE protected=1"):
        protected[int(groups[i])] = True
    attempts = sorted(output.glob("export-*"))
    destination = output/f"export-{len(attempts)+1:03d}"
    destination.mkdir()
    shards = destination/"shards"
    shards.mkdir()
    counters = {s: Counter(tokens=0,documents=0,body_bytes=0) for s in ("train","dev","test")}
    streams = {s:(shards/f"{s}.bin").open("wb") for s in counters}
    indexes = {s:(shards/f"{s}.index.json").open("w",encoding="utf-8") for s in counters}
    for stream in indexes.values():
        stream.write("[\n")
    corpus = (destination/"corpus.jsonl").open("w",encoding="utf-8")
    exclusions = Counter()

    def tasks():
        batch=[]
        for i,payload,text,reason,protect in db.execute("SELECT id,payload,text,reason,protected FROM records ORDER BY id"):
            if reason is not None:
                exclusions[reason] += 1
                continue
            if protect or protected[int(groups[i])]:
                exclusions["protected_cluster"] += 1
                continue
            if int(duplicates[i]) != i:
                exclusions["duplicate"] += 1
                continue
            root = int(groups[i])
            value = int(digest(f'{c["seed"]}:expanded:{root}')[:16],16)%100
            split = "train" if value<90 else "dev" if value<95 else "test"
            row = json.loads(payload)
            row.update(text=text,split=split,cluster_id=root,record_id=i)
            batch.append(row)
            if len(batch)==128:
                yield batch,str(ROOT/c["tokenizer"])
                batch=[]
        if batch:
            yield batch,str(ROOT/c["tokenizer"])

    started = time.monotonic()
    try:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for batch in bounded_map(executor,tokenize_batch,tasks(),workers*2):
                for row,ids,body_tokens in batch:
                    s = row["split"]
                    count = counters[s]
                    index = dict(doc_id=row["doc_id"],split=s,kind="web",bucket=c["bucket"],
                                 canonical_sha256=row["canonical_sha256"],offset=count["tokens"],
                                 body_tokens=body_tokens,bytes=len(row["text"].encode()))
                    if count["documents"]:
                        indexes[s].write(",\n")
                    indexes[s].write(json.dumps(index,ensure_ascii=False))
                    streams[s].write(ids)
                    corpus.write(json.dumps(row,ensure_ascii=False)+"\n")
                    count.update(tokens=body_tokens+2,documents=1,body_bytes=index["bytes"])
                if sum(x["documents"] for x in counters.values())%10000<128:
                    progress={"stage":"export", "splits":counters,"seconds":time.monotonic()-started}
                    write_json(output/"progress.json",progress)
                    print(json.dumps(progress),flush=True)
    finally:
        corpus.close()
        for stream in streams.values():
            stream.close()
        for stream in indexes.values():
            stream.write("\n]\n")
            stream.close()
        db.close()
    tok = Tokenizer(ROOT/c["tokenizer"])
    write_json(shards/"token_bytes.json",[0 if i<8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)])
    manifest={"version":1,"dtype":"<u2","kind":"web","corpus_sha256":sha256(destination/"corpus.jsonl"),
              "tokenizer_sha256":c["tokenizer_sha256"],"vocab_size":tok.vocab_size,
              "packing":"BOS/body/EOS; causal attention across documents; BOS targets masked",
              "limit_per_split":None,"token_bytes_sha256":sha256(shards/"token_bytes.json"),"splits":{}}
    for s,count in counters.items():
        manifest["splits"][s]={**count,"stream_sha256":sha256(shards/f"{s}.bin"),
                                "index_sha256":sha256(shards/f"{s}.index.json")}
    write_json(shards/"manifest.json",manifest)
    result={"status":"built_not_audited","config_sha256":sha256(config),"artifact_directory":str(destination),
            "splits":manifest["splits"],"exclusions":dict(exclusions),"completed_at":now(),
            "target_met":counters["train"]["tokens"]>=c["minimum_train_stream_tokens"],
            "near_scope":"128 permutations/32x4 equal bands; true character5gram Jaccard>=0.85; probabilistic recall"}
    write_json(output/"manifest.json",result)
    return result
