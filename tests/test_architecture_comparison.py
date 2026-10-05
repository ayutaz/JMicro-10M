import importlib.util
from types import SimpleNamespace
import numpy as np
import torch
from jmicro.experiment import ROOT,read_json,write_json
from jmicro.model import JMicroModel

spec=importlib.util.spec_from_file_location('architecture',ROOT/'scripts/run_architecture_comparison.py')
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)


def test_zero_update_parent_is_separate_from_training_latest(tmp_path,monkeypatch):
    torch.set_num_threads(2)
    config=read_json(ROOT/'configs/models/t4k.json')
    config.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,rotary_dim=16,
        num_hidden_layers=2,intermediate_size=48,attention_scale=.25,qk_norm_type='none')
    count=sum(p.numel() for p in JMicroModel(config).parameters())
    source=tmp_path/'source';source.mkdir();write_json(source/'manifest.json',dict(vocab_size=4096))
    shard=SimpleNamespace(directory=source,split='train',tokens=np.array([2,8,9,3]*512,dtype='<u2'),
        manifest=dict(vocab_size=4096),byte_lengths=np.array([0]*8+[1]*4088))
    settings=dict(seed=42,context=1024,batch=32,accumulation=1,lr=.002,weight_decay=.1,warmup=200,
        schedule_updates=100000,dtype='bf16',compile=False,backend='math',training_fast_path=True,
        deterministic=True,scheduler='wsd')
    run=tmp_path/'run';monkeypatch.setattr(runner,'RUN',run)
    state,binding=runner.new_parent('candidate',dict(model_config=config,parameters=count),dict(parent_spec=settings),shard,device='cpu')
    assert state['update']==state['tokens']==state['supervised_tokens']==0 and not state['optimizer']['state']
    assert (run/'parents'/'candidate'/'latest.json').is_file()
    assert not (run/'candidate'/'latest.json').exists()
    state2,binding2=runner.new_parent('candidate',dict(model_config=config,parameters=count),dict(parent_spec=settings),shard,device='cpu')
    assert binding==binding2 and all(torch.equal(v,state2['model'][k]) for k,v in state['model'].items())
