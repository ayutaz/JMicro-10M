"""Reject misleading completion, missing RNG/moments and replayed log evidence.

Synthetic metadata fixtures below are CPU protocol evidence, never GPU learning
or a qualification of model quality. Actual CUDA evidence lives in the probe.
"""
import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
from base_label_smoothing_packed import PackedLabelSmoothingTrainer
from jmicro.model import JMicroModel
from review_base_label_smoothing import audit_checkpoint, audit_terminal, committed_history, HISTORY_KEYS
from run_base_label_smoothing import matched_control_checks

torch.set_num_threads(2)


@pytest.fixture(scope='module')
def checkpoint_fixture():
    config = json.loads((Path(__file__).resolve().parents[1] / 'configs/models/t4k.json').read_text())
    config.update(qk_norm_type='none', expected_parameter_count=10001152)
    model = JMicroModel(config)
    parent = dict(model_config=config, model=model.state_dict(), update=5, tokens=90, supervised_tokens=80)
    c = dict(parent={'path': 'CPU-protocol-parent', 'sha256': 'a' * 64},
             source_binding={'manifest_sha256': 'b' * 64}, source_sha256={},
             goals={'web': 12, 'textbook': 3, 'story': 1}, CE_tokens_per_arm=16,
             batch=48, seed=42, GPU_budget_seconds=100)
    binding = dict(parent=c['parent'], source_binding=c['source_binding'],
                   config_sha256='fixed', weights_role='scientific_smoothing', sources={})
    sampler = SimpleNamespace(goals=c['goals'])
    sampler.state_dict = lambda: dict(binding=c['source_binding'], consumed=c['goals'],
        goals=c['goals'], seed=42, draws=6, windows_emitted=4, pending={}, RNG=('fixture-source',))
    trainer = PackedLabelSmoothingTrainer(parent, sampler, binding, batch=48, device='cpu')
    trainer.counters.update(update=3, supervised_tokens=16, source_teachers=c['goals'],
        source_EOS={'web': 1, 'textbook': 1, 'story': 1}, CE_input_tokens=20,
        physical_input_tokens=64, original_body_bytes=25,
        weighted_original_target_mass=14.4, uniform_target_mass=1.6,uniform_soft_target_positions=16)
    state = trainer.state_dict()
    state['spec'].update(dtype='bf16', backend='flash')  # Synthetic, not a CUDA claim.
    state['scheduler']['last_epoch'] = 3
    state['RNG']['cuda'] = [torch.tensor([1], dtype=torch.uint8)]
    ids = state['optimizer']['param_groups'][0]['params']
    for key, param in zip(ids, trainer.model.parameters(), strict=True):
        state['optimizer']['state'][key] = dict(step=torch.tensor(3.),
            exp_avg=torch.zeros(1).expand_as(param), exp_avg_sq=torch.zeros(1).expand_as(param))
    record = dict(status='complete', binding=binding, counters=copy.deepcopy(state['counters']),
                  sampler=state['sampler'], scientific_CE_teacher_tokens=16, parent_CE_teacher_tokens=80)
    return c, state, record, dict(committed_updates=3, optimizer_updates=3)


def test_native_only_moments_steps_probability_and_source_accounting(checkpoint_fixture):
    c, state, record, history = checkpoint_fixture
    account = audit_checkpoint(state, record, c, 'fixed', history)
    assert account['completed_updates'] == account['optimizer_updates'] == 3
    assert account['native_parameters'] == account['training_parameters'] == 10001152
    assert account['train_only_parameters'] == account['auxiliary_input_tokens'] == 0
    assert account['label_smoothing_epsilon'] == 0.1
    assert account['native_inference_changed'] is False
    assert account['additional_unique_supply_claimed'] is False


@pytest.mark.parametrize('change', ('epsilon', 'support', 'inference_dropout', 'soft_mass', 'contrast',
                                  'quota', 'Adam_step', 'missing_moment', 'CUDA_RNG',
                                  'extra_head', 'nonfinite_weight'))
def test_reject_reinterpreted_or_incomplete_native_state(checkpoint_fixture, change):
    c, original, record, history = checkpoint_fixture
    state = {**original, 'spec': copy.deepcopy(original['spec']),
             'model_config': copy.deepcopy(original['model_config']),
             'model': original['model'].copy(), 'sampler': copy.deepcopy(original['sampler']),
             'optimizer': copy.copy(original['optimizer']), 'RNG': original['RNG'].copy()}
    if change == 'epsilon':
        state['spec']['label_smoothing'] = 0.2
    elif change == 'support':
        state['spec']['uniform_support'] = 'filtered_subset'
    elif change == 'soft_mass':
        state['counters'] = {**state['counters'], 'uniform_target_mass': 2.0}
    elif change == 'inference_dropout':
        state['model_config']['dropout'] = 0.1
    elif change == 'contrast':
        state['spec']['contrast'] = True
    elif change == 'quota':
        state['sampler']['consumed'] = {'web': 11, 'textbook': 4, 'story': 1}
    elif change in ('Adam_step', 'missing_moment'):
        state['optimizer']['state'] = original['optimizer']['state'].copy()
        key = original['optimizer']['param_groups'][0]['params'][-1]
        if change == 'Adam_step':
            state['optimizer']['state'][key] = {**state['optimizer']['state'][key], 'step': torch.tensor(2.)}
        else:
            del state['optimizer']['state'][key]
    elif change == 'CUDA_RNG':
        state['RNG']['cuda'] = []
    elif change == 'extra_head':
        state['projector'] = {'weight': torch.ones(1)}
    else:
        key = 'model.norm.weight'
        state['model'][key] = torch.full_like(state['model'][key], float('nan'))
    with pytest.raises(ValueError):
        audit_checkpoint(state, record, c, 'fixed', history)


def terminal_fixture():
    c = dict(CE_tokens_per_arm=16, GPU_budget_seconds=100)
    trained = dict(counters=dict(update=3, token_digest='same', supervised_tokens=16,
        source_teachers={}, source_EOS={}, CE_input_tokens=20, original_body_bytes=25,
        auxiliary_input_tokens=0, auxiliary_pairs=0, physical_input_tokens=64), sampler={})
    job = dict(status='complete', config_sha256='fixed', GPU_occupancy_seconds=50,
               pid=1, boot_id='boot', start_ticks='2')
    result = dict(status='complete', config_sha256='fixed', GPU_occupancy_seconds=50,
        actual_identity={k: job[k] for k in ('pid', 'boot_id', 'start_ticks')},
        scientific_CE_teacher_tokens=16, reused_control_CE_teachers=100000000,
        reused_control_GPU_seconds=0, results={'smoothing': {'training': trained}},
        common_CE_checks={'CE': matched_control_checks(trained, trained)},
        Base_complete=False, Chat_started=False, quantization_started=False)
    return c, job, result


def test_terminal_requires_real_exit_same_job_budget_and_Base_only():
    c, job, result = terminal_fixture()
    audit_terminal(job, result, c, 'fixed', False)
    with pytest.raises(ValueError, match='exit'):
        audit_terminal(job, result, c, 'fixed', True)
    for changes in ({'GPU_occupancy_seconds': 101}, {'reused_control_GPU_seconds': 1},
                    {'reused_control_CE_teachers': 200000000}, {'Base_complete': True},
                    {'Chat_started': True}, {'quantization_started': True},
                    {'actual_identity': {'pid': 1, 'boot_id': 'other', 'start_ticks': '2'}}):
        with pytest.raises(ValueError, match='terminal'):
            audit_terminal(job, {**result, **changes}, c, 'fixed', False)
    changed = copy.deepcopy(result)
    changed['common_CE_checks']['CE']['physical_input_tokens'] = 1
    with pytest.raises(ValueError, match='terminal'):
        audit_terminal(job, changed, c, 'fixed', False)


def log_rows():
    return [dict(update=i, supervised_tokens=8 * i, source_teachers={'web': 8 * i},
        source_EOS={'web': i}, CE_input_tokens=10 * i, auxiliary_input_tokens=0,
        auxiliary_pairs=0, physical_input_tokens=16 * i, original_body_bytes=13 * i,
        token_digest=str(i) * 64, auxiliary_digest='0' * 64, CE_loss=2., contrast_loss=0.,
        combined_loss=2.6, uniform_smoothing_loss=8., label_smoothing_epsilon=.1,
        weighted_original_target_mass=.9*8*i,uniform_target_mass=.1*8*i,uniform_soft_target_positions=8*i,
        weighted_original_mass_this_update=.9*8,uniform_mass_this_update=.1*8,uniform_positions_this_update=8,auxiliary_gradient_norm=0., gradient_norm=2., seconds=.1,
        data_wait_seconds=.01, lr=1e-5, CE_targets_this_update=8,
        auxiliary_pairs_this_update=0, auxiliary_inputs_this_update=0,
        physical_inputs_this_update=16) for i in range(1, 4)]


def write_log(path, rows):
    path.write_text(''.join(json.dumps(row) + '\n' for row in rows))


def test_committed_history_retains_resumed_path_and_torn_uncommitted_raw(tmp_path):
    rows = log_rows()
    terminal = {k: rows[-1][k] for k in HISTORY_KEYS}
    old, later = tmp_path / 'metrics-999-10.jsonl', tmp_path / 'metrics-3-20.jsonl'
    write_log(old, rows[:2])
    old.write_text(old.read_text() + '{"update":3,')
    write_log(later, rows[1:])
    audit = committed_history([later, old], terminal)
    assert audit['committed_updates'] == audit['optimizer_updates'] == 3
    assert audit['observed_completed_attempt_updates'] == 4
    assert audit['rolled_back_or_replayed_log_rows'] == 1
    assert audit['uncommitted_torn_tails'] == [dict(path=str(old), uncommitted_tail_bytes=12)]
    assert old.read_text().endswith('{"update":3,')
    with pytest.raises(ValueError, match='Complete committed'):
        committed_history([old], terminal)


@pytest.mark.parametrize('change', ('missing_update', 'wrong_counter', 'auxiliary_loss', 'nonfinite', 'terminated_torn', 'soft_mass', 'epsilon', 'mixed_loss'))
def test_history_rejects_missing_nonfinite_or_extra_objective_updates(tmp_path, change):
    rows = log_rows()
    terminal = {k: rows[-1][k] for k in HISTORY_KEYS}
    if change == 'missing_update':
        del rows[1]
    elif change == 'wrong_counter':
        rows[1]['supervised_tokens'] += 1
    elif change == 'auxiliary_loss':
        rows[1]['contrast_loss'] = .1
    elif change == 'soft_mass':
        rows[1]['uniform_target_mass'] += 1
    elif change == 'epsilon':
        rows[1]['label_smoothing_epsilon'] = .2
    elif change == 'mixed_loss':
        rows[1]['combined_loss'] = rows[1]['CE_loss']
    elif change == 'nonfinite':
        rows[1]['combined_loss'] = float('nan')
    path = tmp_path / 'metrics-1-10.jsonl'
    write_log(path, rows)
    if change == 'terminated_torn':
        with path.open('a') as stream:
            stream.write('{"update":4,\n')
    with pytest.raises(ValueError):
        committed_history([path], terminal)
