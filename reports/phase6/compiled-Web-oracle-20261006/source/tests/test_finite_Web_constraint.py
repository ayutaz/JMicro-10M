"""CPU finite-function math and real tiny-model transactional states, not quality."""
import copy
import sys
from pathlib import Path
import pytest
import torch
from torch import nn
from torch.nn import functional as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from jmicro.model import JMicroModel
from jmicro.training import rng_state
from finite_Web_constraint import BodyOracle,constrain,ConstraintRejected,FiniteWebTrainer
from test_interleaved_outcome import historical_fixture
from run_eos_short_pilot import equal_state


class Quadratic:
    def __init__(self,p):self.p=p
    def measure(self,gradient=False):
        value=.5+self.p.square().sum()
        return float(value.detach()),[torch.autograd.grad(value,self.p)[0]] if gradient else None


def test_finite_projection_and_strict_backtrack_independent_quadratic():
    p=nn.Parameter(torch.tensor([.2]));before=[torch.zeros_like(p)]
    d=constrain([p],before,Quadratic(p),.5)
    assert d['accepted'] and d['projected'] and d['backtracked'] and d['scale']==.5
    assert float(.5+p.square().sum())<=.5*1.01 and d['final_body_NLL']<=d['ceiling_body_NLL']
    assert len(d['trials'])==3
    p=nn.Parameter(torch.tensor([2.]))
    with pytest.raises(ConstraintRejected) as exc:constrain([p],[torch.zeros_like(p)],Quadratic(p),.5)
    assert len(exc.value.decision['trials'])==5 and not exc.value.decision['accepted']
    with pytest.raises(ValueError):constrain([p,p],[p.detach().clone(),p.detach().clone()],Quadratic(p),.5)


def memory():
    x=torch.tensor([[2,8,9,3,2,10,11,3],[2,12,13,3,2,8,10,3]])
    y=torch.tensor([[8,9,3,-100,10,11,3,12],[12,13,3,-100,8,10,3,9]])
    return dict(x=x,y=y)


def test_actual_body_oracle_gradients_equal_flat_mean_unique_ties_and_rng(tmp_path):
    _,parent,_,_=historical_fixture(tmp_path);model=JMicroModel(parent['model_config']);model.load_state_dict(parent['model'])
    packet=memory();oracle=BodyOracle(model,packet,1);before=rng_state();value,grads=oracle.measure(True)
    y=packet['y'].clone();y[y.lt(8)]=-100
    logits=model(packet['x'],training_fast_path=True).logits
    loss=F.cross_entropy(logits.flatten(0,1),y.flatten(),ignore_index=-100)
    expected=torch.autograd.grad(loss,list(model.parameters()))
    assert value==pytest.approx(float(loss),abs=1e-6)
    assert all(torch.allclose(a,b,atol=1e-6,rtol=1e-6) for a,b in zip(grads,expected,strict=True))
    assert all(p.grad is None for p in model.parameters()) and model.training and equal_state(before,rng_state())
    assert model.model.embed_tokens.weight is model.lm_head.weight
    assert oracle.stats['gradient_teacher_tokens']==int(y.ne(-100).sum())
    assert oracle.stats['physical_input_tokens']==packet['x'].numel()


def build_fixture(tmp_path):
    pool,parent,b,positive=historical_fixture(tmp_path)
    goals=dict(web=13,story=13,ordinary_textbook=13,conditional_textbook=197)
    def build(binding=b):return FiniteWebTrainer(parent,pool,pool,positive,goals,binding,memory(),{'fixture':'CPU_only'},device='cpu',context=8,batch=3)
    return parent,build


def test_real_cpu_continuous_resume_preserves_all_states_active_mask_and_auxiliary(tmp_path):
    parent,build=build_fixture(tmp_path);t=build()
    assert equal_state(t.model.state_dict(),parent['model']) and equal_state(t.optimizer.state_dict(),parent['optimizer'])
    assert equal_state(t.scheduler.state_dict(),parent['scheduler']) and equal_state(rng_state(),parent['rng'])
    a=[t.step() for _ in range(4)];t.save(tmp_path/'continuous.pt')
    t=build();z=[t.step() for _ in range(2)];t.save(tmp_path/'split.pt');t=build();t.load(tmp_path/'split.pt')
    z.extend(t.step() for _ in range(2));t.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'continuous.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    for key in set(a[0])-{'seconds','data_wait_seconds','tokens_per_second'}:
        assert equal_state([r[key] for r in a],[r[key] for r in z]),key
    assert a[-1]['removed_prefix_targets']['conditional_textbook']>0
    assert all(r['constraint']['final_body_NLL']<=t.reference_ce*1.01 for r in a)
    assert t.auxiliary['accepted_updates']==4
    bad=torch.load(tmp_path/'resumed.pt',weights_only=False);bad['last_constraint']['final_body_NLL']=t.reference_ce*1.02
    torch.save(bad,tmp_path/'bad.pt')
    with pytest.raises(ValueError):build().load(tmp_path/'bad.pt')


def test_failed_real_source_update_restores_complete_boundary_including_sampler_rng(tmp_path):
    _,build=build_fixture(tmp_path);t=build();t.step();t.save(tmp_path/'before.pt')
    before_called=getattr(t.optimizer,'_opt_called',None)
    def impossible(gradient=False):
        t.oracle.stats['gradient_calls' if gradient else 'forward_only_calls']+=1
        t.oracle.stats['teacher_observations']+=t.oracle.teachers;t.oracle.stats['physical_input_tokens']+=t.oracle.physical
        if gradient:t.oracle.stats['gradient_teacher_tokens']+=t.oracle.teachers
        return t.reference_ce*2,[torch.zeros_like(p) for p in t.model.parameters()] if gradient else None
    t.oracle.measure=impossible
    with pytest.raises(ConstraintRejected):t.step()
    t.save(tmp_path/'after.pt')
    assert equal_state(torch.load(tmp_path/'before.pt',weights_only=False),torch.load(tmp_path/'after.pt',weights_only=False))
    assert getattr(t.optimizer,'_opt_called',None)==before_called and all(p.grad is None for p in t.model.parameters())
    assert t.last_rejection['attempted_source_gradient_teacher_tokens']>0
    assert t.last_rejection['auxiliary_completed_calls']['gradient_teacher_tokens']==t.oracle.teachers
    assert t.last_rejection['restored_last_completed_update']==t.update
