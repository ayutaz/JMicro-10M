"""Verify two new matched architectures; reuse existing current80 judgments."""
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
from run_eos_short_pilot import equal_state,rate
from run_architecture_comparison import RUN,CONFIG,MATERIAL_RUN,load_config,validate_parent


def audit():
    c=load_config();result=read_json(RUN/'compare-result.json');job=read_json(RUN/'job.json')
    assert job['status']=='complete' and not alive(job)
    assert result['config_sha256']==job['config_sha256']==sha256(CONFIG)
    assert result['scientific_teacher_tokens_new']==600000000 and result['reused_current_teacher_tokens']==300000000
    assert result['gpu_seconds']<=job['gpu_elapsed_seconds']<=3600 and not result['protected_test_used']
    previous=read_json(MATERIAL_RUN/'compare-result.json');review=read_json(MATERIAL_RUN/'review.json')
    annotations=read_json(MATERIAL_RUN/'annotations.json')['arms']['wikipedia']
    summaries=dict(current=review['summaries']['wikipedia']);scores=dict(current={n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5]) for n in annotations['notes']})
    evaluations=dict(current=previous['evaluations']['wikipedia']);notes=dict(current=annotations)
    original=c['reused_current'];assert original==previous['checkpoints']['wikipedia']
    assert sha256(Path(original['checkpoint']))==original['checkpoint_sha256']
    current=torch.load(original['checkpoint'],map_location='cpu',weights_only=False)['sampler']
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    tok=Tokenizer(ROOT/c['tokenizer']);verification=0
    for arm,d in result['checkpoints'].items():
        entry=c['arms'][arm];parent=torch.load(d['binding']['parent']['path'],map_location='cpu',weights_only=False)
        validate_parent(parent,entry['model_config'],entry['parameters'])
        assert sha256(Path(d['checkpoint']))==d['checkpoint_sha256']
        state=torch.load(d['checkpoint'],map_location='cpu',weights_only=False)
        assert finite_state(state) and all(k in state for k in ('model','optimizer','scheduler','rng','sampler','lineage','token_digest'))
        assert state['model_config']==entry['model_config'] and state['pilot_binding']==d['binding']
        assert state['supervised_tokens']==d['additional_supervised_tokens']==300000000
        assert state['tokens']==d['additional_input_tokens']==sum(state['sampler']['source_tokens'].values())
        assert state['lineage']['parent_update']==state['lineage']['parent_tokens']==state['lineage']['parent_supervised_tokens']==0
        assert state['lineage']['optimizer_policy']=='fresh' and state['spec']['warmup']==200
        assert state['sampler']['source_teachers']==c['goals'] and equal_state(state['sampler']['short'],current['short'])
        assert state['sampler']['source_eos']==current['source_eos'] and sum(state['sampler']['source_physical_tokens'].values())==d['physical_input_tokens']
        history=[json.loads(s) for s in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        assert len(history)==state['update']==state['sampler']['position'] and state['token_digest']==history[-1]['token_digest']
        consumed=0
        for local,r in enumerate(history):
            assert r['update']==local+1 and math.isfinite(r['loss']) and math.isfinite(r['gradient_norm'])
            assert math.isclose(r['lr'],teacher_lr(consumed,300000000,.002)*min(1.,(local+1)/200),rel_tol=1e-12)
            consumed=sum(r['source_teachers'].values())
        assert consumed==300000000 and d['training_seconds']<=600
        gate=read_json(RUN/'resume-gate'/arm/'result.json');assert gate['passed'] and all(gate['checks'].values());verification+=gate['verification_teacher_tokens']
        ev=result['evaluations'][arm];rows=ev['generation']['outputs'];validate_rows(rows,tok)
        assert len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
        assert ev['checkpoint_sha256']==d['checkpoint_sha256'] and ev['binding']==d['binding']
        assert ev['evaluation_RNG_isolated'] and not ev['protected_test_used'] and ev['greedy_rates']==rate(rows)
        body=ev['body'];reference=evaluations['current']['body']
        assert body['documents']==256 and body['body_bytes']==472055 and body['body_tokens']==122343
        assert [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in body['rows']]==[(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in reference['rows']]
        assert all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)
        assert all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
        path=ROOT/f'reports/phase6/architecture_comparison_{arm}_notes.json';n=read_json(path)['notes']
        scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in n}
        assert len(n)==len(scores[arm])==80 and set(scores[arm])==set(cases)
        assert all(len(s['rationale'])>=12 and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values())
        assert all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows)
        notes[arm]=dict(notes=n,notes_sha256=sha256(path),generation_sha256=sha256(RUN/'evaluation'/arm/'evaluation/generation.json'))
        summaries[arm]=dict(parameters=entry['parameters'],BPB=body['bpb'],rates=ev['greedy_rates'],Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
            coherent=sum(s['coherence']==2 for s in scores[arm].values()),appropriate=sum(s['completion'] for s in scores[arm].values()),
            grammar2=sum(s['grammar']==2 for s in scores[arm].values()),relevance2=sum(s['relevance']==2 for s in scores[arm].values()),
            auxiliary={k:v['summary'] for k,v in result['auxiliary'][arm]['results'].items()},scientific_teachers=300000000,
            valid_input_tokens=d['additional_input_tokens'],physical_tokens=d['physical_input_tokens'],seconds=d['training_seconds'],peak_allocated_bytes=d['peak_allocated_bytes'])
        evaluations[arm]=ev;del state,parent
    assert verification==result['verification_teacher_tokens']
    gates={}
    for arm in c['arms']:
        ev=evaluations[arm];s=summaries[arm]
        practical=dict(coherence_at_least27=s['coherent']>=27,appropriate_at_least27=s['appropriate']>=27,EOS_at_least37=s['rates']['eos']>=37,repetition_at_most18=s['rates']['repetition']<=18)
        relative=quality_gates(evaluations['current'],ev,scores['current'],scores[arm],'content')
        original_gate=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),ev)
        gates[arm]=dict(practical=practical,relative_to_current=relative,original_Web=original_gate,adopted=all(practical.values()) and relative['passed'] and all(original_gate.values()))
    annotation=dict(reviewer='Codex nonblind',independent_human_blind=False,current_reused=True,arms=notes)
    write_json(RUN/'annotations.json',annotation);write_json(ROOT/'reports/phase6/architecture_comparison_annotations.json',annotation)
    report=dict(status='stage3_learning_and_content_evidence_complete',summaries=summaries,gates=gates,
        scientific_teacher_tokens_new=600000000,reused_current_teacher_tokens=300000000,verification_teacher_tokens=verification,
        CUDA_verification_optimizer_updates=16,gpu_seconds=result['gpu_seconds'],result_sha256=sha256(RUN/'compare-result.json'),
        annotations_sha256=sha256(RUN/'annotations.json'),interpretation=c['interpretation'],numerical_failures72_unchanged=True,
        independent_human_blind=False,requested_five_steps_complete=False,protected_test_used=False,created_at=now())
    write_json(RUN/'review.json',report);write_json(ROOT/'reports/phase6/architecture_comparison_review.json',report)
    print(json.dumps(dict(summaries=summaries,gates=gates),ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);audit()
