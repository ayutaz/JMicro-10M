import sys
from pathlib import Path

import pytest
import torch
from torch.nn import functional as F

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_label_smoothing import EPSILON,smoothed_teacher_loss


def test_smoothing_matches_full_distribution_and_exact_gradient():
    logits=torch.tensor([[.3,-.4,.5,.9,-.3],[.1,.7,-.2,.4,-.1]],requires_grad=True)
    labels=torch.tensor([3,2])
    loss,detail=smoothed_teacher_loss(logits,labels)
    assert torch.allclose(loss,F.cross_entropy(logits,labels,label_smoothing=EPSILON))
    gradient,=torch.autograd.grad(loss,logits)
    targets=F.one_hot(labels,5).float()*(1-EPSILON)+EPSILON/5
    assert torch.allclose(gradient,(logits.softmax(-1)-targets)/2,atol=1e-7)
    assert detail['original_CE_positions']==2 and detail['original_EOS_positions']==1
    assert detail['weighted_original_target_mass']==1.8 and detail['uniform_target_mass']==.2
    assert detail['uniform_soft_target_positions']==2 and detail['vocabulary_size']==5


def test_masked_padding_and_overlap_have_no_loss_or_gradient():
    logits=torch.arange(30.).reshape(2,3,5).requires_grad_()
    labels=torch.tensor([[3,-100,-100],[-100,4,-100]])
    loss,detail=smoothed_teacher_loss(logits,labels)
    gradient,=torch.autograd.grad(loss,logits)
    assert torch.equal(gradient[labels==-100],torch.zeros_like(gradient[labels==-100]))
    changed=logits.detach().clone();changed[labels==-100]=-500
    actual,_=smoothed_teacher_loss(changed,labels)
    assert torch.equal(loss.detach(),actual) and detail['original_CE_positions']==2


def test_zero_epsilon_is_native_ce_and_invalid_teachers_rejected():
    values=torch.tensor([[.1,.2,-.1,.7]]);labels=torch.tensor([3])
    loss,detail=smoothed_teacher_loss(values,labels,epsilon=0)
    assert torch.equal(loss,F.cross_entropy(values,labels))
    assert detail['uniform_soft_target_positions']==0 and detail['uniform_target_mass']==0
    with pytest.raises(ValueError):smoothed_teacher_loss(values,torch.tensor([-100]))
    with pytest.raises(ValueError):smoothed_teacher_loss(values,torch.tensor([-1]))
    with pytest.raises(ValueError):smoothed_teacher_loss(values,labels,epsilon=1)
