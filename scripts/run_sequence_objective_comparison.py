"""Bounded matched CE/sequence-UL study, gated on the completed material study."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes,atomic_json,gpu_lock
from phase6_performance import alive,identity,finite_state
from run_eos_short_pilot import equal_state
from sequence_objective_trainer import SequenceObjectiveTrainer
from textbook_quantity_trainer import ThreeSourceIndex
from run_textbook_quantity_comparison import CONFIG as SOURCE_CONFIG,RUN as SOURCE_RUN,load_config,latest_checkpoint,reconcile_metrics,detail
import run_complete_text_comparison as evaluation

PROBE_CONFIG=ROOT/"configs/phase6/sequence_objective_probe.json"
CONFIG=ROOT/"configs/phase6/sequence_objective_comparison.json"
RUN=ROOT/"reports/phase6/sequence-objective-comparison-20261006"
POINT="large-1000000000"
TOTAL_CE=25000000
SOURCES=("scripts/run_sequence_objective_comparison.py","scripts/run_sequence_objective_comparison.ps1",
         "scripts/sequence_objective_trainer.py","src/jmicro/sequence_unlikelihood.py",
         "scripts/review_sequence_objective_comparison.py","scripts/run_complete_text_comparison.py",
         "scripts/textbook_quantity_trainer.py","scripts/amount_learning_trainer.py","src/jmicro/learning_curve.py")


def ref(path):return dict(path=str(path),sha256=sha256(path))


def source_contract():
    job=read_json(SOURCE_RUN/"job.json")
    if job["status"]!="complete" or alive(job):
        raise ValueError("Actual material comparison must finish before objective selection")
    base=load_config();result=read_json(SOURCE_RUN/"compare-result.json");review=read_json(SOURCE_RUN/"review.json")
    assert review["status"]=="matched500M_2B_all160_and_actual_learning_evidence_complete"
    assert review["result_sha256"]==sha256(SOURCE_RUN/"compare-result.json")
    assert review["annotations_sha256"]==sha256(SOURCE_RUN/"annotations.json")
    assert not review["Base_adopted"] and not review["protected_test_used"]
    if review["quantity_comparison"]["passed"] or any(s["absolute_screen_pass"] for s in review["practical"].values()):
        raise ValueError("Existing improvement supports the earlier extension/final validation branch; do not launch this alternative")
    assert review["summaries"][POINT]["rates"]["repetition"]>0
    record=result["decay"][POINT];parent=torch.load(record["checkpoint"],map_location="cpu",weights_only=False)
    assert sha256(Path(record["checkpoint"]))==record["checkpoint_sha256"] and finite_state(parent)
    assert parent["pilot_binding"]==record["binding"] and parent["spec"]["curve_schedule"]["mode"]=="decay"
    assert parent["sampler"]["source_teachers"]["short"]==parent["spec"]["curve_schedule"]["teachers"]==20000000
    return base,record,parent


def make_plan():
    base,record,parent=source_contract()
    return dict(kind="sequence-objective-probe",original_config=ref(SOURCE_CONFIG),
        source_result=ref(SOURCE_RUN/"compare-result.json"),source_review=ref(SOURCE_RUN/"review.json"),
        source_annotations=ref(SOURCE_RUN/"annotations.json"),parent=dict(path=record["checkpoint"],sha256=record["checkpoint_sha256"],
            update=parent["update"],tokens_seen=parent["tokens"],supervised_tokens=parent["supervised_tokens"]),
        point=POINT,pool=base["pools"]["large"],CE_teachers_per_arm=TOTAL_CE,
        peak_lr=min(.0002,parent["optimizer"]["param_groups"][0]["lr"]),
        objectives={a:dict(alpha=alpha,every_updates=4,prefixes=8,prefix_tokens=32,max_new_tokens=64,ngram=4)
                    for a,alpha in (("CE",0.),("CE_UL",.1))},
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        GPU_budget_seconds=300,total_study_GPU_ceiling_seconds=1800,
        old_numerical7_preserved=True,quality_criteria_unchanged=True,protected_test_used=False,
        Base_adopted=False,Chat_adopted=False,requested_five_steps_complete=False)


def preflight(path):
    c=read_json(path);base,record,parent=source_contract()
    for k in ("original_config","source_result","source_review","source_annotations"):
        assert sha256(Path(c[k]["path"]))==c[k]["sha256"]
    assert c["parent"]["path"]==record["checkpoint"] and c["parent"]["sha256"]==record["checkpoint_sha256"]
    assert c["point"]==POINT and c["pool"]==base["pools"]["large"] and c["CE_teachers_per_arm"]==TOTAL_CE
    assert c["objectives"]=={a:dict(alpha=alpha,every_updates=4,prefixes=8,prefix_tokens=32,max_new_tokens=64,ngram=4) for a,alpha in (("CE",0.),("CE_UL",.1))}
    assert c["peak_lr"]==min(.0002,parent["optimizer"]["param_groups"][0]["lr"])
    assert c["source_sha256"]=={p:sha256(ROOT/p) for p in SOURCES} and c["implementation"]==implementation_hashes()
    assert not c["protected_test_used"] and c["quality_criteria_unchanged"] and 0<c["GPU_budget_seconds"]<=1800
    assert c["total_study_GPU_ceiling_seconds"]==1800
    output=RUN/"probe" if c["kind"]=="sequence-objective-probe" else RUN
    if (output/"job.json").exists() and alive(read_json(output/"job.json")):
        raise ValueError("Actual sequence objective job is already live; do not duplicate")
    if c["kind"]=="sequence-objective-comparison":
        assert sha256(PROBE_CONFIG)==c["probe_config_sha256"] and sha256(RUN/"probe/result.json")==c["measurement_sha256"]
        measurement=read_json(RUN/"probe/result.json");job=read_json(RUN/"probe/job.json")
        assert job["status"]=="complete" and not alive(job) and measurement["passed"]
        assert all(g["passed"] and all(g["checks"].values()) for g in measurement["gates"].values())
        assert c["verification_GPU_seconds"]==job["gpu_elapsed_seconds"] and c["GPU_budget_seconds"]+c["verification_GPU_seconds"]==1800
    else:assert c["kind"]=="sequence-objective-probe" and c["GPU_budget_seconds"]==300
    return c,base,parent


def prepare_probe():
    if PROBE_CONFIG.exists():preflight(PROBE_CONFIG);return
    c=make_plan();atomic_json(PROBE_CONFIG,c);print("Conditional probe plan frozen; no GPU started")


def freeze():
    if CONFIG.exists():preflight(CONFIG);return
    c,_,_=preflight(PROBE_CONFIG);job=read_json(RUN/"probe/job.json");m=read_json(RUN/"probe/result.json")
    assert job["status"]=="complete" and not alive(job) and m["passed"]
    estimated=0.;timings={}
    for arm,g in m["gates"].items():
        rows=[r for h in g["histories"] for r in h]
        ordinary=statistics.median(r["seconds"] for i,r in enumerate(rows) if i%4!=3)
        rollout=statistics.median(r["seconds"] for i,r in enumerate(rows) if i%4==3)
        teachers=g["verification_teacher_tokens"]/8;updates=math.ceil(TOTAL_CE/teachers);extra=updates//4
        estimate=(updates-extra)*ordinary+extra*rollout
        timings[arm]=dict(ordinary_step_seconds=ordinary,rollout_step_seconds=rollout,measured_CE_teachers_per_update=teachers,
                         estimated_updates=updates,estimated_training_seconds=estimate)
        estimated+=estimate
    estimate_with_margin=estimated*1.3+480
    if estimate_with_margin+job["gpu_elapsed_seconds"]>1800:
        raise ValueError("Measured full25M-per-arm study cannot fit unchanged1800s ceiling; retain measurement and revise explicitly")
    c.update(kind="sequence-objective-comparison",probe_config_sha256=sha256(PROBE_CONFIG),
        measurement_sha256=sha256(RUN/"probe/result.json"),verification_GPU_seconds=job["gpu_elapsed_seconds"],
        GPU_budget_seconds=1800-job["gpu_elapsed_seconds"],measured_timings=timings,
        estimated_scientific_and_evaluation_GPU_seconds_with_margin=estimate_with_margin)
    atomic_json(CONFIG,c);print(json.dumps(dict(status="measured recipe frozen",timings=timings,GPU_budget_seconds=c["GPU_budget_seconds"])))


def binding(c,path,arm):
    return dict(config_sha256=sha256(path),parent=c["parent"],arm=arm,peak_lr=c["peak_lr"],warmup_updates=0,
        optimizer_policy="inherit",initialization="completed-parent-objective-fork",curve_mode="decay",
        curve_boundaries=[TOTAL_CE],short_manifest_sha256=c["pool"]["manifest_sha256"],sequence_objective=c["objectives"][arm])


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG;c,base,parent=preflight(path);output=RUN/"probe" if probe else RUN
    output.mkdir(parents=True,exist_ok=True);jp=output/"job.json";old=read_json(jp) if jp.exists() else {}
    if old:
        assert old["config_sha256"]==sha256(path) and not alive(old)
        if old["status"]=="complete":print("Completed job retained");return
    started=[None];stopped=[False];prior=old.get("gpu_elapsed_seconds",0.)
    job=dict(status="running",**identity(),config_sha256=sha256(path),started_at=old.get("started_at",now()),gpu_elapsed_seconds=prior,
        protected_test_used=False,Base_adopted=False,restart_command=f"scripts/run_sequence_objective_comparison.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError("Stop requested; completed updates retained")
        if started[0] is not None and prior+time.monotonic()-started[0]>c["GPU_budget_seconds"]:raise TimeoutError("Cumulative objective GPU budget exhausted")
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),**extra)
        if started[0] is not None:job["gpu_elapsed_seconds"]=prior+time.monotonic()-started[0]
        atomic_json(jp,job)
    def save(trainer,folder):
        target=folder/f"checkpoint-{trainer.update:08d}.pt";trainer.save(target);return target
    def gate(build,arm):
        gp=output/"resume-gate"/arm/"result.json"
        if gp.exists():
            kept=read_json(gp);assert kept["passed"] and kept["config_sha256"]==sha256(path);return kept
        states=[];histories=[];teachers=0;inputs=0
        for route in ("continuous","resumed"):
            trainer=build();before=trainer.supervised_tokens,trainer.tokens;rows=[]
            for i in range(4):
                check();rows.append(trainer.step())
                if route=="resumed" and i==1:
                    split=gp.parent/"split.pt";trainer.save(split);del trainer;gc.collect();torch.cuda.empty_cache();trainer=build();trainer.load(split)
            teachers+=trainer.supervised_tokens-before[0];inputs+=trainer.tokens-before[1]
            trainer.save(gp.parent/(route+".pt"));states.append(torch.load(gp.parent/(route+".pt"),map_location="cpu",weights_only=False));histories.append(rows)
            del trainer;gc.collect();torch.cuda.empty_cache()
        checks={k:equal_state(states[0][k],states[1][k]) for k in ("model","optimizer","scheduler","rng","sampler","lineage","tokens","supervised_tokens","body_bytes","token_digest","update","spec","model_config","pilot_binding")}
        for key in ("loss","sequence_UL","optimization_loss","gradient_norm","lr","token_digest","source_teachers","sequence_objective"):
            checks["history_"+key]=all(equal_state(a[key],b[key]) for a,b in zip(histories[0],histories[1],strict=True))
        checks["finite"]=all(finite_state(s) for s in states)
        checks["actual_rollout_both_routes"]=all(h[-1]["sequence_objective"]["rollout_batches"]==1 and h[-1]["sequence_objective"]["skipped_rollouts"]==0 for h in histories)
        assert all(checks.values()),checks
        result=dict(passed=True,checks=checks,histories=histories,config_sha256=sha256(path),GPU_optimizer_updates=8,
                    verification_teacher_tokens=teachers,verification_input_tokens=inputs)
        atomic_json(gp,result);heartbeat(arm+"-resume-verified");return result
    try:
        heartbeat("setup");torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES,path.relative_to(ROOT).as_posix()):
            target=output/"source"/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        web=TrainView(base["web_shards"],base["web_manifest_sha256"])
        pool=TrainView(c["pool"]["pool"],c["pool"]["manifest_sha256"]);pool.index=ThreeSourceIndex(pool)
        dev=Shard(Path(base["dev_shards"]),"dev");tok=Tokenizer(ROOT/base["tokenizer"])
        result=read_json(output/"progress-result.json") if (output/"progress-result.json").exists() else dict(checkpoints={},evaluations={},gates={})
        evaluation.RUN=output/"evaluation"
        with gpu_lock("cuda"):
            started[0]=time.monotonic()
            for arm in c["objectives"]:
                b=binding(c,path,arm)
                def build():return SequenceObjectiveTrainer(parent,web,pool,"shuffle",dict(web=0,short=TOTAL_CE),b)
                if probe:
                    result["gates"][arm]=gate(build,arm);atomic_json(output/"progress-result.json",result);continue
                if arm not in result["checkpoints"]:
                    trainer=build();folder=output/arm/"training";folder.mkdir(parents=True,exist_ok=True)
                    latest=latest_checkpoint(folder)
                    if latest is not None:trainer.load(latest)
                    log=folder/"metrics.jsonl";seconds=reconcile_metrics(log,trainer.update)
                    with log.open("a",buffering=1) as stream:
                        while trainer.sampler.source_teachers["short"]<TOTAL_CE:
                            try:check()
                            except (InterruptedError,TimeoutError):save(trainer,folder);raise
                            row=trainer.step();seconds+=row["seconds"];stream.write(json.dumps(row,allow_nan=False)+"\n")
                            if trainer.sampler.position%20==0:heartbeat(arm+"-training",teachers=trainer.sampler.source_teachers["short"],teacher_budget=TOTAL_CE,loss=row["loss"],sequence_UL=row["sequence_UL"])
                            if trainer.sampler.position%100==0:save(trainer,folder)
                    cp=save(trainer,folder);record=detail(trainer,cp,b,seconds);record["sequence_objective"]=trainer.lineage["sequence_objective"]
                    result["checkpoints"][arm]=record;atomic_json(output/"progress-result.json",result)
                    del trainer;gc.collect();torch.cuda.empty_cache()
                if arm not in result["evaluations"]:
                    result["evaluations"][arm]=evaluation.evaluate(arm,result["checkpoints"][arm],dev,tok,base,b,heartbeat,check,started[0]+c["GPU_budget_seconds"]-prior)
                    atomic_json(output/"progress-result.json",result)
            if probe:
                result.update(status="actual_CUDA_objective_measurement_and_resume_complete",passed=True,config_sha256=sha256(path),
                    verification_teacher_tokens=sum(g["verification_teacher_tokens"] for g in result["gates"].values()),scientific_teacher_tokens=0)
                atomic_json(output/"result.json",result)
            else:
                result.update(status="matched_CE_sequence_UL_complete_pending_all160_content",config_sha256=sha256(path),
                    scientific_teacher_tokens=sum(r["additional_supervised_tokens"] for r in result["checkpoints"].values()),
                    verification_teacher_tokens=read_json(RUN/"probe/result.json")["verification_teacher_tokens"],
                    scientific_GPU_seconds=prior+time.monotonic()-started[0],verification_GPU_seconds=c["verification_GPU_seconds"],
                    Base_adopted=False,Chat_adopted=False,protected_test_used=False,requested_five_steps_complete=False)
                assert result["scientific_teacher_tokens"]==2*TOTAL_CE and len(result["evaluations"])==2
                atomic_json(output/"compare-result.json",result)
            heartbeat("complete");job.update(status="complete",completed_at=now())
    except BaseException as error:job.update(status="failed",error=repr(error));raise
    finally:
        if started[0] is not None:job["gpu_elapsed_seconds"]=prior+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();group=p.add_mutually_exclusive_group()
    for mode in ("prepare-probe","preflight-probe","probe","freeze","inspect"):group.add_argument("--"+mode,action="store_true")
    args=p.parse_args()
    if args.prepare_probe:prepare_probe()
    elif args.preflight_probe:preflight(PROBE_CONFIG)
    elif args.freeze:freeze()
    elif args.inspect:preflight(CONFIG)
    else:run(args.probe)
