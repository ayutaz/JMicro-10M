from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_sam_trainer import SAMTrainer, sam_backward, committed_state
from natural_context_contrast_corpus import NaturalCorpusTrainer,OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool'; manifest=fixture_pool(pool); p=parent()
    def build(sam=True):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        return (SAMTrainer if sam else NaturalCorpusTrainer)(p,sampler,dict(parent={'sha256':'fixture'},weights_role='verification_only'),batch=4,contrast=False,device='cpu')
    return p,build


def test_independent_quadratic_perturbation_second_gradient_and_exact_restore():
    model=torch.nn.Linear(2,1,bias=False); model.weight.data.copy_(torch.tensor([[1.,2.]]))
    opt=torch.optim.AdamW(model.parameters(),lr=1e-5,weight_decay=.1)
    original=model.weight.detach().clone(); seen=[]
    def closure():
        seen.append(model.weight.detach().clone())
        return (model.weight.square().sum()/2)
    result=sam_backward(model,opt,closure)
    expected=original+.05*original/original.norm()
    assert torch.allclose(seen[1],expected,atol=1e-7,rtol=0)
    assert torch.equal(model.weight,original)
    expected_gradient=expected/(expected.norm()+1e-6)
    assert torch.allclose(model.weight.grad,expected_gradient,atol=1e-7,rtol=0)
    assert result['perturbed_CE_loss'] > result['CE_loss'] and not opt.state


def test_failure_during_second_pass_restores_exact_weights_and_no_optimizer_step():
    model=torch.nn.Linear(2,1,bias=False); opt=torch.optim.AdamW(model.parameters()); old=host(model.state_dict()); calls=0
    def closure():
        nonlocal calls
        calls+=1
        if calls==2: raise RuntimeError('injected second pass')
        return model.weight.square().sum()
    with pytest.raises(RuntimeError): sam_backward(model,opt,closure)
    assert equal_state(old,host(model.state_dict())) and not opt.state


def test_initial_tied_native_weights_and_same_once_counted_stream(tmp_path):
    p,build=builders(tmp_path); t,control=build(),build(False)
    assert equal_state(p['model'],host(t.model.state_dict()))
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    for _ in range(4):
        a,b=t.step(),control.step()
        for k in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens','original_body_bytes','token_digest','auxiliary_digest','draw_trace','lr'):
            assert equal_state(a[k],b[k]),k
        assert a['repeated_teacher_positions_this_update']==a['CE_targets_this_update']
    assert committed_state(t.state_dict()) and equal_state(t.sampler.state_dict(),control.sampler.state_dict())
    assert not equal_state(t.model.state_dict(),control.model.state_dict())


def test_continuous_vs_resumed_full_state_and_history(tmp_path):
    _,build=builders(tmp_path); t=build(); expected=[t.step() for _ in range(4)]; state=host(t.state_dict())
    split=build(); rows=[split.step() for _ in range(2)]; split.save(tmp_path/'split.pt')
    resumed=build(); resumed.load(tmp_path/'split.pt'); rows.extend(resumed.step() for _ in range(2))
    assert equal_state(state,host(resumed.state_dict()))
    for a,b in zip(expected,rows,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},{k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


@pytest.mark.parametrize('mutation',['rho','repeat','optimizer','sampler'])
def test_mismatched_recipe_or_uncommitted_state_rejected(tmp_path,mutation):
    _,build=builders(tmp_path); t=build(); t.step(); state=host(t.state_dict())
    if mutation=='rho': state['spec']['SAM']['rho']=.1
    if mutation=='repeat': state['SAM']['repeated_teacher_positions']+=1
    if mutation=='optimizer': next(iter(state['optimizer']['state'].values()))['step']+=1
    if mutation=='sampler': state['sampler']['consumed']['web']+=1
    torch.save(state,tmp_path/'bad.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'bad.pt')


def test_uncommitted_failure_cannot_save_or_continue(tmp_path,monkeypatch):
    _,build=builders(tmp_path); t=build()
    import base_sam_trainer
    monkeypatch.setattr(base_sam_trainer,'sam_backward',lambda *args: (_ for _ in ()).throw(RuntimeError('injected')))
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path/'bad.pt')
    with pytest.raises(ValueError): t.step()
