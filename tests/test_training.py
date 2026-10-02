import hashlib
import json
from pathlib import Path

import numpy as np
import pytest
import torch

from jmicro.experiment import ROOT, read_json, write_json
from jmicro.shards import BlockSampler, Shard, build_shards
from jmicro.training import Trainer, evaluate_body, isolated_evaluation, rng_state, scoring_windows

torch.set_num_threads(2)


@pytest.fixture
def shard(tmp_path):
    corpus = tmp_path / "corpus.jsonl"
    rows = []
    for split in ("train", "dev", "test"):
        for i in range(4):
            text = (f"今日は晴れです。散歩に行きます。{i} あいうえお\n" * 5)
            rows.append({"kind": "web", "bucket": "commercial_web", "split": split,
                "text": text, "doc_id": f"{split}-{i}", "canonical_sha256": hashlib.sha256(text.encode()).hexdigest()})
    corpus.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    tokenizer = ROOT / "artifacts/phase2/8192/tokenizer.model"
    if not tokenizer.exists():
        pytest.fail("Restore the pinned tokenizer before running training tests")
    build_shards(corpus, tokenizer, tmp_path / "shards")
    return Shard(tmp_path / "shards")


def config():
    c = read_json(ROOT / "configs/models/t8k.json")
    c.update(num_hidden_layers=1, hidden_size=32, num_attention_heads=2,
             num_key_value_heads=1, head_dim=16, rotary_dim=16, intermediate_size=48,
             attention_scale=0.25)
    return c


def spec(**changes):
    s = dict(seed=42, context=16, batch=2, accumulation=1, lr=0.002,
             weight_decay=0.1, warmup=1, schedule_updates=6, dtype="fp32", compile=False)
    s.update(changes)
    return s


def test_shard_integrity_split_boundary_and_sampler_restore(shard):
    assert all(r["split"] == "train" for r in shard.index)
    for row in shard.index:
        assert shard.tokens[row["offset"]] == 2
        assert shard.tokens[row["offset"] + row["body_tokens"] + 1] == 3
    sampler = BlockSampler(shard, 16, 42)
    # Cross an epoch boundary and ensure restoration never touches global RNG.
    sampler.batch(sampler.blocks + 1)
    state = sampler.state_dict()
    reference = sampler.batch(3)
    restored = BlockSampler(shard, 16, 42)
    restored.load_state_dict(state)
    actual = restored.batch(3)
    assert torch.equal(reference[0], actual[0]) and torch.equal(reference[1], actual[1])
    assert reference[2] == actual[2]
    raw = shard.directory / "train.bin"
    with raw.open("r+b") as stream:
        stream.write(b"xx")
    with pytest.raises(ValueError, match="checksum"):
        Shard(shard.directory)


@pytest.mark.parametrize("body", [1, 15, 16, 31, 32, 70, 1030])
def test_evaluation_targets_scored_once(body):
    seen = []
    for start, end, first, last in scoring_windows(body, 16, 7):
        assert end - start <= 16 and first > start
        seen.extend(range(first, last))
    assert seen == list(range(1, body + 1))


def test_continuous_vs_resumed_updates_with_evaluation_rng_isolation(shard, tmp_path):
    continuous = Trainer(config(), shard, spec())
    expected = [continuous.step() for _ in range(6)]
    paused = Trainer(config(), shard, spec())
    actual = [paused.step() for _ in range(3)]
    state = rng_state()
    with isolated_evaluation(paused.model):
        np.random.rand(5)
        torch.rand(5)
    assert torch.equal(state["torch"], rng_state()["torch"])
    checkpoint = tmp_path / "checkpoint.pt"
    paused.save(checkpoint)
    resumed = Trainer(config(), shard, spec())
    resumed.load(checkpoint)
    actual.extend(resumed.step() for _ in range(3))
    assert [row["token_digest"] for row in expected] == [row["token_digest"] for row in actual]
    assert [row["loss"] for row in expected] == [row["loss"] for row in actual]
    for name, weight in continuous.model.state_dict().items():
        torch.testing.assert_close(weight, resumed.model.state_dict()[name], atol=0, rtol=0)
    assert resumed.scheduler.state_dict() == continuous.scheduler.state_dict()
    assert resumed.tokens == continuous.tokens
    assert resumed.body_bytes == continuous.body_bytes
    invalid = Trainer(config(), shard, spec(schedule_updates=7))
    with pytest.raises(ValueError, match="configuration"):
        invalid.load(checkpoint)


def test_accumulation_matches_global_supervised_token_mean(shard):
    full = Trainer(config(), shard, spec(batch=2))
    full_result = full.step()
    accumulated = Trainer(config(), shard, spec(batch=1, accumulation=2))
    accumulated_result = accumulated.step()
    assert full_result["loss"] == pytest.approx(accumulated_result["loss"], abs=1e-6)
    assert full.supervised_tokens == accumulated.supervised_tokens
    for name, weight in full.model.state_dict().items():
        torch.testing.assert_close(weight, accumulated.model.state_dict()[name], atol=2e-6, rtol=1e-5)


def test_common_byte_denominator_and_body_eos_separation(shard):
    trainer = Trainer(config(), shard, spec())
    dev = Shard(shard.directory, "dev")
    report = evaluate_body(trainer.model, dev, "cpu", context=16)
    assert report["body_bytes"] == sum(row["bytes"] for row in dev.index)
    assert sum(row["body_tokens"] for row in report["rows"]) == sum(row["body_tokens"] for row in dev.index)
    assert report["bpb"] == pytest.approx(report["body_nll"] / (np.log(2) * report["body_bytes"]))
    with pytest.raises(ValueError, match="Only train"):
        Trainer(config(), dev, spec())
