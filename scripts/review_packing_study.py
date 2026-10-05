"""Actual teacher-budget training, native evaluations and unchanged content gates."""
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.condition_diagnostic import summarize_choice
from jmicro.packing_study import teacher_lr
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import clustered_ci
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate
import run_packing_study as study


def main():
    c=study.load_config();run=study.RUN;result=read_json(run/'result.json');job=read_json(run/'job.json');annotations=read_json(run/'annotations.json');checks={}
    def require(name,value):
        checks[name]=bool(value)
        assert value,name
    require('actual_complete_job_exited_within_budget',job['status']=='complete' and not alive(job) and result['GPU_seconds']<=job['gpu_elapsed_seconds']<=c['total_gpu_budget_seconds'])
    require('frozen_run_binding',result['binding']==job['binding'] and job['binding']['plan_sha256']==sha256(study.CONFIG))
    gate=result['resume_gate']
    require('three_actual_CUDA_continuous_resumed_all_states',gate['passed'] and set(gate['arms'])=={'fixed','shuffle','isolated'} and all(all(r['checks'].values()) for r in gate['arms'].values()) and gate['GPU_optimizer_updates']==24)
    require('scientific_verification_exact_teacher_accounting',result['scientific_teacher_tokens']==sum(d['additional_supervised_tokens'] for d in result['checkpoints'].values())==75000000+(200000000 if result['mixed100m_executed'] else 0) and result['verification_teacher_tokens']==gate['verification_teacher_tokens'])
    arms={'fixed','shuffle','isolated'}|({'mixed-fixed','mixed-candidate'} if result['mixed100m_executed'] else set())
    require('frozen_stages_all_terminal_arms',set(result['checkpoints'])==arms and set(result['evaluations'])==arms)
    require('protected_test_unused',not result['protected_test_used'])
    tok=Tokenizer(ROOT/c['tokenizer']);cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    summaries={};scores={};samplers={}
    fresh_by_id={r['id']:r for r in read_json(study.DATA/'dev.json')}
    train_by_id={r['id']:r for r in read_json(study.DATA/'compact-train-eval.json')}
    previous_eval=read_json(run/'previous-dev-evaluation.json')
    require('previous_dev_reference_complete_and_bound',previous_eval['status']=='complete' and previous_eval['old_dev_sha256']==c['previous_dev_sha256'] and set(previous_eval['arms'])==arms and previous_eval['additional_learning_tokens']==0)
    for arm in sorted(arms):
        d=result['checkpoints'][arm];state=torch.load(d['checkpoint'],map_location='cpu',weights_only=False)
        history=[json.loads(line) for line in (run/arm/'metrics.jsonl').read_text().splitlines()];goals=d['binding']['goals'];total=sum(goals.values())
        require(arm+'_finite_hash_bound_full_resume_state',finite_state(state) and sha256(Path(d['checkpoint']))==d['checkpoint_sha256'] and all(k in state for k in ('optimizer','scheduler','rng','sampler','supervised_tokens','body_bytes')))
        require(arm+'_actual_finite_contiguous_updates',len(history)==state['update']-c['parent']['update'] and [r['update'] for r in history]==list(range(c['parent']['update']+1,state['update']+1)) and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
        require(arm+'_exact_teacher_input_PAD_checkpoint_counters',state['tokens']==c['parent']['tokens_seen']+d['additional_input_tokens'] and state['supervised_tokens']-state['lineage']['parent_supervised_tokens']==d['additional_supervised_tokens']==total and state['sampler']['source_teachers']==goals and
            sum(state['sampler']['source_tokens'].values())==d['additional_input_tokens'] and sum(state['sampler']['source_physical_tokens'].values())==d['physical_input_tokens'] and d['physical_input_tokens']>=d['additional_input_tokens'])
        require(arm+'_binding_digest_sampler_cursor',state['pilot_binding']==d['binding'] and state['token_digest']==history[-1]['token_digest'] and state['sampler']['position']==len(history) and state['sampler']['mode']==d['mode'])
        previous=0
        for row in history:
            assert math.isclose(row['lr'],teacher_lr(previous,total,c['peak_lr']),rel_tol=1e-12)
            current=sum(row['source_teachers'].values());assert previous<current<=total;previous=current
        require(arm+'_actual_teacher_stable90percent_and_decay',previous==total and math.isclose(state['optimizer']['param_groups'][0]['lr'],c['peak_lr']*.1,rel_tol=1e-12))
        budget=c['mixed_train_budget_seconds'] if arm.startswith('mixed') else c['diagnostic_train_budget_seconds']
        require(arm+'_measured_training_budget_and_EOS_teachers',d['training_seconds']<=budget and d['source_eos_teachers']['short']>0)
        samplers[arm]=state['sampler']
        if d['mode']=='isolated':require(arm+'_PAD_not_in_learning_or_valid_input',d['physical_input_tokens']>d['additional_input_tokens'])
        else:require(arm+'_unpadded_input_equal_physical',d['physical_input_tokens']==d['additional_input_tokens'])
        condition=result['conditions'][arm]
        require(arm+'_train_and_fresh_dev100_actual_pairs',condition['checkpoint_sha256']==d['checkpoint_sha256'] and all(condition['results'][s]['summary']==summarize_choice(condition['results'][s]['rows']) and len(condition['results'][s]['rows'])==100 for s in ('train','dev')))
        require(arm+'_fixed_primary_prefix_choices_labels',all({r['id'] for r in condition['results'][s]['rows']}==set(frozen) and all(all(r[k]==frozen[r['id']][k] for k in ('prefix','choices','label')) for r in condition['results'][s]['rows']) for s,frozen in [('train',train_by_id),('dev',fresh_by_id)]))
        require(arm+'_old_dev100_reference_checkpoint',previous_eval['arms'][arm]['checkpoint_sha256']==d['checkpoint_sha256'] and len(previous_eval['arms'][arm]['rows'])==100 and previous_eval['arms'][arm]['summary']==summarize_choice(previous_eval['arms'][arm]['rows']))
        require(arm+'_unseen_structure50_and_unchanged_goals',condition['results']['dev']['known_structure']['total']==50 and condition['results']['dev']['unseen_structure']['total']==50 and condition['diagnostic_pass']==(condition['results']['train']['summary']['accuracy']>=.9 and condition['results']['dev']['summary']['accuracy']>=.7))
        ev=result['evaluations'][arm];rows=ev['generation']['outputs'];validate_rows(rows,tok)
        require(arm+'_same_raw_dev80_checkpoint_and_prefixes',ev['checkpoint_sha256']==d['checkpoint_sha256'] and ev['binding']==d['binding'] and len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows))
        entry=annotations['arms'][arm];notes=entry['notes'];scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in notes}
        require(arm+'_all80_individual_raw_bound_content_notes',entry['generation_sha256']==sha256(run/'evaluation'/arm/'evaluation/generation.json') and len(notes)==len(scores[arm])==80 and set(scores[arm])==set(cases) and all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values()))
        require(arm+'_appropriate_completion_actual_EOS_and_content',all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' and scores[arm][r['id']]['relevance']>=1 and scores[arm][r['id']]['coherence']>=1 for r in rows))
        body=ev['body']
        require(arm+'_common_dev256_byte_BPB',body['documents']==256 and body['body_bytes']==472055 and body['body_tokens']==122343 and all(r['scored_body_tokens']==r['body_tokens'] and math.isfinite(r['body_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        require(arm+'_all_Japanese_complete_RNG_isolated',ev['evaluation_RNG_isolated'] and all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==ev['diagnostics'][k]['expected']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items()))
        require(arm+'_rates_recomputed',ev['greedy_rates']==rate(rows))
        summaries[arm]=dict(BPB=body['bpb'],rates=ev['greedy_rates'],content={k+'_score2':sum(s[k]==2 for s in scores[arm].values()) for k in ('grammar','relevance','coherence')},
            appropriate_EOS=sum(s['completion'] for s in scores[arm].values()),diagnostics=ev['diagnostics'],
            condition={s:condition['results'][s]['summary'] for s in ('train','dev')},previous_dev=previous_eval['arms'][arm]['summary'],known_structure=condition['results']['dev']['known_structure'],unseen_structure=condition['results']['dev']['unseen_structure'],
            teachers=total,valid_input=d['additional_input_tokens'],physical_input=d['physical_input_tokens'],training_seconds=d['training_seconds'],
            updates=len(history),EOS_teachers=d['source_eos_teachers'],mode=d['mode'],peak_allocated_bytes=d['peak_allocated_bytes'])
        del state
    eligible=[a for a in ('shuffle','isolated') if result['conditions'][a]['diagnostic_pass']]
    selected=max(eligible,key=lambda a:(result['conditions'][a]['results']['dev']['summary']['accuracy'],result['conditions'][a]['results']['dev']['summary']['both_accuracy'],a=='shuffle')) if eligible else None
    require('frozen_selection_and_conditional100M_recomputed',selected==result['selected'] and bool(selected)==result['mixed100m_executed'])
    if selected:require('mixed_same_Web_teacher_budget_and_sampler_cursor',samplers['mixed-fixed']['web']==samplers['mixed-candidate']['web'] and all(samplers[a]['source_teachers']==dict(web=80000000,short=20000000) for a in ('mixed-fixed','mixed-candidate')))
    pairs=[('fixed','shuffle'),('fixed','isolated')]+([('mixed-fixed','mixed-candidate')] if selected else [])
    comparisons={}
    for left,right in pairs:
        a=result['evaluations'][left];b=result['evaluations'][right]
        require(left+'_'+right+'_paired_same_IDs_bytes',[(r['id'],r['prefix']) for r in a['generation']['outputs']]==[(r['id'],r['prefix']) for r in b['generation']['outputs']] and [(r['doc_id'],r['body_bytes']) for r in a['body']['rows']]==[(r['doc_id'],r['body_bytes']) for r in b['body']['rows']])
        quality=quality_gates(a,b,scores[left],scores[right],'content')
        practical=dict(coherence_at_least27=summaries[right]['content']['coherence_score2']>=27,appropriate_at_least27=summaries[right]['appropriate_EOS']>=27,
            EOS_at_least37=b['greedy_rates']['eos']>=37,repetition_at_most18=b['greedy_rates']['repetition']<=18)
        original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),b)
        differences={}
        for task in c['evaluation']['tasks']:
            l,r=[{v['id']:v for v in read_json(run/'evaluation'/name/'evaluation'/(task+'.json'))['rows']} for name in (left,right)]
            require(left+'_'+right+'_paired_'+task,set(l)==set(r))
            differences[task]=clustered_ci([dict(id=k,family=r[k].get('family',k),difference=r[k]['credit']-l[k]['credit']) for k in l],key='difference')
        comparisons[left+'__'+right]=dict(quality=quality,practical=practical,original_Web_gates=original,paired_diagnostics=differences,
            eligible_for_full=quality['passed'] and all(practical.values()) and all(original.values()))
    review=dict(status='passed_evidence_audit',checks=checks,summaries=summaries,comparisons=comparisons,selected=selected,
        scientific_teacher_tokens=result['scientific_teacher_tokens'],scientific_valid_input_tokens=result['scientific_valid_input_tokens'],physical_input_tokens=result['physical_input_tokens'],
        verification_teacher_tokens=result['verification_teacher_tokens'],GPU_seconds=result['GPU_seconds']+previous_eval['GPU_wall_seconds'],
        config_sha256=sha256(study.CONFIG),result_sha256=sha256(run/'result.json'),annotations_sha256=sha256(run/'annotations.json'),reviewer_sha256=sha256(Path(__file__)),checked_at=now(),
        quality_targets_achieved=False,limits='Single training seed, authored synthetic data, nonblind Codex content review; fresh dev used for selection, protected test unused')
    write_json(run/'review.json',review)
    print(json.dumps(dict(status=review['status'],checks=len(checks),selected=selected,summaries={a:{k:v for k,v in s.items() if k!='diagnostics'} for a,s in summaries.items()},comparisons=comparisons),ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);main()
