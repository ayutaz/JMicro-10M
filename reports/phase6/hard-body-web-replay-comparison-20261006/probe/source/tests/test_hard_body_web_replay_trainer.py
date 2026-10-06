import copy
import sys
import pytest
import torch
from jmicro.experiment import ROOT
from jmicro.training import rng_state
sys.path.insert(0, str(ROOT/'scripts'))
from hard_body_web_replay_trainer import HardBodyReplayTrainer
from eos_decoupled_web_kl_condition_trainer import WebKLTrainer as SoftTrainer
from test_original_web_retention_trainer import setup
from run_eos_short_pilot import equal_state


def test_full_CPU_resume_measured_hard_targets_mass_and_identical_soft_control_inputs(tmp_path):
    pool, parent, binding, positive = setup(tmp_path)
    cursor = copy.deepcopy(parent['sampler'])
    parent = copy.deepcopy(parent)
    parent.update(update=320435, tokens=10500014080, supervised_tokens=10477786961,
        sampler=dict(kind='eos-pilot-mixture-v1', position=0, routes=[], web=cursor, short=dict(position=0),
            source_tokens=dict(web=0, short=0), source_eos=dict(web=0, short=0)))
    for group in parent['optimizer']['param_groups']:
        group['lr'] = .00001
        group['initial_lr'] = .0001
    parent['scheduler']['base_lrs'] = [.0001]*len(parent['optimizer']['param_groups'])
    parent['scheduler']['_last_lr'] = [.00001]*len(parent['optimizer']['param_groups'])
    parent['scheduler']['last_epoch'] = 320435
    goals = dict(web=83, story=31, ordinary_textbook=29, conditional_textbook=37)
    def build(cls=HardBodyReplayTrainer):
        return cls(parent, pool, pool, positive, goals, binding, 'cpu', 8, 3, 2)
    continuous = build()
    assert equal_state(continuous.model.state_dict(), parent['model'])
    assert equal_state(continuous.optimizer.state_dict(), parent['optimizer'])
    assert equal_state(rng_state(), parent['rng'])
    left_rows = [continuous.step() for _ in range(4)]
    continuous.save(tmp_path/'continuous.pt')
    split = build()
    right_rows = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = build()
    resumed.load(tmp_path/'split.pt')
    right_rows.extend(resumed.step() for _ in range(2))
    resumed.save(tmp_path/'resumed.pt')
    left = torch.load(tmp_path/'continuous.pt', map_location='cpu', weights_only=False)
    right = torch.load(tmp_path/'resumed.pt', map_location='cpu', weights_only=False)
    assert equal_state(left, right)  # Includes Adam, scheduler, RNG, both samplers and new ledgers.
    for a, b in zip(left_rows, right_rows, strict=True):
        for key in ('loss', 'ordinary_CE_loss', 'reference_body_CE_loss', 'gradient_norm', 'lr',
                'token_digest', 'reference_digest', 'source_teachers', 'source_eos', 'source_body_bytes',
                'reference_hard_body_target_positions', 'reference_non_EOS_teacher_probability_mass',
                'combined_hard_teacher_positions'):
            assert a[key] == b[key], key
    assert resumed.replay.physical_input_tokens == 64
    assert resumed.tokens-parent['tokens'] == 96
    assert all(row['reference_body_CE_loss'] > 0 for row in left_rows)
    assert 0 < resumed.reference_non_EOS_teacher_mass < resumed.reference_hard_body_teacher_tokens
    assert resumed.reference_hard_body_teacher_tokens == resumed.replay.body_positions
    extra = left['hard_replay_state']
    assert extra['hard_body_teacher_tokens'] == left_rows[-1]['reference_hard_body_target_positions']
    assert extra['non_EOS_teacher_probability_mass'] == left_rows[-1]['reference_non_EOS_teacher_probability_mass']
    assert left_rows[-1]['combined_hard_teacher_positions'] == resumed.supervised_tokens-parent['supervised_tokens']+extra['hard_body_teacher_tokens']
    resumed.verify_teacher()
    soft = build(SoftTrainer)
    soft_rows = [soft.step() for _ in range(4)]
    for a, b in zip(left_rows, soft_rows, strict=True):
        for key in ('token_digest', 'reference_digest', 'source_teachers', 'source_eos', 'source_input_tokens',
                'source_body_bytes', 'source_focus_teachers', 'reference_input_tokens', 'reference_ignored_positions',
                'reference_non_EOS_teacher_probability_mass', 'combined_student_physical_input_tokens'):
            assert a[key] == b[key], key
        assert a['reference_hard_body_target_positions'] == b['reference_soft_target_body_positions']
    bad = copy.deepcopy(left)
    bad['hard_replay_state']['hard_body_teacher_tokens'] -= 1
    torch.save(bad, tmp_path/'bad-count.pt')
    with pytest.raises(ValueError, match='hard targets'):
        build().load(tmp_path/'bad-count.pt')
    soft.save(tmp_path/'soft.pt')
    with pytest.raises(KeyError):
        build().load(tmp_path/'soft.pt')
