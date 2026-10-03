from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import importlib.util
import json
import random
import shutil
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import pytest
from datasketch import MinHash, MinHashLSH

from jmicro.expanded_data import Union, bounded_map, permutations_for, signature
from jmicro.experiment import ROOT, read_json, sha256, write_json


def test_fast_signature_matches_scalar_hash_and_permutation_reference():
    text = "あいうえお日本語の文章。ABC😀123"
    hashes = []
    for i in range(len(text)-4):
        value = 0
        for char in text[i:i+5]:
            value = (value*1000003+ord(char)+1) & ((1 << 64)-1)
        value ^= value >> 33
        value = (value*0xff51afd7ed558ccd) & ((1 << 64)-1)
        value ^= value >> 33
        hashes.append(value & 0xffffffff)
    a, b = permutations_for(42)
    expected = np.array([min((((h*int(x)+int(y)) & ((1 << 64)-1)) % ((1 << 61)-1)) & 0xffffffff
                              for h in set(hashes)) for x,y in zip(a,b)], dtype=np.uint64)
    np.testing.assert_array_equal(signature(text), expected)
    np.testing.assert_array_equal(signature(text), signature(text))
    assert not np.array_equal(signature(text), signature(text, 43))


def test_near_candidate_and_cluster_transitivity():
    text = "これは日本語の文章です。毎日いろいろなことを学びます。"*10
    lsh = MinHashLSH(num_perm=128, params=(32,4))
    def mh(value):
        return MinHash(num_perm=128, seed=42, hashvalues=signature(value),
                       permutations=permutations_for(42), scheme="legacy")
    lsh.insert(0, mh(text))
    assert 0 in lsh.query(mh(text+"追加文章です。"))
    groups = Union()
    for _ in range(4):
        groups.add()
    groups.union(3,2)
    groups.union(1,0)
    groups.union(2,1)
    assert [groups.find(i) for i in range(4)] == [0,0,0,0]


def test_bounded_map_preserves_record_order():
    with ThreadPoolExecutor(max_workers=2) as executor:
        assert list(bounded_map(executor, abs, iter([-3,-1,-2]), pending=2)) == [3,1,2]


def test_expansion_full_pipeline_audit_and_corruption_rejection(tmp_path, monkeypatch):
    import jmicro.expanded_data as module
    # This is a tiny synthetic integrity fixture. It never substitutes for the
    # frozen real-world 500M corpus gate or a Japanese quality experiment.
    root=tmp_path/"fixture"
    c=read_json(ROOT/"configs/phase6/preparation.json")
    c["minimum_train_stream_tokens"]=1
    write_json(root/"configs/phase6/preparation.json",c)
    for relative in ["configs/data/pilot.json","eval/base.jsonl","eval/chat.jsonl",c["tokenizer"],
                     "src/jmicro/expanded_data.py","src/jmicro/data.py","src/jmicro/shards.py",
                     "src/jmicro/evaluation.py","src/jmicro/tokenizer.py","uv.lock"]:
        target=root/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/relative,target)
    old={"doc_id":"protected","kind":"web","status":"kept","split":"dev",
         "url":"https://fixture.example/protected","text":"この文章は昔の評価用です。毎日いろいろなことを学びます。"*4}
    pilot=root/"data/phase1/processed"
    pilot.mkdir(parents=True)
    (pilot/"corpus.jsonl").write_text(json.dumps(old,ensure_ascii=False)+"\n",encoding="utf-8")
    pq.write_table(pa.Table.from_pylist([old]),pilot/"dataset_manifest.parquet")
    rng=random.Random(42)
    chars=[chr(i) for i in range(0x3041,0x3096)]
    rows=[{"text":"".join(rng.choices(chars,k=100)),"language":"jpn","language_score":1.0,
           "score":3.0,"url":f"https://fixture.example/{i}"} for i in range(200)]
    rows[1]["url"]=rows[0]["url"]
    rows.append(dict(rows[0],text=old["text"],url=old["url"]))
    rows.append(dict(rows[2]))  # exact duplicate
    raw=tmp_path/"raw"
    raw.mkdir()
    file=raw/"train-00001-of-00283.parquet"
    pq.write_table(pa.Table.from_pylist(rows),file)
    (raw/"README.upstream.md").write_text("Synthetic fixture only",encoding="utf-8")
    write_json(raw/"sources.json",{"evidence_sha256":sha256(raw/"README.upstream.md")})
    write_json(raw/"acquisition.json",{"status":"complete","config_sha256":sha256(root/"configs/phase6/preparation.json"),
               "files":[{"path":file.name,"sha256":sha256(file),"bytes":file.stat().st_size}]})
    monkeypatch.setattr(module,"ROOT",root)
    output=tmp_path/"output"
    module.build(raw,output,workers=1)
    spec=importlib.util.spec_from_file_location("fixture_audit",ROOT/"scripts/audit_phase6_data.py")
    audit=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    monkeypatch.setattr(audit,"ROOT",root)
    report=audit.audit(raw,output,workers=1)
    assert report["status"]=="passed" and report["raw_records_reconstructed"]==202
    assert report["pilot_protected"]==1 and report["full_round_trip_documents"]==200
    assert report["stream_tokens"]["train"] < 500000000
    assert all(report["all_checks"].values())
    with (output/"signatures.bin").open("r+b") as stream:
        stream.write(b"corrupt!")
    with pytest.raises(ValueError,match="binding"):
        audit.audit(raw,output,workers=1)
