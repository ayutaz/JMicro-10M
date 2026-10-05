import copy
import pytest
import torch
from jmicro.natural_learning import material,apply_optimizer_policy
from jmicro.tokenizer import Tokenizer
from jmicro.experiment import ROOT


def test_material_disjoint_train_dev_and_unique_memorization_prefixes():
    train=material('train',1000);dev=material('dev',128)
    assert len({r['text'] for r in train})==1000
    assert not {r['text'] for r in train}&{r['text'] for r in dev}
    assert len({r['prefix'] for r in train})==1000
    assert {r['scene'] for r in train[:64]}==set(range(32))


def test_natural_codec_targets_include_complete_body_and_eos_without_truncation():
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    for row in material('train',1000)+material('dev',128):
        prefix=tok.encode(row['prefix']);body=tok.encode(row['text'])
        assert body[:len(prefix)]==prefix
        assert tok.decode(body)==row['text'] and len(body)+1<=128
        assert len(body)-len(prefix)+1<=64


def test_fresh_adam_changes_moments_not_weights_or_hyperparameters():
    p=torch.nn.Parameter(torch.tensor([1.,2.]));opt=torch.optim.AdamW([p],lr=.001)
    p.square().sum().backward();opt.step()
    weights=p.detach().clone();groups=copy.deepcopy(opt.param_groups);state=copy.deepcopy(opt.state_dict())
    apply_optimizer_policy(opt,'inherit');assert opt.state_dict()['state'].keys()==state['state'].keys()
    apply_optimizer_policy(opt,'fresh');assert not opt.state
    assert torch.equal(p,weights)
    for k,v in groups[0].items():
        if k!='params':assert opt.param_groups[0][k]==v
    opt.load_state_dict(state);assert opt.state
    assert all(torch.equal(v,state['state'][0][k]) for k,v in opt.state[p].items() if torch.is_tensor(v))


def test_capacity_and_optimizer_errors_are_explicit():
    with pytest.raises(ValueError):material('train',1025)
    with pytest.raises(ValueError):apply_optimizer_policy(torch.optim.AdamW([torch.nn.Parameter(torch.ones(1))]),'reset-on-every-step')
