"""CPU real Adam/native identity and whole-state interrupted execution proof."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from quiet_attention_trainer import QuietTrainer, committed_state
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from jmicro.quiet_attention import ARMS, TAG
from test_pseudo_repetition_training import builders as original_builders


def builders(tmp_path):
    parent, old_build = original_builders(tmp_path)
    parent['model_config']['expected_parameter_count'] = sum(v.numel() for k,v in parent['model'].items() if k != 'lm_head.weight')
    def build(arm='fixed_zero',legacy=False):
        old = old_build(legacy=True)
        if legacy:
            return old
        return QuietTrainer(parent,old.sampler,old.binding,batch=6,device='cpu',arm=arm)
    return parent,build


def test_disabled4_all_original_weights_Adam_CE_gradient_norm_source_schedule_RNG_exact(tmp_path):
    _,build = builders(tmp_path)
    current = build('disabled_native')
    initial = host(current.state_dict())
    snapshots,histories = [],[]
    for _ in range(4):
        histories.append(current.step())
        snapshots.append(host(current.state_dict()))
    old = build(legacy=True)
    assert equal_state(initial['RNG'],host(old.state_dict())['RNG'])
    assert [n for n,_ in current.model.named_parameters()] == [n for n,_ in old.model.named_parameters()]
    for a,saved in zip(histories,snapshots,strict=True):
        b = old.step()
        native_state = host(old.state_dict())
        assert all(torch.equal(saved['model'][k],v) for k,v in native_state['model'].items())
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens',
                    'original_body_bytes','token_digest','draw_trace','CE_loss','gradient_norm','lr'):
            assert equal_state(a[key],b[key]),key
        for key in ('optimizer','scheduler','RNG','sampler'):
            assert equal_state(saved[key],native_state[key]),key
        assert a['quiet_real_query_slots'] == 0
    assert committed_state(current.state_dict())


def test_enabled_original_teacher_stream_and_no_extra_parameters_or_targets(tmp_path):
    _,build = builders(tmp_path)
    current,old = build(),build(legacy=True)
    assert [n for n,_ in current.model.named_parameters()] == [n for n,_ in old.model.named_parameters()]
    for _ in range(4):
        a,b = current.step(),old.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
                    'original_body_bytes','token_digest','draw_trace','lr','physical_input_tokens'):
            assert equal_state(a[key],b[key]),key
        assert equal_state(current.sampler.state_dict(),old.sampler.state_dict())
        c = current.model.config
        assert a['quiet_real_query_slots'] == a['physical_input_tokens']*c['num_hidden_layers']*c['num_attention_heads']
        assert a['auxiliary_pairs'] == a['auxiliary_input_tokens'] == 0
    assert not torch.equal(current.model.model.embed_tokens.weight,old.model.model.embed_tokens.weight)
    assert committed_state(current.state_dict())


@pytest.mark.parametrize('arm',ARMS)
def test_full6_vs3_save_resume3_ALL_model_Adam_RNG_sampler_counters_and_history_exact(tmp_path,arm):
    _,build = builders(tmp_path)
    continuous = build(arm)
    history = [continuous.step() for _ in range(6)]
    expected = host(continuous.state_dict())
    split = build(arm)
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed = build(arm)
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected,host(resumed.state_dict()))
    strip = lambda row:{k:v for k,v in row.items() if k not in ('seconds','data_wait_seconds')}
    assert equal_state([strip(r) for r in history],[strip(r) for r in actual])


@pytest.mark.parametrize('bad',['policy','kind','source_RNG','source_binding','optimizer','clock','nonfinite','compute_clock','runtime_arm'])
def test_corrupt_checkpoint_rejected_before_current_state_mutation(tmp_path,bad):
    _,build = builders(tmp_path)
    source = build()
    source.step()
    state = host(source.state_dict())
    if bad == 'policy': state['model_config'][TAG]['policy']['phantom_logit'] = 1.
    elif bad == 'kind': state['kind'] = 'native'
    elif bad == 'source_RNG': state['sampler']['RNG'] = 'INVALID'
    elif bad == 'source_binding': state['sampler']['binding']['pool'] = 'wrong'
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'clock': state['scheduler']['last_epoch'] += 1
    elif bad == 'nonfinite': state['model']['model.norm.weight'].fill_(torch.nan)
    elif bad == 'runtime_arm': state['model']['quiet_runtime'][1] = 1
    else: state['counters']['quiet_real_query_slots'] += 1
    assert not committed_state(state)
    torch.save(state,tmp_path/'bad.pt')
    current = build()
    before = host(current.state_dict())
    with pytest.raises(ValueError): current.load(tmp_path/'bad.pt')
    assert equal_state(before,host(current.state_dict()))


def test_after_Adam_mutation_cannot_save_retry_but_valid_completed_restore_works(tmp_path,monkeypatch):
    _,build = builders(tmp_path)
    current = build()
    current.save(tmp_path/'initial.pt')
    original = current.optimizer.step
    def interrupted(*args,**kwargs):
        original(*args,**kwargs)
        raise RuntimeError('After Adam mutation')
    monkeypatch.setattr(current.optimizer,'step',interrupted)
    with pytest.raises(RuntimeError): current.step()
    with pytest.raises(ValueError): current.save(tmp_path/'invalid.pt')
    with pytest.raises(ValueError): current.step()
    assert not (tmp_path/'invalid.pt').exists()
    monkeypatch.setattr(current.optimizer,'step',original)
    current.load(tmp_path/'initial.pt')
    current.step()
    clean = build()
    clean.step()
    assert equal_state(host(current.state_dict()),host(clean.state_dict()))


@pytest.mark.parametrize('field',['spec','lineage','model_config'])
def test_explicit_runtime_required_before_state_mutation(tmp_path,field):
    _,build = builders(tmp_path)
    current = build()
    before = host(current.state_dict())
    bad = copy.deepcopy(before)
    if field == 'model_config': bad[field][TAG]['implementation'] = 'native'
    else: bad[field]['attention_implementation'] = 'independent_map'
    assert not committed_state(bad)
    torch.save(bad,tmp_path/'wrong.pt')
    with pytest.raises(ValueError): current.load(tmp_path/'wrong.pt')
    assert equal_state(before,host(current.state_dict()))


def test_native_and_disabled_checkpoints_not_silently_loaded_as_enabled(tmp_path):
    _,build = builders(tmp_path)
    current = build()
    before = host(current.state_dict())
    for name,source in (('disabled',build('disabled_native')),('native',build(legacy=True))):
        source.save(tmp_path/(name+'.pt'))
        with pytest.raises(ValueError): current.load(tmp_path/(name+'.pt'))
        assert equal_state(before,host(current.state_dict()))
