import math
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_preference_loss import collate_continuations,continuation_logps,dpo_loss


def test_prompt_padding_mask_single_shift_and_EOS_gradients():
    rows=[dict(prompt_ids=[2,8,9],chosen_ids=[10,3],rejected_ids=[11,12,3]),
        dict(prompt_ids=[2,8],chosen_ids=[9,3],rejected_ids=[11])]
    x,y,mask=collate_continuations(rows)
    assert x[0].tolist()==[2,8,9,10,0] and y[0].tolist()==[-100,-100,10,3,-100]
    assert y[2].tolist()==[-100,-100,11,12,3] and y[3].tolist()==[-100,11,-100,-100,-100]
    logits=torch.zeros((*x.shape,16),requires_grad=True); scores,counts=continuation_logps(logits,y)
    assert counts.tolist()==[2,2,3,1] and torch.allclose(scores,-counts*math.log(16))
    scores.sum().backward()
    assert not logits.grad[y.eq(-100)].any() and logits.grad[0,3,3]>0 and logits.grad[0,2,10]>0
    assert mask[0].tolist()==[True,True,True,True,False]
    with pytest.raises(ValueError): collate_continuations([dict(rows[0],chosen_ids=[7,3])])
    with pytest.raises(ValueError): collate_continuations([dict(rows[0],chosen_ids=[3,10])])


def test_fixed_reference_ratio_cancels_raw_length_gap_and_gradient_direction():
    chosen=torch.tensor([-180.,-30.],requires_grad=True); rejected=torch.tensor([-5.,-60.],requires_grad=True)
    loss,margin=dpo_loss(chosen,rejected,chosen.detach(),rejected.detach())
    assert loss.item()==pytest.approx(math.log(2)) and not margin.any()
    loss.backward()
    assert torch.all(chosen.grad<0) and torch.all(rejected.grad>0)
    raised,_=dpo_loss(chosen.detach()+1,rejected.detach(),chosen.detach(),rejected.detach())
    assert raised<loss
    with pytest.raises(ValueError): dpo_loss(chosen,rejected,chosen,rejected.detach())
    with pytest.raises(ValueError): dpo_loss(chosen,rejected,chosen.detach(),rejected.detach(),float('nan'))
