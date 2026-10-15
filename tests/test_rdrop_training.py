"""Real CPU Adam, stochastic RNG resume and honest repeated supervision clocks."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from rdrop_trainer import RDropTrainer,committed_state
from jmicro.rdrop import ARMS
from jmicro.phase5 import equal_state
from jmicro.model import JMicroModel
from jmicro.training import rng_state
from natural_context_contrast_trainer import host
from test_document_progress_training import builders as old_builders


def builders(tmp_path):
    parent,old_build = old_builders(tmp_path)
    def build(arm='normalized_rdrop',legacy=False):
        old = old_build(legacy=True)
        if legacy: return old
        return RDropTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    return parent,build


def test_disabled4_ALL_original_weights_Adam_CE_gradient_RNG_source_exact(tmp_path):
    _,build = builders(tmp_path)
    current = build('disabled_native')
    initial = host(current.state_dict())
    rows,states = [],[]
    for _ in range(4):
        rows.append(current.step())
        states.append(host(current.state_dict()))
    native = build(legacy=True)
    assert equal_state(initial['model'],native.model.state_dict())
    assert equal_state(initial['RNG'],host(rng_state()))
    for row,state in zip(rows,states,strict=True):
        expected = native.step()
        ref = host(native.state_dict())
        for key in ('model','optimizer','scheduler','sampler','RNG'):
            assert equal_state(state[key],ref[key]),key
        for key in ('CE_loss','gradient_norm','token_digest','source_teachers','source_EOS','CE_input_tokens',
                'physical_input_tokens','original_body_bytes','draw_trace','lr'):
            assert equal_state(row[key],expected[key]),key
        assert row['combined_loss'] == row['CE_loss']
        assert row['symmetric_KL'] == row['consistency_pairs'] == row['second_view_gold_evaluations'] == 0


def test_active_two_graph_gradients_preserve_main_stream_and_count_duplicate_work(tmp_path):
    _,build = builders(tmp_path)
    current,native = build(),build(legacy=True)
    initial = host(current.state_dict())
    for _ in range(4):
        a,b = current.step(),native.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
                'original_body_bytes','token_digest','draw_trace','lr'):
            assert equal_state(a[key],b[key]),key
        assert equal_state(current.sampler.state_dict(),native.sampler.state_dict())
        assert a['symmetric_KL'] > 0 and a['different_view_positions_this_update'] > 0
        assert a['total_CE_teacher_evaluations'] == 2*a['supervised_tokens']
        assert a['second_view_gold_evaluations'] == a['consistency_pairs'] == a['supervised_tokens']
        assert a['physical_input_tokens'] == 2*a['main_physical_input_tokens'] == 2*b['physical_input_tokens']
        assert a['auxiliary_input_tokens'] == a['CE_input_tokens']
        assert a['second_view_EOS_evaluations'] == sum(a['source_EOS'].values())
        assert a['auxiliary_digest'] == a['token_digest']
    assert not equal_state(initial['RNG'],host(current.state_dict())['RNG'])
    assert not equal_state(current.model.state_dict(),native.model.state_dict())
    assert committed_state(current.state_dict())


@pytest.mark.parametrize('arm',ARMS)
def test_BOTH6_vs3_save3_ALL_numerical_state_stochastic_RNG_and_history_exact(tmp_path,arm):
    _,build = builders(tmp_path)
    full = build(arm)
    rows = [full.step() for _ in range(6)]
    expected = host(full.state_dict())
    split = build(arm)
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed = build(arm)
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected,host(resumed.state_dict()))
    strip = lambda row:{k:v for k,v in row.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(r) for r in rows],[strip(r) for r in actual])


@pytest.mark.parametrize('bad',['policy','kind','binding','optimizer','schedule','model_nan','RNG',
    'sampler_binding','second_gold','physical','auxiliary_digest','EOS','parameter_count'])
def test_invalid_state_refused_before_ANY_mutation(tmp_path,bad):
    _,build = builders(tmp_path)
    current = build()
    current.step()
    state = host(current.state_dict())
    if bad == 'policy': state['spec']['rdrop_policy']['symmetric_KL_coefficient'] = 1.
    elif bad == 'kind': state['kind'] = 'native'
    elif bad == 'binding': state['binding']['weights_role'] = 'different'
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'schedule': state['scheduler']['last_epoch'] += 1
    elif bad == 'model_nan': state['model']['model.norm.weight'][0] = torch.nan
    elif bad == 'RNG': state['RNG'] = {}
    elif bad == 'sampler_binding': state['sampler']['binding']['pool'] = 'different'
    elif bad == 'second_gold': state['counters']['second_view_gold_evaluations'] += 1
    elif bad == 'physical': state['counters']['physical_input_tokens'] += 1
    elif bad == 'auxiliary_digest': state['counters']['auxiliary_digest'] = '0'*64
    elif bad == 'EOS': state['counters']['second_view_EOS_evaluations'] += 1
    else: state['spec']['training_parameters'] += 1
    torch.save(state,tmp_path/'bad.pt')
    target = build()
    before = host(target.state_dict())
    with pytest.raises(ValueError): target.load(tmp_path/'bad.pt')
    assert equal_state(before,host(target.state_dict()))


def test_interrupted_after_Adam_blocks_save_retry_until_valid_completed_restore(tmp_path,monkeypatch):
    _,build = builders(tmp_path)
    current = build()
    current.save(tmp_path/'zero.pt')
    before = host(current.state_dict())
    original = current.optimizer.step
    def interrupted(*args,**kwargs):
        original(*args,**kwargs)
        raise RuntimeError('After Adam mutation')
    monkeypatch.setattr(current.optimizer,'step',interrupted)
    with pytest.raises(RuntimeError): current.step()
    with pytest.raises(ValueError): current.save(tmp_path/'dirty.pt')
    with pytest.raises(ValueError): current.step()
    current.load(tmp_path/'zero.pt')
    assert equal_state(before,host(current.state_dict()))


def test_actual_eval_without_dropout_matches_native_weights_cache_and_RNG(tmp_path):
    parent,build = builders(tmp_path)
    current = build()
    current.step()
    current.model.eval()
    native = JMicroModel(parent['model_config']).eval()
    native.load_state_dict(current.model.state_dict(),strict=True)
    ids = torch.tensor([[2,10,11,12,13,14]])
    before = host(rng_state())
    with torch.no_grad():
        a,b = current.model(ids,use_cache=True),native(ids,use_cache=True)
        prefix = current.model(ids[:,:3],use_cache=True)
        suffix = current.model(ids[:,3:],cache=prefix.cache,use_cache=True)
    assert equal_state(before,host(rng_state()))
    assert torch.equal(a.logits,b.logits)
    assert torch.allclose(a.logits[:,-3:],suffix.logits,atol=3e-5,rtol=2e-5)
    assert set(current.model.state_dict()) == set(native.state_dict())
    for pair,want in zip(a.cache.layers,b.cache.layers,strict=True):
        assert all(torch.equal(x,y) for x,y in zip(pair,want,strict=True))


def test_legacy_or_other_arm_checkpoint_cannot_be_relabelled(tmp_path):
    _,build = builders(tmp_path)
    old = build(legacy=True)
    old.save(tmp_path/'legacy.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'legacy.pt')
    disabled = build('disabled_native')
    disabled.save(tmp_path/'disabled.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'disabled.pt')
