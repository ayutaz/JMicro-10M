"""Independent gate derivatives, native conversion, causal/cache/state checks."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
from base_headwise_gate_model import (ARMS, POLICY, TAG, HeadwiseGatedAttention,
    HeadwiseGateModel, gated_config, model_from_config, native_config)
from jmicro.model import Attention, JMicroModel
from jmicro.phase5 import equal_state
from natural_context_contrast_trainer import host
from test_natural_context_contrast_corpus import parent


def original():
    config = copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        config['expected_parameter_count'] = sum(p.numel() for p in JMicroModel(config).parameters())
    torch.manual_seed(42)
    return JMicroModel(config)


def test_independent_sigmoid_gate_forward_and_analytical_gradient():
    native = original().double().model.layers[0].self_attn
    gated = HeadwiseGatedAttention(copy.deepcopy(native), 'query_headwise')
    h = gated.q_proj.in_features
    x = torch.arange(1,h+1,dtype=torch.float64).view(1,h)/10
    x[:,1::2] *= -1
    # A length-one query has softmax weight one independent of Q/K and RoPE.
    h, heads, dim = x.shape[-1], gated.qheads, gated.dim
    assert h == heads * dim
    with torch.no_grad():
        gated.gate_proj.weight.copy_(torch.arange(heads*h).view(heads,h).double()/30)
    v = (x @ gated.v_proj.weight.detach().T).view(1,1,gated.kvheads,dim)
    v = v.repeat_interleave(heads//gated.kvheads,dim=2)
    scores = x @ gated.gate_proj.weight.detach().T
    sig = 1/(1+torch.exp(-scores))
    expected = (v*sig.view(1,1,heads,1)).flatten(2) @ gated.o_proj.weight.detach().T
    actual, _ = gated(x[:,None],torch.zeros((1,1),dtype=torch.long),None,None,causal=True)
    torch.testing.assert_close(actual, expected, atol=1e-14, rtol=1e-14)
    actual.sum().backward()
    d_output = torch.ones_like(actual) @ gated.o_proj.weight.detach()
    d_gate = (d_output.view(1,1,heads,dim)*v).sum(-1).view(1,heads)*sig*(1-sig)
    expected_gradient = d_gate.T @ x
    torch.testing.assert_close(gated.gate_proj.weight.grad, expected_gradient, atol=1e-14, rtol=1e-14)
    assert gated.gate_proj.bias is None


@pytest.mark.parametrize('arm', ARMS)
def test_conversion_preserves_parent_full_fast_padded_logits_and_rng(arm):
    native = original().eval()
    before, rng = host(native.state_dict()), torch.get_rng_state().clone()
    gated = HeadwiseGateModel.from_native(native, arm)
    assert torch.equal(rng, torch.get_rng_state())
    assert equal_state(before, host(native.state_dict()))
    assert gated.lm_head.weight is gated.model.embed_tokens.weight
    ids = torch.tensor([[2,8,9,10,11],[2,9,10,0,0]])
    mask = ids.ne(0)
    assert torch.equal(native(ids, mask).logits, gated(ids, mask).logits)
    unpadded = ids[:1]
    assert torch.equal(native(unpadded, training_fast_path=True).logits,
                       gated(unpadded, training_fast_path=True).logits)
    state = gated.state_dict()
    for key, value in before.items():
        if key.endswith('self_attn.o_proj.weight'):
            assert torch.equal(state[key], value*2.)
        else:
            assert torch.equal(state[key], value)
    assert all(torch.count_nonzero(b.self_attn.gate_proj.weight)==0 for b in gated.model.layers)


def test_actual_10M_parameter_counts_without_learned_or_random_quality_claim():
    path = Path(__file__).resolve().parents[1]/'reports/phase6/base_relu_squared_proposal.json'
    config = json.loads(path.read_text())['variants']['SwiGLU']
    with torch.device('meta'):
        native = JMicroModel(config)
        a = model_from_config(gated_config(config, 'static_half'))
        b = model_from_config(gated_config(config, 'query_headwise'))
    assert sum(p.numel() for p in native.parameters()) == 10001152
    assert sum(p.numel() for p in a.parameters()) == sum(p.numel() for p in b.parameters()) == 10014464
    assert 10014464-10001152 == 13*256*4
    assert a.lm_head.weight is a.model.embed_tokens.weight


def test_static_control_zero_gate_gradients_query_gates_receive_original_CE():
    native = original()
    ids = torch.tensor([[2,8,9,10,11],[2,9,8,11,10]])
    norms = {}
    for arm in ARMS:
        model = HeadwiseGateModel.from_native(native, arm)
        parameters = list(model.parameters())
        optimizer = torch.optim.AdamW(parameters, lr=1e-5, weight_decay=.1)
        assert len({id(p) for p in parameters}) == len(parameters)
        assert parameters == optimizer.param_groups[0]['params']
        logits = model(ids, training_fast_path=True).logits
        F.cross_entropy(logits[:,:-1].reshape(-1,logits.shape[-1]),ids[:,1:].flatten()).backward()
        gradients = [b.self_attn.gate_proj.weight.grad for b in model.model.layers]
        assert all(g is not None and torch.isfinite(g).all() for g in gradients)
        norms[arm] = sum(float(g.norm()) for g in gradients)
        optimizer.step()
        if arm == 'static_half':
            assert all(torch.count_nonzero(b.self_attn.gate_proj.weight)==0 for b in model.model.layers)
    assert norms['static_half'] == 0 and norms['query_headwise'] > 0


@pytest.mark.parametrize('arm', ARMS)
def test_nonzero_query_gates_causal_future_isolation_padding_and_chunk_cache(arm):
    model = HeadwiseGateModel.from_native(original().double(), arm).eval()
    with torch.no_grad():
        for b in model.model.layers:
            b.self_attn.gate_proj.weight.normal_(0,.2)
    ids = torch.tensor([[2,8,9,10,11]])
    full = model(ids, use_cache=True)
    changed = ids.clone();changed[:,3:] = torch.tensor([12,13])
    assert torch.equal(full.logits[:,:3],model(changed).logits[:,:3])
    prefill = model(ids[:,:2],use_cache=True)
    tail = model(ids[:,2:],cache=prefill.cache,use_cache=True)
    torch.testing.assert_close(tail.logits,full.logits[:,2:],atol=1e-12,rtol=1e-12)
    for a,b in zip(tail.cache.layers, full.cache.layers):
        for av,bv in zip(a,b):
            torch.testing.assert_close(av,bv,atol=1e-12,rtol=1e-12)
    padded = torch.cat((ids,torch.zeros((1,2),dtype=torch.long)),dim=1)
    logits = model(padded,attention_mask=padded.ne(0)).logits
    assert torch.equal(logits[:,:5],full.logits)
    assert torch.count_nonzero(logits[:,5:]) == 0
    torch.testing.assert_close(model(ids,training_fast_path=True).logits,full.logits,atol=1e-12,rtol=1e-12)


def test_matched_initial_gradient_and_after_learning_gate_effect():
    native = original().double()
    a,b = [HeadwiseGateModel.from_native(native,arm) for arm in ARMS]
    ids = torch.tensor([[2,8,9,10,11]])
    for model in (a,b):
        logits = model(ids,training_fast_path=True).logits
        logits.square().sum().backward()
    for (name,p),(other,q) in zip(a.named_parameters(),b.named_parameters()):
        assert name == other
        if 'gate_proj' not in name:
            assert torch.equal(p.grad,q.grad)
    with torch.no_grad():
        for model in (a,b):
            for block in model.model.layers:
                block.self_attn.gate_proj.weight.fill_(.3)
    assert not torch.equal(a(ids).logits,b(ids).logits)


def test_full_tagged_model_and_adam_state_continuous_vs_saved_resume(tmp_path):
    native = original()
    first = HeadwiseGateModel.from_native(native,'query_headwise')
    resumed = model_from_config(first.config)
    resumed.load_state_dict(first.state_dict(),strict=True)
    opt = torch.optim.AdamW(first.parameters(),lr=1e-5,weight_decay=.1)
    ropt = torch.optim.AdamW(resumed.parameters(),lr=1e-5,weight_decay=.1)
    ids = torch.tensor([[2,8,9,10,11],[2,9,8,11,10]])
    def step(model,optimizer):
        optimizer.zero_grad(set_to_none=True)
        logits = model(ids,training_fast_path=True).logits
        loss = F.cross_entropy(logits[:,:-1].reshape(-1,logits.shape[-1]),ids[:,1:].flatten())
        loss.backward();optimizer.step();return float(loss.detach())
    for _ in range(2):
        assert step(first,opt)==step(resumed,ropt)
    path = tmp_path/'gate-model-state.pt'
    torch.save(dict(config=resumed.config,model=host(resumed.state_dict()),optimizer=host(ropt.state_dict())),path)
    saved = torch.load(path,weights_only=False)
    resumed = model_from_config(saved['config']);resumed.load_state_dict(saved['model'],strict=True)
    ropt = torch.optim.AdamW(resumed.parameters(),lr=1e-5,weight_decay=.1);ropt.load_state_dict(saved['optimizer'])
    for _ in range(2):
        assert step(first,opt)==step(resumed,ropt)
    assert equal_state(host(first.state_dict()),host(resumed.state_dict()))
    assert equal_state(host(opt.state_dict()),host(ropt.state_dict()))
    # This checks model/Adam tensors only; full scientific sampler/RNG/scheduler
    # verification still requires the owned trainer/probe before science.


@pytest.mark.parametrize('mutation', ('kind','arm','count','foreign'))
def test_changed_policy_arm_count_and_foreign_architecture_refused(mutation):
    config = gated_config(original().config,'query_headwise')
    assert native_config(config)==original().config
    if mutation=='kind':config[TAG]['policy']['kind']='other'
    elif mutation=='arm':config[TAG]['arm']='elementwise'
    elif mutation=='count':config['expected_parameter_count']+=1
    else:config['ffn_research']={}
    with pytest.raises(ValueError):model_from_config(config)


def test_wrong_native_count_nonfinite_parent_repeated_conversion_and_stock_load_refused():
    native = original()
    wrong = copy.deepcopy(native);wrong.config['expected_parameter_count']+=1
    with pytest.raises(ValueError):HeadwiseGateModel.from_native(wrong,'query_headwise')
    broken = copy.deepcopy(native)
    with torch.no_grad():broken.model.embed_tokens.weight[0,0]=float('nan')
    with pytest.raises(ValueError):HeadwiseGateModel.from_native(broken,'query_headwise')
    huge = copy.deepcopy(native)
    with torch.no_grad():
        huge.model.layers[0].self_attn.o_proj.weight[0,0]=torch.finfo(torch.float32).max*.75
    with pytest.raises(ValueError):HeadwiseGateModel.from_native(huge,'query_headwise')
    gated = HeadwiseGateModel.from_native(native,'query_headwise')
    with pytest.raises(ValueError):HeadwiseGateModel.from_native(gated,'query_headwise')
    with pytest.raises(RuntimeError):native.load_state_dict(gated.state_dict(),strict=True)
    with pytest.raises(ValueError):gated.hf_reference()
    with pytest.raises(ValueError):gated.save(Path('unused'))


def test_tagged_load_refuses_partial_untied_nonfinite_and_nonzero_static_gate_state():
    model = HeadwiseGateModel.from_native(original(),'static_half')
    for problem in ('partial','untied','nonfinite','static'):
        state = host(model.state_dict())
        if problem == 'partial':del state['model.layers.0.self_attn.q_proj.weight']
        elif problem == 'untied':state['lm_head.weight'][0,0]+=1
        elif problem == 'nonfinite':state['model.layers.0.self_attn.q_proj.weight'][0,0]=float('nan')
        else:state['model.layers.0.self_attn.gate_proj.weight'][0,0]=1
        before = host(model.state_dict())
        with pytest.raises(ValueError):model.load_state_dict(state,strict=True)
        assert equal_state(before,host(model.state_dict()))
    with pytest.raises(ValueError):model.load_state_dict(model.state_dict(),strict=False)
