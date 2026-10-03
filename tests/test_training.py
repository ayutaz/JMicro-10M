import hashlib
import json
from pathlib import Path

import numpy as np
import pytest
import torch

from jmicro.experiment import ROOT, read_json, write_json
from jmicro.shards import BlockSampler, Shard, build_shards
from jmicro.training import Trainer, evaluate_body, isolated_evaluation, learning_rate_factor, rng_state, scoring_windows
from jmicro.phase5 import equal_state

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


def test_wsd_boundaries_and_budget_independence():
    stable = spec(scheduler="wsd", warmup=2)
    assert [learning_rate_factor(stable, i) for i in range(7)] == [0.5, 1, 1, 1, 1, 1, 1]
    assert learning_rate_factor(stable, 4) == learning_rate_factor(dict(stable, schedule_updates=10000), 4)
    decay = dict(stable, scheduler="wsd_decay", branch_at=3, decay_updates=3, minimum_lr_ratio=0.1)
    assert learning_rate_factor(decay, 3) == 1
    assert learning_rate_factor(decay, 6) == pytest.approx(0.1)
    assert learning_rate_factor(decay, 4) > learning_rate_factor(decay, 5)


def test_wsd_resume_branch_and_stable_isolation_all_state(shard, tmp_path):
    frozen = spec(scheduler="wsd", warmup=2)
    stable = Trainer(config(), shard, frozen)
    reference = [stable.step() for _ in range(6)]
    stable.save(tmp_path / "continuous.pt")
    interrupted = Trainer(config(), shard, frozen)
    prefix = [interrupted.step() for _ in range(3)]
    parent = tmp_path / "parent.pt"
    interrupted.save(parent)
    digest = hashlib.sha256(parent.read_bytes()).hexdigest()
    branch_spec = dict(frozen, scheduler="wsd_decay", branch_at=3, decay_updates=3, minimum_lr_ratio=0.1)
    branch = Trainer(config(), shard, branch_spec)
    branch.load(parent, decay_branch=True)
    expected = [branch.step() for _ in range(3)]
    branch.save(tmp_path / "decay-continuous.pt")
    paused = Trainer(config(), shard, branch_spec)
    paused.load(parent, decay_branch=True)
    actual = [paused.step()]
    paused.save(tmp_path / "branch-pause.pt")
    resumed = Trainer(config(), shard, branch_spec)
    resumed.load(tmp_path / "branch-pause.pt")
    actual += [resumed.step() for _ in range(2)]
    resumed.save(tmp_path / "decay-resumed.pt")
    restored = Trainer(config(), shard, frozen)
    restored.load(parent)
    suffix = [restored.step() for _ in range(3)]
    restored.save(tmp_path / "stable-resumed.pt")
    assert [r["loss"] for r in reference] == [r["loss"] for r in prefix+suffix]
    assert [r["loss"] for r in expected] == [r["loss"] for r in actual]
    assert [r["lr"] for r in expected] == [0.002, pytest.approx(0.00155), pytest.approx(0.00065)]
    for a, b in [("continuous.pt", "stable-resumed.pt"), ("decay-continuous.pt", "decay-resumed.pt")]:
        assert equal_state(torch.load(tmp_path/a, weights_only=False), torch.load(tmp_path/b, weights_only=False))
    assert hashlib.sha256(parent.read_bytes()).hexdigest() == digest
    assert resumed.lineage["parent_sha256"] == digest
    state = torch.load(tmp_path/"decay-resumed.pt", weights_only=False)
    assert state["branch_updates"] == 3 and state["branch_tokens"] == 3*2*16
    with pytest.raises(ValueError, match="configuration"):
        Trainer(config(), shard, dict(frozen, schedule_updates=7)).load(parent)
    with pytest.raises(ValueError, match="identical"):
        Trainer(config(), shard, dict(branch_spec, lr=0.001)).load(parent, decay_branch=True)
    with pytest.raises(ValueError, match="stable"):
        Trainer(config(), shard, branch_spec).load(tmp_path/"branch-pause.pt", decay_branch=True)
    damaged = torch.load(parent, weights_only=False)
    damaged["implementation_sha256"]["src/jmicro/training.py"] = "0"*64
    torch.save(damaged, tmp_path/"damaged.pt")
    with pytest.raises(ValueError, match="implementation"):
        restored.load(tmp_path/"damaged.pt")
