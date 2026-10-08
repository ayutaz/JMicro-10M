"""Actual initialization coupling and complete resume/foreign-state refusal."""
import copy
from pathlib import Path
import sys

import pytest
import torch
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_residual_initialization_trainer import InitializationTrainer, committed_initialization, policy
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
        source = CEOnlyOriginalSampler(pool, manifest, FixtureCodec(), dict(web=75000,textbook=20000,story=5000))
        return FreshResidualTrainer(config, source, dict(proposal='initialization_fixture'),
                                    'sequential', batch=4, device='cpu', warmup=1000)
    return fresh


def test_initial_weight_control_rng_tie_count_and_single_application(build):
    native = build()
    initial = host(native.state_dict())
    candidate = InitializationTrainer(native)
    expected_names = {f'model.layers.{i}.{suffix}.weight' for i in range(native.model.config['num_hidden_layers'])
                      for suffix in ('self_attn.o_proj','mlp.down_proj')}
    factor = policy(native.model.config)['factor']
    for name, value in native.model.state_dict().items():
        assert torch.equal(value, initial['model'][name]*factor if name in expected_names else initial['model'][name])
    assert equal_state(candidate.state_dict()['RNG'], initial['RNG'])
    assert native.model.lm_head.weight is native.model.model.embed_tokens.weight
    assert not native.optimizer.state
    assert committed_initialization(candidate.state_dict())
    with pytest.raises(ValueError, match='Untouched'):
        InitializationTrainer(native)


def test_real_four_vs_two_save_two_resume_all_state_and_history(build,tmp_path):
    first = InitializationTrainer(build())
    continuous = [first.step() for _ in range(4)]
    expected = host(first.state_dict())
    split = InitializationTrainer(build())
    resumed = [split.step() for _ in range(2)]
    path = tmp_path/'initialized.pt'
    split.save(path)
    other = InitializationTrainer(build())
    other.load(path)
    resumed.extend(other.step() for _ in range(2))
    assert equal_state(expected, host(other.state_dict()))
    strip = lambda row: {k:v for k,v in row.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(row) for row in continuous],[strip(row) for row in resumed])
    control = build()
    original = [control.step() for _ in range(4)]
    for actual, baseline in zip(continuous, original, strict=True):
        for key in (*control.counters, 'draw_trace','lr'):
            assert equal_state(actual[key],baseline[key]), key


@pytest.mark.parametrize('corruption', ['legacy_kind','factor','binding'])
def test_foreign_or_malformed_state_refused_without_model_mutation(build,tmp_path,corruption):
    source = InitializationTrainer(build())
    source.step()
    state = host(source.state_dict())
    if corruption == 'legacy_kind':
        state = host(build().state_dict())
    elif corruption == 'factor':
        state['initialization']['factor'] *= 2
    else:
        state['binding']['proposal'] = 'different'
    path = tmp_path/'foreign.pt'
    torch.save(state,path)
    target = InitializationTrainer(build())
    before = host(target.state_dict())
    with pytest.raises(ValueError):
        target.load(path)
    assert equal_state(before,host(target.state_dict()))
