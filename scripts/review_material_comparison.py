"""Audit actual equal300M learning and all160 individually reviewed outputs."""
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.packing_study import teacher_lr
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate
from run_material_comparison import RUN,CONFIG,load_config,validate_parent


def audit():
    c=load_config();result=read_json(RUN/'compare-result.json');job=read_json(RUN/'job.json')
    assert job['status']=='complete' and not alive(job)
    assert result['config_sha256']==job['config_sha256']==sha256(CONFIG)
    assert result['scientific_teacher_tokens']==600000000 and result['gpu_seconds']<=job['gpu_elapsed_seconds']<=1800
    assert not result['requested_five_steps_complete'] and not result['protected_test_used']
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);validate_parent(parent)
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    tok=Tokenizer(ROOT/c['tokenizer']);scores={};summary={};verification=0;annotations=dict(reviewer='Codex nonblind',independent_human_blind=False,arms={})
    body_ids=None
    for arm,d in result['checkpoints'].items():
        assert sha256(Path(d['checkpoint']))==d['checkpoint_sha256']
        state=torch.load(d['checkpoint'],map_location='cpu',weights_only=False)
        assert finite_state(state) and all(k in state for k in ('model','optimizer','scheduler','rng','sampler','lineage','token_digest'))
        assert state['pilot_binding']==d['binding'] and state['sampler']['source_teachers']==c['goals']
        assert state['supervised_tokens']==d['additional_supervised_tokens']==300000000
        assert state['tokens']==d['additional_input_tokens']==sum(state['sampler']['source_tokens'].values())
        assert sum(state['sampler']['source_physical_tokens'].values())==d['physical_input_tokens']
        assert state['lineage']['parent_update']==state['lineage']['parent_tokens']==state['lineage']['parent_supervised_tokens']==0
        assert state['lineage']['optimizer_policy']=='fresh' and state['spec']['warmup']==200
        assert d['binding']['parent']==c['parent'] and d['binding']['short_manifest_sha256']==c['arms'][arm]['manifest_sha256']
        history=[json.loads(s) for s in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        assert len(history)==state['update']==state['sampler']['position']
        assert [r['update'] for r in history]==list(range(1,state['update']+1)) and state['token_digest']==history[-1]['token_digest']
        consumed=0
        for local,r in enumerate(history):
            expected=teacher_lr(consumed,300000000,.002)*min(1.,(local+1)/200)
            assert math.isclose(r['lr'],expected,rel_tol=1e-12)
            assert math.isfinite(r['loss']) and math.isfinite(r['gradient_norm'])
            consumed=sum(r['source_teachers'].values())
        assert consumed==300000000 and d['training_seconds']<=600
        gate=read_json(RUN/'resume-gate'/arm/'result.json');assert gate['passed'] and all(gate['checks'].values())
        verification+=gate['verification_teacher_tokens']
        ev=result['evaluations'][arm];rows=ev['generation']['outputs'];validate_rows(rows,tok)
        assert len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
        assert ev['checkpoint_sha256']==d['checkpoint_sha256'] and ev['binding']==d['binding']
        assert ev['evaluation_RNG_isolated'] and not ev['protected_test_used'] and ev['greedy_rates']==rate(rows)
        body=ev['body'];assert body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343
        assert all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows'])
        assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)
        ids=[(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in body['rows']]
        if body_ids is None:body_ids=ids
        else:assert body_ids==ids
        assert all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
        notespath=ROOT/f'reports/phase6/material_comparison_{arm}_notes.json';notes=read_json(notespath)['notes']
        scores[arm]={n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in notes}
        assert len(notes)==len(scores[arm])==80 and set(scores[arm])==set(cases)
        assert all(len(s['rationale'])>=12 and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values())
        assert all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows)
        annotations['arms'][arm]=dict(notes=notes,notes_sha256=sha256(notespath),generation_sha256=sha256(RUN/'evaluation'/arm/'evaluation/generation.json'))
        aux=result['auxiliary'][arm];assert aux['checkpoint_sha256']==d['checkpoint_sha256']
        for group,entry in aux['results'].items():
            assert entry['cases_sha256']==c['reference_sha256'][group+'.json'] and len(entry['teacher'])==len(entry['generation'])==32
        s=scores[arm]
        summary[arm]=dict(BPB=body['bpb'],rates=ev['greedy_rates'],Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
            grammar2=sum(v['grammar']==2 for v in s.values()),relevance2=sum(v['relevance']==2 for v in s.values()),
            coherent=sum(v['coherence']==2 for v in s.values()),appropriate=sum(v['completion'] for v in s.values()),
            auxiliary={k:v['summary'] for k,v in aux['results'].items()},scientific_teachers=300000000,
            valid_input_tokens=d['additional_input_tokens'],physical_tokens=d['physical_input_tokens'],
            seconds=d['training_seconds'],peak_allocated_bytes=d['peak_allocated_bytes'],additional_EOS_teachers=d['source_eos_teachers'])
        del state
    assert verification==result['verification_teacher_tokens']
    assert result['valid_input_tokens']==sum(d['additional_input_tokens'] for d in result['checkpoints'].values())
    assert result['physical_input_tokens']==sum(d['physical_input_tokens'] for d in result['checkpoints'].values())
    gates={}
    for arm,other in [('control','wikipedia'),('wikipedia','control')]:
        ev=result['evaluations'][arm];s=summary[arm]
        practical=dict(coherence_at_least27=s['coherent']>=27,appropriate_at_least27=s['appropriate']>=27,
            EOS_at_least37=s['rates']['eos']>=37,repetition_at_most18=s['rates']['repetition']<=18)
        relative=quality_gates(result['evaluations'][other],ev,scores[other],scores[arm],'content')
        original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),ev)
        gates[arm]=dict(practical=practical,relative=relative,original_Web=original,
            adopted=all(practical.values()) and relative['passed'] and all(original.values()))
    write_json(RUN/'annotations.json',annotations);write_json(ROOT/'reports/phase6/material_comparison_annotations.json',annotations)
    report=dict(status='stage2_learning_and_content_evidence_complete',summaries=summary,gates=gates,
        baseline={k:v['summary'] for k,v in result['baseline']['results'].items()},
        scientific_teacher_tokens=600000000,valid_input_tokens=result['valid_input_tokens'],physical_input_tokens=result['physical_input_tokens'],
        verification_teacher_tokens=verification,CUDA_verification_optimizer_updates=16,gpu_seconds=result['gpu_seconds'],
        result_sha256=sha256(RUN/'compare-result.json'),annotations_sha256=sha256(RUN/'annotations.json'),
        interpretation=c['interpretation'],numerical_failures72_unchanged=True,independent_human_blind=False,
        requested_five_steps_complete=False,protected_test_used=False,created_at=now())
    write_json(RUN/'review.json',report);write_json(ROOT/'reports/phase6/material_comparison_review.json',report)
    print(json.dumps(dict(summaries=summary,gates=gates),ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);audit()
