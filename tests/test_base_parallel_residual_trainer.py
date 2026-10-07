"""Original gold equality, actual full resume and refusal after partial Adam."""
import copy
from pathlib import Path
import sys
import pytest
import torch
from torch.nn import functional as F
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_parallel_residual_model import parallel_config
from base_parallel_residual_trainer import FreshResidualTrainer,committed_state
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from natural_context_contrast_trainer import host,right_pad
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


@pytest.fixture
def builders(tmp_path):
    pool=tmp_path/'pool';manifest=fixture_pool(pool)
    native=copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        native['expected_parameter_count']=sum(p.numel() for p in JMicroModel(native).parameters())
    configs=dict(sequential=native,parallel=parallel_config(native))
    def source():return CEOnlyOriginalSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
    def build(arm='parallel',warmup=1000):
        return FreshResidualTrainer(configs[arm],source(),dict(proposal='fixture'),arm,batch=4,device='cpu',warmup=warmup)
    return source,build


@pytest.mark.parametrize('arm',['sequential','parallel'])
def test_actual_postwarmup_cosine_updates_remain_saveable(builders,tmp_path,arm):
    _,build=builders;t=build(arm,warmup=1)
    for _ in range(16):
        if t.sampler.exhausted:break
        row=t.step()
        assert row['supervised_tokens']>t.scheduler.warmup
        assert row['lr']==t.scheduler.value(row['supervised_tokens'])
        assert committed_state(t.state_dict())
    assert t.counters['supervised_tokens']==sum(t.sampler.goals.values())
    cp=tmp_path/(arm+'-cosine.pt');t.save(cp)
    restored=build(arm,warmup=1);restored.load(cp)
    assert equal_state(host(t.state_dict()),host(restored.state_dict()))


def test_same_initial_every_weight_RNG_original_masked_CE_EOS_and_schedule(builders):
    source,build=builders;sequential=build('sequential')
    initial_RNG=host(sequential.state_dict()['RNG']);parallel=build()
    assert equal_state(host(sequential.model.state_dict()),host(parallel.model.state_dict()))
    assert equal_state(initial_RNG,parallel.state_dict()['RNG'])
    assert not sequential.optimizer.state and not parallel.optimizer.state
    rows=source().take(4);ids,_=right_pad([r['input_ids'] for r in rows],'cpu')
    targets=torch.full_like(ids,-100)
    for i,row in enumerate(rows):targets[i,:len(row['target_ids'])]=torch.tensor(row['target_ids'])
    expected=F.cross_entropy(parallel.model(ids).logits.reshape(-1,128),targets.reshape(-1),ignore_index=-100)
    first,other=parallel.step(),sequential.step()
    assert first['CE_loss']==pytest.approx(float(expected.detach()),abs=1e-6)
    for _ in range(3):
        for key in (*parallel.counters,'draw_trace','lr'):
            assert equal_state(first[key],other[key]),key
        first,other=parallel.step(),sequential.step()
    assert equal_state(parallel.sampler.state_dict(),sequential.sampler.state_dict())
    assert sum(parallel.counters['source_EOS'].values())>0
    assert parallel.counters['supervised_tokens']==parallel.scheduler.tokens


@pytest.mark.parametrize('arm',['sequential','parallel'])
def test_continuous4_vs_saved2_resume2_allstate_history(builders,tmp_path,arm):
    _,build=builders;continuous=build(arm)
    full=[continuous.step() for _ in range(4)];expected=host(continuous.state_dict())
    split=build(arm);rows=[split.step() for _ in range(2)];path=tmp_path/'state.pt';split.save(path)
    resumed=build(arm);resumed.load(path);rows.extend(resumed.step() for _ in range(2))
    assert committed_state(expected) and equal_state(expected,host(resumed.state_dict()))
    for a,b in zip(full,rows,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


@pytest.mark.parametrize('field',['arm','policy','class','Adam','sampler','scheduler','nonfinite'])
def test_malformed_state_refused_before_weights_change(builders,tmp_path,field):
    _,build=builders;t=build();t.step();state=copy.deepcopy(host(t.state_dict()))
    if field=='arm':state['spec']['arm']='sequential'
    if field=='policy':state['spec']['residual_policy']['residual_gain']=.5
    if field=='class':state['spec']['model_class']='JMicroModel'
    if field=='Adam':next(iter(state['optimizer']['state'].values()))['step'].zero_()
    if field=='sampler':state['sampler']['consumed']['web']+=1
    if field=='scheduler':state['scheduler']['tokens']-=1
    if field=='nonfinite':next(iter(state['model'].values())).fill_(float('nan'))
    assert not committed_state(state)
    path=tmp_path/'bad.pt';torch.save(state,path);recipient=build();before=host(recipient.model.state_dict())
    with pytest.raises(ValueError):recipient.load(path)
    assert equal_state(before,host(recipient.model.state_dict()))


def test_error_after_Adam_refuses_save_and_continue(builders,tmp_path):
    _,build=builders;t=build();original=t.optimizer.step
    def interrupted(*args,**kwargs):
        original(*args,**kwargs);raise RuntimeError('After Adam fixture failure')
    t.optimizer.step=interrupted
    with pytest.raises(RuntimeError):t.step()
    with pytest.raises(ValueError):t.save(tmp_path/'partial.pt')
    with pytest.raises(ValueError):t.step()
