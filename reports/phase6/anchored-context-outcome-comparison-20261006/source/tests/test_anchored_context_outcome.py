import sys
from pathlib import Path
import math
import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from anchored_context_outcome import anchored_outcome_loss
from context_outcome_ranking import outcome_ranking_loss


def test_same_ranking_and_token_weighted_positive_anchor_masks_and_gradients():
    logits=torch.zeros(4,3,11,requires_grad=True)
    labels=torch.tensor([[-100,8,9],[-100,9,-100],[-100,8,9],[-100,9,-100]])
    combined,ranking,anchor,counts=anchored_outcome_loss(logits,labels)
    prior,old_counts=outcome_ranking_loss(logits,labels)
    assert ranking.item()==prior.item()==pytest.approx(math.log(2))
    assert anchor.item()==pytest.approx(math.log(10))
    assert combined.item()==pytest.approx(ranking.item()+anchor.item())
    for k,v in old_counts.items():assert counts[k]==v
    assert counts['positive_anchor_body_teacher_tokens']==3
    assert counts['positive_anchor_ignored_positions']==9
    anchor.backward()
    assert logits.grad[[1,2]].eq(0).all()  # Foil rows are never hard teachers.
    assert logits.grad[labels==-100].eq(0).all()
    assert logits.grad[...,3].eq(0).all()
    assert all(logits.grad[r,t,labels[r,t]]<0 for r,t in ((0,1),(0,2),(3,1)))
    assert logits.grad[0,1,8].item()==pytest.approx(logits.grad[3,1,9].item())
    changed=logits.detach().clone();changed[...,3]=100
    for a,b in zip(anchored_outcome_loss(changed,labels)[:3],(combined,ranking,anchor),strict=True):
        assert a.item()==b.item()
    with pytest.raises(ValueError):anchored_outcome_loss(logits,torch.full_like(labels,3))


def test_improved_relative_margin_can_reduce_gold_probability_and_raise_anchor():
    labels=torch.tensor([[-100,8],[-100,9],[-100,8],[-100,9]])
    before=torch.zeros(4,2,11)
    before[0,1,8]=before[3,1,9]=2
    after=before.clone()
    after[0,1,8]=after[3,1,9]=1
    after[1,1,9]=after[2,1,8]=-6
    a=anchored_outcome_loss(before,labels);b=anchored_outcome_loss(after,labels)
    assert b[1]<a[1]  # Relative-only objective rewards this change.
    assert b[2]>a[2]  # The new term detects lower absolute gold probability.
    assert b[0]>a[0]

