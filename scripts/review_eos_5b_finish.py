"""Audit saved final5B finishing evidence on CPU, without repeated inference."""
import json
import math
from pathlib import Path
import re
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from jmicro.eos_pilot import pilot_lr
from phase6_performance import alive
from run_eos_short_pilot import rate
from run_eos_complete_100m import adoption_checks
from run_eos_low_lr import tests_summary
from run_eos_5b_finish import safe_control, SOURCES


def validate_rows(rows,tok):
    for row in rows:
        ids = row['generated_ids']
        assert 0<len(ids)<=64 and 3 not in ids[:-1]
        try:
            raw = tok.decode_bytes(ids) if 1 not in ids else b''
            text, valid = raw.decode('utf-8'), 1 not in ids
        except UnicodeDecodeError:
            text, valid = raw.decode('utf-8',errors='replace'), False
        assert row['text']==text and row['valid_utf8']==valid
        assert row['stop_reason']==('stop_id' if ids[-1]==3 else 'max_new_tokens')
        assert row['repetition']==bool(re.search(r'(.{2,}?)\1\1',text,flags=re.DOTALL))
        assert row['empty_response']==(not text.strip())
        assert row['role_leak']==any(i in (4,5,6,7) for i in ids)


def main():
    torch.set_num_threads(2)
    plan_path = ROOT / 'configs/phase6/eos_5b_finish_100m.json'
    plan = read_json(plan_path)
    run = ROOT / plan['output']
    job, result = read_json(run / 'job.json'), read_json(run / 'result.json')
    checks = {}
    def require(key,condition):
        checks[key] = bool(condition)
        assert condition,key
    require('actual_job_complete_and_exited',job['status']=='complete' and not alive(job))
    require('GPU_budget',job['gpu_elapsed_seconds']<=plan['gpu_budget_seconds'])
    require('frozen_plan_source_core',result['binding']==job['binding'] and result['binding']['plan_sha256']==sha256(plan_path) and
            implementation_hashes()==plan['implementation'] and plan['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES})
    require('same_parent_unchanged',sha256(Path(plan['parent']['path']))==plan['parent']['sha256'])
    require('parent_full_fixed_reused_unchanged',sha256(Path(plan['parent_full_body']))==plan['baseline_body_sha256'] and
            sha256(Path(plan['parent_generation']))==plan['baseline_generation_sha256'] and result['parent_fixed_and_full_reused'])
    require('targeted_CPU_checks',result['tests']==tests_summary(run/'tests.xml') and result['tests']['tests']>=33)
    display = read_json(ROOT/'reports/phase6/text_display_verification.json')
    require('production_display_evidence',display['status']=='passed_production_display_saved400' and display['unchanged_valid_text']==398 and
            display['raw_unicode_failures_retained']==2 and all(sha256(ROOT/p)==h for p,h in display['implementation'].items()))
    gate = read_json(run/'resume-gate.json')
    require('actual_CUDA8_resume_allstate_history',gate==result['resume_gate'] and gate['passed'] and all(gate['checks'].values()) and
            gate['GPU_optimizer_updates']==8 and gate['input_tokens']==262144 and gate['binding']==result['binding'])
    tok = Tokenizer(ROOT/plan['tokenizer'])
    require('tokenizer_and_suites_frozen',sha256(ROOT/plan['tokenizer'])==plan['tokenizer_sha256'] and
            sha256(ROOT/'eval/base.jsonl')==plan['suite_sha256'] and sha256(run/'auxiliary-dev.json')==plan['auxiliary_sha256'])
    fixed_cases = [json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines() if json.loads(line)['split']=='dev'][:80]
    aux = read_json(run/'auxiliary-dev.json')['cases']
    parent_aux = read_json(run/'parent-auxiliary.json')
    require('new5B_parent_auxiliary_bound',parent_aux['binding']==result['binding'] and parent_aux['checkpoint_sha256']==plan['parent']['sha256'] and
            [r['id'] for r in parent_aux['auxiliary']['outputs']]==[c['id'] for c in aux])
    validate_rows(parent_aux['auxiliary']['outputs'],tok)
    screens, arms = {}, {}
    parent_body = read_json(Path(plan['parent_full_body']))['body']
    growth = {}
    for arm,record in result['arms'].items():
        checkpoint = Path(record['checkpoint'])
        require(arm+'_checkpoint_and_binding',sha256(checkpoint)==record['checkpoint_sha256'] and record['binding']==result['binding'])
        state = torch.load(checkpoint,map_location='cpu',weights_only=False)
        require(arm+'_actual_final_tokens_updates',state['tokens']==plan['final_cumulative_tokens'] and state['update']==plan['final_update'] and
                record['additional_input_tokens']==plan['tokens_per_arm'] and record['tokens']==state['tokens'] and record['update']==state['update'])
        require(arm+'_state_lineage_core',state['pilot_binding']==result['binding'] and state['implementation_sha256']==plan['implementation'] and
                state['lineage']['parent_update']==plan['parent']['update'] and state['lineage']['parent_tokens']==plan['parent']['tokens_seen'])
        sampler = state['sampler']
        require(arm+'_saved_cursors_no_short_wrap',sampler['position']==plan['updates_per_arm'] and sampler['short']['epoch']==0 and
                sum(sampler['source_tokens'].values())==plan['tokens_per_arm'] and sampler['source_tokens']==record['source_tokens'] and
                sampler['source_eos']==record['source_eos_teachers'] and sampler['source_tokens']['short']==(19988480 if arm=='short20' else 0))
        require(arm+'_finite_weights_Adam',all(bool(torch.isfinite(t).all()) for t in state['model'].values()) and
                all(bool(torch.isfinite(t).all()) for r in state['optimizer']['state'].values() for t in r.values() if isinstance(t,torch.Tensor)))
        require(arm+'_optimizer_scheduler_RNG_saved',all(int(r['step'])==state['update'] for r in state['optimizer']['state'].values()) and
                state['scheduler']['last_epoch']==state['update'] and len(state['rng']['cuda'])==1 and
                all(math.isclose(g['lr'],.00002,rel_tol=1e-12) for g in state['optimizer']['param_groups']))
        rows = [json.loads(line) for line in (run/arm/'metrics.jsonl').read_text().splitlines()]
        require(arm+'_all3052_finite_contiguous_updates',len(rows)==3052 and [r['update'] for r in rows]==list(range(152589,155641)) and
                all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in rows) and
                rows[-1]['token_digest']==state['token_digest'] and rows[-1]['tokens_seen']==state['tokens'])
        require(arm+'_frozen_actual_LR_curve',all(math.isclose(r['lr'],.0002*pilot_lr(state['spec'],r['update']-1),rel_tol=1e-12) for r in rows))
        screen = read_json(run/(arm+'-evaluation.json'))
        screens[arm] = screen
        require(arm+'_screen_binding_and256',screen['binding']==result['binding'] and screen['checkpoint_sha256']==record['checkpoint_sha256'] and
                screen['body']['documents']==256 and screen['evaluation_RNG_isolated'] and
                math.isfinite(screen['body']['bpb']) and all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) and
                r['body_tokens']==r['scored_body_tokens'] for r in screen['body']['rows']) and
                [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in screen['body']['rows']]==
                [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in parent_body['rows'][:256]])
        require(arm+'_fixed80_aux80_same',[(r['id'],r['prefix']) for r in screen['generation']['outputs']]==[(c['id'],c['prefix']) for c in fixed_cases] and
                [r['id'] for r in screen['auxiliary']['outputs']]==[c['id'] for c in aux] and screen['auxiliary_sha256']==plan['auxiliary_sha256'])
        validate_rows(screen['generation']['outputs']+screen['auxiliary']['outputs'],tok)
        require(arm+'_raw_screen_flags_and_rates',rate(screen['generation']['outputs'])==screen['greedy_rates'] and
                rate(screen['auxiliary']['outputs'])==screen['auxiliary']['rates'])
        arms[arm] = dict(checkpoint=str(checkpoint),checkpoint_sha256=record['checkpoint_sha256'],training_input_tokens=state['tokens'],
            additional_training_input_tokens=record['additional_input_tokens'],training_seconds=record['training_seconds'],
            source_tokens=record['source_tokens'],source_eos_teachers=record['source_eos_teachers'],screen_BPB=screen['body']['bpb'],
            fixed80=screen['greedy_rates'],auxiliary=screen['auxiliary']['rates'],
            auxiliary_teacher_EOS_NLL=screen['auxiliary']['teacher_mean_eos_nll'],auxiliary_teacher_EOS_argmax=screen['auxiliary']['teacher_eos_argmax'])
        del state
    mixture = adoption_checks(screens['web'],screens['short20'])
    require('original_mixture_gate_recomputed',mixture==result['improvement_checks'] and all(mixture.values())==result['improvement_gate_passed'])
    safe = safe_control(screens['web']['greedy_rates'],plan['parent_fixed_repetition'])
    expected_full = ['web','short20'] if result['improvement_gate_passed'] else (['web'] if safe else [])
    require('conditional_full_not_weakened',result['web_full_generation_eligible']==safe and result['full_evaluated_arms']==expected_full)
    body_keys = lambda b:[(r['doc_id'],r['body_bytes'],r['body_tokens'],r['scored_body_tokens']) for r in b['rows']]
    parent_gen = read_json(Path(plan['parent_generation']))['generation']
    gen_keys = lambda g:[(r['id'],r['prefix'],r['category'],r['decoding'],r['suppressed'],r['seed']) for r in g['outputs']]
    for arm in expected_full:
        full = read_json(run/(arm+'-full-evaluation.json'))
        body = full['body']
        require(arm+'_same_full_body_finite_once',full['binding']==result['binding'] and body_keys(body)==body_keys(parent_body) and
            body['documents']==89416 and body['body_bytes']==164344743 and body['body_tokens']==42003934 and
            all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) and r['body_tokens']==r['scored_body_tokens'] for r in body['rows']) and
            math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        arms[arm]['full_BPB'] = body['bpb']
        if 'generation' in full:
            gen = full['generation']
            require(arm+'_same400_keys_and_RNG',gen_keys(gen)==gen_keys(parent_gen) and full['evaluation_RNG_isolated'])
            validate_rows(gen['outputs'],tok)
            fixed = [r for r in gen['outputs'] if r['decoding']=='greedy' and r['suppressed']]
            require(arm+'_full_screen_IDs_match',[r['generated_ids'] for r in fixed]==[r['generated_ids'] for r in screens[arm]['generation']['outputs']])
            arms[arm]['all400'] = rate(gen['outputs'])
            growth[arm] = dict(full_BPB_no_major_regression=body['bpb']<=plan['parent_full_BPB']+.001,
                fixed_repetition_not8_worse=rate(fixed)['repetition']<plan['parent_fixed_repetition']+8,
                no_new_empty_role_unicode=all(rate(gen['outputs'])[k]==0 for k in ('empty','role_leak','unicode_failure')),
                all80_screen_IDs_match=True)
    require('growth_criteria_independently_recomputed',growth==result['growth_checks'])
    if result['improvement_gate_passed']:
        raw = arms['short20']['all400']
        full_checks = dict(BPB_within1percent_full_control=arms['short20']['full_BPB']<=arms['web']['full_BPB']*1.01,
            all80_screen_IDs_match=True,no_new_empty_role_unicode_vs_original2B=all(raw[k]==0 for k in ('empty','role_leak','unicode_failure')))
        require('full_adoption_criteria_recomputed',full_checks==result['full_adoption_checks'] and
                all(full_checks.values())==result['automatic_full_gate_passed'])
    require('scientific_verification_budgets_separate',result['scientific_training_input_tokens']==200015872 and
            result['verification_training_input_tokens']==262144 and not result['test_split_used'] and not result['quality_targets_achieved'])
    packet_path = run/'content-review-packet.json'
    content_path = ROOT/'reports/phase6/eos_5b_content_review.json'
    packet, content = read_json(packet_path), read_json(content_path)
    require('all_fixed80_and_natural_stop_content_review',content['status']=='completed_saved_content_review' and
        content['packet_sha256']==sha256(packet_path) and content['fixed80_reviewed_ids']==[r['id'] for r in screens['short20']['generation']['outputs']] and
        content['candidate_natural_stops_reviewed']==packet['natural_stops_total'] and
        content['candidate_unique_stop_text_indices_reviewed']==list(range(len(packet['unique_natural_stop_texts']))) and
        content['control_natural_stops_reviewed']==len(packet['control_natural_stops']) and
        content['auxiliary_natural_stop_ids_reviewed']==[r['id'] for r in screens['short20']['auxiliary']['outputs'] if r['stop_reason']=='stop_id'] and
        all(sha256(ROOT/p)==digest for p,digest in packet['source_sha256'].items()) and
        not content['blind_human_score'] and not content['quality_targets_achieved'])
    review = dict(status='completed_verified5B_finishing_steps1_2_3',verified_at=now(),checks=checks,
        parent=plan['parent'],parent_full_BPB=plan['parent_full_BPB'],parent_auxiliary=parent_aux['auxiliary']['rates'],
        arms=arms,improvement_checks=mixture,full_adoption_checks=result['full_adoption_checks'],
        automatic_full_gate_passed=result['automatic_full_gate_passed'],growth_checks=result['growth_checks'],
        scientific_training_input_tokens=200015872,verification_training_input_tokens=262144,
        gpu_elapsed_seconds=job['gpu_elapsed_seconds'],GPU_budget_seconds=3000,
        quality_targets_achieved=False,test_split_used=False,stop_before=result['stop_before'],binding=result['binding'],
        content_review_sha256=sha256(content_path))
    write_json(ROOT/'reports/phase6/eos_5b_finish_review.json',review)
    print(json.dumps(dict(status=review['status'],checks=checks,arms=arms),ensure_ascii=False))


if __name__=='__main__':
    main()
