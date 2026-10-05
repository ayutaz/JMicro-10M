from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from jmicro.chat_training import AssistantBudgetSampler, AssistantTrainer
from jmicro.experiment import ROOT,read_json,write_json,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer


def dialogues():
    return [dict(doc_id="train-a",split="train",messages=[
        dict(role="user",text="パンを買いました。"),dict(role="assistant",text="何パンですか？"),
        dict(role="user",text="食パンです。"),dict(role="assistant",text="朝食に使えますね。")]),
        dict(doc_id="train-b",split="train",messages=[
            dict(role="user",text="今日は雨です。"),dict(role="assistant",text="傘を持って出かけましょう。")])]


def same(a,b):
    if isinstance(a,torch.Tensor): return torch.equal(a,b)
    if isinstance(a,np.ndarray): return np.array_equal(a,b)
    if isinstance(a,dict): return a.keys() == b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,(list,tuple)): return len(a) == len(b) and all(same(x,y) for x,y in zip(a,b))
    return a == b


def test_budget_finishes_assistant_eot_without_teaching_empty_rows():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    sampler = AssistantBudgetSampler(dialogues(),tok,128,42,1)
    x,y,_ = sampler.batch(4)
    assert y[0].eq(7).sum() == 1 and y[1:].eq(-100).all() and x[1:].eq(0).all()
    assert sampler.eot_teachers == sampler.examples == 1
    assert sampler.series_tokens == sampler.input_tokens+1 < 1+129
    assert sampler.physical_tokens == 4*128
    with pytest.raises(ValueError,match="exhausted"): sampler.batch(4)
    with pytest.raises(ValueError,match="budget"):
        AssistantBudgetSampler(dialogues(),tok,128,42,2).load_state_dict(sampler.state_dict())


def test_real_optimizer_resume_and_masked_padding_counters(tmp_path):
    torch.set_num_threads(2)
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    directory = tmp_path/"data";directory.mkdir();write_json(directory/"manifest.json",dict(vocab_size=4096))
    config = read_json(ROOT/"configs/models/t4k.json")
    config.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,
        rotary_dim=16,num_hidden_layers=1,intermediate_size=48,attention_scale=.25,qk_norm_type="none")
    ids = np.asarray([2,8,9,10,11,3]*128,dtype="<u2")
    shard = SimpleNamespace(directory=directory,split="train",manifest=dict(vocab_size=4096),tokens=ids,
        index=[dict(offset=i*6,body_tokens=4) for i in range(128)],byte_lengths=np.asarray([0]*8+[1]*4088))
    base_spec = dict(seed=42,context=128,batch=2,accumulation=1,lr=.002,weight_decay=.1,
        warmup=1,schedule_updates=100,dtype="fp32",compile=False,backend="math",scheduler="wsd")
    base = Trainer(config,shard,base_spec);base.step();base.save(tmp_path/"base/learned.pt")
    parent = torch.load(tmp_path/"base/learned.pt",map_location="cpu",weights_only=False)
    ref = dict(path=str(tmp_path/"base/learned.pt"),sha256=sha256(tmp_path/"base/learned.pt"))
    spec = dict(base_spec,lr=.0001,sampler="document",training_fast_path=False)
    def build(budget=1000): return AssistantTrainer(parent,ref,dialogues(),tok,directory,spec,budget)
    a = build();assert same(a.model.state_dict(),parent["model"]) and not a.optimizer.state
    a.step();a.save(tmp_path/"split/checkpoint.pt")
    a.step();a.step();a.save(tmp_path/"continuous/checkpoint.pt")
    b = build();b.load(tmp_path/"split/checkpoint.pt");b.step();b.step();b.save(tmp_path/"resumed/checkpoint.pt")
    first = torch.load(tmp_path/"continuous/checkpoint.pt",map_location="cpu",weights_only=False)
    second = torch.load(tmp_path/"resumed/checkpoint.pt",map_location="cpu",weights_only=False)
    assert all(same(first[k],second[k]) for k in ("model","optimizer","scheduler","rng","sampler","tokens","supervised_tokens","body_bytes","token_digest","lineage","update"))
    assert b.tokens == b.sampler.input_tokens < b.sampler.physical_tokens
    assert b.supervised_tokens == b.sampler.teacher_tokens < b.tokens
    assert b.lineage["base_tokens"] == parent["tokens"] and b.update == 3
    with pytest.raises(ValueError,match="configuration"): build(1001).load(tmp_path/"split/checkpoint.pt")
    last = build(1);row = last.step()
    assert row["EOT_teachers"] == 1 and row["examples"] == 1
    assert row["padding_input_tokens"] > 0 and row["final_whole_window_overshoot"] < 129
    assert np.isfinite(row["loss"]) and np.isfinite(row["gradient_norm"])
    # This is an actual CPU update/counter fixture, not adopted-Base/CUDA evidence.
    import sys
    sys.path.insert(0, str(ROOT/"scripts"))
    from chat_stage_evidence import validate_sft_terminal
    last.save(tmp_path/"final.pt")
    state = torch.load(tmp_path/"final.pt", map_location="cpu", weights_only=False)
    recipe = dict(spec=spec, series_budget=1, route="direct-sft", implementation=state["implementation_sha256"], dialogue_binding=last.sampler.binding)
    result = dict(full_sampler=last.sampler.state_dict(), Base_lineage=last.lineage, actual_series_tokens=last.sampler.series_tokens,
        Assistant_teacher_tokens=last.supervised_tokens, valid_input_tokens=last.tokens, physical_tokens=last.sampler.physical_tokens,
        EOT_teachers=last.sampler.eot_teachers, adopted_Base=ref, model_parent=ref)
    validate_sft_terminal(state, result, recipe)
    with pytest.raises(AssertionError): validate_sft_terminal(state, dict(result, Assistant_teacher_tokens=last.supervised_tokens+1), recipe)


def test_command_refuses_unadopted_base_before_dataset_or_gpu_work(tmp_path):
    import sys
    sys.path.insert(0,str(ROOT/"scripts"))
    from run_chat_sft import preflight,SOURCES
    from jmicro.training import implementation_hashes
    accepted = tmp_path/"rejected.json";write_json(accepted,dict(Base_adopted=False))
    ref = dict(path=str(accepted),sha256=sha256(accepted))
    config = dict(implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        **{key:ref for key in ("parent","tokenizer","train_records","Base_acceptance","Base_evaluation","Base_annotations")})
    path = tmp_path/"config.json";write_json(path,config)
    with pytest.raises(ValueError,match="quality-adopted Base"):
        preflight(path)
