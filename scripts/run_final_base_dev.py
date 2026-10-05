"""Conditional full dev confirmation of a quality-screened, completed Base.

No training or protected test. Sampling seeds are not independent training
seeds. This command cannot adopt Base or authorize Chat by itself.
"""
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
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all, rng_state
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import alive, identity, finite_state
from run_eos_short_pilot import equal_state, rate
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from run_textbook_quantity_comparison import CONFIG as QUANTITY_CONFIG, RUN as QUANTITY_RUN, load_config
from run_textbook_improved_base import preflight as extension_preflight
from run_eos_complete_100m import adoption_checks
from run_eos_5b_finish import evaluate
from evaluate_japanese_base import evaluate_long
from compare_base_10b import require_alignment, growth_checks
from compare_base_5b import summarize

SOURCES = ("scripts/run_final_base_dev.py", "scripts/run_final_base_dev.ps1", "scripts/review_final_base_dev.py",
    "scripts/run_eos_5b_finish.py", "scripts/evaluate_japanese_base.py",
    "scripts/compare_base_10b.py", "scripts/compare_base_5b.py",
    "scripts/review_eos_5b_finish.py", "scripts/review_textbook_quantity_comparison.py",
    "scripts/run_textbook_improved_base.py", "scripts/run_eos_complete_100m.py",
    "scripts/run_seeded_base_confirmation.py", "scripts/review_seeded_base_confirmation.py",
    "src/jmicro/readiness.py", "src/jmicro/evaluation_memory.py",
    "src/jmicro/japanese_evaluation.py")


def completed_source(run):
    job = read_json(run/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Source learning must actually finish before final dev confirmation")
    return job


def screen_checks(ev, scores):
    rates = ev["greedy_rates"]
    return dict(grammar_at_least56=sum(s["grammar"] == 2 for s in scores.values()) >= 56,
        coherence_at_least27=sum(s["coherence"] == 2 for s in scores.values()) >= 27,
        appropriate_at_least27=sum(s["completion"] for s in scores.values()) >= 27,
        EOS_at_least37=rates["eos"] >= 37, repetition_at_most18=rates["repetition"] <= 18,
        no_empty_role_unicode=all(rates[k] == 0 for k in ("empty", "role_leak", "unicode_failure")))


def source_evidence(training_config, run, point):
    job = completed_source(run)
    assert run.resolve().is_relative_to(ROOT/"reports/phase6")
    if training_config.resolve() == QUANTITY_CONFIG.resolve():
        base = load_config()
        assert run == QUANTITY_RUN
        status = "matched500M_2B_all160_and_actual_learning_evidence_complete"
    elif read_json(training_config).get("kind") == "independent-training-seed-confirmation":
        from run_seeded_base_confirmation import preflight as seed_preflight
        recipe, base, _ = seed_preflight(training_config)
        assert run == ROOT/recipe["output"]
        status = "independent_training_seed_all80_and_learning_evidence_complete"
    else:
        recipe, base, _, _, _ = extension_preflight(training_config)
        assert run == ROOT/recipe["output"]
        status = "improved_base_stage_evidence_complete"
    reviewed, result = read_json(run/"review.json"), read_json(run/"compare-result.json")
    assert reviewed["status"] == status
    if status != "matched500M_2B_all160_and_actual_learning_evidence_complete":
        assert reviewed["quality_criteria_unchanged"] is True
    assert not reviewed["protected_test_used"] and not reviewed["Base_adopted"]
    assert reviewed["result_sha256"] == sha256(run/"compare-result.json")
    assert reviewed["annotations_sha256"] == sha256(run/"annotations.json")
    assert job["config_sha256"] == result["config_sha256"] == sha256(training_config)
    ev, record = result["evaluations"][point], result["decay"][point]
    assert ev["checkpoint_sha256"] == record["checkpoint_sha256"] and ev["binding"] == record["binding"]
    assert sha256(Path(record["checkpoint"])) == record["checkpoint_sha256"]
    state = torch.load(record["checkpoint"], map_location="cpu", weights_only=False)
    assert finite_state(state) and state["update"] > 0 and state["supervised_tokens"] > 0
    assert state["pilot_binding"] == record["binding"] and state["spec"]["curve_schedule"]["mode"] == "decay"
    assert state["sampler"]["source_teachers"]["short"] == 20000000
    assert ev["evaluation_RNG_isolated"] and not ev["protected_test_used"]
    assert all(ev["diagnostics"][k]["complete"] and ev["diagnostics"][k]["count"] == n
        for k, n in {"semantics":192, "jblimp":331, "jcqa":1119}.items())
    raw_path = run/"evaluation"/point/"evaluation/generation.json"
    assert equal_state(read_json(raw_path), ev["generation"])
    tok = Tokenizer(ROOT/base["tokenizer"])
    rows = ev["generation"]["outputs"]; validate_rows(rows, tok)
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
    assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows) and rate(rows) == ev["greedy_rates"]
    annotations = read_json(run/"annotations.json")["arms"][point]
    assert annotations["generation_sha256"] == sha256(raw_path)
    scores = validate_notes(rows, dict(annotations, generation_sha256=sha256(raw_path),
        reviewer="Inherited individually raw-bound dev review", independent_human_blind=False), sha256(raw_path))
    absolute = screen_checks(ev, scores)
    original = adoption_checks(read_json(Path(base["reference"]["web_screen"]["path"])), ev)
    if not (all(absolute.values()) and all(original.values())):
        raise ValueError("Unchanged absolute Base and original-Web screens must pass before full dev evaluation")
    if status != "matched500M_2B_all160_and_actual_learning_evidence_complete":
        assert reviewed["point"] == point and reviewed["eligible_for_final_Base_validation"]
        assert reviewed["absolute_dev_screen"] == absolute and reviewed["original_Web"] == original
    else:
        practical = reviewed["practical"][point]
        assert practical["absolute_screen_pass"] and practical["checks"] == absolute and practical["original_Web"] == original
    return base, ev, record, annotations


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def preflight(path, recipe=None):
    c = read_json(path) if recipe is None else recipe
    run = Path(c["source_run"])
    # Reject live training before touching model, UI, CUDA, or held-out files.
    completed_source(run)
    for key in ("training_config", "source_review", "source_result", "source_annotations", "checkpoint",
                "tokenizer", "long_config"):
        value = c[key]; assert sha256(Path(value["path"])) == value["sha256"]
    base, screen, record, annotations = source_evidence(Path(c["training_config"]["path"]), run, c["point"])
    assert record["checkpoint"] == c["checkpoint"]["path"] and record["checkpoint_sha256"] == c["checkpoint"]["sha256"]
    assert c["implementation"] == implementation_hashes()
    assert c["source_sha256"] == {p:sha256(ROOT/p) for p in SOURCES}
    assert c["dev_shards"] == base["dev_shards"] and c["dev_manifest_sha256"] == base["dev_manifest_sha256"]
    assert sha256(Path(c["dev_shards"])/"manifest.json") == c["dev_manifest_sha256"]
    assert c["suite_sha256"] == sha256(ROOT/"eval/base.jsonl") == base["suite_sha256"]
    assert c["tokenizer"]["sha256"] == base["tokenizer_sha256"]
    assert c["long_config"]["sha256"] == base["evaluation"]["config_sha256"]
    for value in c["references"].values():
        assert sha256(Path(value["path"])) == value["sha256"]
    assert c["rules"] == dict(maximum_parent_full_BPB_regression=.001, maximum_Web_full_BPB_ratio=1.01,
        fixed_repetition_increase_must_be_less_than=8, all400_raw_failures_zero=True)
    assert c["GPU_budget_seconds"] == 3000 and c["protected_test_used"] is False and c["quality_criteria_unchanged"] is True
    output = (ROOT/c["output"]).resolve()
    assert output.is_relative_to(ROOT/"reports/phase6") and output != run.resolve()
    job_path = output/"job.json"
    if job_path.exists() and alive(read_json(job_path)):
        raise ValueError("Final dev evaluation is already live; do not duplicate it")
    return c, screen, record, annotations


def freeze(path, args):
    if path.exists():
        preflight(path); print("Existing frozen full dev confirmation retained; no GPU started"); return
    if args.source_run is None or args.training_config is None or args.point is None:
        raise ValueError("Freeze requires completed --source-run, --training-config and --point")
    run = (ROOT/args.source_run).resolve(); training_config = args.training_config.resolve()
    assert training_config.is_relative_to(ROOT/"configs/phase6")
    base, _, record, _ = source_evidence(training_config, run, args.point)
    c = dict(version=1, source_run=str(run), point=args.point,
        training_config=ref(training_config), source_review=ref(run/"review.json"),
        source_result=ref(run/"compare-result.json"), source_annotations=ref(run/"annotations.json"),
        checkpoint=dict(path=record["checkpoint"], sha256=record["checkpoint_sha256"]),
        tokenizer=ref(ROOT/base["tokenizer"]), suite_sha256=base["suite_sha256"],
        dev_shards=base["dev_shards"], dev_manifest_sha256=base["dev_manifest_sha256"],
        long_config=ref(ROOT/base["evaluation"]["config"]),
        references={k:base["reference"][k] for k in ("parent_body", "parent_generation", "web_full")},
        rules=dict(maximum_parent_full_BPB_regression=.001, maximum_Web_full_BPB_ratio=1.01,
            fixed_repetition_increase_must_be_less_than=8, all400_raw_failures_zero=True),
        output="reports/phase6/"+path.stem, GPU_budget_seconds=3000,
        budget_basis="Same completed full-dev/400/long128512 evaluation protocol and existing conditional3000s ceiling; no training",
        implementation=implementation_hashes(), source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        scope="Full dev/400/long128512 confirmation only; independent training seed and protected test remain separate",
        Base_adopted=False, protected_test_used=False, quality_criteria_unchanged=True, created_at=now())
    preflight(path, c)
    path.parent.mkdir(parents=True, exist_ok=True); atomic_json(path, c)
    print("Conditional full dev protocol frozen; no GPU started")


def validate_body(body):
    assert body["documents"] == len(body["rows"]) and body["limit_documents"] is None and body["split"] == "dev"
    assert len({r["doc_id"] for r in body["rows"]}) == len(body["rows"])
    assert all(r["body_tokens"] == r["scored_body_tokens"] and math.isfinite(r["body_nll"])
        and math.isfinite(r["eos_nll"]) for r in body["rows"])
    assert body["body_bytes"] == sum(r["body_bytes"] for r in body["rows"])
    assert body["body_tokens"] == sum(r["body_tokens"] for r in body["rows"])
    assert math.isclose(body["body_nll"], sum(r["body_nll"] for r in body["rows"]), rel_tol=1e-12)
    assert math.isclose(body["bpb"], sum(r["body_nll"] for r in body["rows"])/math.log(2)/body["body_bytes"], rel_tol=1e-12)


def validate_generation(generated, screen, tok, reference):
    keys = lambda g: [(r["id"], r["prefix"], r["category"], r["decoding"], r["suppressed"], r["seed"]) for r in g["outputs"]]
    assert keys(generated) == keys(reference)
    for key in ("suite_sha256", "max_new_tokens", "sampling_evaluated", "temperature", "top_p"):
        assert generated[key] == reference[key]
    rows = generated["outputs"]; validate_rows(rows, tok)
    assert len(rows) == 400 and generated["split"] == "dev" and generated["sampling_evaluated"]
    assert generated["max_new_tokens"] == 64 and generated["temperature"] == .8 and generated["top_p"] == .9
    assert all(r["split"] == "dev" for r in rows)
    fixed = {r["id"]:r for r in rows if r["suppressed"] and r["decoding"] == "greedy"}
    assert len(fixed) == 80 and len(screen["generation"]["outputs"]) == 80
    assert all(fixed[r["id"]]["generated_ids"] == r["generated_ids"] for r in screen["generation"]["outputs"])
    return dict(fixed80=rate(list(fixed.values())), all400=rate(rows))


def audit_full(ev, screen, tok, reference_body, reference_generation, web_full):
    assert ev["full"] and ev["evaluation_RNG_isolated"]
    assert ev["checkpoint_sha256"] == screen["checkpoint_sha256"]
    body, generated = ev["body"], ev["generation"]
    require_alignment(body, generated, reference_body, reference_generation)
    validate_body(body)
    rates = validate_generation(generated, screen, tok, reference_generation)
    assert ev["greedy_rates"] == rates["fixed80"]
    current = summarize("candidate", 0, body, generated)
    parent = summarize("parent", 0, reference_body, reference_generation)
    return dict(parent_growth=growth_checks(current, parent), original_Web=adoption_checks(web_full, ev)), current


def run(path):
    c, screen, trained_record, _ = preflight(path)
    output = ROOT/c["output"]; output.mkdir(parents=True, exist_ok=True)
    job_path = output/"job.json"; old = read_json(job_path) if job_path.exists() else {}
    if old:
        assert old["config_sha256"] == sha256(path) and not alive(old)
        if old["status"] == "complete": print("Completed full dev retained"); return
    prior, started, stopped = old.get("gpu_elapsed_seconds", 0.), [None], [False]
    job = dict(status="starting", **identity(), config_sha256=sha256(path),
        started_at=old.get("started_at", now()), gpu_elapsed_seconds=prior,
        restart_command=f"scripts/run_final_base_dev.ps1 -Config {path.relative_to(ROOT).as_posix()} -Worker",
        additional_training_tokens=0, protected_test_used=False, Base_adopted=False)
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError("Evaluation interrupted; completed sections retained")
        if started[0] is not None and prior+time.monotonic()-started[0] > c["GPU_budget_seconds"]:
            raise TimeoutError("Cumulative full dev GPU budget exhausted")
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started[0] is not None: job["gpu_elapsed_seconds"] = prior+time.monotonic()-started[0]
        atomic_json(job_path, job)
    try:
        heartbeat("setup"); torch.set_num_threads(2); seed_all(42); torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES, path.relative_to(ROOT).as_posix()):
            target = output/"source"/relative; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/relative).read_bytes()
            else: shutil.copyfile(ROOT/relative, target)
        dev = Shard(Path(c["dev_shards"]), "dev"); tok = Tokenizer(c["tokenizer"]["path"])
        binding = dict(config_sha256=sha256(path), checkpoint_sha256=c["checkpoint"]["sha256"], source_sha256=c["source_sha256"])
        with gpu_lock("cuda"):
            started[0] = time.monotonic(); heartbeat("full-dev-and400")
            ev = evaluate(Path(c["checkpoint"]["path"]), dev, tok, None, output/"full-dev.json", binding, heartbeat, check, full=True)
            reference_body = read_json(Path(c["references"]["parent_body"]["path"]))["body"]
            reference_generation = read_json(Path(c["references"]["parent_generation"]["path"]))["generation"]
            web_full = read_json(Path(c["references"]["web_full"]["path"]))
            checks, summary = audit_full(ev, screen, tok, reference_body, reference_generation, web_full)
            summary["training_input_tokens"] = trained_record["tokens"]
            state = torch.load(c["checkpoint"]["path"], map_location="cpu", weights_only=False)
            model = JMicroModel(state["model_config"]).to("cuda").eval(); model.load_state_dict(state["model"], strict=True)
            memory = bound_evaluation_cache(model); before = rng_state()
            hook = model.register_forward_pre_hook(lambda *_: check())
            heartbeat("long128512")
            with sdpa_kernel(SDPBackend.MATH):
                long = evaluate_long(NativeLikelihood(model, tok, batch=16), read_json(Path(c["long_config"]["path"])),
                    output, json.dumps(binding, sort_keys=True), started[0]+c["GPU_budget_seconds"]-prior)
            hook.remove(); assert long["complete"] and equal_state(before, rng_state()) and not model.training
            check(); del model, state; gc.collect(); torch.cuda.empty_cache()
            result = dict(status="full_dev_complete_pending_independent_training_seed_test_and_content", binding=binding,
                full_evaluation_sha256=sha256(output/"full-dev.json"), long_generation_sha256=sha256(output/"long-generation.json"),
                summary=summary, checks=checks, full_automatic_conditions_pass=all(v for group in checks.values() for v in group.values()),
                long_generation=long, memory=dict(memory), evaluation_RNG_isolated=True, additional_training_tokens=0,
                GPU_seconds=prior+time.monotonic()-started[0], protected_test_used=False, Base_adopted=False,
                independent_training_seed_confirmed=False, independent_human_blind=False,
                all400_and_long_content_review_pending=True, quality_criteria_unchanged=True, requested_five_steps_complete=False, completed_at=now())
            atomic_json(output/"result.json", result); heartbeat("complete"); job.update(status="complete", completed_at=now())
    except BaseException as error:
        job.update(status="failed", error=repr(error)); raise
    finally:
        if started[0] is not None: job["gpu_elapsed_seconds"] = prior+time.monotonic()-started[0]
        atomic_json(job_path, job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser(); parser.add_argument("--config", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(); mode.add_argument("--freeze", action="store_true"); mode.add_argument("--inspect", action="store_true")
    parser.add_argument("--training-config", type=Path); parser.add_argument("--source-run", type=Path); parser.add_argument("--point")
    args = parser.parse_args(); path = args.config.resolve()
    assert path.is_relative_to(ROOT/"configs/phase6")
    if args.freeze: freeze(path, args)
    elif args.inspect: preflight(path); print("Conditional full dev preflight passed; no GPU started")
    else: run(path)
