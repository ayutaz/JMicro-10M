"""Audit a completed independent training seed and all80 native dev judgments."""
import argparse
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive
from run_eos_short_pilot import equal_state, rate
from review_eos_5b_finish import validate_rows
from review_amount_learning_comparison import audit_checkpoint
from review_textbook_quantity_comparison import validate_notes
from run_eos_complete_100m import adoption_checks
from run_final_base_dev import screen_checks
from run_seeded_base_confirmation import preflight, validate_zero
from textbook_quantity_trainer import TAG_MAPPING, GENRES


def completed(run):
    job = read_json(run/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Independent learning must actually finish before content review")
    return job


def audit_replicate_checkpoint(record, history, config, mode, total, config_sha):
    state = audit_checkpoint(record,history,config,mode,total)
    assert state["spec"]["seed"] == state["sampler"]["short"]["seed"] == 43
    assert state["sampler"]["genre_tag_mapping"] == TAG_MAPPING
    assert set(state["sampler"]["genre_teachers"]) == set(state["sampler"]["genre_eos"]) == set(GENRES)
    provenance = state["lineage"]["independent_training_seed"]
    assert all(provenance[k] == 43 for k in ("seed","initialization_seed","training_RNG_seed","material_shuffle_seed"))
    assert provenance["source_sha256"] == sha256(ROOT/"scripts/seeded_textbook_trainer.py")
    assert state["pilot_binding"]["training_seed"] == 43 and state["pilot_binding"]["config_sha256"] == config_sha
    assert len(history) == state["update"]-state["lineage"]["parent_update"]
    return state


def audit_training(c, base, run, result):
    binding = read_json(run/"zero-binding.json")
    assert binding["config_sha256"] == result["config_sha256"] and binding["parent"] == result["zero_parent"]
    assert binding["original_zero"] == c["original_zero"] and binding["training_seed"] == 43
    assert sha256(Path(result["zero_parent"]["path"])) == result["zero_parent"]["sha256"]
    zero = torch.load(result["zero_parent"]["path"],map_location="cpu",weights_only=False)
    original = torch.load(c["original_zero"]["path"],map_location="cpu",weights_only=False)
    validate_zero(zero,original,43)
    key = "seed43-"+c["source_point"]
    assert result["point"] == key and set(result["stable"]) == set(result["decay"]) == set(result["evaluations"]) == {key}
    audit_config = dict(base,parent=result["zero_parent"])
    states = {}
    for mode,total in (("stable",c["teacher_budget"]),("decay",20000000)):
        history = [json.loads(s) for s in (run/mode/"metrics.jsonl").read_text().splitlines()]
        state = audit_replicate_checkpoint(result[mode][key],history,audit_config,mode,total,result["config_sha256"])
        states[mode] = state
    assert states["stable"]["model_config"] == states["decay"]["model_config"] == original["model_config"]
    assert list(states["stable"]["spec"]["curve_schedule"]["boundaries"]) == c["boundaries"]
    assert result["scientific_stable_teachers"] == c["teacher_budget"] and result["scientific_decay_teachers"] == 20000000
    gates = [read_json(run/"resume-gate"/label/"result.json") for label in ("independent-stable","independent-decay")]
    assert equal_state(gates,result["resume_gates"])
    assert all(g["passed"] and all(g["checks"].values()) and g["GPU_optimizer_updates"] == 8
        and g["training_seed"] == 43 and g["config_sha256"] == result["config_sha256"] for g in gates)
    assert result["verification_teacher_tokens"] == sum(g["verification_teacher_tokens"] for g in gates)
    return states


def review(path,notes_path,template=False):
    recipe = read_json(path); run = ROOT/recipe["output"]; job = completed(run)
    c,base,source_screen = preflight(path)
    result = read_json(run/"compare-result.json")
    assert result["config_sha256"] == job["config_sha256"] == sha256(path)
    assert result["GPU_seconds"] <= job["gpu_elapsed_seconds"] <= c["GPU_budget_seconds"]
    assert result["training_seed"] == 43 and result["source_training_seed"] == 42
    assert not result["Base_adopted"] and not result["protected_test_used"] and not result["requested_five_steps_complete"]
    audit_training(c,base,run,result)
    key = result["point"]; ev = result["evaluations"][key]
    assert ev["checkpoint_sha256"] == result["decay"][key]["checkpoint_sha256"] and ev["binding"] == result["decay"][key]["binding"]
    assert ev["evaluation_RNG_isolated"] and not ev["protected_test_used"]
    assert all(ev["diagnostics"][k]["complete"] and ev["diagnostics"][k]["count"] == n for k,n in {"semantics":192,"jblimp":331,"jcqa":1119}.items())
    rows = ev["generation"]["outputs"]; tok = Tokenizer(ROOT/base["tokenizer"]); validate_rows(rows,tok)
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
    assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows) and rate(rows) == ev["greedy_rates"]
    raw_path = run/"evaluation"/key/"evaluation/generation.json"
    assert equal_state(read_json(raw_path),ev["generation"])
    body = ev["body"]
    assert body["documents"] == len(body["rows"]) == 256 and body["body_bytes"] == 472055 and body["body_tokens"] == 122343
    assert all(r["body_tokens"] == r["scored_body_tokens"] and math.isfinite(r["body_nll"]) for r in body["rows"])
    assert math.isclose(body["bpb"],sum(r["body_nll"] for r in body["rows"])/math.log(2)/472055,rel_tol=1e-12)
    ids = lambda b:[(r["doc_id"],r["body_tokens"],r["body_bytes"]) for r in b["rows"]]
    assert ids(body) == ids(source_screen["body"])
    if template:
        assert not notes_path.exists(),"Existing notes preserved"
        atomic_json(notes_path,dict(generation_sha256=sha256(raw_path),reviewer="Codex nonblind; read all80 new independent outputs",
            independent_human_blind=False,notes=[[r["id"],None,None,None,None,""] for r in rows]))
        print("Unscored80 independent-seed template saved"); return
    notes = read_json(notes_path); scores = validate_notes(rows,notes,sha256(raw_path))
    absolute = screen_checks(ev,scores)
    original = adoption_checks(read_json(Path(base["reference"]["web_screen"]["path"])),ev)
    seed_screen_passed = all(absolute.values()) and all(original.values())
    summary = dict(training_seed=43,prepared_tokens=base["prepared_tokens"][c["arm"]],stable_teachers=c["teacher_budget"],decay_teachers=20000000,
        BPB=body["bpb"],rates=ev["greedy_rates"],grammar2=sum(s["grammar"]==2 for s in scores.values()),
        relevance2=sum(s["relevance"]==2 for s in scores.values()),coherent=sum(s["coherence"]==2 for s in scores.values()),
        appropriate=sum(s["completion"] for s in scores.values()),
        Japanese={k:ev["diagnostics"][k]["primary"]["accuracy"]["point"] for k in ("semantics","jblimp","jcqa")})
    annotations = dict(reviewer=notes["reviewer"],independent_human_blind=False,
        arms={key:dict(notes=notes["notes"],notes_sha256=sha256(notes_path),generation_sha256=sha256(raw_path))})
    atomic_json(run/"annotations.json",annotations)
    report = dict(status="independent_training_seed_all80_and_learning_evidence_complete",point=key,summary=summary,
        absolute_dev_screen=absolute,original_Web=original,eligible_for_final_Base_validation=seed_screen_passed,
        independent_training_seed_screen_passed=seed_screen_passed,actual_independent_training_complete=True,
        source_training_seed=42,replicate_training_seed=43,replicate_rule=c["replicate_rule"],
        result_sha256=sha256(run/"compare-result.json"),annotations_sha256=sha256(run/"annotations.json"),
        notes_sha256=sha256(notes_path),source_review=c["source_review"],source_annotations=c["source_annotations"],
        scientific_stable_teachers=c["teacher_budget"],scientific_decay_teachers=20000000,
        verification_teacher_tokens=result["verification_teacher_tokens"],GPU_seconds=result["GPU_seconds"],
        Base_adopted=False,protected_test_used=False,independent_human_blind=False,quality_criteria_unchanged=True,
        independent_training_seed_confirmed=False,full_dev_and_final_test_pending=True,requested_five_steps_complete=False,created_at=now())
    atomic_json(run/"review.json",report); atomic_json(ROOT/"reports/phase6"/(run.name+"_review.json"),report)
    atomic_json(ROOT/"reports/phase6"/(run.name+"_annotations.json"),annotations)
    print(json.dumps(report,ensure_ascii=False))


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7); torch.set_num_threads(2)
    p=argparse.ArgumentParser(); p.add_argument("--config",type=Path,required=True); p.add_argument("--notes",type=Path,required=True)
    p.add_argument("--template",action="store_true"); args=p.parse_args(); path,notes=args.config.resolve(),args.notes.resolve()
    assert path.is_relative_to(ROOT/"configs/phase6") and notes.is_relative_to(ROOT/"reports/phase6")
    review(path,notes,args.template)
