"""Review all320 budget-study outputs and compare same-pool100M/500M evidence."""
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.japanese_evaluation import clustered_ci
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from run_story10_comparison import selection_checks
from run_eos_short_pilot import routes
import run_story20_budget as study


def expected_cursor(tokens,context,blocks):
    consumed=tokens//context
    assert tokens%context==0 and blocks>0
    return (0,0) if consumed==0 else ((consumed-1)//blocks,(consumed-1)%blocks+1)


def main():
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    config=study.load_config();result=read_json(study.RUN/'result.json');job=read_json(study.RUN/'screen-job.json')
    assert job['status']=='complete' and not alive(job) and result['GPU_seconds']<=config['screen_gpu_budget_seconds']
    annotations=read_json(study.RUN/'annotations.json');tok=Tokenizer(ROOT/config['tokenizer']);scores={};evaluated={};summaries={};checks={}
    def require(name,value):
        checks[name]=bool(value);assert value,name
    require('actual_mixed_CUDA_save_resume',result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values()) and result['verification_tokens']==262144)
    require('paired500M_scientific_tokens',result['scientific_tokens']==1000013824)
    cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    for arm in config['arms']:
        scores[arm]={};evaluated[arm]={};summaries[arm]={}
        history=[json.loads(line) for line in (study.RUN/arm/'metrics.jsonl').read_text().splitlines()]
        require(arm+'_15259_contiguous_finite_updates',len(history)==15259 and [r['update'] for r in history]==list(range(305177,320436)) and
                all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
        routing=routes(15259,config['arms'][arm]['short_updates'])
        for label,local in [('intermediate100M',3052),('result',15259)]:
            directory=study.RUN/'evaluation'/label/arm/'evaluation'
            evaluated[arm][label]=read_json(directory/'result.json');evaluation=evaluated[arm][label]
            rows=evaluation['generation']['outputs'];validate_rows(rows,tok)
            require(arm+'_'+label+'_generation_hash_and_exact80_IDs',annotations['generation_sha256'][arm][label]==sha256(directory/'generation.json') and
                    {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows))
            entries=annotations['scores'][arm][label]
            scored={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in entries}
            require(arm+'_'+label+'_all80_individual_content_notes',len(entries)==len(scored)==80 and set(scored)==set(cases))
            for row in rows:
                rating=scored[row['id']]
                assert all(rating[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and rating['completion'] in (0,1) and rating['rationale']
                assert not rating['completion'] or row['stop_reason']=='stop_id'
            scores[arm][label]=scored
            detail=read_json(study.RUN/arm/(label+'.json'))
            require(arm+'_'+label+'_actual_checkpoint_hash',sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']==evaluation['checkpoint_sha256'])
            state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False);short=sum(routing[:local])*32768
            require(arm+'_'+label+'_finite_full_state_counters',finite_state(state) and state['tokens']==10000007168+local*32768 and
                    state['update']==305176+local and state['pilot_binding']==detail['binding']==evaluation['binding'] and
                    state['token_digest']==history[local-1]['token_digest'] and
                    all(k in state for k in ('optimizer','scheduler','rng','sampler','supervised_tokens','body_bytes')))
            require(arm+'_'+label+'_common_schedule_and_source_counts',state['spec']['lr']==.0001 and
                    state['spec']['pilot_schedule']==dict(parent_update=305176,stable_updates=14500,decay_updates=759) and
                    state['sampler']['source_tokens']==dict(web=local*32768-short,short=short))
            cursor=state['sampler']['short']
            require(arm+'_'+label+'_actual_epoch_reuse_disclosed',tuple(cursor[k] for k in ('epoch','position'))==expected_cursor(short,1024,cursor['blocks']))
            body=evaluation['body']
            require(arm+'_'+label+'_common256_actual_finite_BPB',body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and
                    body['body_tokens']==122343 and all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and
                    math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
            require(arm+'_'+label+'_complete_Japanese_tasks_RNG_isolated',evaluation['evaluation_RNG_isolated'] and
                    all(evaluation['diagnostics'][k]['complete'] and evaluation['diagnostics'][k]['count']==evaluation['diagnostics'][k]['expected']==n
                        for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items()))
            summary={k+'_score2':sum(r[k]==2 for r in scored.values()) for k in ('grammar','relevance','coherence')}
            summary.update(count=80,appropriate_EOS=sum(r['completion'] for r in scored.values()),epoch=cursor['epoch'],position=cursor['position'])
            summaries[arm][label]=summary
    selection={label:selection_checks(evaluated['web'][label],evaluated['coherent20'][label],scores['web'][label],scores['coherent20'][label]) for label in ('intermediate100M','result')}
    paired={};within={}
    for label in ('intermediate100M','result'):
        paired[label]={}
        for task in config['evaluation']['tasks']:
            rows={a:{r['id']:r for r in read_json(study.RUN/'evaluation'/label/a/'evaluation'/(task+'.json'))['rows']} for a in config['arms']}
            assert set(rows['web'])==set(rows['coherent20'])
            paired[label][task]=clustered_ci([dict(id=k,family=rows['web'][k].get('family',k),difference=rows['coherent20'][k]['credit']-rows['web'][k]['credit']) for k in rows['web']],key='difference')
    for arm in config['arms']:
        within[arm]={}
        for task in config['evaluation']['tasks']:
            rows={label:{r['id']:r for r in read_json(study.RUN/'evaluation'/label/arm/'evaluation'/(task+'.json'))['rows']} for label in ('intermediate100M','result')}
            a,b=rows['intermediate100M'],rows['result'];assert set(a)==set(b)
            within[arm][task]=clustered_ci([dict(id=k,family=a[k].get('family',k),difference=b[k]['credit']-a[k]['credit']) for k in a],key='difference')
        within[arm]['coherence']=clustered_ci([dict(id=k,family=k,difference=int(scores[arm]['result'][k]['coherence']==2)-int(scores[arm]['intermediate100M'][k]['coherence']==2)) for k in scores[arm]['result']],key='difference')
    require('no_protected_test',not result['protected_test_used'])
    review=dict(status='passed',checked_at=now(),checks=checks,config_sha256=sha256(study.CONFIG),result_sha256=sha256(study.RUN/'result.json'),
                summary=summaries,selection=selection,eligible_for_full=selection['result']['eligible_for_full'],paired_diagnostics=paired,within_arm_100M_to500M=within,
                scientific_tokens=1000013824,verification_tokens=262144,protected_test_used=False,quality_targets_achieved=False,
                independent_human_blind='not performed',scored_outputs={a:{label:[dict(row,**scores[a][label][row['id']]) for row in evaluated[a][label]['generation']['outputs']] for label in ('intermediate100M','result')} for a in config['arms']},
                reviewer_sha256=sha256(Path(__file__)))
    write_json(study.RUN/'review.json',review)
    print(json.dumps({k:v for k,v in review.items() if k!='scored_outputs'},ensure_ascii=False),flush=True)


if __name__=='__main__':main()
