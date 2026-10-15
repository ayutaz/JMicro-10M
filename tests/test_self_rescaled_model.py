"""Owned model/tag/cache, all-parameter integration and original conversion."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch

from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.self_rescaled_model import (TAG,ARMS,SelfRescaledModel as Model,
    SelfRescaledCache,native_config,tagged_config,added_parameters,extra_parameter)
from jmicro.self_rescaled_norm import SelfRescaledRMSNorm
from test_value_residual import native


def active():
    model = Model.from_native(native())
    with torch.no_grad():
        for index,(_,m) in enumerate((n,m) for n,m in model.named_modules() if type(m) is SelfRescaledRMSNorm):
            m.rescale_beta.copy_(torch.linspace(-.07,.08,len(m.weight))*(1+index/10))
            m.rescale_alpha.copy_(torch.linspace(.2,1.2,len(m.weight)))
    return model


@pytest.mark.parametrize('arm',ARMS)
def test_original_tensors_names_tie_count_RNG_native_initial_function_and_ALL_old_gradients(arm):
    original = native()
    state = copy.deepcopy(original.state_dict())
    rng = torch.get_rng_state().clone()
    model = Model.from_native(original,arm)
    assert torch.equal(rng,torch.get_rng_state()) and not torch.cuda.is_initialized()
    assert equal_state(original.state_dict(),state)
    assert all(torch.equal(model.state_dict()[k],v) for k,v in state.items())
    assert [n for n,_ in model.named_parameters() if not extra_parameter(n)] == [n for n,_ in original.named_parameters()]
    assert model.lm_head.weight is model.model.embed_tokens.weight
    assert native_config(model.config) == original.config
    assert sum(p.numel() for p in model.parameters()) == sum(p.numel() for p in original.parameters())+added_parameters(original.config)
    ids = torch.tensor([[2,11,12,13,3]])
    a,b = original(ids).logits,model(ids).logits
    assert torch.equal(a,b)
    assert torch.equal(original(ids,training_fast_path=True).logits,model(ids,training_fast_path=True).logits)
    a.square().sum().backward()
    b.square().sum().backward()
    for n,p in original.named_parameters():
        assert torch.equal(p.grad,dict(model.named_parameters())[n].grad),n


def test_actual_tagged_factory_all27_RMS_sites_count54_new_tensors_no_QK_norm():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    with torch.device('meta'): model = Model(tagged_config(c))
    assert sum(p.numel() for p in model.parameters()) == 10014976
    assert added_parameters(c) == 13824
    assert sum(type(m) is SelfRescaledRMSNorm for m in model.modules()) == 27
    assert len([n for n,_ in model.named_parameters() if extra_parameter(n)]) == 54
    assert native_config(model.config) == c
    assert all(type(layer.self_attn.q_norm) is torch.nn.Identity and type(layer.self_attn.k_norm) is torch.nn.Identity for layer in model.model.layers)


@pytest.mark.parametrize('mask',[
    [[1,1,1,1,1,1],[1,1,1,0,0,0]],
    [[0,0,1,1,1,1],[1,0,1,0,1,1]],
    [[0,0,0,0,0,0],[0,1,0,1,0,1]],
])
def test_active_full_chunk_token_real_cache_padding_holes_allPAD_no_recompute(mask):
    model = active()
    ids = torch.tensor([[2,11,12,13,14,3],[2,21,22,23,24,3]])
    valid = torch.tensor(mask,dtype=torch.bool)
    full = model(ids,attention_mask=valid,use_cache=True)
    prefix = model(ids[:,:3],attention_mask=valid[:,:3],use_cache=True)
    observed = []
    h = model.model.embed_tokens.register_forward_pre_hook(lambda _,args:observed.append(args[0].shape[1]))
    try: suffix = model(ids[:,3:],attention_mask=valid[:,3:],cache=prefix.cache,use_cache=True)
    finally: h.remove()
    assert observed == [3]
    torch.testing.assert_close(torch.cat((prefix.logits,suffix.logits),1),full.logits,atol=3e-6,rtol=2e-5)
    pieces,cache = [],None
    for i in range(6):
        out = model(ids[:,i:i+1],attention_mask=valid[:,i:i+1],cache=cache,use_cache=True)
        pieces.append(out.logits)
        cache = out.cache
    torch.testing.assert_close(torch.cat(pieces,1),full.logits,atol=3e-6,rtol=2e-5)
    assert type(cache) is SelfRescaledCache and not hasattr(cache,'layers')
    assert torch.equal(cache.valid,valid) and torch.equal(cache.positions,full.cache.positions)
    for pair,want in zip(cache.real,full.cache.real,strict=True):
        assert pair[0].shape[2] == pair[1].shape[2] == 6
        for x,y in zip(pair,want,strict=True):
            torch.testing.assert_close(x,y,atol=3e-6,rtol=2e-5)
    assert torch.isfinite(full.logits).all() and not torch.count_nonzero(full.logits[~valid])


def test_active_real_cache_history_ALL_parameter_gradients_match_full():
    full,chunked = active(),active()
    ids = torch.tensor([[2,11,12,13,14,3],[2,21,22,23,24,3]])
    valid = torch.tensor([[1,0,1,1,0,1],[0,0,0,0,0,0]],dtype=torch.bool)
    a = full(ids,attention_mask=valid).logits[:,3:]
    prefix = chunked(ids[:,:3],attention_mask=valid[:,:3],use_cache=True)
    b = chunked(ids[:,3:],attention_mask=valid[:,3:],cache=prefix.cache).logits
    a.square().sum().backward()
    b.square().sum().backward()
    for (n,p),(other,q) in zip(full.named_parameters(),chunked.named_parameters(),strict=True):
        assert n == other and p.grad is not None and torch.isfinite(p.grad).all()
        torch.testing.assert_close(p.grad,q.grad,atol=3e-6,rtol=4e-5,msg=n)


def test_ALL_new_vectors_receive_real_gradients_when_active_and_fast_path_matches():
    m = active()
    ids = torch.tensor([[2,11,12,13,3],[2,21,22,23,3]])
    torch.testing.assert_close(m(ids).logits,m(ids,training_fast_path=True).logits,atol=2e-6,rtol=2e-5)
    m(ids,labels=ids).loss.backward()
    for n,p in m.named_parameters():
        assert p.grad is not None and torch.isfinite(p.grad).all(),n
        if extra_parameter(n): assert p.grad.abs().sum() > 0,n


@pytest.mark.parametrize('bad',['native','arm','runtime','shape','nan','positions'])
def test_foreign_or_corrupt_cache_refused_before_mutation(bad):
    m = active()
    ids = torch.tensor([[2,11,12]])
    cache = m(ids,use_cache=True).cache
    if bad == 'native': cache = native()(ids,use_cache=True).cache
    elif bad == 'arm': cache.arm = 'disabled_zero'
    elif bad == 'runtime': cache.implementation = 'native'
    elif bad == 'shape': cache.real[0] = (cache.real[0][0][:,:,:1],cache.real[0][1])
    elif bad == 'nan': cache.real[0][0][0,0,0,0] = torch.nan
    else: cache.positions[0,0] = 99
    before = copy.deepcopy(m.state_dict())
    with pytest.raises(ValueError): m(ids[:,:1],cache=cache)
    assert equal_state(before,m.state_dict())


@pytest.mark.parametrize('bad',['native','arm','nan','tie','disabled_beta','count','policy'])
def test_strict_config_and_state_refused_before_mutation(bad):
    m = Model.from_native(native(),'disabled_zero')
    before = copy.deepcopy(m.state_dict())
    state = copy.deepcopy(before)
    if bad in ('count','policy'):
        c = copy.deepcopy(m.config)
        if bad == 'count': c['expected_parameter_count'] += 1
        else: c[TAG]['policy']['activation'] = 'sigmoid'
        with pytest.raises(ValueError): Model(c)
    else:
        if bad == 'native': del state['rescale_runtime']
        elif bad == 'arm': state['rescale_runtime'][1] = 0
        elif bad == 'nan': state['model.norm.rescale_alpha'][0] = torch.nan
        elif bad == 'tie': state['lm_head.weight'] = state['lm_head.weight'].clone()+1
        else: state['model.norm.rescale_beta'][0] = .1
        with pytest.raises(ValueError): m.load_state_dict(state)
    assert equal_state(before,m.state_dict())
    m.load_state_dict(before)


def test_native_helper_export_foreign_cache_context_and_labels_refused():
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
    from natural_context_contrast_trainer import right_padded_hidden
    m = active()
    ids = torch.tensor([[2,11,12,3]])
    with pytest.raises(ValueError,match='model-owned'): right_padded_hidden(m,ids)
    with pytest.raises(AttributeError): native()(ids[:,:1],cache=m(ids,use_cache=True).cache)
    with pytest.raises(ValueError): m.hf_reference()
    with pytest.raises(ValueError): m.save('unused')
    with pytest.raises(ValueError): Model.load('unused')
    with pytest.raises(ValueError): m(torch.ones(1,1025,dtype=torch.long),training_fast_path=True)
    with pytest.raises(ValueError): m(ids,attention_mask=torch.ones_like(ids),training_fast_path=True)
    with pytest.raises(ValueError): m(ids,labels=torch.full_like(ids,-100))
