"""Actual small CPU optimizer trajectories; not GPU/quality evidence."""
import copy
import sys

import pytest
import torch

from jmicro.experiment import ROOT,sha256
from jmicro.training import rng_state

sys.path.insert(0,str(ROOT/"scripts"))
from test_textbook_curve_extension import fixture
from sequence_objective_trainer import SequenceObjectiveTrainer,train_prefixes
from textbook_quantity_trainer import ThreeSourceTrainer
from run_eos_short_pilot import equal_state


def build_fixture(tmp_path,monkeypatch,alpha=.1):
    monkeypatch.setattr(torch.cuda,"is_available",lambda:False)
    path,_,shard,_,_=fixture(tmp_path)
    parent=torch.load(path,map_location="cpu",weights_only=False)
    binding=dict(config_sha256="objective-fixture",parent=dict(path=str(path),sha256=sha256(path)),
        peak_lr=.001,warmup_updates=0,optimizer_policy="inherit",initialization="completed-parent-fork",
        curve_mode="decay",curve_boundaries=[2500],
        sequence_objective=dict(alpha=alpha,every_updates=1,prefixes=2,prefix_tokens=4,max_new_tokens=6,ngram=2))
    def build():return SequenceObjectiveTrainer(parent,shard,shard,"shuffle",dict(web=0,short=2500),binding,device="cpu")
    return parent,shard,binding,build


def test_real_optimizer_full_state_and_generated_counters_match_resume(tmp_path,monkeypatch):
    parent,_,_,build=build_fixture(tmp_path,monkeypatch)
    trainer=build()
    assert equal_state(trainer.model.state_dict(),parent["model"])
    assert equal_state(trainer.optimizer.state_dict()["state"],parent["optimizer"]["state"])
    assert equal_state(rng_state(),parent["rng"])
    first=trainer.step();trainer.save(tmp_path/"split.pt")
    second=trainer.step();trainer.save(tmp_path/"continuous.pt")
    resumed=build();resumed.load(tmp_path/"split.pt");actual=resumed.step();resumed.save(tmp_path/"resumed.pt")
    a=torch.load(tmp_path/"continuous.pt",map_location="cpu",weights_only=False)
    b=torch.load(tmp_path/"resumed.pt",map_location="cpu",weights_only=False)
    assert all(equal_state(a[k],b[k]) for k in ("model","optimizer","scheduler","rng","sampler","lineage","tokens","supervised_tokens","update","token_digest"))
    assert all(equal_state(second[k],actual[k]) for k in ("loss","sequence_UL","gradient_norm","lr","sequence_objective"))
    counts=first["sequence_objective"]
    assert counts["rollout_batches"]==1 and counts["generated_continuations"]==2
    assert counts["extra_physical_input_tokens"]>0 and counts["extra_valid_input_tokens"]<=counts["extra_physical_input_tokens"]
    split=torch.load(tmp_path/"split.pt",map_location="cpu",weights_only=False)
    assert first["additional_supervised_tokens"]==split["supervised_tokens"]-parent["supervised_tokens"]
    assert split["tokens"]-parent["tokens"]==1024
    assert counts["extra_physical_input_tokens"] not in (0,split["tokens"]-parent["tokens"])


def test_zero_alpha_has_same_CE_optimizer_trajectory_and_separate_extra_work(tmp_path,monkeypatch):
    parent,shard,binding,build=build_fixture(tmp_path,monkeypatch,alpha=0.)
    trainer=build();actual=trainer.step()
    control=ThreeSourceTrainer(parent,shard,shard,"shuffle",dict(web=0,short=2500),binding,device="cpu")
    expected=control.step()
    assert equal_state(trainer.model.state_dict(),control.model.state_dict())
    assert equal_state(trainer.optimizer.state_dict(),control.optimizer.state_dict())
    assert equal_state(trainer.sampler.state_dict(),control.sampler.state_dict())
    assert actual["loss"]==expected["loss"] and actual["token_digest"]==expected["token_digest"]
    assert actual["sequence_objective"]["rollout_batches"]==1


def test_refuses_unfinished_parent_LR_reheat_and_modified_resume_source(tmp_path,monkeypatch):
    parent,shard,binding,build=build_fixture(tmp_path,monkeypatch)
    unfinished=copy.deepcopy(parent);unfinished["sampler"]["source_teachers"]["short"]-=1
    with pytest.raises(ValueError,match="completed actual parent"):
        SequenceObjectiveTrainer(unfinished,shard,shard,"shuffle",dict(web=0,short=2500),binding,device="cpu")
    changed=dict(binding,peak_lr=.003)
    with pytest.raises(ValueError,match="reheat"):
        SequenceObjectiveTrainer(parent,shard,shard,"shuffle",dict(web=0,short=2500),changed,device="cpu")
    trainer=build();trainer.step();trainer.save(tmp_path/"checkpoint.pt")
    state=torch.load(tmp_path/"checkpoint.pt",map_location="cpu",weights_only=False)
    state["lineage"]["sequence_objective"]["source_sha256"]={};torch.save(state,tmp_path/"modified.pt")
    with pytest.raises(ValueError,match="source differs"):build().load(tmp_path/"modified.pt")


def test_train_prefixes_never_cross_packed_document_boundaries():
    x=torch.tensor([[9,9,2,8,9,3,2,10,11,12,13,3]])
    assert train_prefixes([(x,x,0)],8,4).tolist()==[[2,10,11,12]]
    assert train_prefixes([(x,x,0)],8,7) is None
