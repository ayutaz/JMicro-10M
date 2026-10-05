"""Actual paired1B evidence, unchanged quality gates, and conditional full audit."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import pilot_lr
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import clustered_ci
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from review_story20_budget import expected_cursor
from review_matched_story_study import quality_gates
from run_eos_short_pilot import routes,rate
from run_eos_complete_100m import adoption_checks
import run_dataset_expansion as study

def primary():
    c=study.load_config();run=study.RUN;result=read_json(run/'result.json');job=read_json(run/'screen-job.json');annotations=read_json(run/'annotations.json');checks={}
    def require(name,value):checks[name]=bool(value);assert value,name
    require('actual_job_complete_exited_budget',job['status']=='complete' and not alive(job) and result['GPU_seconds']<=job['gpu_elapsed_seconds']<=c['screen_gpu_budget_seconds'])
    require('frozen_binding_scientific_verification_scope',result['binding']==job['binding'] and job['binding']['plan_sha256']==sha256(study.CONFIG) and result['scientific_tokens']==2000027648 and result['verification_tokens']==262144 and not result['protected_test_used'])
    gate=result['resume_gate'];require('actual_CUDA_stable_decay_continuous_resumed_exact',gate['passed'] and all(gate['checks'].values()) and gate['binding']==result['binding'] and gate['input_tokens']==262144)
    require('actual200M_new_source_train_only_disclosed',c['actual_data']['new_pool_tokens']>=200000000 and c['actual_data']['new_source_tokens']>=140000000 and result['actual_data']==c['actual_data'] and result['comparison_interpretation']==c['comparison_interpretation'])
    tok=Tokenizer(ROOT/c['tokenizer']);cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    evaluations=result['evaluations'];scores={};summaries={};rows_by={};samplers={}
    for arm,detail in result['arms'].items():
        directory=run/arm;history=[json.loads(line) for line in (directory/'metrics.jsonl').read_text().splitlines()]
        state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False);routing=routes(c['updates_per_arm'],6102);samplers[arm]=state['sampler']
        require(arm+'_finite_checkpoint_full_resume_hash',finite_state(state) and sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256'] and all(k in state for k in ('optimizer','scheduler','rng','sampler','body_bytes','supervised_tokens')))
        require(arm+'_actual30518_contiguous_finite_updates',len(history)==30518 and [r['update'] for r in history]==list(range(305177,335695)) and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
        require(arm+'_final_counters_binding_digest',state['update']==335694 and state['tokens']==11000020992 and detail['binding']==state['pilot_binding'] and state['token_digest']==history[-1]['token_digest'] and detail['additional_input_tokens']==1000013824)
        require(arm+'_actual_all_LR_stable_decay',state['spec']['lr']==.0001 and state['spec']['pilot_schedule']==dict(parent_update=305176,stable_updates=29000,decay_updates=1518) and all(math.isclose(r['lr'],.0001*pilot_lr(state['spec'],r['update']),rel_tol=1e-12) for r in history))
        require(arm+'_actual_source_routes_short_cursors',tuple(state['sampler']['routes'])==tuple(routing) and state['sampler']['source_tokens']==dict(web=800063488,short=199950336) and tuple(state['sampler']['short'][k] for k in ('epoch','position'))==expected_cursor(199950336,1024,state['sampler']['short']['blocks']))
        mid=read_json(directory/'midpoint500M.json');midstate=torch.load(mid['checkpoint'],map_location='cpu',weights_only=False)
        require(arm+'_actual500M_saved_same_lineage',sha256(Path(mid['checkpoint']))==mid['checkpoint_sha256'] and midstate['tokens']==10500014080 and midstate['update']==320435 and midstate['token_digest']==history[15258]['token_digest'] and midstate['pilot_binding']==state['pilot_binding'])
        ev=evaluations[arm];rows=ev['generation']['outputs'];rows_by[arm]=rows;validate_rows(rows,tok)
        require(arm+'_checkpoint_bound_raw80',ev['checkpoint_sha256']==detail['checkpoint_sha256'] and ev['binding']==detail['binding'] and len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows))
        entry=annotations['arms'][arm];require(arm+'_annotations_raw_hash',entry['generation_sha256']==sha256(run/'evaluation'/arm/'evaluation/generation.json'))
        notes=entry['notes'];scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in notes}
        require(arm+'_all80_individual_notes',len(notes)==len(scores[arm])==80 and set(scores[arm])==set(cases) and all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values()))
        require(arm+'_appropriate_completion_actual_EOS',all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows))
        body=ev['body'];require(arm+'_common256_actual_NLL_BPB',body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343 and all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        require(arm+'_raw_rates_recomputed',ev['greedy_rates']==rate(rows))
        require(arm+'_Japanese_complete_RNG_isolated',ev['evaluation_RNG_isolated'] and all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==ev['diagnostics'][k]['expected']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items()))
        summaries[arm]=dict(BPB=body['bpb'],rates=ev['greedy_rates'],content={k+'_score2':sum(s[k]==2 for s in scores[arm].values()) for k in ('grammar','relevance','coherence')},appropriate_EOS=sum(s['completion'] for s in scores[arm].values()),diagnostics=ev['diagnostics'])
    require('paired_fixed80_and_common_bytes_alignment',[(r['id'],r['prefix']) for r in rows_by['control']]==[(r['id'],r['prefix']) for r in rows_by['refined']] and [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in evaluations['control']['body']['rows']]==[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in evaluations['refined']['body']['rows']])
    require('same_actual_Web_routes_tokens_and_final_cursor',result['arms']['control']['source_tokens']==result['arms']['refined']['source_tokens'] and samplers['control']['web']==samplers['refined']['web'] and result['arms']['control']['source_eos_teachers']['web']==result['arms']['refined']['source_eos_teachers']['web'])
    quality=quality_gates(evaluations['control'],evaluations['refined'],scores['control'],scores['refined'],'content')
    practical=dict(coherence_at_least27=summaries['refined']['content']['coherence_score2']>=27,appropriate_at_least27=summaries['refined']['appropriate_EOS']>=27,
        EOS_at_least37=evaluations['refined']['greedy_rates']['eos']>=37,repetition_at_most18=evaluations['refined']['greedy_rates']['repetition']<=18)
    original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),evaluations['refined']);differences={}
    for task in c['evaluation']['tasks']:
        left,right=[{r['id']:r for r in read_json(run/'evaluation'/arm/'evaluation'/(task+'.json'))['rows']} for arm in ('control','refined')]
        require('paired_Japanese_IDs_'+task,set(left)==set(right))
        differences[task]=clustered_ci([dict(id=k,family=right[k].get('family',k),difference=right[k]['credit']-left[k]['credit']) for k in left],key='difference')
    review=dict(status='passed',checks=checks,summaries=summaries,quality_comparison=quality,practical=practical,original_Web_gates=original,
        paired_diagnostics=differences,eligible_for_full=quality['passed'] and all(practical.values()) and all(original.values()),
        scored_outputs={a:[dict(row,**scores[a][row['id']]) for row in rows_by[a]] for a in rows_by},
        actual_data=c['actual_data'],comparison_interpretation=c['comparison_interpretation'],
        config_sha256=sha256(study.CONFIG),result_sha256=sha256(run/'result.json'),annotations_sha256=sha256(run/'annotations.json'),
        reviewer_sha256=sha256(Path(__file__)),checked_at=now(),independent_human_blind='not performed; individual nonblind Codex diagnosis',
        quality_targets_achieved=False,protected_test_used=False)
    write_json(run/'review.json',review)
    print(json.dumps({k:v for k,v in review.items() if k not in ('scored_outputs','summaries')},ensure_ascii=False),flush=True)

def full():
    # Reuse the existing full-byte/400/40-long evidence audit through an explicit
    # config/path adapter. Historical files and frozen runner sources stay unchanged.
    from types import SimpleNamespace
    import review_matched_story_study as existing
    c=study.load_config()
    existing.study=SimpleNamespace(load_config=lambda _:c,paths=lambda _:(study.RUN,study.CONFIG,study.SCHEMA))
    existing.full('content')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('primary','full'),default='primary');a=p.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    primary() if a.mode=='primary' else full()
