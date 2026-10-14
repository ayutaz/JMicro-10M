"""Real CPU optimizer/full-state tests for the declared model variant."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from causal_qkv_trainer import CausalQKVTrainer, committed_state
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_pseudo_repetition_training import builders as original_builders


def builders(tmp_path):
    parent, old_build = original_builders(tmp_path)
    parent['model_config']['expected_parameter_count'] = sum(v.numel() for k,v in parent['model'].items() if k != 'lm_head.weight')
    def build(arm='lag_learned', legacy=False):
        old = old_build(legacy=True)
        if legacy:
            return old
        return CausalQKVTrainer(parent, old.sampler, old.binding, batch=6, device='cpu', arm=arm)
    return parent, build


def assert_original_coordinates(candidate, old):
    assert all(torch.equal(candidate.model.state_dict()[k], v) for k,v in old.model.state_dict().items())
    original_parameters = dict(old.model.named_parameters())
    for name, parameter in candidate.model.named_parameters():
        if name.endswith(('.q_lag','.k_lag','.v_lag')):
            assert torch.count_nonzero(parameter) == 0
            continue
        assert equal_state(candidate.optimizer.state[parameter], old.optimizer.state[original_parameters[name]])


def test_static_identity_real_CE_model_Adam_coordinates_schedule_RNG_and_source_equal_native(tmp_path):
    _, build = builders(tmp_path)
    current = build('static_identity')
    initial = host(current.state_dict())
    snapshots, histories = [], []
    for _ in range(4):
        histories.append(current.step())
        snapshots.append((host(current.state_dict()), copy.deepcopy(current.optimizer.state_dict())))
    old = build(legacy=True)
    assert all(torch.equal(initial['model'][k], v) for k,v in old.model.state_dict().items())
    assert equal_state(initial['RNG'], host(old.state_dict())['RNG'])
    # Compare at each update by loading saved candidate snapshots, without
    # replacing the native parameter names by shifted numeric Adam IDs.
    for index, (a, (saved, _)) in enumerate(zip(histories, snapshots)):
        b = old.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
                    'original_body_bytes','token_digest','draw_trace','CE_loss','gradient_norm','lr'):
            assert equal_state(a[key], b[key]), key
        assert all(equal_state(saved[k], host(old.state_dict())[k]) for k in ('scheduler','RNG','sampler'))
        path = tmp_path/f'candidate-{index}.pt'
        torch.save(saved, path)
        current.load(path)
        assert_original_coordinates(current, old)
    assert committed_state(current.state_dict())


def test_learned_QKV_lags_update_coefficients_and_preserve_all_original_stream_clocks(tmp_path):
    _, build = builders(tmp_path)
    current, old = build(), build(legacy=True)
    for _ in range(4):
        a, b = current.step(), old.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
                    'original_body_bytes','token_digest','draw_trace','lr','physical_input_tokens'):
            assert equal_state(a[key], b[key]), key
        assert equal_state(current.sampler.state_dict(), old.sampler.state_dict())
        assert a['lag_coefficient_abs_max'] > 0
        assert a['causal_QKV_lag_elements'] == a['physical_input_tokens']*2*(4+2*2)*8*2
        assert a['auxiliary_pairs'] == a['auxiliary_input_tokens'] == 0
    assert not equal_state(current.model.state_dict()['model.embed_tokens.weight'], old.model.state_dict()['model.embed_tokens.weight'])
    assert committed_state(current.state_dict())


def test_full6_vs3_save_resume3_tagged_model_Adam_RNG_material_and_history_exact(tmp_path):
    _, build = builders(tmp_path)
    continuous = build()
    history = [continuous.step() for _ in range(6)]
    expected = host(continuous.state_dict())
    split = build()
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed = build()
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected, host(resumed.state_dict()))
    strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(r) for r in history], [strip(r) for r in actual])


@pytest.mark.parametrize('bad', ['model_tag','kind','source_RNG','source_binding','optimizer','clock','nonfinite','compute_clock'])
def test_invalid_checkpoint_rejected_before_mutating_current_state(tmp_path, bad):
    _, build = builders(tmp_path)
    source = build()
    source.step()
    state = host(source.state_dict())
    if bad == 'model_tag': state['model_config']['causal_QKV_lag_research']['policy']['previous_lags'] = [1,3]
    elif bad == 'kind': state['kind'] = 'native'
    elif bad == 'source_RNG': state['sampler']['RNG'] = 'INVALID'
    elif bad == 'source_binding': state['sampler']['binding']['pool'] = 'wrong'
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'clock': state['scheduler']['last_epoch'] += 1
    elif bad == 'nonfinite': state['model']['model.layers.1.self_attn.q_lag'].fill_(torch.nan)
    else: state['counters']['causal_QKV_lag_elements'] += 1
    torch.save(state, tmp_path/'bad.pt')
    target = build()
    before = host(target.state_dict())
    with pytest.raises(ValueError): target.load(tmp_path/'bad.pt')
    assert equal_state(before, host(target.state_dict()))


def test_after_Adam_interruption_no_save_or_retry_then_valid_completed_restore(tmp_path, monkeypatch):
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
