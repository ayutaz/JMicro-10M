"""Independent probability/gradient oracles for both non-detached views."""
import json
from pathlib import Path
import sys

import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from jmicro.rdrop import two_view_objective
from jmicro.model import JMicroModel
from jmicro.training import rng_state
from jmicro.phase5 import equal_state
from base_residual_dropout import install_training_dropout
from natural_context_contrast_trainer import host


def sample():
    return torch.tensor([[1.2,-.7,.4],[.3,.8,-.2]],requires_grad=True),torch.tensor([[-.2,.6,1.],[.7,-.3,.1]],requires_grad=True),torch.tensor([2,0])


def test_value_matches_independent_double_precision_probability_formula():
    a,b,y = sample()
    result = two_view_objective(a,b,y)
    p,q = a.double().softmax(-1),b.double().softmax(-1)
    ce = -.5*(p[torch.arange(2),y].log()+q[torch.arange(2),y].log()).mean()
    symmetric = .5*(p*(p/q).log()+q*(q/p).log()).sum(-1).mean()
    assert torch.allclose(result['CE_loss'].double(),ce,atol=1e-7,rtol=1e-7)
    assert torch.allclose(result['symmetric_KL'].double(),symmetric,atol=1e-7,rtol=1e-7)
    assert torch.allclose(result['combined_loss'].double(),ce+.5*symmetric,atol=1e-7,rtol=1e-7)


def test_BOTH_view_gradients_match_closed_form_Jeffreys_derivatives():
    a,b,y = sample()
    p,q = a.detach().double().softmax(-1),b.detach().double().softmax(-1)
    d = p.log()-q.log()
    want_a = .5*(p*(d-(p*d).sum(-1,keepdim=True))+(p-q))/2
    want_b = .5*(q*(-d+(q*d).sum(-1,keepdim=True))+(q-p))/2
    two_view_objective(a,b,y)['symmetric_KL'].backward()
    assert a.grad.abs().max() > 0 and b.grad.abs().max() > 0
    assert torch.allclose(a.grad.double(),want_a,atol=1e-7,rtol=1e-6)
    assert torch.allclose(b.grad.double(),want_b,atol=1e-7,rtol=1e-6)


def test_joint_gradient_has_meanCE_scale_and_no_frozen_teacher():
    a,b,y = sample()
    p,q = a.detach().double().softmax(-1),b.detach().double().softmax(-1)
    d = p.log()-q.log()
    onehot = torch.nn.functional.one_hot(y,3).double()
    want_a = .5*(p-onehot)/2+.25*(p*(d-(p*d).sum(-1,keepdim=True))+(p-q))/2
    want_b = .5*(q-onehot)/2+.25*(q*(-d+(q*d).sum(-1,keepdim=True))+(q-p))/2
    two_view_objective(a,b,y)['combined_loss'].backward()
    assert torch.allclose(a.grad.double(),want_a,atol=1e-7,rtol=1e-6)
    assert torch.allclose(b.grad.double(),want_b,atol=1e-7,rtol=1e-6)


def test_equal_views_have_exact_zero_KL_and_zero_KL_gradient():
    a,_,y = sample()
    b = a.detach().clone().requires_grad_()
    result = two_view_objective(a,b,y)
    assert result['symmetric_KL'] == 0
    result['symmetric_KL'].backward()
    assert torch.count_nonzero(a.grad) == torch.count_nonzero(b.grad) == 0
    assert result['combined_loss'] == result['CE_view1_loss']


@pytest.mark.parametrize('change',['swap','row_duplicate','row_permute','class_permute','constant_shift'])
def test_symmetry_normalization_and_probability_invariants(change):
    a,b,y = sample()
    original = two_view_objective(a,b,y)
    if change == 'swap': a,b = b,a
    elif change == 'row_duplicate': a,b,y = a.repeat(3,1),b.repeat(3,1),y.repeat(3)
    elif change == 'row_permute': a,b,y = a.flip(0),b.flip(0),y.flip(0)
    elif change == 'class_permute': a,b,y = a.flip(1),b.flip(1),2-y
    else: a,b = a+torch.tensor([[3.],[-2.]]),b+torch.tensor([[-4.],[1.]])
    changed = two_view_objective(a,b,y)
    for key in ('CE_loss','symmetric_KL','combined_loss'):
        assert torch.allclose(original[key],changed[key],atol=3e-7,rtol=1e-6)


@pytest.mark.parametrize('bad',['empty','shape','vocab','logit_integer','target_float','masked','out_of_range','nonfinite'])
def test_only_finite_selected_original_gold_not_PAD_or_overlap(bad):
    a,b,y = sample()
    if bad == 'empty': a,b,y = a[:0],b[:0],y[:0]
    elif bad == 'shape': b = b[:1]
    elif bad == 'vocab': a,b = a[:,:1],b[:,:1]
    elif bad == 'logit_integer': a = a.long()
    elif bad == 'target_float': y = y.float()
    elif bad == 'masked': y[0] = -100
    elif bad == 'out_of_range': y[0] = 3
    else:
        b = b.detach()
        b[0,0] = float('nan')
    with pytest.raises(ValueError): two_view_objective(a,b,y)


def test_explicit_FP32_loss_inside_BF16_autocast():
    a,b,y = sample()
    with torch.autocast('cpu',dtype=torch.bfloat16):
        result = two_view_objective(a.bfloat16(),b.bfloat16(),y)
    assert all(v.dtype == torch.float32 and torch.isfinite(v) for v in result.values())


def test_native_meta_count_tie_and_old_hook_install_add_no_state_or_RNG():
    config = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    with torch.device('meta'):
        model = JMicroModel(config)
    before = host(rng_state())
    keys = set(model.state_dict())
    handles = install_training_dropout(model)
    assert len(handles) == 27
    assert sum(p.numel() for p in model.parameters()) == 10001152
    assert model.lm_head.weight is model.model.embed_tokens.weight
    assert set(model.state_dict()) == keys and equal_state(before,host(rng_state()))
    with pytest.raises(ValueError): install_training_dropout(model)
