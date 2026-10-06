import copy
import sys
import pytest
import torch
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from web_kl_preservation import body_parent_kl,WebBodyReplay
from test_original_web_retention_trainer import setup
from run_eos_short_pilot import equal_state


def test_KL_direction_teacher_detachment_and_body_only_mask():
    parent=torch.tensor([[[2.,0.,1.],[0.,2.,1.],[1.,0.,2.]]],requires_grad=True)
    student=torch.tensor([[[0.,2.,1.],[2.,0.,1.],[2.,1.,0.]]],requires_grad=True)
    labels=torch.tensor([[8,3,-100]])
    loss,count=body_parent_kl(student,parent,labels)
    expected=(parent[0,0].detach().softmax(-1)*(parent[0,0].detach().log_softmax(-1)-student[0,0].log_softmax(-1))).sum()
    assert loss.item()==pytest.approx(expected.item())
    loss.backward()
    assert parent.grad is None and student.grad[0,0].abs().sum()>0 and not student.grad[0,1:].any()
    assert count==dict(soft_target_body_positions=1,ignored_special_positions=2,physical_reference_input_tokens=3,new_ordinary_CE_teacher_tokens=0)
    assert body_parent_kl(parent,parent.detach(),labels)[0].item()==pytest.approx(0.)
    with pytest.raises(ValueError):body_parent_kl(student,parent,torch.full_like(labels,3))
    with pytest.raises(ValueError):body_parent_kl(student,parent[:,:2],labels)


def test_replay_fork_preserves_main_cursor_and_exact_resume_accounting(tmp_path):
    pool,parent,_,_=setup(tmp_path);cursor=copy.deepcopy(parent['sampler'])
    def build():return WebBodyReplay(pool,cursor,batch=2,context=8)
    continuous,split=build(),build()
    left=[continuous.next() for _ in range(4)]
    right=[split.next() for _ in range(2)]
    state=copy.deepcopy(split.state_dict());resumed=build();resumed.load_state_dict(state)
    right.extend(resumed.next() for _ in range(2))
    assert equal_state(left,right) and equal_state(continuous.state_dict(),resumed.state_dict())
    assert parent['sampler']==cursor
    assert continuous.physical_input_tokens==64
    assert continuous.body_positions+continuous.ignored_positions==64
    for key,value in (('physical_input_tokens',65),('batch',3),('kind','different')):
        with pytest.raises(ValueError):build().load_state_dict({**state,key:value})
