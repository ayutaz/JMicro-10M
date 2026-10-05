"""Review one completed stable extension and preserve raw-bound evidence.

Passing research gates or the dev screen does not adopt a final Base. Final
recipe, repeated-seed/full evaluation and protected-test evidence stay separate.
"""
import argparse
import json
import math
from pathlib import Path
import sys
import tarfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive, finite_state
from review_amount_learning_comparison import audit_checkpoint
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import equal_state, rate
from run_improved_base import preflight


def audit_extension(record, history, parent, recipe, base):
    """Audit only new metric rows, while retaining cumulative stable counters."""
    path = Path(record["checkpoint"])
    assert sha256(path) == record["checkpoint_sha256"]
    state = torch.load(path, map_location="cpu", weights_only=False)
    assert finite_state(state)
    assert all(k in state for k in ("optimizer", "scheduler", "rng", "lineage", "sampler", "token_digest"))
    assert state["pilot_binding"] == record["binding"]
    curve = state["spec"]["curve_schedule"]
    target = recipe["target_teachers"]
    assert curve["mode"] == "stable" and curve["no_reheat"] and curve["teachers"] == target
    assert tuple(curve["boundaries"]) == (*parent["spec"]["curve_schedule"]["boundaries"], target)
    extension = state["lineage"]["stable_extension"]
    assert extension["parent_sha256"] == recipe["parent"]["sha256"]
    assert extension["parent_update"] == parent["update"] and extension["parent_tokens"] == parent["tokens"]
    assert extension["parent_supervised_tokens"] == parent["supervised_tokens"]
    assert equal_state(extension["parent_lineage"], parent["lineage"])
    assert extension["old_teacher_budget"] == parent["spec"]["curve_schedule"]["teachers"]
    assert extension["new_teacher_budget"] == target
    assert extension["extension_implementation_sha256"] == sha256(ROOT/"scripts/extend_amount_learning_trainer.py")
    sampler, lineage = state["sampler"], state["lineage"]
    assert sampler["source_teachers"] == dict(web=0, short=target)
    assert state["supervised_tokens"]-lineage["parent_supervised_tokens"] == record["additional_supervised_tokens"] == target
    assert state["tokens"]-lineage["parent_tokens"] == record["additional_input_tokens"] == sum(sampler["source_tokens"].values())
    assert record["physical_input_tokens"] == sum(sampler["source_physical_tokens"].values())
    assert record["update"] == state["update"] and record["tokens"] == state["tokens"]
    assert record["supervised_tokens"] == state["supervised_tokens"]
    assert equal_state(record["sampler"], sampler)
    assert sampler["genre_teachers"] == record["genre_teachers"] and sum(record["genre_teachers"].values()) == target
    assert sampler["genre_eos"] == record["genre_eos"] and sum(record["genre_eos"].values()) == sampler["source_eos"]["short"]
    assert len(history) == state["update"]-parent["update"] > 0
    assert sampler["position"] == state["update"]-lineage["parent_update"]
    assert [r["update"] for r in history] == list(range(parent["update"]+1, state["update"]+1))
    consumed = parent["sampler"]["source_teachers"]["short"]
    assert record["measured_stage_teachers"] == target-consumed
    for row in history:
        assert math.isfinite(row["loss"]) and math.isfinite(row["gradient_norm"])
        assert math.isclose(row["lr"], base["peak_lr"], rel_tol=1e-12)
        following = sum(row["source_teachers"].values())
        assert consumed < following <= target
        consumed = following
    assert consumed == target and state["token_digest"] == history[-1]["token_digest"]
    assert math.isclose(record["training_step_seconds"], sum(r["seconds"] for r in history), rel_tol=1e-12)
    a, b = parent["sampler"]["short"], sampler["short"]
    assert a["blocks"] == b["blocks"]
    cursor_inputs = ((b["epoch"]-a["epoch"])*a["blocks"]+b["position"]-a["position"])*state["spec"]["context"]
    assert cursor_inputs == record["physical_input_tokens"]-sum(parent["sampler"]["source_physical_tokens"].values())
    return state


def validate_content(notes, evaluation, tokenizer, cases):
    rows = evaluation["generation"]["outputs"]
    validate_rows(rows, tokenizer)
    assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
    assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows)
    assert evaluation["evaluation_RNG_isolated"] and not evaluation["protected_test_used"]
    assert evaluation["greedy_rates"] == rate(rows)
    scores = {n[0]:dict(grammar=n[1], relevance=n[2], coherence=n[3], completion=n[4], rationale=n[5]) for n in notes}
    assert len(notes) == len(scores) == 80 and set(scores) == set(cases)
    assert all(all(type(n[i]) is int and n[i] in (0, 1, 2) for i in (1, 2, 3))
               and type(n[4]) is int and n[4] in (0, 1) and isinstance(n[5], str) and len(n[5]) >= 12 for n in notes)
    assert all(not scores[r["id"]]["completion"] or r["stop_reason"] == "stop_id"
               and scores[r["id"]]["relevance"] >= 1 and scores[r["id"]]["coherence"] >= 1 for r in rows)
    return scores


def review(config, notes_path):
    recipe = read_json(config)
    run = (ROOT/recipe["output"]).resolve()
    job = read_json(run/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Improved Base job must actually finish before review")
    recipe, base, parent, source, _ = preflight(config)
    result = read_json(run/"compare-result.json")
    assert result["config_sha256"] == job["config_sha256"] == sha256(config)
    assert result["GPU_seconds"] <= job["GPU_elapsed_seconds"] <= recipe["GPU_budget_seconds"]
    assert not result["Base_adopted"] and not result["protected_test_used"] and not result["requested_five_steps_complete"]
    parent_key = recipe["parent_point"]
    key = parent["pilot_binding"]["arm"]+"-"+str(recipe["target_teachers"])
    assert set(result["stable"]) == set(result["decay"]) == set(result["evaluations"]) == {parent_key, key}
    for section in ("stable", "decay", "evaluations"):
        assert equal_state(result[section][parent_key], source[section][parent_key])
    history = [json.loads(s) for s in (run/"stable/metrics.jsonl").read_text().splitlines()]
    stable = audit_extension(result["stable"][key], history, parent, recipe, base)
    decay_history = [json.loads(s) for s in (run/"decay/metrics.jsonl").read_text().splitlines()]
    decay = audit_checkpoint(result["decay"][key], decay_history, base, "decay", recipe["decay_teacher_tokens"])
    assert result["decay"][key]["binding"]["parent"]["sha256"] == result["stable"][key]["checkpoint_sha256"]
    assert equal_state(decay["lineage"]["actual_parent_sampler"], stable["sampler"])
    assert result["scientific_stable_teachers"] == recipe["target_teachers"]-parent["sampler"]["source_teachers"]["short"]
    assert result["scientific_decay_teachers"] == recipe["decay_teacher_tokens"] == 20000000
    assert result["additional_valid_input_tokens"] == stable["tokens"]-parent["tokens"]+result["decay"][key]["additional_input_tokens"]
    assert result["additional_physical_input_tokens"] == sum(stable["sampler"]["source_physical_tokens"].values())-sum(parent["sampler"]["source_physical_tokens"].values())+result["decay"][key]["physical_input_tokens"]
    gates = [read_json(run/"resume-gate"/label/"result.json") for label in ("stable-extension", "decay")]
    assert equal_state(gates, result["resume_gates"])
    assert all(g["passed"] and all(g["checks"].values()) and g["config_sha256"] == sha256(config) and g["GPU_optimizer_updates"] == 8 for g in gates)
    assert result["verification_teacher_tokens"] == sum(g["verification_teacher_tokens"] for g in gates)
    ev = result["evaluations"][key]
    assert ev["checkpoint_sha256"] == result["decay"][key]["checkpoint_sha256"] and ev["binding"] == result["decay"][key]["binding"]
    raw_path = run/"evaluation"/key/"evaluation/generation.json"
    assert equal_state(read_json(raw_path), ev["generation"])
    tok = Tokenizer(ROOT/base["tokenizer"])
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    notes_document = read_json(notes_path)
    # New notes must bind the reviewed raw output, preventing accidental reuse
    # of judgments from a different trained point with the same 80 case IDs.
    assert notes_document["generation_sha256"] == sha256(raw_path)
    scores = validate_content(notes_document["notes"], ev, tok, cases)
    inherited = read_json(Path(recipe["source_annotations"]["path"]))["arms"][parent_key]
    old_scores = validate_content(inherited["notes"], result["evaluations"][parent_key], tok, cases)
    body, old_body = ev["body"], result["evaluations"][parent_key]["body"]
    assert body["documents"] == len(body["rows"]) == 256 and body["body_bytes"] == 472055 and body["body_tokens"] == 122343
    assert all(r["body_tokens"] == r["scored_body_tokens"] and math.isfinite(r["body_nll"]) for r in body["rows"])
    assert math.isclose(body["bpb"], sum(r["body_nll"] for r in body["rows"])/math.log(2)/body["body_bytes"], rel_tol=1e-12)
    assert [(r["doc_id"], r["body_tokens"], r["body_bytes"]) for r in body["rows"]] == [(r["doc_id"], r["body_tokens"], r["body_bytes"]) for r in old_body["rows"]]
    assert all(ev["diagnostics"][task]["complete"] and ev["diagnostics"][task]["count"] == count for task, count in {"semantics":192, "jblimp":331, "jcqa":1119}.items())
    rates = ev["greedy_rates"]
    summary = dict(prepared_tokens=base["prepared_tokens"][parent["pilot_binding"]["arm"]],
        stable_teachers=recipe["target_teachers"], decay_teachers=20000000, BPB=body["bpb"], rates=rates,
        grammar2=sum(s["grammar"] == 2 for s in scores.values()), relevance2=sum(s["relevance"] == 2 for s in scores.values()),
        coherent=sum(s["coherence"] == 2 for s in scores.values()), appropriate=sum(s["completion"] for s in scores.values()),
        Japanese={task:ev["diagnostics"][task]["primary"]["accuracy"]["point"] for task in ("semantics", "jblimp", "jcqa")})
    absolute = dict(grammar_at_least56=summary["grammar2"] >= 56, coherence_at_least27=summary["coherent"] >= 27,
        appropriate_at_least27=summary["appropriate"] >= 27, EOS_at_least37=rates["eos"] >= 37,
        repetition_at_most18=rates["repetition"] <= 18, no_empty_role_unicode=all(rates[k] == 0 for k in ("empty", "role_leak", "unicode_failure")))
    original_web = adoption_checks(read_json(Path(base["reference"]["web_screen"]["path"])), ev)
    annotations = dict(reviewer="Codex nonblind", independent_human_blind=False, arms={parent_key:inherited,
        key:dict(notes=notes_document["notes"], notes_sha256=sha256(notes_path), generation_sha256=sha256(raw_path))})
    write_json(run/"annotations.json", annotations)
    report = dict(status="improved_base_stage_evidence_complete", point=key, summary=summary,
        quality_comparison=quality_gates(result["evaluations"][parent_key], ev, old_scores, scores, "amount"),
        absolute_dev_screen=absolute, original_Web=original_web,
        eligible_for_final_Base_validation=all(absolute.values()) and all(original_web.values()),
        result_sha256=sha256(run/"compare-result.json"), annotations_sha256=sha256(run/"annotations.json"),
        notes_sha256=sha256(notes_path), scientific_stable_teachers=result["scientific_stable_teachers"],
        scientific_decay_teachers=result["scientific_decay_teachers"], verification_teacher_tokens=result["verification_teacher_tokens"],
        GPU_seconds=result["GPU_seconds"], independent_human_blind=False, protected_test_used=False,
        quality_criteria_unchanged=True, numerical_failures72_unchanged=True, Base_adopted=False,
        requested_five_steps_complete=False, final_seed_full_evaluation_test_pending=True, created_at=now())
    write_json(run/"review.json", report)
    portable = ROOT/"reports/phase6"/(run.name+"_review.json")
    write_json(portable, report)
    write_json(portable.with_name(run.name+"_annotations.json"), annotations)
    print(json.dumps(report, ensure_ascii=False), flush=True)
    return run, report


def archive(run, config, notes_path):
    job, reviewed = read_json(run/"job.json"), read_json(run/"review.json")
    assert job["status"] == "complete" and not alive(job) and reviewed["status"] == "improved_base_stage_evidence_complete"
    assert reviewed["result_sha256"] == sha256(run/"compare-result.json")
    assert reviewed["annotations_sha256"] == sha256(run/"annotations.json") and reviewed["notes_sha256"] == sha256(notes_path)
    files = {p for p in run.rglob("*") if p.is_file() and p.suffix in (".json", ".jsonl", ".py", ".ps1", ".xml")}
    files.update((config, notes_path, Path(__file__).resolve()))
    assert all(p.resolve().is_relative_to(ROOT) for p in files)
    target = ROOT/"reports/phase6"/(run.name+"_evidence.tar.gz")
    with tarfile.open(target, "w:gz", compresslevel=3) as bundle:
        for path in sorted(files): bundle.add(path, arcname=str(path.relative_to(ROOT)), recursive=False)
    manifest = dict(path=str(target.relative_to(ROOT)), sha256=sha256(target), bytes=target.stat().st_size,
        members=[dict(path=str(p.relative_to(ROOT)), sha256=sha256(p), bytes=p.stat().st_size) for p in sorted(files)],
        limitation="Tensor checkpoints/data remain at bound WSL paths; research/dev evidence does not adopt Base", created_at=now())
    write_json(target.with_name(run.name+"_evidence_manifest.json"), manifest)
    print(f"Archived {len(files)} text files, {manifest['bytes']} bytes", flush=True)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    torch.set_num_threads(2)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--notes", type=Path, required=True)
    parser.add_argument("--archive", action="store_true")
    args = parser.parse_args()
    config, notes_path = args.config.resolve(), args.notes.resolve()
    assert config.is_relative_to(ROOT/"configs/phase6") and notes_path.is_relative_to(ROOT/"reports/phase6")
    run, _ = review(config, notes_path)
    if args.archive: archive(run, config, notes_path)
