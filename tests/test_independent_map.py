"""Independent dense oracle, novel information path and typed real-K2 cache."""
import copy
import json
import math
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

from jmicro.independent_map import (TAG, ARMS, IndependentMapModel as Model,
    IndependentMapCache, added_parameters, extra_parameter, independent_map_attention,
    native_config, tagged_config)
from jmicro.model import JMicroModel, rope
from jmicro.phase5 import equal_state
from test_value_residual import native, config


def active():
    model = Model.from_native(native())
    with torch.no_grad():
        for layer in model.model.layers:
            layer.self_attn.independent_raw.copy_(torch.tensor([.4,-.2,.3,-.5]))
    return model


def dense(q,k,v,mask,scale):
    return ((q@k.transpose(-1,-2))*scale).masked_fill(~mask,-torch.inf).softmax(-1)@v


def test_dense_two_map_values_and_all_QKV_independent_QK_coefficient_gradients():
    torch.manual_seed(8)
    tensors = [torch.randn(2,4,7,8,dtype=torch.float64,requires_grad=True) for _ in range(5)]
    q,k,v,q2,k2 = tensors
    raw = torch.tensor([-.4,.2,.7,-.8],dtype=torch.float64,requires_grad=True)
    actual = independent_map_attention(*tensors,raw,causal=True,scale=.3)
    mask = torch.ones(7,7,dtype=torch.bool).tril()
    expected = dense(q,k,v,mask,.3)-raw.tanh()[None,:,None,None]*dense(q2,k2,v,mask,.3)
    torch.testing.assert_close(actual,expected,atol=1e-14,rtol=1e-13)
    weight = torch.linspace(-1,2,actual.numel(),dtype=torch.float64).reshape_as(actual)
    a = torch.autograd.grad((actual*weight).sum(),(*tensors,raw),retain_graph=True)
    b = torch.autograd.grad((expected*weight).sum(),(*tensors,raw))
    for x,y in zip(a,b,strict=True):
        torch.testing.assert_close(x,y,atol=1e-13,rtol=1e-12)


def test_independent_basis_emits_signal_unavailable_to_native_head_permutation_or_output_scaling():
    from jmicro.cross_gqa_map import cross_map_attention
    q = torch.zeros(1,4,1,1,dtype=torch.float64)
    k = torch.zeros(1,4,2,1,dtype=torch.float64)
    v = torch.zeros_like(k)
    v[:,:,0],v[:,:,1] = 1.,-1.
    raw = torch.full((4,),math.atanh(.5),dtype=torch.float64)
    assert torch.count_nonzero(cross_map_attention(q,k,v,raw,scale=1.)) == 0
    q2,k2 = torch.ones_like(q),k.clone()
    k2[:,:,0],k2[:,:,1] = math.log(9)/2,-math.log(9)/2
    out = independent_map_attention(q,k,v,q2,k2,raw,scale=1.)
    torch.testing.assert_close(out,torch.full_like(out,-.4),atol=1e-14,rtol=0)


def test_zero_coefficient_original_value_and_original_gradients_exact_new_coefficient_active():
    torch.manual_seed(3)
    q,k,v,q2,k2 = [torch.randn(1,4,5,8,dtype=torch.float64,requires_grad=True) for _ in range(5)]
    raw = torch.zeros(4,dtype=torch.float64,requires_grad=True)
    standard = F.scaled_dot_product_attention(q,k,v,is_causal=True)
    expected = torch.autograd.grad(standard.square().sum(),(q,k,v))
    actual = independent_map_attention(q,k,v,q2,k2,raw,causal=True)
    actual.square().sum().backward()
    assert torch.equal(actual,standard)
    assert all(torch.equal(x.grad,y) for x,y in zip((q,k,v),expected,strict=True))
    assert raw.grad.abs().sum() > 0 and torch.count_nonzero(q2.grad) == torch.count_nonzero(k2.grad) == 0


@pytest.mark.parametrize('arm',ARMS)
def test_original_tensors_function_tie_RNG_and_real_count_conversion(arm):
    original = native()
    before = copy.deepcopy(original.state_dict())
    rng = torch.get_rng_state().clone()
    model = Model.from_native(original,arm)
    assert torch.equal(rng,torch.get_rng_state()) and not torch.cuda.is_initialized()
    assert equal_state(original.state_dict(),before)
    assert all(torch.equal(model.state_dict()[k],v) for k,v in before.items())
    assert model.lm_head.weight is model.model.embed_tokens.weight
    assert sum(p.numel() for p in model.parameters()) == sum(p.numel() for p in original.parameters())+added_parameters(original.config)
    assert native_config(model.config) == original.config
    ids = torch.tensor([[2,11,12,13,3]])
    assert torch.equal(original(ids).logits,model(ids).logits)
    assert torch.equal(original(ids,training_fast_path=True).logits,model(ids,training_fast_path=True).logits)
    extras = {n:p for n,p in model.named_parameters() if extra_parameter(n)}
    assert len(extras) == 4*original.config['num_hidden_layers']
    assert all(torch.count_nonzero(p) > 0 for n,p in extras.items() if not n.endswith('.independent_raw'))


def test_actual_meta_architecture_parameter_budget_and_config_roundtrip():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    with torch.device('meta'): model = Model(tagged_config(c))
    assert added_parameters(c) == 66612
    assert sum(p.numel() for p in model.parameters()) == 10067764
    assert 9500000 <= sum(p.numel() for p in model.parameters() if p.requires_grad) <= 10100000
    assert native_config(model.config) == c


@pytest.mark.parametrize('mask',[
    [[1,1,1,1,1,1],[1,1,1,0,0,0]],
    [[0,0,1,1,1,1],[1,0,1,0,1,1]],
    [[0,0,0,0,0,0],[0,1,0,1,0,1]],
])
def test_active_real_K2_cache_padding_holes_allPAD_and_no_past_recomputation(mask):
    model = active()
    ids = torch.tensor([[2,11,12,13,14,3],[2,21,22,23,24,3]])
    valid = torch.tensor(mask,dtype=torch.bool)
    full = model(ids,attention_mask=valid,use_cache=True)
    prefix = model(ids[:,:3],attention_mask=valid[:,:3],use_cache=True)
    observed = []
    handle = model.model.embed_tokens.register_forward_pre_hook(lambda _,args: observed.append(args[0].shape[1]))
    try: suffix = model(ids[:,3:],attention_mask=valid[:,3:],cache=prefix.cache,use_cache=True)
    finally: handle.remove()
    assert observed == [3]
    torch.testing.assert_close(torch.cat((prefix.logits,suffix.logits),1),full.logits,atol=3e-6,rtol=2e-5)
    cache = suffix.cache
    assert type(cache) is IndependentMapCache and not hasattr(cache,'layers')
    assert torch.equal(cache.valid,valid) and torch.equal(cache.positions,full.cache.positions)
    for pair,k2,want in zip(cache.primary,cache.secondary,full.cache.secondary,strict=True):
        assert pair[0].shape[2] == pair[1].shape[2] == k2.shape[2] == 6
        torch.testing.assert_close(k2,want,atol=3e-6,rtol=2e-5)
    assert torch.isfinite(full.logits).all() and torch.count_nonzero(full.logits[~valid]) == 0


def test_cache_history_all_parameter_gradients_match_full_and_allPAD_backward_finite():
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


def test_all_new_projection_paths_and_raw_get_real_gradients_after_coefficient_moves():
    model = active().train()
    ids = torch.tensor([[2,11,12,13,3],[2,21,22,23,3]])
    model(ids,labels=ids).loss.backward()
    for n,p in model.named_parameters():
        assert p.grad is not None and torch.isfinite(p.grad).all(),n
        if extra_parameter(n): assert p.grad.abs().sum() > 0,n


def test_independent_whole_model_dense_oracle_all_values_and_parameter_gradients():
    model = active()
    oracle = copy.deepcopy(model)
    ids = torch.tensor([[2,11,12,13,3]])
    batch,length = ids.shape
    positions = torch.arange(length)[None]
    mask = torch.ones(length,length,dtype=torch.bool).tril()
    x = oracle.model.embed_tokens(ids)
    for block in oracle.model.layers:
        a = block.self_attn
        z = block.input_layernorm(x)
        project = lambda m,source,h: m(source).view(batch,length,h,8).transpose(1,2)
        q,k = [rope(project(m,z,h),positions,a.theta) for m,h in ((a.q_proj,4),(a.k_proj,2))]
        v = project(a.v_proj,z,2).repeat_interleave(2,1)
        u = a.independent_down(z)
        q2,k2 = [rope(project(m,u,h),positions,a.theta) for m,h in ((a.independent_q,4),(a.independent_k,2))]
        value = dense(q,k.repeat_interleave(2,1),v,mask,a.scale)-a.independent_raw.tanh()[None,:,None,None]*dense(q2,k2.repeat_interleave(2,1),v,mask,a.scale)
        x = x+a.o_proj(value.transpose(1,2).reshape(batch,length,32))
        x = x+block.mlp(block.post_attention_layernorm(x))
    expected = oracle.lm_head(oracle.model.norm(x)).float()
    actual = model(ids).logits
    torch.testing.assert_close(actual,expected,atol=2e-6,rtol=2e-5)
    actual.square().sum().backward()
    expected.square().sum().backward()
    for (n,p),(other,q) in zip(model.named_parameters(),oracle.named_parameters(),strict=True):
        assert n == other
        torch.testing.assert_close(p.grad,q.grad,atol=3e-6,rtol=4e-5,msg=n)


@pytest.mark.parametrize('bad',['native','runtime','K2_shape','K2_nan','positions','arm'])
def test_foreign_or_corrupt_cache_refused_before_input_state_mutation(bad):
    model = active()
    ids = torch.tensor([[2,11,12]])
    cache = model(ids,use_cache=True).cache
    if bad == 'native': cache = native()(ids,use_cache=True).cache
    elif bad == 'runtime': cache.implementation = 'wrong'
    elif bad == 'K2_shape': cache.secondary[0] = cache.secondary[0][:,:,:1]
    elif bad == 'K2_nan': cache.secondary[0][0,0,0,0] = torch.nan
    elif bad == 'positions': cache.positions[0,0] = 99
    else: cache.arm = 'disabled_zero'
    before = copy.deepcopy(model.state_dict())
    with pytest.raises(ValueError): model(ids[:,:1],cache=cache)
    assert equal_state(before,model.state_dict())


def test_native_helpers_and_export_cannot_drop_independent_map_or_K2():
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
    from natural_context_contrast_trainer import right_padded_hidden
    model = active()
    ids = torch.tensor([[2,11,12,3]])
    with pytest.raises(ValueError,match='model-owned'): right_padded_hidden(model,ids)
    with pytest.raises(AttributeError): native()(ids[:,:1],cache=model(ids,use_cache=True).cache)
    with pytest.raises(ValueError): model.hf_reference()
    with pytest.raises(ValueError): model.save('unused')
    with pytest.raises(ValueError): Model.load('unused')


@pytest.mark.parametrize('bad',['policy','count','nativeQK','runtime','missing','nan','tie','static_nonzero'])
def test_strict_config_and_state_before_mutation(bad):
    model = Model.from_native(native(),'disabled_zero')
    state = copy.deepcopy(model.state_dict())
    if bad in ('policy','count','nativeQK','runtime'):
        c = copy.deepcopy(model.config)
        if bad == 'policy': c[TAG]['policy']['rank'] = 4
        elif bad == 'count': c['expected_parameter_count'] += 1
        elif bad == 'nativeQK': c['qk_norm_type'] = 'rms_head_shared'
        else: c[TAG]['implementation'] = 'wrong'
        with pytest.raises(ValueError): Model(c)
    else:
        badstate = copy.deepcopy(state)
        key = 'model.layers.0.self_attn.independent_raw'
        if bad == 'missing': del badstate[key]
        elif bad == 'nan': badstate[key][0] = torch.nan
        elif bad == 'tie': badstate['lm_head.weight'] = badstate['lm_head.weight'].clone()+1
        else: badstate[key][0] = 1
        with pytest.raises(ValueError): model.load_state_dict(badstate)
    assert equal_state(state,model.state_dict())
