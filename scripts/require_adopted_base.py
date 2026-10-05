"""Shared evidence checks for an adopted Base before dialogue GPU training."""
import json
from functools import lru_cache
from pathlib import Path
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.tokenizer import Tokenizer
from review_eos_5b_finish import validate_rows
from run_eos_short_pilot import rate


def require_adopted_base(config):
    for key in ("parent", "Base_acceptance", "Base_evaluation", "Base_annotations", "tokenizer"):
        ref = config[key]
        assert sha256(Path(ref["path"])) == ref["sha256"]
    accepted = read_json(Path(config["Base_acceptance"]["path"]))
    if accepted.get("Base_adopted") is not True:
        raise ValueError("A quality-adopted Base is required before dialogue GPU training")
    assert accepted["checkpoint_sha256"] == config["parent"]["sha256"]
    assert accepted["evaluation_sha256"] == config["Base_evaluation"]["sha256"]
    assert accepted["annotations_sha256"] == config["Base_annotations"]["sha256"]
    assert accepted["quality_criteria_unchanged"] is True
    ev = read_json(Path(config["Base_evaluation"]["path"]))
    assert ev["checkpoint_sha256"] == config["parent"]["sha256"] and ev["evaluation_RNG_isolated"] and not ev["protected_test_used"]
    tok = Tokenizer(config["tokenizer"]["path"])
    # Per-instance cache only: preserve the codec/IDs while reusing repeated
    # conversation bodies during preflight, batch probes and resume builders.
    tok.encode = lru_cache(maxsize=100000)(tok.encode)
    rows = ev["generation"]["outputs"]; validate_rows(rows, tok)
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
    assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows)
    notes = read_json(Path(config["Base_annotations"]["path"]))["notes"]
    scores = {n[0]:n for n in notes}
    assert len(notes) == len(scores) == 80 and set(scores) == set(cases)
    assert all(all(type(n[i]) is int and n[i] in (0,1,2) for i in (1,2,3))
               and type(n[4]) is int and n[4] in (0,1) and isinstance(n[5],str) and len(n[5]) >= 12 for n in notes)
    assert all(not scores[r["id"]][4] or r["stop_reason"] == "stop_id" and scores[r["id"]][2] >= 1 and scores[r["id"]][3] >= 1 for r in rows)
    assert sum(n[1] == 2 for n in notes) >= 56 and sum(n[3] == 2 for n in notes) >= 27 and sum(n[4] for n in notes) >= 27
    rates = rate(rows); assert rates == ev["greedy_rates"]
    assert rates["eos"] >= 37 and rates["repetition"] <= 18 and all(rates[k] == 0 for k in ("unicode_failure", "role_leak", "empty"))
    return tok


def validate_midtraining_state(state, result, recipe, root_ref):
    """Model-parent provenance/accounting only; not CUDA or quality evidence."""
    from phase6_performance import finite_state
    from run_eos_short_pilot import equal_state
    assert finite_state(state) and state["update"] > 0
    lineage = state["lineage"]
    assert lineage["kind"] == "dialogue-midtraining-fresh-optimizer" and lineage["base_checkpoint"] == root_ref
    assert result["Base_lineage"] == lineage and recipe["parent"] == root_ref
    assert state["spec"]["dialogue_midtraining"]["data_binding"] == recipe["mixture_binding"]
    assert state["implementation_sha256"] == recipe["implementation"]
    assert state["sampler"]["budgets"] == recipe["series_budgets"] == result["series_budgets"]
    assert equal_state(state["sampler"], result["full_sampler"])
    sampler = state["sampler"]
    assert all(goal <= sampler["source_series"][source] < goal+state["spec"]["context"]+1
               for source, goal in recipe["series_budgets"].items() if goal)
    assert state["tokens"] == sum(sampler["source_inputs"].values()) == result["valid_input_tokens"]
    assert state["supervised_tokens"] == sum(sampler["source_teachers"].values()) == result["teacher_tokens"]
    assert sum(sampler["source_series"].values()) == result["actual_series_tokens"]
    assert sampler["physical_tokens"] == result["physical_input_tokens"]
    assert sampler["updates"] == state["update"]


def require_sft_parent(config, root_ref):
    """Allow a completed mid-trained descendant without labeling it Base-adopted."""
    route = config.get("route", "direct-sft")
    parent_ref = config["parent"]
    assert sha256(Path(parent_ref["path"])) == parent_ref["sha256"]
    if route == "direct-sft":
        if parent_ref != root_ref: raise ValueError("Direct SFT must start from the adopted Base")
        return
    if route != "midtraining-sft": raise ValueError("Unknown SFT route")
    ref = config["mid_training"]
    result_path, recipe_path = Path(ref["result"]["path"]), Path(ref["config"]["path"])
    from phase6_performance import alive
    run = result_path.parent
    job = read_json(run/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Mid-training must actually finish before SFT")
    assert run.resolve().is_relative_to(ROOT/"reports/phase7")
    assert recipe_path.resolve().is_relative_to(ROOT/"configs/phase7")
    assert sha256(result_path) == ref["result"]["sha256"] and sha256(recipe_path) == ref["config"]["sha256"]
    result, recipe = read_json(result_path), read_json(recipe_path)
    assert result["config_sha256"] == job["config_sha256"] == sha256(recipe_path)
    assert result["checkpoint"] == parent_ref["path"] and result["checkpoint_sha256"] == parent_ref["sha256"]
    assert result["status"] == "learning_complete_pending_Base_retention_and_Chat_ablation"
    assert not result["Chat_adopted"] and not result["protected_test_used"] and not result["requested_five_steps_complete"]
    assert recipe["Base_acceptance"] == config["Base_acceptance"]
    assert recipe["data_manifest_sha256"] == config["data_manifest_sha256"] and recipe["train_records"] == config["train_records"]
    assert recipe["tokenizer"] == config["tokenizer"]
    from run_dialogue_midtraining import SOURCES
    assert recipe["source_sha256"] == {p:sha256(ROOT/p) for p in SOURCES}
    gate = read_json(run/"resume-gate/result.json")
    assert gate == result["resume_gate"] and gate["passed"] and all(gate["checks"].values())
    assert gate["config_sha256"] == sha256(recipe_path) and gate["GPU_optimizer_updates"] == 8
    import torch
    state = torch.load(parent_ref["path"],map_location="cpu",weights_only=False)
    validate_midtraining_state(state, result, recipe, root_ref)
