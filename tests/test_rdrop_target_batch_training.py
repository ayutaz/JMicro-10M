"""Every numerical coordinate and RNG/history must equal the frozen reference."""
import copy
from pathlib import Path
import sys

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from rdrop_analytic_trainer import AnalyticRDropTrainer
from rdrop_target_batch_trainer import TargetBatchRDropTrainer,committed_state
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from jmicro.rdrop import ARMS
from test_rdrop_training import builders as reference_builders


def builders(tmp_path):
    parent,reference = reference_builders(tmp_path)
    def build(arm='normalized_rdrop'):
        old = reference(legacy=True)
        return TargetBatchRDropTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    def baseline(arm='normalized_rdrop'):
        old = reference(legacy=True)
        return AnalyticRDropTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    return baseline,build

def only_runtime_labels_removed(state):
    result = host(state)
    for key in ('spec','lineage'):
        result[key].pop('input_runtime',None)
        result[key]['kind'] = 'REFERENCE_LABEL_ONLY'
    result['kind'] = 'REFERENCE_LABEL_ONLY'
    return result


@pytest.mark.parametrize('arm',ARMS)
def test_reference4_ALL_weights_Adam_RNG_sampler_counters_history_EXACT(tmp_path,arm):
    reference,build = builders(tmp_path)
    old = reference(arm)
    initial = only_runtime_labels_removed(old.state_dict())
    rows,snapshots = [],[]
    for _ in range(4):
        rows.append(old.step())
        snapshots.append(only_runtime_labels_removed(old.state_dict()))
    current = build(arm)
    assert equal_state(initial,only_runtime_labels_removed(current.state_dict()))
    strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    for row,snapshot in zip(rows,snapshots,strict=True):
        actual = current.step()
        assert equal_state(strip(row),strip(actual))
        assert equal_state(snapshot,only_runtime_labels_removed(current.state_dict()))


@pytest.mark.parametrize('arm',ARMS)
def test_BOTH6vs3_save3_ALL_typed_state_and_stochastic_history_EXACT(tmp_path,arm):
    _,build = builders(tmp_path)
    full = build(arm)
    history = [full.step() for _ in range(6)]
    expected = host(full.state_dict())
    split = build(arm)
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed = build(arm)
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected,host(resumed.state_dict()))
    strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(r) for r in history],[strip(r) for r in actual])


@pytest.mark.parametrize('bad',['runtime','lineage','optimizer','RNG','second_view','sampler','weights'])
def test_bad_typed_state_refused_before_mutation(tmp_path,bad):
    _,build = builders(tmp_path)
    old = build()
    old.step()
    state = host(old.state_dict())
    if bad == 'runtime': state['spec']['input_runtime'] = 'reference'
    elif bad == 'lineage': state['lineage']['input_runtime'] = 'reference'
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'RNG': state['RNG'] = {}
    elif bad == 'second_view': state['counters']['second_view_gold_evaluations'] += 1
    elif bad == 'sampler': state['sampler']['binding']['pool'] = 'other'
    else: state['model']['model.norm.weight'][0] = float('nan')
    assert not committed_state(state)
    old_path = tmp_path/'invalid.pt'
    import torch
    torch.save(state,old_path)
    target = build()
    before = host(target.state_dict())
    with pytest.raises(ValueError): target.load(old_path)
    assert equal_state(before,host(target.state_dict()))


def test_reference_checkpoint_not_silently_relabelled_or_loaded(tmp_path):
    reference,build = builders(tmp_path)
    old = reference()
    old.step()
    old.save(tmp_path/'reference.pt')
    current = build()
    before = host(current.state_dict())
    with pytest.raises(ValueError): current.load(tmp_path/'reference.pt')
    assert equal_state(before,host(current.state_dict()))


def test_after_Adam_interruption_no_save_or_retry_until_completed_restore(tmp_path,monkeypatch):
    _,build = builders(tmp_path)
    current = build()
    current.save(tmp_path/'zero.pt')
    before = host(current.state_dict())
    original = current.optimizer.step
    def interrupted(*args,**kwargs):
        original(*args,**kwargs)
        raise RuntimeError('After Adam')
    monkeypatch.setattr(current.optimizer,'step',interrupted)
    with pytest.raises(RuntimeError): current.step()
    with pytest.raises(ValueError): current.step()
    with pytest.raises(ValueError): current.save(tmp_path/'dirty.pt')
    current.load(tmp_path/'zero.pt')
    assert equal_state(before,host(current.state_dict()))


def test_runtime_comparison_does_not_hide_loss_or_numerical_differences(tmp_path):
    baseline,build = builders(tmp_path)
    a,b = baseline().state_dict(),build().state_dict()
    assert equal_state(only_runtime_labels_removed(a),only_runtime_labels_removed(b))
    for key in ('model','optimizer','RNG','sampler','counters'):
        bad = copy.deepcopy(b)
        bad[key]['changed_payload'] = 1
        assert not equal_state(only_runtime_labels_removed(a),only_runtime_labels_removed(bad))
    bad = copy.deepcopy(b)
    bad['spec']['loss_runtime'] = 'different_loss'
    assert not committed_state(bad)
    assert not equal_state(only_runtime_labels_removed(a),only_runtime_labels_removed(bad))
    for key in ('spec','lineage'):
        bad = copy.deepcopy(b)
        del bad[key]['input_runtime']
        assert not committed_state(bad)
