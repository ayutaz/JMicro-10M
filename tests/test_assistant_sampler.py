import copy
from pathlib import Path

import pytest
import torch

from jmicro.assistant_sampler import AssistantSampler
from jmicro.experiment import read_json
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer

ROOT = Path(__file__).resolve().parents[1]


def dataset():
    return [dict(doc_id="dialogue-a", split="train", messages=[
        dict(role="system", text="短く答えてください。"),
        dict(role="user", text="パンを買いました。"),
        dict(role="assistant", text="何パンですか？"),
        dict(role="user", text="食パンです。"),
        dict(role="assistant", text="朝食に使えますね。")]),
        dict(doc_id="dialogue-b", split="train", messages=[
            dict(role="user", text="今日は雨です。"),
            dict(role="assistant", text="傘を持って出かけましょう。")])]


def test_causal_shift_padding_and_complete_assistant_targets():
    tok = Tokenizer(ROOT / "artifacts/phase2/4096/tokenizer.model")
    sampler = AssistantSampler(dataset(), tok, 128, 42)
    x, y, _ = sampler.batch(3)
    expected = sorted(tuple([*tok.encode(m["text"]), 7])
        for r in dataset() for m in r["messages"] if m["role"] == "assistant")
    assert sorted(tuple(row[row != -100].tolist()) for row in y) == expected
    assert y[x == 0].eq(-100).all()
    for inputs, labels in zip(x, y):
        first = int(labels.ne(-100).nonzero()[0])
        assert inputs[first] == 6  # Assistant role predicts first body token.
        assert inputs[int(labels.eq(7).nonzero()[0])] >= 8  # Last body predicts EOT.
    state = sampler.state_dict()
    assert state["eot_teachers"] == 3
    assert state["series_tokens"] == state["input_tokens"] + 3
    config = read_json(ROOT / "configs/models/t4k.json")
    config.update(hidden_size=32, num_attention_heads=2, num_key_value_heads=1,
        head_dim=16, rotary_dim=16, num_hidden_layers=1, intermediate_size=48,
        attention_scale=.25, qk_norm_type="none")
    torch.set_num_threads(2)
    model = JMicroModel(config).eval()
    logits = model(x, attention_mask=x.ne(0)).logits
    # Compare the actual model's internal causal loss against sampler targets.
    padded = torch.cat([x, torch.zeros((3, 1), dtype=torch.long)], dim=1)
    unshifted = torch.cat([torch.full((3, 1), -100), y], dim=1)
    loss = model(padded, attention_mask=padded.ne(0), labels=unshifted).loss
    manual = torch.nn.functional.cross_entropy(logits.reshape(-1, 4096), y.reshape(-1), ignore_index=-100)
    assert torch.allclose(loss, manual, atol=1e-6, rtol=1e-6)


def test_resume_across_epoch_preserves_next_batches_and_counters():
    tok = Tokenizer(ROOT / "artifacts/phase2/4096/tokenizer.model")
    first = AssistantSampler(dataset(), tok, 128, 42)
    first.batch(5)
    resumed = AssistantSampler(dataset(), tok, 128, 42)
    resumed.load_state_dict(copy.deepcopy(first.state_dict()))
    for size in (1, 4, 7):
        a, b = first.batch(size), resumed.batch(size)
        assert torch.equal(a[0], b[0]) and torch.equal(a[1], b[1]) and a[2] == b[2]
        assert first.state_dict() == resumed.state_dict()
    changed = dataset()
    changed[0]["messages"][2]["text"] = "別の回答です。"
    with pytest.raises(ValueError, match="differ"):
        AssistantSampler(changed, tok, 128, 42).load_state_dict(first.state_dict())


def test_reject_dev_and_truncation_and_trim_only_complete_old_turns():
    tok = Tokenizer(ROOT / "artifacts/phase2/4096/tokenizer.model")
    dev = dataset()
    dev[0]["split"] = "dev"
    with pytest.raises(ValueError, match="train"):
        AssistantSampler(dev, tok, 128, 42)
    with pytest.raises(ValueError, match="exceeds"):
        AssistantSampler(dataset(), tok, 2, 42)
    long = [dict(doc_id="long", split="train", messages=[
        dict(role="user", text="あ" * 20), dict(role="assistant", text="い" * 20),
        dict(role="user", text="現在の質問です。"), dict(role="assistant", text="現在の回答です。")])]
    messages = long[0]["messages"]
    context = max(len(tok.dialogue(messages[:2])[0]), len(tok.dialogue(messages[2:])[0])) - 1
    sampler = AssistantSampler(long, tok, context, 42)
    final = sampler.windows[-1]
    assert final["removed_turns"] == 1
    assert tok.encode("現在の質問です。") == final["ids"][2:2+len(tok.encode("現在の質問です。"))].tolist()
