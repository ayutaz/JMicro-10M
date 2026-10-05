import copy
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT,read_json,write_json
from jmicro.training import Trainer
from jmicro.curriculum_strategy import StrategyTrainer

spec=importlib.util.spec_from_file_location('repair',ROOT/'scripts/resume_curriculum_strategy.py')
repair=importlib.util.module_from_spec(spec);spec.loader.exec_module(repair)


def test_zero_update_constructor_preserves_actual_warmup_and_empty_adam(tmp_path):
    torch.set_num_threads(2)
    config=read_json(ROOT/'configs/models/t4k.json')
    config.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,rotary_dim=16,
        num_hidden_layers=2,intermediate_size=48,attention_scale=.25,qk_norm_type='none')
    write_json(tmp_path/'manifest.json',dict(vocab_size=4096))
    tokens=np.array([2,8,9,10,3]*500,dtype='<u2')
    shard=SimpleNamespace(directory=tmp_path,split='train',tokens=tokens,
        index=[dict(offset=i*5,body_tokens=3,split='train') for i in range(500)],
        manifest=dict(vocab_size=4096),byte_lengths=np.array([0]*8+[1]*4088))
    settings=dict(seed=42,context=1024,batch=1,accumulation=1,lr=.002,weight_decay=.1,warmup=200,
        schedule_updates=100000,dtype='fp32',compile=False,backend='math',training_fast_path=True,
        deterministic=True,scheduler='wsd')
    initial=Trainer(config,shard,settings,'cpu');initial.save(tmp_path/'initial.pt')
    parent=torch.load(tmp_path/'initial.pt',map_location='cpu',weights_only=False)
    original=copy.deepcopy(parent['spec']);binding=dict(parent=dict(path='test'),peak_lr=.002,
        warmup_updates=200,optimizer_policy='fresh',initialization='new-random')
    with pytest.raises(ValueError,match='Invalid warmup'):
        StrategyTrainer(parent,shard,shard,'shuffle',dict(web=0,short=100000),binding,'cpu')
    trainer=repair.BootstrapStrategyTrainer(parent,shard,shard,'shuffle',dict(web=0,short=100000),binding,'cpu')
    assert parent['spec']==original and trainer.spec['warmup']==200
    assert trainer.lineage['parent_spec']==original and not trainer.optimizer.state
    assert trainer.optimizer.param_groups[0]['lr']==pytest.approx(.002/200)
    row=trainer.step()
    assert row['lr']==pytest.approx(.002/200)
    assert trainer.optimizer.param_groups[0]['lr']==pytest.approx(.002*2/200)
