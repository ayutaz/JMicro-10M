"""Real CPU optimizer/full-state tests for the declared model variant."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from independent_map_trainer import IndependentMapTrainer, committed_state
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from jmicro.independent_map import extra_parameter, added_parameters, ARMS
from test_pseudo_repetition_training import builders as original_builders


def builders(tmp_path):
    parent, old_build = original_builders(tmp_path)
    parent['model_config']['expected_parameter_count'] = sum(v.numel() for k,v in parent['model'].items() if k != 'lm_head.weight')
    def build(arm='independent_learned', legacy=False):
        old = old_build(legacy=True)
        if legacy:
            return old
        return IndependentMapTrainer(parent, old.sampler, old.binding, batch=6, device='cpu', arm=arm)
    return parent, build


def assert_original_coordinates(candidate, old):
    assert all(torch.equal(candidate.model.state_dict()[k], v) for k,v in old.model.state_dict().items())
    original_parameters = dict(old.model.named_parameters())
    for name, parameter in candidate.model.named_parameters():
        if extra_parameter(name):
            if name.endswith('.independent_raw'): assert torch.count_nonzero(parameter) == 0
            continue
        assert equal_state(candidate.optimizer.state[parameter], old.optimizer.state[original_parameters[name]])


def test_disabled_zero_real_CE_model_Adam_coordinates_schedule_RNG_and_source_equal_native(tmp_path):
    _, build = builders(tmp_path)
    current = build('disabled_zero')
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


def test_learned_value_shortcuts_update_coefficients_and_preserve_all_original_stream_clocks(tmp_path):
    _, build = builders(tmp_path)
    current, old = build(), build(legacy=True)
    for _ in range(4):
        a, b = current.step(), old.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
                    'original_body_bytes','token_digest','draw_trace','lr','physical_input_tokens'):
            assert equal_state(a[key], b[key]), key
        assert equal_state(current.sampler.state_dict(), old.sampler.state_dict())
        assert a['independent_coefficient_abs_max'] > 0
        c = current.model.config
        assert a['independent_projection_elements'] == a['physical_input_tokens']*(added_parameters(c)-c['num_hidden_layers']*c['num_attention_heads'])
        assert a['auxiliary_pairs'] == a['auxiliary_input_tokens'] == 0
    assert not equal_state(current.model.state_dict()['model.embed_tokens.weight'], old.model.state_dict()['model.embed_tokens.weight'])
    assert committed_state(current.state_dict())


@pytest.mark.parametrize('arm', ARMS)
def test_full6_vs3_save_resume3_tagged_model_Adam_RNG_material_and_history_exact(tmp_path,arm):
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
    strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(r) for r in history], [strip(r) for r in actual])


@pytest.mark.parametrize('bad', ['model_tag','kind','source_RNG','source_binding','optimizer','clock','nonfinite','compute_clock'])
def test_invalid_checkpoint_rejected_before_mutating_current_state(tmp_path, bad):
    _, build = builders(tmp_path)
    source = build()
    source.step()
    state = host(source.state_dict())
    if bad == 'model_tag': state['model_config']['independent_QK_map_research']['policy']['rank'] = True
    elif bad == 'kind': state['kind'] = 'native'
    elif bad == 'source_RNG': state['sampler']['RNG'] = 'INVALID'
    elif bad == 'source_binding': state['sampler']['binding']['pool'] = 'wrong'
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'clock': state['scheduler']['last_epoch'] += 1
    elif bad == 'nonfinite': state['model']['model.layers.1.self_attn.independent_raw'].fill_(torch.nan)
    else: state['counters']['independent_projection_elements'] += 1
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


def test_all_independent_projection_and_coefficient_Adam_paths_become_active(tmp_path):
    _,build = builders(tmp_path)
    trainer = build()
    for _ in range(4): trainer.step()
    for name,p in trainer.model.named_parameters():
        assert float(trainer.optimizer.state[p]['step']) == 4
        if extra_parameter(name):
            assert p.grad is not None and torch.isfinite(p.grad).all() and p.grad.abs().sum() > 0,name
            assert trainer.optimizer.state[p]['exp_avg'].abs().sum() > 0,name
    assert committed_state(trainer.state_dict())


@pytest.mark.parametrize('field',['spec','lineage','model_config'])
def test_explicit_implementation_binding_required_before_checkpoint_mutation(tmp_path,field):
    _,build = builders(tmp_path)
    trainer = build()
    before = host(trainer.state_dict())
    bad = copy.deepcopy(before)
    if field == 'model_config': bad[field]['independent_QK_map_research']['implementation'] = 'native'
    else: bad[field]['attention_implementation'] = 'cross_map'
    assert not committed_state(bad)
    torch.save(bad,tmp_path/'wrong_impl.pt')
    with pytest.raises(ValueError): trainer.load(tmp_path/'wrong_impl.pt')
    assert equal_state(before,host(trainer.state_dict()))


def test_disabled_and_native_checkpoints_are_not_silently_imported_into_learned_runtime(tmp_path):
    _,build = builders(tmp_path)
    current = build()
    before = host(current.state_dict())
    for name,source in (('disabled',build('disabled_zero')),('native',build(legacy=True))):
        source.save(tmp_path/(name+'.pt'))
        with pytest.raises(ValueError): current.load(tmp_path/(name+'.pt'))
        assert equal_state(before,host(current.state_dict()))
