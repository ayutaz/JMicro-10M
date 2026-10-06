import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from eos_decoupled_web_kl_preservation import body_parent_kl
from web_kl_eos_decomposition import decompose


def test_weighted_conditional_component_and_zero_direct_EOS_gradient():
    g = torch.Generator().manual_seed(42)
    parent = torch.randn(2,4,11,generator=g,requires_grad=True)
    student = torch.randn(2,4,11,generator=g,requires_grad=True)
    labels = torch.tensor([[8,3,9,-100],[2,10,8,3]])
    loss,counts = body_parent_kl(student,parent,labels)
    reference = decompose(parent.detach(),student.detach(),labels)
    assert loss.item() == pytest.approx(reference['weighted_conditional_non_EOS_KL'].mean().item(),abs=1e-6)
    loss.backward()
    assert parent.grad is None
    assert student.grad[...,3].eq(0).all()
    assert student.grad[labels<8].eq(0).all()
    assert student.grad[...,8:].abs().sum() > 0
    assert counts['soft_target_body_positions'] == 4
    assert counts['ignored_special_positions'] == 4
    assert 0 < counts['non_EOS_teacher_probability_mass'] < 4
    with pytest.raises(ValueError):
        body_parent_kl(student,parent,torch.full_like(labels,3))


def test_changing_only_student_EOS_logit_leaves_loss_identical():
    g = torch.Generator().manual_seed(13)
    parent = torch.randn(1,3,11,generator=g)
    student = torch.randn(1,3,11,generator=g)
    labels = torch.full((1,3),8)
    changed = student.clone(); changed[...,3] += 100
    first,_ = body_parent_kl(student,parent,labels)
    second,_ = body_parent_kl(changed,parent,labels)
    assert first.item() == second.item()
