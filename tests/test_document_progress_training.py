"""Original native identity, exact typed resume and honest auxiliary clocks."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from document_progress_trainer import DocumentProgressTrainer,committed_state
from natural_context_contrast_trainer import host
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.document_progress import ARMS
from test_pseudo_repetition_training import builders as original_builders


def builders(tmp_path):
    parent,old_build = original_builders(tmp_path)
    parent['model_config']['expected_parameter_count'] = sum(v.numel() for k,v in parent['model'].items() if k != 'lm_head.weight')
    def build(arm='document_progress',legacy=False):
        old = old_build(legacy=True)
        if legacy: return old
        return DocumentProgressTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    return parent,build


def test_control4_native_model_Adam_by_name_CE_gradient_schedule_RNG_stream_exact(tmp_path):
    _,build = builders(tmp_path)
    control = build('native_CE_control')
    initial = host(control.state_dict())
    snapshots,history = [],[]
    for _ in range(4):
        history.append(control.step())
        snapshots.append(host(control.state_dict()))
    native = build(legacy=True)
    assert equal_state(initial['model'],native.model.state_dict())
    assert equal_state(initial['RNG'],host(native.state_dict())['RNG'])
    for row,saved in zip(history,snapshots,strict=True):
        expected = native.step()
        reference = host(native.state_dict())
        assert equal_state(saved['model'],reference['model'])
        for key in ('CE_loss','gradient_norm','token_digest','source_teachers','source_EOS',
                    'physical_input_tokens','CE_input_tokens','original_body_bytes','draw_trace','lr'):
            assert equal_state(row[key],expected[key]),key
        for key in ('sampler','scheduler','RNG'):
            assert equal_state(saved[key],reference[key]),key
        by_name = dict(zip((n for n,_ in control.model.named_parameters()),saved['optimizer']['param_groups'][0]['params'][:-1],strict=True))
        for name,p in native.model.named_parameters():
            assert equal_state(saved['optimizer']['state'][by_name[name]],host(native.optimizer.state[p])),name
        assert torch.count_nonzero(saved['progress_head']['weight']) == 0
        assert row['head_gradient_abs_max_after_clip'] == row['head_weight_abs_max'] == 0
        assert row['progress_learning_positions'] == 0
        assert row['combined_loss'] == row['CE_loss']
    assert committed_state(control.state_dict())


def test_enabled_preserves_main_source_and_counts_additional_scalar_supervision(tmp_path):
    _,build = builders(tmp_path)
    active,native = build(),build(legacy=True)
    for _ in range(4):
        a,b = active.step(),native.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
                    'original_body_bytes','token_digest','draw_trace','lr','physical_input_tokens'):
            assert equal_state(a[key],b[key]),key
        assert equal_state(active.sampler.state_dict(),native.sampler.state_dict())
        assert a['progress_label_positions'] == a['progress_learning_positions'] == a['supervised_tokens']
        assert a['progress_zero_EOS_labels'] == sum(a['source_EOS'].values())
        assert a['progress_source_labels'] == a['source_teachers']
        assert a['head_weight_abs_max'] > 0 and a['head_gradient_abs_max_after_clip'] > 0
        assert a['auxiliary_input_tokens'] == a['auxiliary_pairs'] == 0
    assert not equal_state(active.model.state_dict(),native.model.state_dict())
    assert committed_state(active.state_dict())


@pytest.mark.parametrize('arm',ARMS)
def test_both6_vs3_save_resume3_ALL_model_head_Adam_RNG_sampler_counter_history_exact(tmp_path,arm):
    _,build = builders(tmp_path)
    continuous = build(arm)
    history = [continuous.step() for _ in range(6)]
    expected = host(continuous.state_dict())
    split = build(arm)
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed = build(arm)
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected,host(resumed.state_dict()))
    strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(r) for r in history],[strip(r) for r in actual])


@pytest.mark.parametrize('bad',['policy','kind','source_RNG','source_binding','optimizer','clock',
    'model_nan','head_nan','head_shape','missing_head','progress_clock','EOS_clock','label_digest'])
def test_malformed_typed_checkpoint_refused_before_any_mutation(tmp_path,bad):
    _,build = builders(tmp_path)
    current = build()
    current.step()
    state = host(current.state_dict())
    if bad == 'policy': state['spec']['progress_policy']['coefficient'] = 1.
    elif bad == 'kind': state['kind'] = 'native'
    elif bad == 'source_RNG': state['sampler']['RNG'] = 'INVALID'
    elif bad == 'source_binding': state['sampler']['binding']['pool'] = 'wrong'
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'clock': state['scheduler']['last_epoch'] += 1
    elif bad == 'model_nan': state['model']['model.norm.weight'][0] = torch.nan
    elif bad == 'head_nan': state['progress_head']['weight'][0,0] = torch.nan
    elif bad == 'head_shape': state['progress_head']['weight'] = state['progress_head']['weight'][:,:1]
    elif bad == 'missing_head': del state['progress_head']
    elif bad == 'progress_clock': state['counters']['progress_learning_positions'] += 1
    elif bad == 'EOS_clock': state['counters']['progress_zero_EOS_labels'] += 1
    else: state['counters']['progress_target_digest'] = 'invalid'
    assert not committed_state(state)
    torch.save(state,tmp_path/'bad.pt')
    target = build()
    before = host(target.state_dict())
    with pytest.raises(ValueError): target.load(tmp_path/'bad.pt')
    assert equal_state(before,host(target.state_dict()))


def test_interruption_after_Adam_cannot_save_retry_but_completed_restore_works(tmp_path,monkeypatch):
    _,build = builders(tmp_path)
    current = build()
    current.save(tmp_path/'initial.pt')
    original = current.optimizer.step
    def interrupted(*args,**kwargs):
        original(*args,**kwargs)
        raise RuntimeError('After Adam mutation')
    monkeypatch.setattr(current.optimizer,'step',interrupted)
    with pytest.raises(RuntimeError): current.step()
    with pytest.raises(ValueError): current.save(tmp_path/'invalid.pt')
    with pytest.raises(ValueError): current.step()
    assert not (tmp_path/'invalid.pt').exists()
    monkeypatch.setattr(current.optimizer,'step',original)
    current.load(tmp_path/'initial.pt')
    current.step()
    clean = build()
    clean.step()
    assert equal_state(host(current.state_dict()),host(clean.state_dict()))


def test_native_inference_omits_head_and_same_native_weights_load_exactly(tmp_path):
    _,build = builders(tmp_path)
    current = build()
    current.step()
    ids = torch.tensor([[2,11,12,13]])
    before = current.model(ids,use_cache=True).logits
    current.progress_head.weight.data.fill_(100.)
    assert torch.equal(before,current.model(ids,use_cache=True).logits)
    # A native inference factory needs exactly the native model weights; no
    # document-length/target/head state is supplied and no special stop rule.
    restored = JMicroModel(current.model.config)
    restored.load_state_dict(current.model.state_dict(),strict=True)
    assert torch.equal(before,restored(ids,use_cache=True).logits)


def test_other_arm_and_legacy_states_never_forged_into_progress_training(tmp_path):
    _,build = builders(tmp_path)
    current = build()
    before = host(current.state_dict())
    for name,source in (('control',build('native_CE_control')),('legacy',build(legacy=True))):
        source.save(tmp_path/(name+'.pt'))
        with pytest.raises(ValueError): current.load(tmp_path/(name+'.pt'))
        assert equal_state(before,host(current.state_dict()))


def test_control_nonzero_head_and_mismatched_inference_policy_are_refused(tmp_path):
    _,build = builders(tmp_path)
    current = build('native_CE_control')
    state = host(current.state_dict())
    state['progress_head']['weight'][0,0] = .1
    assert not committed_state(state)
    state = host(current.state_dict())
    state['spec']['inference_policy'] = 'use_progress_stop'
    assert not committed_state(state)
