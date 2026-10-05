import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch

from jmicro.experiment import ROOT, read_json, write_json
from jmicro.training import Trainer

sys.path.insert(0, str(ROOT / "scripts"))
from amount_learning_trainer import CurveTrainer
from run_eos_short_pilot import equal_state
from run_amount_learning_comparison import reconcile_metrics, latest_checkpoint


def test_stable_resume_and_decay_inherit_actual_weights_adam_and_cursor(tmp_path):
    torch.set_num_threads(2)
    folder = tmp_path / "source"; folder.mkdir()
    write_json(folder / "manifest.json", dict(vocab_size=4096))
    ids = np.asarray([2, 8, 9, 10, 11, 12, 3] * 2048, dtype="<u2")
    shard = SimpleNamespace(directory=folder, split="train", tokens=ids,
        index=[dict(offset=i*7, body_tokens=5) for i in range(2048)],
        manifest=dict(vocab_size=4096), byte_lengths=np.asarray([0]*8+[1]*4088))
    config = read_json(ROOT / "configs/models/t4k.json")
    config.update(hidden_size=32, num_attention_heads=2, num_key_value_heads=1,
        head_dim=16, rotary_dim=16, num_hidden_layers=1, intermediate_size=48,
        attention_scale=.25, qk_norm_type="none")
    spec = dict(seed=42, context=1024, batch=1, accumulation=1, lr=.002,
        weight_decay=.1, warmup=2, schedule_updates=100000, dtype="fp32",
        compile=False, backend="math", training_fast_path=True, scheduler="wsd")
    initial = Trainer(config, shard, spec)
    first_path = tmp_path / "parents" / "initial.pt"; initial.save(first_path)
    parent = torch.load(first_path, map_location="cpu", weights_only=False)
    binding = dict(parent=dict(path=str(first_path)), peak_lr=.002,
        optimizer_policy="fresh", initialization="new-random", warmup_updates=2,
        curve_mode="stable", curve_boundaries=[1000, 2000, 4000])
    trainer = CurveTrainer(parent, shard, shard, "shuffle", dict(web=0, short=4000), binding, device="cpu")
    trainer.step(); trainer.step()
    assert trainer.sampler.source_teachers["short"] == 1000
    stable_path = tmp_path / "stable" / "checkpoint.pt"; trainer.save(stable_path)
    stable = torch.load(stable_path, map_location="cpu", weights_only=False)
    trainer.step(); trainer.step()
    trainer.save(tmp_path / "continuous" / "checkpoint.pt")
    resumed = CurveTrainer(parent, shard, shard, "shuffle", dict(web=0, short=4000), binding, device="cpu")
    resumed.load(stable_path); resumed.step(); resumed.step()
    resumed.save(tmp_path / "resumed" / "checkpoint.pt")
    a = torch.load(tmp_path / "continuous" / "checkpoint.pt", map_location="cpu", weights_only=False)
    b = torch.load(tmp_path / "resumed" / "checkpoint.pt", map_location="cpu", weights_only=False)
    assert all(equal_state(a[k], b[k]) for k in ("model", "optimizer", "scheduler", "rng", "sampler", "tokens", "supervised_tokens", "lineage"))
    decay_binding = dict(binding, parent=dict(path=str(stable_path)), optimizer_policy="inherit",
        initialization="stable-fork", warmup_updates=0, curve_mode="decay", curve_boundaries=[100])
    decay = CurveTrainer(stable, shard, shard, "shuffle", dict(web=0, short=100), decay_binding, device="cpu")
    assert equal_state(decay.model.state_dict(), stable["model"])
    assert equal_state(decay.sampler.short.state_dict(), stable["sampler"]["short"])
    assert equal_state(decay.optimizer.state_dict()["state"], stable["optimizer"]["state"])
    decay.step()
    assert decay.supervised_tokens == stable["supervised_tokens"] + 100
    assert decay.sampler.source_teachers["short"] == 100
    assert decay.sampler.source_tokens["short"] == decay.tokens - stable["tokens"]
    assert decay.optimizer.param_groups[0]["lr"] == .0002
    # Fork computation consumes RNG. Reloading stable state must restore the
    # original trajectory, including Adam, counters and shuffled cursor.
    restored = CurveTrainer(parent,shard,shard,"shuffle",dict(web=0,short=4000),binding,device="cpu")
    restored.load(stable_path); restored.step(); restored.step()
    restored.save(tmp_path / "after-fork" / "checkpoint.pt")
    after = torch.load(tmp_path / "after-fork" / "checkpoint.pt",map_location="cpu",weights_only=False)
    assert all(equal_state(a[k],after[k]) for k in ("model","optimizer","scheduler","rng","sampler","tokens","supervised_tokens"))
    assert latest_checkpoint(tmp_path / "after-fork") == tmp_path / "after-fork" / "checkpoint.pt"


def test_metrics_recovery_keeps_completed_update_seconds_and_original_log(tmp_path):
    import json
    log = tmp_path / "metrics.jsonl"
    rows = [dict(update=n,seconds=n/10) for n in (2,3,4)]
    log.write_text("".join(json.dumps(r)+"\n" for r in rows))
    assert reconcile_metrics(log,3) == .5
    assert [json.loads(s)["update"] for s in log.read_text().splitlines()] == [2,3]
    backup = list(tmp_path.glob("metrics-before-resume-*.jsonl"))
    assert len(backup) == 1 and len(backup[0].read_text().splitlines()) == 3
    assert reconcile_metrics(log,3) == .5
