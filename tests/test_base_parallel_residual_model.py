"""Independent residual algebra, same physical matrices and native causal paths."""
import copy
from pathlib import Path
import sys
import pytest
import torch
from torch import nn
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_parallel_residual_model import (POLICY,TAG,FOREIGN_TAGS,ParallelResidualBlock,
    ParallelResidualModel,parallel_config,model_from_config)
from jmicro.model import Block,JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import parent


@pytest.fixture
def config():
    c=copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        c['expected_parameter_count']=sum(p.numel() for p in JMicroModel(c).parameters())
    return c


class TwiceAttention(nn.Module):
    def forward(self,x,positions,allowed,past,causal=False):
        return 2*x,past


class TripleFFN(nn.Module):
    def forward(self,x):return 3*x


def test_independent_block_algebra_and_cache(config):
    native=Block(config)
    native.self_attn=TwiceAttention();native.mlp=TripleFFN()
    native.input_layernorm=nn.Identity();native.post_attention_layernorm=nn.Identity()
    parallel=ParallelResidualBlock(native)
    x=torch.tensor([[[2.,-3.]]],requires_grad=True);past=object()
    output,cache=parallel(x,None,None,past)
    assert torch.equal(output,6*x) and cache is past
    assert torch.equal(native(x,None,None,past)[0],12*x)
    output.sum().backward();assert torch.equal(x.grad,torch.full_like(x,6.))


def test_initial_matrices_order_rng_tie_and_count(config):
    native=JMicroModel(config);original=copy.deepcopy(native.state_dict())
    rng=torch.get_rng_state();names=[n for n,_ in native.named_parameters()]
    parallel=ParallelResidualModel.from_native_fresh(native)
    assert torch.equal(rng,torch.get_rng_state())
    assert equal_state(original,parallel.state_dict())
    assert names==[n for n,_ in parallel.named_parameters()]
    assert sum(p.numel() for p in parallel.parameters())==config['expected_parameter_count']
    assert parallel.lm_head.weight is parallel.model.embed_tokens.weight
    assert all(type(b) is ParallelResidualBlock for b in parallel.model.layers)


def test_full_fast_causal_padding_and_chunk_cache(config):
    model=ParallelResidualModel(parallel_config(config)).eval()
    ids=torch.tensor([[2,8,9,10,11,12]])
    full=model(ids).logits
    torch.testing.assert_close(full,model(ids,training_fast_path=True).logits,atol=1e-6,rtol=1e-6)
    changed=ids.clone();changed[0,-1]=13
    torch.testing.assert_close(full[:,:-1],model(changed).logits[:,:-1],atol=1e-6,rtol=1e-6)
    padded=torch.tensor([[0,0,2,8,9,10,11,12]])
    out=model(padded,attention_mask=padded.ne(0)).logits
    torch.testing.assert_close(full,out[:,2:],atol=1e-6,rtol=1e-6)
    assert torch.count_nonzero(out[:,:2])==0
    prefix=model(ids[:,:2],use_cache=True)
    middle=model(ids[:,2:4],cache=prefix.cache,use_cache=True)
    end=model(ids[:,4:],cache=middle.cache,use_cache=True)
    torch.testing.assert_close(full,torch.cat([prefix.logits,middle.logits,end.logits],dim=1),atol=1e-6,rtol=1e-6)


def test_tagged_roundtrip_finite_backward_and_refused_stock_export(config,tmp_path):
    model=ParallelResidualModel(parallel_config(config));ids=torch.tensor([[2,8,9,10]])
    labels=ids.clone();labels[:,0]=-100
    out=model(ids,labels=labels);assert torch.isfinite(out.loss)
    out.loss.backward()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())
    restored=model_from_config(copy.deepcopy(model.config));restored.load_state_dict(model.state_dict(),strict=True)
    torch.testing.assert_close(out.logits,restored(ids).logits,atol=0,rtol=0)
    with pytest.raises(ValueError):model.hf_reference()
    with pytest.raises(ValueError):model.save(tmp_path/'export')


@pytest.mark.parametrize('foreign',FOREIGN_TAGS)
def test_foreign_architecture_refused(config,foreign):
    bad=copy.deepcopy(config);bad[foreign]={}
    with pytest.raises(ValueError):parallel_config(bad)
    with pytest.raises(ValueError):model_from_config(bad)


def test_changed_recipe_and_grad_scaffold_refused(config):
    bad=parallel_config(config);bad[TAG]['policy']['residual_gain']=.5
    with pytest.raises(ValueError):model_from_config(bad)
    native=JMicroModel(config);next(native.parameters()).grad=torch.ones_like(next(native.parameters()))
    with pytest.raises(ValueError):ParallelResidualModel.from_native_fresh(native)


def test_meta_actual_count_same(config):
    with torch.device('meta'):
        native=model_from_config(config);parallel=model_from_config(parallel_config(config))
    assert [p.shape for p in native.parameters()]==[p.shape for p in parallel.parameters()]
    assert sum(p.numel() for p in parallel.parameters())==config['expected_parameter_count']
