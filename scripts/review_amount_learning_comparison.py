"""Audit stage4 learning and all400 raw-bound content judgments, without training."""
import json
import math
import argparse
from itertools import islice
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.learning_curve import curve_lr
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive, finite_state
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import equal_state, rate
from run_amount_learning_comparison import RUN, CONFIG, load_config


def audit_checkpoint(d,history,c,mode,teachers):
    path = Path(d["checkpoint"])
    assert sha256(path) == d["checkpoint_sha256"]
    state = torch.load(path,map_location="cpu",weights_only=False)
    assert finite_state(state) and all(k in state for k in ("optimizer","scheduler","rng","sampler","lineage","token_digest"))
    assert state["pilot_binding"] == d["binding"] and state["spec"]["curve_schedule"]["mode"] == mode
    assert state["spec"]["curve_schedule"]["no_reheat"]
    sampler, lineage = state["sampler"],state["lineage"]
    assert state["supervised_tokens"]-lineage["parent_supervised_tokens"] == d["additional_supervised_tokens"] == teachers
    assert sampler["source_teachers"] == dict(web=0,short=teachers)
    assert state["tokens"]-lineage["parent_tokens"] == d["additional_input_tokens"] == sum(sampler["source_tokens"].values())
    assert d["physical_input_tokens"] == sum(sampler["source_physical_tokens"].values())
    assert sampler["genre_teachers"] == d["genre_teachers"] and sum(d["genre_teachers"].values()) == teachers
    assert sampler["genre_eos"] == d["genre_eos"] and sum(d["genre_eos"].values()) == sampler["source_eos"]["short"]
    count = state["update"]-lineage["parent_update"]
    rows = history[:count]
    assert len(rows) == sampler["position"] == count and state["token_digest"] == rows[-1]["token_digest"]
    assert [r["update"] for r in rows] == list(range(lineage["parent_update"]+1,state["update"]+1))
    consumed = 0
    for local,r in enumerate(rows):
        expected = curve_lr(consumed,c["peak_lr"],mode,c["decay_teacher_tokens"])
        if mode == "stable": expected *= min(1.,(local+1)/c["warmup_updates"])
        assert math.isclose(r["lr"],expected,rel_tol=1e-12)
        assert math.isfinite(r["loss"]) and math.isfinite(r["gradient_norm"])
        following = sum(r["source_teachers"].values())
        assert consumed < following <= teachers
        consumed = following
    assert consumed == teachers and math.isclose(d["training_step_seconds"],sum(r["seconds"] for r in rows),rel_tol=1e-12)
    if mode == "stable":
        assert lineage["parent_update"] == lineage["parent_tokens"] == lineage["parent_supervised_tokens"] == 0
        assert lineage["optimizer_policy"] == "fresh" and d["binding"]["parent"] == c["parent"]
    else:
        parent_path = Path(d["binding"]["parent"]["path"])
        assert sha256(parent_path) == d["binding"]["parent"]["sha256"]
        parent = torch.load(parent_path,map_location="cpu",weights_only=False)
        assert equal_state(lineage["actual_parent_sampler"],parent["sampler"])
        assert lineage["optimizer_policy"] == "inherit" and d["binding"]["warmup_updates"] == 0
        assert lineage["parent_update"] == parent["update"] and lineage["parent_supervised_tokens"] == parent["supervised_tokens"]
        a,b = parent["sampler"]["short"],sampler["short"]
        blocks = a["blocks"]; assert b["blocks"] == blocks
        cursor_inputs = ((b["epoch"]-a["epoch"])*blocks+b["position"]-a["position"])*1024
        assert cursor_inputs == d["physical_input_tokens"]
    return state


def audit():
    c = load_config(); result = read_json(RUN/"compare-result.json"); job = read_json(RUN/"job.json")
    assert job["status"] == "complete" and not alive(job)
    assert result["config_sha256"] == job["config_sha256"] == sha256(CONFIG)
    assert result["gpu_seconds"] <= job["gpu_elapsed_seconds"] <= c["GPU_budget_seconds"]
    assert result["scientific_stable_teachers"] == 3000000000 and result["scientific_decay_teachers"] == 100000000
    assert not result["requested_five_steps_complete"] and not result["protected_test_used"]
    histories = {arm:[json.loads(s) for s in (RUN/arm/"stable/metrics.jsonl").read_text().splitlines()] for arm in c["arms"]}
    for key,d in result["stable"].items():
        arm,point = key.split("-")
        assert int(point) in c["arms"][arm]["boundaries"]
        state = audit_checkpoint(d,histories[arm],c,"stable",int(point)); del state
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    tok = Tokenizer(ROOT/c["tokenizer"]); scores = {}; summaries = {}; body_ids = None
    annotations = dict(reviewer="Codex nonblind",independent_human_blind=False,arms={})
    for key,d in result["decay"].items():
        arm,point = key.split("-")
        assert int(point) in c["arms"][arm]["evaluate"]
        history = [json.loads(s) for s in (RUN/key/"decay/metrics.jsonl").read_text().splitlines()]
        state = audit_checkpoint(d,history,c,"decay",c["decay_teacher_tokens"])
        ev = result["evaluations"][key]; rows = ev["generation"]["outputs"]; validate_rows(rows,tok)
        assert ev["checkpoint_sha256"] == d["checkpoint_sha256"] and ev["binding"] == d["binding"]
        assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
        assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows)
        assert ev["evaluation_RNG_isolated"] and not ev["protected_test_used"] and ev["greedy_rates"] == rate(rows)
        body = ev["body"]
        assert body["documents"] == len(body["rows"]) == 256 and body["body_bytes"] == 472055 and body["body_tokens"] == 122343
        assert all(r["body_tokens"] == r["scored_body_tokens"] for r in body["rows"])
        assert math.isclose(body["bpb"],sum(r["body_nll"] for r in body["rows"])/math.log(2)/472055,rel_tol=1e-12)
        ids = [(r["doc_id"],r["body_bytes"],r["body_tokens"]) for r in body["rows"]]
        if body_ids is None: body_ids = ids
        else: assert body_ids == ids
        assert all(ev["diagnostics"][k]["complete"] and ev["diagnostics"][k]["count"] == n for k,n in {"semantics":192,"jblimp":331,"jcqa":1119}.items())
        note_path = ROOT/f"reports/phase6/amount_learning_{key}_notes.json"
        notes = read_json(note_path)["notes"]
        scores[key] = {n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in notes}
        assert len(notes) == len(scores[key]) == 80 and set(scores[key]) == set(cases)
        assert all(len(s["rationale"]) >= 12 and all(s[k] in (0,1,2) for k in ("grammar","relevance","coherence")) and s["completion"] in (0,1) for s in scores[key].values())
        assert all(not scores[key][r["id"]]["completion"] or r["stop_reason"] == "stop_id" for r in rows)
        annotations["arms"][key] = dict(notes=notes,notes_sha256=sha256(note_path),generation_sha256=sha256(RUN/"evaluation"/key/"evaluation/generation.json"))
        s = scores[key]
        summaries[key] = dict(prepared_tokens=c["prepared_tokens"][arm],stable_teachers=int(point),decay_teachers=c["decay_teacher_tokens"],
            BPB=body["bpb"],rates=ev["greedy_rates"],Japanese={k:ev["diagnostics"][k]["primary"]["accuracy"]["point"] for k in ("semantics","jblimp","jcqa")},
            grammar2=sum(v["grammar"] == 2 for v in s.values()),relevance2=sum(v["relevance"] == 2 for v in s.values()),
            coherent=sum(v["coherence"] == 2 for v in s.values()),appropriate=sum(v["completion"] for v in s.values()),
            stable_exposure={k:result["stable"][key][k] for k in ("additional_input_tokens","physical_input_tokens","genre_teachers","genre_eos","sampler","training_step_seconds")},
            branch_step_seconds=d["training_step_seconds"],peak_allocated_bytes=d["peak_allocated_bytes"])
        del state
    assert len(summaries) == 5
    pairs = [("quantity100Mvs500M","small-1000000000","large-1000000000"),
             ("learning100Mvs500M","large-100000000","large-500000000"),
             ("learning500Mvs1B","large-500000000","large-1000000000"),
             ("learning1Bvs2B","large-1000000000","large-2000000000")]
    comparison = {name:quality_gates(result["evaluations"][a],result["evaluations"][b],scores[a],scores[b],"content" if name.startswith("quantity") else "amount") for name,a,b in pairs}
    practical = {}
    for key,s in summaries.items():
        checks = dict(coherence_at_least27=s["coherent"] >= 27,appropriate_at_least27=s["appropriate"] >= 27,
                      EOS_at_least37=s["rates"]["eos"] >= 37,repetition_at_most18=s["rates"]["repetition"] <= 18,
                      raw_Unicode0=s["rates"]["unicode_failure"] == 0)
        original = adoption_checks(read_json(Path(c["reference"]["web_screen"]["path"])),result["evaluations"][key])
        practical[key] = dict(checks=checks,original_Web=original,absolute_screen_pass=all(checks.values()) and all(original.values()),
                              Base_adopted=False,reason="Research preference and Base final adoption are separate; final recipe/seed and Base criteria still required")
    gates = [read_json(p) for p in (RUN/"resume-gate").glob("*/result.json")]
    assert len(gates) == 3 and all(g["passed"] and all(g["checks"].values()) for g in gates)
    verification = sum(g["verification_teacher_tokens"] for g in gates)
    assert verification == result["verification_teacher_tokens"]
    write_json(RUN/"annotations.json",annotations); write_json(ROOT/"reports/phase6/amount_learning_annotations.json",annotations)
    report = dict(status="stage4_learning_and_all400_content_evidence_complete",summaries=summaries,comparisons=comparison,practical=practical,
        scientific_stable_teachers=3000000000,scientific_decay_teachers=100000000,verification_teacher_tokens=verification,
        CUDA_verification_optimizer_updates=24,gpu_seconds=result["gpu_seconds"],result_sha256=sha256(RUN/"compare-result.json"),
        annotations_sha256=sha256(RUN/"annotations.json"),interpretation=c["interpretation"],unique_exposure_policy=c["unique_exposure_policy"],
        numerical_failures72_unchanged=True,independent_human_blind=False,requested_five_steps_complete=False,protected_test_used=False,created_at=now())
    write_json(RUN/"review.json",report);write_json(ROOT/"reports/phase6/amount_learning_review.json",report)
    print(json.dumps(dict(comparisons=comparison,practical=practical),ensure_ascii=False),flush=True)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7);torch.set_num_threads(2)
    parser = argparse.ArgumentParser();parser.add_argument("--checkpoint");args = parser.parse_args()
    if args.checkpoint:
        c = load_config();d = read_json(RUN/"progress-result.json")["stable"][args.checkpoint]
        arm,point = args.checkpoint.split("-")
        with (RUN/arm/"stable/metrics.jsonl").open() as stream:
            history = [json.loads(s) for s in islice(stream,d["update"])]
        state = audit_checkpoint(d,history,c,"stable",int(point))
        record = dict(status="completed_stable_checkpoint_audited_only",checkpoint=args.checkpoint,
            checkpoint_sha256=d["checkpoint_sha256"],additional_supervised_tokens=d["additional_supervised_tokens"],
            genre_teachers=d["genre_teachers"],decay_and_generation_quality_not_asserted=True,
            requested_five_steps_complete=False,created_at=now())
        write_json(RUN/("checkpoint-audit-"+args.checkpoint+".json"),record)
        print(json.dumps(record),flush=True)
    else: audit()
