"""CPU information-path/cache/state checks; no trained Japanese quality."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

from jmicro.causal_qkv import (TAG,CausalQKVModel,TemporalKVCache,added_parameters,
                               mix_lags,native_config,tagged_config)
from jmicro.model import JMicroModel,rope
from jmicro.phase5 import equal_state
from test_value_residual import native,config


def independent_lags(x,w,valid,past=None):
    """Simple per-row valid-token list, independent of vectorized gather plan."""
    result=torch.empty_like(x)
    histories=[]
    validity=[]
    for b in range(x.shape[0]):
        memory=[] if past is None else list(past[b])
        for t in range(x.shape[2]):
            z=x[b,:,t]
            if memory: z=z+w[...,0]*memory[-1]
            if len(memory)>1: z=z+w[...,1]*memory[-2]
            result[b,:,t]=z
            if valid[b,t]: memory.append(x[b,:,t])
        memory=memory[-2:]
        padded=[torch.zeros_like(x[b,:,0])]*(2-len(memory))+memory
        histories.append(torch.stack(padded,dim=1))
        validity.append([False]*(2-len(memory))+[True]*len(memory))
    return result,torch.stack(histories),torch.tensor(validity,dtype=torch.bool)


def active():
    model=CausalQKVModel.from_native(native())
    with torch.no_grad():
        for index,block in enumerate(model.model.layers):
            block.self_attn.q_lag[...,0]=.1*(index+1)
            block.self_attn.k_lag[...,1]=-.2
            block.self_attn.v_lag[...,0]=.3
            block.self_attn.v_lag[...,1]=-.1
    return model


def test_independent_channel_lag_formula_holes_chunk_history_and_gradients():
    torch.manual_seed(17)
    x=torch.randn(2,4,7,8,dtype=torch.float64,requires_grad=True)
    w=torch.randn(4,8,2,dtype=torch.float64,requires_grad=True)
    valid=torch.tensor([[0,1,0,1,1,0,1],[1,0,1,0,0,1,1]],dtype=torch.bool)
    actual,tail,tail_valid=mix_lags(x,w,valid)
    expected,h,v=independent_lags(x,w,valid)
    assert torch.equal(actual,expected) and torch.equal(tail,h) and torch.equal(tail_valid,v)
    first,history,hv=mix_lags(x[:,:,:3],w,valid[:,:3])
    last,last_h,last_v=mix_lags(x[:,:,3:],w,valid[:,3:],history,hv)
    assert torch.equal(actual,torch.cat((first,last),dim=2))
    assert torch.equal(tail,last_h) and torch.equal(tail_valid,last_v)
    actual.square().sum().backward()
    assert x.grad.abs().sum()>0 and torch.isfinite(x.grad).all()
    assert w.grad.abs().sum()>0 and torch.isfinite(w.grad).all()


def test_same_current_projection_different_prior_token_cannot_be_pointwise_readout():
    x=torch.zeros(1,4,2,8)
    y=x.clone()
    y[:,:,0]=1.
    w=torch.ones(4,8,2)
    valid=torch.ones(1,2,dtype=torch.bool)
    a=mix_lags(x,w,valid)[0][:,:,1]
    b=mix_lags(y,w,valid)[0][:,:,1]
    assert torch.equal(x[:,:,1],y[:,:,1]) and not torch.equal(a,b)


def test_whole_model_independent_attention_matrix_and_pre_RoPE_lag_order():
    model=active().double()
    ids=torch.tensor([[2,11,12,13,14]])
    valid=torch.ones_like(ids,dtype=torch.bool)
    positions=torch.arange(5)[None]
    x=model.model.embed_tokens(ids)
    for block in model.model.layers:
        a=block.self_attn
        h=block.input_layernorm(x)
        projections=[]
        for linear,heads,weights in ((a.q_proj,4,a.q_lag),(a.k_proj,2,a.k_lag),(a.v_proj,2,a.v_lag)):
            raw=linear(h).view(1,5,heads,8).transpose(1,2)
            projections.append(independent_lags(raw,weights,valid)[0])
        q=rope(a.q_norm(projections[0]),positions,a.theta)
        k=rope(a.k_norm(projections[1]),positions,a.theta)
        maps=(q@k.repeat_interleave(2,dim=1).transpose(-1,-2))*a.scale
        maps=maps.masked_fill(~torch.ones(5,5,dtype=torch.bool).tril(),-torch.inf).softmax(-1)
        values=maps@projections[2].repeat_interleave(2,dim=1)
        x=x+a.o_proj(values.transpose(1,2).reshape(1,5,32))
        x=x+block.mlp(block.post_attention_layernorm(x))
    expected=model.lm_head(model.model.norm(x)).float()
    assert torch.allclose(model(ids).logits,expected,atol=2e-7,rtol=2e-6)


def test_zero_conversion_original_weights_logits_gradients_RNG_and_tie_exact():
    original=native().train()
    before=torch.get_rng_state().clone()
    model=CausalQKVModel.from_native(original).train()
    assert torch.equal(before,torch.get_rng_state())
    assert model.lm_head.weight is model.model.embed_tokens.weight
    old=dict(original.named_parameters())
    new=dict(model.named_parameters())
    assert all(torch.equal(p,new[n]) and p.data_ptr()!=new[n].data_ptr() for n,p in old.items())
    assert sum(p.numel() for p in model.parameters())==sum(p.numel() for p in original.parameters())+added_parameters(config())
    ids=torch.tensor([[2,11,12,13,3],[2,31,32,33,3]])
    a,b=original(ids,labels=ids),model(ids,labels=ids)
    assert torch.equal(a.logits,b.logits) and torch.equal(a.loss,b.loss)
    a.loss.backward()
    b.loss.backward()
    assert all(torch.equal(p.grad,new[n].grad) for n,p in old.items())
    assert all(p.grad is not None and p.grad.abs().sum()>0 for n,p in new.items()
               if n.endswith(('.q_lag','.k_lag','.v_lag')))


@pytest.mark.parametrize('mask',[
    [[1,1,1,1,1,1,1,1],[1,1,1,1,1,0,0,0]],
    [[0,0,1,1,1,1,1,1],[1,0,1,0,1,1,0,1]],
    [[1,0,0,0,0,0,1,1],[0,0,0,0,0,0,1,1]],
])
def test_active_logical_lags_full_chunks_padding_holes_all_PAD_chunk_and_causality(mask):
    model=active()
    ids=torch.tensor([[2,11,12,13,14,15,16,3],[2,31,32,33,34,35,36,3]])
    valid=torch.tensor(mask,dtype=torch.bool)
    full=model(ids,attention_mask=valid,use_cache=True)
    assert type(full.cache) is TemporalKVCache
    cache=None
    chunks=[]
    for start,end in ((0,2),(2,6),(6,8)):
        result=model(ids[:,start:end],attention_mask=valid[:,start:end],cache=cache,use_cache=True)
        chunks.append(result.logits)
        cache=result.cache
    assert torch.allclose(full.logits,torch.cat(chunks,dim=1),atol=4e-7,rtol=3e-6)
    assert torch.equal(full.cache.raw_valid,cache.raw_valid)
    assert torch.equal(full.cache.positions,cache.positions)
    assert torch.equal(cache.raw_valid.sum(-1),valid.sum(-1).clamp_max(2))
    for (a,b),(c,d) in zip(full.cache.layers,cache.layers):
        assert a.shape[1]==b.shape[1]==2
        assert torch.allclose(a,c,atol=4e-7,rtol=3e-6)
        assert torch.allclose(b,d,atol=4e-7,rtol=3e-6)
    for a,b in zip(full.cache.raw_projections,cache.raw_projections):
        assert all(torch.allclose(c,d,atol=4e-7,rtol=3e-6) for c,d in zip(a,b))
    changed=ids.clone()
    changed[0,6:]=torch.tensor([98,99])
    other=model(changed,attention_mask=valid)
    assert torch.equal(full.logits[0,:6],other.logits[0,:6])
    assert torch.equal(full.logits[1],other.logits[1])


def test_training_fast_path_native_hidden_helper_and_labels_keep_active_lags():
    sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
    from natural_context_contrast_trainer import right_padded_hidden
    model=active()
    ids=torch.tensor([[2,11,12,13,3],[2,31,3,0,0]])
    valid=ids.ne(0)
    full=model(ids,attention_mask=valid).logits
    assert torch.allclose(model.lm_head(right_padded_hidden(model,ids))[valid],full[valid],atol=4e-7,rtol=3e-6)
    assert torch.allclose(model(ids[:1]).logits,model(ids[:1],training_fast_path=True).logits,atol=4e-7,rtol=3e-6)
    labels=ids.clone()
    labels[~valid]=-100
    a=model(ids,attention_mask=valid,labels=labels)
    assert torch.equal(a.loss,F.cross_entropy(a.logits[:,:-1].reshape(-1,128),labels[:,1:].reshape(-1),ignore_index=-100))


def test_technical_identity_three_Adam_steps_exact_original_gradients_weights_and_Adam():
    original=native().train()
    model=CausalQKVModel.from_native(original,'static_identity').train()
    opts=[torch.optim.AdamW(m.parameters(),lr=1e-5,weight_decay=.1) for m in (original,model)]
    ids=torch.tensor([[2,11,12,13,3]])
    for _ in range(3):
        for m,opt in zip((original,model),opts):
            opt.zero_grad(set_to_none=True)
            m(ids,labels=ids).loss.backward()
        new=dict(model.named_parameters())
        assert all(torch.equal(p.grad,new[n].grad) for n,p in original.named_parameters())
        assert torch.equal(torch.nn.utils.clip_grad_norm_(original.parameters(),1.),model.clip_grad_norm(1.))
        for opt in opts: opt.step()
        for n,p in original.named_parameters():
            assert torch.equal(p,new[n])
            assert equal_state(opts[0].state[p],opts[1].state[new[n]])
        assert all(torch.count_nonzero(p)==0 and torch.count_nonzero(p.grad)==0 for n,p in new.items()
                   if n.endswith(('.q_lag','.k_lag','.v_lag')))


@pytest.mark.parametrize('bad',['missing','nan','dtype','tie','static_nonzero'])
def test_strict_bad_state_rejected_before_mutation(bad):
    model=CausalQKVModel.from_native(native(),'static_identity' if bad=='static_nonzero' else 'lag_learned')
    before=copy.deepcopy(model.state_dict())
    state=copy.deepcopy(before)
    key='model.layers.0.self_attn.q_lag'
    if bad=='missing': del state[key]
    elif bad=='nan': state[key].fill_(float('nan'))
    elif bad=='dtype': state[key]=state[key].double()
    elif bad=='tie': state['lm_head.weight']=state['lm_head.weight'].clone()+.1
    else: state[key].fill_(.1)
    with pytest.raises(ValueError): model.load_state_dict(state)
    assert equal_state(before,model.state_dict())


@pytest.mark.parametrize('bad',['policy','count','arm','norm'])
def test_undeclared_tag_changes_refused(bad):
    c=tagged_config(config())
    if bad=='policy': c[TAG]['policy']['previous_lags']=[1,3]
    elif bad=='count': c['expected_parameter_count']+=1
    elif bad=='arm': c[TAG]['arm']='other'
    else: c['qk_norm_type']='rms_head_shared'
    with pytest.raises(ValueError): CausalQKVModel(c)


def test_native_cache_and_bad_raw_validity_refused():
    ids=torch.tensor([[2,11,12]])
    model=active()
    old=native()(ids,use_cache=True).cache
    with pytest.raises(ValueError): model(ids,cache=old)
    cache=model(ids,use_cache=True).cache
    cache.raw_valid[:]=False
    with pytest.raises(ValueError): model(ids,cache=cache)


def test_bad_raw_projection_tuple_refused():
    model=active()
    ids=torch.tensor([[2,11,12]])
    cache=model(ids,use_cache=True).cache
    cache.raw_projections[0]=cache.raw_projections[0][:2]
    with pytest.raises(ValueError): model(ids,cache=cache)


def test_scientific_clip_includes_lag_coordinates_and_refuses_nonfinite():
    model=active()
    original=model.model.layers[0].self_attn.q_proj.weight
    lag=model.model.layers[0].self_attn.q_lag
    original.grad=torch.zeros_like(original)
    original.grad[0,0]=4.
    lag.grad=torch.zeros_like(lag)
    lag.grad[0,0,0]=3.
    assert model.clip_grad_norm(1.).item()==5.
    assert lag.grad[0,0,0].item()==pytest.approx(3./(5.+1e-6),abs=1e-7)
    lag.grad[0,0,0]=float('nan')
    with pytest.raises(RuntimeError,match='non-finite'): model.clip_grad_norm(1.)


def test_masked_ID_changes_do_not_enter_valid_lags_or_outputs():
    model=active()
    ids=torch.tensor([[2,11,12,13,14,15]])
    valid=torch.tensor([[0,1,0,1,0,1]],dtype=torch.bool)
    changed=ids.clone()
    changed[~valid]=torch.tensor([99,98,97])
    a=model(ids,attention_mask=valid,use_cache=True)
    b=model(changed,attention_mask=valid,use_cache=True)
    assert torch.equal(a.logits,b.logits)
    assert equal_state(a.cache.raw_projections,b.cache.raw_projections)


def test_every_single_token_cached_decode_matches_full_active_model():
    model=active()
    ids=torch.tensor([[2,11,12,13,14,3]])
    full=model(ids,use_cache=True)
    cache=None
    outputs=[]
    for index in range(ids.shape[1]):
        out=model(ids[:,index:index+1],cache=cache,use_cache=True)
        cache=out.cache
        outputs.append(out.logits)
    assert torch.allclose(full.logits,torch.cat(outputs,dim=1),atol=4e-7,rtol=3e-6)
    assert all(torch.allclose(c,d,atol=4e-7,rtol=3e-6)
               for a,b in zip(full.cache.raw_projections,cache.raw_projections) for c,d in zip(a,b))


def test_actual_native13layer_meta_count_roundtrip_and_native_export_refusal(tmp_path):
    c=json.loads((Path(__file__).resolve().parents[1]/'reports/phase6/value-residual-science-20261015/training.json').read_text())['spec']['original_model_config']
    with torch.device('meta'):
        model=CausalQKVModel(tagged_config(c))
    assert sum(p.numel() for p in model.parameters())==10014464
    first=active()
    second=CausalQKVModel(copy.deepcopy(first.config))
    second.load_state_dict(first.state_dict())
    assert equal_state(first.state_dict(),second.state_dict())
    assert native_config(first.config)==config()
    for action in (first.hf_reference,lambda:first.save(tmp_path),lambda:CausalQKVModel.load(tmp_path)):
        with pytest.raises(ValueError): action()
