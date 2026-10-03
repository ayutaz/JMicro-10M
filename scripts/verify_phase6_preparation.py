"""Persistent real CUDA WSD/decay CLI verification. Run through pinned uv."""
from pathlib import Path
import argparse
import fcntl
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.phase5 import equal_state
from jmicro.shards import Shard
from jmicro.training import (Trainer, evaluate_body, gpu_lock, implementation_hashes,
                             isolated_evaluation, learning_rate_factor, rng_state, source_snapshot)


def verify(output, shards, job):
    c=read_json(ROOT/"configs/phase6/preparation.json")
    v=c["verification"]
    candidate=read_json(ROOT/"reports/phase5/candidate_configs.json")["100m-no-qknorm"]
    if sha256(Path(candidate["checkpoint"])) != candidate["checkpoint_sha256"]:
        raise ValueError("Selected Phase 5 artifact differs")
    model_file=output/"selected_model.json"
    if model_file.exists() and read_json(model_file) != candidate["model_config"]:
        raise ValueError("Selected architecture changed")
    write_json(model_file,candidate["model_config"])
    common=[sys.executable,str(ROOT/"scripts/train.py"),"train","--model",str(model_file),"--shards",str(shards),
            "--device","cuda","--dtype",v["dtype"],"--backend",v["backend"],"--phase","6",
            "--context",str(v["context"]),"--batch",str(v["batch"]),"--accumulation",str(v["accumulation"]),
            "--lr",str(v["lr"]),"--warmup",str(v["warmup"]),"--seed",str(c["seed"]),
            "--scheduler","wsd","--save-every","50","--log-every","20","--schedule-updates","200"]
    parent=output/"stable-resumed/checkpoint-00000100.pt"
    branch=["--branch-from",str(parent),"--decay-updates",str(v["decay_updates"]),
            "--minimum-lr-ratio",str(v["minimum_lr_ratio"])]
    stages=[("stable-continuous",[],200),
            ("stable-resumed",["--stop-after","100"],100),
            ("decay-continuous",branch,200),
            ("decay-resumed",[*branch,"--stop-after","150"],150),
            ("decay-resumed",["--resume",str(output/"decay-resumed/checkpoint-00000150.pt")],200),
            ("stable-resumed",["--resume",str(parent)],200)]
    frozen_parent=None
    for index,(name,extra,end) in enumerate(stages):
        run=output/name
        if index==2:
            frozen_parent={p.name:sha256(p) for p in (parent,parent.parent/"metrics.jsonl",parent.parent/"run.json",parent.parent/"latest.json")}
            if not (output/"stable_before_branches.json").exists():
                write_json(output/"stable_before_branches.json",frozen_parent)
        if index==5 and not (output/"branch_isolation.json").exists():
            current={p.name:sha256(p) for p in (parent,parent.parent/"metrics.jsonl",parent.parent/"run.json",parent.parent/"latest.json")}
            if current != read_json(output/"stable_before_branches.json"):
                raise ValueError("Decay branches mutated stable checkpoint/metrics/run/latest")
            write_json(output/"branch_isolation.json",{"passed":True,"unchanged_sha256":current,"verified_at":now()})
        record=read_json(run/"run.json") if (run/"run.json").exists() else None
        if record and record["update"] >= end and record["status"] in ("complete","paused"):
            continue
        command=[*common,"--output",str(run),*extra]
        if record:
            latest=read_json(run/"latest.json")
            checkpoint=Path(latest["path"])
            if sha256(checkpoint) != latest["sha256"]:
                raise ValueError("Persistent checkpoint checksum differs")
            # Resume an interrupted stage from its own completed update, using
            # the original branch spec rather than branching for a second time.
            command=[*common,"--output",str(run),"--resume",str(checkpoint),"--stop-after",str(end)]
        job.update(status="running",stage=index,active_run=name,command=command)
        write_json(output/"job.json",job)
        with (output/f"stage-{index:02d}.log").open("a",buffering=1) as log:
            child=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT)
            job.update(worker_pid=child.pid)
            if Path(f"/proc/{child.pid}/stat").exists():
                job["worker_start_ticks"]=Path(f"/proc/{child.pid}/stat").read_text().split()[21]
            write_json(output/"job.json",job)
            print(json.dumps({"stage":index,"run":name,"worker_pid":child.pid,"status":"running"}),flush=True)
            while child.poll() is None:
                time.sleep(5)
                job["heartbeat_at"]=now()
                write_json(output/"job.json",job)
            if child.returncode:
                raise RuntimeError(f"Verification worker {name} failed: {child.returncode}; see stage-{index:02d}.log")
        print(json.dumps({"stage":index,"run":name,"status":"passed"}),flush=True)
    checks={}
    fields=("model","optimizer","scheduler","rng","sampler","tokens","supervised_tokens","body_bytes",
            "token_digest","spec","model_config","implementation_sha256","update")
    metrics={name:[json.loads(line) for line in (output/name/"metrics.jsonl").read_text().splitlines()]
             for name in ("stable-continuous","stable-resumed","decay-continuous","decay-resumed")}
    checkpoints={}
    for prefix,a,b,count in [("stable","stable-continuous","stable-resumed",200),("decay","decay-continuous","decay-resumed",100)]:
        states=[torch.load(output/name/"checkpoint-00000200.pt",map_location="cpu",weights_only=False) for name in (a,b)]
        for field in fields:
            checks[f"{prefix}_{field}_exact"]=equal_state(states[0][field],states[1][field])
        if prefix=="decay":
            for field in ("lineage","branch_updates","branch_tokens"):
                checks[f"{prefix}_{field}_exact"]=equal_state(states[0][field],states[1][field])
            checks["branch_budget_accounted"]=(states[0]["branch_updates"]==100 and states[0]["branch_tokens"]==819200
                                                and states[0]["lineage"]["parent_sha256"]==sha256(parent))
        checks[prefix+"_metrics_complete"]=len(metrics[a])==len(metrics[b])==count
        for field in ("update","loss","lr","gradient_norm","tokens_seen","supervised_tokens","body_bytes_seen","token_digest"):
            checks[f"{prefix}_{field}_history_exact"]=[r[field] for r in metrics[a]]==[r[field] for r in metrics[b]]
        checks[prefix+"_lr_matches_frozen_schedule"]=all(r["lr"]==v["lr"]*learning_rate_factor(states[0]["spec"],r["update"]-1) for r in metrics[a])
        for name in (a,b):
            state=torch.load(output/name/"checkpoint-00000200.pt",map_location="cpu",weights_only=False)
            latest=read_json(output/name/"latest.json")
            checks[name+"_latest_sha256"]=latest["sha256"]==sha256(Path(latest["path"]))
            checks[name+"_completed"]=read_json(output/name/"run.json")["status"]=="complete"
            checks[name+"_finite_weights"]=all(torch.isfinite(t).all().item() for t in state["model"].values())
            checks[name+"_finite_optimizer"]=all(torch.isfinite(t).all().item() for row in state["optimizer"]["state"].values() for t in row.values() if isinstance(t,torch.Tensor))
            checkpoints[name]={"path":str((output/name/"checkpoint-00000200.pt").resolve()),"sha256":sha256(output/name/"checkpoint-00000200.pt")}
    checks["stable_parent_not_mutated"]=sha256(parent)==read_json(output/"stable_before_branches.json")[parent.name]
    checks["stable_run_unchanged_during_branches"]=read_json(output/"branch_isolation.json")["passed"]
    checks["selected_no_norm_architecture"]=candidate["model_config"]["qk_norm_type"]=="none"
    checks["cuda_bf16"]=torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    with gpu_lock("cuda"):
        stable_state=torch.load(output/"stable-continuous/checkpoint-00000200.pt",map_location="cpu",weights_only=False)
        trainer=Trainer(candidate["model_config"],Shard(shards),stable_state["spec"],"cuda")
        trainer.load(output/"stable-continuous/checkpoint-00000200.pt")
        before_rng=rng_state()
        before_model={k:t.clone() for k,t in trainer.model.state_dict().items()}
        with isolated_evaluation(trainer.model):
            torch.rand(8,device="cuda")
            torch.rand(8)
        body=evaluate_body(trainer.model,Shard(shards,"dev"),"cuda","bf16",limit=4)
        checks["cuda_evaluation_rng_and_mode_preserved"]=equal_state(before_rng,rng_state()) and trainer.model.training
        checks["cuda_evaluation_model_preserved"]=equal_state(before_model,trainer.model.state_dict())
        checks["cuda_evaluation_actual_dev"]=body["documents"]==4 and body["body_bytes"]>0
        write_json(output/"evaluation_isolation.json",{"scope":"integrity only; not Base quality", "body":body,
                   "rng_and_model_preserved":checks["cuda_evaluation_rng_and_mode_preserved"] and checks["cuda_evaluation_model_preserved"]})
    report={"status":"passed_exact" if all(checks.values()) else "failed","checks":checks,
            "scope":"Phase6 steps 1-2 CUDA preparation; no scaling/quality claim","device":"cuda","dtype":v["dtype"],
            "verification":v,"config_sha256":sha256(ROOT/"configs/phase6/preparation.json"),
            "implementation_sha256":implementation_hashes(),"shard_manifest_sha256":sha256(shards/"manifest.json"),
            "checkpoint_sha256":checkpoints,"stable_updates":200,"decay_updates":100,
            "stable_tokens_per_run":1638400,"decay_extra_tokens_per_run":819200,
            "completed_at":now(),"commands":read_json(output/"commands.json")}
    write_json(output/"wsd_resume_report.json",report)
    if not all(checks.values()):
        raise ValueError(f"CUDA exact verification failed: {[k for k,v in checks.items() if not v]}")
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--shards",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    torch.set_num_threads(2)
    job={"pid":os.getpid(),"boot_id":Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
         "start_ticks":Path("/proc/self/stat").read_text().split()[21],"started_at":now(),"status":"running"}
    lock=args.output.parent/"phase6-preparation.lock"
    with lock.open("a+") as stream:
        fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if not (args.output/"snapshot").exists():
            write_json(args.output/"source_sha256.json",source_snapshot(args.output/"snapshot"))
        write_json(args.output/"commands.json",{"start_and_supervisor_restart":["uv","run","--frozen","--extra","hub","--extra","data","--extra","ml","--extra","export","scripts/verify_phase6_preparation.py","--shards",str(args.shards),"--output",str(args.output)]})
        write_json(args.output/"job.json",job)
        try:
            report=verify(args.output,args.shards,job)
            job.update(status="complete",completed_at=now(),worker_pid=None)
            print(json.dumps({"status":report["status"],"checks":len(report["checks"])}),flush=True)
        except Exception as exc:
            job.update(status="failed",completed_at=now(),failure=f"{type(exc).__name__}: {exc}")
            raise
        finally:
            write_json(args.output/"job.json",job)


if __name__=="__main__":
    main()
