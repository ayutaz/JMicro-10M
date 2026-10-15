"""Real CPU Adam, original coordinates/stream and strict full-state resume."""
import copy
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from scalegrad_trainer import ScaleGradTrainer,committed_state
from jmicro.phase5 import equal_state
from jmicro.scalegrad import ARMS
from natural_context_contrast_trainer import host
from test_document_progress_training import builders as original_builders


def builders(tmp_path):
    parent,old_build = original_builders(tmp_path)
    def build(arm='scalegrad',legacy=False):
        old=old_build(legacy=True)
        if legacy: return old
        return ScaleGradTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    return build


def test_disabled4_ALL_native_weights_Adam_RNG_CE_gradient_source_exact(tmp_path):
    build=builders(tmp_path)
    control=build('native_CE_control')
    initial=host(control.state_dict())
    rows,states=[],[]
    for _ in range(4):
        rows.append(control.step())
        states.append(host(control.state_dict()))
    native=build(legacy=True)
    assert equal_state(initial['model'],native.state_dict()['model'])
    for row,state in zip(rows,states,strict=True):
        expected=native.step()
        for key in ('model','optimizer','scheduler','RNG','sampler'):
            assert equal_state(state[key],host(native.state_dict()[key])),key
        for key in ('CE_loss','gradient_norm','token_digest','source_teachers','source_EOS',
                'CE_input_tokens','physical_input_tokens','original_body_bytes','draw_trace','lr'):
            assert equal_state(row[key],expected[key]),key
        assert row['combined_loss']==row['CE_loss']
        assert row['modified_loss_evaluations']==0
        assert row['total_CE_evaluations']==row['supervised_tokens']


def test_active4_same_original_stream_no_extra_parameters_and_honest_loss_clocks(tmp_path):
    build=builders(tmp_path)
    active,native=build(),build(legacy=True)
    before=host(active.state_dict())
    for _ in range(4):
        a,b=active.step(),native.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
                'physical_input_tokens','original_body_bytes','token_digest','draw_trace','lr'):
            assert equal_state(a[key],b[key]),key
        assert a['modified_loss_evaluations']==a['original_CE_metric_evaluations']==a['supervised_tokens']
        assert a['total_CE_evaluations']==2*a['supervised_tokens']
        assert a['novel_gold_positions']==a['novel_body_gold_positions']+a['novel_EOS_gold_positions']
        assert a['novel_EOS_gold_positions']==sum(a['source_EOS'].values())
        assert 0<a['novel_body_gold_positions']<a['supervised_tokens']
        assert a['decoder_forwards_this_update']==1 and a['auxiliary_input_tokens']==0
        assert committed_state(active.state_dict())
    after=host(active.state_dict())
    assert not equal_state(after['model'],native.state_dict()['model'])
    assert equal_state(before['RNG'],after['RNG'])
    assert after['spec']['native_parameters']==after['spec']['training_parameters']
    assert after['spec']['train_only_parameters']==0


@pytest.mark.parametrize('arm',ARMS)
def test_BOTH6vs3_save3_ALL_numerical_state_sampler_RNG_history_exact(tmp_path,arm):
    build=builders(tmp_path)
    full=build(arm)
    history=[full.step() for _ in range(6)]
    expected=host(full.state_dict())
    split=build(arm)
    rows=[split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed=build(arm)
    resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(3))
    assert equal_state(expected,host(resumed.state_dict()))
    strip=lambda rs:[{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')} for r in rs]
    assert equal_state(strip(history),strip(rows))


@pytest.mark.parametrize('bad',['policy','gamma','kind','role','optimizer','schedule','model_nan','RNG',
    'sampler_binding','modified_loss','novel_gold','physical','parameter_count'])
def test_bad_state_refused_before_ANY_mutation(tmp_path,bad):
    build=builders(tmp_path)
    current=build()
    current.step()
    state=host(current.state_dict())
    if bad=='policy': state['spec']['scalegrad_policy']['gamma']=.5
    elif bad=='gamma': state['spec']['gamma']=.5
    elif bad=='kind': state['kind']='native'
    elif bad=='role': state['binding']['weights_role']='other'
    elif bad=='optimizer': next(iter(state['optimizer']['state'].values()))['step']+=1
    elif bad=='schedule': state['scheduler']['last_epoch']+=1
    elif bad=='model_nan': state['model']['model.norm.weight'][0]=float('nan')
    elif bad=='RNG': state['RNG']={}
    elif bad=='sampler_binding': state['sampler']['binding']['pool']='other'
    elif bad=='modified_loss': state['counters']['modified_loss_evaluations']+=1
    elif bad=='novel_gold': state['counters']['novel_gold_positions']+=1
    elif bad=='physical': state['counters']['physical_input_tokens']=0
    else: state['spec']['native_parameters']+=1
    assert not committed_state(state)
    torch.save(state,tmp_path/'invalid.pt')
    target=build()
    before=host(target.state_dict())
    with pytest.raises(ValueError): target.load(tmp_path/'invalid.pt')
    assert equal_state(before,host(target.state_dict()))


def test_native_checkpoint_cannot_be_relabelled_as_new_scientific_state(tmp_path):
    build=builders(tmp_path)
    old=build(legacy=True)
    old.step()
    old.save(tmp_path/'native.pt')
    current=build()
    before=host(current.state_dict())
    with pytest.raises(ValueError): current.load(tmp_path/'native.pt')
    assert equal_state(before,host(current.state_dict()))


def test_after_Adam_failure_no_save_or_retry_before_completed_restore(tmp_path,monkeypatch):
    build=builders(tmp_path)
    current=build()
    current.save(tmp_path/'zero.pt')
    expected=host(current.state_dict())
    step=current.optimizer.step
    def interrupted(*args,**kwargs):
        step(*args,**kwargs)
        raise RuntimeError('after Adam')
    monkeypatch.setattr(current.optimizer,'step',interrupted)
    with pytest.raises(RuntimeError): current.step()
    with pytest.raises(ValueError): current.step()
    with pytest.raises(ValueError): current.save(tmp_path/'dirty.pt')
    current.load(tmp_path/'zero.pt')
    assert equal_state(expected,host(current.state_dict()))
