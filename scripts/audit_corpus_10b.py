"""Reconstruct the complete corpus/protection/edges and verify every emitted token."""
import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from jmicro.data import contaminated,digest,evaluation_patterns,normalized,overlap,shingles,url_key
from jmicro.expanded_data import Union,analyze_batch,bounded_map,signature
from jmicro.experiment import ROOT,now,sha256
from jmicro.corpus_state import read_json,write_json
from jmicro.large_corpus import band_order,batches,protected_rows,tokenize_batch
from jmicro.tokenizer import Tokenizer


def array_items(path):
    """Stream the generated one-object-per-line JSON array without loading it."""
    with path.open(encoding="utf-8") as stream:
        if stream.readline().strip()!="[":
            raise ValueError("Unexpected index framing")
        for line in stream:
            line=line.strip()
            if line=="]":
                if stream.read().strip():
                    raise ValueError("Index has trailing data")
                return
            if line:
                yield json.loads(line.rstrip(","))
        raise ValueError("Truncated index array")


def audit(config,raw,output,workers=16):
    started=time.monotonic()
    c=read_json(config)
    built=read_json(output/"manifest.json")
    artifact=Path(built["artifact_directory"])
    ingest=read_json(output/"ingest_complete.json")
    bindings=ingest["bindings"]
    if sha256(config)!=bindings["config"] or sha256(config)!=built["config_sha256"]:
        raise ValueError("Config binding differs")
    if sha256(raw/"acquisition.json")!=bindings["acquisition"]:
        raise ValueError("Acquisition binding differs")
    if sha256(Path(c["protected_corpus"]))!=bindings["protected"]:
        raise ValueError("Protected corpus changed")
    if sha256(ROOT/"data/phase1/processed/dataset_manifest.parquet")!=bindings["pilot"]:
        raise ValueError("Pilot changed")
    for path,expected in bindings["evaluation"].items():
        if sha256(ROOT/path)!=expected:
            raise ValueError("Fixed evaluation changed")
    for path,expected in bindings["code"].items():
        if hashlib.sha256((ROOT/path).read_bytes().replace(b"\r\n",b"\n")).hexdigest()!=expected:
            raise ValueError("Ingest code changed")
    source=read_json(raw/"sources.json")
    if source["config_sha256"]!=sha256(config) or sha256(raw/"README.upstream.md")!=source["evidence_sha256"]:
        raise ValueError("Pinned source conditions changed")
    db=sqlite3.connect(f'file:{output/"records.sqlite"}?mode=ro',uri=True)
    if db.execute("PRAGMA integrity_check").fetchone()[0]!="ok":
        raise ValueError("SQLite integrity failed")
    n=db.execute("SELECT count(*) FROM records").fetchone()[0]
    if n!=ingest["records"] or (output/"signatures.u32.bin").stat().st_size!=n*512:
        raise ValueError("Ingest count/signature size differs")
    sketches=np.memmap(output/"signatures.u32.bin",dtype="<u4",mode="r",shape=(n,128))
    groups,duplicates=Union(),Union()
    exact,urls={},{}
    protected=[]
    eligible=[]
    patterns=evaluation_patterns(read_json(ROOT/"configs/data/pilot.json"),ROOT)
    position=0
    all_records=db.execute("SELECT * FROM records ORDER BY id")

    def inspect(values,protect=False):
        nonlocal position
        row,text,canonical,normhash,reason,sketch=values
        i=position
        position+=1
        assert groups.add()==duplicates.add()==i
        actual=next(all_records,None)
        if actual is None:
            raise ValueError("Reconstructed row is absent")
        payload=json.loads(actual[1])
        key=url_key(row.get("url","")) if row.get("url") else ""
        bad=protect or (reason is None and contaminated({"text":text},patterns))
        if (actual[0],actual[2],actual[3],actual[4],actual[5],actual[6])!=(i,text,normhash,key,reason,int(bad)):
            raise ValueError("Source/filter/protection reconstruction differs")
        expected_payload=dict(doc_id=row["doc_id"],kind="web",bucket=c["bucket"],canonical_sha256=canonical,
                              source=c["source"],source_subset=c["subset"],revision=c["revision"],license=c["license"],
                              url=row.get("url",""),crawl_date=row.get("date"),quality_score=row.get("score"),
                              source_file=row.get("source_file"),source_row=row.get("source_row"),raw_sha256=row.get("raw_sha256"))
        if payload!=expected_payload:
            raise ValueError("Source payload reconstruction differs")
        expected_sketch=(sketch if sketch is not None else np.zeros(128)).astype(np.uint32)
        if not np.array_equal(expected_sketch,sketches[i]):
            raise ValueError("Signature reconstruction differs")
        if bad:
            protected.append(i)
        rep=i
        if reason is None:
            rep=exact.setdefault(normhash,i)
            groups.union(i,rep)
            duplicates.union(i,rep)
            if key:
                groups.union(i,urls.setdefault(key,i))
        use=reason is None and rep==i and sketch is not None
        if (actual[7],actual[8])!=(rep,int(use)):
            raise ValueError("Exact representative or sketch eligibility differs")
        if use:
            eligible.append(i)

    for row in protected_rows(c):
        text=row["text"]
        clean=normalized(text)
        inspect((row,text,digest(text),digest(clean),None,
                 signature(clean,c["seed"]) if len(clean)>=c["dedup"]["near_min_chars"] else None),True)
    protected_documents=position
    receipt=read_json(raw/"acquisition.json")
    for file in receipt["files"]:
        path=raw/Path(file["path"]).name
        if sha256(path)!=file["sha256"] or path.stat().st_size!=file["bytes"]:
            raise ValueError("Raw pinned checksum/size differs")
        with ProcessPoolExecutor(max_workers=workers) as executor:
            for batch in bounded_map(executor,analyze_batch,batches(path,file,c),workers*2):
                for values in batch:
                    inspect(values)
        progress={"stage":"audit_raw","file":path.name,"records":position,"seconds":time.monotonic()-started}
        write_json(output/"audit_progress.json",progress)
        print(json.dumps(progress),flush=True)
    if position!=n or next(all_records,None) is not None:
        raise ValueError("Complete raw membership differs")
    del exact,urls
    ids=np.asarray(eligible,dtype=np.uint32)
    del eligible

    @lru_cache(maxsize=4096)
    def features(i):
        return shingles(normalized(db.execute("SELECT text FROM records WHERE id=?",(int(i),)).fetchone()[0]),5)

    for band in range(32):
        ordered,bounds=band_order(sketches,ids,band)
        for a,b in zip(bounds[:-1],bounds[1:]):
            if b-a<2:
                continue
            members=ordered[a:b]
            for pos,i in enumerate(members):
                for j in members[:pos]:
                    if duplicates.find(i)!=duplicates.find(j) and overlap(features(int(i)),features(int(j)))>=.85:
                        groups.union(i,j)
                        duplicates.union(i,j)
        progress={"stage":"audit_edges","band":band,"seconds":time.monotonic()-started}
        write_json(output/"audit_progress.json",progress)
        print(json.dumps(progress),flush=True)
    actual_groups=np.load(output/"groups.npy",mmap_mode="r")
    actual_duplicates=np.load(output/"duplicates.npy",mmap_mode="r")
    for i in range(n):
        if groups.find(i)!=int(actual_groups[i]) or duplicates.find(i)!=int(actual_duplicates[i]):
            raise ValueError("Independent component/duplicate representative differs")
    protected_roots={groups.find(i) for i in protected}
    shard_manifest=read_json(artifact/"shards/manifest.json")
    if sha256(artifact/"corpus.jsonl")!=shard_manifest["corpus_sha256"]:
        raise ValueError("Corpus hash differs")
    if sha256(ROOT/c["tokenizer"])!=shard_manifest["tokenizer_sha256"] or shard_manifest["tokenizer_sha256"]!=c["tokenizer_sha256"]:
        raise ValueError("Tokenizer hash differs")
    tok=Tokenizer(ROOT/c["tokenizer"])
    byte_table=artifact/"shards/token_bytes.json"
    if (sha256(byte_table)!=shard_manifest["token_bytes_sha256"] or
        read_json(byte_table)!=[0 if i<8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)]):
        raise ValueError("Token byte accounting differs")
    for s,details in shard_manifest["splits"].items():
        if (sha256(artifact/f"shards/{s}.bin")!=details["stream_sha256"] or
            sha256(artifact/f"shards/{s}.index.json")!=details["index_sha256"]):
            raise ValueError("Shard/index checksum differs")
    streams={s:np.memmap(artifact/f"shards/{s}.bin",dtype="<u2",mode="r") for s in ("train","dev","test")}
    indexes={s:iter(array_items(artifact/f"shards/{s}.index.json")) for s in streams}
    counts={s:Counter(tokens=0,documents=0,body_bytes=0) for s in streams}
    corpus=(artifact/"corpus.jsonl").open(encoding="utf-8")
    expected_rows=[]
    for i,payload,text,reason,protect in db.execute("SELECT id,payload,text,reason,protected FROM records ORDER BY id"):
        root=groups.find(i)
        if reason is not None or protect or root in protected_roots or duplicates.find(i)!=i:
            continue
        value=int(digest(f'{c["seed"]}:expanded:{root}')[:16],16)%100
        s="train" if value<90 else "dev" if value<95 else "test"
        row=json.loads(payload)
        row.update(text=text,split=s,cluster_id=root,record_id=i)
        line=corpus.readline()
        if not line or json.loads(line)!=row:
            raise ValueError("Full retained membership/cluster split differs")
        expected_rows.append(row)
        if len(expected_rows)==128:
            verify_batch(expected_rows,ROOT/c["tokenizer"],indexes,streams,counts)
            expected_rows=[]
    if expected_rows:
        verify_batch(expected_rows,ROOT/c["tokenizer"],indexes,streams,counts)
    if corpus.readline():
        raise ValueError("Extra corpus records")
    corpus.close()
    for s,count in counts.items():
        if next(indexes[s],None) is not None or count["tokens"]!=len(streams[s]):
            raise ValueError("Extra index/token stream content")
        if (artifact/f"shards/{s}.bin").stat().st_size!=count["tokens"]*2:
            raise ValueError("Truncated or non-uint16 stream framing")
        if any(count[k]!=shard_manifest["splits"][s][k] for k in count):
            raise ValueError("Full shard accounting differs")
        if built["splits"][s]!=shard_manifest["splits"][s]:
            raise ValueError("Builder manifest differs")
    if counts["train"]["tokens"]<c["minimum_train_stream_tokens"]:
        raise ValueError("10B prepared train requirement not met")
    report={"status":"passed","completed_at":now(),"raw_records_reconstructed":n-protected_documents,
            "protected_documents":protected_documents,"splits":counts,"manifest_sha256":sha256(output/"manifest.json"),
            "artifact_directory":str(artifact),"elapsed_seconds":time.monotonic()-started,
            "checks":["all_pinned_raw_hashes","all_source_records_filters_payloads",
                      "all_signatures_recomputed","all_detected_near_url_exact_components_rebuilt",
                      "previous_heldout_pilot_fixed_suite_protected","all_corpus_membership_splits",
                      "all_tokenizer_roundtrips_stream_tokens_indexes_bytes","at_least_10b_train_stream_tokens"],
            "test_usage":"structural integrity only; no model evaluation/training",
            "near_scope":built["near_scope"]}
    write_json(output/"corpus_audit.json",report)
    db.close()
    return report


def verify_batch(rows,tokenizer,indexes,streams,counts):
    for row,encoded,body_tokens in tokenize_batch((rows,str(tokenizer))):
        s=row["split"]
        count=counts[s]
        index=next(indexes[s],None)
        expected=dict(doc_id=row["doc_id"],split=s,kind="web",bucket=row["bucket"],
                      canonical_sha256=row["canonical_sha256"],offset=count["tokens"],
                      body_tokens=body_tokens,bytes=len(row["text"].encode()))
        if index!=expected:
            raise ValueError("Full index reconstruction differs")
        if streams[s][count["tokens"]:count["tokens"]+body_tokens+2].tobytes()!=encoded:
            raise ValueError("Full stream reconstruction differs")
        count.update(tokens=body_tokens+2,documents=1,body_bytes=expected["bytes"])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config",type=Path,default=ROOT/"configs/phase6/corpus_10b.json")
    p.add_argument("--raw",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--workers",type=int,default=16)
    args=p.parse_args()
    record={"status":"running","pid":os.getpid(),"started_at":now(),
            "boot_id":Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
            "start_ticks":Path("/proc/self/stat").read_text().split()[21]}
    write_json(args.output/"audit_job.json",record)
    try:
        report=audit(args.config,args.raw,args.output,args.workers)
        record.update(status="complete",completed_at=now())
        print(json.dumps(report),flush=True)
    except Exception as exc:
        record.update(status="failed",completed_at=now(),failure=f"{type(exc).__name__}: {exc}")
        raise
    finally:
        write_json(args.output/"audit_job.json",record)
