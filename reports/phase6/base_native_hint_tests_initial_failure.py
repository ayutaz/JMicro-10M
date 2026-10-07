"""Native hint numerics and protocol fixtures, not Japanese model quality."""
import copy
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_native_hint_trainer import NativeHintTrainer,hidden_with_hint,hint_loss,committed_state,RECIPE
from natural_context_contrast_corpus import NaturalCorpusTrainer,OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host,right_padded_hidden
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path,web_only=False):
    pool=tmp_path/'pool'; manifest=fixture_pool(pool); p=parent(); teacher=copy.deepcopy(p)
    for key,value in teacher['model'].items():
        if '.layers.0.' in key and value.ndim==2: value.add_(.03*torch.randn_like(value))
    goals=dict(web=7500,textbook=0 if web_only else 2000,story=0 if web_only else 500)
    def build(control=False):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),goals)
        args=(p,sampler,dict(parent={'sha256':'fixture'},weights_role='verification_only'))
        if control: return NaturalCorpusTrainer(*args,batch=4,device='cpu')
        return NativeHintTrainer(*args,teacher_checkpoint=teacher,
            teacher_reference=dict(sha256='fixture_teacher'),batch=4,device='cpu')
    return p,teacher,build


def test_independent_angular_loss_gradient_denominator_teacher_detach():
    x=torch.tensor([[3.,4.],[-2.,1.]],requires_grad=True)
    y=torch.tensor([[4.,3.],[1.,2.]],requires_grad=True)
    loss=hint_loss(x,y,10)
    nx=x.detach().norm(dim=-1,keepdim=True); ny=y.detach().norm(dim=-1,keepdim=True)
    dot=(x.detach()*y.detach()).sum(-1,keepdim=True)/(nx*ny)
    assert torch.allclose(loss,(1-dot).sum()/10,atol=1e-7)
    loss.backward()
    expected=(dot*x.detach()/nx.square()-y.detach()/(nx*ny))/10
    assert torch.allclose(x.grad,expected,atol=1e-7) and y.grad is None
    assert torch.allclose(loss.detach(),hint_loss(x.detach()*3,y.detach()*2,10),atol=1e-7)
    with pytest.raises(ValueError): hint_loss(x,y,1)
    with pytest.raises(ValueError): hint_loss(x,torch.full_like(y,float('nan')),10)


def test_unchanged_full_native_forward_and_teacher_stops_exact_middle():
    config=parent()['model_config'].copy(); config['num_hidden_layers']=4
    model=JMicroModel(config); ids=torch.tensor([[2,65,66,67],[2,68,0,0]])
    final,middle=hidden_with_hint(model,ids)
    assert equal_state(model.model.norm(final),right_padded_hidden(model,ids))
    def forbidden(*_): raise AssertionError('Teacher must not run upper layers/norm/head')
    hooks=[module.register_forward_hook(forbidden) for module in
           (model.model.layers[2],model.model.norm,model.lm_head)]
    try:
        stopped,hint=hidden_with_hint(model,ids,teacher_only=True)
        assert stopped is None and equal_state(hint,middle)
    finally:
        for hook in hooks: hook.remove()
    # Strictly right-padded future positions cannot change valid causal hints.
    _,trimmed=hidden_with_hint(model,ids[1:2,:2],teacher_only=True)
    assert torch.allclose(trimmed,hint[1:2,:2],atol=1e-6)


def test_teacher_is_frozen_student_only_optimizer_and_rng_preserved(tmp_path):
    p,teacher,build=builders(tmp_path); t=build(); control=build(True)
    assert equal_state(p['model'],host(t.model.state_dict()))
    assert equal_state(host(t.state_dict())['RNG'],host(control.state_dict())['RNG'])
    student={id(v) for v in t.model.parameters()}
    optimizer={id(v) for g in t.optimizer.param_groups for v in g['params']}
    assert student==optimizer and not optimizer.intersection({id(v) for v in t.teacher.parameters()})
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    assert not t.teacher.training and all(not v.requires_grad for v in t.teacher.parameters())
    assert equal_state(teacher['model'],host(t.teacher.state_dict()))


def test_same_original_stream_masks_EOS_with_short_only_hints(tmp_path):
    _,teacher,build=builders(tmp_path); t=build(); control=build(True)
    for _ in range(4):
        a,b=t.step(),control.step()
        for key in (*t.counters,'draw_trace','lr'): assert equal_state(a[key],b[key]),key
        assert a['CE_targets_this_update']>=a['hint_positions_this_update']
        assert a['combined_loss']==pytest.approx(a['CE_loss']+a['hint_loss'],abs=2e-6)
    h=t.native_hint
    assert h['positions']==sum(t.counters['source_teachers'][g] for g in RECIPE['sources'])>0
    assert h['EOS']==sum(t.counters['source_EOS'][g] for g in RECIPE['sources'])
    assert h['source_positions']['web']==0 and h['angular_penalty_sum']>0
    assert committed_state(host(t.state_dict()))
    assert equal_state(teacher['model'],host(t.teacher.state_dict()))
    assert all(v.grad is None for v in t.teacher.parameters())


def test_web_only_no_teacher_compute_and_original_CE_parity(tmp_path):
    _,_,build=builders(tmp_path,web_only=True); t=build(); control=build(True)
    def forbidden(*_): raise AssertionError('No teacher compute for Web-only gold')
    hook=t.teacher.model.embed_tokens.register_forward_hook(forbidden)
    try:
        a,b=t.step(),control.step()
    finally: hook.remove()
    assert a['hint_loss']==0 and a['hint_positions_this_update']==0
    assert a['teacher_physical_inputs_this_update']==0
    assert a['CE_loss']==b['CE_loss']
    assert equal_state(host(t.model.state_dict()),host(control.model.state_dict()))


def test_full_state_real_save_resume4vs2plus2(tmp_path):
    _,_,build=builders(tmp_path); t=build(); history=[t.step() for _ in range(4)]
    expected=host(t.state_dict()); split=build(); actual=[split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt'); resumed=build(); resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    for a,b in zip(history,actual,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


def test_post_optimizer_failure_cannot_save_or_continue(tmp_path,monkeypatch):
    _,_,build=builders(tmp_path); t=build(); step=t.optimizer.step
    def fail():
        step()
        raise RuntimeError('Injected between Adam and committed counters')
    monkeypatch.setattr(t.optimizer,'step',fail)
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path/'invalid.pt')
    with pytest.raises(ValueError): t.step()
    assert not (tmp_path/'invalid.pt').exists()


@pytest.mark.parametrize('mutation',['recipe','teacher','positions','Adam','sampler','old_kind'])
def test_incompatible_or_partial_states_cannot_be_reused(tmp_path,mutation):
    _,_,build=builders(tmp_path); t=build(); t.step(); state=host(t.state_dict())
    if mutation=='recipe': state['spec']['native_hint']['coefficient']=2.
    if mutation=='teacher': state['spec']['teacher']['sha256']='other'
    if mutation=='positions': state['native_hint']['positions']+=1
    if mutation=='Adam': next(iter(state['optimizer']['state'].values()))['step']+=1
    if mutation=='sampler': state['sampler']['consumed']['web']+=1
    if mutation=='old_kind': state['kind']='old_native_predictive_KD'
    torch.save(state,tmp_path/'invalid.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'invalid.pt')
