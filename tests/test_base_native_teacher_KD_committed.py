import copy
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_native_teacher_KD_committed import CommittedNativeTeacherKDTrainer,committed_state
from base_native_teacher_KD_trainer import NativeTeacherKDTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool'; manifest=fixture_pool(pool); p=parent(); teacher=copy.deepcopy(p)
    def build(guard=True):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        return (CommittedNativeTeacherKDTrainer if guard else NativeTeacherKDTrainer)(p,sampler,
            dict(parent={'sha256':'fixture'},weights_role='verification_only'),teacher,
            dict(path='fixture_teacher',sha256='fixture'),batch=4,device='cpu')
    return build


def test_boundary_preserves_original_frozen_KD_numerics_and_source(tmp_path):
    build=builders(tmp_path); guarded,original=build(),build(False)
    for _ in range(4):
        a,b=guarded.step(),original.step()
        assert a['committed_update'] is True
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds','committed_update')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})
    left,right=host(guarded.state_dict()),host(original.state_dict())
    assert all(equal_state(left[k],right[k]) for k in left if k!='spec')
    assert committed_state(left) and left['native_teacher_KD']['teacher_positions']>0
    assert all(p.grad is None for p in guarded.teacher.parameters())


def test_continuous_vs_saved2plus2_complete_state_and_history(tmp_path):
    build=builders(tmp_path); t=build(); history=[t.step() for _ in range(4)]; expected=host(t.state_dict())
    split=build(); actual=[split.step() for _ in range(2)]; split.save(tmp_path/'split.pt')
    resumed=build(); resumed.load(tmp_path/'split.pt'); actual.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    assert all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(history,actual,strict=True))


def test_failure_after_optimizer_cannot_save_or_continue(tmp_path,monkeypatch):
    t=builders(tmp_path)(); step=t.optimizer.step
    def interrupted():
        step()
        raise RuntimeError('injected after Adam before counters')
    monkeypatch.setattr(t.optimizer,'step',interrupted)
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path/'invalid.pt')
    with pytest.raises(ValueError): t.step()
    assert not (tmp_path/'invalid.pt').exists()


@pytest.mark.parametrize('field',['KD_updates','Adam_step','boundary','source_positions','sampler'])
def test_mismatched_committed_boundary_rejected(tmp_path,field):
    build=builders(tmp_path); t=build(); t.step(); state=host(t.state_dict())
    if field=='KD_updates': state['native_teacher_KD']['updates']+=1
    if field=='Adam_step': next(iter(state['optimizer']['state'].values()))['step']+=1
    if field=='boundary': state['spec']['commit_boundary']='unfinished'
    if field=='source_positions': state['native_teacher_KD']['source_positions']['web']=1
    if field=='sampler': state['sampler']['consumed']['web']+=1
    assert not committed_state(state)
    torch.save(state,tmp_path/'bad.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'bad.pt')


def test_old_probe_state_is_not_a_new_study_checkpoint(tmp_path):
    build=builders(tmp_path); original=build(False); original.step(); original.save(tmp_path/'old.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'old.pt')
