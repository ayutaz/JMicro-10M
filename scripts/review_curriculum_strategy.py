"""Check actual training/evaluation and raw-bound content; preserve failed gates."""
import gzip
import json
import math
from pathlib import Path
import sys
import urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.packing_study import teacher_lr
from jmicro.japanese_evaluation import clustered_ci
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate
from run_curriculum_strategy import RUN,DATA,CONFIG,load_config


def audit():
    c=load_config();result=read_json(RUN/'compare-result.json');job=read_json(RUN/'job.json')
    assert job['status']=='complete' and not alive(job) and result['binding']==job['binding']
    assert result['gpu_seconds']<=job['gpu_elapsed_seconds']<=c['gpu_budget_seconds']
    assert result['scientific_teacher_tokens']==200000000 and not result['protected_test_used']
    annotation=read_json(RUN/'annotations.json');scores={};summaries={};states=[];verification=0
    cases={json.loads(line)['id']:json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines() if json.loads(line)['split']=='dev'}
    tok=Tokenizer(ROOT/c['tokenizer'])
    for arm,detail in result['checkpoints'].items():
        assert sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']
        state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False);assert finite_state(state)
        assert all(k in state for k in ('optimizer','scheduler','rng','sampler','lineage','token_digest'))
        assert state['pilot_binding']==detail['binding'] and state['sampler']['source_teachers']==c['goals']
        history=[json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        parent_update=state['lineage']['parent_update'];parent_tokens=state['lineage']['parent_tokens']
        assert len(history)==state['update']-parent_update==state['sampler']['position']
        assert [r['update'] for r in history]==list(range(parent_update+1,state['update']+1))
        assert state['supervised_tokens']-state['lineage']['parent_supervised_tokens']==detail['additional_supervised_tokens']==100000000
        assert state['tokens']-parent_tokens==detail['additional_input_tokens']==sum(state['sampler']['source_tokens'].values())
        assert sum(state['sampler']['source_physical_tokens'].values())==detail['physical_input_tokens']
        assert state['token_digest']==history[-1]['token_digest']
        consumed=0;policy=c['strategies'][arm]
        for local,row in enumerate(history):
            lr=teacher_lr(consumed,100000000,policy['peak_lr'])
            if policy['warmup_updates']:lr*=min(1.,(local+1)/policy['warmup_updates'])
            assert math.isclose(row['lr'],lr,rel_tol=1e-12) and math.isfinite(row['loss']) and math.isfinite(row['gradient_norm'])
            consumed=sum(row['source_teachers'].values())
        assert consumed==100000000 and state['lineage']['optimizer_policy']==policy['optimizer_policy']
        if arm=='fresh':assert parent_update==parent_tokens==state['lineage']['parent_supervised_tokens']==0
        else:assert parent_update==c['parent']['update'] and parent_tokens==c['parent']['tokens_seen']
        gate=read_json(RUN/'resume-gate'/arm/'result.json');assert gate['passed'] and all(gate['checks'].values())
        verification+=gate['verification_teacher_tokens']
        ev=result['evaluations'][arm];rows=ev['generation']['outputs'];validate_rows(rows,tok)
        assert len(rows)==80 and {r['id'] for r in rows}==set(cases)
        assert all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
        assert ev['checkpoint_sha256']==detail['checkpoint_sha256'] and ev['binding']==detail['binding']
        assert ev['evaluation_RNG_isolated'] and not ev['protected_test_used'] and ev['greedy_rates']==rate(rows)
        body=ev['body'];assert body['documents']==256 and body['body_bytes']==472055 and body['body_tokens']==122343
        assert all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows'])
        assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12)
        assert all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
        entry=annotation['arms'][arm]
        assert entry['generation_sha256']==sha256(RUN/'evaluation'/arm/'evaluation/generation.json')
        notes=entry['notes'];scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in notes}
        assert len(notes)==len(scores[arm])==80 and set(scores[arm])==set(cases)
        assert all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values())
        assert all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows)
        summaries[arm]=dict(BPB=body['bpb'],rates=ev['greedy_rates'],Japanese=ev['diagnostics'],
            grammar2=sum(s['grammar']==2 for s in scores[arm].values()),relevance2=sum(s['relevance']==2 for s in scores[arm].values()),
            coherent=sum(s['coherence']==2 for s in scores[arm].values()),appropriate=sum(s['completion'] for s in scores[arm].values()),
            auxiliary=result['auxiliary'][arm]['summary'],teacher_tokens=detail['additional_supervised_tokens'],
            valid_input_tokens=detail['additional_input_tokens'],physical_tokens=detail['physical_input_tokens'],
            seconds=detail['training_seconds'],peak_allocated_bytes=detail['peak_allocated_bytes'],EOS_teachers=detail['source_eos_teachers'])
        states.append(state['sampler']);del state
    assert verification==result['verification_teacher_tokens']
    assert states[0]['source_teachers']==states[1]['source_teachers'] and states[0]['source_eos']==states[1]['source_eos']
    assert states[0]['short']==states[1]['short']
    # Report both directions; select neither merely because the other arm is worse.
    gates={}
    for arm,other in [('continuation','fresh'),('fresh','continuation')]:
        ev=result['evaluations'][arm];s=summaries[arm]
        practical=dict(coherence_at_least27=s['coherent']>=27,appropriate_at_least27=s['appropriate']>=27,
            EOS_at_least37=ev['greedy_rates']['eos']>=37,repetition_at_most18=ev['greedy_rates']['repetition']<=18)
        relative=quality_gates(result['evaluations'][other],ev,scores[other],scores[arm],'content')
        original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),ev)
        gates[arm]=dict(practical=practical,relative=relative,original_Web=original,
            adopted=all(practical.values()) and relative['passed'] and all(original.values()))
    difference={}
    for task in ('semantics','jblimp','jcqa'):
        l,r=[{v['id']:v for v in read_json(RUN/'evaluation'/a/'evaluation'/(task+'.json'))['rows']} for a in ('continuation','fresh')]
        assert set(l)==set(r)
        difference[task]=clustered_ci([dict(id=k,family=r[k].get('family',k),difference=r[k]['credit']-l[k]['credit']) for k in l],key='difference')
    review=dict(status='verified_learning_and_content_evidence',summaries=summaries,gates=gates,
        paired_fresh_minus_continuation=difference,scientific_teacher_tokens=200000000,verification_teacher_tokens=verification,
        gpu_seconds=result['gpu_seconds'],result_sha256=sha256(RUN/'compare-result.json'),annotations_sha256=sha256(RUN/'annotations.json'),
        interpretation='Different histories/LR/optimizer strategy, not isolated model-capacity comparison; auxiliary Web may have been seen by parent; common official dev is held out.',
        numerical_failures72_unchanged=True,independent_human_blind=False,protected_test_used=False,created_at=now())
    write_json(RUN/'review.json',review);write_json(ROOT/'reports/phase6/curriculum_strategy_review.json',review)
    print(json.dumps(dict(summaries=summaries,gates=gates),ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);audit()
