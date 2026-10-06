"""Audit whole staged ledger, boundary-only constraints and unchanged Base gates."""
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
from run_eos_short_pilot import equal_state
import run_block_Web_constraint as study


def accounting(parent,state,record,history,c):
    ledger=read_json(Path(c['references']['reference_input_ledger']['path']))
    expected=[json.loads(s) for s in Path(c['references']['staged_metrics']['path']).read_text().splitlines()]
    sampler=state['sampler'];a=sampler['prefix_mask_accounting'];reference=sampler.copy();reference.pop('prefix_mask_accounting')
    if (not finite_state(state) or len(history)!=3068 or len(expected)!=3068
            or state['update']-parent['update']!=3068 or state['tokens']-parent['tokens']!=100532224
            or state['supervised_tokens']-parent['supervised_tokens']!=91641755 or record['additional_supervised_tokens']!=91641755
            or record['additional_input_tokens']!=100532224 or sampler['source_teachers']!=c['teacher_goals']
            or a['reference_policy']!='staged' or a['actual']!=ledger['actual_source_accounting']
            or reference!=ledger['staged_reference_sampler'] or a['source_digests']!=ledger['source_digests']
            or record['sampler']!=sampler or record['source_digests']!=a['source_digests']
            or state['study_binding']!=study.binding(c,study.CONFIG) or record['binding']!=state['study_binding']
            or state['spec']['research_kind']!=study.KIND or state['spec']['block_updates']!=20
            or not state['spec']['projected_updates_field_counts_blocks']
            or state['spec']['block_Web_trainer_sha256']!=c['source_sha256']['scripts/block_Web_constraint.py']
            or state['lineage']['actual_parent_sampler']!=parent['sampler'] or state['lineage']['parent_scheduler']!=parent['scheduler']
            or not state['lineage']['no_reheat'] or any(g['lr']!=.00001 for g in state['optimizer']['param_groups'])):
        raise ValueError('Whole actual staged native/counter/source/lineage differs')
    body=c['memory_binding']['body_teachers'];physical=c['memory_binding']['physical_input_tokens'];previous_teachers=0
    totals=dict(forward_only_calls=0,gradient_calls=0,teacher_observations=0,gradient_teacher_tokens=0,physical_input_tokens=0,
        projected_updates=0,backtracked_updates=0,accepted_updates=0,accepted_blocks=0)
    boundaries=[]
    for i,(row,ref) in enumerate(zip(history,expected,strict=True)):
        k=i//20+1;start=parent['update']+(k-1)*20;end=parent['update']+min(k*20,3068);decision=row['boundary_constraint']
        if (row['update']!=parent['update']+i+1 or row['reference_token_digest']!=ref['token_digest']
                or row['lr']!=.00001 or row['outcome_weight']!=1 or row['weighted_teacher_mass']!=row['additional_teacher_tokens']
                or sum(row['actual_source_teachers'].values())!=row['additional_teacher_tokens']
                or row['additional_teacher_tokens']<=previous_teachers or not all(math.isfinite(row[key]) for key in ('loss','gradient_norm'))
                or row['block_boundary_index']!=k or row['block_boundary_update']!=end
                or not row['constraint_valid_only_at_block_boundary'] or decision['scope']!='accepted_block_boundary_only'
                or decision['block_start_update']!=start or decision['block_end_update']!=end or decision['block_source_updates']!=end-start
                or not decision['accepted'] or decision['reference_body_NLL']!=c['reference_body_NLL']
                or decision['ceiling_body_NLL']!=c['reference_body_NLL']*1.01 or decision['final_body_NLL']>decision['ceiling_body_NLL']):
            raise ValueError('Actual source row or explicitly scoped boundary differs')
        previous_teachers=row['additional_teacher_tokens']
        if i and i%20 and decision!=history[i-1]['boundary_constraint']:raise ValueError('Same block boundary metadata differs')
        at_end=row['update']==end
        if ('block_GPU_seconds' in row)!=at_end or ('accepted_auxiliary' in row)!=at_end:raise ValueError('Boundary accounting must only commit at end')
        if at_end:
            if not math.isfinite(row['block_GPU_seconds']) or row['block_GPU_seconds']<=0:raise ValueError('Actual block timing required')
            calls=len(decision['trials']);gradient=int(decision['projected'])
            if decision['trials'][-1]['body_NLL']!=decision['final_body_NLL'] or any(not math.isfinite(t['body_NLL']) for t in decision['trials']):
                raise ValueError('Finite memory observations differ')
            totals['forward_only_calls']+=calls;totals['gradient_calls']+=gradient
            totals['teacher_observations']+=(calls+gradient)*body;totals['gradient_teacher_tokens']+=gradient*body
            totals['physical_input_tokens']+=(calls+gradient)*physical;totals['projected_updates']+=gradient
            totals['backtracked_updates']+=int(decision['backtracked']);totals['accepted_updates']+=end-start;totals['accepted_blocks']+=1
            if row['accepted_auxiliary']!=totals:raise ValueError('Actual auxiliary gradient/observation ledger differs')
            boundaries.append(decision)
    if state['auxiliary']!=totals or record['auxiliary']!=totals or state['last_constraint']!=boundaries[-1]:raise ValueError('Terminal boundary/auxiliary differs')
    for key in ('token_digest','focus_token_digest','focus_teacher_tokens','weighted_teacher_mass'):
        if state[key]!=history[-1][key]:raise ValueError('Terminal source history differs')
    return dict(source_updates=3068,accepted_blocks=154,source_CE_teachers=91641755,reference_teachers=100000000,
        physical_source_positions=100532224,auxiliary=totals,total_source_plus_auxiliary_gradient_teachers=91641755+totals['gradient_teacher_tokens'],
        all_original_staged_global_inputs_targets_match=True,all_common_masked_per_source_windows_match=True,
        bound_scope='154 accepted native FP32/math boundaries; intermediate updates not guaranteed.',
        all_boundary_losses_bounded=True,maximum_boundary_body_NLL=max(d['final_body_NLL'] for d in boundaries))


def main():
    torch.set_num_threads(2);c=study.inspect(study.CONFIG);r=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['config_sha256']!=sha256(study.CONFIG) or 'finite_rejection' in r
            or r['GPU_seconds']+c['verification_GPU_seconds']+c['previous_related_GPU_seconds']>2400):
        raise ValueError('Actual complete candidate within cumulative budget required')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);record=r['checkpoint']
    study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    audit=accounting(parent,state,record,[json.loads(s) for s in (study.RUN/study.ARM/'training/metrics.jsonl').read_text().splitlines()],c)
    from jmicro.model import JMicroModel
    native=JMicroModel(state['model_config']);native.load_state_dict(state['model'],strict=True)
    if sum(p.numel() for p in native.parameters())!=10001152:raise ValueError('Native10M model required')
    base=read_json(Path(c['original_config']['path']));candidate=r['evaluation']
    summary,scores=content(study.ARM,candidate,record,base,study.RUN/f'evaluation/{study.ARM}/evaluation/generation.json',study.RUN/'content-notes.json')
    ref=c['references']['control_result'];old=read_json(Path(ref['path']));strong=old['evaluations']['source_order']
    strong_summary,strong_scores=content('historical_full_staged',strong,old['checkpoints']['source_order'],base,
        Path(ref['path']).parent/'evaluation/source_order/evaluation/generation.json',Path(c['references']['control_notes']['path']))
    if strong_summary['coherent']!=23 or strong_summary['rates']['eos']!=76 or strong_summary['rates']['repetition']!=2:raise ValueError('Original strong baseline changed')
    relative=quality_gates(strong,candidate,strong_scores,scores,'content');rates=summary['rates']
    absolute=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,appropriate_at_least27=summary['appropriate']>=27,
        EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
    web=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),candidate)
    masked=read_json(Path(c['references']['masked_staged_control']['path']))
    masked_summary,masked_scores=content('cached_masked_staged',masked['evaluation'],masked['checkpoint'],base,
        Path(c['references']['masked_staged_control']['path']).parent/'evaluation/outcome_EOS_only/evaluation/generation.json',Path(c['references']['masked_staged_notes']['path']))
    eligible=relative['passed'] and all(absolute.values()) and all(web.values())
    proposal=read_json(study.PROPOSAL);original_proposal=read_json(ROOT/'reports/phase6/finite_Web_constraint_proposal.json')
    clarification=dict(inherited_provenance_fields=['algorithm','required_before_science'],
        inherited_fields_equal_original=all(proposal[k]==original_proposal[k] for k in ('algorithm','required_before_science')),
        active_prelaunch_fields=['kind','block_updates','scope_difference','transaction','persistence','probe','measured_budget','no_rescue'],
        clarification='Inherited original per-update prose was left in raw block proposal. The explicit block fields, prelaunch configs/trainer/tests/CUDA evidence define this separate20-update recipe; raw proposal retained. No old per-update gate is claimed passed and quality selection is unchanged.',
        quality_selection_equal_original=proposal['selection']==original_proposal['selection'])
    if not clarification['inherited_fields_equal_original'] or not clarification['quality_selection_equal_original']:raise ValueError('Original provenance/quality changed')
    report=dict(status='qualified_block_recipe_pending_independent_learning_seed_full_dev_protected_test' if eligible else 'fixed20_block_Web_constraint_rejected',created_at=now(),
        result=study.reference(study.RUN/'compare-result.json'),config=study.reference(study.CONFIG),summary=summary,accounting=audit,
        relative_to_unchanged_strong=relative,absolute=absolute,historical_Web=web,eligible_for_final_Base_validation=eligible,
        cached_masked_staged_summary=masked_summary,observed_vs_cached_masked_staged=quality_gates(masked['evaluation'],candidate,masked_scores,scores,'content'),
        all80_individually_read=True,independent_human_blind=False,proposal_metadata_clarification=clarification,
        actual_science_GPU_seconds=r['GPU_seconds'],own_probe_GPU_seconds=c['verification_GPU_seconds'],previous_related_GPU_seconds=c['previous_related_GPU_seconds'],
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Only eligible recipe enters independent learned recipe seed/full dev/protected test/adoption. Failure ends this fixed cadence without cadence/memory/ceiling/projector/LR/source/mask/decoder/checkpoint rescue.')
    if (study.RUN/'review.json').exists():raise ValueError('Preserve original review')
    atomic_json(study.RUN/'review.json',report);atomic_json(ROOT/'reports/phase6/block_Web_constraint_review.json',report)
    print(json.dumps(dict(status=report['status'],summary=summary,eligible=eligible),ensure_ascii=False))


if __name__=='__main__':main()
