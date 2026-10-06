"""Native full-state clocks and separate positive/auxiliary continuation exposure."""
import math
from run_eos_short_pilot import equal_state
from base_preference_trainer import Web_cursor, PairQuotaSampler


def accounting(parent, state, record, history, goal, binding, pairs=None, byte_lengths=None):
    s, lineage, spec = state['sampler'], state['lineage'], state['spec']
    n = len(history)
    common = spec['phase'] == 'common_Web'
    teachers = s['source_teachers']['web'] if common else s['teachers']
    physical = s['source_tokens']['web'] if common else s['physical']
    body_bytes = s['source_body_bytes']['web'] if common else s['body_bytes']
    if (teachers != goal or state['supervised_tokens'] - parent['supervised_tokens'] != goal
            or state['tokens'] - parent['tokens'] != physical or state['body_bytes'] - parent['body_bytes'] != body_bytes
            or state['update'] - parent['update'] != n or s['position'] != n or n == 0
            or state['weighted_teacher_mass'] != goal or state['focus_teacher_tokens'] != 0
            or state['study_binding'] != binding or record['binding'] != binding or record['sampler'] != s
            or record['additional_supervised_tokens'] != goal or record['additional_input_tokens'] != physical
            or lineage['parent'] != binding['parent'] or not lineage['no_reheat'] or lineage['optimizer_policy'] != 'inherit'
            or not equal_state(lineage['actual_parent_sampler'], parent['sampler'])
            or not equal_state(lineage['parent_scheduler'], parent['scheduler'])
            or state['model_config'] != parent['model_config']):
        raise ValueError('Completed native positive/common state accounting differs')
    groups, old = state['optimizer']['param_groups'], parent['optimizer']['param_groups']
    if len(groups) != len(old): raise ValueError('Inherited native Adam groups differ')
    for group, original in zip(groups, old, strict=True):
        if group != original or group['lr'] != .00001: raise ValueError('Native Adam settings reheated or changed')
        for key in group['params']:
            current, previous = state['optimizer']['state'][key], parent['optimizer']['state'][key]
            if (int(current['step']) != int(previous['step']) + n
                    or current['exp_avg'].shape != previous['exp_avg'].shape or current['exp_avg_sq'].shape != previous['exp_avg_sq'].shape):
                raise ValueError('Native Adam moment/update clock differs')
    if (state['scheduler']['last_epoch'] != parent['scheduler']['last_epoch'] + n
            or state['scheduler']['_step_count'] != parent['scheduler']['_step_count'] + n
            or state['scheduler']['base_lrs'] != parent['scheduler']['base_lrs']):
        raise ValueError('Inherited native scheduler clock differs')
    previous_teachers = 0
    replay = None if common else PairQuotaSampler(pairs, goal, spec['batch'], byte_lengths, spec['reference_digest'])
    for i, row in enumerate(history, 1):
        t = row['additional_teacher_tokens']
        if (row['update'] != parent['update'] + i or row['lr'] != .00001
                or not previous_teachers < t <= goal or row['weighted_teacher_mass'] != t
                or row['supervised_tokens'] != parent['supervised_tokens'] + t
                or row['tokens_seen'] != parent['tokens'] + row['physical_input_tokens']
                or row['physical_input_tokens'] != i * spec['batch'] * spec['context'] * (1 if common else 2)
                or any(not math.isfinite(row[k]) for k in ('loss', 'gradient_norm', 'seconds')) or row['seconds'] <= 0):
            raise ValueError('Actual finite ordered positive history differs')
        if common:
            if (row['source_teachers'] != dict(web=t) or row['source_focus_teachers'] != dict(web=0)
                    or row['source_eos']['web'] > t or row['valid_input_tokens'] != row['physical_input_tokens']
                    or row['body_bytes_seen'] != parent['body_bytes'] + row['source_body_bytes']['web']):
                raise ValueError('Common Web exposure differs')
        else:
            group, *_ = replay.batch()
            expected = dict(group=group, additional_teacher_tokens=replay.teachers, CE_EOS=replay.EOS,
                physical_input_tokens=replay.physical, valid_input_tokens=replay.valid,
                scored_chosen_positions=replay.scored_chosen, scored_rejected_positions=replay.scored_rejected,
                active_pair_exposures=replay.active_pair_exposures, auxiliary_digest=replay.auxiliary_digest,
                body_bytes_seen=parent['body_bytes'] + replay.body_bytes,
                optimizer_pair_exposures=replay.active_pair_exposures if spec['coefficient'] else 0)
            if (any(row[k] != v for k, v in expected.items()) or row['DPO_coefficient'] != spec['coefficient']
                    or row['beta'] != .1 or not math.isclose(row['loss'], row['CE_loss'] + spec['coefficient'] * row['DPO_loss'], rel_tol=2e-6, abs_tol=2e-6)
                    or any(not math.isfinite(row[k]) for k in ('CE_loss', 'DPO_loss', 'mean_reference_ratio_margin'))):
                raise ValueError('Actual completion mask/negative/reference/quota accounting differs')
        previous_teachers = t
    if common:
        start, end = Web_cursor(parent), s['streams']['web']['sampler']
        if any(start[k] != end[k] for k in ('seed', 'context', 'blocks')): raise ValueError('Original Web shuffle recipe differs')
        blocks = (end['epoch'] - start['epoch']) * start['blocks'] + end['position'] - start['position']
        if blocks * spec['context'] != physical: raise ValueError('Original Web cursor exposure differs')
    elif replay.state_dict() != s:
        raise ValueError('Terminal full pair replay differs')
    for k in ('token_digest', 'focus_token_digest'):
        if history[-1][k] != state[k] or record[k] != state[k]: raise ValueError('Terminal input digest differs')
    return dict(completed_updates=n, positive_teacher_tokens=goal, physical_input_positions=physical,
        CE_body_bytes=body_bytes, sampler=s, native_Adam_and_scheduler_inherited=True)


def matched_exposure(a, b):
    fields = ('update', 'tokens_seen', 'supervised_tokens', 'body_bytes_seen', 'token_digest', 'focus_token_digest',
        'additional_teacher_tokens', 'physical_input_tokens', 'valid_input_tokens', 'CE_EOS',
        'scored_chosen_positions', 'scored_rejected_positions', 'active_pair_exposures', 'auxiliary_digest', 'group', 'lr')
    if len(a) != len(b) or any(x[k] != y[k] for x, y in zip(a, b, strict=True) for k in fields):
        raise ValueError('Both objectives must use identical input/positive/auxiliary streams')
    return dict(matched_updates=len(a), exact_same_CE_input_and_auxiliary_exposure=True)
