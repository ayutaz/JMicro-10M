"""Bounded Chat-first diagnostic from an explicitly unadopted frozen Base."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.chat_training import AssistantTrainer,AssistantBudgetSampler
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,implementation_hashes
from phase6_performance import alive,identity,finite_state
from run_amount_learning_comparison import reconcile_metrics,latest_checkpoint
from run_eos_short_pilot import equal_state
from chat_first_contract import preflight as diagnostic_preflight, parent_state
from chat_batch_evidence import require_batch_evidence

SOURCES = ("scripts/run_chat_sft.py","src/jmicro/chat_training.py","src/jmicro/assistant_sampler.py",
           "scripts/run_chat_sft.ps1",
           "scripts/phase6_performance.py","scripts/run_amount_learning_comparison.py",
           "scripts/run_eos_short_pilot.py","scripts/review_eos_5b_finish.py","src/jmicro/tokenizer.py",
           "scripts/require_adopted_base.py","scripts/run_dialogue_midtraining.py","src/jmicro/dialogue_training.py",
           "scripts/chat_batch_evidence.py")


SOURCES = (*SOURCES, "scripts/run_chat_first_sft.py", "scripts/run_chat_first_sft.ps1", "scripts/chat_first_contract.py")


def preflight(config, *, require_batch=True):
    return diagnostic_preflight(config, SOURCES, require_batch=require_batch)


def resume_gate(parent,c,tok,records,run,check):
    path = run/"resume-gate/result.json"
    if path.exists():
        gate = read_json(path);assert gate["passed"] and gate["config_sha256"] == c["config_sha256"];return gate
    states,history = [],[];series = teachers = 0
    for branch in ("continuous","resumed"):
        trainer = AssistantTrainer(parent,c["parent"],records,tok,c["data_directory"],c["spec"],c["series_budget"],device="cuda")
        rows = []
        for update in range(4):
            check();rows.append(trainer.step())
            if branch == "resumed" and update == 1:
                split = run/"resume-gate/split.pt";trainer.save(split)
                del trainer;gc.collect();torch.cuda.empty_cache()
                trainer = AssistantTrainer(parent,c["parent"],records,tok,c["data_directory"],c["spec"],c["series_budget"],device="cuda");trainer.load(split)
        series += trainer.sampler.series_tokens;teachers += trainer.supervised_tokens
        end = run/"resume-gate"/(branch+".pt");trainer.save(end)
        states.append(torch.load(end,map_location="cpu",weights_only=False));history.append(rows)
        del trainer;gc.collect();torch.cuda.empty_cache()
    keys = ("model","optimizer","scheduler","rng","sampler","tokens","supervised_tokens","body_bytes","token_digest","lineage","update","spec")
    checks = {k:equal_state(states[0][k],states[1][k]) for k in keys}
    checks["finite_history"] = all(math.isfinite(r["loss"]) and math.isfinite(r["gradient_norm"]) for rows in history for r in rows)
    for key in ("loss","gradient_norm","lr","series_tokens","assistant_teacher_tokens","EOT_teachers"):
        checks["history_"+key] = [r[key] for r in history[0]] == [r[key] for r in history[1]]
    assert all(checks.values()),checks
    result = dict(passed=True,config_sha256=c["config_sha256"],checks=checks,history=history,
        verification_series_tokens=series,verification_Assistant_teachers=teachers,GPU_optimizer_updates=8)
    atomic_json(path,result);return result


def run(config):
    c,tok,records = preflight(config);c["config_sha256"] = sha256(config)
    run = ROOT/c["output"];run.mkdir(parents=True,exist_ok=True)
    job_path = run/"job.json";previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["config_sha256"] == c["config_sha256"] and not alive(previous)
        if previous["status"] == "complete": print("Completed SFT retained");return
    prior = previous.get("GPU_elapsed_seconds",0.);started = None;stopped = [False]
    training_started = None; prior_training = previous.get("training_GPU_elapsed_seconds", 0.)
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    job = dict(status="starting",**identity(),config_sha256=c["config_sha256"],started_at=previous.get("started_at",now()),
        GPU_elapsed_seconds=prior,restart_command=f"uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_chat_first_sft.py --config {config}")
    def check():
        if training_started is not None and prior_training+time.monotonic()-training_started > c["training_GPU_budget_seconds"]: raise TimeoutError("Frozen training budget exhausted")
        if training_started is None and started is not None and time.monotonic()-started > c["resume_GPU_budget_seconds"]: raise TimeoutError("Resume gate budget exhausted")
        if stopped[0]: raise InterruptedError("SFT stop requested")
        if started is not None and prior+time.monotonic()-started > c["GPU_budget_seconds"]: raise TimeoutError("Frozen cumulative SFT GPU budget exhausted")
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        if training_started is not None: job["training_GPU_elapsed_seconds"] = prior_training+time.monotonic()-training_started
        atomic_json(job_path,job)
    try:
        heartbeat("setup");torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for source in (*SOURCES,str(config.relative_to(ROOT))):
            target = run/"source"/source;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/source).read_bytes()
            else: shutil.copyfile(ROOT/source,target)
        parent = parent_state(c)
        with gpu_lock("cuda"):
            started = time.monotonic();gate = resume_gate(parent,c,tok,records,run,check)
            trainer = AssistantTrainer(parent,c["parent"],records,tok,c["data_directory"],c["spec"],c["series_budget"],device="cuda")
            last = latest_checkpoint(run)
            if last: trainer.load(last)
            training_started = time.monotonic(); last_save = training_started
            checkpoints = read_json(run/"checkpoints.json") if (run/"checkpoints.json").exists() else {}
            log_path = run/"metrics.jsonl";seconds = reconcile_metrics(log_path,trainer.update)
            with log_path.open("a",buffering=1) as log:
                while trainer.sampler.series_tokens < c["series_budget"]:
                    try: check()
                    except (InterruptedError,TimeoutError): trainer.save(run/f"checkpoint-{trainer.update:08d}.pt");raise
                    row = trainer.step();seconds += row["seconds"];log.write(json.dumps(row,allow_nan=False)+"\n")
                    if trainer.update == 1 or trainer.update%100 == 0:
                        heartbeat("SFT",series_tokens=row["series_tokens"],Assistant_teachers=row["assistant_teacher_tokens"],EOT_teachers=row["EOT_teachers"],loss=row["loss"])
                        print(json.dumps(row,allow_nan=False),flush=True)
                    reached = [f"epoch{n}" for n in (1,2,3) if trainer.sampler.series_tokens >= n*10189157 and f"epoch{n}" not in checkpoints]
                    if reached or trainer.update%250 == 0 or time.monotonic()-last_save >= 300:
                        target = run/f"checkpoint-{trainer.update:08d}.pt";trainer.save(target);last_save = time.monotonic()
                        for name in reached:
                            checkpoints[name] = dict(path=str(target),sha256=sha256(target),update=trainer.update,
                                examples=trainer.sampler.examples,Assistant_teachers=trainer.supervised_tokens,series_tokens=trainer.sampler.series_tokens)
                        atomic_json(run/"checkpoints.json",checkpoints)
            checkpoint = run/f"checkpoint-{trainer.update:08d}.pt";trainer.save(checkpoint)
            result = dict(status="learning_complete_pending_Chat_quality",config_sha256=c["config_sha256"],checkpoint=str(checkpoint),checkpoint_sha256=sha256(checkpoint),
                requested_series_budget=c["series_budget"],actual_series_tokens=trainer.sampler.series_tokens,Assistant_teacher_tokens=trainer.supervised_tokens,
                valid_input_tokens=trainer.tokens,physical_tokens=trainer.sampler.physical_tokens,EOT_teachers=trainer.sampler.eot_teachers,
                full_sampler=trainer.sampler.state_dict(),Base_lineage=trainer.lineage,training_step_seconds=seconds,
                route=c.get("route","direct-sft"),root_Base=c["parent"],model_parent=c["parent"],Base_adopted=False,purpose="chat_first_diagnostic",checkpoints=checkpoints,
                resume_gate=gate,Chat_adopted=False,requested_five_steps_complete=False,completed_at=now())
            assert c["series_budget"] <= result["actual_series_tokens"] < c["series_budget"]+c["spec"]["context"]+1
            assert trainer.sampler.examples == 121098 and trainer.supervised_tokens == 1899555 and trainer.sampler.series_tokens == 30567471
            assert set(checkpoints) == {"epoch1","epoch2","epoch3"}
            atomic_json(run/"result.json",result);heartbeat("learning-complete");job.update(status="complete",completed_at=now())
    except BaseException as error: job.update(status="failed",error=repr(error));raise
    finally:
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        if training_started is not None: job["training_GPU_elapsed_seconds"] = prior_training+time.monotonic()-training_started
        atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser();parser.add_argument("--config",type=Path,required=True);parser.add_argument("--inspect",action="store_true");args = parser.parse_args()
    if args.inspect:
        c,tok,records = preflight(args.config.resolve());print(json.dumps(dict(status="CPU_preflight_only",records=len(records),series_budget=c["series_budget"],GPU_started=False)))
    else: run(args.config.resolve())
