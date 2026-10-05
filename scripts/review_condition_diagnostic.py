"""Audit actual learning, unchanged quality gates, and individual content judgments."""
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import pilot_lr
from jmicro.condition_diagnostic import summarize_choice
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import clustered_ci
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import routes,rate
import run_condition_diagnostic as study


def main():
    c=study.load_config();run=study.RUN;result=read_json(run/'result.json');job=read_json(run/'job.json');annotations=read_json(run/'annotations.json');checks={}
    def require(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    require('actual_complete_job_exited_within_budget',job['status']=='complete' and not alive(job) and result['GPU_seconds']<=job['gpu_elapsed_seconds']<=c['total_gpu_budget_seconds'])
    require('frozen_run_binding',result['binding']==job['binding'] and job['binding']['plan_sha256']==sha256(study.CONFIG))
    require('actual_CUDA_all_resume_state_and_losses',result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values()) and result['verification_tokens']==262144)
    eligible=any(result['conditions'][a]['diagnostic_pass'] for a in ('compact','expanded'))
    arms={'compact','expanded'}|({'mixed-control','mixed-candidate'} if eligible else set())
    require('frozen_conditional_100M_branch',result['mixed100m_executed']==eligible and set(result['checkpoints'])==arms)
    require('scientific_verification_separate_accounting',result['scientific_tokens']==sum(d['additional_input_tokens'] for d in result['checkpoints'].values())==49938432+(199950336 if eligible else 0))
    require('protected_test_unused',not result['protected_test_used'])
    tok=Tokenizer(ROOT/c['tokenizer']);cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    summaries={};scores={};diagnoses={};states={}
    for arm in sorted(arms):
        d=result['checkpoints'][arm];p=study.train_configuration(c,arm,arm.startswith('mixed'))
        history=[json.loads(line) for line in (run/arm/'metrics.jsonl').read_text().splitlines()]
        state=torch.load(d['checkpoint'],map_location='cpu',weights_only=False)
        require(arm+'_finite_hash_bound_all_resume_state',finite_state(state) and sha256(Path(d['checkpoint']))==d['checkpoint_sha256'] and all(k in state for k in ('optimizer','scheduler','rng','sampler','supervised_tokens','body_bytes')))
        require(arm+'_actual_finite_contiguous_updates',len(history)==p['updates_per_arm'] and [r['update'] for r in history]==list(range(c['parent']['update']+1,p['final_update']+1)) and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
        require(arm+'_actual_tokens_binding_digest',state['tokens']==p['final_tokens'] and state['update']==p['final_update'] and state['pilot_binding']==d['binding'] and state['token_digest']==history[-1]['token_digest'] and d['additional_input_tokens']==p['tokens_per_arm'])
        require(arm+'_actual_base_objective_not_chat_or_answer_only',state['spec'].get('sampler','block')=='block' and state['model_config']['vocab_size']==4096 and state['sampler']['source_eos']['short']>0 and state['supervised_tokens']>c['parent']['tokens_seen']*.8)
        # Trainer logs the LR applied before optimizer.step/scheduler.step.
        require(arm+'_actual_LR_stable_decay',all(math.isclose(r['lr'],.0001*pilot_lr(state['spec'],r['update']-1),rel_tol=1e-12) for r in history))
        routing=routes(p['updates_per_arm'],p['arms'][arm]['short_updates']);short=sum(routing)*32768
        require(arm+'_actual_train_only_source_routes',tuple(state['sampler']['routes'])==tuple(routing) and state['sampler']['source_tokens']==dict(web=p['tokens_per_arm']-short,short=short) and state['sampler']['position']==p['updates_per_arm'])
        states[arm]=state['sampler']
        ev=result['evaluations'][arm];rows=ev['generation']['outputs'];validate_rows(rows,tok)
        require(arm+'_actual_fixed_dev80_raw_checkpoint_binding',ev['checkpoint_sha256']==d['checkpoint_sha256'] and ev['binding']==d['binding'] and len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows))
        entry=annotations['arms'][arm];notes=entry['notes'];scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in notes}
        require(arm+'_all80_individual_raw_bound_content_reviews',entry['generation_sha256']==sha256(run/'evaluation'/arm/'evaluation/generation.json') and len(notes)==len(scores[arm])==80 and set(scores[arm])==set(cases) and all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values()))
        require(arm+'_appropriate_completion_actual_EOS',all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' and scores[arm][r['id']]['relevance']>=1 and scores[arm][r['id']]['coherence']>=1 for r in rows))
        body=ev['body']
        require(arm+'_same_dev256_common_byte_BPB',body['documents']==256 and body['body_bytes']==472055 and body['body_tokens']==122343 and all(r['scored_body_tokens']==r['body_tokens'] and math.isfinite(r['body_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        require(arm+'_complete_Japanese_diagnostics_RNG_isolated',ev['evaluation_RNG_isolated'] and all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==ev['diagnostics'][k]['expected']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items()))
        require(arm+'_raw_rates_recomputed',ev['greedy_rates']==rate(rows))
        condition=result['conditions'][arm]
        require(arm+'_condition_eval_same_new_checkpoint',condition['checkpoint_sha256']==d['checkpoint_sha256'] and not condition['protected_test_used'])
        for split in ('train','dev'):
            records=condition['results'][split]['rows']
            require(arm+'_'+split+'_100_actual_paired_credits',len(records)==100 and condition['results'][split]['summary']==summarize_choice(records) and all(r['correct']==(r['prediction']==r['label']) and all(math.isfinite(v) for v in r['log_likelihood']) for r in records))
        require(arm+'_unseen_structure_50_separate',condition['results']['dev']['known_structure']['total']==50 and condition['results']['dev']['unseen_structure']['total']==50)
        require(arm+'_train90_dev70_goal_recomputed',condition['diagnostic_pass']==(condition['results']['train']['summary']['accuracy']>=.9 and condition['results']['dev']['summary']['accuracy']>=.7))
        diagnostics={s:condition['results'][s]['summary'] for s in ('train','dev')}
        train=diagnostics['train']['accuracy'];dev=diagnostics['dev']['accuracy']
        diagnoses[arm]='Train learning goal missed; objective, target supply and finite state checked, no proved implementation defect or capacity limit' if train<.9 else 'Train succeeds; unseen condition generalization goal missed' if dev<.7 else 'Authored closed-world conditions learned; does not prove general Japanese generation quality'
        records=condition['results']['train']['rows']
        summaries[arm]=dict(BPB=body['bpb'],rates=ev['greedy_rates'],
            content={k+'_score2':sum(s[k]==2 for s in scores[arm].values()) for k in ('grammar','relevance','coherence')},
            appropriate_EOS=sum(s['completion'] for s in scores[arm].values()),diagnostics=ev['diagnostics'],condition=diagnostics,
            unseen_structure=condition['results']['dev']['unseen_structure'],known_structure=condition['results']['dev']['known_structure'],
            expected_train_continuation_nll_per_token=sum(r['expected_continuation_nll'] for r in records)/sum(r['expected_continuation_tokens'] for r in records),
            training_seconds=d['training_seconds'],source_tokens=d['source_tokens'],source_EOS=d['source_eos_teachers'],
            actual_short_epoch=d['sampler']['short']['epoch'],actual_short_cursor=d['sampler']['short']['position'])
    if eligible:
        require('mixed_same_Web_actual_cursor',states['mixed-control']['web']==states['mixed-candidate']['web'])
    comparisons={}
    for left,right in [('compact','expanded')]+([('mixed-control','mixed-candidate')] if eligible else []):
        a=result['evaluations'][left];b=result['evaluations'][right]
        require(left+'_'+right+'_paired_fixed_IDs_bytes',[(r['id'],r['prefix']) for r in a['generation']['outputs']]==[(r['id'],r['prefix']) for r in b['generation']['outputs']] and [(r['doc_id'],r['body_bytes']) for r in a['body']['rows']]==[(r['doc_id'],r['body_bytes']) for r in b['body']['rows']])
        practical=dict(coherence_at_least27=summaries[right]['content']['coherence_score2']>=27,
            appropriate_at_least27=summaries[right]['appropriate_EOS']>=27,EOS_at_least37=b['greedy_rates']['eos']>=37,
            repetition_at_most18=b['greedy_rates']['repetition']<=18)
        quality=quality_gates(a,b,scores[left],scores[right],'content')
        original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),b)
        differences={}
        for task in c['evaluation']['tasks']:
            l,r=[{v['id']:v for v in read_json(run/'evaluation'/name/'evaluation'/(task+'.json'))['rows']} for name in (left,right)]
            require(left+'_'+right+'_paired_'+task,set(l)==set(r))
            differences[task]=clustered_ci([dict(id=k,family=r[k].get('family',k),difference=r[k]['credit']-l[k]['credit']) for k in l],key='difference')
        comparisons[left+'__'+right]=dict(quality=quality,practical=practical,original_Web_gates=original,paired_diagnostics=differences,
            eligible_for_full=quality['passed'] and all(practical.values()) and all(original.values()))
    review=dict(status='passed_evidence_audit',checks=checks,summaries=summaries,diagnoses=diagnoses,comparisons=comparisons,
                condition_parent=result['conditions']['parent']['results'],scientific_tokens=result['scientific_tokens'],verification_tokens=result['verification_tokens'],GPU_seconds=result['GPU_seconds'],
                result_sha256=sha256(run/'result.json'),annotations_sha256=sha256(run/'annotations.json'),config_sha256=sha256(study.CONFIG),
                reviewer_sha256=sha256(Path(__file__)),checked_at=now(),quality_targets_achieved=False,
                limits='Single training seed; Codex authored synthetic examples and nonblind content scoring; dev reused for branch selection; no independent human/test evaluation')
    write_json(run/'review.json',review)
    print(json.dumps(dict(status=review['status'],evidence_checks=len(checks),scientific_tokens=result['scientific_tokens'],
        summaries={a:{k:v for k,v in s.items() if k not in ('diagnostics',)} for a,s in summaries.items()},comparisons=comparisons),ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);main()
