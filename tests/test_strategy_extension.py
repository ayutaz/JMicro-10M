import copy
import sys
from pathlib import Path
from types import SimpleNamespace
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT,read_json,write_json
from jmicro.training import Trainer
from jmicro.curriculum_strategy import StrategyTrainer
from run_strategy_extension import ExtensionTrainer
from run_eos_short_pilot import equal_state


def test_extension_keeps_learned_moments_weights_and_next_document_block(tmp_path):
    torch.set_num_threads(2)
    config=read_json(ROOT/'configs/models/t4k.json')
    config.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,rotary_dim=16,
        num_hidden_layers=2,intermediate_size=48,attention_scale=.25,qk_norm_type='none')
    write_json(tmp_path/'manifest.json',dict(vocab_size=4096))
    tokens=np.array([2,8,9,10,3]*500,dtype='<u2')
    shard=SimpleNamespace(directory=tmp_path,split='train',tokens=tokens,
        index=[dict(offset=i*5,body_tokens=3,split='train') for i in range(500)],
        manifest=dict(vocab_size=4096),byte_lengths=np.array([0]*8+[1]*4088))
    settings=dict(seed=42,context=1024,batch=1,accumulation=1,lr=.002,weight_decay=.1,warmup=0,
        schedule_updates=100000,dtype='fp32',compile=False,backend='math',training_fast_path=True,
        deterministic=True,scheduler='wsd')
    initial=Trainer(config,shard,settings,'cpu');initial.save(tmp_path/'initial.pt')
    parent=torch.load(tmp_path/'initial.pt',map_location='cpu',weights_only=False)
    binding=dict(parent=dict(path='test'),peak_lr=.002,warmup_updates=0,optimizer_policy='inherit',initialization='test')
    first=StrategyTrainer(parent,shard,shard,'shuffle',dict(web=0,short=6000),binding,'cpu')
    for _ in range(3):first.step()
    first.save(tmp_path/'first.pt');trained=torch.load(tmp_path/'first.pt',map_location='cpu',weights_only=False)
    original=copy.deepcopy(trained['sampler'])
    extended=ExtensionTrainer(trained,shard,shard,'shuffle',dict(web=0,short=8000),binding,'cpu')
    assert equal_state(first.model.state_dict(),extended.model.state_dict())
    assert equal_state(first.optimizer.state_dict()['state'],extended.optimizer.state_dict()['state'])
    assert extended.update==first.update and extended.supervised_tokens==first.supervised_tokens
    assert extended.sampler.position==0 and sum(extended.sampler.source_teachers.values())==0
    assert extended.sampler.short.state_dict()==original['short'] and trained['sampler']==original
    before=first.sampler.short.batch(1);after=extended.sampler.short.batch(1)
    assert torch.equal(before[0],after[0]) and torch.equal(before[1],after[1])
    # Restore the inspected cursor before stepping and exercising full resume.
    extended.sampler.short.load_state_dict(original['short'])
    row=extended.step();assert row['lr']==pytest.approx(.002)
    extended.save(tmp_path/'extension.pt')
    resumed=ExtensionTrainer(trained,shard,shard,'shuffle',dict(web=0,short=8000),binding,'cpu')
    resumed.load(tmp_path/'extension.pt')
    assert equal_state(resumed.model.state_dict(),extended.model.state_dict())
    assert equal_state(resumed.optimizer.state_dict(),extended.optimizer.state_dict())
    assert resumed.sampler.state_dict()==extended.sampler.state_dict()
