"""Original-input suffix accounting, all80 raw-bound review, unchanged guards."""
import json
import math
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,finite_state
from run_eos_short_pilot import equal_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from review_parameter_displacement_anchor import content
import run_conditional_prefix_mask as study


def accounting(parent,state,record,history,ledger):
    a=state['sampler']['prefix_mask_accounting'];actual=a['actual'];lineage=state['lineage']
    teachers=sum(actual['teachers'].values());physical=len(history)*state['spec']['context']*state['spec']['batch']
    if (not finite_state(state) or not history or len(history)!=len(ledger['rows'])
            or [row['update'] for row in history]!=list(range(parent['update']+1,state['update']+1))
            or state['update']-parent['update']!=len(history)
            or state['tokens']-parent['tokens']!=physical or record['additional_input_tokens']!=physical
            or state['supervised_tokens']-parent['supervised_tokens']!=teachers
            or record['additional_supervised_tokens']!=teachers or ledger['actual_masked_suffix_teacher_tokens']!=teachers
            or actual!=ledger['actual_source_accounting'] or a['initial_reference']!=parent['sampler']
            or state['body_bytes']-parent['body_bytes']!=sum(actual['body_bytes'].values())
            or state['weighted_teacher_mass']!=teachers or state['focus_teacher_tokens']!=sum(actual['focus'].values())
            or lineage['actual_parent_sampler']!=parent['sampler'] or lineage['parent_scheduler']!=parent['scheduler']
            or not lineage['no_reheat'] or lineage['optimizer_policy']!='inherit'
            or state['study_binding']!=record['binding'] or state['spec']['research_kind']!=study.KIND
            or record['sampler']!=state['sampler'] or record['token_digest']!=state['token_digest']
            or record['reference_token_digest']!=a['reference_token_digest']
            or a['reference_token_digest']!=ledger['original_reference_token_digest']
            or any(g['lr']!=.00001 for g in state['optimizer']['param_groups'])):
        raise ValueError('Actual masked teachers versus original reference input accounting differs')
    reference=state['sampler'].copy();reference.pop('prefix_mask_accounting')
    if reference!=ledger['terminal_reference_sampler']:raise ValueError('All original source/input cursors differ')
    previous_teachers=previous_bytes=0
    for row,expected in zip(history,ledger['rows'],strict=True):
        if (row['update']!=expected['update'] or row['reference_token_digest']!=expected['reference_token_digest']
                or row['actual_source_routes']!=expected['actual_source_routes']
                or row['additional_teacher_tokens']-previous_teachers!=expected['actual_teachers']
                or row['body_bytes_seen']-parent['body_bytes']-previous_bytes!=expected['actual_body_bytes']
                or row['lr']!=.00001 or row['outcome_weight']!=1
                or any(not math.isfinite(row[k]) for k in ('loss','gradient_norm'))
                or row['weighted_teacher_mass']!=row['additional_teacher_tokens']):
            raise ValueError('Complete scientific masked/reference history differs')
        previous_teachers=row['additional_teacher_tokens'];previous_bytes=row['body_bytes_seen']-parent['body_bytes']
    for key in ('token_digest','focus_token_digest','focus_teacher_tokens','weighted_teacher_mass'):
        if history[-1][key]!=state[key]:raise ValueError('Terminal masked history digest/counters differ')
    return dict(completed_updates=len(history),new_actual_hard_teachers=teachers,physical_input_tokens=physical,
        reference_input_teachers=ledger['original_reference_suffix_teacher_tokens'],actual_source_accounting=actual,
        all_original_reference_input_and_cursor_checks=True,matched_teacher_budget=False)


def main():
    torch.set_num_threads(2);c=study.inspect(study.CONFIG);job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'compare-result.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']+c['verification_GPU_seconds']>600 or r['config_sha256']!=sha256(study.CONFIG)
            or not r['matched_input_suffix'] or r['matched_teacher_budget'] or r['scientific_optimizer_updates']!=318):
        raise ValueError('Actual terminated fixed-input scientific suffix required')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);record=r['checkpoint']
    study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    history=[json.loads(s) for s in (study.RUN/study.ARM/'training/metrics.jsonl').read_text().splitlines()]
    if (state['study_binding']!=study.binding(c,study.CONFIG) or state['sampler']['source_teachers']!=study.prior.GOALS
            or r['scientific_teacher_tokens']!=c['actual_scientific_teacher_tokens_predicted']):raise ValueError('Fixed completed masked suffix differs')
    audit=accounting(parent,state,record,history,read_json(study.LEDGER));base=read_json(Path(c['original_config']['path']))
    candidate=r['evaluation'];raw=study.RUN/f'evaluation/{study.ARM}/evaluation/generation.json'
    summary,scores=content(study.ARM,candidate,record,base,raw,study.RUN/'content-notes.json')
    previous=read_json(Path(c['references']['control_result']['path']));strong=previous['evaluations']['source_order']
    old_record=previous['checkpoints']['source_order']
    if dict(path=old_record['checkpoint'],sha256=old_record['checkpoint_sha256'])!=c['strong_control']:raise ValueError('Strong original control differs')
    old_raw=ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json'
    old_summary,old_scores=content('strong_staged',strong,old_record,base,old_raw,Path(c['references']['control_notes']['path']))
    if old_summary['coherent']!=23 or old_summary['rates']['eos']!=76 or old_summary['rates']['repetition']!=2:raise ValueError('Original quality baseline changed')
    relative=quality_gates(strong,candidate,old_scores,scores,'content')
    historical=read_json(Path(base['reference']['web_screen']['path']));absolute=adoption_checks(historical,candidate)
    for suite in ('bridge','retention'):
        t=r[suite]
        if t['evaluated_requests']!=512 or not all(t['checks'].values()) or t['checkpoint_sha256']!=record['checkpoint_sha256']:
            raise ValueError('All actual read-only transfer requests required')
    eligible=relative['passed'] and all(absolute.values())
    report=dict(status='qualified_pilot_pending_independent_learning_seed_full_dev_protected_test' if eligible else 'rejected_single_prefix_mask_comparison',
        created_at=now(),result_sha256=sha256(study.RUN/'compare-result.json'),summaries=dict(strong_staged=old_summary,outcome_EOS_only=summary),
        accounting=audit,relative_to_original_strong_staged=relative,absolute_and_historical_guards=absolute,
        eligible_for_final_Base_validation=eligible,all80_individually_read=True,independent_human_blind=False,
        actual_science_GPU_seconds=r['GPU_seconds'],own_probe_GPU_seconds=c['verification_GPU_seconds'],
        control_whole100M_and_shared_prefix_are_reused_not_new_learning=True,matched_input_suffix=True,matched_teacher_budget=False,
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        limitations='Masking changes hard teacher count and EOS target fraction, and the hypothesis follows observed failures. '
            'One suffix/nonblind80 does not isolate amount, prove the sole root cause, certify human judgement or a model capacity ceiling.',
        next_action='Only qualified pilot permits independent learned recipe seed/full dev/protected test/adoption; '
            'failure terminates this single mask/source/checkpoint/decoder comparison without salvage sweep.')
    destination=study.RUN/'review.json'
    if destination.exists():raise ValueError('Preserve original complete review')
    atomic_json(destination,report);atomic_json(ROOT/'reports/phase6/conditional_prefix_mask_review.json',report)
    print(json.dumps(dict(summaries=report['summaries'],eligible=eligible),ensure_ascii=False))


if __name__=='__main__':main()
