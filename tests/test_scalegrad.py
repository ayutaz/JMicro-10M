"""Independent prefix, probability, gradient and native-disable oracles."""
import copy
import math
import pytest
import torch
from torch.nn import functional as F
from jmicro.scalegrad import selected_novel_mask,scalegrad_objective


def prefix_oracle(rows,vocab):
    return torch.tensor([[token not in {v for v in row['input_ids'][:column+1] if v >= 8}
        for token in range(vocab)] for row in rows for column,target in enumerate(row['target_ids'])
        if target != -100],dtype=torch.bool)


@pytest.mark.parametrize('rows',[
    [dict(input_ids=[2,8,9,8],target_ids=[8,9,8,3])],
    [dict(input_ids=[8,9,10,8],target_ids=[-100,-100,8,3]),
     dict(input_ids=[9,8],target_ids=[8,3])],
    [dict(input_ids=[2,8,8],target_ids=[-100,-100,-100]),
     dict(input_ids=[2,10,9,10],target_ids=[10,-100,10,3])],
    [dict(input_ids=[8]*1024,target_ids=[-100]*1023+[3])],
])
def test_full_history_oracle_no_future_leak_row_leak_or_input_mutation(rows):
    saved=copy.deepcopy(rows)
    before=torch.get_rng_state().clone()
    result=selected_novel_mask(rows,16,'cpu')
    assert torch.equal(result,prefix_oracle(rows,16))
    assert result[:,:8].all() and result.dtype==torch.bool
    assert rows==saved and torch.equal(before,torch.get_rng_state())


def test_current_input_is_history_but_current_target_and_future_are_not():
    rows=[dict(input_ids=[8,9,10,8],target_ids=[9,10,8,3])]
    mask=selected_novel_mask(rows,16,'cpu')
    assert not mask[0,8] and mask[0,9] and mask[0,10]
    assert not mask[1,9] and mask[1,10]
    assert not mask[2,8] and not mask[2,10]
    assert mask[:,3].all()


@pytest.mark.parametrize('mask_kind',['mixed','all_novel','none_novel'])
def test_probability_renormalization_scalar_and_ALL_logits_gradients(mask_kind):
    generator=torch.Generator().manual_seed(821)
    logits=torch.randn(5,16,dtype=torch.float64,generator=generator,requires_grad=True)
    targets=torch.tensor([3,8,9,10,15])
    mask=torch.rand(5,16,generator=generator)>.4
    if mask_kind=='all_novel': mask[:]=True
    if mask_kind=='none_novel': mask[:]=False
    values=scalegrad_objective(logits,targets,mask)
    actual=torch.autograd.grad(values['combined_loss'],logits)[0]
    raw=logits.detach().clone().requires_grad_(True)
    probabilities=raw.softmax(-1)
    scaled=probabilities*torch.where(mask,probabilities.new_tensor(.2),probabilities.new_tensor(1.))
    normalized=scaled/scaled.sum(-1,keepdim=True)
    expected=-normalized[torch.arange(5),targets].log().mean()
    reference=torch.autograd.grad(expected,raw)[0]
    analytic=normalized.detach().clone()
    analytic[torch.arange(5),targets]-=1
    analytic/=len(targets)
    torch.testing.assert_close(values['combined_loss'],expected,atol=1e-12,rtol=1e-12)
    torch.testing.assert_close(actual,reference,atol=1e-12,rtol=1e-12)
    torch.testing.assert_close(actual,analytic,atol=1e-12,rtol=1e-12)
    assert values['CE_loss']==F.cross_entropy(logits,targets)
    assert not values['CE_loss'].requires_grad


def test_gamma1_is_BITWISE_native_CE_and_native_gradient():
    generator=torch.Generator().manual_seed(13)
    values=torch.randn(4,16,generator=generator,requires_grad=True)
    targets=torch.tensor([8,3,9,10])
    result=scalegrad_objective(values,targets,torch.ones_like(values,dtype=torch.bool),gamma=1.)
    native=F.cross_entropy(values,targets)
    assert torch.equal(result['combined_loss'],native)
    assert torch.equal(torch.autograd.grad(result['combined_loss'],values)[0],
                       torch.autograd.grad(native,values)[0])


def test_novel_gold_increases_gold_gradient_and_seen_nongold_gradient():
    logits=torch.zeros(1,16,requires_grad=True)
    target=torch.tensor([9])
    mask=torch.ones_like(logits,dtype=torch.bool)
    mask[:,8]=False
    loss=scalegrad_objective(logits,target,mask)['combined_loss']
    gradient=torch.autograd.grad(loss,logits)[0]
    native=logits.detach().softmax(-1)
    native[0,9]-=1
    assert gradient[0,9]<native[0,9]<0
    assert gradient[0,8]>native[0,8]>0
    assert abs(float(gradient.sum()))<1e-6


def test_saturated_low_gold_stays_finite_without_probability_epsilon_or_clipping():
    logits=torch.tensor([[1000.]+[0.]*14+[-1000.]],requires_grad=True)
    mask=torch.ones_like(logits,dtype=torch.bool)
    mask[0,0]=False
    result=scalegrad_objective(logits,torch.tensor([15]),mask)
    result['combined_loss'].backward()
    assert torch.isfinite(result['combined_loss']) and torch.isfinite(logits.grad).all()
    assert logits.grad[0,15]==-1 and logits.grad[0,0]==1


@pytest.mark.parametrize('bad',[0.,-.1,1.01,float('inf'),float('nan'),True])
def test_invalid_strength_refused(bad):
    with pytest.raises(ValueError):
        scalegrad_objective(torch.zeros(1,16),torch.tensor([8]),torch.ones(1,16,dtype=torch.bool),gamma=bad)


@pytest.mark.parametrize('rows',[
    [],[dict(input_ids=[],target_ids=[])],
    [dict(input_ids=[0,8],target_ids=[8,3])],
    [dict(input_ids=[2,16],target_ids=[8,3])],
    [dict(input_ids=[2,8],target_ids=[8])],
    [dict(input_ids=[2,8],target_ids=[8,7])],
    [dict(input_ids=[2,8],target_ids=[8,16])],
    [dict(input_ids=[2,8],target_ids=[-100,-100])],
])
def test_invalid_material_or_empty_teacher_set_refused(rows):
    with pytest.raises(ValueError): selected_novel_mask(rows,16,'cpu')
