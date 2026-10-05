"""Durable dialogue+Base replay mid-training; no automatic SFT or adoption."""
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
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.dialogue_training import DialogueTrainer, DialogueReplaySampler
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json, gpu_lock, implementation_hashes
from phase6_performance import alive, identity, finite_state
from run_eos_short_pilot import equal_state
from run_amount_learning_comparison import latest_checkpoint, reconcile_metrics
from amount_learning_trainer import CompactIndex
from require_adopted_base import require_adopted_base

SOURCES = ("scripts/run_dialogue_midtraining.py", "scripts/run_dialogue_midtraining.ps1",
    "scripts/require_adopted_base.py", "src/jmicro/dialogue_training.py", "src/jmicro/tokenizer.py",
    "scripts/amount_learning_trainer.py", "scripts/run_amount_learning_comparison.py", "scripts/phase6_performance.py")


def preflight(config):
    c = read_json(config)
    assert c["implementation"] == implementation_hashes()
    assert c["source_sha256"] == {p:sha256(ROOT/p) for p in SOURCES}
    tok = require_adopted_base(c)
    assert (ROOT/c["output"]).resolve().is_relative_to(ROOT/"reports/phase7")
    assert c["GPU_budget_seconds"] > 0 and math.isfinite(c["GPU_budget_seconds"])
    assert c["quality_criteria_unchanged"] and not c["protected_test_used"]
    assert sha256(Path(c["train_records"]["path"])) == c["train_records"]["sha256"]
    directory = Path(c["data_directory"])
    assert sha256(directory/"manifest.json") == c["data_manifest_sha256"]
    assert read_json(directory/"manifest.json")["train_records_sha256"] == c["train_records"]["sha256"]
    with Path(c["train_records"]["path"]).open() as stream: records = [json.loads(line) for line in stream]
    replay = None
    if c["series_budgets"]["replay"]:
        replay = TrainView(c["replay_shards"], c["replay_manifest_sha256"]); replay.index = CompactIndex(replay)
    sampler = DialogueReplaySampler(records, tok, replay, c["spec"]["context"], c["spec"]["seed"], c["series_budgets"])
    assert sampler.binding == c["mixture_binding"]
    # Batch evidence must describe this new masked shape, rather than borrowing
    # an unrelated unpadded Base throughput measurement.
    batch_ref = c["batch_evidence"]
    assert sha256(Path(batch_ref["path"])) == batch_ref["sha256"]
    batch = read_json(Path(batch_ref["path"]))
    assert batch["actual_CUDA_BF16"] and batch["finite_forward_backward"]
    assert batch["selected_batch"] == c["spec"]["batch"] and batch["context"] == c["spec"]["context"]
    assert batch["mixture_binding"] == sampler.binding and batch["trainer_sha256"] == sha256(ROOT/"src/jmicro/dialogue_training.py")
    return c, tok, records, replay


def gate(build, run, config_sha, check):
    path = run/"resume-gate/result.json"
    if path.exists():
        kept = read_json(path); assert kept["passed"] and kept["config_sha256"] == config_sha; return kept
    states, histories = [],[]; series = teachers = 0
    for label in ("continuous", "resumed"):
        trainer = build(); history = []
        for i in range(4):
            check(); history.append(trainer.step())
            if label == "resumed" and i == 1:
                split = run/"resume-gate/split.pt"; trainer.save(split)
                del trainer; gc.collect(); torch.cuda.empty_cache(); trainer = build(); trainer.load(split)
        series += trainer.sampler.series_tokens; teachers += trainer.supervised_tokens
        end = run/"resume-gate"/(label+".pt"); trainer.save(end)
        states.append(torch.load(end, map_location="cpu", weights_only=False)); histories.append(history)
        del trainer; gc.collect(); torch.cuda.empty_cache()
    checks = {k:equal_state(states[0][k], states[1][k]) for k in ("model", "optimizer", "scheduler", "rng", "sampler", "lineage", "tokens", "supervised_tokens", "body_bytes", "token_digest", "update", "spec")}
    checks["finite"] = all(finite_state(s) for s in states)
    for field in ("loss", "gradient_norm", "lr", "series_tokens", "source_series", "source_teachers", "dialogue_teacher_kinds"):
        checks["history_"+field] = [r[field] for r in histories[0]] == [r[field] for r in histories[1]]
    assert all(checks.values()), checks
    report = dict(passed=True, checks=checks, config_sha256=config_sha, GPU_optimizer_updates=8,
        verification_series_tokens=series, verification_teacher_tokens=teachers)
    atomic_json(path, report); return report


def run(config):
    c,tok,records,replay = preflight(config); config_sha = sha256(config)
    run = ROOT/c["output"]; run.mkdir(parents=True, exist_ok=True); job_path = run/"job.json"
    previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["config_sha256"] == config_sha and not alive(previous)
        if previous["status"] == "complete": print("Completed mid-training retained"); return
    prior = previous.get("GPU_elapsed_seconds", 0.); started = None; stop = [False]
    signal.signal(signal.SIGTERM, lambda *_:stop.__setitem__(0, True)); signal.signal(signal.SIGINT, lambda *_:stop.__setitem__(0, True))
    job = dict(status="starting", **identity(), config_sha256=config_sha, started_at=previous.get("started_at", now()),
        GPU_elapsed_seconds=prior, restart_command=f"scripts/run_dialogue_midtraining.ps1 -Config {config.relative_to(ROOT).as_posix()} -Worker",
        Chat_adopted=False, requested_five_steps_complete=False)
    def check():
        if stop[0]: raise InterruptedError("Mid-training stop requested; only completed updates saved")
        if started is not None and prior+time.monotonic()-started > c["GPU_budget_seconds"]: raise TimeoutError("Frozen mid-training GPU budget exhausted")
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path, job)
    try:
        heartbeat("setup"); torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        for source in (*SOURCES, str(config.relative_to(ROOT))):
            target = run/"source"/source; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/source).read_bytes()
            else: shutil.copyfile(ROOT/source, target)
        parent = torch.load(c["parent"]["path"], map_location="cpu", weights_only=False); assert finite_state(parent)
        def build(): return DialogueTrainer(parent,c["parent"],records,tok,c["data_directory"],replay,c["spec"],c["series_budgets"],device="cuda")
        with gpu_lock("cuda"):
            started = time.monotonic(); verification = gate(build,run,config_sha,check)
            trainer = build(); latest = latest_checkpoint(run)
            if latest: trainer.load(latest)
            log = run/"metrics.jsonl"; seconds = reconcile_metrics(log,trainer.update)
            with log.open("a",buffering=1) as stream:
                while not trainer.sampler.complete:
                    try: check()
                    except (InterruptedError,TimeoutError): trainer.save(run/f"checkpoint-{trainer.update:08d}.pt"); raise
                    row = trainer.step(); seconds += row["seconds"]; stream.write(json.dumps(row,allow_nan=False)+"\n")
                    if trainer.update == 1 or trainer.update%100 == 0:
                        heartbeat("mid-training",series_tokens=row["series_tokens"],source_series=row["source_series"],loss=row["loss"])
                        print(json.dumps(row,allow_nan=False),flush=True)
                    if trainer.update%250 == 0: trainer.save(run/f"checkpoint-{trainer.update:08d}.pt")
            checkpoint = run/f"checkpoint-{trainer.update:08d}.pt"; trainer.save(checkpoint)
            result = dict(status="learning_complete_pending_Base_retention_and_Chat_ablation", config_sha256=config_sha,
                checkpoint=str(checkpoint),checkpoint_sha256=sha256(checkpoint),series_budgets=c["series_budgets"],
                actual_series_tokens=trainer.sampler.series_tokens,teacher_tokens=trainer.supervised_tokens,
                valid_input_tokens=trainer.tokens,physical_input_tokens=trainer.sampler.physical_tokens,
                full_sampler=trainer.sampler.state_dict(),Base_lineage=trainer.lineage,resume_gate=verification,
                training_step_seconds=seconds,protected_test_used=False,Chat_adopted=False,requested_five_steps_complete=False,completed_at=now())
            assert all(c["series_budgets"][s] <= trainer.sampler.source_series[s] < c["series_budgets"][s]+c["spec"]["context"]+1 for s in c["series_budgets"] if c["series_budgets"][s])
            atomic_json(run/"result.json",result); heartbeat("learning-complete"); job.update(status="complete",completed_at=now())
    except BaseException as error: job.update(status="failed",error=repr(error)); raise
    finally:
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser(); parser.add_argument("--config",type=Path,required=True); parser.add_argument("--inspect",action="store_true")
    args = parser.parse_args(); config = args.config.resolve()
    assert config.is_relative_to(ROOT/"configs/phase7")
    if args.inspect:
        c,_,records,_ = preflight(config); print(json.dumps(dict(status="CPU_preflight_only",records=len(records),series_budgets=c["series_budgets"],GPU_started=False)))
    else: run(config)
