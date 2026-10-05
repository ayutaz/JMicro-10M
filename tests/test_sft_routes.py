"""Actual CPU mid-training->SFT provenance/optimizer tests; no quality claim."""
import sys
from types import SimpleNamespace
import numpy as np
import pytest
import torch
from jmicro.chat_training import AssistantTrainer
from jmicro.dialogue_training import DialogueTrainer
from jmicro.experiment import ROOT,read_json,write_json,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer,implementation_hashes
from test_chat_training import dialogues,same

sys.path.insert(0,str(ROOT/"scripts"))
from require_adopted_base import require_sft_parent,validate_midtraining_state


def test_actual_midtraining_parent_fresh_sft_and_full_resume_keep_root_base(tmp_path):
    torch.set_num_threads(2)
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    directory = tmp_path/"data";directory.mkdir();write_json(directory/"manifest.json",dict(vocab_size=4096))
    ids = np.asarray([2,8,9,10,11,3]*128,dtype="<u2")
    shard = SimpleNamespace(directory=directory,split="train",manifest=dict(vocab_size=4096),tokens=ids,
        index=[dict(offset=i*6,body_tokens=4) for i in range(128)],byte_lengths=np.asarray([0]*8+[1]*4088))
    model = read_json(ROOT/"configs/models/t4k.json")
    model.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,
        rotary_dim=16,num_hidden_layers=1,intermediate_size=48,attention_scale=.25,qk_norm_type="none")
    spec = dict(seed=42,context=128,batch=2,accumulation=1,lr=.0001,weight_decay=.1,warmup=1,
        schedule_updates=100,dtype="fp32",compile=False,backend="math",sampler="document",training_fast_path=False,scheduler="wsd")
    base = Trainer(model,shard,spec);base.step();base_path = tmp_path/"base.pt";base.save(base_path)
    root_ref = dict(path=str(base_path),sha256=sha256(base_path))
    root = torch.load(base_path,map_location="cpu",weights_only=False)
    budgets = dict(dialogue=1,replay=1)
    mid = DialogueTrainer(root,root_ref,dialogues(),tok,directory,shard,spec,budgets)
    mid.step();assert mid.sampler.complete
    mid_path = tmp_path/"mid.pt";mid.save(mid_path)
    parent = torch.load(mid_path,map_location="cpu",weights_only=False)
    recipe = dict(parent=root_ref,mixture_binding=mid.sampler.binding,series_budgets=budgets,implementation=implementation_hashes())
    result = dict(Base_lineage=mid.lineage,series_budgets=budgets,full_sampler=mid.sampler.state_dict(),
        valid_input_tokens=mid.tokens,teacher_tokens=mid.supervised_tokens,actual_series_tokens=mid.sampler.series_tokens,
        physical_input_tokens=mid.sampler.physical_tokens)
    validate_midtraining_state(parent,result,recipe,root_ref)
    with pytest.raises(AssertionError): validate_midtraining_state(parent,dict(result,teacher_tokens=mid.supervised_tokens+1),recipe,root_ref)
    with pytest.raises(AssertionError): validate_midtraining_state(parent,result,recipe,dict(root_ref,sha256="00"*32))
    mid_ref = dict(path=str(mid_path),sha256=sha256(mid_path))
    def build():return AssistantTrainer(parent,mid_ref,dialogues(),tok,directory,spec,1000)
    trained = build();assert same(trained.model.state_dict(),parent["model"]) and not trained.optimizer.state
    assert trained.lineage["root_Base_checkpoint"] == root_ref and trained.lineage["base_checkpoint"] == mid_ref
    assert trained.lineage["route"] == "midtraining-sft" and trained.lineage["model_parent_lineage"] == mid.lineage
    trained.step();trained.save(tmp_path/"split.pt");trained.step();trained.save(tmp_path/"continuous.pt")
    resumed = build();resumed.load(tmp_path/"split.pt");resumed.step();resumed.save(tmp_path/"resumed.pt")
    a = torch.load(tmp_path/"continuous.pt",map_location="cpu",weights_only=False)
    b = torch.load(tmp_path/"resumed.pt",map_location="cpu",weights_only=False)
    assert all(same(a[k],b[k]) for k in ("model","optimizer","scheduler","rng","sampler","lineage","tokens","supervised_tokens","token_digest","body_bytes","update"))


def test_live_midtraining_and_direct_parent_substitution_are_rejected(tmp_path):
    from phase6_performance import identity
    parent = tmp_path/"parent.json";write_json(parent,dict(not_a_model=True))
    ref = dict(path=str(parent),sha256=sha256(parent))
    with pytest.raises(ValueError,match="adopted Base"):
        require_sft_parent(dict(parent=ref,route="direct-sft"),dict(ref,sha256="00"*32))
    run = tmp_path/"run";run.mkdir()
    c = dict(parent=ref,route="midtraining-sft",mid_training=dict(result=dict(path=str(run/"result.json")),config=dict(path=str(tmp_path/"recipe.json"))))
    for job in (dict(status="running"),dict(status="complete",**identity())):
        write_json(run/"job.json",job)
        with pytest.raises(ValueError,match="actually finish"):require_sft_parent(c,ref)
