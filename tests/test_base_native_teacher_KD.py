import copy
from pathlib import Path
import sys
import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_native_teacher_KD_trainer import NativeTeacherKDTrainer,predictive_KL,finite_KD_state
from natural_context_contrast_corpus import NaturalCorpusTrainer,OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool';manifest=fixture_pool(pool);p=parent();teacher=copy.deepcopy(p)
    def build(control=False):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        args=(p,sampler,dict(parent={'sha256':'fixture'},weights_role='verification_only'))
        kwargs=dict(batch=4,contrast=False,device='cpu')
        if control: return NaturalCorpusTrainer(*args,**kwargs)
        return NativeTeacherKDTrainer(*args,teacher_checkpoint=teacher,teacher_reference=dict(sha256='teacher-fixture'),**kwargs)
    return p,teacher,build


def test_T1_full_gold_denominator_gradient_and_teacher_stop_gradient():
    logits=torch.tensor([[.2,.4,-.2],[1.,-.2,.3]],requires_grad=True)
    teacher=torch.tensor([[.8,.1,-.3],[-.4,.8,.2]],requires_grad=True)
    gold=torch.tensor([1,2]);loss,stats=predictive_KL(logits,teacher,gold,10)
    p=logits.softmax(-1);q=teacher.detach().softmax(-1)
    expected=(q*(q.log()-p.log())).sum()/10
    assert torch.allclose(loss,expected,atol=1e-7)
    loss.backward()
    assert torch.allclose(logits.grad,(p.detach()-q)/10,atol=1e-7) and teacher.grad is None
    assert abs(stats['teacher_gold_probability_sum']-float(q.gather(1,gold[:,None]).sum()))<1e-6
    with pytest.raises(ValueError): predictive_KL(logits,teacher,gold,1)


def test_teacher_construction_keeps_student_rng_ties_optimizer_and_weights(tmp_path):
    p,teacher,build=builders(tmp_path);t=build();state=host(t.state_dict());control=build(True)
    assert equal_state(p['model'],state['model']) and equal_state(state['RNG'],host(control.state_dict()['RNG']))
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    assert t.teacher.lm_head.weight is t.teacher.model.embed_tokens.weight and not t.teacher.training
    assert all(not v.requires_grad for v in t.teacher.parameters())
    student_ids={id(v) for v in t.model.parameters()};opt_ids={id(v) for g in t.optimizer.param_groups for v in g['params']}
    assert student_ids==opt_ids and not opt_ids.intersection({id(v) for v in t.teacher.parameters()})
    assert equal_state(teacher['model'],host(t.teacher.state_dict()))


def test_all_gold_masks_sources_and_full_sampler_match_CE_while_KD_counts_only_short(tmp_path):
    _,teacher,build=builders(tmp_path);t,control=build(),build(True)
    for _ in range(4):
        a,b=t.step(),control.step()
        for key in (*t.counters,'draw_trace','lr'): assert equal_state(a[key],b[key]),key
    assert equal_state(t.sampler.state_dict(),control.sampler.state_dict())
    assert t.KD['teacher_positions']==sum(t.counters['source_teachers'][g] for g in ('textbook','story'))>0
    assert t.KD['source_positions']['web']==0
    assert t.KD['teacher_EOS']==sum(t.counters['source_EOS'][g] for g in ('textbook','story'))
    assert finite_KD_state(t.state_dict()) and equal_state(teacher['model'],host(t.teacher.state_dict()))
    assert all(p.grad is None for p in t.teacher.parameters())


def test_all_state_and_history_continuous_vs_real_saved_resume(tmp_path):
    _,_,build=builders(tmp_path);t=build();history=[t.step() for _ in range(4)];expected=host(t.state_dict())
    split=build();other=[split.step() for _ in range(2)];split.save(tmp_path/'split.pt')
    resumed=build();resumed.load(tmp_path/'split.pt');other.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    for a,b in zip(history,other,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
            {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


@pytest.mark.parametrize('mutation',['updates','gold','KD','teacher','temperature','oldkind'])
def test_committed_state_teacher_recipe_and_old_CE_relabel_are_rejected(tmp_path,mutation):
    _,_,build=builders(tmp_path);t=build();t.step();state=host(t.state_dict())
    if mutation=='updates': state['native_teacher_KD']['updates']+=1
    if mutation=='gold': state['counters']['source_teachers']['web']+=1
    if mutation=='KD': state['native_teacher_KD']['teacher_positions']+=1
    if mutation=='teacher': state['spec']['teacher']['sha256']='different-teacher'
    if mutation=='temperature': state['spec']['KD_temperature']=2.
    if mutation=='oldkind': state['kind']='old-CE-state';state.pop('native_teacher_KD')
    torch.save(state,tmp_path/'wrong.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'wrong.pt')
