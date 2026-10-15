"""Real optimizer/full-state CPU checks for both explicitly matched arms."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from forgetting_attention_prefetch_trainer import PrefetchForgettingTrainer as ForgettingTrainer, committed_state, KIND
from natural_context_contrast_trainer import host
from jmicro.forgetting_attention_canonical import TAG, ARMS, IMPLEMENTATION, RUNTIME_KEY
from jmicro.phase5 import equal_state
from test_pseudo_repetition_training import builders as original_builders
from forgetting_attention_prefetch_loader import PrefetchedOriginalSampler


@pytest.fixture(autouse=True)
def drain_owned_test_producers(monkeypatch):
    live = []
    original = PrefetchedOriginalSampler.__init__
    def init(instance, *args, **kwargs):
        original(instance, *args, **kwargs)
        live.append(instance)
    monkeypatch.setattr(PrefetchedOriginalSampler, '__init__', init)
    yield
    for producer in live:
        producer.close()


def builders(tmp_path):
    parent, old_build = original_builders(tmp_path)
    parent['model_config']['expected_parameter_count'] = sum(
        v.numel() for k, v in parent['model'].items() if k != 'lm_head.weight')
    def build(arm='learned_forget', legacy=False):
        old = old_build(legacy=True)
        if legacy:
            return old
        return ForgettingTrainer(parent, old.sampler, old.binding, batch=6, device='cpu', arm=arm)
    return parent, build


def test_initial_arms_model_optimizer_rng_sampler_and_first_CE_exact(tmp_path):
    _, build = builders(tmp_path)
    a = build()
    initial = host(a.state_dict())
    first = a.step()
    b = build('static_half_forget')
    static_initial = host(b.state_dict())
    assert all(equal_state(initial[k], static_initial[k]) for k in
               ('model', 'optimizer', 'scheduler', 'RNG', 'sampler', 'counters'))
    second = b.step()
    assert first['CE_loss'] == second['CE_loss']
    assert first['forget_projection_abs_max'] > 0
    assert second['forget_projection_abs_max'] == 0
    assert initial['kind'] == static_initial['kind'] == KIND
    assert initial['spec']['attention_backend'] == 'pinned_author_tiled_BF16_canonical64_MATH_FP32_cache_v1'
    assert initial['spec']['attention_implementation'] == IMPLEMENTATION
    assert initial['lineage']['attention_implementation'] == IMPLEMENTATION
    # These are changed native inference functions, not original-native parity.
    assert initial['model_config'][TAG]['policy']['native_initial_function_preserved'] is False


@pytest.mark.parametrize('arm', ARMS)
def test_both_arms_retain_original_stream_all_source_clocks_and_real_Adam_steps(tmp_path, arm):
    _, build = builders(tmp_path)
    current, original = build(arm), build(legacy=True)
    for _ in range(4):
        a, b = current.step(), original.step()
        for key in ('supervised_tokens', 'source_teachers', 'source_EOS', 'CE_input_tokens',
                    'original_body_bytes', 'token_digest', 'draw_trace', 'lr', 'physical_input_tokens'):
            assert equal_state(a[key], b[key]), key
        assert equal_state(current.sampler.state_dict(), original.sampler.state_dict())
        c = current.model.config
        assert a['forget_gate_projection_elements'] == a['physical_input_tokens']*c['num_hidden_layers']*4*(c['hidden_size']+1)
        assert a['auxiliary_pairs'] == a['auxiliary_input_tokens'] == 0
        for name, p in current.model.named_parameters():
            assert float(current.optimizer.state[p]['step']) == a['update']
            if arm == 'static_half_forget' and '.forget_proj.' in name:
                assert torch.count_nonzero(p) == 0
                assert torch.count_nonzero(current.optimizer.state[p]['exp_avg']) == 0
                assert torch.count_nonzero(current.optimizer.state[p]['exp_avg_sq']) == 0
    assert committed_state(current.state_dict())


@pytest.mark.parametrize('arm', ARMS)
def test_full6_vs3_save_resume3_all_typed_state_and_history_exact(tmp_path, arm):
    _, build = builders(tmp_path)
    continuous = build(arm)
    history = [continuous.step() for _ in range(6)]
    expected = host(continuous.state_dict())
    split = build(arm)
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed = build(arm)
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected, host(resumed.state_dict()))
    strip = lambda r: {k: v for k, v in r.items() if k not in ('seconds', 'data_wait_seconds')}
    assert equal_state([strip(r) for r in history], [strip(r) for r in actual])


@pytest.mark.parametrize('bad', ['model_tag', 'kind', 'source_RNG', 'source_binding',
    'optimizer', 'clock', 'nonfinite', 'compute_clock', 'backend', 'arm', 'native_count'])
def test_invalid_checkpoint_rejected_before_current_state_changes(tmp_path, bad):
    _, build = builders(tmp_path)
    source = build()
    source.step()
    state = host(source.state_dict())
    if bad == 'model_tag': state['model_config'][TAG]['policy']['initial_forget'] = .9
    elif bad == 'kind': state['kind'] = 'native'
    elif bad == 'source_RNG': state['sampler']['RNG'] = 'INVALID'
    elif bad == 'source_binding': state['sampler']['binding']['pool'] = 'wrong'
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'clock': state['scheduler']['last_epoch'] += 1
    elif bad == 'nonfinite': state['model']['model.layers.1.self_attn.forget_proj.bias'].fill_(torch.nan)
    elif bad == 'compute_clock': state['counters']['forget_gate_projection_elements'] += 1
    elif bad == 'backend': state['spec']['attention_backend'] = 'flash'
    elif bad == 'arm': state['spec']['forgetting_arm'] = 'static_half_forget'
    elif bad == 'native_count': state['spec']['actual_unique_parameters'] += 1
    torch.save(state, tmp_path/'bad.pt')
    target = build()
    before = host(target.state_dict())
    with pytest.raises(ValueError): target.load(tmp_path/'bad.pt')
    assert equal_state(before, host(target.state_dict()))


def test_cross_arm_checkpoint_refused_even_if_numerically_initially_equal(tmp_path):
    _, build = builders(tmp_path)
    learned = build()
    learned.save(tmp_path/'learned.pt')
    static = build('static_half_forget')
    before = host(static.state_dict())
    with pytest.raises(ValueError): static.load(tmp_path/'learned.pt')
    assert equal_state(before, host(static.state_dict()))


def test_static_checkpoint_nonzero_added_coordinate_refused(tmp_path):
    _, build = builders(tmp_path)
    current = build('static_half_forget')
    state = host(current.state_dict())
    state['model']['model.layers.0.self_attn.forget_proj.bias'][0] = 1
    assert not committed_state(state)
    torch.save(state, tmp_path/'bad.pt')
    before = host(current.state_dict())
    with pytest.raises(ValueError): current.load(tmp_path/'bad.pt')
    assert equal_state(before, host(current.state_dict()))


def test_after_Adam_interruption_cannot_save_retry_and_completed_restore_is_exact(tmp_path, monkeypatch):
    _, build = builders(tmp_path)
    current = build()
    current.save(tmp_path/'initial.pt')
    original = current.optimizer.step
    def interrupted(*args, **kwargs):
        original(*args, **kwargs)
        raise RuntimeError('After Adam mutation')
    monkeypatch.setattr(current.optimizer, 'step', interrupted)
    with pytest.raises(RuntimeError): current.step()
    assert current.counters['update'] == 0
    with pytest.raises(ValueError): current.save(tmp_path/'invalid.pt')
    with pytest.raises(ValueError): current.step()
    assert not (tmp_path/'invalid.pt').exists()
    monkeypatch.setattr(current.optimizer, 'step', original)
    current.load(tmp_path/'initial.pt')
    current.step()
    expected = host(current.state_dict())
    clean = build()
    clean.step()
    assert equal_state(expected, host(clean.state_dict()))


def test_reference_checkpoint_refused_without_migration_before_mutation(tmp_path):
    from forgetting_attention_trainer import ForgettingTrainer as Reference
    parent, build = builders(tmp_path)
    bootstrap = build(legacy=True)
    old = Reference(parent, bootstrap.sampler, bootstrap.binding, batch=6, device='cpu')
    old.save(tmp_path/'reference.pt')
    new = build()
    before = host(new.state_dict())
    with pytest.raises(ValueError): new.load(tmp_path/'reference.pt')
    assert equal_state(before, host(new.state_dict()))


@pytest.mark.parametrize('field', ['model_runtime', 'spec_implementation', 'lineage_implementation'])
def test_runtime_markers_cannot_be_missing_or_rebound(tmp_path, field):
    _, build = builders(tmp_path)
    new = build()
    state = host(new.state_dict())
    if field == 'model_runtime': state['model_config'][RUNTIME_KEY] = 'reference'
    elif field == 'spec_implementation': state['spec']['attention_implementation'] = 'reference'
    else: state['lineage']['attention_implementation'] = 'reference'
    assert not committed_state(state)
    torch.save(state, tmp_path/'wrong.pt')
    before = host(new.state_dict())
    with pytest.raises(ValueError): new.load(tmp_path/'wrong.pt')
    assert equal_state(before, host(new.state_dict()))


def test_closed_key_bias_checkpoint_refused_before_mutation(tmp_path):
    from forgetting_attention_key_bias_trainer import KeyBiasForgettingTrainer
    parent, build = builders(tmp_path)
    bootstrap = build(legacy=True)
    old = KeyBiasForgettingTrainer(parent, bootstrap.sampler, bootstrap.binding, batch=6, device='cpu')
    old.save(tmp_path/'key_bias.pt')
    new = build()
    before = host(new.state_dict())
    with pytest.raises(ValueError): new.load(tmp_path/'key_bias.pt')
    assert equal_state(before, host(new.state_dict()))


def test_closed_fused_checkpoint_refused_before_mutation(tmp_path):
    from forgetting_attention_fused_trainer import FusedForgettingTrainer
    parent, build = builders(tmp_path)
    bootstrap = build(legacy=True)
    old = FusedForgettingTrainer(parent, bootstrap.sampler, bootstrap.binding, batch=6, device='cpu')
    old.save(tmp_path/'fused.pt')
    new = build()
    before = host(new.state_dict())
    with pytest.raises(ValueError): new.load(tmp_path/'fused.pt')
    assert equal_state(before, host(new.state_dict()))


@pytest.mark.parametrize('field', ['spec', 'lineage'])
def test_arithmetic_policy_cannot_be_removed_or_silently_changed(tmp_path, field):
    _, build = builders(tmp_path)
    new = build()
    before = host(new.state_dict())
    for operation in ('missing', 'changed'):
        bad = copy.deepcopy(before)
        if operation == 'missing': del bad[field]['FP32_arithmetic_policy']
        else: bad[field]['FP32_arithmetic_policy']['recompute_past_decoder_states'] = True
        assert not committed_state(bad)
        torch.save(bad, tmp_path/'bad_policy.pt')
        with pytest.raises(ValueError): new.load(tmp_path/'bad_policy.pt')
        assert equal_state(before, host(new.state_dict()))


@pytest.mark.parametrize('arm', ARMS)
def test_CPU_all_numeric_state_and_non_time_history_equal_to_synchronous_canonical(tmp_path, arm):
    from forgetting_attention_canonical_trainer import CanonicalForgettingTrainer
    parent, build = builders(tmp_path)
    source = build(legacy=True)
    synchronous = CanonicalForgettingTrainer(parent, source.sampler, source.binding, batch=6, device='cpu', arm=arm)
    expected = [synchronous.step() for _ in range(6)]
    old_state = host(synchronous.state_dict())
    new = build(arm)
    rows = [new.step() for _ in range(6)]
    new_state = host(new.state_dict())
    for key in ('model', 'optimizer', 'scheduler', 'RNG', 'sampler', 'counters'):
        assert equal_state(new_state[key], old_state[key]), key
    strip = lambda r: {k: v for k, v in r.items() if k not in ('seconds', 'data_wait_seconds')}
    assert equal_state([strip(r) for r in rows], [strip(r) for r in expected])
    synchronous.save(tmp_path/'canonical.pt')
    before = host(new.state_dict())
    with pytest.raises(ValueError): new.load(tmp_path/'canonical.pt')
    assert equal_state(before, host(new.state_dict()))
    synchronous.sampler.handle.close()


@pytest.mark.parametrize('field', ['spec', 'lineage'])
def test_loader_policy_cannot_be_removed_or_silently_changed(tmp_path, field):
    _, build = builders(tmp_path)
    new = build()
    before = host(new.state_dict())
    for operation in ('missing', 'changed'):
        bad = copy.deepcopy(before)
        if operation == 'missing': del bad[field]['loader_policy']
        else: bad[field]['loader_policy']['checkpoint_sampler'] = 'speculative_future'
        assert not committed_state(bad)
        torch.save(bad, tmp_path/'bad_loader_policy.pt')
        with pytest.raises(ValueError): new.load(tmp_path/'bad_loader_policy.pt')
        assert equal_state(before, host(new.state_dict()))
