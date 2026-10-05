"""Evidence and unchanged prespecified adoption gates for both plan56 comparisons."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.japanese_evaluation import clustered_ci,repetition_metrics
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from review_story20_budget import expected_cursor
from run_eos_short_pilot import rate,routes
from run_eos_complete_100m import adoption_checks
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
import run_matched_story_study as study

def quality_gates(control,candidate,a,b,stage):
    keys=sorted(a);assert set(a)==set(b) and len(keys)==80
    delta=np.array([int(b[k]['coherence']==2)-int(a[k]['coherence']==2) for k in keys]);rng=np.random.default_rng(42)
    interval=np.quantile(delta[rng.integers(0,80,size=(2000,80))].mean(axis=1),[.025,.975]).tolist()
    checks=dict(coherence_gain_at_least8=int(delta.sum())>=8,paired_CI_lower_above0=interval[0]>0,
        EOS_nonworsening=candidate['greedy_rates']['eos']>=control['greedy_rates']['eos'],
        repetition_nonworsening=candidate['greedy_rates']['repetition']<=control['greedy_rates']['repetition'],
        no_empty_role_unicode=all(candidate['greedy_rates'][k]==0 for k in ('empty','role_leak','unicode_failure')),
        BPB_gate=candidate['body']['bpb']<=control['body']['bpb']*(1.01 if stage=='content' else 1),
        appropriate_completion_not_punctuation=all(not s['completion'] or s['relevance']>=1 and s['coherence']>=1 for s in b.values()))
    return dict(checks=checks,passed=all(checks.values()),difference_count=int(delta.sum()),CI95=interval)

def primary(stage):
    c=study.load_config(stage);run,path,_=study.paths(stage);result=read_json(run/'result.json');job=read_json(run/'screen-job.json');annotations=read_json(run/'annotations.json');checks={}
    def require(name,value):checks[name]=bool(value);assert value,name
    require('actual_job_complete_exited_budget',job['status']=='complete' and not alive(job) and result['GPU_seconds']<=job['gpu_elapsed_seconds']<=c['screen_gpu_budget_seconds'])
    require('frozen_binding_scientific_verification_scope',result['binding']==job['binding'] and job['binding']['plan_sha256']==sha256(path) and result['scientific_tokens']==1000013824 and result['verification_tokens']==262144 and not result['protected_test_used'])
    gate=result['resume_gate'];require('actual_CUDA_continuous_resumed_exact',gate['passed'] and all(gate['checks'].values()) and gate['binding']==result['binding'] and gate['input_tokens']==262144)
    tok=Tokenizer(ROOT/c['tokenizer']);cases={json.loads(line)['id']:json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines() if json.loads(line)['split']=='dev'}
    summaries={};scores={};evaluations=result['evaluations'];rows_by={}
    for arm,detail in result['arms'].items():
        directory=run/arm;history=[json.loads(line) for line in (directory/'metrics.jsonl').read_text().splitlines()]
        state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False);count=c['updates_per_arm'];routing=routes(count,c['arms'][arm]['short_updates'])
        require(arm+'_finite_checkpoint_full_resume_hash',finite_state(state) and sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256'] and all(k in state for k in ('optimizer','scheduler','rng','sampler','body_bytes','supervised_tokens')))
        require(arm+'_actual_contiguous_finite_updates',len(history)==count and [r['update'] for r in history]==list(range(305177,c['final_update']+1)) and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
        require(arm+'_final_counters_binding_digest',state['update']==c['final_update'] and state['tokens']==c['final_tokens'] and detail['binding']==state['pilot_binding'] and state['token_digest']==history[-1]['token_digest'])
        require(arm+'_actual_LR_schedule',state['spec']['lr']==.0001 and state['spec']['pilot_schedule']==dict(parent_update=305176,stable_updates=c['stable_updates'],decay_updates=c['decay_updates']))
        short=sum(routing)*32768
        require(arm+'_actual_source_routes_cursors',tuple(state['sampler']['routes'])==tuple(routing) and state['sampler']['source_tokens']==dict(web=count*32768-short,short=short) and tuple(state['sampler']['short'][k] for k in ('epoch','position'))==expected_cursor(short,1024,state['sampler']['short']['blocks']))
        if stage=='amount':
            require('constant_LR_all30518_updates',all(math.isclose(r['lr'],.0001,rel_tol=1e-12) for r in history) and routing[:15259]==routes(15259,3051))
            mid=result['checkpoints']['constant500M'];midstate=torch.load(mid['checkpoint'],map_location='cpu',weights_only=False)
            require('actual500M_midpoint_same_continuous_lineage',sha256(Path(mid['checkpoint']))==mid['checkpoint_sha256'] and midstate['tokens']==10500014080 and midstate['update']==320435 and midstate['token_digest']==history[15258]['token_digest'] and midstate['pilot_binding']==state['pilot_binding'])
            require('learning_before_all_evaluation',mid['checkpoint_role']=='midpoint500M' and all(ev['completed_at']>detail['completed_at'] for ev in evaluations.values()))
    for name,ev in evaluations.items():
        directory=run/'evaluation'/name/'evaluation';detail=result['checkpoints'][name];rows=ev['generation']['outputs'];rows_by[name]=rows
        validate_rows(rows,tok);require(name+'_checkpoint_bound_raw80',ev['checkpoint_sha256']==detail['checkpoint_sha256'] and ev['binding']==detail['binding'] and len(rows)==80 and {r['id'] for r in rows}==set(cases))
        entry=annotations['arms'][name];require(name+'_annotations_raw_hash',entry['generation_sha256']==sha256(directory/'generation.json'))
        notes=entry['notes'];scores[name]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in notes}
        require(name+'_all80_individual_notes',len(notes)==len(scores[name])==80 and set(scores[name])==set(cases) and all(r['rationale'] and all(r[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and r['completion'] in (0,1) for r in scores[name].values()))
        require(name+'_appropriate_completion_actual_EOS',all(not scores[name][r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows))
        body=ev['body'];require(name+'_common256_actual_NLL_BPB',body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343 and all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        require(name+'_raw_rates_recomputed',ev['greedy_rates']==rate(rows))
        require(name+'_Japanese_complete_RNG_isolated',ev['evaluation_RNG_isolated'] and all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==ev['diagnostics'][k]['expected']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items()))
        summaries[name]=dict(BPB=body['bpb'],rates=ev['greedy_rates'],content={k+'_score2':sum(s[k]==2 for s in scores[name].values()) for k in ('grammar','relevance','coherence')},appropriate_EOS=sum(s['completion'] for s in scores[name].values()),diagnostics=ev['diagnostics'])
    names=['control','refined'] if stage=='content' else ['constant500M','constant1B'];a,b=names
    require('paired_fixed80_and_common_bytes_alignment',[(r['id'],r['prefix']) for r in rows_by[a]]==[(r['id'],r['prefix']) for r in rows_by[b]] and [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in evaluations[a]['body']['rows']]==[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in evaluations[b]['body']['rows']])
    if stage=='content':
        require('actual_same_source_token_and_EOS_teacher_counts',result['arms'][a]['source_tokens']==result['arms'][b]['source_tokens'] and result['arms'][a]['source_eos_teachers']==result['arms'][b]['source_eos_teachers'])
    quality=quality_gates(evaluations[a],evaluations[b],scores[a],scores[b],stage)
    practical=dict(coherence_at_least27=summaries[b]['content']['coherence_score2']>=27,appropriate_at_least27=summaries[b]['appropriate_EOS']>=27,
        EOS_at_least37=evaluations[b]['greedy_rates']['eos']>=37,repetition_at_most18=evaluations[b]['greedy_rates']['repetition']<=18)
    web=read_json(Path(c['reference']['web_screen']['path']));original=adoption_checks(web,evaluations[b])
    diagnostic_difference={}
    for task in c['evaluation']['tasks']:
        pair=[{r['id']:r for r in read_json(run/'evaluation'/n/'evaluation'/(task+'.json'))['rows']} for n in names];left,right=pair
        require('paired_Japanese_IDs_'+task,set(left)==set(right))
        diagnostic_difference[task]=clustered_ci([dict(id=k,family=right[k].get('family',k),difference=right[k]['credit']-left[k]['credit']) for k in left],key='difference')
    review=dict(status='passed',stage=stage,checks=checks,summaries=summaries,quality_comparison=quality,practical=practical,original_Web_gates=original,
        paired_diagnostics=diagnostic_difference,eligible_for_full=quality['passed'] and all(practical.values()) and all(original.values()),
        scored_outputs={n:[dict(row,**scores[n][row['id']]) for row in rows_by[n]] for n in names},
        config_sha256=sha256(path),result_sha256=sha256(run/'result.json'),annotations_sha256=sha256(run/'annotations.json'),reviewer_sha256=sha256(Path(__file__)),checked_at=now(),
        independent_human_blind='not performed; individual nonblind Codex content diagnosis',quality_targets_achieved=False,protected_test_used=False)
    write_json(run/'review.json',review);print(json.dumps({k:v for k,v in review.items() if k not in ('scored_outputs','summaries')},ensure_ascii=False),flush=True)

def full(stage):
    c=study.load_config(stage);run,_,_=study.paths(stage);output=run/'full';result=read_json(output/'result.json');job=read_json(output/'full-job.json');checks={}
    def require(name,value):checks[name]=bool(value);assert value,name
    require('actual_eligible_complete_exited_budget',read_json(run/'review.json')['eligible_for_full'] and job['status']=='complete' and not alive(job) and result['binding']==job['binding'] and result['GPU_seconds']<=job['gpu_elapsed_seconds']<=c['full_gpu_budget_seconds'])
    require('binding_zero_learning_scope',result['binding']['review_sha256']==sha256(run/'review.json') and result['additional_training_tokens']==0 and not result['protected_test_used'])
    tok=Tokenizer(ROOT/c['tokenizer']);trained=read_json(run/'result.json')['checkpoints'];parent_body=read_json(Path(c['reference']['parent_body']['path']))['body'];parent_gen=read_json(Path(c['reference']['parent_generation']['path']))['generation'];parent=summarize('parent10B',10000007168,parent_body,parent_gen);records={};summaries={}
    for name in result['summaries']:
        record=read_json(output/(name+'-full.json'));body=record['body'];generation=record['generation'];records[name]=record
        require(name+'_actual89416_full_bytes_NLL',record['full'] and body['documents']==len(body['rows'])==89416 and body['body_bytes']==164344743 and body['body_tokens']==42003934 and all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        require(name+'_checkpoint_binding_RNG',record['checkpoint_sha256']==trained[name]['checkpoint_sha256'] and record['binding']==result['binding'] and record['evaluation_RNG_isolated'])
        require_alignment(body,generation,parent_body,parent_gen);validate_rows(generation['outputs'],tok);require(name+'_actual400_aligned_requests',len(generation['outputs'])==400)
        fixed={r['id']:r for r in generation['outputs'] if r['decoding']=='greedy' and r['suppressed']}
        require(name+'_fixed80_same_IDs_as_primary',all(fixed[r['id']]['generated_ids']==r['generated_ids'] for r in read_json(run/'result.json')['evaluations'][name]['generation']['outputs']))
        long=read_json(output/name/'long-generation.json');require(name+'_actual_long40_binding',long['complete'] and len(long['rows'])==40 and long['binding']==json.dumps(result['binding'],sort_keys=True))
        for row in long['rows']:
            raw=tok.decode_bytes(row['generated_ids'])
            try:text=raw.decode('utf-8');valid=True
            except UnicodeDecodeError:text=raw.decode('utf-8',errors='replace');valid=False
            assert text==row['text'] and valid==row['valid_utf8'] and repetition_metrics(row)==row['metrics']
        require(name+'_long_raw_and_metrics_recomputed',True);summaries[name]=summarize(name,trained[name]['tokens'],body,generation)
    candidate='refined' if stage=='content' else 'constant1B';control=read_json(Path(c['reference']['web_full']['path'])) if stage=='content' else records['constant500M']
    require_alignment(records[candidate]['body'],records[candidate]['generation'],control['body'],control['generation'])
    gates=dict(parent_growth=growth_checks(summaries[candidate],parent))
    if stage=='content':gates['mixture']=adoption_checks(control,records[candidate])
    else:gates['matched_growth']=growth_checks(summaries[candidate],summaries['constant500M'])
    require('full_gates_recomputed',gates==result['checks'] and result['candidate_passes_all_full_conditions']==all(v for group in gates.values() for v in group.values()))
    write_json(output/'review.json',dict(status='passed',checks=checks,summaries=summaries,full_conditions=gates,candidate_passes_all_full_conditions=result['candidate_passes_all_full_conditions'],result_sha256=sha256(output/'result.json'),checked_at=now(),reviewer_sha256=sha256(Path(__file__))))
    print(json.dumps(dict(checks=checks,full_conditions=gates)),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--stage',choices=('content','amount'),required=True);parser.add_argument('--mode',choices=('primary','full'),default='primary');args=parser.parse_args();assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='primary':primary(args.stage)
    else:full(args.stage)
