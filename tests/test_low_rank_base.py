"""Real small-model CPU gradients/merge and complete-state resume, not quality."""
import copy
import sys
from pathlib import Path
import pytest
import torch
from torch import nn
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from jmicro.model import JMicroModel
from jmicro.training import rng_state
from low_rank_base_trainer import LowRankLinear,LowRankBaseTrainer,attach,merged_state
from test_interleaved_outcome import historical_fixture
from run_eos_short_pilot import equal_state


def test_rank_four_gradient_math_frozen_weight_and_exact_merge():
    torch.manual_seed(7);linear=nn.Linear(9,11,bias=False)
    rng=rng_state();layer=LowRankLinear(linear,torch.Generator().manual_seed(42))
    assert equal_state(rng,rng_state())
    x=torch.randn(3,9);original=linear.weight.detach().clone()
    assert torch.equal(layer(x),linear(x))
    layer(x).square().mean().backward()
    assert layer.weight.grad is None and torch.count_nonzero(layer.A.grad)==0 and torch.count_nonzero(layer.B.grad)>0
    with torch.no_grad():layer.B.add_(torch.randn_like(layer.B)*.1)
    expected=nn.functional.linear(x,original+layer.B@layer.A)
    assert torch.allclose(layer(x),expected,atol=1e-6,rtol=1e-6)
    assert torch.equal(layer.weight,original)
    with pytest.raises(ValueError):LowRankLinear(nn.Linear(9,11),torch.Generator())


def test_full_native_model_zero_initialization_merge_and_tied_parameter_count(tmp_path):
    _,parent,_,_=historical_fixture(tmp_path)
    model=JMicroModel(parent['model_config']);model.load_state_dict(parent['model']);model.eval()
    x=torch.tensor([[2,8,9,10,3,2,12,3]])
    before=model(x).logits;original=copy.deepcopy(model.state_dict());rng=rng_state();names=attach(model)
    assert equal_state(rng,rng_state()) and torch.equal(before,model(x).logits)
    assert len(names)==7*len(model.model.layers)
    with torch.no_grad():
        for name in names:model.get_submodule(name).B.normal_(0,.01)
    saved=merged_state(model);native=JMicroModel(parent['model_config']);native.load_state_dict(saved);native.eval()
    assert set(saved)==set(original) and native.model.embed_tokens.weight is native.lm_head.weight
    assert torch.allclose(model(x).logits,native(x).logits,atol=1e-5,rtol=1e-5)
    assert all(torch.equal(model.state_dict()[k],v) for k,v in original.items())
    assert sum(p.numel() for p in native.parameters())==sum(p.numel() for p in model.parameters() if not p.requires_grad)


@pytest.mark.parametrize('arm',['full_fresh_Adam','rank4_frozen_backbone'])
def test_same_fresh_optimizer_policy_and_exact_cpu_save_resume(tmp_path,arm):
    pool,parent,b,positive=historical_fixture(tmp_path)
    goals=dict(web=199,story=51,ordinary_textbook=71,conditional_textbook=197)
    def build(binding=b):return LowRankBaseTrainer(parent,pool,pool,positive,goals,binding,arm,'cpu',8,3)
    t=build();assert not t.optimizer.state and equal_state(t.scheduler.state_dict(),parent['scheduler'])
    assert equal_state(rng_state(),parent['rng']) and equal_state(merged_state(t.model),parent['model'])
    assert all(g['lr']==.00001 for g in t.optimizer.param_groups)
    a=[t.step() for _ in range(4)];t.save(tmp_path/'continuous.pt')
    t=build();z=[t.step() for _ in range(2)];t.save(tmp_path/'split.pt');t=build();t.load(tmp_path/'split.pt')
    z.extend(t.step() for _ in range(2));t.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'continuous.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    for key in set(a[0])-{'seconds','data_wait_seconds','tokens_per_second'}:
        assert equal_state([r[key] for r in a],[r[key] for r in z]),key
    state=torch.load(tmp_path/'resumed.pt',weights_only=False);bad=copy.deepcopy(state)
    bad['model']['model.norm.weight'][0]+=1;torch.save(bad,tmp_path/'bad.pt')
    with pytest.raises(ValueError):build().load(tmp_path/'bad.pt')
    with pytest.raises(ValueError):build(dict(b,arm='other')).load(tmp_path/'split.pt')
