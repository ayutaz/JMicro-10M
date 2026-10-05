import copy
import json
import sys
from types import SimpleNamespace
import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256
from jmicro.shards import BlockSampler
from jmicro.training import Trainer
sys.path.insert(0,str(ROOT/"scripts"))
from textbook_quantity_trainer import ThreeSourceIndex,ThreeSourceMixture,ThreeSourceTrainer,GENRES
from run_eos_short_pilot import equal_state


def shard(tmp_path):
    folder=tmp_path/"source";folder.mkdir()
    ids=np.asarray([2,8,9,10,11,12,3]*2048,dtype="<u2")
    rows=[dict(offset=i*7,body_tokens=5,source=GENRES[i%3],split="train") for i in range(2048)]
    path=folder/"train.index.jsonl";path.write_text("".join(json.dumps(r)+"\n" for r in rows))
    manifest=dict(vocab_size=4096,splits=dict(train=dict(documents=len(rows),index_sha256=sha256(path))))
    write_json(folder/"manifest.json",manifest)
    result=SimpleNamespace(directory=folder,split="train",tokens=ids,manifest=manifest,
        byte_lengths=np.asarray([0]*8+[1]*4088))
    result.index=ThreeSourceIndex(result)
    return result


def test_three_source_exact_masked_teachers_eos_and_resume_tags(tmp_path):
    source=shard(tmp_path);parent=BlockSampler(source,1024,42).state_dict()
    a=ThreeSourceMixture(source,source,parent,[850,1700,3400]);a.batch(1)
    assert set(a.genre_teachers)==set(GENRES) and all(a.genre_teachers[g]>0 for g in GENRES)
    assert sum(a.genre_teachers.values())==850 and sum(a.genre_eos.values())==a.source_eos["short"]
    state=copy.deepcopy(a.state_dict());b=ThreeSourceMixture(source,source,parent,[850,1700,3400]);b.load_state_dict(state)
    for _ in range(3):
        x,y=a.batch(1),b.batch(1)
        assert torch.equal(x[0],y[0]) and torch.equal(x[1],y[1]) and a.state_dict()==b.state_dict()
    changed=copy.deepcopy(state);changed["genre_tag_mapping"]["textbook"]=0
    with pytest.raises(ValueError,match="mapping differs"):b.load_state_dict(changed)


def test_three_source_cpu_weights_adam_schedule_rng_cursor_and_decay_resume(tmp_path):
    torch.set_num_threads(2);source=shard(tmp_path)
    config=read_json(ROOT/"configs/models/t4k.json")
    config.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,
        rotary_dim=16,num_hidden_layers=1,intermediate_size=48,attention_scale=.25,qk_norm_type="none")
    spec=dict(seed=42,context=1024,batch=1,accumulation=1,lr=.002,weight_decay=.1,warmup=2,
        schedule_updates=100000,dtype="fp32",compile=False,backend="math",training_fast_path=True,scheduler="wsd")
    initial=Trainer(config,source,spec);initial.save(tmp_path/"initial/parent.pt")
    parent=torch.load(tmp_path/"initial/parent.pt",map_location="cpu",weights_only=False)
    binding=dict(parent=dict(path=str(tmp_path/"initial/parent.pt")),peak_lr=.002,optimizer_policy="fresh",
        initialization="new-random",warmup_updates=2,curve_mode="stable",curve_boundaries=[1700,3400])
    a=ThreeSourceTrainer(parent,source,source,"shuffle",dict(web=0,short=3400),binding,device="cpu")
    a.step();a.step();a.save(tmp_path/"stable/point.pt")
    stable=torch.load(tmp_path/"stable/point.pt",map_location="cpu",weights_only=False)
    a.step();a.step();a.save(tmp_path/"continuous/point.pt")
    b=ThreeSourceTrainer(parent,source,source,"shuffle",dict(web=0,short=3400),binding,device="cpu")
    b.load(tmp_path/"stable/point.pt");b.step();b.step();b.save(tmp_path/"resumed/point.pt")
    left=torch.load(tmp_path/"continuous/point.pt",map_location="cpu",weights_only=False)
    right=torch.load(tmp_path/"resumed/point.pt",map_location="cpu",weights_only=False)
    assert all(equal_state(left[k],right[k]) for k in ("model","optimizer","scheduler","rng","sampler","tokens","supervised_tokens","spec","lineage"))
    decay_binding=dict(binding,parent=dict(path=str(tmp_path/"stable/point.pt")),optimizer_policy="inherit",
        initialization="stable-fork",warmup_updates=0,curve_mode="decay",curve_boundaries=[100])
    decay=ThreeSourceTrainer(stable,source,source,"shuffle",dict(web=0,short=100),decay_binding,device="cpu")
    assert equal_state(decay.optimizer.state_dict()["state"],stable["optimizer"]["state"])
    assert decay.sampler.short.state_dict()==stable["sampler"]["short"]
    decay.step();decay.save(tmp_path/"decay/point.pt")
    resumed=ThreeSourceTrainer(stable,source,source,"shuffle",dict(web=0,short=100),decay_binding,device="cpu")
    resumed.load(tmp_path/"decay/point.pt")
    assert resumed.sampler.state_dict()==decay.sampler.state_dict()
    assert sum(decay.sampler.genre_teachers.values())==100
