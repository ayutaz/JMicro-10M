"""Independent analytic derivatives, native identity and information path."""
import copy
import json
from pathlib import Path

import pytest
import torch

from jmicro.model import JMicroModel,RMSNorm
from jmicro.self_rescaled_norm import (ARMS,SelfRescaledRMSNorm,added_parameters,
    extra_parameter,rescale)

torch.set_num_threads(2)


def test_independent_analytic_ALL_input_gamma_alpha_beta_derivatives():
    torch.manual_seed(51)
    x = torch.randn(2,3,7,dtype=torch.float64,requires_grad=True)
    gamma,alpha,beta = [torch.randn(7,dtype=torch.float64,requires_grad=True) for _ in range(3)]
    g = torch.randn_like(x)
    epsilon = 1e-6
    r = (x.square().mean(-1,keepdim=True)+epsilon).sqrt()
    u = x/r
    actual = rescale(u,x,gamma,alpha,beta)
    gradients = torch.autograd.grad((actual*g).sum(),(x,gamma,alpha,beta))
    # Independently derived complete Jacobian, including the original RMS
    # projection term and the extra raw-input dot product's derivative.
    t = (x.detach()*beta.detach()).sum(-1,keepdim=True).tanh()
    q = g*(gamma.detach()+alpha.detach()*t)
    dot = (g*u.detach()*alpha.detach()).sum(-1,keepdim=True)*(1-t.square())
    expected = (
        q/r.detach()-x.detach()*(q*x.detach()).sum(-1,keepdim=True)/(7*r.detach().pow(3))+dot*beta.detach(),
        (g*u.detach()).sum((0,1)),
        (g*u.detach()*t).sum((0,1)),
        (dot*x.detach()).sum((0,1)),
    )
    assert torch.isfinite(actual).all()
    for a,b in zip(gradients,expected,strict=True):
        torch.testing.assert_close(a,b,atol=3e-13,rtol=2e-12)


@pytest.mark.parametrize('dtype',[torch.float32,torch.bfloat16])
@pytest.mark.parametrize('arm',ARMS)
def test_zero_beta_native_function_original_gradients_tie_RNG_exact(dtype,arm):
    torch.manual_seed(6)
    original = RMSNorm(8,1e-6)
    original.weight.data.copy_(torch.linspace(.4,1.5,8))
    before = original.weight.detach().clone()
    rng = torch.get_rng_state().clone()
    current = SelfRescaledRMSNorm(copy.deepcopy(original),arm)
    assert torch.equal(torch.get_rng_state(),rng) and not torch.cuda.is_initialized()
    assert torch.equal(current.weight,before)
    a = torch.randn(2,4,8,dtype=dtype,requires_grad=True)
    b = a.detach().clone().requires_grad_()
    y,z = original(a),current.owned_forward(b)
    assert torch.equal(y,z)
    weight = torch.linspace(-1,2,y.numel()).reshape_as(y)
    (y*weight).sum().backward()
    (z*weight).sum().backward()
    assert torch.equal(a.grad,b.grad)
    assert torch.equal(original.weight.grad,current.weight.grad)
    assert torch.count_nonzero(current.rescale_alpha.grad) == 0
    if arm == 'self_rescaled':
        assert current.rescale_beta.grad.abs().sum() > 0
    else:
        assert torch.count_nonzero(current.rescale_beta.grad) == 0


def test_dynamic_norm_is_not_any_static_RMS_gain_exact_positive_epsilon_counterexample():
    original = RMSNorm(2,1e-6)
    current = SelfRescaledRMSNorm(copy.deepcopy(original))
    with torch.no_grad():
        current.rescale_alpha.copy_(torch.tensor([1.,2.]))
        current.rescale_beta.copy_(torch.tensor([1.,0.]))
    x = torch.tensor([[1.,1.]])
    # Any static diagonal RMS gain is odd, including the native epsilon.
    assert torch.equal(original(-x),-original(x))
    positive,negative = current.owned_forward(x),current.owned_forward(-x)
    assert not torch.allclose(negative,-positive)
    # Channel-dependent dynamic scale also changes direction, whereas a
    # token-wide scalar gain cannot turn equal coordinates into unequal ones.
    assert positive[0,0] != positive[0,1]
    assert (positive+negative).abs().sum() > 0


def test_both_new_vectors_active_after_beta_moves_and_native_gamma_still_learns():
    current = SelfRescaledRMSNorm(RMSNorm(8,1e-6))
    current.rescale_beta.data.copy_(torch.linspace(-.3,.3,8))
    x = torch.linspace(-2,3,64).reshape(2,4,8).requires_grad_()
    current.owned_forward(x).square().sum().backward()
    for p in (current.weight,current.rescale_alpha,current.rescale_beta):
        assert p.grad is not None and torch.isfinite(p.grad).all() and p.grad.abs().sum() > 0


def test_disabled_with_nonzero_beta_preserves_native_values_and_original_gradients():
    original = RMSNorm(8,1e-6)
    current = SelfRescaledRMSNorm(copy.deepcopy(original),'disabled_zero')
    current.rescale_beta.data.fill_(.25)
    current.rescale_alpha.data.copy_(torch.linspace(.3,1.5,8))
    a = torch.linspace(-2,3,64).reshape(2,4,8).requires_grad_()
    b = a.detach().clone().requires_grad_()
    y,z = original(a),current.owned_forward(b)
    assert torch.equal(y,z)
    y.square().sum().backward()
    z.square().sum().backward()
    assert torch.equal(a.grad,b.grad) and torch.equal(original.weight.grad,current.weight.grad)
    assert not torch.count_nonzero(current.rescale_alpha.grad)
    assert not torch.count_nonzero(current.rescale_beta.grad)


def test_full_meta_assembly_count_all27_sites_no_QK_norm_and_original_tied_names():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    with torch.device('meta'):
        model = JMicroModel(c)
        original_names = [n for n,_ in model.named_parameters()]
        norms = [(name,m) for name,m in model.named_modules() if type(m) is RMSNorm]
        assert len(norms) == 27
        assert all('.q_norm' not in n and '.k_norm' not in n for n,_ in norms)
        for name,norm in norms:
            parent,field = name.rsplit('.',1)
            setattr(model.get_submodule(parent),field,SelfRescaledRMSNorm(norm))
    assert added_parameters(c) == 13824
    assert sum(p.numel() for p in model.parameters()) == 10014976
    assert 9500000 <= sum(p.numel() for p in model.parameters() if p.requires_grad) <= 10100000
    assert [n for n,_ in model.named_parameters() if not extra_parameter(n)] == original_names
    assert len([n for n,_ in model.named_parameters() if extra_parameter(n)]) == 54
    assert model.lm_head.weight is model.model.embed_tokens.weight
    # Assembly is only a count proof: generic native execution is deliberately
    # unavailable until a tagged owned model/cache/trainer is implemented.


@pytest.mark.parametrize('value',[0.,1e-10,1.,10000.])
def test_zero_tiny_and_large_inputs_finite(value):
    m = SelfRescaledRMSNorm(RMSNorm(8,1e-6))
    m.rescale_beta.data.fill_(.2)
    x = torch.full((2,4,8),value,requires_grad=True)
    y = m.owned_forward(x)
    y.sum().backward()
    assert torch.isfinite(y).all() and torch.isfinite(x.grad).all()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in m.parameters())


def test_generic_norm_forward_refuses_untyped_native_traversal():
    m = SelfRescaledRMSNorm(RMSNorm(8,1e-6))
    with pytest.raises(ValueError,match='model-owned'):
        m(torch.ones(1,8))


@pytest.mark.parametrize('bad',['arm','unit_shape','beta_shape','parameter_dtype','integer'])
def test_invalid_mathematical_contract_refused(bad):
    raw = torch.ones(2,8)
    unit = raw.clone()
    gamma,alpha,beta = torch.ones(8),torch.ones(8),torch.zeros(8)
    arm = 'self_rescaled'
    if bad == 'arm': arm = 'native'
    elif bad == 'unit_shape': unit = unit[:,:4]
    elif bad == 'beta_shape': beta = beta[:4]
    elif bad == 'parameter_dtype': alpha = alpha.double()
    else: raw=raw.long(); unit=unit.long()
    with pytest.raises(ValueError): rescale(unit,raw,gamma,alpha,beta,arm)
