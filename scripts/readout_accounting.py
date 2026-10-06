"""Complete source/state accounting with an explicit fresh readout LR."""
import math
import torch
from phase6_performance import finite_state
from run_eos_short_pilot import equal_state
from readout_adapter_trainer import READOUT_LR
import run_readout_adapter_comparison as study

def accounting(parent,state,record,history,c,arm):
    sampler=state['sampler'];lineage=state['lineage'];spec=state['spec']
    if (not finite_state(state) or sampler['source_teachers']!=study.GOALS
            or sampler.get('source_order')!=list(study.prior.SOURCE_ORDER)
            or state['supervised_tokens']-parent['supervised_tokens']!=study.TOTAL
            or state['tokens']-parent['tokens']!=sum(sampler['source_tokens'].values())
            or state['body_bytes']-parent['body_bytes']!=sum(sampler['source_body_bytes'].values())
            or state['update']-parent['update']!=sampler['position'] or len(history)!=sampler['position']
            or [r['update'] for r in history]!=list(range(parent['update']+1,state['update']+1))
            or state['weighted_teacher_mass']!=study.TOTAL or state['focus_teacher_tokens']!=sum(sampler['source_focus_teachers'].values())
            or state['study_binding']!=study.binding(c,study.CONFIG,arm) or record['binding']!=state['study_binding']
            or record['additional_supervised_tokens']!=study.TOTAL or record['parameter_penalty_teacher_tokens']
            or spec['parameter_coefficient']!=c['coefficients'][arm] or spec['research_kind']!=study.KIND
            or spec['anchor_checkpoint']!=c['parent'] or lineage['parent']!=c['parent']
            or not lineage['no_reheat'] or not equal_state(lineage['actual_parent_sampler'],parent['sampler'])
            or not equal_state(lineage['parent_scheduler'],parent['scheduler'])
            or any(g['lr']!=READOUT_LR for g in state['optimizer']['param_groups'])):
        raise ValueError('Completed fullstate/teacher/source/anchor accounting differs')
    digest=__import__('hashlib').sha256()
    from jmicro.model import JMicroModel
    with torch.random.fork_rng(devices=[]):model=JMicroModel(parent['model_config'])
    for k,_ in model.named_parameters():
        digest.update(k.encode());digest.update(parent['model'][k].numpy().tobytes())
    if digest.hexdigest()!=lineage['anchor_initial_digest'] or record['anchor_initial_digest']!=digest.hexdigest():
        raise ValueError('Actual anchor does not bind original unique parent parameters')
    for row in history:
        if (any(not math.isfinite(row[k]) for k in ('loss','CE_loss','parameter_penalty','gradient_norm'))
                or row['parameter_coefficient']!=c['coefficients'][arm] or row['parameter_penalty_teacher_tokens']
                or row['parameter_penalty']<0 or row['lr']!=READOUT_LR
                or not math.isclose(row['loss'],row['CE_loss']+row['parameter_penalty'],rel_tol=1e-6,abs_tol=1e-6)):
            raise ValueError('Full actual objective history differs')
    for k in ('token_digest','focus_token_digest'):
        if history[-1][k]!=state[k] or record[k]!=state[k]:raise ValueError('Terminal raw input digest differs')
    if record['sampler']!=sampler:raise ValueError('Terminal sampler record differs')
    initial=parent['sampler']['streams']['web']['sampler'];final=sampler['streams']['web']['sampler']
    if any(initial[k]!=final[k] for k in ('seed','context','blocks')):raise ValueError('Actual Web recipe differs')
    blocks=(final['epoch']-initial['epoch'])*initial['blocks']+final['position']-initial['position']
    if blocks*initial['context']!=sampler['source_tokens']['web']:raise ValueError('Actual Web cursor exposure differs')
    return dict(completed_updates=len(history),teachers=study.TOTAL,physical_input_positions=record['additional_input_tokens'],
        parameter_penalty_teacher_tokens=0,final_parameter_penalty=history[-1]['parameter_penalty'],
        actual_Web_blocks_consumed=blocks,source_teachers=sampler['source_teachers'],source_EOS=sampler['source_eos'])

