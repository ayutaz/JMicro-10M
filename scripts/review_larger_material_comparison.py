"""Review two matched material arms and all160 native Japanese continuations."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from review_amount_learning_comparison import audit_checkpoint
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate
from run_larger_material_comparison import RUN,CONFIG,load_config


def validate_notes(rows,notes,generation_sha):
    assert notes["generation_sha256"]==generation_sha and notes["independent_human_blind"] is False
    assert isinstance(notes["reviewer"],str) and notes["reviewer"].strip()
    scores={n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in notes["notes"]}
    assert len(notes["notes"])==len(scores)==len(rows)==80 and set(scores)=={r["id"] for r in rows}
    for s in scores.values():
        assert all(type(s[k]) is int and s[k] in (0,1,2) for k in ("grammar","relevance","coherence"))
        assert type(s["completion"]) is int and s["completion"] in (0,1)
        assert isinstance(s["rationale"],str) and len(s["rationale"].strip())>=12
    assert all(not scores[r["id"]]["completion"] or r["stop_reason"]=="stop_id" and scores[r["id"]]["relevance"]>=1 and scores[r["id"]]["coherence"]>=1 for r in rows)
    return scores


def point(key,template=False):
    c=load_config();assert key in {name+"-1000000000" for name in c["arms"]}
    progress=read_json(RUN/"progress-result.json");ev=progress["evaluations"][key];trained=progress["decay"][key]
    raw_path=RUN/"evaluation"/key/"evaluation/generation.json";raw_sha=sha256(raw_path)
    assert ev["checkpoint_sha256"]==trained["checkpoint_sha256"] and ev["binding"]==trained["binding"]
    assert ev["evaluation_RNG_isolated"] and not ev["protected_test_used"]
    assert all(ev["diagnostics"][k]["complete"] and ev["diagnostics"][k]["count"]==n for k,n in {"semantics":192,"jblimp":331,"jcqa":1119}.items())
    rows=ev["generation"]["outputs"];validate_rows(rows,Tokenizer(ROOT/c["tokenizer"]))
    cases={r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"]=="dev"}
    assert len(rows)==80 and {r["id"] for r in rows}==set(cases)
    assert all(r["prefix"]==cases[r["id"]]["prefix"] for r in rows) and ev["greedy_rates"]==rate(rows)
    body=ev["body"]
    assert body["documents"]==len(body["rows"])==256 and body["body_bytes"]==472055 and body["body_tokens"]==122343
    assert all(r["body_tokens"]==r["scored_body_tokens"] for r in body["rows"])
    assert math.isclose(body["bpb"],sum(r["body_nll"] for r in body["rows"])/math.log(2)/472055,rel_tol=1e-12)
    note_path=ROOT/f"reports/phase6/larger_material_{key}_notes.json"
    if template:
        assert not note_path.exists(),"Existing notes preserved"
        write_json(note_path,dict(reviewer="Codex nonblind; all80 require individual reading",independent_human_blind=False,
            generation_sha256=raw_sha,notes=[[r["id"],None,None,None,None,""] for r in rows]))
        print(f"Unscored80 template: {note_path}");return
    notes=read_json(note_path);scores=validate_notes(rows,notes,raw_sha)
    arm=key.split("-")[0]
    summary=dict(prepared_tokens=c["prepared_tokens"][arm],stable_teachers=1000000000,decay_teachers=20000000,
        BPB=body["bpb"],rates=ev["greedy_rates"],Japanese={k:ev["diagnostics"][k]["primary"]["accuracy"]["point"] for k in ("semantics","jblimp","jcqa")},
        grammar2=sum(s["grammar"]==2 for s in scores.values()),relevance2=sum(s["relevance"]==2 for s in scores.values()),
        coherent=sum(s["coherence"]==2 for s in scores.values()),appropriate=sum(s["completion"] for s in scores.values()),
        generation_sha256=raw_sha,notes_sha256=sha256(note_path),Base_adopted=False,independent_human_blind=False)
    write_json(RUN/("content-review-"+key+".json"),summary)
    write_json(ROOT/f"reports/phase6/larger_material_{key}_content_review.json",summary)
    return summary,scores,dict(notes=notes["notes"],notes_sha256=sha256(note_path),generation_sha256=raw_sha)


def audit():
    c=load_config();result=read_json(RUN/"compare-result.json");job=read_json(RUN/"job.json")
    assert job["status"]=="complete" and not alive(job)
    assert result["config_sha256"]==job["config_sha256"]==sha256(CONFIG)
    assert result["gpu_seconds"]<=job["gpu_elapsed_seconds"]<=c["GPU_budget_seconds"]
    assert result["scientific_stable_teachers"]==2000000000 and result["scientific_decay_teachers"]==40000000
    assert not result["protected_test_used"] and not result["requested_five_steps_complete"]
    keys={name+"-1000000000" for name in c["arms"]}
    assert set(result["stable"])==set(result["decay"])==set(result["evaluations"])==keys
    summaries={};scores={};annotations={};body_ids=None
    for key in sorted(keys):
        arm=key.split("-")[0]
        history=[json.loads(s) for s in (RUN/arm/"stable/metrics.jsonl").read_text().splitlines()]
        state=audit_checkpoint(result["stable"][key],history,c,"stable",1000000000);del state
        history=[json.loads(s) for s in (RUN/key/"decay/metrics.jsonl").read_text().splitlines()]
        state=audit_checkpoint(result["decay"][key],history,c,"decay",20000000);del state
        summaries[key],scores[key],annotations[key]=point(key)
        summaries[key]["exposure"]={k:result["stable"][key][k] for k in ("genre_teachers","genre_eos","sampler","additional_input_tokens","physical_input_tokens","training_step_seconds")}
        ids=[(r["doc_id"],r["body_tokens"],r["body_bytes"]) for r in result["evaluations"][key]["body"]["rows"]]
        if body_ids is None:body_ids=ids
        else:assert body_ids==ids
    small,large="small-1000000000","large-1000000000"
    relative=quality_gates(result["evaluations"][small],result["evaluations"][large],scores[small],scores[large],"content")
    practical={}
    for key,s in summaries.items():
        checks=dict(grammar_at_least56=s["grammar2"]>=56,coherence_at_least27=s["coherent"]>=27,
            appropriate_at_least27=s["appropriate"]>=27,EOS_at_least37=s["rates"]["eos"]>=37,
            repetition_at_most18=s["rates"]["repetition"]<=18,
            no_empty_role_unicode=all(s["rates"][k]==0 for k in ("empty","role_leak","unicode_failure")))
        original=adoption_checks(read_json(Path(c["reference"]["web_screen"]["path"])),result["evaluations"][key])
        practical[key]=dict(checks=checks,original_Web=original,absolute_screen_pass=all(checks.values()) and all(original.values()),
            Base_adopted=False,final_seed_full_test_pending=True)
    gates=[read_json(p) for p in (RUN/"resume-gate").glob("*/result.json")]
    assert len(gates)==3 and all(g["passed"] and all(g["checks"].values()) for g in gates)
    assert sum(g["verification_teacher_tokens"] for g in gates)==result["verification_teacher_tokens"]
    write_json(RUN/"annotations.json",dict(reviewer="Codex nonblind",independent_human_blind=False,arms=annotations))
    review=dict(status="matched500M_2B_all160_and_actual_learning_evidence_complete",summaries=summaries,
        quantity_comparison=relative,practical=practical,scientific_stable_teachers=2000000000,
        scientific_decay_teachers=40000000,verification_teacher_tokens=result["verification_teacher_tokens"],
        gpu_seconds=result["gpu_seconds"],result_sha256=sha256(RUN/"compare-result.json"),
        annotations_sha256=sha256(RUN/"annotations.json"),interpretation=c["interpretation"],
        unique_exposure_policy=c["unique_exposure_policy"],Base_adopted=False,Chat_adopted=False,
        independent_human_blind=False,old_numerical7_preserved=True,protected_test_used=False,
        requested_five_steps_complete=False,created_at=now())
    write_json(RUN/"review.json",review);write_json(ROOT/"reports/phase6/larger_material_comparison_review.json",review)
    print(json.dumps(dict(comparison=relative,practical=practical),ensure_ascii=False),flush=True)


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    p=argparse.ArgumentParser();p.add_argument("--point",choices=("small-1000000000","large-1000000000"))
    p.add_argument("--template",action="store_true");args=p.parse_args()
    if args.template and not args.point:p.error("--template requires --point")
    point(args.point,args.template) if args.point else audit()
