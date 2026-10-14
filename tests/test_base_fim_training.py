"""Real fixture CE/backward/Adam, native identity matching and complete resume.

These are CPU correctness checks, not native GPU learning or quality evidence.
"""
import copy
from collections import Counter
from pathlib import Path
import sys

import pytest
import torch
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_fim_sampler import FimOriginalSampler
from base_fim_trainer import FreshFimTrainer, committed_state
from base_parallel_residual_trainer import FreshResidualTrainer
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from jmicro.model import JMicroModel
from test_natural_context_contrast_corpus import FixtureCodec, fixture_pool, parent


@pytest.fixture
def factory(tmp_path):
    pool = tmp_path/'source'; pin = fixture_pool(pool)
    config = copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        config['expected_parameter_count'] = sum(p.numel() for p in JMicroModel(config).parameters())
    def make(kind='FIM', seed=42, goals=None):
        goals = goals or dict(web=75000, textbook=20000, story=5000)
        sampler = (FimOriginalSampler if kind == 'FIM' else CEOnlyOriginalSampler)(
            pool, pin, FixtureCodec(), goals, seed=seed)
        binding = dict(role='CPU_fixture_only', seed=seed)
        if kind == 'FIM':
            return FreshFimTrainer(config,sampler,binding,batch=4,device='cpu',seed=seed,warmup=1000)
        return FreshResidualTrainer(config,sampler,binding,'sequential',batch=4,device='cpu',seed=seed,warmup=1000)
    return make


def test_exact_original_draws_gold_and_partial_quota_masks(factory):
    goals = dict(web=1007, textbook=81, story=79)
    control = factory('AR', goals=goals).sampler
    candidate = factory(goals=goals).sampler
    applied = long_rows = partial_augmented = 0
    while not control.exhausted:
        native, augmented = control.take(4), candidate.take(4)
        assert len(native) == len(augmented)
        for old,new in zip(native,augmented):
            for key in ('index_byte_position','index_record_sha256','teacher_tokens','teacher_body_bytes',
                        'source','original_EOS_targets','target_first','target_end','input_start'):
                assert old[key] == new[key], key
            assert Counter(t for t in old['target_ids'] if t >= 0) == Counter(t for t in new['target_ids'] if t >= 0)
            assert len(new['input_ids']) == len(new['target_ids']) <= 1024
            if new['FIM_applied']:
                applied += 1
                assert new['FIM_marker_inputs'] > 0
                assert new['input_ids'] != old['input_ids']
                assert new['target_ids'].count(-100) - old['target_ids'].count(-100) == new['FIM_marker_inputs']
                partial_augmented += -100 in old['target_ids']
            if old['original_body_tokens'] + 1 > 512:
                long_rows += 1
                assert not new['FIM_applied']
                assert new['input_ids'] == old['input_ids'] and new['target_ids'] == old['target_ids']
        a,b = control.state_dict(),candidate.state_dict()
        assert equal_state({k:a[k] for k in a if k != 'kind'}, {k:b[k] for k in a if k != 'kind'})
    assert applied > 0 and partial_augmented > 0
    assert candidate.consumed == control.consumed == goals
    # Long-unit coverage is exercised independently below if this draw omitted one.


def test_all_long_windows_remain_AR_and_one_original_EOS(factory):
    native = factory('AR').sampler; candidate = factory().sampler
    long = []
    for _ in range(30):
        a,b = native.take(4),candidate.take(4)
        for old,new in zip(a,b):
            if old['original_body_tokens'] > 511:
                long.append(new)
                assert not new['FIM_eligible'] and not new['FIM_applied']
                assert old['input_ids'] == new['input_ids'] and old['target_ids'] == new['target_ids']
    assert long and any(r['original_EOS_targets'] == 1 for r in long)


def test_native_initialization_training_RNG_and_material_stream_match(factory):
    baseline = factory('AR'); before = host(baseline.state_dict())
    candidate = factory(); initial = host(candidate.state_dict())
    assert equal_state(before['model'],initial['model'])
    assert equal_state(before['optimizer'],initial['optimizer'])
    assert equal_state(before['scheduler'],initial['scheduler'])
    assert equal_state(before['RNG'],initial['RNG'])
    assert equal_state(before['sampler']['RNG'],initial['sampler']['RNG'])
    control_rows = [baseline.step() for _ in range(4)]
    candidate_rows = [candidate.step() for _ in range(4)]
    for old,new in zip(control_rows,candidate_rows):
        for key in ('update','supervised_tokens','source_teachers','source_EOS','original_body_bytes','lr','draw_trace'):
            assert equal_state(old[key],new[key]), key
        assert new['FIM_counters']['native_stream_digest'] == old['token_digest']
    assert candidate.sampler.fim['applied_rows'] > 0
    assert committed_state(candidate.state_dict())
    assert candidate.model.lm_head.weight is candidate.model.model.embed_tokens.weight


def test_actual_four_steps_match_two_save_two_all_state_and_history(factory,tmp_path):
    complete = factory(); history = [complete.step() for _ in range(4)]
    expected = host(complete.state_dict())
    split = factory(); resumed = [split.step() for _ in range(2)]
    path = tmp_path/'fullstate.pt'; split.save(path)
    other = factory(); other.load(path)
    resumed.extend(other.step() for _ in range(2))
    assert equal_state(expected,host(other.state_dict()))
    strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(r) for r in history],[strip(r) for r in resumed])


@pytest.mark.parametrize('corruption', ['kind','binding','policy','schedule','Adam_step',
    'model_dtype','material_RNG','augmentation_RNG','pending_source','FIM_count'])
def test_bad_completed_state_refused_before_any_mutation(factory,tmp_path,corruption):
    source = factory(); source.step(); state = host(source.state_dict())
    if corruption == 'kind': state['kind'] = 'legacy_or_random_seed_claim'
    elif corruption == 'binding': state['binding']['role'] = 'foreign'
    elif corruption == 'policy': state['spec']['FIM_policy']['probability'] = .9
    elif corruption == 'schedule': state['scheduler']['tokens'] += 1
    elif corruption == 'Adam_step': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif corruption == 'model_dtype':
        state['model']['model.norm.weight'] = state['model']['model.norm.weight'].half()
    elif corruption == 'material_RNG': state['sampler']['RNG'] = None
    elif corruption == 'augmentation_RNG': state['sampler']['FIM_RNG'] = None
    elif corruption == 'pending_source':
        windows = next(v for v in state['sampler']['pending'].values() if v)
        windows[0]['source'] = 'TEST'
    else: state['sampler']['FIM_counters']['rows'] += 1
    path = tmp_path/'bad.pt'; torch.save(state,path)
    target = factory(); before = host(target.state_dict())
    with pytest.raises(ValueError): target.load(path)
    assert equal_state(before,host(target.state_dict()))


def test_interrupted_update_cannot_be_saved_or_retried_and_can_resume(factory,tmp_path,monkeypatch):
    candidate = factory(); path = tmp_path/'valid.pt'; candidate.save(path)
    with monkeypatch.context() as context:
        def failed(): raise RuntimeError('fixture Adam update interruption')
        context.setattr(candidate.optimizer,'step',failed)
        with pytest.raises(RuntimeError,match='interruption'): candidate.step()
    with pytest.raises(ValueError,match='interrupted'): candidate.state_dict()
    with pytest.raises(ValueError,match='Interrupted'): candidate.step()
    candidate.load(path)
    assert candidate.counters['update'] == 0 and not candidate._step_in_progress
    candidate.step()
    assert committed_state(candidate.state_dict())


def test_fresh_43_has_distinct_actual_weights_and_both_actual_RNGs(factory):
    a = host(factory(seed=42).state_dict()); b = host(factory(seed=43).state_dict())
    assert not equal_state(a['model'],b['model']) and not equal_state(a['RNG'],b['RNG'])
    assert not equal_state(a['sampler']['RNG'],b['sampler']['RNG'])
    assert not equal_state(a['sampler']['FIM_RNG'],b['sampler']['FIM_RNG'])
    assert a['counters']['update'] == b['counters']['update'] == 0
    assert a['lineage']['parent'] is b['lineage']['parent'] is None
    assert not a['optimizer']['state'] and not b['optimizer']['state']
