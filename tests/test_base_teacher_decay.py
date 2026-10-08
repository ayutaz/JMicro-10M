"""Actual one-step AdamW math, unchanged draws, complete resume and rejection."""
import copy
from pathlib import Path
import sys

import pytest
import torch
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_teacher_decay_trainer import TeacherDecayTrainer, effective_decay, committed_decay, policy
from base_parallel_residual_trainer import FreshResidualTrainer, CEOnlyOriginalSampler
from natural_context_contrast_trainer import host
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


@pytest.fixture
def build(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    config = copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        config['expected_parameter_count'] = sum(p.numel() for p in JMicroModel(config).parameters())
    def fresh():
        source = CEOnlyOriginalSampler(pool,manifest,FixtureCodec(),dict(web=75000,textbook=20000,story=5000))
        return FreshResidualTrainer(config,source,dict(proposal='teacher_decay_fixture'),
                                    'sequential',batch=4,device='cpu',warmup=1000)
    return fresh


def test_one_native_step_matches_independent_parameter_decay_difference(build):
    control = build()
    initial = host(control.state_dict())
    baseline = control.step()
    original = host(control.state_dict())
    candidate = TeacherDecayTrainer(build())
    assert equal_state(initial['model'],candidate.state_dict()['model'])
    assert equal_state(initial['RNG'],candidate.state_dict()['RNG'])
    row = candidate.step()
    actual = host(candidate.state_dict())
    n, lr = row['CE_targets_this_update'], row['lr']
    wd = effective_decay(lr,n)
    assert 1-lr*wd == pytest.approx((1-lr*.1)**(n/32768),rel=1e-15)
    assert effective_decay(lr,32768) == pytest.approx(.1)
    assert equal_state(original['optimizer']['state'],actual['optimizer']['state'])
    # First-step CE gradient, clipping and Adam correction are identical.
    # The only parameter difference is the separate decay of the SAME W0.
    for name, value in actual['model'].items():
        expected = original['model'][name]+initial['model'][name]*(lr*(.1-wd))
        torch.testing.assert_close(value,expected,rtol=2e-6,atol=2e-7)
    for key in (*control.counters,'draw_trace','lr'):
        assert equal_state(row[key],baseline[key]),key
    assert committed_decay(actual)
    assert candidate.native.model.lm_head.weight is candidate.native.model.model.embed_tokens.weight
    with pytest.raises(ValueError,match='Untouched'):
        TeacherDecayTrainer(candidate.native)


def test_four_vs_two_save_two_all_state_and_history(build,tmp_path):
    full = TeacherDecayTrainer(build())
    history = [full.step() for _ in range(4)]
    expected = host(full.state_dict())
    split = TeacherDecayTrainer(build())
    resumed = [split.step() for _ in range(2)]
    path = tmp_path/'decay.pt'
    split.save(path)
    other = TeacherDecayTrainer(build())
    other.load(path)
    resumed.extend(other.step() for _ in range(2))
    assert equal_state(expected,host(other.state_dict()))
    strip = lambda row:{k:v for k,v in row.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(row) for row in history],[strip(row) for row in resumed])


@pytest.mark.parametrize('corruption',['legacy_kind','reference','actual_rate','teacher_count','binding'])
def test_foreign_or_uncoupled_state_refused_before_mutation(build,tmp_path,corruption):
    source = TeacherDecayTrainer(build())
    source.step()
    state = host(source.state_dict())
    if corruption=='legacy_kind':
        state = host(build().state_dict())
    elif corruption=='reference':
        state['decay']['policy']['reference_teachers'] *= 2
    elif corruption=='actual_rate':
        state['optimizer']['param_groups'][0]['weight_decay'] = .1
    elif corruption=='teacher_count':
        state['decay']['last_update_teachers'] += 1
    else:
        state['binding']['proposal'] = 'different'
    path = tmp_path/'foreign.pt'
    torch.save(state,path)
    target = TeacherDecayTrainer(build())
    before = host(target.state_dict())
    with pytest.raises(ValueError):
        target.load(path)
    assert equal_state(before,host(target.state_dict()))
