"""Repeat one quality-screened Base recipe with a distinct actual training seed."""
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
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes
from phase6_performance import alive, identity, finite_state
from seeded_textbook_trainer import make_zero_parent, SeededThreeSourceTrainer
from textbook_quantity_trainer import ThreeSourceIndex, TAG_MAPPING, GENRES
from run_textbook_quantity_comparison import latest_checkpoint, reconcile_metrics, detail
from run_final_base_dev import source_evidence, completed_source, ref
from run_eos_short_pilot import equal_state
import run_complete_text_comparison as evaluation

SOURCES = ("scripts/run_seeded_base_confirmation.py", "scripts/run_seeded_base_confirmation.ps1",
    "scripts/review_seeded_base_confirmation.py", "scripts/seeded_textbook_trainer.py",
    "scripts/run_final_base_dev.py", "scripts/textbook_quantity_trainer.py",
    "scripts/amount_learning_trainer.py", "scripts/run_complete_text_comparison.py",
    "src/jmicro/learning_curve.py", "scripts/resume_curriculum_strategy.py")


def validate_zero(zero, original, seed):
    assert finite_state(zero) and all(zero[k] == 0 for k in ("update", "tokens", "supervised_tokens", "body_bytes"))
    assert not zero["optimizer"]["state"] and zero["spec"] == dict(original["spec"], seed=seed)
    assert zero["model_config"] == original["model_config"] and zero["implementation_sha256"] == original["implementation_sha256"]
    assert zero["shard_manifest_sha256"] == original["shard_manifest_sha256"]
    assert not equal_state(zero["model"], original["model"]) and not equal_state(zero["rng"], original["rng"])
    assert zero["sampler"] == dict(original["sampler"], seed=42, epoch=0, position=0)
    lineage = zero["lineage"]
    assert lineage["kind"] == "independent-seed-zero" and lineage["source_sha256"] == sha256(ROOT/"scripts/seeded_textbook_trainer.py")
    assert all(lineage[k] == seed for k in ("initialization_seed", "training_RNG_seed", "material_shuffle_seed"))


def preflight(path, recipe=None):
    c = read_json(path) if recipe is None else recipe
    source_run = Path(c["source_run"]); completed_source(source_run)
    for key in ("training_config", "source_result", "source_review", "source_annotations"):
        value = c[key]; assert sha256(Path(value["path"])) == value["sha256"]
    base, screen, _, _ = source_evidence(Path(c["training_config"]["path"]), source_run, c["source_point"])
    stable_record = read_json(source_run/"compare-result.json")["stable"][c["source_point"]]
    assert c["stable_reference"]["path"] == stable_record["checkpoint"] and c["stable_reference"]["sha256"] == stable_record["checkpoint_sha256"]
    assert sha256(Path(c["stable_reference"]["path"])) == c["stable_reference"]["sha256"]
    stable = torch.load(c["stable_reference"]["path"], map_location="cpu", weights_only=False)
    schedule = stable["spec"]["curve_schedule"]
    assert schedule["mode"] == "stable" and c["teacher_budget"] == schedule["teachers"] == stable_record["additional_supervised_tokens"]
    assert c["boundaries"] == list(schedule["boundaries"]) and stable["sampler"]["source_teachers"]["short"] == c["teacher_budget"]
    assert c["training_seed"] == 43 and c["source_training_seed"] == stable["spec"]["seed"] == 42
    assert c["arm"] == stable["pilot_binding"]["arm"] and c["pool"] == base["pools"][c["arm"]]
    assert c["peak_lr"] == base["peak_lr"] and c["warmup_updates"] == base["warmup_updates"]
    assert c["decay_teacher_tokens"] == base["decay_teacher_tokens"] == 20000000
    assert c["original_zero"] == base["parent"] and sha256(Path(c["original_zero"]["path"])) == c["original_zero"]["sha256"]
    assert c["implementation"] == implementation_hashes() and c["source_sha256"] == {p:sha256(ROOT/p) for p in SOURCES}
    assert c["kind"] == "independent-training-seed-confirmation" and c["protected_test_used"] is False
    assert c["quality_criteria_unchanged"] is True and math.isfinite(c["GPU_budget_seconds"]) and c["GPU_budget_seconds"] > 0
    assert c["replicate_rule"] == "Same recipe, both independent learned seeds must pass unchanged Base/original-Web screens; no favorable-seed selection or automatic adoption"
    output = (ROOT/c["output"]).resolve()
    assert output.is_relative_to(ROOT/"reports/phase6") and output != source_run.resolve()
    if (output/"job.json").exists() and alive(read_json(output/"job.json")):
        raise ValueError("Independent seed job is already live; do not duplicate")
    return c, base, screen


def freeze(path, args):
    if path.exists(): preflight(path); print("Frozen independent seed recipe retained; no GPU started"); return
    if any(v is None for v in (args.source_run, args.training_config, args.point)):
        raise ValueError("Freeze needs completed --source-run, --training-config and --point")
    source_run = (ROOT/args.source_run).resolve(); training_config = args.training_config.resolve()
    assert training_config.is_relative_to(ROOT/"configs/phase6")
    base, _, _, _ = source_evidence(training_config, source_run, args.point)
    stable = read_json(source_run/"compare-result.json")["stable"][args.point]
    state = torch.load(stable["checkpoint"], map_location="cpu", weights_only=False)
    total = stable["additional_supervised_tokens"]; schedule = state["spec"]["curve_schedule"]
    measured = stable.get("measured_stage_teachers", total)
    throughput = measured/stable["training_step_seconds"]
    assert throughput > 0 and math.isfinite(throughput)
    arm = state["pilot_binding"]["arm"]
    c = dict(version=1, kind="independent-training-seed-confirmation", source_run=str(source_run), source_point=args.point,
        training_config=ref(training_config), source_result=ref(source_run/"compare-result.json"),
        source_review=ref(source_run/"review.json"), source_annotations=ref(source_run/"annotations.json"),
        stable_reference=ref(Path(stable["checkpoint"])), original_zero=base["parent"], arm=arm, pool=base["pools"][arm],
        training_seed=43, source_training_seed=42, teacher_budget=total, boundaries=list(schedule["boundaries"]),
        decay_teacher_tokens=20000000, peak_lr=base["peak_lr"], warmup_updates=base["warmup_updates"],
        GPU_budget_seconds=math.ceil((total+20000000)/throughput*1.3+1800),
        budget_estimate=dict(source_completed_teacher_tokens=measured, source_training_step_seconds=stable["training_step_seconds"],
            observed_teacher_tokens_per_second=throughput, rule="Full repeated stable+equal decay teachers/observed speed*1.3+1800s for setup/two CUDA gates/Japanese evaluation/saving"),
        replicate_rule="Same recipe, both independent learned seeds must pass unchanged Base/original-Web screens; no favorable-seed selection or automatic adoption",
        output="reports/phase6/"+path.stem, implementation=implementation_hashes(), source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        Base_adopted=False, protected_test_used=False, quality_criteria_unchanged=True, requested_five_steps_complete=False, created_at=now())
    preflight(path, c); path.parent.mkdir(parents=True, exist_ok=True); atomic_json(path,c)
    print("Distinct initialization/RNG/material seed43 protocol frozen; no GPU started")


def run(path):
    c, base, _ = preflight(path)
    output = ROOT/c["output"]; output.mkdir(parents=True, exist_ok=True)
    job_path = output/"job.json"; previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["config_sha256"] == sha256(path) and not alive(previous)
        if previous["status"] == "complete": print("Completed independent learning retained"); return
    prior, started, stopped = previous.get("gpu_elapsed_seconds",0.), [None], [False]
    job = dict(status="starting", **identity(), config_sha256=sha256(path), started_at=previous.get("started_at",now()),
        gpu_elapsed_seconds=prior, training_seed=43, Base_adopted=False, protected_test_used=False,
        restart_command=f"scripts/run_seeded_base_confirmation.ps1 -Config {path.relative_to(ROOT).as_posix()} -Worker")
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True)); signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]: raise InterruptedError("Stop requested; completed updates retained")
        if started[0] is not None and prior+time.monotonic()-started[0] > c["GPU_budget_seconds"]:
            raise TimeoutError("Cumulative independent seed GPU budget exhausted")
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started[0] is not None: job["gpu_elapsed_seconds"] = prior+time.monotonic()-started[0]
        atomic_json(job_path,job)
    def save(trainer, folder):
        target = folder/f"checkpoint-{trainer.update:08d}.pt"; trainer.save(target); return target
    def train(trainer, folder, total, label):
        folder.mkdir(parents=True, exist_ok=True); last = latest_checkpoint(folder)
        if last is not None: trainer.load(last)
        log = folder/"metrics.jsonl"; seconds = reconcile_metrics(log,trainer.update)
        with log.open("a", buffering=1) as stream:
            while trainer.sampler.source_teachers["short"] < total:
                try: check()
                except (InterruptedError,TimeoutError): save(trainer,folder); raise
                row = trainer.step(); assert math.isfinite(row["loss"]) and math.isfinite(row["gradient_norm"])
                seconds += row["seconds"]; stream.write(json.dumps(row,allow_nan=False)+"\n")
                if trainer.update%100 == 0: heartbeat(label, teachers=trainer.sampler.source_teachers["short"], teacher_budget=total, loss=row["loss"])
                if trainer.update%250 == 0 or trainer.sampler.source_teachers["short"] in trainer.sampler.boundaries: save(trainer,folder)
        return detail(trainer,save(trainer,folder),trainer.pilot_binding,seconds)
    def gate(build, name):
        gate_path = output/"resume-gate"/name/"result.json"
        if gate_path.exists():
            kept = read_json(gate_path); assert kept["passed"] and kept["config_sha256"] == sha256(path); return kept
        states, histories, teachers, inputs = [], [], 0, 0
        for branch in ("continuous", "resumed"):
            trainer = build(); before = trainer.supervised_tokens, trainer.tokens; rows = []
            for index in range(4):
                check(); rows.append(trainer.step())
                if branch == "resumed" and index == 1:
                    split = output/"resume-gate"/name/"split.pt"; trainer.save(split)
                    del trainer; gc.collect(); torch.cuda.empty_cache(); trainer = build(); trainer.load(split)
            teachers += trainer.supervised_tokens-before[0]; inputs += trainer.tokens-before[1]
            end = output/"resume-gate"/name/(branch+".pt"); trainer.save(end)
            states.append(torch.load(end,map_location="cpu",weights_only=False)); histories.append(rows)
            del trainer; gc.collect(); torch.cuda.empty_cache()
        checks = {k:equal_state(states[0][k],states[1][k]) for k in ("model","optimizer","scheduler","rng","sampler","lineage","tokens","supervised_tokens","body_bytes","token_digest","update")}
        checks["history"] = all([r[k] for r in histories[0]] == [r[k] for r in histories[1]] for k in ("loss","gradient_norm","lr","token_digest","source_teachers"))
        checks["finite"] = all(finite_state(s) for s in states)
        assert all(checks.values()), checks
        record = dict(passed=True,checks=checks,config_sha256=sha256(path),GPU_optimizer_updates=8,
            verification_teacher_tokens=teachers,verification_input_tokens=inputs,training_seed=43)
        atomic_json(gate_path,record); return record
    try:
        heartbeat("setup"); torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES,path.relative_to(ROOT).as_posix()):
            target = output/"source"/relative; target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/relative).read_bytes()
            else: shutil.copyfile(ROOT/relative,target)
        web = TrainView(base["web_shards"],base["web_manifest_sha256"])
        pool = TrainView(c["pool"]["pool"],c["pool"]["manifest_sha256"]); pool.index = ThreeSourceIndex(pool)
        dev = Shard(Path(base["dev_shards"]),"dev"); tok = Tokenizer(ROOT/base["tokenizer"])
        original = torch.load(c["original_zero"]["path"],map_location="cpu",weights_only=False)
        with gpu_lock("cuda"):
            started[0] = time.monotonic(); heartbeat("independent-zero")
            zero_path = output/"initial/checkpoint-00000000.pt"
            if zero_path.exists(): zero = torch.load(zero_path,map_location="cpu",weights_only=False)
            else: zero = make_zero_parent(original,web,zero_path,seed=43,device="cuda")
            validate_zero(zero,original,43); zero_ref = dict(path=str(zero_path),sha256=sha256(zero_path),update=0,tokens_seen=0)
            zero_manifest = dict(config_sha256=sha256(path),parent=zero_ref,original_zero=c["original_zero"],training_seed=43)
            if (output/"zero-binding.json").exists(): assert read_json(output/"zero-binding.json") == zero_manifest
            else: atomic_json(output/"zero-binding.json",zero_manifest)
            gc.collect(); torch.cuda.empty_cache()
            binding = dict(config_sha256=sha256(path),parent=zero_ref,arm=c["arm"],training_seed=43,
                peak_lr=c["peak_lr"],warmup_updates=c["warmup_updates"],optimizer_policy="fresh",initialization="independent-new-random",
                curve_mode="stable",curve_boundaries=c["boundaries"],short_manifest_sha256=c["pool"]["manifest_sha256"])
            def build(): return SeededThreeSourceTrainer(zero,web,pool,"shuffle",dict(web=0,short=c["teacher_budget"]),binding)
            stable_gate = gate(build,"independent-stable")
            trainer = build(); stable = train(trainer,output/"stable",c["teacher_budget"],"stable43")
            del trainer; gc.collect(); torch.cuda.empty_cache()
            stable_state = torch.load(stable["checkpoint"],map_location="cpu",weights_only=False)
            key = "seed43-"+c["source_point"]
            decay_binding = dict(binding,arm=key,curve_mode="decay",curve_boundaries=[20000000],warmup_updates=0,
                optimizer_policy="inherit",initialization="stable-fork",parent=dict(path=stable["checkpoint"],sha256=stable["checkpoint_sha256"],
                    update=stable_state["update"],tokens_seen=stable_state["tokens"],supervised_tokens=stable_state["supervised_tokens"]))
            def build_decay(): return SeededThreeSourceTrainer(stable_state,web,pool,"shuffle",dict(web=0,short=20000000),decay_binding)
            decay_gate = gate(build_decay,"independent-decay")
            trainer = build_decay(); decay = train(trainer,output/"decay",20000000,"decay43")
            del trainer; gc.collect(); torch.cuda.empty_cache()
            evaluation.RUN = output/"evaluation"
            ev = evaluation.evaluate(key,decay,dev,tok,base,decay_binding,heartbeat,check,started[0]+c["GPU_budget_seconds"]-prior)
            result = dict(status="independent_training_complete_pending_all80_content",config_sha256=sha256(path),point=key,
                stable={key:stable},decay={key:decay},evaluations={key:ev},training_seed=43,source_training_seed=42,
                zero_parent=zero_ref,scientific_stable_teachers=c["teacher_budget"],scientific_decay_teachers=20000000,
                verification_teacher_tokens=stable_gate["verification_teacher_tokens"]+decay_gate["verification_teacher_tokens"],
                resume_gates=[stable_gate,decay_gate],GPU_seconds=prior+time.monotonic()-started[0],
                protected_test_used=False,Base_adopted=False,independent_training_seed_confirmed=False,
                requested_five_steps_complete=False,completed_at=now())
            atomic_json(output/"compare-result.json",result); heartbeat("complete"); job.update(status="complete",completed_at=now())
    except BaseException as error: job.update(status="failed",error=repr(error)); raise
    finally:
        if started[0] is not None: job["gpu_elapsed_seconds"] = prior+time.monotonic()-started[0]
        atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser=argparse.ArgumentParser(); parser.add_argument("--config",type=Path,required=True)
    mode=parser.add_mutually_exclusive_group(); mode.add_argument("--freeze",action="store_true"); mode.add_argument("--inspect",action="store_true")
    parser.add_argument("--source-run",type=Path); parser.add_argument("--training-config",type=Path); parser.add_argument("--point")
    args=parser.parse_args(); path=args.config.resolve(); assert path.is_relative_to(ROOT/"configs/phase6")
    if args.freeze: freeze(path,args)
    elif args.inspect: preflight(path); print("Independent seed preflight passed; no GPU started")
    else: run(path)
