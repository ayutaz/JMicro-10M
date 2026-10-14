"""New CPU evidence for an implementation comparison; not a probe rerun."""
import copy

import pytest
import torch

from jmicro.causal_qkv import CausalQKVModel,mix_lags
from jmicro.causal_qkv_contiguous import ContiguousCausalQKVModel,contiguous_lags
from jmicro.phase5 import equal_state
from test_causal_qkv import active
from test_value_residual import native


@pytest.mark.parametrize('length',[1,2,3,64])
@pytest.mark.parametrize('dtype',[torch.float32,torch.float64])
def test_values_history_AND_all_gradients_exact_for_contiguous_precondition(length,dtype):
    torch.manual_seed(11)
    x=torch.randn(2,4,length,8,dtype=dtype,requires_grad=True)
    w=torch.randn(4,8,2,dtype=dtype,requires_grad=True)
    y=x.detach().clone().requires_grad_()
    u=w.detach().clone().requires_grad_()
    old,old_tail,old_valid=mix_lags(x,w,torch.ones(2,length,dtype=torch.bool))
    new,new_tail,new_valid=contiguous_lags(y,u)
    assert torch.equal(old,new) and torch.equal(old_tail,new_tail) and torch.equal(old_valid,new_valid)
    old.square().sum().backward()
    new.square().sum().backward()
    assert torch.equal(x.grad,y.grad) and torch.equal(w.grad,u.grad)


def pair():
    reference=active().train()
    model=ContiguousCausalQKVModel(copy.deepcopy(reference.config)).train()
    model.load_state_dict(reference.state_dict())
    return reference,model


def test_full_model_active_fast_logits_gradients_and3_Adam_updates_exact():
    reference,model=pair()
    ids=torch.tensor([[2,11,12,13,14,3],[2,31,32,33,3,0]])
    targets=ids.clone()
    targets[ids==0]=-100
    opts=[torch.optim.AdamW(m.parameters(),lr=1e-5,weight_decay=.1) for m in (reference,model)]
    for _ in range(3):
        losses=[]
        for m,opt in zip((reference,model),opts):
            opt.zero_grad(set_to_none=True)
            logits=m(ids,training_fast_path=True).logits
            loss=torch.nn.functional.cross_entropy(logits[:,:-1].reshape(-1,128),targets[:,1:].reshape(-1),ignore_index=-100)
            losses.append(loss.detach())
            loss.backward()
        assert torch.equal(losses[0],losses[1])
        assert all(torch.equal(a.grad,b.grad) for a,b in zip(reference.parameters(),model.parameters(),strict=True))
        assert torch.equal(reference.clip_grad_norm(1.),model.clip_grad_norm(1.))
        for opt in opts: opt.step()
        assert equal_state(reference.state_dict(),model.state_dict())
        assert equal_state(opts[0].state_dict(),opts[1].state_dict())


def test_masked_and_chunked_calls_keep_exact_reference_logits_and_full_raw_cache():
    reference,model=pair()
    ids=torch.tensor([[2,11,12,13,14,3],[2,31,32,33,34,3]])
    valid=torch.tensor([[0,1,0,1,1,1],[1,1,0,0,1,1]],dtype=torch.bool)
    for m in (reference,model): m.eval()
    cache_a=cache_b=None
    for start,end in ((0,2),(2,4),(4,6)):
        a=reference(ids[:,start:end],attention_mask=valid[:,start:end],cache=cache_a,use_cache=True)
        b=model(ids[:,start:end],attention_mask=valid[:,start:end],cache=cache_b,use_cache=True)
        assert torch.equal(a.logits,b.logits)
        assert equal_state(a.cache.layers,b.cache.layers)
        assert equal_state(a.cache.raw_projections,b.cache.raw_projections)
        assert torch.equal(a.cache.raw_valid,b.cache.raw_valid)
        cache_a,cache_b=a.cache,b.cache


def test_zero_conversion_state_topology_tie_and_RNG_unchanged():
    old=native()
    reference=CausalQKVModel.from_native(old)
    rng=torch.get_rng_state().clone()
    model=ContiguousCausalQKVModel.from_native(old)
    assert torch.equal(rng,torch.get_rng_state())
    assert equal_state(reference.state_dict(),model.state_dict())
    assert list(dict(reference.named_parameters()))==list(dict(model.named_parameters()))
    assert model.lm_head.weight is model.model.embed_tokens.weight
    assert sum(p.numel() for p in reference.parameters())==sum(p.numel() for p in model.parameters())
    ids=torch.tensor([[2,11,12,3]])
    assert torch.equal(old(ids).logits,model(ids).logits)
