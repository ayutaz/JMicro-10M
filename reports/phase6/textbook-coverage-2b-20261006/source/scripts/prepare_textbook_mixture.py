"""Recompose matched500M/2B Web75/textbook20/story5 without a Web rescan.

The previous95/5 cache failed content acceptance. Reusing its original units
does not accept it: exclude all inspected families and review a new fixed64.
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
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.larger_material import FourGroups
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive, identity
import prepare_larger_material_v3 as original

DATA = Path("/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006")
RUN = ROOT/"reports/phase6/textbook-mixture-20261006"
OLD = Path("/home/aihub_ubuntu/jmicro-data/phase6/larger-material-20261006-95web-v3")
TEXTBOOK = Path("/home/aihub_ubuntu/jmicro-data/phase6/textbook-component-20261006")
TARGETS = dict(web=375000000, textbook=100000000, story=25000000)
QUOTAS = dict(web=24, textbook=24, story=16)
SEED, BUDGET = 2026100632, 900


def cached_groups(large_path, small_path):
    """Read every original4-group and its one actual nested selection once."""
    with Path(large_path).open() as large, Path(small_path).open() as small:
        for small_line in small:
            choice = json.loads(small_line)
            members = []
            for _ in range(4):
                line = large.readline()
                assert line, "Incomplete original4-group"
                members.append(json.loads(line))
            assert len({r["doc_id"] for r in members}) == 4
            assert len({(r["source"], r["body_tokens"], r["unit_kind"]) for r in members}) == 1
            matches = [i for i,r in enumerate(members) if r["doc_id"] == choice["doc_id"]]
            assert len(matches) == 1
            selected = members[matches[0]]
            assert all(selected[k] == choice[k] for k in ("canonical_sha256", "source_family", "body_tokens", "source", "unit_kind"))
            yield members, matches[0]
        assert not large.readline(), "Extra large cache groups"


def prepare():
    old_ready, textbook_ready = read_json(OLD/"ready.json"), read_json(TEXTBOOK/"ready.json")
    for run, ready, ceiling in ((ROOT/"reports/phase6/larger-material-20261006-95web-v3",old_ready,1800),
            (ROOT/"reports/phase6/textbook-component-20261006",textbook_ready,1800)):
        job = read_json(run/("prepare-job.json" if run.name.startswith("larger-") else "job.json"))
        assert job["status"] == "complete" and not alive(job) and job["seconds"] <= ceiling
        assert job["binding"] == ready["binding"]
    inspected = read_json(OLD/"sample64.json")
    assert sha256(OLD/"sample64.json") == old_ready["sample_sha256"]
    excluded = {r["source_family"] for r in inspected}
    tokenizer = ROOT/"artifacts/phase2/4096/tokenizer.model"
    token_sha = sha256(tokenizer)
    assert token_sha == old_ready["binding"]["tokenizer_sha256"] == textbook_ready["binding"]["tokenizer_sha256"]
    sources = {"web":old_ready, "textbook":textbook_ready}
    for ready in sources.values():
        for name in ("small", "large"):
            ref=ready["pools"][name]
            assert sha256(Path(ref["pool"])/"manifest.json") == ref["manifest_sha256"]
    story_ref=old_ready["binding"]["sources"]["story"]
    code = ("scripts/prepare_textbook_mixture.py", "scripts/prepare_textbook_mixture.ps1",
        "scripts/prepare_larger_material_v3.py", "scripts/prepare_complete_units.py",
        "src/jmicro/larger_material_v3.py", "src/jmicro/larger_material.py",
        "src/jmicro/nested_material.py", "src/jmicro/nested_material_v2.py",
        "src/jmicro/tokenizer.py", "src/jmicro/eos_pilot.py")
    binding = dict(seed=SEED, CPU_budget_seconds=BUDGET, workers=8, small_targets=TARGETS,
        source_ratio=dict(web=.75,textbook=.20,story=.05), exact_large_to_small_ratio=4,
        tokenizer_sha256=token_sha, source_sha256={p:sha256(ROOT/p) for p in code},
        old_cache_ready_sha256=sha256(OLD/"ready.json"), textbook_component_ready_sha256=sha256(TEXTBOOK/"ready.json"),
        inspected64_family_exclusion_sha256=sha256(OLD/"sample64.json"), fixed_content_sample_quotas=QUOTAS,
        policy="Original cached Web groups and new textbook groups, unchanged body IDs; new source-train whole stories; skip any group containing an inspected family or canonical duplicate; preserve exact4 source/length/unit/EOS histograms",
        limitations="Previous Web cache rejected, not accepted material; synthetic facts/global original-Web overlap unverified; new fixed64 weak<=10 required before matched1B teachers; no GPU")
    RUN.mkdir(parents=True,exist_ok=True); DATA.mkdir(parents=True,exist_ok=True)
    job_path=RUN/"job.json"
    if job_path.exists():
        job=read_json(job_path); assert job["binding"] == binding and not alive(job)
        if job["status"] == "complete": print("Completed mixture retained",flush=True); return
        raise RuntimeError("Preserve failed mixture; no blind retry")
    assert not any(DATA.iterdir())
    start=time.monotonic(); job=dict(status="running",**identity(),binding=binding,started_at=now())
    totals, counts, offsets, documents, body_bytes=Counter(),Counter(),Counter(),Counter(),Counter()
    handles,indexes={},{}; hist={n:Counter() for n in ("small","large")}
    samples={s:[] for s in TARGETS}; draws=Counter(); rng=random.Random(SEED+1); seen=set()
    protected=[]
    for suite in ("eval/base.jsonl","eval/japanese_semantics_v2_1.jsonl"):
        for line in (ROOT/suite).read_text().splitlines():
            row=json.loads(line)
            if row.get("split","dev")=="dev":
                protected.extend(row[k] for k in ("prefix","context") if isinstance(row.get(k),str) and len(row[k])>=12)
    def heartbeat(stage):
        job.update(stage=stage,heartbeat_at=now(),seconds=time.monotonic()-start,
            counts=dict(counts),prepared_tokens=dict(totals)); atomic_json(job_path,job)
        if job["seconds"] > BUDGET: raise TimeoutError("900s recomposition cap exhausted; partials not ready")
    try:
        heartbeat("setup"); write_json(RUN/"recipe.json",binding)
        for p in code:
            dest=RUN/"source"/p;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/p,dest)
        for name in hist:
            folder=DATA/name;folder.mkdir()
            handles[name]=(folder/"train.partial.bin").open("wb")
            indexes[name]=(folder/"train.index.partial.jsonl").open("w")
        def append(name, unit, ids):
            row={k:v for k,v in unit.items() if k not in ("text","token_ids")}
            row.update(offset=offsets[name],split="train",doc_id="mixture-"+unit["canonical_sha256"][:24])
            assert len(ids)==unit["body_tokens"]+2 and ids[0]==2 and ids[-1]==3
            handles[name].write(np.asarray(ids,dtype="<u2").tobytes())
            indexes[name].write(json.dumps(row,ensure_ascii=False)+"\n")
            offsets[name]+=len(ids);totals[name+"_"+unit["source"]]+=len(ids)
            documents[name]+=1;body_bytes[name]+=row["bytes"]
            hist[name][unit["source"]+":"+str(unit["body_tokens"])+":"+unit["unit_kind"]]+=1
            if name=="large":
                source=unit["source"];draws[source]+=1;selection=samples[source]
                entry=dict(row)
                if len(selection)<QUOTAS[source]:
                    selection.append(dict(entry,_ids=ids.tolist()))
                else:
                    slot=rng.randrange(draws[source])
                    if slot<QUOTAS[source]: selection[slot]=dict(entry,_ids=ids.tolist())
        for source, ready in sources.items():
            large=Path(ready["pools"]["large"]["pool"]);small=Path(ready["pools"]["small"]["pool"])
            tokens=np.memmap(large/"train.bin",dtype="<u2",mode="r")
            assert len(tokens)==ready["pools"]["large"]["splits"]["train"]["tokens"]
            heartbeat("copy-"+source);last=time.monotonic()
            for members,slot in cached_groups(large/"train.index.jsonl",small/"train.index.jsonl"):
                if members[0]["source"] != source: continue
                digests={r["canonical_sha256"] for r in members}
                if any(r["source_family"] in excluded for r in members) or digests & seen:
                    counts["group_excluded_"+source]+=1;continue
                seen.update(digests)
                for i,row in enumerate(members):
                    unit=dict(row,cache_pool=str(large),cache_offset=row["offset"])
                    ids=tokens[row["offset"]:row["offset"]+row["body_tokens"]+2]
                    append("large",unit,ids)
                    if i==slot:append("small",unit,ids)
                if time.monotonic()-last>5:heartbeat("copy-"+source);last=time.monotonic()
                if totals["small_"+source]>=TARGETS[source]:break
            assert totals["small_"+source]>=TARGETS[source],dict(totals)
            del tokens
        heartbeat("story-setup")
        story=TrainView(story_ref["pool"],story_ref["manifest_sha256"]); groups=FourGroups(SEED)
        with mp.get_context("fork").Pool(8,initializer=original.decode.worker_init,
                initargs=(str(tokenizer),str(story.directory/"train.bin"))) as workers:
            last=time.monotonic()
            for units in workers.imap(original.worker,original.batches(story,"story",lambda: heartbeat("story-scan"),counts),chunksize=1):
                for unit in units:
                    if (unit["split"]!="train" or unit["source_family"] in excluded or
                            unit["canonical_sha256"] in seen or any(p in unit["text"] for p in protected)):continue
                    seen.add(unit["canonical_sha256"]);group=groups.add(unit)
                    if group:
                        members,slot=group
                        for i,row in enumerate(members):
                            row=dict(row,bytes=len(row["text"].encode()),source_manifest_sha256=story_ref["manifest_sha256"])
                            ids=story.tokens[row["source_start"]:row["source_end"]+1]
                            append("large",row,ids)
                            if i==slot:append("small",row,ids)
                    if totals["small_story"]>=TARGETS["story"]:break
                if time.monotonic()-last>5:heartbeat("story-extract");last=time.monotonic()
                if totals["small_story"]>=TARGETS["story"]:break
            workers.terminate()
        assert totals["small_story"]>=TARGETS["story"],dict(totals)
        assert offsets["large"]==4*offsets["small"] and documents["large"]==4*documents["small"]
        assert hist["large"]==Counter({k:4*v for k,v in hist["small"].items()})
        pools={}
        for name in hist:
            for handle in (handles[name],indexes[name]):handle.flush();os.fsync(handle.fileno());handle.close()
            folder=DATA/name
            os.replace(folder/"train.partial.bin",folder/"train.bin");os.replace(folder/"train.index.partial.jsonl",folder/"train.index.jsonl")
            shutil.copyfile(OLD/"large/token_bytes.json",folder/"token_bytes.json")
            manifest=dict(version=1,dtype="<u2",kind="web",vocab_size=4096,tokenizer_sha256=token_sha,
                token_bytes_sha256=sha256(folder/"token_bytes.json"),binding=binding,
                packing="Native unchanged original complete bodies/paragraphs; three provenance sources; BOS masked",
                splits=dict(train=dict(tokens=offsets[name],documents=documents[name],body_bytes=body_bytes[name],
                    stream_sha256=sha256(folder/"train.bin"),index_sha256=sha256(folder/"train.index.jsonl"),index_format="jsonl")))
            write_json(folder/"manifest.json",manifest)
            pools[name]=dict(pool=str(folder),manifest_sha256=sha256(folder/"manifest.json"),splits=manifest["splits"])
        tok=Tokenizer(tokenizer);sample=[]
        for source,quota in QUOTAS.items():
            assert len(samples[source])==quota
            for row in samples[source]:
                ids=row.pop("_ids");row["text"]=tok.decode(ids[1:-1]);sample.append(row)
        write_json(DATA/"sample64.json",sample)
        ready=dict(status="prepared_pending_fixed_content_review",binding=binding,pools=pools,
            prepared_tokens=dict(totals),histograms={k:dict(v) for k,v in hist.items()},sample_sha256=sha256(DATA/"sample64.json"),
            nested_ratio_exact=4,small_subset_of_large=True,source_length_EOS_histograms_exact_ratio=True,
            editorial_unit_histograms_exact_ratio=True,CPU_seconds=time.monotonic()-start,
            protected_test_used=False,Base_adopted=False,GPU_teacher_tokens=0,created_at=now())
        heartbeat("finalize");write_json(DATA/"ready.json",ready);write_json(RUN/"ready.json",ready)
        job.update(status="complete",completed_at=now());print(json.dumps(dict(status=ready["status"],tokens=dict(totals))),flush=True)
    except BaseException as error:job.update(status="failed",error=repr(error));raise
    finally:
        for handle in (*handles.values(),*indexes.values()):
            if not handle.closed:handle.close()
        job["seconds"]=time.monotonic()-start;atomic_json(job_path,job)


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    prepare()
