from pathlib import Path
import math
import sys
import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_confidence_penalty_trainer import ConfidencePenaltyTrainer,confidence_losses,uniform_confidence_loss,committed_state
from natural_context_contrast_corpus import NaturalCorpusTrainer,OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host,right_padded_hidden
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool'; manifest=fixture_pool(pool); p=parent()
    def build(auxiliary=True):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        return (ConfidencePenaltyTrainer if auxiliary else NaturalCorpusTrainer)(p,sampler,
            dict(parent={'sha256':'fixture'},weights_role='verification_only'),batch=4,contrast=False,device='cpu')
    return p,build


def math_fixture():
    p=parent(); p['model_config']['num_hidden_layers']=4
    model=JMicroModel(p['model_config'])
    ids=torch.tensor([[2,65,66,67],[2,68,0,0]])
    targets=torch.tensor([[-100,66,67,3],[68,3,-100,-100]])
    return model,ids,targets


def test_independent_probability_loss_and_analytic_combined_logit_gradient():
    scores=torch.tensor([[2.,-.5,.3],[-1.,.7,1.4]],requires_grad=True); gold=torch.tensor([0,2])
    ce,penalty,combined,entropy=uniform_confidence_loss(scores,gold)
    values=scores.detach().double(); exp=(values-values.max(-1,keepdim=True).values).exp(); p=exp/exp.sum(-1,keepdim=True)
    logp=p.log(); expected_ce=-logp[torch.arange(2),gold].mean(); expected_kl=(p*(logp+math.log(3))).sum(-1).mean()
    assert abs(float(ce.detach())-float(expected_ce))<1e-6
    assert abs(float(penalty.detach())-float(expected_kl))<1e-6
    assert abs(float(entropy.detach())-float(-(p*logp).sum(-1).mean()))<1e-6
    expected=p.clone(); expected[torch.arange(2),gold]-=1
    expected=(expected+.1*p*(logp-(p*logp).sum(-1,keepdim=True)))/2
    actual=torch.autograd.grad(combined,scores)[0]
    assert torch.allclose(actual.double(),expected,atol=1e-7,rtol=1e-6)


def test_uniform_peaked_bounds_and_shift_stability():
    gold=torch.tensor([1,0]); uniform=torch.zeros(2,4,requires_grad=True)
    ce,kl,loss,h=uniform_confidence_loss(uniform,gold)
    assert abs(float(kl.detach()))<1e-6 and abs(float(h.detach())-math.log(4))<1e-6
    assert torch.equal(torch.autograd.grad(kl,uniform)[0],torch.zeros_like(uniform))
    peaked=torch.tensor([[1000.,0.,-1000.,-2000.],[0.,1000.,-1000.,-2000.]],requires_grad=True)
    row=uniform_confidence_loss(peaked,gold)
    assert all(torch.isfinite(x) for x in row) and abs(float(row[1].detach())-math.log(4))<1e-6
    assert torch.isfinite(torch.autograd.grad(row[2],peaked)[0]).all()
    scores=torch.tensor([[2.,-.5,.3],[-1.,.7,1.4]])
    assert all(torch.allclose(a,b,atol=2e-6,rtol=0) for a,b in zip(uniform_confidence_loss(scores,gold),uniform_confidence_loss(scores+30,gold),strict=True))


def test_reverse_kl_gradient_direction_and_difference_from_label_smoothing():
    scores=torch.tensor([[2.,0.,-1.]],requires_grad=True); gold=torch.tensor([0])
    ce,kl,_,_=uniform_confidence_loss(scores,gold)
    actual=torch.autograd.grad(kl,scores,retain_graph=True)[0]
    forward_uniform=-F.log_softmax(scores,-1).mean()-math.log(3)
    other=torch.autograd.grad(forward_uniform,scores)[0]
    assert actual[0,0]>0 and actual[0,1]<0 and actual[0,2]<0
    assert not torch.allclose(actual,other,atol=1e-3,rtol=0)
    assert abs(float(actual.sum()))<1e-6


def test_original_native_ce_and_gradient_preserved():
    model,ids,targets=math_fixture(); ce,_,_,_=confidence_losses(model,ids,targets)
    actual=torch.autograd.grad(ce,list(model.parameters()))
    native=F.cross_entropy(model.lm_head(right_padded_hidden(model,ids))[targets.ne(-100)].float(),targets[targets.ne(-100)])
    expected=torch.autograd.grad(native,list(model.parameters()))
    assert torch.equal(ce,native)
    assert all(torch.allclose(a,b,atol=1e-7,rtol=1e-6) for a,b in zip(actual,expected,strict=True))


def test_only_original_supervised_positions_regularized_and_invalid_gold_rejected():
    model,ids,targets=math_fixture(); actual=confidence_losses(model,ids,targets)
    full=model.lm_head(right_padded_hidden(model,ids)).float(); terms=[]
    for row,column in targets.ne(-100).nonzero():
        logits=full[row,column]; probability=logits.softmax(0)
        terms.append((probability*(probability.log()+math.log(len(logits)))).sum())
    assert torch.allclose(actual[1],torch.stack(terms).mean(),atol=1e-6,rtol=0)
    with pytest.raises(ValueError): confidence_losses(model,ids,torch.full_like(targets,-100))
    for gold in (torch.tensor([-1]),torch.tensor([3])):
        with pytest.raises(ValueError): uniform_confidence_loss(torch.ones(1,3),gold)


def test_initial_tied_native_weights_and_same_once_counted_stream(tmp_path):
    p,build=builders(tmp_path); t,control=build(),build(False)
    assert equal_state(p['model'],host(t.model.state_dict()))
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    assert sum(v.numel() for v in t.model.parameters())==sum(v.numel() for v in control.model.parameters())
    for _ in range(4):
        a,b=t.step(),control.step()
        for k in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens',
                  'original_body_bytes','token_digest','auxiliary_digest','draw_trace','lr'):
            assert equal_state(a[k],b[k]),k
        assert a['confidence_positions_this_update']==a['CE_targets_this_update']
        assert a['decoder_forwards_this_update']==1
    assert committed_state(t.state_dict()) and equal_state(t.sampler.state_dict(),control.sampler.state_dict())
    assert not equal_state(t.model.state_dict(),control.model.state_dict())


def test_continuous_vs_resumed_full_state_and_history(tmp_path):
    _,build=builders(tmp_path); t=build(); expected=[t.step() for _ in range(4)]; state=host(t.state_dict())
    split=build(); rows=[split.step() for _ in range(2)]; split.save(tmp_path/'split.pt')
    resumed=build(); resumed.load(tmp_path/'split.pt'); rows.extend(resumed.step() for _ in range(2))
    assert equal_state(state,host(resumed.state_dict()))
    for a,b in zip(expected,rows,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


@pytest.mark.parametrize('mutation',['coefficient','kind','positions','optimizer','sampler'])
def test_mismatched_recipe_or_uncommitted_state_rejected(tmp_path,mutation):
    _,build=builders(tmp_path); t=build(); t.step(); state=host(t.state_dict())
    if mutation=='coefficient': state['spec']['confidence_penalty']['coefficient']=.2
    if mutation=='kind': state['kind']='native_original_CE_only'
    if mutation=='positions': state['confidence_penalty']['positions']+=1
    if mutation=='optimizer': next(iter(state['optimizer']['state'].values()))['step']+=1
    if mutation=='sampler': state['sampler']['consumed']['web']+=1
    torch.save(state,tmp_path/'bad.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'bad.pt')


def test_uncommitted_failure_cannot_save_or_continue(tmp_path,monkeypatch):
    _,build=builders(tmp_path); t=build()
    import base_confidence_penalty_trainer
    monkeypatch.setattr(base_confidence_penalty_trainer,'confidence_losses',lambda *args: (_ for _ in ()).throw(RuntimeError('injected')))
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path/'bad.pt')
    with pytest.raises(ValueError): t.step()
