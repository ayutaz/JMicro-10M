"""Audit actual paired objective learning and all160 original content notes."""
import argparse
import json
import math
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from review_amount_learning_comparison import audit_checkpoint
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate,equal_state
from sequence_objective_trainer import source_binding
from run_sequence_objective_comparison import CONFIG,PROBE_CONFIG,RUN,TOTAL_CE,preflight,source_contract


def point(arm,template=False):
    c=read_json(CONFIG);base,_,_=source_contract()
    progress=read_json(RUN/"progress-result.json");ev=progress["evaluations"][arm];d=progress["checkpoints"][arm]
    assert ev["checkpoint_sha256"]==d["checkpoint_sha256"] and ev["binding"]==d["binding"]
    assert d["binding"]["config_sha256"]==sha256(CONFIG) and ev["evaluation_RNG_isolated"] and not ev["protected_test_used"]
    assert all(ev["diagnostics"][k]["complete"] and ev["diagnostics"][k]["count"]==n for k,n in {"semantics":192,"jblimp":331,"jcqa":1119}.items())
    rows=ev["generation"]["outputs"];validate_rows(rows,Tokenizer(ROOT/base["tokenizer"]))
    cases={r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"]=="dev"}
    assert len(rows)==80 and {r["id"] for r in rows}==set(cases) and all(r["prefix"]==cases[r["id"]]["prefix"] for r in rows)
    assert ev["greedy_rates"]==rate(rows)
    body=ev["body"]
    assert body["documents"]==len(body["rows"])==256 and body["body_bytes"]==472055 and body["body_tokens"]==122343
    assert all(r["body_tokens"]==r["scored_body_tokens"] for r in body["rows"])
    assert math.isclose(body["bpb"],sum(r["body_nll"] for r in body["rows"])/math.log(2)/472055,rel_tol=1e-12)
    raw=RUN/"evaluation"/arm/"evaluation/generation.json";note=ROOT/f"reports/phase6/sequence_objective_{arm}_notes.json"
    if template:
        assert not note.exists(),"Existing notes preserved"
        write_json(note,dict(reviewer="Codex nonblind; all80 individually read",independent_human_blind=False,
                            generation_sha256=sha256(raw),notes=[[r["id"],None,None,None,None,""] for r in rows]));return
    notes=read_json(note);scores=validate_notes(rows,notes,sha256(raw))
    summary=dict(CE_teachers=TOTAL_CE,BPB=body["bpb"],rates=ev["greedy_rates"],
        grammar2=sum(s["grammar"]==2 for s in scores.values()),relevance2=sum(s["relevance"]==2 for s in scores.values()),
        coherent=sum(s["coherence"]==2 for s in scores.values()),appropriate=sum(s["completion"] for s in scores.values()),
        Japanese={k:ev["diagnostics"][k]["primary"]["accuracy"]["point"] for k in ("semantics","jblimp","jcqa")},
        generation_sha256=sha256(raw),notes_sha256=sha256(note),Base_adopted=False,independent_human_blind=False)
    write_json(RUN/("content-review-"+arm+".json"),summary)
    write_json(ROOT/f"reports/phase6/sequence_objective_{arm}_content_review.json",summary)
    return summary,scores,dict(notes=notes["notes"],notes_sha256=sha256(note),generation_sha256=sha256(raw))


def audit_extra(state,record,history,c):
    actual=state["lineage"]["sequence_objective"];o=state["spec"]["sequence_objective"]
    assert actual["source_sha256"]==source_binding() and actual["objective"]==o==c["objectives"][record["binding"]["arm"]]
    assert actual==record["sequence_objective"]==history[-1]["sequence_objective"]
    names=("rollout_batches","skipped_rollouts","generated_continuations","generated_body_tokens","generated_EOS",
           "negative_token_positions","extra_valid_input_tokens","extra_physical_input_tokens")
    previous={key:0 for key in names}
    for local,row in enumerate(history,1):
        values=row["sequence_objective"]
        assert all(type(values[k]) is int and values[k]>=previous[k] for k in names)
        assert values["rollout_batches"]+values["skipped_rollouts"]==local//o["every_updates"]
        if local%o["every_updates"]:
            assert all(values[k]==previous[k] for k in names) and row["sequence_UL"]==0
        assert 0<=values["negative_token_positions"]<=values["generated_body_tokens"]
        assert values["extra_valid_input_tokens"]<=values["extra_physical_input_tokens"]
        assert values["generated_EOS"]<=values["generated_continuations"]<=values["rollout_batches"]*o["prefixes"]
        assert math.isfinite(row["sequence_UL"]) and row["sequence_UL"]>=0
        assert math.isclose(row["optimization_loss"],row["loss"]+o["alpha"]*row["sequence_UL"],rel_tol=1e-12)
        previous={k:values[k] for k in names}
    assert actual["rollout_batches"]>0 and actual["skipped_rollouts"]==0 and actual["extra_physical_input_tokens"]>0
    return actual


def audit():
    c,base,_=preflight(CONFIG);job=read_json(RUN/"job.json");result=read_json(RUN/"compare-result.json")
    assert job["status"]=="complete" and not alive(job) and result["config_sha256"]==job["config_sha256"]==sha256(CONFIG)
    assert result["scientific_teacher_tokens"]==50000000 and not result["protected_test_used"]
    assert result["scientific_GPU_seconds"]<=job["gpu_elapsed_seconds"]<=c["GPU_budget_seconds"]
    assert job["gpu_elapsed_seconds"]+c["verification_GPU_seconds"]<=1800
    measurement=read_json(RUN/"probe/result.json")
    assert all(g["config_sha256"]==sha256(PROBE_CONFIG) and g["passed"] and all(g["checks"].values()) for g in measurement["gates"].values())
    assert result["verification_teacher_tokens"]==sum(g["verification_teacher_tokens"] for g in measurement["gates"].values())
    summaries={};scores={};annotations={};extras={};native=[]
    audit_config=dict(c,decay_teacher_tokens=TOTAL_CE)
    for arm,d in result["checkpoints"].items():
        history=[json.loads(s) for s in (RUN/arm/"training/metrics.jsonl").read_text().splitlines()]
        state=audit_checkpoint(d,history,audit_config,"decay",TOTAL_CE)
        extras[arm]=audit_extra(state,d,history,c);native.append(state)
        summaries[arm],scores[arm],annotations[arm]=point(arm)
    assert set(summaries)=={"CE","CE_UL"}
    for key in ("source_teachers","source_tokens","source_physical_tokens","source_eos","genre_teachers","genre_eos","short"):
        assert equal_state(native[0]["sampler"][key],native[1]["sampler"][key])
    assert native[0]["token_digest"]==native[1]["token_digest"]
    bodies=[result["evaluations"][a]["body"] for a in ("CE","CE_UL")]
    assert [(r["doc_id"],r["body_tokens"],r["body_bytes"]) for r in bodies[0]["rows"]]==[(r["doc_id"],r["body_tokens"],r["body_bytes"]) for r in bodies[1]["rows"]]
    comparison=quality_gates(result["evaluations"]["CE"],result["evaluations"]["CE_UL"],scores["CE"],scores["CE_UL"],"content")
    practical={}
    for arm,s in summaries.items():
        checks=dict(grammar_at_least56=s["grammar2"]>=56,coherence_at_least27=s["coherent"]>=27,appropriate_at_least27=s["appropriate"]>=27,
                    EOS_at_least37=s["rates"]["eos"]>=37,repetition_at_most18=s["rates"]["repetition"]<=18,
                    no_empty_role_unicode=all(s["rates"][k]==0 for k in ("empty","role_leak","unicode_failure")))
        original=adoption_checks(read_json(Path(base["reference"]["web_screen"]["path"])),result["evaluations"][arm])
        practical[arm]=dict(checks=checks,original_Web=original,absolute_screen_pass=all(checks.values()) and all(original.values()),
                            Base_adopted=False,final_seed_full_test_pending=True)
    write_json(RUN/"annotations.json",dict(reviewer="Codex nonblind",independent_human_blind=False,arms=annotations))
    report=dict(status="matched_CE_sequence_UL_learning_and_all160_content_evidence_complete",summaries=summaries,
        objective_comparison=comparison,practical=practical,extra_generation_accounting=extras,scientific_teacher_tokens=50000000,
        verification_teacher_tokens=result["verification_teacher_tokens"],scientific_GPU_seconds=job["gpu_elapsed_seconds"],
        verification_GPU_seconds=c["verification_GPU_seconds"],result_sha256=sha256(RUN/"compare-result.json"),
        annotations_sha256=sha256(RUN/"annotations.json"),Base_adopted=False,Chat_adopted=False,
        independent_human_blind=False,protected_test_used=False,old_numerical7_preserved=True,requested_five_steps_complete=False,created_at=now())
    write_json(RUN/"review.json",report);write_json(ROOT/"reports/phase6/sequence_objective_comparison_review.json",report)
    print(json.dumps(dict(comparison=comparison,practical=practical),ensure_ascii=False))


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    p=argparse.ArgumentParser();p.add_argument("--point",choices=("CE","CE_UL"));p.add_argument("--template",action="store_true")
    args=p.parse_args()
    if args.template and not args.point:p.error("Template requires --point")
    point(args.point,args.template) if args.point else audit()
