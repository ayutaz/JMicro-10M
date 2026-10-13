"""Raw-bound Base retention comparison, without automatic Chat acceptance."""
import argparse
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.japanese_evaluation import clustered_ci
from phase6_performance import alive
from review_improved_base import validate_content
from run_eos_short_pilot import rate
from run_chat_base_retention import preflight


def validate_body(body):
    rows = body["rows"]
    assert len(rows) == body["documents"] == 256 and len({r["doc_id"] for r in rows}) == 256
    assert all(type(r["body_tokens"]) is int and r["body_tokens"] == r["scored_body_tokens"] > 0
               and type(r["body_bytes"]) is int and r["body_bytes"] > 0
               and all(math.isfinite(r[k]) and r[k] >= 0 for k in ("body_nll", "eos_nll")) for r in rows)
    assert body["body_bytes"] == sum(r["body_bytes"] for r in rows) and body["body_tokens"] == sum(r["body_tokens"] for r in rows)
    assert math.isclose(body["body_nll"], sum(r["body_nll"] for r in rows), rel_tol=1e-12)
    assert math.isclose(body["bpb"], body["body_nll"]/math.log(2)/body["body_bytes"], rel_tol=1e-12)
    assert body["split"] == "dev" and body["context"] == 1024 and body["stride"] == 512


def paired_bpb(control, target, repetitions=2000, seed=42):
    """Document bootstrap of the byte-weighted ratio, not mean document BPB."""
    for body in (control, target): validate_body(body)
    a, b = control["rows"], target["rows"]
    assert [(r["doc_id"], r["body_tokens"], r["body_bytes"]) for r in a] == [(r["doc_id"], r["body_tokens"], r["body_bytes"]) for r in b]
    delta = np.asarray([(y["body_nll"]-x["body_nll"])/math.log(2) for x, y in zip(a, b, strict=True)])
    byte_count = np.asarray([r["body_bytes"] for r in a], dtype=np.float64)
    draws = np.random.default_rng(seed).integers(0, len(a), (repetitions, len(a)))
    statistics = delta[draws].sum(1)/byte_count[draws].sum(1)
    point = float(delta.sum()/byte_count.sum())
    assert math.isclose(point, target["bpb"]-control["bpb"], rel_tol=1e-10, abs_tol=1e-12)
    interval = np.quantile(statistics, [.025, .975]).tolist()
    return dict(point=point, ci95=interval, documents=len(a), common_bytes=int(byte_count.sum()),
        control_BPB=control["bpb"], target_BPB=target["bpb"], relative_ratio=target["bpb"]/control["bpb"] if control["bpb"] else None,
        degradation_ci_lower_above0=interval[0] > 0, seed=seed, repetitions=repetitions,
        direction="target minus adopted Base; positive means worse",
        note="Paired document resampling, byte-weighted aggregate; not independent seed confirmation or whole-corpus audit")


def summarize(evaluation, scores):
    rates = rate(evaluation["generation"]["outputs"])
    assert rates == evaluation["greedy_rates"]
    content = dict(grammar2=sum(r["grammar"] == 2 for r in scores.values()), relevance2=sum(r["relevance"] == 2 for r in scores.values()),
        coherence2=sum(r["coherence"] == 2 for r in scores.values()), appropriate=sum(r["completion"] for r in scores.values()))
    checks = dict(grammar_at_least56=content["grammar2"] >= 56, coherence_at_least27=content["coherence2"] >= 27,
        appropriate_at_least27=content["appropriate"] >= 27, EOS_at_least37=rates["eos"] >= 37,
        repetition_at_most18=rates["repetition"] <= 18, no_empty_role_unicode=all(rates[k] == 0 for k in ("empty", "role_leak", "unicode_failure")))
    return dict(BPB=evaluation["body"]["bpb"], content=content, rates=rates, existing_Base_absolute_screen=checks,
        screen_passed=all(checks.values()))


def compare(control, target, control_scores, target_scores, cases):
    assert len(cases) == len(control_scores) == len(target_scores) == 80 and set(cases) == set(control_scores) == set(target_scores)
    assert control["evaluation_RNG_isolated"] is target["evaluation_RNG_isolated"] is True
    assert control["protected_test_used"] is target["protected_test_used"] is False
    bpb = paired_bpb(control["body"], target["body"])
    summaries = dict(adopted_Base=summarize(control, control_scores), target=summarize(target, target_scores))
    paired = {}
    for metric in ("grammar", "relevance", "coherence", "completion"):
        rows = []
        for case_id, case in cases.items():
            x, y = control_scores[case_id][metric], target_scores[case_id][metric]
            rows.append(dict(id=case_id, family=case.get("family_id", case_id), difference=(y-x if metric == "completion" else int(y == 2)-int(x == 2))))
        paired[metric] = clustered_ci(rows, key="difference")
    diagnostics = {}
    for task, count in {"semantics":192, "jblimp":331, "jcqa":1119}.items():
        for ev in (control, target):
            assert ev["diagnostics"][task]["complete"] and ev["diagnostics"][task]["count"] == count
        before = control["diagnostics"][task]["primary"]["accuracy"]["point"]
        after = target["diagnostics"][task]["primary"]["accuracy"]["point"]
        diagnostics[task] = dict(control=before, target=after, difference=after-before, examples=count,
            note="Aggregate dev diagnostic, not paired significance or practical acceptance")
    return dict(status="Base_retention_all80_content_comparison_complete_Chat_adoption_pending",
        BPB=bpb, summaries=summaries, paired_content=paired, Japanese=diagnostics,
        historical_Base_BPB_within1percent=target["body"]["bpb"] <= control["body"]["bpb"]*1.01,
        failure_differences={k: summaries["target"]["rates"][k]-summaries["adopted_Base"]["rates"][k] for k in ("eos", "repetition", "empty", "role_leak", "unicode_failure")},
        independent_human_blind=False, protected_test_used=False, Chat_adopted=False, requested_five_steps_complete=False,
        acceptance_policy="Report retention and unchanged Base screen; no automatic Chat selection or relaxed thresholds",
        pending=["matched Chat grammar/relevance/context", "all sampling seeds", "independent blind human judgments/agreement", "final recipe then protected test", "quantization and UI"])


def load_run(run):
    run = run.resolve(); assert run.is_relative_to(ROOT/"reports/phase7")
    job = read_json(run/"job.json")
    if job["status"] != "complete" or alive(job): raise ValueError("Retention GPU evaluation must actually finish before review")
    result = read_json(run/"result.json"); binding = result["binding"]
    assert result["status"] == "native_retention_evaluation_complete_pending_all80_content" and binding == job["binding"]
    assert 0 < job["GPU_elapsed_seconds"] <= binding["GPU_budget_seconds"] and result["control_reused_without_GPU"] is True
    assert all(sha256(run/"source"/p) == digest for p, digest in binding["source_sha256"].items())
    config = Path(binding["stage_provenance"]["sft_config"]["path"])
    args = argparse.Namespace(sft_config=config, reference_config=Path(binding["reference_config"]["path"]),
        stage=binding["stage_provenance"]["stage"], gpu_budget_seconds=binding["GPU_budget_seconds"])
    tok, provenance, recipe, _, _ = preflight(args)
    assert provenance == binding["stage_provenance"] and sha256(config) == binding["sft_config_sha256"]
    assert sha256(args.reference_config) == binding["reference_config"]["sha256"]
    for key in ("target_evaluation", "target_generation"):
        ref = result[key]; path = Path(ref["path"]).resolve()
        assert path.is_relative_to(run) and sha256(path) == ref["sha256"]
    target = read_json(Path(result["target_evaluation"]["path"]))
    assert target["binding"] == binding and target["checkpoint_sha256"] == provenance["checkpoint"]["sha256"]
    assert target["generation"] == read_json(Path(result["target_generation"]["path"]))
    control = read_json(Path(recipe["Base_evaluation"]["path"]))
    control_notes = read_json(Path(recipe["Base_annotations"]["path"]))["notes"]
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    return result, target, control, control_notes, tok, cases


def run(args):
    result, target, control, old_notes, tok, cases = load_run(args.run)
    if args.template:
        assert args.template.resolve().is_relative_to(ROOT/"reports/phase7")
        if args.template.exists(): raise FileExistsError("Preserve existing retention judgments")
        write_json(args.template, dict(generation_sha256=result["target_generation"]["sha256"], reviewer="Codex nonblind",
            independent_human_blind=False, notes=[[r["id"], None, None, None, None, ""] for r in target["generation"]["outputs"]]))
        print("Prepared80 unscored Base-completion notes; not content quality evidence"); return
    notes = read_json(args.notes)
    assert notes["generation_sha256"] == result["target_generation"]["sha256"]
    assert notes["reviewer"] == "Codex nonblind" and notes["independent_human_blind"] is False
    a = validate_content(old_notes, control, tok, cases); b = validate_content(notes["notes"], target, tok, cases)
    report = compare(control, target, a, b, cases)
    report.update(binding=result["binding"], result_sha256=sha256(args.run/"result.json"), target_notes_sha256=sha256(args.notes), reviewed_at=now())
    output = args.run/"retention_review.json"
    if output.exists() and read_json(output)["target_notes_sha256"] != report["target_notes_sha256"]: raise FileExistsError("Preserve prior retention notes")
    write_json(output, report)
    print("Reviewed all80 native Base completions; retention reported, Chat acceptance still pending")


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser(); parser.add_argument("--run", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--template", type=Path); mode.add_argument("--notes", type=Path)
    run(parser.parse_args())
