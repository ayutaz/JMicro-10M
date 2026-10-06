"""Validate separate reference positions/cursor without rescanning train arrays."""
import hashlib
from jmicro.experiment import ROOT,sha256
from eos_decoupled_web_kl_preservation import POLICY
from historical_parent_condition_trainer import historical_web_cursor
from run_eos_short_pilot import equal_state


def weight_digest(state):
    digest=hashlib.sha256()
    for key,value in state.items():
        digest.update(key.encode());digest.update(value.detach().cpu().contiguous().numpy().tobytes())
    return digest.hexdigest()


def audit_reference(parent,state,record,history,config):
    extra=state['KL_state']; replay=extra['replay'];policy=config['KL_policy']
    if (policy!=POLICY or extra['policy']!=policy or state['spec']['KL_policy']!=policy
            or extra['reference_teacher']!=config['parent'] or state['lineage']['reference_teacher']!=config['parent']
            or extra['source_sha256']!=state['spec']['KL_sources']
            or any(v!=config['source_sha256'][k] or sha256(ROOT/k)!=v for k,v in extra['source_sha256'].items())
            or extra['teacher_weight_digest']!=weight_digest(parent['model'])
            or extra['teacher_weight_digest']!=state['lineage']['reference_teacher_weight_digest']
            or extra['teacher_weight_digest']!=record['reference_teacher_weight_digest']
            or record['KL_policy']!=policy or record['reference_replay']!=replay):
        raise ValueError('Frozen teacher/policy/source/replay identity differs')
    updates=state['update']-parent['update'];width=policy['reference_context'];batch=policy['reference_batch']
    initial=historical_web_cursor(parent);stream=replay['stream'];final=stream['sampler']
    if (updates!=len(history) or replay['updates']!=updates or replay['kind']!=POLICY['kind']
            or replay['context']!=width or replay['batch']!=batch or replay['initial_cursor']!=initial
            or stream['kind']!='actual-parent-Web-block-cursor-v1' or stream['manifest_sha256']!=parent['shard_manifest_sha256']
            or any(initial[k]!=final[k] for k in ('seed','context','blocks'))
            or (final['epoch']-initial['epoch'])*initial['blocks']+final['position']-initial['position']!=updates*batch
            or replay['physical_input_tokens']!=updates*width*batch
            or replay['body_positions']+replay['ignored_positions']!=replay['physical_input_tokens']):
        raise ValueError('Actual train Web reference cursor/counters differ')
    previous_positions=0
    for index,row in enumerate(history,1):
        if (row['reference_input_tokens']!=index*width*batch
                or not 0<row['reference_soft_target_body_positions']-previous_positions<=width*batch
                or row['reference_ignored_positions']+row['reference_soft_target_body_positions']!=row['reference_input_tokens']
                or row['combined_student_physical_input_tokens']!=row['physical_input_tokens']+row['reference_input_tokens']
                or len(bytes.fromhex(row['reference_digest']))!=32):
            raise ValueError('Completed update auxiliary ledger differs')
        previous_positions=row['reference_soft_target_body_positions']
    if (not history or previous_positions!=replay['body_positions'] or history[-1]['reference_digest']!=replay['digest']
            or record['reference_input_tokens']!=replay['physical_input_tokens']
            or record['reference_soft_target_body_positions']!=replay['body_positions']
            or record['combined_student_physical_input_tokens']!=record['additional_input_tokens']+replay['physical_input_tokens']):
        raise ValueError('Terminal full auxiliary ledger differs')
    mass=extra['non_EOS_teacher_probability_mass']
    if not 0<mass<=replay['body_positions'] or mass!=record['reference_non_EOS_teacher_probability_mass'] or mass!=history[-1]['reference_non_EOS_teacher_probability_mass']:
        raise ValueError('Terminal retained probability-mass ledger differs')
    previous_mass=0.;previous_positions=0
    for row in history:
        increment=row['reference_non_EOS_teacher_probability_mass']-previous_mass
        positions=row['reference_soft_target_body_positions']-previous_positions
        if not 0<increment<=positions+1e-3:raise ValueError('Retained per-update target probability mass differs')
        previous_mass=row['reference_non_EOS_teacher_probability_mass'];previous_positions=row['reference_soft_target_body_positions']
    return dict(reference_non_EOS_teacher_probability_mass=mass,frozen_parent_teacher_digest_verified=True,reference_cursor_blocks=updates*batch,
        reference_input_tokens=replay['physical_input_tokens'],reference_soft_target_body_positions=replay['body_positions'],
        ignored_special_positions=replay['ignored_positions'],main_ordinary_CE_teacher_tokens=record['additional_supervised_tokens'],
        combined_student_physical_input_tokens=record['combined_student_physical_input_tokens'],
        newly_prepared_source_tokens=0,replay_overlaps_primary_Web=True,
        labels='Main CE teachers and auxiliary distribution targets are separate; not equal total supervision with cached control.')
