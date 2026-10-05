"""Actual low-alpha learning audit, unchanged reused control and all80 notes."""
import argparse
import json
import math
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_amount_learning_comparison import audit_checkpoint
from review_sequence_objective_comparison import audit_extra
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import equal_state,rate
from run_sequence_objective_low_alpha import CONFIG,RUN,TOTAL,inspect,probe_evidence
import run_sequence_objective_comparison as old

NOTES=ROOT/'reports/phase6/sequence_objective_low_alpha_notes.json'


def matched_scientific_counters(control,candidate):
    for key in ('source_teachers','source_tokens','source_physical_tokens','source_eos','genre_teachers','genre_eos','short'):
        if not equal_state(control['sampler'][key],candidate['sampler'][key]):
            raise ValueError('Reused control input/counter differs: '+key)
    if control['token_digest']!=candidate['token_digest']:
        raise ValueError('Reused control token digest differs')


def point(template=False):
    c,base,_,_=inspect(CONFIG);progress=read_json(RUN/'progress-result.json')
    d=progress['checkpoints']['CE_UL'];ev=progress['evaluations']['CE_UL'];rows=ev['generation']['outputs']
    assert d['binding']['config_sha256']==sha256(CONFIG) and d['binding']==ev['binding']
    assert ev['checkpoint_sha256']==d['checkpoint_sha256'] and ev['evaluation_RNG_isolated'] and not ev['protected_test_used']
    assert all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
    validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    assert len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
    assert ev['greedy_rates']==rate(rows)
    body=ev['body'];assert body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343
    assert all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows'])
    assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)
    raw=RUN/'evaluation/CE_UL/evaluation/generation.json'
    if template:
        assert not NOTES.exists(),'Preserve existing notes'
        write_json(NOTES,dict(reviewer='Codex nonblind; all80 individually read',independent_human_blind=False,
            generation_sha256=sha256(raw),notes=[[r['id'],None,None,None,None,''] for r in rows]));return
    notes=read_json(NOTES);scores=validate_notes(rows,notes,sha256(raw))
    summary=dict(CE_teachers=TOTAL,BPB=body['bpb'],rates=ev['greedy_rates'],
        grammar2=sum(s['grammar']==2 for s in scores.values()),relevance2=sum(s['relevance']==2 for s in scores.values()),
        coherent=sum(s['coherence']==2 for s in scores.values()),appropriate=sum(s['completion'] for s in scores.values()),
        Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
        generation_sha256=sha256(raw),notes_sha256=sha256(NOTES),Base_adopted=False,independent_human_blind=False)
    write_json(RUN/'content-review.json',summary)
    write_json(ROOT/'reports/phase6/sequence_objective_low_alpha_content_review.json',summary)
    return summary,scores


def audit():
    c,base,_,prior=inspect(CONFIG);job=read_json(RUN/'job.json');result=read_json(RUN/'compare-result.json');probe=probe_evidence()
    assert job['status']=='complete' and not alive(job) and job['config_sha256']==result['config_sha256']==sha256(CONFIG)
    assert result['new_scientific_teacher_tokens']==TOTAL and result['compared_teacher_tokens']==2*TOTAL
    assert result['new_scientific_GPU_seconds']==job['gpu_elapsed_seconds']<=c['GPU_budget_seconds']
    assert job['gpu_elapsed_seconds']+probe['GPU_seconds']<=1800
    assert result['checkpoints']['CE']==prior['checkpoints']['CE'] and result['evaluations']['CE']==prior['evaluations']['CE']
    d=result['checkpoints']['CE_UL'];history=[json.loads(s) for s in (RUN/'CE_UL/training/metrics.jsonl').read_text().splitlines()]
    candidate=audit_checkpoint(d,history,dict(c,decay_teacher_tokens=TOTAL),'decay',TOTAL)
    extra=audit_extra(candidate,d,history,dict(objectives={'CE_UL':c['objective']}))
    control=torch.load(prior['checkpoints']['CE']['checkpoint'],map_location='cpu',weights_only=False)
    matched_scientific_counters(control,candidate)
    summary,scores=point()
    control_rows=prior['evaluations']['CE']['generation']['outputs']
    control_scores=validate_notes(control_rows,read_json(Path(c['control_notes']['path'])),c['control_generation']['sha256'])
    bodies=[prior['evaluations']['CE']['body'],result['evaluations']['CE_UL']['body']]
    assert [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in bodies[0]['rows']]==[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in bodies[1]['rows']]
    comparison=quality_gates(prior['evaluations']['CE'],result['evaluations']['CE_UL'],control_scores,scores,'content')
    checks=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
        appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=summary['rates']['eos']>=37,
        repetition_at_most18=summary['rates']['repetition']<=18,
        no_empty_role_unicode=all(summary['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    original=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),result['evaluations']['CE_UL'])
    report=dict(status='matched_reused_CE_and_actual_low_alpha25M_all80_complete',summary=summary,
        objective_comparison=comparison,practical=dict(checks=checks,original_Web=original,
            absolute_screen_pass=all(checks.values()) and all(original.values())),
        new_scientific_teacher_tokens=TOTAL,reused_control_teacher_tokens=TOTAL,compared_teacher_tokens=2*TOTAL,
        verification_teacher_tokens=probe['verification_teacher_tokens'],new_scientific_GPU_seconds=job['gpu_elapsed_seconds'],
        verification_GPU_seconds=probe['GPU_seconds'],extra_generation_accounting=extra,
        result_sha256=sha256(RUN/'compare-result.json'),notes_sha256=sha256(NOTES),
        Base_adopted=False,Chat_adopted=False,independent_human_blind=False,protected_test_used=False,
        old_numerical7_preserved=True,requested_five_steps_complete=False,created_at=now())
    write_json(RUN/'review.json',report);write_json(ROOT/'reports/phase6/sequence_objective_low_alpha_review.json',report)
    print(json.dumps(report,ensure_ascii=False))


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    p=argparse.ArgumentParser();p.add_argument('--template',action='store_true');args=p.parse_args()
    point(True) if args.template else audit()
