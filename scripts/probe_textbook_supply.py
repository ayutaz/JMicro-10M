"""One pinned train parquet only: native token supply and unreviewed examples.

Official validation/test are never acquired. Estimates concern this first train
file only, and include possible repeated source families. They are not new
prepared shards or evidence that the full16-file source is sufficiently good.
"""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import random
import shutil
import sys
import time
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT","60")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS","1")
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download,try_to_load_from_cache
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.larger_material_v3 import material_units
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive

DATA=Path("/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005")


def row_groups(lengths,selected):
    """Map uniform row IDs to row-group/local IDs without sampling group means."""
    bounds=np.cumsum([0,*lengths]);result={}
    for row in selected:
        assert 0<=row<bounds[-1]
        group=int(np.searchsorted(bounds,row,side="right")-1)
        result.setdefault(group,[]).append((row,int(row-bounds[group])))
    return result


def selected_units(row,tok):
    text=row["rewrite"]
    if not isinstance(text,str) or row["source_id"] is None:return [],0
    ids=tok.encode(text)
    if not 64<=len(ids)<=8192 or any(i<8 for i in ids):return [],len(ids)
    units=material_units(text,ids,"web",tok)
    family="textbook:"+hashlib.sha256(str(row["source_id"]).encode()).hexdigest()
    split="dev" if int(hashlib.sha256(family.encode()).hexdigest()[:8],16)%100==0 else "train"
    for unit in units:
        unit.update(source="textbook",source_family=family,split=split,
            source_id=row["source_id"],url=row["url"],prompt_type=row["prompt_type"])
    return units,len(ids)


def run(args):
    assert sys.version_info[:3]==(3,12,7) and 512<=args.draws<=2048 and 0<args.budget_seconds<=600
    source=read_json(DATA/"supply.json")["sources"]["KeisukeMiyamoto/SyntheticTextbook-jp"]
    assert source["repository"]=="KeisukeMiyamoto/SyntheticTextbook-jp" and source["revision"]=="f928b35fde6732f7d981860d32a18ef451cd539e"
    assert source["license"]=="apache-2.0" and sha256(Path(source["card_path"]))==source["card_sha256"]
    item=source["files"][0];assert item["path"]=="train-00000.parquet" and item["bytes"]<=300000000
    tok_path=ROOT/"artifacts/phase2/4096/tokenizer.model"
    expected=read_json(ROOT/"configs/phase6/amount_learning_comparison.json")["tokenizer_sha256"]
    assert sha256(tok_path)==expected
    files=("scripts/probe_textbook_supply.py","src/jmicro/larger_material_v3.py","src/jmicro/nested_material.py",
        "src/jmicro/complete_units.py","src/jmicro/coherent_units.py","src/jmicro/tokenizer.py")
    binding=dict(repository=source["repository"],revision=source["revision"],license=source["license"],
        file=item,card_sha256=source["card_sha256"],tokenizer_sha256=expected,draws=args.draws,seed=args.seed,
        CPU_wall_budget_seconds=args.budget_seconds,source_sha256={p:sha256(ROOT/p) for p in files},
        policy="One fixed official train file; verify actual acquisition SHA before reading; uniform row IDs, whole or intact first32 paragraphs with unchanged content filters; source_id family dev split",
        role="Fallback supply/content diagnosis while main2B CPU preparation runs; no recipe adoption, shards, GPU or full16-file download")
    output=args.output.resolve();assert output.is_relative_to(ROOT/"reports/phase6")
    output.mkdir(parents=True,exist_ok=True);job_path=output/"job.json"
    if job_path.exists():
        old=read_json(job_path);assert old["binding"]==binding and not alive(old)
        if old["status"]=="complete":print("Completed textbook pilot retained");return
        raise RuntimeError("Preserve failed bounded acquisition; no blind identical retries")
    start=time.monotonic();job=dict(status="running",**identity(),binding=binding,started_at=now())
    def heartbeat(stage,**values):
        if time.monotonic()-start>args.budget_seconds:raise TimeoutError("Bounded one-file textbook pilot exceeded CPU wall budget")
        job.update(stage=stage,heartbeat_at=now(),seconds=time.monotonic()-start,**values);atomic_json(job_path,job)
    try:
        heartbeat("acquire-one-pinned-train");atomic_json(output/"recipe.json",binding)
        for p in files:
            dest=output/"source"/p;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/p,dest)
        cached=try_to_load_from_cache(source["repository"],item["path"],revision=source["revision"],repo_type="dataset")
        path=Path(hf_hub_download(source["repository"],item["path"],revision=source["revision"],repo_type="dataset",token=False)).resolve()
        heartbeat("verify-first-acquisition",cached_before_acquisition=isinstance(cached,str))
        assert path.stat().st_size==item["bytes"] and sha256(path)==item["sha256"]
        parquet=pq.ParquetFile(path);schema=parquet.schema_arrow.names
        required=("source_id","url","prompt_type","rewrite");assert all(k in schema for k in required)
        count=parquet.metadata.num_rows;assert count>=args.draws
        rng=random.Random(args.seed);selected=rng.sample(range(count),args.draws)
        groups=row_groups([parquet.metadata.row_group(i).num_rows for i in range(parquet.metadata.num_row_groups)],selected)
        tok=Tokenizer(tok_path);draws=[];examples=[];seen_families=set();levels=Counter()
        for group,locations in groups.items():
            heartbeat("inspect-uniform-train-rows",completed_draws=len(draws))
            table=parquet.read_row_group(group,columns=list(required),use_threads=False)
            for row_number,local in locations:
                row=table.slice(local,1).to_pylist()[0];units,native=selected_units(row,tok)
                eligible=[u for u in units if u["split"]=="train"]
                teachers=sum(u["body_tokens"]+2 for u in eligible)
                draws.append(dict(row=row_number,native_body_tokens=native,eligible_train_tokens=teachers,
                    eligible_units=len(eligible),prompt_type=row["prompt_type"],source_id=row["source_id"]))
                levels[str(row["prompt_type"])]+=1
                if eligible and eligible[0]["source_family"] not in seen_families and len(examples)<32:
                    seen_families.add(eligible[0]["source_family"])
                    u=eligible[0]
                    examples.append({**{k:v for k,v in u.items() if k!="token_ids"},"source_row":row_number,
                        "original_rewrite_sha256":hashlib.sha256(row["rewrite"].encode()).hexdigest()})
        assert len(draws)==args.draws
        rates=np.asarray([d["eligible_train_tokens"] for d in draws],dtype=float)
        bootstrap=np.random.default_rng(args.seed).choice(rates,size=(2000,len(rates)),replace=True).mean(1)*count
        atomic_json(output/"draws.json",dict(binding=binding,rows=draws))
        atomic_json(output/"sample32.json",dict(binding=binding,examples=examples,
            selection="First32 distinct eligible sampled source_id train families in fixed group/row order; original paragraphs, not content reviewed"))
        result=dict(status="one_file_native_supply_and_unreviewed_content_complete",binding=binding,
            actual_cached_path=str(path),verified_actual_sha256=item["sha256"],file_rows=count,row_groups=parquet.metadata.num_row_groups,
            inspected_rows=len(draws),accepted_train_rows=int((rates>0).sum()),prompt_types=dict(levels),
            mean_native_body_tokens=float(np.mean([d["native_body_tokens"] for d in draws])),
            estimated_this_file_eligible_tokens=float(rates.mean()*count),this_file_bootstrap_ci95=np.quantile(bootstrap,[.025,.975]).tolist(),
            sample_examples=len(examples),new_acquired_bytes=0 if isinstance(cached,str) else item["bytes"],
            new_prepared_tokens=0,GPU_teacher_tokens=0,Base_adopted=False,Chat_adopted=False,
            protected_test_used=False,independent_human_blind=False,requested_five_steps_complete=False,
            limits="First train file only; estimates include duplicate source families and exclude neither protected prefixes nor global overlaps. Other15files/whole-source capacity, factual correctness and content acceptance unmeasured. Gemma counts are not native4k counts",
            CPU_wall_seconds=time.monotonic()-start,completed_at=now())
        atomic_json(output/"result.json",result);heartbeat("complete");job.update(status="complete",completed_at=now())
        print(json.dumps({k:v for k,v in result.items() if k!="binding"}),flush=True)
    except BaseException as error:job.update(status="failed",error=repr(error));raise
    finally:job["seconds"]=time.monotonic()-start;atomic_json(job_path,job)


if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);p.add_argument("--draws",type=int,default=1024)
    p.add_argument("--budget-seconds",type=float,default=600);p.add_argument("--seed",type=int,default=2026100623)
    run(p.parse_args())
