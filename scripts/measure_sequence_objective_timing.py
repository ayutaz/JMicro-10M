"""Bounded continuous timing after actual resume gates; weights are discarded."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import gpu_lock,atomic_json,implementation_hashes
from jmicro.eos_pilot import TrainView
from phase6_performance import alive,identity,finite_state
from sequence_objective_trainer import SequenceObjectiveTrainer
from textbook_quantity_trainer import ThreeSourceIndex
from run_textbook_quantity_comparison import latest_checkpoint,reconcile_metrics
from run_sequence_objective_comparison import RUN as STUDY,PROBE_CONFIG,preflight

CONFIG=ROOT/"configs/phase6/sequence_objective_timing.json"
RUN=STUDY/"continuous-timing"
SOURCES=("scripts/measure_sequence_objective_timing.py","scripts/measure_sequence_objective_timing.ps1",
         "scripts/sequence_objective_trainer.py","src/jmicro/sequence_unlikelihood.py","scripts/textbook_quantity_trainer.py")


def inspect():
    c=read_json(CONFIG);base_c,base,parent=preflight(PROBE_CONFIG)
    job=read_json(STUDY/"probe/job.json");m=read_json(STUDY/"probe/result.json")
    assert job["status"]=="complete" and not alive(job) and m["passed"]
    assert c["original_probe_sha256"]==sha256(PROBE_CONFIG) and c["measurement_sha256"]==sha256(STUDY/"probe/result.json")
    assert c["original_probe_GPU_seconds"]==job["gpu_elapsed_seconds"] and c["GPU_budget_seconds"]+job["gpu_elapsed_seconds"]==300
    assert c["timing_updates_per_arm"]==16 and c["source_sha256"]=={p:sha256(ROOT/p) for p in SOURCES}
    assert c["implementation"]==implementation_hashes() and not c["protected_test_used"]
    for arm,ref in c["continuous_checkpoints"].items():
        assert sha256(Path(ref["path"]))==ref["sha256"] and m["gates"][arm]["passed"] and all(m["gates"][arm]["checks"].values())
    if (RUN/"job.json").exists() and alive(read_json(RUN/"job.json")):raise ValueError("Timing process is live; do not duplicate")
    return c,base_c,base,parent


def prepare():
    if CONFIG.exists():inspect();return
    _,_,_=preflight(PROBE_CONFIG);job=read_json(STUDY/"probe/job.json");m=read_json(STUDY/"probe/result.json")
    assert job["status"]=="complete" and not alive(job) and m["passed"]
    c=dict(kind="continuous-objective-timing-not-scientific-learning",original_probe_sha256=sha256(PROBE_CONFIG),
        measurement_sha256=sha256(STUDY/"probe/result.json"),original_probe_GPU_seconds=job["gpu_elapsed_seconds"],
        GPU_budget_seconds=300-job["gpu_elapsed_seconds"],timing_updates_per_arm=16,
        continuous_checkpoints={a:dict(path=str(STUDY/"probe/resume-gate"/a/"continuous.pt"),
            sha256=sha256(STUDY/"probe/resume-gate"/a/"continuous.pt")) for a in m["gates"]},
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        scientific_teacher_tokens=0,protected_test_used=False,Base_adopted=False,weights_used_for_scientific_parent=False,
        estimation_rule="Record all16 updates per arm; first4 contain load/compile warmup and remain counted, use subsequent12 contiguous updates including3 real rollout cycles for steady median, no favorable-seed selection")
    atomic_json(CONFIG,c);print("Continuous timing plan frozen; no GPU started")


def run():
    c,base_c,base,parent=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/"job.json"
    old=read_json(jp) if jp.exists() else {}
    if old:
        assert old["config_sha256"]==sha256(CONFIG) and not alive(old)
        if old["status"]=="complete":print("Completed timing retained");return
    prior=old.get("gpu_elapsed_seconds",0.);start=[None];stop=[False]
    job=dict(status="running",**identity(),config_sha256=sha256(CONFIG),started_at=old.get("started_at",now()),
             gpu_elapsed_seconds=prior,restart_command="scripts/measure_sequence_objective_timing.ps1 -Worker",scientific_teacher_tokens=0)
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError("Stop requested; completed timing checkpoint retained")
        if start[0] is not None and prior+time.monotonic()-start[0]>c["GPU_budget_seconds"]:raise TimeoutError("Probe plus timing300s ceiling exhausted")
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if start[0] is not None:job["gpu_elapsed_seconds"]=prior+time.monotonic()-start[0]
        atomic_json(jp,job)
    try:
        heartbeat("index");torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/"source"/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        web=TrainView(base["web_shards"],base["web_manifest_sha256"])
        pool=TrainView(base_c["pool"]["pool"],base_c["pool"]["manifest_sha256"]);pool.index=ThreeSourceIndex(pool)
        result={}
        with gpu_lock("cuda"):
            start[0]=time.monotonic()
            for arm,ref in c["continuous_checkpoints"].items():
                state=torch.load(ref["path"],map_location="cpu",weights_only=False);binding=state["pilot_binding"]
                trainer=SequenceObjectiveTrainer(parent,web,pool,"shuffle",dict(web=0,short=25000000),binding)
                folder=RUN/arm;folder.mkdir(parents=True,exist_ok=True);latest=latest_checkpoint(folder)
                trainer.load(latest or Path(ref["path"]));base_update=state["update"];base_teachers=state["supervised_tokens"]
                log=folder/"metrics.jsonl";reconcile_metrics(log,trainer.update)
                with log.open("a",buffering=1) as stream:
                    while trainer.update-base_update<16:
                        check();row=trainer.step();stream.write(json.dumps(row,allow_nan=False)+"\n")
                        trainer.save(folder/f"checkpoint-{trainer.update:08d}.pt")
                        heartbeat(arm+"-continuous-timing",completed_updates=trainer.update-base_update,total_updates=16)
                rows=[json.loads(s) for s in log.read_text().splitlines()]
                assert len(rows)==16 and all(r["sequence_objective"]["skipped_rollouts"]==0 for r in rows)
                assert all(finite_state(r) for r in rows)
                cp=latest_checkpoint(folder)
                result[arm]=dict(histories=rows,verification_teacher_tokens=trainer.supervised_tokens-base_teachers,
                    checkpoint=str(cp),checkpoint_sha256=sha256(cp),weights_discarded_for_science=True)
                del trainer,state;gc.collect();torch.cuda.empty_cache()
            atomic_json(RUN/"result.json",dict(status="actual_continuous_timing_complete",config_sha256=sha256(CONFIG),
                arms=result,verification_teacher_tokens=sum(r["verification_teacher_tokens"] for r in result.values()),
                scientific_teacher_tokens=0,Base_adopted=False,protected_test_used=False,weights_used_for_scientific_parent=False))
            heartbeat("complete");job.update(status="complete",completed_at=now())
    except BaseException as error:job.update(status="failed",error=repr(error));raise
    finally:
        if start[0] is not None:job["gpu_elapsed_seconds"]=prior+time.monotonic()-start[0]
        atomic_json(jp,job)


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument("--prepare",action="store_true");g.add_argument("--inspect",action="store_true")
    args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect()
    else:run()
