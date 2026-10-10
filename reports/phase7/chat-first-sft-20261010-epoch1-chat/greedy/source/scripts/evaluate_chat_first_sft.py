"""Durable matched Base/mid/SFT Chat dev evaluation, greedy or seeded sampling.

Each seed retains all 219 raw responses and can use the same content reviewer.
Seeds are repeated measurements of the same families, not independent cases.
"""
import argparse
import gc
import math
import os
from pathlib import Path
import shutil
import shlex
import signal
import sys
import time

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.chat_evaluation import generate_reply, rollout_dialogue, summarize_chat, validate_sampling
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, rng_state, seed_all
from chat_first_contract import resolve_diagnostic as resolve_stage
from evaluate_chat_sft import load_dev, SOURCES as GREEDY_SOURCES
from phase6_performance import identity, alive
from run_chat_first_sft import SOURCES as TRAINING_SOURCES
from run_eos_short_pilot import equal_state

SOURCES = tuple(dict.fromkeys((*GREEDY_SOURCES, *TRAINING_SOURCES,
    "scripts/evaluate_chat_first_sft.py", "scripts/run_chat_first_sft.ps1", "scripts/chat_stage_evidence.py")))


def evaluation_seeds(decoding, seeds):
    if decoding == "greedy":
        if seeds is not None and seeds != [42]: raise ValueError("Greedy comparison uses fixed seed42")
        return [42]
    seeds = [42, 43, 44] if seeds is None else seeds
    if not 3 <= len(seeds) <= 5 or len(set(seeds)) != len(seeds) or any(type(s) is not int or not 0 <= s < 2**63-4 for s in seeds):
        raise ValueError("Sampling requires 3-5 distinct valid seeds; do not select a favorable single seed")
    return seeds


def summarize_seed(saved, cases, contexts, binding):
    assert len(saved["provided"]) == 160 and len(saved["rollouts"]) == 24
    primary = [saved["provided"]["suppressed-"+c["id"]] for c in cases]
    control = [saved["provided"]["unsuppressed-"+c["id"]] for c in cases]
    final = [saved["rollouts"][c["id"]]["replies"][-1] for c in contexts]
    turns = [r for c in contexts for r in saved["rollouts"][c["id"]]["replies"]]
    assert len(turns) == 59
    return dict(status="mechanical_evaluation_complete_pending_all_content_judgments", binding=binding,
        primary=summarize_chat(primary), role_control=summarize_chat(control), own_history_final24=summarize_chat(final),
        own_history_all_turns=summarize_chat(turns), outputs=saved["provided"], rollouts=saved["rollouts"],
        context_scoring_unit="24 families; seed repeats are correlated, not independent extra families",
        grammar_relevance_context_not_scored=True, evaluation_RNG_isolated=True, protected_test_used=False,
        Chat_adopted=False, requested_five_steps_complete=False, completed_at=now())


def run(args):
    directory = (ROOT/args.output).resolve()
    if not directory.is_relative_to(ROOT/"reports/phase7"): raise ValueError("Keep stage evaluation in reports/phase7")
    assert math.isfinite(args.gpu_budget_seconds) and 0 < args.gpu_budget_seconds <= 1800
    seeds = evaluation_seeds(args.decoding, args.seeds)
    state, tok, provenance = resolve_stage(args.sft_config, args.stage)
    sampling = dict(seed=seeds[0], temperature=args.temperature, top_p=args.top_p, top_k=args.top_k)
    if args.decoding == "sampling": validate_sampling(sampling, tok.vocab_size)
    cases, contexts = load_dev(tok, state["model_config"]["max_position_embeddings"])
    if args.inspect:
        print("CPU stage preflight only; explicit diagnostic parent and checkpoint verified; no GPU job started")
        return
    binding = dict(checkpoint=provenance["checkpoint"]["path"], checkpoint_sha256=provenance["checkpoint"]["sha256"],
        stage=args.stage, diagnostic_provenance=provenance, tokenizer_sha256=sha256(tok.path), suite_sha256=sha256(ROOT/"eval/chat.jsonl"),
        max_new_tokens=64, model_context=state["model_config"]["max_position_embeddings"], dtype="bf16", backend="math",
        decoding=args.decoding, evaluation_seeds=seeds, GPU_budget_seconds=args.gpu_budget_seconds,
        source_sha256={p: sha256(ROOT/p) for p in SOURCES}, implementation=implementation_hashes(),
        scored_split="dev", protected_test_used=False,
        protocol="provided80 suppressed + provided80 unsuppressed role control +24 own-history2-4turn dialogues")
    if args.decoding == "sampling": binding["sampling_recipe"] = {k: sampling[k] for k in ("temperature", "top_p", "top_k")}
    directory.mkdir(parents=True, exist_ok=True)
    job_path = directory/"job.json"; previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["binding"] == binding and not alive(previous)
        if previous["status"] == "complete": print("Completed stage evaluation retained"); return
    progress_path = directory/"progress.json"
    saved = read_json(progress_path) if progress_path.exists() else dict(binding=binding, seeds={})
    assert saved["binding"] == binding
    prior = previous.get("GPU_elapsed_seconds", 0.); started = None; stopped = [False]
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    restart = ["uv", "run", "--frozen", "--extra", "hub", "--extra", "data", "--extra", "ml", "--extra", "export",
        "scripts/evaluate_chat_first_sft.py", "--sft-config", str(args.sft_config), "--stage", args.stage, "--decoding", args.decoding,
        "--seeds", *map(str, seeds), "--temperature", str(args.temperature), "--top-p", str(args.top_p), "--top-k", str(args.top_k),
        "--gpu-budget-seconds", str(args.gpu_budget_seconds), "--output", str(args.output)]
    job = dict(status="starting", **identity(), binding=binding, GPU_elapsed_seconds=prior,
        started_at=previous.get("started_at", now()), restart_command=shlex.join(restart))
    def check():
        if stopped[0]: raise InterruptedError("Evaluation stopped; completed cases retained")
        if started is not None and prior+time.monotonic()-started > args.gpu_budget_seconds: raise TimeoutError("Cumulative multi-seed GPU budget exhausted")
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path, job)
    try:
        heartbeat("setup"); torch.set_num_threads(2); seed_all(42); torch.use_deterministic_algorithms(True)
        with gpu_lock("cuda"), sdpa_kernel(SDPBackend.MATH):
            started = time.monotonic()
            model = JMicroModel(state["model_config"]).cuda().eval(); model.load_state_dict(state["model"], strict=True); del state
            before = rng_state()
            for seed in seeds:
                rows = saved["seeds"].setdefault(str(seed), dict(provided={}, rollouts={}))
                sampling_args = None if args.decoding == "greedy" else dict(sampling, seed=seed)
                for suppressed in (True, False):
                    mode = "suppressed" if suppressed else "unsuppressed"
                    for index, case in enumerate(cases):
                        key = mode+"-"+case["id"]
                        if key in rows["provided"]: continue
                        heartbeat("provided-"+mode, evaluation_seed=seed, completed=index, total=80)
                        row = generate_reply(model, tok, case["messages"], "cuda", "bf16", 64, suppressed, check, sampling=sampling_args)
                        row.update({k: case[k] for k in ("id", "family_id", "category", "split", "checks", "messages")})
                        row["history_mode"] = "provided_assistant_history"
                        assert row["full_history_retained"]
                        rows["provided"][key] = row; atomic_json(progress_path, saved)
                for index, case in enumerate(contexts):
                    if case["id"] in rows["rollouts"]: continue
                    heartbeat("own-history", evaluation_seed=seed, completed=index, total=24)
                    row = rollout_dialogue(model, tok, case, "cuda", "bf16", 64, check, sampling=sampling_args)
                    assert row["full_history_retained"], "Do not discard a failed fixed-context task"
                    rows["rollouts"][case["id"]] = row; atomic_json(progress_path, saved)
            assert equal_state(before, rng_state()), "Sampling must not consume training/global RNG"
            references = []
            for seed in seeds:
                heartbeat("save-seed", evaluation_seed=seed)
                leaf = directory/("greedy" if args.decoding == "greedy" else f"seed-{seed}")
                leaf.mkdir(parents=True, exist_ok=True)
                leaf_binding = dict(binding, evaluation_seed=seed)
                if args.decoding == "sampling": leaf_binding["sampling"] = dict(sampling, seed=seed)
                for source in SOURCES:
                    target = leaf/"source"/source; target.parent.mkdir(parents=True, exist_ok=True)
                    if target.exists(): assert sha256(target) == binding["source_sha256"][source]
                    else:
                        assert sha256(ROOT/source) == binding["source_sha256"][source]
                        shutil.copyfile(ROOT/source, target)
                result = summarize_seed(saved["seeds"][str(seed)], cases, contexts, leaf_binding)
                atomic_json(leaf/"recipe.json", leaf_binding); atomic_json(leaf/"result.json", result)
                leaf_job = dict(job, status="complete", binding=leaf_binding, parent_job=str(job_path), parent_binding=binding,
                    GPU_elapsed_scope="whole multi-seed evaluation, not independent per-seed budget", completed_at=now())
                atomic_json(leaf/"job.json", leaf_job)
                references.append(dict(path=str(leaf/"result.json"), sha256=sha256(leaf/"result.json"), seed=seed,
                    primary=result["primary"], own_history_final24=result["own_history_final24"]))
            atomic_json(directory/"summary.json", dict(binding=binding, per_seed=references, seeds=len(seeds),
                family_units="80 provided and24 own-history families; repeated seeds do not multiply independent cases",
                all_seeds_retained=True, grammar_relevance_context_not_scored=True, Chat_adopted=False,
                protected_test_used=False, requested_five_steps_complete=False, completed_at=now()))
            heartbeat("complete"); job.update(status="complete", completed_at=now())
            del model; gc.collect(); torch.cuda.empty_cache()
    except BaseException as error: job.update(status="failed", error=repr(error)); raise
    finally:
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        expired_after_success = job["status"] == "complete" and job["GPU_elapsed_seconds"] > args.gpu_budget_seconds
        if job["GPU_elapsed_seconds"] > args.gpu_budget_seconds:
            job.update(status="failed", error="Cumulative GPU budget exhausted, including final cleanup")
        atomic_json(job_path, job)
        if expired_after_success: raise TimeoutError("Cumulative GPU budget exhausted during final cleanup")


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    parser.add_argument("--sft-config", "--config", type=Path, required=True)
    parser.add_argument("--stage", choices=("base", "epoch1", "epoch2", "epoch3"), required=True)
    parser.add_argument("--decoding", choices=("greedy", "sampling"), default="greedy")
    parser.add_argument("--seeds", type=int, nargs="+")
    parser.add_argument("--temperature", type=float, default=.8)
    parser.add_argument("--top-p", type=float, default=.9)
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--gpu-budget-seconds", type=float, default=1800.)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--inspect", action="store_true")
    run(parser.parse_args())
