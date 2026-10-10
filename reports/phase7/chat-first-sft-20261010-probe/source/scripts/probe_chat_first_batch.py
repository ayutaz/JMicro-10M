"""Measured CUDA/BF16 batch selection for adopted-Base dialogue/SFT recipes.

Probe checkpoints are never used as model parents. Teacher, series, valid-input
and physical throughput are separate. The search has an explicit finite range.
"""
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
from jmicro.chat_training import AssistantTrainer
from jmicro.dialogue_training import DialogueTrainer
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,implementation_hashes
from phase6_performance import alive,identity,finite_state
import run_chat_first_sft as sft
import run_dialogue_midtraining as mid

SOURCES = ("scripts/probe_chat_first_batch.py","scripts/probe_chat_first_batch.ps1","scripts/chat_batch_evidence.py")


def selection(records):
    successful = [r for r in records if r["status"] == "complete" and r["finite_forward_backward"]]
    if not successful: raise ValueError("No finite CUDA batch candidate")
    return max(successful,key=lambda r:r["median_teacher_tokens_per_second"])


def preflight(config):
    c = read_json(config);kind = c["probe_kind"]
    if kind != "sft": raise ValueError("Choose sft or mid-training batch probe")
    assert c["probe_source_sha256"] == {p:sha256(ROOT/p) for p in SOURCES}
    if kind == "sft":
        recipe,tok,records = sft.preflight(config,require_batch=False);replay = None
        binding = c["dialogue_binding"];trainer_path = "src/jmicro/chat_training.py"
    else:
        recipe,tok,records,replay = mid.preflight(config,require_batch=False)
        binding = c["mixture_binding"];trainer_path = "src/jmicro/dialogue_training.py"
    assert c["spec"]["dtype"] == "bf16" and c["spec"]["sampler"] == "document" and not c["spec"]["training_fast_path"]
    assert c["spec"]["accumulation"] == 1
    batches = c["candidate_batches"]
    assert batches == sorted(set(batches)) and 1 <= len(batches) <= 12 and all(type(b) is int and 1 <= b <= 256 for b in batches)
    assert type(c["probe_warmup_updates"]) is int and 1 <= c["probe_warmup_updates"] <= 20
    assert type(c["probe_measured_updates"]) is int and 4 <= c["probe_measured_updates"] <= 100
    assert math.isfinite(c["probe_GPU_budget_seconds"]) and 0 < c["probe_GPU_budget_seconds"] <= 1800
    directory = (ROOT/c["probe_output"]).resolve()
    assert directory.is_relative_to(ROOT/"reports/phase7") and directory != (ROOT/c["output"]).resolve()
    return recipe,tok,records,replay,binding,trainer_path


def run(config):
    c,tok,records,replay,binding,trainer_path = preflight(config)
    run = ROOT/c["probe_output"];run.mkdir(parents=True,exist_ok=True);job_path = run/"probe-job.json"
    config_sha = sha256(config);previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["config_sha256"] == config_sha and not alive(previous)
        if previous["status"] == "complete": print("Completed masked batch probe retained");return
    prior = previous.get("GPU_elapsed_seconds",0.);started = None;stop = [False]
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    job = dict(status="starting",**identity(),config_sha256=config_sha,started_at=previous.get("started_at",now()),
        GPU_elapsed_seconds=prior,restart_command=f"scripts/probe_chat_first_batch.ps1 -Config {config.relative_to(ROOT).as_posix()} -Worker",probe_weights_discarded=True)
    def check():
        if stop[0]: raise InterruptedError("Masked batch probe interrupted; candidate measurements persisted")
        if started is not None and prior+time.monotonic()-started > c["probe_GPU_budget_seconds"]: raise TimeoutError("Cumulative masked batch probe GPU budget exhausted")
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)
    try:
        heartbeat("setup");torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for source in (*SOURCES,*c["source_sha256"],str(config.relative_to(ROOT))):
            target = run/"source"/source;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/source).read_bytes()
            else: shutil.copyfile(ROOT/source,target)
        parent = torch.load(c["parent"]["path"],map_location="cpu",weights_only=False);assert finite_state(parent)
        results = []
        with gpu_lock("cuda"):
            started = time.monotonic();job["status"] = "running"
            device = dict(name=torch.cuda.get_device_name(0),total_bytes=torch.cuda.get_device_properties(0).total_memory)
            for size in c["candidate_batches"]:
                path = run/f"batch-{size}.json"
                if path.exists():
                    saved = read_json(path);assert saved["config_sha256"] == config_sha and saved["batch"] == size
                    results.append(saved);continue
                heartbeat("candidate",batch=size);trainer = None;rows = []
                try:
                    torch.cuda.reset_peak_memory_stats()
                    spec = dict(c["spec"],batch=size)
                    if c["probe_kind"] == "sft":
                        trainer = AssistantTrainer(parent,c["parent"],records,tok,c["data_directory"],spec,c["series_budget"],device="cuda")
                    else:
                        trainer = DialogueTrainer(parent,c["parent"],records,tok,c["data_directory"],replay,spec,c["series_budgets"],device="cuda")
                    count = c["probe_warmup_updates"]+c["probe_measured_updates"]
                    for index in range(count):
                        check();series_before = trainer.sampler.series_tokens;teachers_before = trainer.supervised_tokens
                        inputs_before = trainer.tokens;physical_before = trainer.sampler.physical_tokens
                        row = trainer.step()
                        assert math.isfinite(row["loss"]) and math.isfinite(row["gradient_norm"])
                        row.update(series_delta=trainer.sampler.series_tokens-series_before,
                            teachers_delta=trainer.supervised_tokens-teachers_before,input_delta=trainer.tokens-inputs_before,
                            physical_delta=trainer.sampler.physical_tokens-physical_before)
                        rows.append(row);heartbeat("candidate-update",batch=size,update=index+1)
                    measured = rows[c["probe_warmup_updates"]:]
                    result = dict(status="complete",batch=size,config_sha256=config_sha,finite_forward_backward=True,
                        median_teacher_tokens_per_second=statistics.median(r["teachers_delta"]/r["seconds"] for r in measured),
                        median_series_tokens_per_second=statistics.median(r["series_delta"]/r["seconds"] for r in measured),
                        median_valid_input_tokens_per_second=statistics.median(r["input_delta"]/r["seconds"] for r in measured),
                        median_physical_tokens_per_second=statistics.median(r["physical_delta"]/r["seconds"] for r in measured),
                        peak_allocated_bytes=torch.cuda.max_memory_allocated(),peak_reserved_bytes=torch.cuda.max_memory_reserved(),
                        probe_series_tokens=trainer.sampler.series_tokens,probe_teacher_tokens=trainer.supervised_tokens,
                        measured_updates=len(measured),first_update_seconds=rows[0]["seconds"],rows=rows,created_at=now())
                except torch.cuda.OutOfMemoryError as error:
                    result = dict(status="oom",batch=size,config_sha256=config_sha,finite_forward_backward=False,
                        error=repr(error),completed_rows=rows,
                        probe_teacher_tokens=sum(r["teachers_delta"] for r in rows),
                        probe_series_tokens=sum(r["series_delta"] for r in rows),
                        failed_update_not_counted_as_completed=True,created_at=now())
                finally:
                    del trainer;gc.collect();torch.cuda.empty_cache()
                atomic_json(path,result);results.append(result)
            best = selection(results)
            report = dict(status="complete_masked_CUDA_batch_measurement",kind=c["probe_kind"],config_sha256=config_sha,
                actual_CUDA_BF16=True,finite_forward_backward=True,parent_checkpoint_sha256=c["parent"]["sha256"],data_binding=binding,
                trainer_sha256=sha256(ROOT/trainer_path),implementation=implementation_hashes(),device=device,
                training_shape={k:c["spec"][k] for k in ("context","dtype","backend","compile","accumulation","sampler","training_fast_path")},
                selected_batch=best["batch"],selected_measurement=best,selection_metric="median_teacher_tokens_per_second",
                maximum_successful_batch_within_probed_range=max(r["batch"] for r in results if r["status"] == "complete"),
                candidate_batches=c["candidate_batches"],candidates=results,
                capacity_policy="Finite candidate range; no claim of an exact maximum or all-backend optimum",
                quality_evaluated=False,probe_weights_discarded=True,protected_test_used=False,
                total_probe_teacher_tokens=sum(r.get("probe_teacher_tokens",0) for r in results),
                total_probe_series_tokens=sum(r.get("probe_series_tokens",0) for r in results),
                Chat_adopted=False,requested_five_steps_complete=False,created_at=now())
            atomic_json(run/"batch-report.json",report);heartbeat("complete");job.update(status="complete",completed_at=now())
            print(json.dumps(dict(selected_batch=best["batch"],teacher_tokens_per_second=best["median_teacher_tokens_per_second"],quality_evaluated=False)),flush=True)
    except BaseException as error:job.update(status="failed",error=repr(error));raise
    finally:
        if started is not None:job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser();parser.add_argument("--config",type=Path,required=True);parser.add_argument("--inspect",action="store_true")
    args = parser.parse_args();config = args.config.resolve();assert config.is_relative_to(ROOT/"configs/phase7")
    if args.inspect:
        c,*_ = preflight(config);print(json.dumps(dict(status="CPU_preflight_only",kind=c["probe_kind"],candidate_batches=c["candidate_batches"],GPU_started=False)))
    else:run(config)
