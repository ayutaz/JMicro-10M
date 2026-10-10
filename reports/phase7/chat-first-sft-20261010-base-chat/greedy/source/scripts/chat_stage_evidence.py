"""Bind Chat stage evaluation to an adopted root and completed real learning."""
from pathlib import Path

import torch
from jmicro.experiment import ROOT, read_json, sha256
from phase6_performance import alive, finite_state
from run_eos_short_pilot import equal_state


def validate_sft_terminal(state, result, recipe):
    assert finite_state(state) and state["update"] > 0
    assert state["implementation_sha256"] == recipe["implementation"]
    assert state["spec"]["assistant_training"]["data_binding"] == recipe["dialogue_binding"]
    assert equal_state(state["sampler"], result["full_sampler"]) and equal_state(state["lineage"], result["Base_lineage"])
    sampler = state["sampler"]
    assert sampler["series_tokens"] == result["actual_series_tokens"] and sampler["series_budget"] == recipe["series_budget"]
    assert sampler["teacher_tokens"] == state["supervised_tokens"] == result["Assistant_teacher_tokens"]
    assert sampler["input_tokens"] == state["tokens"] == result["valid_input_tokens"]
    assert sampler["physical_tokens"] == result["physical_tokens"] == state["update"]*recipe["spec"]["context"]*recipe["spec"]["batch"]
    assert sampler["eot_teachers"] == sampler["examples"] == result["EOT_teachers"]
    assert state["lineage"]["kind"] == "assistant-sft-fresh-optimizer"
    assert state["lineage"]["route"] == recipe["route"] and state["lineage"]["root_Base_checkpoint"] == result["adopted_Base"]
    assert state["lineage"]["base_checkpoint"] == result["model_parent"] and state["lineage"]["optimizer_policy"] == "fresh"
    assert {k: v for k, v in state["spec"].items() if k != "assistant_training"} == recipe["spec"]
    assert recipe["series_budget"] <= sampler["series_tokens"] < recipe["series_budget"]+recipe["spec"]["context"]+1


def resolve_stage(config_path, stage):
    from run_chat_sft import preflight
    config_path = config_path.resolve()
    assert config_path.is_relative_to(ROOT/"configs/phase7")
    recipe, tokenizer, _ = preflight(config_path)
    root_ref = recipe.get("adopted_Base", recipe["parent"])
    provenance = dict(sft_config=dict(path=str(config_path), sha256=sha256(config_path)), stage=stage, adopted_Base=root_ref)
    result = None
    if stage == "base":
        ref = root_ref
    elif stage == "mid-training":
        if recipe["route"] != "midtraining-sft": raise ValueError("Mid-training control requires a completed mid-training parent")
        ref = recipe["parent"]
        provenance["mid_training"] = recipe["mid_training"]
    elif stage == "sft":
        run = ROOT/recipe["output"]
        job = read_json(run/"job.json")
        if job["status"] != "complete" or alive(job): raise ValueError("SFT learning must actually finish before stage evaluation")
        result = read_json(run/"result.json")
        assert result["status"] == "learning_complete_pending_Chat_quality"
        assert result["config_sha256"] == job["config_sha256"] == sha256(config_path)
        assert not result["Chat_adopted"] and not result["requested_five_steps_complete"]
        assert result["route"] == recipe["route"] and result["model_parent"] == recipe["parent"] and result["adopted_Base"] == root_ref
        assert result["requested_series_budget"] == recipe["series_budget"]
        gate = read_json(run/"resume-gate/result.json")
        assert gate == result["resume_gate"] and gate["passed"] and all(gate["checks"].values()) and gate["GPU_optimizer_updates"] == 8
        assert gate["config_sha256"] == sha256(config_path)
        assert 0 < result["training_step_seconds"] <= job["GPU_elapsed_seconds"] <= recipe["GPU_budget_seconds"]
        ref = dict(path=result["checkpoint"], sha256=result["checkpoint_sha256"])
        provenance["SFT_result"] = dict(path=str(run/"result.json"), sha256=sha256(run/"result.json"))
    else: raise ValueError("Unknown Chat evaluation stage")
    assert sha256(Path(ref["path"])) == ref["sha256"]
    state = torch.load(ref["path"], map_location="cpu", weights_only=False)
    assert state["implementation_sha256"] == recipe["implementation"] and state["update"] > 0 and finite_state(state)
    if stage == "base":
        assert not state["spec"].get("assistant_training") and not state["spec"].get("dialogue_midtraining")
    elif stage == "mid-training":
        assert state["lineage"]["kind"] == "dialogue-midtraining-fresh-optimizer"
    else:
        validate_sft_terminal(state, result, recipe)
    provenance["checkpoint"] = ref
    return state, tokenizer, provenance
