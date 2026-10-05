"""Actual matched direct-SFT versus mid-training+SFT dev content comparison.

SFT exposure and recipe must match. Added mid-training is separately accounted,
so this experiment is never described as equal total teacher or GPU budgets.
"""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.chat_review import content_review, paired_chat_comparison
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from phase6_performance import alive
from review_chat_sft import load_evaluation
from run_chat_sft import preflight
from run_eos_short_pilot import equal_state
from chat_stage_evidence import validate_sft_terminal


def load_arm(config_path, evaluation_path, notes_path, route):
    recipe, _, _ = preflight(config_path.resolve())
    assert recipe["route"] == route
    run = ROOT/recipe["output"]
    job = read_json(run/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Both SFT jobs must actually finish before ablation review")
    result = read_json(run/"result.json")
    assert result["status"] == "learning_complete_pending_Chat_quality"
    assert result["Chat_adopted"] is False and result["requested_five_steps_complete"] is False
    assert result["config_sha256"] == job["config_sha256"] == sha256(config_path)
    assert result["resume_gate"]["passed"] is True and all(result["resume_gate"]["checks"].values())
    assert result["resume_gate"]["config_sha256"] == result["config_sha256"]
    assert result["route"] == route and result["model_parent"] == recipe["parent"]
    assert result["adopted_Base"] == recipe.get("adopted_Base", recipe["parent"])
    assert result["requested_series_budget"] == recipe["series_budget"]
    assert recipe["series_budget"] <= result["actual_series_tokens"] < recipe["series_budget"]+recipe["spec"]["context"]+1
    assert 0 < result["training_step_seconds"] <= job["GPU_elapsed_seconds"] <= recipe["GPU_budget_seconds"]
    ev, items = load_evaluation(evaluation_path, Path(recipe["tokenizer"]["path"]))
    assert ev["binding"]["checkpoint"] == result["checkpoint"] and ev["binding"]["checkpoint_sha256"] == result["checkpoint_sha256"]
    state = torch.load(result["checkpoint"], map_location="cpu", weights_only=False)
    validate_sft_terminal(state, result, recipe)
    notes = read_json(notes_path)
    report = content_review(ev, sha256(evaluation_path), notes, items)
    refs = dict(config_sha256=sha256(config_path), training_result_sha256=sha256(run/"result.json"),
                evaluation_sha256=sha256(evaluation_path), annotations_sha256=sha256(notes_path),
                checkpoint_sha256=result["checkpoint_sha256"])
    return recipe, result, job, ev, items, report, refs


def validate_matched_sft(direct, main):
    left, right = direct[0], main[0]
    assert left["route"] == "direct-sft" and right["route"] == "midtraining-sft"
    assert left.get("adopted_Base", left["parent"]) == right["adopted_Base"]
    assert left["spec"] == right["spec"], "Match SFT seed, batch, context, LR, warmup and runtime"
    assert all(left[k] == right[k] for k in ("series_budget", "dialogue_binding", "train_records", "data_manifest_sha256", "tokenizer", "implementation", "source_sha256"))
    a, b = direct[1], main[1]
    assert all(equal_state(a[k], b[k]) for k in ("actual_series_tokens", "Assistant_teacher_tokens", "valid_input_tokens", "physical_tokens", "EOT_teachers", "full_sampler")), "Match actual SFT windows/exposure, not just proposed budgets"


def run(args):
    output = args.output.resolve()
    assert output.is_relative_to(ROOT/"reports/phase7")
    if output.exists(): raise FileExistsError("Preserve existing ablation evidence")
    direct = load_arm(args.direct_config, args.direct_evaluation, args.direct_notes, "direct-sft")
    main = load_arm(args.main_config, args.main_evaluation, args.main_notes, "midtraining-sft")
    validate_matched_sft(direct, main)
    report = paired_chat_comparison(direct[3], main[3], direct[4], main[4], direct[5], main[5])
    mid_ref = main[0]["mid_training"]["result"]
    assert sha256(Path(mid_ref["path"])) == mid_ref["sha256"]
    mid = read_json(Path(mid_ref["path"]))
    report.update(reviewed_at=now(), adopted_Base=main[0]["adopted_Base"], references=dict(direct_sft=direct[6], midtraining_sft=main[6], midtraining=mid_ref),
        matched_SFT=dict(series_budget=direct[0]["series_budget"], actual_series=direct[1]["actual_series_tokens"],
            Assistant_teacher_tokens=direct[1]["Assistant_teacher_tokens"], physical_tokens=direct[1]["physical_tokens"], spec=direct[0]["spec"]),
        additional_midtraining=dict(series_budgets=mid["series_budgets"], series_tokens=mid["actual_series_tokens"],
            teacher_tokens=mid["teacher_tokens"], valid_input_tokens=mid["valid_input_tokens"], physical_input_tokens=mid["physical_input_tokens"], training_step_seconds=mid["training_step_seconds"]),
        SFT_GPU_seconds=dict(direct_sft=direct[2]["GPU_elapsed_seconds"], midtraining_sft=main[2]["GPU_elapsed_seconds"]),
        budget_comparison="Same SFT exposure; main route has additional mid-training. Total teachers and GPU budgets differ.")
    write_json(output, report)
    print("Saved matched dev comparison; Base retention, sampling, human agreement and final test remain pending")


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    for name in ("direct-config", "direct-evaluation", "direct-notes", "main-config", "main-evaluation", "main-notes", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    run(parser.parse_args())
