"""Actual CPU optimizer/RNG/cursor tests, not independent CUDA quality evidence."""
import copy
import sys
import torch
import pytest
from jmicro.experiment import ROOT, sha256
from jmicro.training import rng_state

sys.path.insert(0, str(ROOT/"scripts"))
from test_textbook_curve_extension import fixture
from seeded_textbook_trainer import make_zero_parent, SeededThreeSourceTrainer
from run_eos_short_pilot import equal_state


def test_independent_zero_has_different_weights_rng_and_material_order_and_resumes(tmp_path, monkeypatch):
    monkeypatch.setattr(torch.cuda, "is_available", lambda:False)
    _, original, shard, binding, _ = fixture(tmp_path)
    zero_path = tmp_path/"seed43-zero.pt"
    zero = make_zero_parent(original, shard, zero_path, seed=43)
    assert zero["update"] == zero["tokens"] == zero["supervised_tokens"] == 0 and not zero["optimizer"]["state"]
    assert not equal_state(original["model"], zero["model"])
    assert not equal_state(original["rng"], zero["rng"])
    replicate_binding = dict(binding, training_seed=43, parent=dict(path=str(zero_path), sha256=sha256(zero_path)))
    def build():
        return SeededThreeSourceTrainer(zero, shard, shard, "shuffle", dict(web=0,short=2000), replicate_binding, device="cpu")
    trainer = build()
    assert equal_state(trainer.model.state_dict(), zero["model"]) and equal_state(rng_state(), zero["rng"])
    assert trainer.spec["seed"] == trainer.sampler.short.seed == 43
    assert trainer.sampler.web.seed == 42 and trainer.sampler.goals["web"] == 0
    from textbook_quantity_trainer import ThreeSourceTrainer
    control = ThreeSourceTrainer(original, shard, shard, "shuffle", dict(web=0,short=2000), binding, device="cpu")
    assert not (control.sampler.short.documents == trainer.sampler.short.documents).all()
    trainer = build(); first = trainer.step(); trainer.save(tmp_path/"split.pt")
    second = trainer.step(); trainer.save(tmp_path/"continuous.pt")
    resumed = build(); resumed.load(tmp_path/"split.pt"); actual = resumed.step(); resumed.save(tmp_path/"resumed.pt")
    a = torch.load(tmp_path/"continuous.pt", map_location="cpu", weights_only=False)
    b = torch.load(tmp_path/"resumed.pt", map_location="cpu", weights_only=False)
    assert all(equal_state(a[k],b[k]) for k in ("model","optimizer","scheduler","rng","sampler","lineage","tokens","supervised_tokens","update","token_digest"))
    assert all(second[k] == actual[k] for k in ("loss","gradient_norm","lr","token_digest"))
    assert first["lr"] == .001 and second["lr"] == .002
    while resumed.sampler.source_teachers["short"] < 2000: resumed.step()
    resumed.save(tmp_path/"stable-complete.pt")
    stable = torch.load(tmp_path/"stable-complete.pt", map_location="cpu", weights_only=False)
    # Actual decay uses the stable replicate cursor/Adam/RNG, without silently
    # going back to source seed42 or resetting the short-material position.
    decay_binding = dict(replicate_binding, curve_mode="decay", curve_boundaries=[1000],
        warmup_updates=0, optimizer_policy="inherit", initialization="stable-fork")
    decay = SeededThreeSourceTrainer(stable, shard, shard, "shuffle", dict(web=0,short=1000), decay_binding, device="cpu")
    assert equal_state(decay.sampler.short.state_dict(), stable["sampler"]["short"])
    assert equal_state(decay.optimizer.state_dict()["state"], stable["optimizer"]["state"])
    assert equal_state(rng_state(), stable["rng"])
    assert decay.sampler.source_teachers == dict(web=0,short=0)


def test_independent_zero_refuses_same_seed_learned_parent_and_overwrite(tmp_path, monkeypatch):
    monkeypatch.setattr(torch.cuda, "is_available", lambda:False)
    learned_path, original, shard, _, _ = fixture(tmp_path)
    with pytest.raises(ValueError, match="distinct"):
        make_zero_parent(original, shard, tmp_path/"same.pt", seed=42)
    learned = torch.load(learned_path, map_location="cpu", weights_only=False)
    with pytest.raises(ValueError, match="zero-update"):
        make_zero_parent(learned, shard, tmp_path/"learned.pt", seed=43)
    path = tmp_path/"new.pt"; make_zero_parent(original, shard, path, seed=43)
    with pytest.raises(ValueError, match="never overwritten"):
        make_zero_parent(original, shard, path, seed=43)


def test_replicate_refuses_wrong_seed_resume_and_incomplete_stable_decay(tmp_path, monkeypatch):
    monkeypatch.setattr(torch.cuda, "is_available", lambda:False)
    _, original, shard, binding, _ = fixture(tmp_path)
    path = tmp_path/"zero43.pt"; zero = make_zero_parent(original, shard, path, seed=43)
    b = dict(binding, training_seed=43, parent=dict(path=str(path),sha256=sha256(path)))
    trainer = SeededThreeSourceTrainer(zero, shard, shard, "shuffle", dict(web=0,short=2000), b, device="cpu")
    trainer.step(); saved_path=tmp_path/"partial.pt"; trainer.save(saved_path)
    partial = torch.load(saved_path,map_location="cpu",weights_only=False)
    decay_binding = dict(b, curve_mode="decay", curve_boundaries=[1000], warmup_updates=0,optimizer_policy="inherit")
    with pytest.raises(ValueError, match="actual stable cursor"):
        SeededThreeSourceTrainer(partial, shard, shard, "shuffle", dict(web=0,short=1000), decay_binding, device="cpu")
    changed = copy.deepcopy(partial); changed["lineage"]["independent_training_seed"]["seed"] = 44
    torch.save(changed,tmp_path/"wrong-seed.pt")
    with pytest.raises(ValueError, match="seed/source provenance"):
        trainer.load(tmp_path/"wrong-seed.pt")
