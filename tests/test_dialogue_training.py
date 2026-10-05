"""Real CPU dialogue/replay gradients and resume, not model-quality evidence."""
from types import SimpleNamespace

import numpy as np
import pytest
import torch
from jmicro.dialogue_training import DialogueWindows, DialogueReplaySampler, DialogueTrainer
from jmicro.experiment import ROOT, read_json, write_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer
from test_chat_training import dialogues, same


def test_long_dialogue_teaches_each_body_role_eot_once_and_keeps_pairs():
    tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    messages = [dict(role="system", text="短く答える。")]+dialogues()[0]["messages"]*8
    windows = DialogueWindows([dict(doc_id="long", split="train", messages=messages)], tok, 64, 42)
    assert len(windows.windows) > 1
    all_targets = [int(i) for w in windows.windows for i in w["labels"] if i != -100]
    original,_ = tok.dialogue(messages)
    assert all_targets == original[1:]
    assert all(w["labels"][-1] == 7 and (w["end_message"]-w["first_message"])%2 == 0 for w in windows.windows)
    assert any(sum(w["labels"] == -100) > 1 for w in windows.windows[1:])
    trailing = messages[:-1]
    preserved = DialogueWindows([dict(doc_id="trailing",split="train",messages=trailing)],tok,64,42)
    assert [int(i) for w in preserved.windows for i in w["labels"] if i != -100] == tok.dialogue(trailing)[0][1:]
    for records in ([dict(doc_id="dev", split="dev", messages=messages)], [dict(doc_id="bad", split="train", messages=messages[:-2]+[messages[-1]])]):
        with pytest.raises(ValueError): DialogueWindows(records, tok, 64, 42)


def test_real_midtraining_optimizer_mixture_resume_and_final_whole_windows(tmp_path):
    torch.set_num_threads(2); tok = Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    data = tmp_path/"data"; data.mkdir(); write_json(data/"manifest.json", dict(vocab_size=4096))
    ids = np.asarray([2,8,9,10,11,3]*128, dtype="<u2")
    replay = SimpleNamespace(directory=data, split="train", manifest=dict(vocab_size=4096), tokens=ids,
        index=[dict(offset=i*6, body_tokens=4) for i in range(128)], byte_lengths=np.asarray([0]*8+[1]*4088))
    config = read_json(ROOT/"configs/models/t4k.json")
    config.update(hidden_size=32, num_attention_heads=2, num_key_value_heads=1, head_dim=16,
        rotary_dim=16, num_hidden_layers=1, intermediate_size=48, attention_scale=.25, qk_norm_type="none")
    spec = dict(seed=42, context=128, batch=2, accumulation=1, lr=.0001, weight_decay=.1,
        warmup=1, schedule_updates=100, dtype="fp32", compile=False, backend="math", scheduler="wsd", sampler="document", training_fast_path=False)
    base = Trainer(config, replay, spec); base.step(); base_path = tmp_path/"base.pt"; base.save(base_path)
    parent = torch.load(base_path, map_location="cpu", weights_only=False); ref = dict(path=str(base_path), sha256=sha256(base_path))
    budgets = dict(dialogue=500, replay=200)
    def build(b=budgets): return DialogueTrainer(parent, ref, dialogues(), tok, data, replay, spec, b)
    trainer = build(); assert same(trainer.model.state_dict(), parent["model"]) and not trainer.optimizer.state
    trainer.step(); trainer.save(tmp_path/"split.pt")
    trainer.step(); trainer.step(); trainer.save(tmp_path/"continuous.pt")
    resumed = build(); resumed.load(tmp_path/"split.pt"); resumed.step(); resumed.step(); resumed.save(tmp_path/"resumed.pt")
    a = torch.load(tmp_path/"continuous.pt", map_location="cpu", weights_only=False)
    b = torch.load(tmp_path/"resumed.pt", map_location="cpu", weights_only=False)
    assert all(same(a[k], b[k]) for k in ("model", "optimizer", "scheduler", "rng", "sampler", "tokens", "supervised_tokens", "token_digest", "body_bytes", "lineage", "update"))
    assert all(resumed.sampler.source_teachers[s] > 0 for s in budgets)
    assert resumed.sampler.dialogue_teacher_kinds["user"] > 0 and resumed.sampler.dialogue_teacher_kinds["role"] > 0
    with pytest.raises(ValueError): build(dict(dialogue=501, replay=200)).load(tmp_path/"split.pt")
    last = DialogueReplaySampler(dialogues(), tok, replay, 128, 42, dict(dialogue=1, replay=1))
    x,y,_ = last.batch(8)
    assert last.complete and all(1 <= last.source_series[s] < 130 for s in budgets)
    assert x[2:].eq(0).all() and y[2:].eq(-100).all()
    last.load_state_dict(last.state_dict())
    with pytest.raises(ValueError, match="exhausted"): last.batch(1)


def test_midtraining_command_rejects_unadopted_base_before_dataset_or_gpu(tmp_path):
    import sys
    sys.path.insert(0,str(ROOT/"scripts"))
    from run_dialogue_midtraining import preflight, SOURCES
    from jmicro.training import implementation_hashes
    rejected = tmp_path/"rejected.json"; write_json(rejected, dict(Base_adopted=False))
    ref = dict(path=str(rejected),sha256=sha256(rejected))
    c = dict(implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        **{name:ref for name in ("parent","Base_acceptance","Base_evaluation","Base_annotations","tokenizer")})
    config = tmp_path/"recipe.json"; write_json(config,c)
    with pytest.raises(ValueError,match="quality-adopted Base"): preflight(config)
