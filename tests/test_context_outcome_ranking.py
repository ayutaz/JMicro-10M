import copy
import sys
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from context_outcome_ranking import outcome_ranking_loss,OutcomePairSampler


def test_balanced_opposite_context_loss_gradients_and_no_direct_EOS_or_prefix_gradient():
    logits=torch.zeros(4,2,11,requires_grad=True)
    labels=torch.tensor([[-100,8],[-100,9],[-100,8],[-100,9]])
    loss,counts=outcome_ranking_loss(logits,labels)
    assert loss.item()==pytest.approx(np.log(2))
    loss.backward()
    assert logits.grad[:,0].eq(0).all()
    assert logits.grad[...,3].eq(0).all()
    assert logits.grad[0,1,8]<0 and logits.grad[1,1,9]>0
    assert logits.grad[2,1,8]>0 and logits.grad[3,1,9]<0
    assert counts['relational_choice_labels']==2
    assert counts['gold_body_scored_positions']==counts['foil_body_scored_positions']==2
    assert counts['ordinary_CE_teacher_tokens']==counts['soft_target_body_positions']==0
    changed=logits.detach().clone();changed[...,3]=100
    assert outcome_ranking_loss(changed,labels)[0].item()==loss.item()
    # A global preference for candidate8 helps one pole but hurts its opposite.
    biased=logits.detach().clone();biased[0,1,8]=biased[2,1,8]=4
    assert outcome_ranking_loss(biased,labels)[0].item()>loss.item()
    contextual=logits.detach().clone();contextual[0,1,8]=contextual[3,1,9]=4
    assert outcome_ranking_loss(contextual,labels)[0].item()<loss.item()
    with pytest.raises(ValueError):
        outcome_ranking_loss(logits,torch.full_like(labels,3))


def toy_view():
    # Three families force an epoch boundary across a two-family update.
    inputs=np.zeros((12,8),dtype=np.int64);inputs[:,:3]=[2,8,9]
    labels=np.full((12,8),-100,dtype=np.int64)
    labels[:,2]=[8,9,8,9]*3
    valid=inputs!=0
    return SimpleNamespace(inputs=inputs,labels=labels,valid=valid,target_bytes=np.full(12,3),
        family_ids=['train-a','train-b','train-c'],context=8,binding=dict(source='fixed-train'))


def test_pair_sampler_all_state_resume_across_epoch_without_global_rng_and_no_hidden_CE():
    view=toy_view();before=torch.get_rng_state().clone()
    continuous=OutcomePairSampler(view);left=[continuous.next() for _ in range(4)]
    split=OutcomePairSampler(view);right=[split.next() for _ in range(2)]
    resumed=OutcomePairSampler(view);resumed.load_state_dict(split.state_dict())
    right.extend(resumed.next() for _ in range(2))
    for a,b in zip(left,right,strict=True):
        assert a[-1]==b[-1]
        for x,y in zip(a[:3],b[:3],strict=True):assert torch.equal(x,y)
    assert continuous.state_dict()==resumed.state_dict()
    assert torch.equal(before,torch.get_rng_state())
    assert resumed.relational_choice_labels==16
    assert resumed.physical_input_positions==256
    assert resumed.gold_body_scored_positions==resumed.foil_body_scored_positions==16
    bad=copy.deepcopy(resumed.state_dict());bad['relational_choice_labels']-=1
    with pytest.raises(ValueError):OutcomePairSampler(view).load_state_dict(bad)
