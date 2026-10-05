"""Bounded Base-completion retention after actual mid-training or SFT.

Reuse the adopted root's saved control; no duplicate Base GPU evaluation.
The native Base EOS/role policy is unchanged, including reporting Chat EOT7
as a role leak in an untagged Base completion. No training/test is performed.
"""
import argparse
import math
import os
from pathlib import Path
import shlex
import shutil
import signal
import sys
import time

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.shards import Shard
from jmicro.training import atomic_json, gpu_lock, seed_all
from chat_stage_evidence import resolve_stage
from phase6_performance import identity, alive
from run_chat_sft import SOURCES as TRAINING_SOURCES
import run_complete_text_comparison as native

SOURCES = tuple(dict.fromkeys((*TRAINING_SOURCES, *native.SOURCES,
    "scripts/run_chat_base_retention.py", "scripts/run_chat_base_retention.ps1", "scripts/chat_stage_evidence.py",
    "scripts/evaluate_japanese_base.py", "scripts/prepare_japanese_evaluation.py", "scripts/run_eos_short_pilot.py",
    "src/jmicro/readiness.py", "src/jmicro/japanese_evaluation.py", "src/jmicro/evaluation_memory.py")))


def preflight(args):
    assert args.stage in ("mid-training", "sft") and math.isfinite(args.gpu_budget_seconds) and 0 < args.gpu_budget_seconds <= 1800
    state, tok, provenance = resolve_stage(args.sft_config, args.stage)
    del state
    recipe = read_json(args.sft_config)
    reference_path = args.reference_config.resolve()
    assert reference_path.is_relative_to(ROOT/"configs/phase6")
    reference = read_json(reference_path)
    assert reference["quality_criteria_unchanged"] is True and reference["protected_test_used"] is False
    assert reference["tokenizer_sha256"] == sha256(tok.path) and reference["suite_sha256"] == sha256(ROOT/"eval/base.jsonl")
    assert reference["source_sha256"] == {p: sha256(ROOT/p) for p in reference["source_sha256"]}
    ev = reference["evaluation"]
    assert (ev["dev_documents"], ev["fixed_dev_prefixes"], ev["max_new_tokens"]) == (256, 80, 64)
    assert ev["tasks"] == ["semantics", "jblimp", "jcqa"]
    assert sha256(ROOT/ev["config"]) == ev["config_sha256"]
    assert sha256(ROOT/ev["semantic_suite"]) == ev["semantic_sha256"]
    config = read_json(ROOT/ev["config"])
    assert sha256(Path(config["data"])/"manifest.json") == ev["data_manifest_sha256"]
    assert sha256(Path(reference["dev_shards"])/"manifest.json") == reference["dev_manifest_sha256"]
    dev = Shard(Path(reference["dev_shards"]), "dev")
    control = read_json(Path(recipe["Base_evaluation"]["path"]))
    assert control["checkpoint_sha256"] == provenance["adopted_Base"]["sha256"] and control["evaluation_RNG_isolated"] is True
    assert control["protected_test_used"] is False
    expected = [(d["doc_id"], d["body_tokens"], d["bytes"]) for d in dev.index[:256]]
    assert [(r["doc_id"], r["body_tokens"], r["body_bytes"]) for r in control["body"]["rows"]] == expected
    assert len(expected) == control["body"]["documents"] == 256, "Reuse only the identical accepted control byte budget"
    return tok, provenance, recipe, reference, dev


def run(args):
    directory = (ROOT/args.output).resolve()
    assert directory.is_relative_to(ROOT/"reports/phase7")
    tok, provenance, recipe, reference, dev = preflight(args)
    if args.inspect:
        print("CPU retention preflight only; same accepted256-document control; GPU0")
        return
    binding = dict(stage_provenance=provenance, sft_config_sha256=sha256(args.sft_config),
        reference_config=dict(path=str(args.reference_config.resolve()), sha256=sha256(args.reference_config)),
        control_evaluation=recipe["Base_evaluation"], control_annotations=recipe["Base_annotations"],
        tokenizer=dict(path=str(tok.path), sha256=sha256(tok.path)), suite_sha256=reference["suite_sha256"],
        dev_manifest_sha256=reference["dev_manifest_sha256"], evaluation=reference["evaluation"],
        dtype="bf16", backend="math", max_new_tokens=64, scored_split="dev", protected_test_used=False,
        source_sha256={p: sha256(ROOT/p) for p in SOURCES}, GPU_budget_seconds=args.gpu_budget_seconds,
        policy="Original Base BOS/prefix, EOS3 only; raw EOT7 is a role leak, no Chat role prompt or display repair")
    directory.mkdir(parents=True, exist_ok=True); job_path = directory/"job.json"
    previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["binding"] == binding and not alive(previous)
        if previous["status"] == "complete": print("Completed retention evidence retained"); return
    prior = previous.get("GPU_elapsed_seconds", 0.); started = None; stopped = [False]
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    restart = ["uv", "run", "--frozen", "--extra", "hub", "--extra", "data", "--extra", "ml", "--extra", "export",
        "scripts/run_chat_base_retention.py", "--sft-config", str(args.sft_config), "--reference-config", str(args.reference_config),
        "--stage", args.stage, "--output", str(args.output), "--gpu-budget-seconds", str(args.gpu_budget_seconds)]
    job = dict(status="starting", **identity(), binding=binding, GPU_elapsed_seconds=prior,
        started_at=previous.get("started_at", now()), restart_command=shlex.join(restart))
    def check():
        if stopped[0]: raise InterruptedError("Retention evaluation stopped; completed native sections retained")
        if started is not None and prior+time.monotonic()-started > args.gpu_budget_seconds: raise TimeoutError("Cumulative retention GPU budget exhausted")
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path, job)
    try:
        heartbeat("setup"); torch.set_num_threads(2); seed_all(42); torch.use_deterministic_algorithms(True)
        for source in SOURCES:
            target = directory/"source"/source; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists(): assert sha256(target) == binding["source_sha256"][source]
            else: shutil.copyfile(ROOT/source, target)
        atomic_json(directory/"recipe.json", binding)
        native.RUN = directory  # Process-local output routing; old source/runs remain intact.
        with gpu_lock("cuda"):
            started = time.monotonic()
            ev = native.evaluate(args.stage, dict(checkpoint=provenance["checkpoint"]["path"], checkpoint_sha256=provenance["checkpoint"]["sha256"]),
                dev, tok, reference, binding, heartbeat, check, started+args.gpu_budget_seconds-prior)
            target = directory/args.stage/"evaluation/result.json"
            generation = target.with_name("generation.json")
            check()
            atomic_json(directory/"result.json", dict(status="native_retention_evaluation_complete_pending_all80_content",
                binding=binding, target_evaluation=dict(path=str(target), sha256=sha256(target)),
                target_generation=dict(path=str(generation), sha256=sha256(generation)), control_reused_without_GPU=True,
                target_checkpoint_sha256=ev["checkpoint_sha256"], scientific_teacher_tokens=0,
                protected_test_used=False, Base_adopted=False, Chat_adopted=False, requested_five_steps_complete=False, completed_at=now()))
            heartbeat("complete"); job.update(status="complete", completed_at=now())
    except BaseException as error: job.update(status="failed", error=repr(error)); raise
    finally:
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        expired_after_success = job["status"] == "complete" and job["GPU_elapsed_seconds"] > args.gpu_budget_seconds
        if job["GPU_elapsed_seconds"] > args.gpu_budget_seconds: job.update(status="failed", error="Cumulative retention budget exceeded")
        atomic_json(job_path, job)
        if expired_after_success: raise TimeoutError("Cumulative retention budget exceeded")


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    parser.add_argument("--sft-config", type=Path, required=True)
    parser.add_argument("--reference-config", type=Path, default=ROOT/"configs/phase6/amount_learning_comparison.json")
    parser.add_argument("--stage", choices=("mid-training", "sft"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--gpu-budget-seconds", type=float, default=1800.)
    parser.add_argument("--inspect", action="store_true")
    run(parser.parse_args())
