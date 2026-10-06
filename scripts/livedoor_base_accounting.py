"""Completed native inherited state and fresh news exposure accounting."""
import math
from run_eos_short_pilot import equal_state


def accounting(parent, state, record, history, goals, binding):
    total=sum(goals.values()); sampler=state['sampler']; lineage=state['lineage']; spec=state['spec']
    if (sampler['source_teachers'] != goals or sampler['source_order'] != ['web', 'authored_news']
            or state['supervised_tokens']-parent['supervised_tokens'] != total
            or state['tokens']-parent['tokens'] != sum(sampler['source_tokens'].values())
            or state['body_bytes']-parent['body_bytes'] != sum(sampler['source_body_bytes'].values())
            or state['update']-parent['update'] != sampler['position'] or len(history) != sampler['position']
            or [r['update'] for r in history] != list(range(parent['update']+1, state['update']+1))
            or state['weighted_teacher_mass'] != total or state['focus_teacher_tokens'] != 0
            or any(sampler['source_focus_teachers'].values()) or state['study_binding'] != binding or record['binding'] != binding
            or record['additional_supervised_tokens'] != total or record['sampler'] != sampler
            or lineage['parent'] != binding['parent'] or lineage['original_parent'] != binding.get('original_parent')
            or not lineage['no_reheat'] or lineage['optimizer_policy'] != 'inherit'
            or not equal_state(lineage['actual_parent_sampler'], parent['sampler'])
            or not equal_state(lineage['parent_scheduler'], parent['scheduler'])
            or state['model_config'] != parent['model_config'] or spec['teacher_goals'] != goals or spec['outcome_weight'] != 1):
        raise ValueError('Native inherited source/teacher/update/lineage accounting differs')
    groups=state['optimizer']['param_groups']; old=parent['optimizer']['param_groups']
    if len(groups) != len(old): raise ValueError('Inherited native Adam groups differ')
    for group, original in zip(groups, old, strict=True):
        if group != original or group['lr'] != .00001: raise ValueError('Native Adam settings reheated or changed')
        for key in group['params']:
            moment=state['optimizer']['state'][key]; previous=parent['optimizer']['state'][key]
            if (int(moment['step']) != int(previous['step'])+len(history)
                    or moment['exp_avg'].shape != previous['exp_avg'].shape or moment['exp_avg_sq'].shape != previous['exp_avg_sq'].shape):
                raise ValueError('Inherited native Adam update clock differs')
    if (state['scheduler']['last_epoch'] != parent['scheduler']['last_epoch']+len(history)
            or state['scheduler']['_step_count'] != parent['scheduler']['_step_count']+len(history)
            or state['scheduler']['base_lrs'] != parent['scheduler']['base_lrs']):
        raise ValueError('Inherited scheduler clock differs')
    previous=dict.fromkeys(goals, 0)
    for row in history:
        teachers=row['source_teachers']; physical=row['source_input_tokens']; bytes_=row['source_body_bytes']
        if (row['lr'] != .00001 or row['outcome_weight'] != 1 or row['focus_teacher_tokens'] != 0
                or any(not math.isfinite(row[k]) for k in ('loss', 'gradient_norm', 'seconds')) or row['seconds'] <= 0
                or any(teachers[g] < previous[g] or teachers[g] > goals[g] for g in goals)
                or teachers['authored_news'] and teachers['web'] != goals['web']
                or row['additional_teacher_tokens'] != sum(teachers.values()) or row['weighted_teacher_mass'] != sum(teachers.values())
                or row['supervised_tokens'] != parent['supervised_tokens']+sum(teachers.values())
                or row['tokens_seen'] != parent['tokens']+sum(physical.values())
                or row['body_bytes_seen'] != parent['body_bytes']+sum(bytes_.values())
                or sum(physical.values()) != (row['update']-parent['update'])*spec['batch']*spec['context']
                or any(row['source_eos'][g] > teachers[g] for g in goals)):
            raise ValueError('Actual full native loss/exposure history differs')
        previous=teachers
    for key in ('token_digest', 'focus_token_digest'):
        if history[-1][key] != state[key] or record[key] != state[key]: raise ValueError('Terminal input digest differs')
    blocks={}
    for source in goals:
        final=sampler['streams'][source]['sampler']
        initial=parent['sampler']['streams']['web']['sampler'] if source == 'web' else dict(seed=42, context=spec['context'], blocks=final['blocks'], epoch=0, position=0)
        if any(initial[k] != final[k] for k in ('seed', 'context', 'blocks')): raise ValueError('Source shuffle recipe differs')
        blocks[source]=(final['epoch']-initial['epoch'])*initial['blocks']+final['position']-initial['position']
        if blocks[source]*spec['context'] != sampler['source_tokens'][source]: raise ValueError('Actual source cursor exposure differs')
    return dict(completed_updates=len(history), new_teacher_tokens=total, physical_input_positions=state['tokens']-parent['tokens'],
        source_teachers=sampler['source_teachers'], source_EOS=sampler['source_eos'], actual_blocks_consumed=blocks,
        news_epoch= sampler['streams']['authored_news']['sampler']['epoch'], native_Adam_and_scheduler_inherited=True)
