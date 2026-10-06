"""Prevent unfinished jobs and mismatched completed checkpoints qualifying Base."""
import copy
import json
import sys
from pathlib import Path

import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from review_natural_context_contrast import COMMON, KIND, audit_checkpoint, audit_terminal


def fixture(arm='CE'):
    c = dict(parent={'path': 'parent.pt', 'sha256': 'a' * 64}, source_binding={'manifest_sha256': 'b' * 64},
        source_sha256={}, goals={'web': 12, 'textbook': 3, 'story': 1}, CE_tokens_per_arm=16,
        batch=48, seed=42, temperature=.1, coefficient=.1, GPU_budget_seconds=100)
    binding = dict(parent=c['parent'], source_binding=c['source_binding'], config_sha256='frozen',
                   weights_role='scientific_' + arm, sources={})
    state = dict(kind=KIND, binding=binding,
        spec=dict(kind=KIND, batch=48, seed=42, contrast=arm == 'contrast', temperature=.1, coefficient=.1,
                  lr=1e-5, weight_decay=.1, scheduler='constant', optimizer_policy='fresh_equal_AdamW_both_arms',
                  dtype='bf16', backend='flash'),
        lineage=dict(parent=c['parent'], parent_supervised_tokens=100, weights_role='scientific_' + arm),
        counters=dict(update=2, supervised_tokens=16, source_teachers=c['goals'], source_EOS={'web': 1, 'textbook': 1, 'story': 1},
                      auxiliary_pairs=4 if arm == 'contrast' else 0, auxiliary_input_tokens=20 if arm == 'contrast' else 0,
                      CE_input_tokens=20, physical_input_tokens=64, original_body_bytes=25, token_digest='c' * 64),
        sampler=dict(binding=c['source_binding'], consumed=c['goals'], goals=c['goals'], seed=42,
                     draws=6, windows_emitted=4, pending={}, RNG=('source',)),
        model={'weight': torch.tensor([1.0])},
        optimizer={'param_groups': [{'lr': 1e-5, 'weight_decay': .1}], 'state': {0: {'step': torch.tensor(2.)}}},
        scheduler={'last_epoch': 2}, RNG={'torch': torch.tensor([1], dtype=torch.uint8)})
    record = dict(status='complete', binding=binding, counters=copy.deepcopy(state['counters']),
        sampler=copy.deepcopy(state['sampler']), scientific_CE_teacher_tokens=16, parent_CE_teacher_tokens=100)
    # Terminal JSON converts sampler RNG tuples to lists; the .pt state does not.
    return c, state, json.loads(json.dumps(record))


def test_each_arm_completed_update_and_extra_exposure():
    for arm in ('CE', 'contrast'):
        c, state, record = fixture(arm)
        account = audit_checkpoint(state, record, c, arm, 'frozen')
        assert account['CE_teacher_tokens'] == 16
        assert account['auxiliary_pairs'] == (4 if arm == 'contrast' else 0)
        assert account['additional_unique_supply_claimed'] is False


@pytest.mark.parametrize('corrupt', ('quota', 'adam_step', 'rng_missing', 'CE_auxiliary', 'nonfinite', 'recipe'))
def test_checkpoint_requires_actual_source_optimizer_and_recipe(corrupt):
    c, state, record = fixture()
    if corrupt == 'quota':
        state['sampler']['consumed'] = {'web': 11, 'textbook': 4, 'story': 1}
        record['sampler'] = copy.deepcopy(state['sampler'])
    elif corrupt == 'adam_step':
        state['optimizer']['state'][0]['step'] = torch.tensor(1.)
    elif corrupt == 'rng_missing':
        del state['RNG']
    elif corrupt == 'CE_auxiliary':
        state['counters']['auxiliary_input_tokens'] = 1
        record['counters'] = copy.deepcopy(state['counters'])
    elif corrupt == 'nonfinite':
        state['model']['weight'][0] = float('nan')
    else:
        state['spec']['coefficient'] = .01
    with pytest.raises(ValueError, match='full-state accounting'):
        audit_checkpoint(state, record, c, 'CE', 'frozen')


def test_terminal_file_alone_cannot_prove_exit_or_base_completion():
    c, _, _ = fixture()
    job = dict(status='complete', config_sha256='frozen', GPU_occupancy_seconds=50,
               pid=123, boot_id='boot', start_ticks='456')
    result = dict(status='complete', config_sha256='frozen', GPU_occupancy_seconds=50,
        actual_identity={k: job[k] for k in ('pid', 'boot_id', 'start_ticks')}, scientific_CE_teacher_tokens=32,
        results={'CE': {}, 'contrast': {}}, common_CE_checks=dict.fromkeys(COMMON, True),
        Base_complete=False, Chat_started=False, quantization_started=False)
    audit_terminal(job, result, c, 'frozen', False)
    with pytest.raises(ValueError, match='exited'):
        audit_terminal(job, result, c, 'frozen', True)
    for change in ({'actual_identity': {'pid': 123, 'boot_id': 'other', 'start_ticks': '456'}},
                   {'scientific_CE_teacher_tokens': 31}, {'GPU_occupancy_seconds': 101},
                   {'Base_complete': True}, {'common_CE_checks': dict.fromkeys(COMMON, 1)}):
        with pytest.raises(ValueError, match='bounded Base-only'):
            audit_terminal(job, {**result, **change}, c, 'frozen', False)
