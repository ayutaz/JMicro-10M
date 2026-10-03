"""Integrity checks for the scalable pipeline, not real-data quality evidence."""
import json
import importlib.util
from pathlib import Path
import random
import shutil

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import pytest
from datasketch import MinHash, MinHashLSH

from jmicro.expanded_data import permutations_for, signature
from jmicro.experiment import ROOT, read_json, sha256, write_json
from jmicro.large_corpus import Groups, band_order


def test_external_band_candidates_equal_frozen_lsh():
    texts = ["日本語の文章を読みながら様々なことを学ぶ日々です。"*8,
             "日本語の文章を読みながら様々なことを学ぶ日々です。"*8+"今日は晴れ。",
             "全く違う内容として科学技術と地域経済について説明しています。"*5]
    sketches = np.asarray([signature(t) for t in texts],dtype=np.uint32)
    ids = np.arange(len(texts),dtype=np.uint32)
    external=set()
    for band in range(32):
        ordered,bounds=band_order(sketches,ids,band)
        for a,b in zip(bounds[:-1],bounds[1:]):
            members=ordered[a:b]
            external.update(tuple(sorted((int(i),int(j)))) for i in members for j in members if i!=j)
    lsh=MinHashLSH(num_perm=128,params=(32,4))
    expected=set()
    for i,sketch in enumerate(sketches):
        mh=MinHash(num_perm=128,seed=42,hashvalues=sketch.astype(np.uint64),
                   permutations=permutations_for(42),scheme="legacy")
        expected.update((j,i) for j in lsh.query(mh))
        lsh.insert(i,mh)
    assert external==expected and (0,1) in external


def test_groups_preserve_minimum_transitive_representative():
    g=Groups(6)
    for a,b in [(5,4),(3,2),(4,3),(2,1)]:
        g.union(a,b)
    assert [g.find(i) for i in range(6)]==[0,1,1,1,1,1]


def test_restartable_ingest_protects_previous_heldout_and_exports_losslessly(tmp_path,monkeypatch):
    import jmicro.large_corpus as module
    import jmicro.expanded_data as original
    from jmicro.shards import Shard
    from jmicro.tokenizer import Tokenizer
    root=tmp_path/"root"
    c=read_json(ROOT/"configs/phase6/corpus_10b.json")
    for relative in ["configs/data/pilot.json","eval/base.jsonl","eval/chat.jsonl",c["tokenizer"],
                     "src/jmicro/large_corpus.py","src/jmicro/corpus_state.py","src/jmicro/expanded_data.py","src/jmicro/data.py",
                     "src/jmicro/tokenizer.py","uv.lock"]:
        target=root/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/relative,target)
    protected={"doc_id":"previous-dev","kind":"web","status":"kept","split":"dev",
               "text":"以前の評価に使われた日本語の文章です。"+"".join(
                   random.Random(7).choices([chr(i) for i in range(0x3041,0x3096)],k=500)),
               "url":"https://example.test/heldout"}
    previous=tmp_path/"previous.jsonl"
    previous.write_text(json.dumps(protected,ensure_ascii=False)+"\n",encoding="utf-8")
    c.update(protected_corpus=str(previous),protected_corpus_sha256=sha256(previous),minimum_train_stream_tokens=1)
    pilot=root/"data/phase1/processed"
    pilot.mkdir(parents=True)
    pq.write_table(pa.Table.from_pylist([dict(protected,doc_id="pilot-dev")]),pilot/"dataset_manifest.parquet")
    config=tmp_path/"config.json"
    write_json(config,c)
    rng=random.Random(42)
    rows=[dict(text="".join(rng.choices([chr(i) for i in range(0x3041,0x3096)],k=100)),
               language="jpn",language_score=1.,score=3.,url=f"https://example.test/{i}") for i in range(150)]
    rows.extend([dict(rows[0]),dict(rows[1],text=protected["text"],url=protected["url"]),
                 dict(rows[2],text=protected["text"]+"少しの追記です。",url="https://example.test/near-heldout")])
    raw=tmp_path/"raw"
    raw.mkdir()
    file=raw/"train-00001-of-00283.parquet"
    pq.write_table(pa.Table.from_pylist(rows),file)
    write_json(raw/"acquisition.json",{"status":"complete","config_sha256":sha256(config),
               "files":[{"path":file.name,"sha256":sha256(file),"bytes":file.stat().st_size}]})
    (raw/"README.upstream.md").write_text("Synthetic fixture only",encoding="utf-8")
    write_json(raw/"sources.json",{"config_sha256":sha256(config),"evidence_sha256":sha256(raw/"README.upstream.md")})
    monkeypatch.setattr(module,"ROOT",root)
    monkeypatch.setattr(original,"ROOT",root)
    output=tmp_path/"output"
    n=module.ingest(config,raw,output,workers=1)
    assert n==155
    sig=output/"signatures.u32.bin"
    expected=sha256(sig)
    with sig.open("ab") as stream:
        stream.write(b"uncommitted crash residue")
    assert module.ingest(config,raw,output,workers=1)==n
    assert sha256(sig)==expected
    module.deduplicate(output)
    parents=sha256(output/"groups.npy")
    module.deduplicate(output)
    assert sha256(output/"groups.npy")==parents
    from jmicro.parallel_corpus_dedup import parallel_components
    parallel=tmp_path/"parallel"
    parallel_components(output,parallel,n,workers=2)
    np.testing.assert_array_equal(np.load(parallel/"groups.npy"),np.load(output/"groups.npy"))
    np.testing.assert_array_equal(np.load(parallel/"duplicates.npy"),np.load(output/"duplicates.npy"))
    edge_hash=sha256(parallel/"band-00.edges.npy")
    parallel_components(output,parallel,n,workers=2)
    assert sha256(parallel/"band-00.edges.npy")==edge_hash
    result=module.export(config,output,workers=1)
    assert result["target_met"]
    artifact=Path(result["artifact_directory"])
    retained=[json.loads(line) for line in (artifact/"corpus.jsonl").read_text().splitlines()]
    assert len(retained)==150
    assert not any("以前の評価" in r["text"] for r in retained)
    tokenizer=Tokenizer(root/c["tokenizer"])
    for split in ("train","dev","test"):
        shard=Shard(artifact/"shards",split)
        for index,row in zip(shard.index,[r for r in retained if r["split"]==split]):
            start=index["offset"]
            ids=shard.tokens[start:start+index["body_tokens"]+2].tolist()
            assert ids[0]==2 and ids[-1]==3 and tokenizer.decode(ids[1:-1])==row["text"]
    spec=importlib.util.spec_from_file_location("large_fixture_audit",ROOT/"scripts/audit_corpus_10b.py")
    auditor=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(auditor)
    monkeypatch.setattr(auditor,"ROOT",root)
    report=auditor.audit(config,raw,output,workers=1)
    assert report["status"]=="passed" and report["raw_records_reconstructed"]==153
    from jmicro.cached_corpus_audit import audit_with_cache
    original_decorator=auditor.lru_cache
    cached_report=audit_with_cache(auditor,config,raw,output,workers=1)
    assert auditor.lru_cache is original_decorator
    assert cached_report["checks"]==report["checks"]
    assert cached_report["splits"]==report["splits"]
    assert read_json(output/"audit_cache_metrics.json")["feature_cache"]["max_charged_bytes"]==2*1024**3
    spec=importlib.util.spec_from_file_location("fixture_ready",ROOT/"scripts/check_corpus_10b_ready.py")
    ready=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ready)
    monkeypatch.setattr(ready,"ROOT",root)
    terminal={"status":"complete","pid":2147483647,"boot_id":"synthetic-nonlive","start_ticks":"0"}
    write_json(output/"job.json",terminal)
    actual_loader=ready.check(config,output,output/"ready.json")
    assert actual_loader["status"]=="passed_actual_training_loader" and actual_loader["sampler_replay_exact"]
    write_json(output/"job.json",dict(terminal,status="running"))
    with pytest.raises(ValueError,match="not completed"):
        ready.check(config,output,output/"refused.json")
    write_json(output/"job.json",terminal)
    saved_audit=read_json(output/"corpus_audit.json")
    write_json(output/"corpus_audit.json",dict(saved_audit,status="failed"))
    with pytest.raises(ValueError,match="binding"):
        ready.check(config,output,output/"refused.json")
    write_json(output/"corpus_audit.json",saved_audit)
    with (artifact/"shards/train.bin").open("r+b") as stream:
        stream.write(b"bad!")
    with pytest.raises(ValueError,match="checksum"):
        auditor.audit(config,raw,output,workers=1)
    with pytest.raises(ValueError,match="checksum"):
        audit_with_cache(auditor,config,raw,output,workers=1)
    assert auditor.lru_cache is original_decorator
