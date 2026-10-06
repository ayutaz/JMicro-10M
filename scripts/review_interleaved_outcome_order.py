"""Whole masked recipe accounting and all80 against unchanged strong controls."""
import json
import math
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,finite_state
from review_parameter_displacement_anchor import content
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from interleaved_order_analysis import four_cell_contrasts
import run_interleaved_outcome_order as study


def accounting(parent,state,record,history,ledger):
    a=state['sampler']['prefix_mask_accounting'];actual=a['actual'];lineage=state['lineage'];teachers=sum(actual['teachers'].values())
    physical=len(history)*state['spec']['context']*state['spec']['batch'];reference=state['sampler'].copy();reference.pop('prefix_mask_accounting')
    if (not finite_state(state) or not history or len(history)!=len(ledger['rows'])
            or [row['update'] for row in history]!=list(range(parent['update']+1,state['update']+1))
            or state['update']-parent['update']!=len(history) or state['tokens']-parent['tokens']!=physical
            or record['additional_input_tokens']!=physical or state['supervised_tokens']-parent['supervised_tokens']!=teachers
            or record['additional_supervised_tokens']!=teachers or ledger['actual_masked_suffix_teacher_tokens']!=teachers
            or actual!=ledger['actual_source_accounting'] or a['reference_policy']!='interleaved'
            or a['initial_reference']!=lineage['actual_initial_reference_sampler']
            or any(a['initial_reference']['source_teachers'].values())
            or state['body_bytes']-parent['body_bytes']!=sum(actual['body_bytes'].values())
            or state['weighted_teacher_mass']!=teachers or state['focus_teacher_tokens']!=sum(actual['focus'].values())
            or lineage['actual_parent_sampler']!=parent['sampler'] or lineage['parent_scheduler']!=parent['scheduler']
            or not lineage['no_reheat'] or state['study_binding']!=record['binding']
            or record['sampler']!=state['sampler'] or record['token_digest']!=state['token_digest']
            or record['reference_token_digest']!=a['reference_token_digest']
            or a['reference_token_digest']!=ledger['original_reference_token_digest']
            or a['source_digests']!=ledger['source_digests'] or record['source_digests']!=ledger['source_digests']
            or a['source_digests']!=ledger['staged_source_digests'] or reference!=ledger['terminal_reference_sampler']
            or state['spec']['research_kind']!=study.KIND or any(g['lr']!=.00001 for g in state['optimizer']['param_groups'])):
        raise ValueError('Actual masked whole-recipe versus original reference/source accounting differs')
    previous_teachers=previous_bytes=0
    for row,expected in zip(history,ledger['rows'],strict=True):
        if (row['update']!=expected['update'] or row['reference_token_digest']!=expected['reference_token_digest']
                or row['actual_source_routes']!=expected['actual_source_routes']
                or row['additional_teacher_tokens']-previous_teachers!=expected['actual_teachers']
                or row['body_bytes_seen']-parent['body_bytes']-previous_bytes!=expected['actual_body_bytes']
                or row['lr']!=.00001 or row['outcome_weight']!=1 or row['weighted_teacher_mass']!=row['additional_teacher_tokens']
                or any(not math.isfinite(row[k]) for k in ('loss','gradient_norm'))):raise ValueError('Complete actual mixed history differs')
        previous_teachers=row['additional_teacher_tokens'];previous_bytes=row['body_bytes_seen']-parent['body_bytes']
    for key in ('token_digest','focus_token_digest','focus_teacher_tokens','weighted_teacher_mass'):
        if history[-1][key]!=state[key]:raise ValueError('Terminal actual target history differs')
    return dict(updates=len(history),actual_new_hard_teachers=teachers,original_nominal_reference_teachers=ledger['original_reference_suffix_teacher_tokens'],
        physical_input_tokens=physical,all_original_mixed_global_inputs_match=True,all_per_source_both_order_windows_targets_and_cursors_match=True,
        actual_source_accounting=actual,source_digests=a['source_digests'])


def main():
    torch.set_num_threads(2);c=study.inspect(study.CONFIG);r=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json')
    if (job['status']!='complete' or alive(job) or job['GPU_elapsed_seconds']!=r['GPU_seconds']
            or r['GPU_seconds']+c['verification_GPU_seconds']>900 or r['config_sha256']!=sha256(study.CONFIG)
            or r['scientific_optimizer_updates']!=3068 or r['scientific_teacher_tokens']!=91641755):raise ValueError('Actual finite terminal fourth cell required')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);record=r['checkpoint']
    study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    if state['study_binding']!=study.binding(c,study.CONFIG) or state['sampler']['source_teachers']!=study.prior.GOALS:raise ValueError('Completed whole source quotas required')
    history=[json.loads(s) for s in (study.RUN/study.ARM/'training/metrics.jsonl').read_text().splitlines()]
    audit=accounting(parent,state,record,history,read_json(study.LEDGER));base=read_json(Path(c['original_config']['path']))
    evaluations={'masked_mixed':r['evaluation']};summaries={};scores={}
    summaries['masked_mixed'],scores['masked_mixed']=content('masked_mixed',r['evaluation'],record,base,
        study.RUN/f'evaluation/{study.ARM}/evaluation/generation.json',study.RUN/'content-notes.json')
    old=[('full_mixed','mixed_control_result','historical_parent','mixed_control_notes'),('full_staged','control_result','source_order','control_notes')]
    for name,key,arm,notes_key in old:
        ref=c['references'][key];saved=read_json(Path(ref['path']));evaluations[name]=saved['evaluations'][arm]
        raw=Path(ref['path']).parent/f'evaluation/{arm}/evaluation/generation.json'
        summaries[name],scores[name]=content(name,evaluations[name],saved['checkpoints'][arm],base,raw,Path(c['references'][notes_key]['path']))
    ref=c['references']['masked_staged_result'];saved=read_json(Path(ref['path']));evaluations['masked_staged']=saved['evaluation']
    summaries['masked_staged'],scores['masked_staged']=content('masked_staged',saved['evaluation'],saved['checkpoint'],base,
        Path(ref['path']).parent/'evaluation/outcome_EOS_only/evaluation/generation.json',Path(ref['path']).parent/'content-notes.json')
    if summaries['full_staged']['coherent']!=23 or summaries['full_staged']['rates']['eos']!=76 or summaries['masked_staged']['coherent']!=35:
        raise ValueError('Fixed old cell content baseline changed')
    candidate=evaluations['masked_mixed'];relative=quality_gates(evaluations['full_staged'],candidate,scores['full_staged'],scores['masked_mixed'],'content')
    summary=summaries['masked_mixed'];rates=summary['rates']
    absolute=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,appropriate_at_least27=summary['appropriate']>=27,
        EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
    original=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),candidate)
    supplemental=quality_gates(evaluations['masked_staged'],candidate,scores['masked_staged'],scores['masked_mixed'],'content')
    for suite in ('bridge','retention'):
        t=r[suite]
        if t['evaluated_requests']!=512 or not all(t['checks'].values()) or t['checkpoint_sha256']!=record['checkpoint_sha256']:raise ValueError('All read-only transfer requests required')
    eligible=relative['passed'] and all(absolute.values()) and all(original.values())
    report=dict(status='qualified_fourth_cell_pending_independent_learning_seed_full_dev_protected_test' if eligible else 'rejected_single_order_target_fourth_cell',
        created_at=now(),result_sha256=sha256(study.RUN/'compare-result.json'),summaries=summaries,accounting=audit,
        relative_to_strong_staged=relative,absolute_dev_screen=absolute,historical_Web=original,
        observed_masked_staged_comparison=supplemental,four_cell_analysis=four_cell_contrasts(evaluations,scores),eligible_for_final_Base_validation=eligible,
        all80_individually_read=True,independent_human_blind=False,three_old_cells_reused_unchanged=True,
        actual_science_GPU_seconds=r['GPU_seconds'],own_probe_GPU_seconds=c['verification_GPU_seconds'],
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Only qualified recipe permits independent learned recipe seed/full dev/protected test/adoption; failure ends this one fourth-cell comparison without salvage sweep.')
    if (study.RUN/'review.json').exists():raise ValueError('Preserve original terminal four-cell review')
    atomic_json(study.RUN/'review.json',report);atomic_json(ROOT/'reports/phase6/interleaved_outcome_review.json',report)
    print(json.dumps(dict(summaries=summaries,eligible=eligible),ensure_ascii=False))


if __name__=='__main__':main()
