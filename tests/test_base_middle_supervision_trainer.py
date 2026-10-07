from pathlib import Path
import sys
import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_middle_supervision_trainer import MiddleSupervisionTrainer,middle_losses,middle_hidden,committed_state
from natural_context_contrast_corpus import NaturalCorpusTrainer,OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host,right_padded_hidden
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool'; manifest=fixture_pool(pool); p=parent()
    def build(auxiliary=True):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        return (MiddleSupervisionTrainer if auxiliary else NaturalCorpusTrainer)(p,sampler,
            dict(parent={'sha256':'fixture'},weights_role='verification_only'),batch=4,contrast=False,device='cpu')
    return p,build


def math_fixture():
    p=parent(); p['model_config']['num_hidden_layers']=4
    model=JMicroModel(p['model_config'])
    ids=torch.tensor([[2,65,66,67],[2,68,0,0]])
    targets=torch.tensor([[-100,66,67,3],[68,3,-100,-100]])
    return model,ids,targets


def test_independent_per_position_logsoftmax_loss_and_combined_gradient():
    model,ids,targets=math_fixture(); ce,aux,combined=middle_losses(model,ids,targets)
    x=model.model.embed_tokens(ids); positions=torch.arange(4)[None].expand(2,-1)
    for index,layer in enumerate(model.model.layers,1):
        x,_=layer(x,positions,None,None,causal=True)
        if index==2: middle=x
    manual=[]
    for hidden in (x,middle):
        logits=model.lm_head(model.model.norm(hidden)).float()
        terms=[]
        for row,column in targets.ne(-100).nonzero():
            terms.append(torch.logsumexp(logits[row,column],0)-logits[row,column,targets[row,column]])
        manual.append(torch.stack(terms).mean())
    assert torch.allclose(ce,manual[0],atol=1e-6,rtol=0)
    assert torch.allclose(aux,manual[1],atol=1e-6,rtol=0)
    assert torch.allclose(combined,manual[0]+.1*manual[1],atol=1e-6,rtol=0)
    actual=torch.autograd.grad(combined,list(model.parameters()),retain_graph=True)
    expected=torch.autograd.grad(manual[0]+.1*manual[1],list(model.parameters()))
    assert all(torch.allclose(a,b,atol=1e-6,rtol=1e-5) for a,b in zip(actual,expected,strict=True))


def test_auxiliary_gradient_reaches_native_early_layers_and_shared_head_only():
    model,ids,targets=math_fixture(); _,aux,_=middle_losses(model,ids,targets); aux.backward()
    for name,p in model.named_parameters():
        early=not name.startswith('model.layers.') or int(name.split('.')[2])<2
        if early:
            assert p.grad is not None and torch.isfinite(p.grad).all() and p.grad.norm()>0,name
        else: assert p.grad is None,name
    assert model.lm_head.weight is model.model.embed_tokens.weight


def test_disabled_auxiliary_matches_native_final_outputs_and_gradients():
    model,ids,targets=math_fixture(); ce,_,_=middle_losses(model,ids,targets)
    actual=torch.autograd.grad(ce,list(model.parameters()))
    native=F.cross_entropy(model.lm_head(right_padded_hidden(model,ids))[targets.ne(-100)].float(),targets[targets.ne(-100)])
    expected=torch.autograd.grad(native,list(model.parameters()))
    assert torch.equal(ce,native)
    assert all(torch.allclose(a,b,atol=1e-7,rtol=1e-6) for a,b in zip(actual,expected,strict=True))
    final,_=middle_hidden(model,ids)
    assert torch.equal(model.model.norm(final),right_padded_hidden(model,ids))


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
        assert a['middle_gold_evaluations_this_update']==a['CE_targets_this_update']
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


@pytest.mark.parametrize('mutation',['coefficient','kind','evaluations','optimizer','sampler'])
def test_mismatched_recipe_or_uncommitted_state_rejected(tmp_path,mutation):
    _,build=builders(tmp_path); t=build(); t.step(); state=host(t.state_dict())
    if mutation=='coefficient': state['spec']['middle_supervision']['coefficient']=.2
    if mutation=='kind': state['kind']='native_original_CE_only'
    if mutation=='evaluations': state['middle_supervision']['middle_gold_evaluations']+=1
    if mutation=='optimizer': next(iter(state['optimizer']['state'].values()))['step']+=1
    if mutation=='sampler': state['sampler']['consumed']['web']+=1
    torch.save(state,tmp_path/'bad.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'bad.pt')


def test_uncommitted_failure_cannot_save_or_continue(tmp_path,monkeypatch):
    _,build=builders(tmp_path); t=build()
    import base_middle_supervision_trainer
    monkeypatch.setattr(base_middle_supervision_trainer,'middle_losses',lambda *args: (_ for _ in ()).throw(RuntimeError('injected')))
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path/'bad.pt')
    with pytest.raises(ValueError): t.step()
