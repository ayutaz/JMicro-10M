"""Actual CPU optimizer trajectories; no claim of GPU or useful model quality."""
import sys
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from jmicro.experiment import ROOT,read_json,write_json,sha256
from jmicro.training import Trainer,rng_state

sys.path.insert(0,str(ROOT/"scripts"))
from textbook_quantity_trainer import ThreeSourceTrainer as CurveTrainer, ThreeSourceIndex
from extend_textbook_quantity_trainer import ExtendedCurveTrainer
from run_eos_short_pilot import equal_state


def fixture(tmp_path):
    torch.set_num_threads(2)
    data = tmp_path/"data";data.mkdir();write_json(data/"manifest.json",dict(vocab_size=4096))
    ids = np.asarray([2,8,9,10,11,12,3]*2048,dtype="<u2")
    shard = SimpleNamespace(directory=data,split="train",tokens=ids,
        index=[dict(offset=i*7,body_tokens=5,source=("web","story","textbook")[i%3],split="train") for i in range(2048)],
        manifest=dict(vocab_size=4096),byte_lengths=np.asarray([0]*8+[1]*4088))
    import json
    index_path=data/"train.index.jsonl"
    index_path.write_text("".join(json.dumps(row)+"\n" for row in shard.index))
    shard.manifest["splits"]=dict(train=dict(documents=len(shard.index),index_sha256=sha256(index_path)))
    shard.index=ThreeSourceIndex(shard)
    config = read_json(ROOT/"configs/models/t4k.json")
    config.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,
        rotary_dim=16,num_hidden_layers=1,intermediate_size=48,attention_scale=.25,qk_norm_type="none")
    spec = dict(seed=42,context=1024,batch=1,accumulation=1,lr=.002,weight_decay=.1,warmup=2,
        schedule_updates=100000,dtype="fp32",compile=False,backend="math",training_fast_path=True,scheduler="wsd")
    zero_path = tmp_path/"zero/checkpoint.pt";Trainer(config,shard,spec).save(zero_path)
    zero = torch.load(zero_path,map_location="cpu",weights_only=False)
    binding = dict(config_sha256="old-fixture",parent=dict(path=str(zero_path)),peak_lr=.002,
        optimizer_policy="fresh",initialization="new-random",warmup_updates=2,
        curve_mode="stable",curve_boundaries=[1000,2000])
    short = CurveTrainer(zero,shard,shard,"shuffle",dict(web=0,short=2000),binding,device="cpu")
    while short.sampler.source_teachers["short"] < 2000: short.step()
    path = tmp_path/"stable/checkpoint.pt";short.save(path)
    ref = dict(path=str(path),sha256=sha256(path),source_sha256=sha256(ROOT/"scripts/extend_textbook_quantity_trainer.py"))
    extended = dict(binding,config_sha256="new-fixture",curve_boundaries=[1000,2000,4000],stable_extension=ref)
    def build(b=extended):
        return ExtendedCurveTrainer(zero,shard,shard,"shuffle",dict(web=0,short=4000),b,device="cpu")
    return path,zero,shard,binding,build


def test_extension_preserves_full_state_matches_predeclared_long_run_and_resumes(tmp_path):
    path,zero,shard,binding,build = fixture(tmp_path)
    saved = torch.load(path,map_location="cpu",weights_only=False)
    trainer = build();trainer.load_extension(path)
    for name in ("model","optimizer","scheduler"):
        assert equal_state(getattr(trainer,name).state_dict(),saved[name])
    assert equal_state(rng_state(),saved["rng"])
    before = trainer.sampler.state_dict()
    for key in ("short","web","position","source_tokens","source_physical_tokens","source_teachers","source_eos","genre_teachers","genre_eos"):
        assert equal_state(before[key],saved["sampler"][key])
    assert before["boundaries"] == (1000,2000,4000) and before["goals"]["short"] == 4000
    for name in ("tokens","supervised_tokens","body_bytes","token_digest","update"):
        assert getattr(trainer,name) == saved[name]
    history = [trainer.step() for _ in range(2)]
    trainer.save(tmp_path/"continuous/checkpoint.pt")
    continuous = torch.load(tmp_path/"continuous/checkpoint.pt",map_location="cpu",weights_only=False)
    resumed = build();resumed.load_extension(path);actual = [resumed.step()]
    resumed.save(tmp_path/"split/checkpoint.pt")
    restarted = build();restarted.load(tmp_path/"split/checkpoint.pt");actual.append(restarted.step())
    restarted.save(tmp_path/"resumed/checkpoint.pt")
    result = torch.load(tmp_path/"resumed/checkpoint.pt",map_location="cpu",weights_only=False)
    assert all(equal_state(continuous[k],result[k]) for k in ("model","optimizer","scheduler","rng","sampler","lineage","tokens","supervised_tokens","token_digest","body_bytes","update"))
    for key in ("loss","gradient_norm","lr","token_digest","source_teachers"):
        assert [r[key] for r in history] == [r[key] for r in actual]
    # A control whose larger schedule was declared from update zero must have
    # the identical inputs/Adam trajectory through the same old milestones.
    long_binding = dict(binding,curve_boundaries=[1000,2000,4000])
    control = CurveTrainer(zero,shard,shard,"shuffle",dict(web=0,short=4000),long_binding,device="cpu")
    for _ in range(trainer.update): control.step()
    for name in ("model","optimizer","scheduler","sampler"):
        assert equal_state(getattr(control,name).state_dict(),getattr(trainer,name).state_dict())
    assert equal_state(rng_state(),continuous["rng"])
    assert control.token_digest == trainer.token_digest and control.supervised_tokens == trainer.supervised_tokens


def test_extension_rejects_changed_recipe_or_ordinary_budget_mutation(tmp_path):
    path,_,_,binding,build = fixture(tmp_path)
    changed = dict(binding,peak_lr=.003,config_sha256="new-fixture",curve_boundaries=[1000,2000,4000],
        stable_extension=dict(path=str(path),sha256=sha256(path),source_sha256=sha256(ROOT/"scripts/extend_textbook_quantity_trainer.py")))
    with pytest.raises(ValueError,match="only appended"):
        build(changed).load_extension(path)
    invalid = dict(changed,peak_lr=.002,curve_boundaries=[1500,2000,4000])
    with pytest.raises(ValueError,match="only appended"):
        build(invalid).load_extension(path)
    ordinary = build()
    with pytest.raises(ValueError,match="resume provenance"):
        ordinary.load(path)
    tampered = dict(invalid,curve_boundaries=[1000,2000,4000],stable_extension=dict(invalid["stable_extension"],sha256="00"*32))
    with pytest.raises(ValueError,match="checksum"):
        build(tampered).load_extension(path)
