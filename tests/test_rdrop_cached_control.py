"""Original-coordinate compatibility with the prior zero-head CE25M protocol."""
from pathlib import Path
import sys

import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from rdrop_trainer import RDropTrainer,committed_state
from jmicro.phase5 import equal_state
from natural_context_contrast_trainer import host
from test_document_progress_training import builders


def test_fresh_disabled4_equals_old_zero_head_control_every_original_Adam_coordinate(tmp_path):
    parent,old_build = builders(tmp_path)
    old = old_build('native_CE_control')
    initial = host(old.state_dict())
    snapshots,rows = [],[]
    for _ in range(4):
        rows.append(old.step())
        snapshots.append(host(old.state_dict()))
    native = old_build(legacy=True)
    current = RDropTrainer(parent,native.sampler,native.binding,batch=6,device='cpu',arm='disabled_native')
    assert equal_state(initial['model'],current.model.state_dict())
    assert equal_state(initial['RNG'],host(current.state_dict())['RNG'])
    for expected,snapshot in zip(rows,snapshots,strict=True):
        actual = current.step()
        state = host(current.state_dict())
        for key in ('model','sampler','scheduler','RNG'):
            assert equal_state(snapshot[key],state[key]),key
        for key in ('CE_loss','gradient_norm','token_digest','source_teachers','source_EOS','CE_input_tokens',
                'physical_input_tokens','original_body_bytes','draw_trace','lr'):
            assert equal_state(expected[key],actual[key]),key
        names = [n for n,_ in current.model.named_parameters()]
        previous = dict(zip(names,snapshot['optimizer']['param_groups'][0]['params'][:-1],strict=True))
        present = dict(zip(names,state['optimizer']['param_groups'][0]['params'],strict=True))
        for name in names:
            assert equal_state(snapshot['optimizer']['state'][previous[name]],state['optimizer']['state'][present[name]]),name
        old_group,new_group = snapshot['optimizer']['param_groups'][0],state['optimizer']['param_groups'][0]
        assert {k:v for k,v in old_group.items() if k != 'params'} == {k:v for k,v in new_group.items() if k != 'params'}
        assert torch.count_nonzero(snapshot['progress_head']['weight']) == 0
    assert committed_state(current.state_dict())


def test_cached_typed_endpoint_is_reference_only_not_new_trainer_or_initializer(tmp_path):
    parent,old_build = builders(tmp_path)
    old = old_build('native_CE_control')
    old.step()
    path = tmp_path/'old-control.pt'
    old.save(path)
    native = old_build(legacy=True)
    current = RDropTrainer(parent,native.sampler,native.binding,batch=6,device='cpu')
    before = host(current.state_dict())
    assert not committed_state(host(old.state_dict()))
    with pytest.raises(ValueError): current.load(path)
    assert equal_state(before,host(current.state_dict()))
