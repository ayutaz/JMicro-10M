"""Frozen, durable SFT entry point; adopted Base evidence is required before GPU use."""
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
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,implementation_hashes
from phase6_performance import alive,identity,finite_state
from run_amount_learning_comparison import reconcile_metrics,latest_checkpoint
from run_eos_short_pilot import equal_state,rate
from review_eos_5b_finish import validate_rows

SOURCES = ("scripts/run_chat_sft.py","src/jmicro/chat_training.py","src/jmicro/assistant_sampler.py",
           "scripts/phase6_performance.py","scripts/run_amount_learning_comparison.py",
           "scripts/run_eos_short_pilot.py","scripts/review_eos_5b_finish.py","src/jmicro/tokenizer.py")


def preflight(config):
    c = read_json(config)
    assert c["implementation"] == implementation_hashes()
    assert c["source_sha256"] == {p:sha256(ROOT/p) for p in SOURCES}
    for ref in (c["parent"],c["tokenizer"],c["train_records"],c["Base_acceptance"],c["Base_evaluation"],c["Base_annotations"]):
        assert sha256(Path(ref["path"])) == ref["sha256"]
    accepted = read_json(Path(c["Base_acceptance"]["path"]))
    ev = read_json(Path(c["Base_evaluation"]["path"]))
    if accepted.get("Base_adopted") is not True:
        raise ValueError("A quality-adopted Base is required before SFT GPU training")
    assert accepted["Base_adopted"] is True and accepted["checkpoint_sha256"] == c["parent"]["sha256"]
    assert accepted["evaluation_sha256"] == c["Base_evaluation"]["sha256"] and accepted["annotations_sha256"] == c["Base_annotations"]["sha256"]
    assert accepted["quality_criteria_unchanged"] is True
    assert ev["checkpoint_sha256"] == c["parent"]["sha256"] and ev["evaluation_RNG_isolated"] and not ev["protected_test_used"]
    tok = Tokenizer(c["tokenizer"]["path"]);rows = ev["generation"]["outputs"];validate_rows(rows,tok)
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
    assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows)
    notes = read_json(Path(c["Base_annotations"]["path"]))["notes"]
    scores = {n[0]:n for n in notes}
    assert len(notes) == len(scores) == 80 and set(scores) == set(cases)
    assert all(all(n[i] in (0,1,2) for i in (1,2,3)) and n[4] in (0,1) and len(n[5]) >= 12 for n in notes)
    assert all(not scores[r["id"]][4] or r["stop_reason"] == "stop_id" and scores[r["id"]][2] >= 1 and scores[r["id"]][3] >= 1 for r in rows)
    assert sum(n[1] == 2 for n in notes) >= 56 and sum(n[3] == 2 for n in notes) >= 27 and sum(n[4] for n in notes) >= 27
    rates = rate(rows);assert rates == ev["greedy_rates"]
    assert rates["eos"] >= 37 and rates["repetition"] <= 18 and all(rates[k] == 0 for k in ("unicode_failure","role_leak","empty"))
    with Path(c["train_records"]["path"]).open() as stream: records = [json.loads(s) for s in stream]
    sampler = AssistantBudgetSampler(records,tok,c["spec"]["context"],c["spec"]["seed"],c["series_budget"])
    assert sampler.binding == c["dialogue_binding"] and all(r["split"] == "train" for r in records)
    assert c["series_budget"] in (10000000,30000000,100000000)
    data_manifest = Path(c["data_directory"])/"manifest.json"
    assert sha256(data_manifest) == c["data_manifest_sha256"]
    assert read_json(data_manifest)["train_records_sha256"] == c["train_records"]["sha256"]
    assert c["GPU_budget_seconds"] > 0
    assert (ROOT/c["output"]).resolve().is_relative_to(ROOT/"reports/phase7")
    return c,tok,records


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
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    job = dict(status="starting",**identity(),config_sha256=c["config_sha256"],started_at=previous.get("started_at",now()),
        GPU_elapsed_seconds=prior,restart_command=f"uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_chat_sft.py --config {config}")
    def check():
        if stopped[0]: raise InterruptedError("SFT stop requested")
        if started is not None and prior+time.monotonic()-started > c["GPU_budget_seconds"]: raise TimeoutError("Frozen cumulative SFT GPU budget exhausted")
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)
    try:
        heartbeat("setup");torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for source in (*SOURCES,str(config.relative_to(ROOT))):
            target = run/"source"/source;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/source).read_bytes()
            else: shutil.copyfile(ROOT/source,target)
        parent = torch.load(c["parent"]["path"],map_location="cpu",weights_only=False);assert finite_state(parent)
        with gpu_lock("cuda"):
            started = time.monotonic();gate = resume_gate(parent,c,tok,records,run,check)
            trainer = AssistantTrainer(parent,c["parent"],records,tok,c["data_directory"],c["spec"],c["series_budget"],device="cuda")
            last = latest_checkpoint(run)
            if last: trainer.load(last)
            log_path = run/"metrics.jsonl";seconds = reconcile_metrics(log_path,trainer.update)
            with log_path.open("a",buffering=1) as log:
                while trainer.sampler.series_tokens < c["series_budget"]:
                    try: check()
                    except (InterruptedError,TimeoutError): trainer.save(run/f"checkpoint-{trainer.update:08d}.pt");raise
                    row = trainer.step();seconds += row["seconds"];log.write(json.dumps(row,allow_nan=False)+"\n")
                    if trainer.update == 1 or trainer.update%100 == 0:
                        heartbeat("SFT",series_tokens=row["series_tokens"],Assistant_teachers=row["assistant_teacher_tokens"],EOT_teachers=row["EOT_teachers"],loss=row["loss"])
                        print(json.dumps(row,allow_nan=False),flush=True)
                    if trainer.update%250 == 0: trainer.save(run/f"checkpoint-{trainer.update:08d}.pt")
            checkpoint = run/f"checkpoint-{trainer.update:08d}.pt";trainer.save(checkpoint)
            result = dict(status="learning_complete_pending_Chat_quality",config_sha256=c["config_sha256"],checkpoint=str(checkpoint),checkpoint_sha256=sha256(checkpoint),
                requested_series_budget=c["series_budget"],actual_series_tokens=trainer.sampler.series_tokens,Assistant_teacher_tokens=trainer.supervised_tokens,
                valid_input_tokens=trainer.tokens,physical_tokens=trainer.sampler.physical_tokens,EOT_teachers=trainer.sampler.eot_teachers,
                full_sampler=trainer.sampler.state_dict(),Base_lineage=trainer.lineage,training_step_seconds=seconds,
                resume_gate=gate,Chat_adopted=False,requested_five_steps_complete=False,completed_at=now())
            assert c["series_budget"] <= result["actual_series_tokens"] < c["series_budget"]+c["spec"]["context"]+1
            atomic_json(run/"result.json",result);heartbeat("learning-complete");job.update(status="complete",completed_at=now())
    except BaseException as error: job.update(status="failed",error=repr(error));raise
    finally:
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser();parser.add_argument("--config",type=Path,required=True);parser.add_argument("--inspect",action="store_true");args = parser.parse_args()
    if args.inspect:
        c,tok,records = preflight(args.config.resolve());print(json.dumps(dict(status="CPU_preflight_only",records=len(records),series_budget=c["series_budget"],GPU_started=False)))
    else: run(args.config.resolve())
