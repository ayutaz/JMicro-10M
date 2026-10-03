"""Check milestone/resume safety before the future long Base run is started."""
from pathlib import Path
import importlib.util
import sys

import pytest

from jmicro.experiment import ROOT, sha256, write_json

sys.path.insert(0, str(ROOT/'scripts'))
spec = importlib.util.spec_from_file_location('base_launcher', ROOT/'scripts/run_base.py')
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


def configuration():
    return dict(model='reports/phase6/base_model.json', shards='/fixed/shards', dtype='bf16',
        schedule_updates=305176, seed=42, context=1024, batch=32, accumulation=1,
        lr=.002, weight_decay=.1, warmup=200, save_every=1000, log_every=50,
        minimum_lr_ratio=.1, variant={'backend':'flash','compile_mode':'reduce-overhead'},
        milestones={'500M':{'stable_updates':15259,'decay_updates':763,'decay_end_update':16022},
                    '1B':{'stable_updates':30518,'decay_updates':1526,'decay_end_update':32044}})


def test_observation_and_resume_preserve_global_schedule(tmp_path):
    config=configuration()
    first=launcher.prepare(config,'500M',tmp_path,'stable')['commands'][0]
    stable=tmp_path/'stable'
    stable.mkdir()
    checkpoint=stable/'checkpoint-00015259.pt'
    checkpoint.write_bytes(b'saved completed checkpoint fixture')
    write_json(stable/'latest.json',{'path':str(checkpoint),'sha256':sha256(checkpoint),'update':15259})
    second=launcher.prepare(config,'1B',tmp_path,'stable')['commands'][0]
    for command in (first,second):
        assert command[command.index('--schedule-updates')+1]=='305176'
    assert first[first.index('--stop-after')+1]=='15259'
    assert second[second.index('--stop-after')+1]=='30518'
    assert second[second.index('--resume')+1]==str(checkpoint)
    checkpoint.write_bytes(b'corrupted checkpoint')
    with pytest.raises(AssertionError,match='checksum'):
        launcher.prepare(config,'1B',tmp_path,'stable')


def test_decay_requires_parent_and_keeps_it_immutable(tmp_path):
    config=configuration()
    with pytest.raises(AssertionError,match='observation checkpoint'):
        launcher.prepare(config,'500M',tmp_path,'decay')
    parent=tmp_path/'stable/checkpoint-00015259.pt'
    parent.parent.mkdir()
    parent.write_bytes(b'completed observation checkpoint fixture')
    before=sha256(parent)
    command=launcher.prepare(config,'500M',tmp_path,'decay')['commands'][0]
    assert command[command.index('--branch-from')+1]==str(parent)
    assert command[command.index('--schedule-updates')+1]=='16022'
    assert command[command.index('--decay-updates')+1]=='763'
    assert command[command.index('--output')+1]!=str(parent.parent)
    assert sha256(parent)==before
    with pytest.raises(AssertionError):
        launcher.prepare(config,'500M',tmp_path,'evaluate')


def test_existing_run_without_checkpoint_is_not_reinitialized(tmp_path):
    (tmp_path/'stable').mkdir()
    with pytest.raises(ValueError,match='without a valid checkpoint'):
        launcher.prepare(configuration(),'500M',tmp_path,'stable')
