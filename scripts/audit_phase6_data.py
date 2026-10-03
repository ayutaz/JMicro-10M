"""Independently reconstruct all expansion records/edges and verify every shard doc."""
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import argparse
import hashlib
import json
import os
import sqlite3
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from datasketch import MinHash, MinHashLSH
from jmicro.data import contaminated, digest, evaluation_patterns, normalized, overlap, shingles, url_key
from jmicro.expanded_data import Union, analyze_batch, bounded_map, permutations_for, pilot_rows, raw_batches, signature
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer


def audit(raw, output, workers):
    started = time.perf_counter()
    c = read_json(ROOT/"configs/phase6/preparation.json")
    m = read_json(output/"manifest.json")
    for key, path in [("config_sha256", ROOT/"configs/phase6/preparation.json"),
                      ("corpus_sha256",output/"corpus.jsonl"), ("records_sha256",output/"records.sqlite"),
                      ("signatures_sha256",output/"signatures.bin"), ("source_manifest_sha256",raw/"sources.json"),
                      ("acquisition_sha256",raw/"acquisition.json"), ("pilot_sha256",ROOT/"data/phase1/processed/corpus.jsonl"),
                      ("pilot_manifest_sha256",ROOT/"data/phase1/processed/dataset_manifest.parquet"),
                      ("shard_manifest_sha256",output/"shards/manifest.json")]:
        if sha256(path) != m[key]:
            raise ValueError(f"Manifest binding differs: {key}")
    for name, expected in m["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes().replace(b"\r\n",b"\n")).hexdigest() != expected:
            raise ValueError("Expansion implementation changed")
    for name, expected in m["fixed_suite_sha256"].items():
        if sha256(ROOT/name) != expected:
            raise ValueError("Fixed evaluation changed")
    if sha256(ROOT/c["tokenizer"]) != c["tokenizer_sha256"]:
        raise ValueError("Public tokenizer differs")
    source = read_json(raw/"sources.json")
    if sha256(raw/"README.upstream.md") != source["evidence_sha256"]:
        raise ValueError("Pinned source conditions changed")
    db = sqlite3.connect(f'file:{output/"records.sqlite"}?mode=ro', uri=True)
    if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        raise ValueError("Record database integrity failed")
    n = db.execute("SELECT count(*) FROM records").fetchone()[0]
    if (output/"signatures.bin").stat().st_size != n*128*8:
        raise ValueError("Sketch count differs")
    sketches = np.memmap(output/"signatures.bin", dtype="<u8", mode="r", shape=(n,128))
    patterns = evaluation_patterns(read_json(ROOT/"configs/data/pilot.json"), ROOT)
    groups, duplicate_groups = Union(), Union()
    lsh = MinHashLSH(num_perm=128, params=(32,4))
    exact, urls, protected, edge_counts = {}, {}, set(), Counter()
    position = 0

    def inspect(row, text, canonical, normhash, filter_reason, sketch, pilot):
        nonlocal position
        i = position
        position += 1
        assert groups.add() == duplicate_groups.add() == i
        stored = db.execute("SELECT payload,text,canonical,normalized,url,pilot,contaminated,reason FROM records WHERE id=?",(i,)).fetchone()
        if stored is None:
            raise ValueError("Raw record absent")
        payload, actual_text, can, norm, key, is_pilot, bad, reason = stored
        payload = json.loads(payload)
        expected_url = url_key(row.get("url", "")) if row.get("url") else ""
        expected_bad = contaminated({"text":text},patterns) if filter_reason is None else False
        if (actual_text,can,norm,key,is_pilot,bad) != (text,canonical,normhash,expected_url,int(pilot),int(expected_bad)):
            raise ValueError("Raw canonical/dedup/URL/contamination reconstruction differs")
        if payload["doc_id"] != row["doc_id"] or payload["canonical_sha256"] != canonical:
            raise ValueError("Source document identity differs")
        if not pilot:
            for field in ("source_file","source_row","raw_sha256","url"):
                if payload[field] != row.get(field):
                    raise ValueError("Source provenance differs")
        expected_sketch = sketch if sketch is not None else np.zeros(128,dtype=np.uint64)
        if not np.array_equal(sketches[i],expected_sketch):
            raise ValueError("Reconstructed signature differs")
        if pilot or bad:
            protected.add(i)
        if filter_reason is not None:
            if reason != filter_reason:
                raise ValueError("Filter reconstruction differs")
            return
        if key:
            previous = urls.setdefault(key,i)
            if previous != i:
                groups.union(i,previous)
                edge_counts["url_links"] += 1
        previous = exact.setdefault(normhash,i)
        if previous != i:
            groups.union(i,previous)
            duplicate_groups.union(i,previous)
            edge_counts["normalized_exact_links"] += 1
            return
        if sketch is not None:
            mh = MinHash(num_perm=128,seed=c["seed"],hashvalues=sketch,permutations=permutations_for(c["seed"]),scheme="legacy")
            features = None
            for other in sorted(lsh.query(mh)):
                edge_counts["lsh_candidate_pairs"] += 1
                if features is None:
                    features = shingles(normalized(text),5)
                old_text = db.execute("SELECT text FROM records WHERE id=?",(other,)).fetchone()[0]
                if overlap(features,shingles(normalized(old_text),5)) >= 0.85:
                    groups.union(i,other)
                    duplicate_groups.union(i,other)
                    edge_counts["verified_near_links"] += 1
            lsh.insert(i,mh)

    for row in pilot_rows():
        text = row["text"]
        clean = normalized(text)
        inspect(row,text,digest(text),digest(clean),None,signature(clean,c["seed"]) if len(clean)>=64 else None,True)
    pilot_count = position
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for batch in bounded_map(executor,analyze_batch,raw_batches(raw,c),workers*2):
            for values in batch:
                inspect(*values,False)
            if (position-pilot_count) % 10000 < 128:
                print(json.dumps({"stage":"raw_and_edges","records":position-pilot_count,"seconds":time.perf_counter()-started}),flush=True)
    if position != n or position-pilot_count != m["counts"]["raw_records"] or pilot_count != m["counts"]["pilot"]:
        raise ValueError("Raw membership/count differs")
    for field in ("url_links","normalized_exact_links","lsh_candidate_pairs","verified_near_links"):
        if edge_counts[field] != m["counts"].get(field,0):
            raise ValueError("Dedup edge evidence differs")
    protected = {groups.find(i) for i in protected}
    del lsh, exact, urls
    splits, canonical_seen, clusters_by_split = Counter(), set(), {}
    with (output/"corpus.jsonl").open(encoding="utf-8") as corpus:
        for i,payload,text,pilot,bad,reason,cluster,split in db.execute("SELECT * FROM (SELECT id,payload,text,pilot,contaminated,reason,cluster,split FROM records) ORDER BY id"):
            root = groups.find(i)
            if cluster != root:
                raise ValueError("Independent connected component differs")
            if pilot or reason in ("web_length","language","language_score","quality_score","invalid_record"):
                expected = "excluded"
            elif root in protected:
                expected = "excluded"
                if reason != "pilot_or_fixed_evaluation_cluster":
                    raise ValueError("Protected cluster was not excluded")
            elif duplicate_groups.find(i) != i:
                expected = "excluded"
                if reason != "normalized_exact_or_verified_near":
                    raise ValueError("Duplicate representative differs")
            else:
                value = int(digest(f'{c["seed"]}:expanded:{root}')[:16],16)%100
                expected = "train" if value<90 else "dev" if value<95 else "test"
                if reason is not None:
                    raise ValueError("Unexpected exclusion")
            if split != expected:
                raise ValueError("Independent deterministic cluster split differs")
            if split != "excluded":
                row = json.loads(payload)
                row.update(text=text,split=split,cluster_id=root)
                line = corpus.readline()
                if not line or json.loads(line) != row:
                    raise ValueError("Corpus differs from reconstructed retained records")
                if row["canonical_sha256"] in canonical_seen or clusters_by_split.setdefault(root,split) != split:
                    raise ValueError("Retained duplicate or split cluster contamination")
                canonical_seen.add(row["canonical_sha256"])
                splits[split] += 1
        if corpus.readline():
            raise ValueError("Unexpected extra corpus record")
    if dict(splits) != m["split_documents"]:
        raise ValueError("Split counts differ")
    db.close()
    del groups, duplicate_groups, canonical_seen, clusters_by_split, sketches
    tok = Tokenizer(ROOT/c["tokenizer"])
    shards = {s:Shard(output/"shards",s) for s in ("train","dev","test")}
    cursors, offsets, body_tokens, body_bytes = Counter(), Counter(), Counter(), Counter()
    with (output/"corpus.jsonl").open(encoding="utf-8") as stream:
        for number,line in enumerate(stream,1):
            row = json.loads(line)
            s, text = row["split"],row["text"]
            shard = shards[s]
            index = shard.index[cursors[s]]
            cursors[s] += 1
            body = tok.encode(text)
            encoded = np.asarray([2,*body,3],dtype="<u2")
            if tok.decode_bytes(body) != text.encode() or digest(text) != row["canonical_sha256"]:
                raise ValueError("Tokenizer round-trip or canonical hash failed")
            expected_index = {"doc_id":row["doc_id"],"split":s,"kind":"web","bucket":row["bucket"],
                              "canonical_sha256":row["canonical_sha256"],"offset":offsets[s],
                              "body_tokens":len(body),"bytes":len(text.encode())}
            if index != expected_index or not np.array_equal(shard.tokens[offsets[s]:offsets[s]+len(encoded)],encoded):
                raise ValueError("Full shard token/index reconstruction failed")
            offsets[s] += len(encoded)
            body_tokens[s] += len(body)
            body_bytes[s] += len(text.encode())
            if number % 10000 == 0:
                print(json.dumps({"stage":"all_shard_documents","documents":number,"seconds":time.perf_counter()-started}),flush=True)
    for s,shard in shards.items():
        details = shard.manifest["splits"][s]
        if cursors[s] != details["documents"] or offsets[s] != details["tokens"] or body_bytes[s] != details["body_bytes"]:
            raise ValueError("Shard count/byte/token denominator differs")
        if sha256(output/"corpus.jsonl") != shard.manifest["corpus_sha256"] or shard.manifest["tokenizer_sha256"] != c["tokenizer_sha256"]:
            raise ValueError("Shard source/Tokenizer binding differs")
    if offsets["train"] < c["minimum_train_stream_tokens"]:
        raise ValueError(f'Insufficient unique train stream tokens: {offsets["train"]}; frozen goal {c["minimum_train_stream_tokens"]}')
    report = {"status":"passed", "completed_at":now(),"raw_records_reconstructed":n-pilot_count,"pilot_protected":pilot_count,
              "dedup_edges":dict(edge_counts),"split_documents":dict(cursors),"stream_tokens":dict(offsets),
              "body_tokens":dict(body_tokens),"body_bytes":dict(body_bytes),"full_round_trip_documents":sum(cursors.values()),
              "all_checks": {k:True for k in ("pinned_raw_sha256", "source_and_terms_binding", "source_unchanged",
                  "all_raw_record_reconstruction", "all_signatures_recomputed", "all_detected_near_and_url_edges_rebuilt",
                  "cluster_split_disjoint", "normalized_exact_and_detected_near_dedup", "pilot_and_fixed_suite_cluster_exclusion",
                  "corpus_full_membership_and_payload", "all_shard_tokens_indexes_and_roundtrips", "500m_unique_train_stream_tokens")},
              "manifest_sha256":sha256(output/"manifest.json"),"elapsed_seconds":time.perf_counter()-started,
              "near_recall_limitation":m["near_scope"],"test_usage":"structural_integrity_only; no model evaluation or selection"}
    write_json(output/"corpus_audit.json",report)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--raw",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--workers",type=int,default=8)
    args=p.parse_args()
    record={"status":"running","pid":os.getpid(),"started_at":now(),
            "boot_id":Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
            "start_ticks":Path("/proc/self/stat").read_text().split()[21]}
    write_json(args.output/"audit_job.json",record)
    try:
        report=audit(args.raw,args.output,args.workers)
        record.update(status="complete",completed_at=now())
        print(json.dumps({"status":report["status"],"train_tokens":report["stream_tokens"]["train"]}),flush=True)
    except Exception as exc:
        record.update(status="failed",completed_at=now(),failure=f"{type(exc).__name__}: {exc}")
        raise
    finally:
        write_json(args.output/"audit_job.json",record)


if __name__ == "__main__":
    main()
