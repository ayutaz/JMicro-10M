"""CPU protocol/state evidence only; no simulated records used as GPU quality."""
import copy
import sys
from types import SimpleNamespace
import pytest
import torch
from jmicro.experiment import ROOT, write_json, sha256

sys.path.insert(0,str(ROOT/"scripts"))
from run_seeded_base_confirmation import preflight, freeze, validate_zero
from review_seeded_base_confirmation import review, audit_replicate_checkpoint
from seeded_textbook_trainer import make_zero_parent, SeededThreeSourceTrainer
from test_textbook_curve_extension import fixture
from phase6_performance import identity


def test_seed_confirmation_refuses_live_source_before_model_or_recipe_creation(tmp_path):
    run=tmp_path/"learning";run.mkdir();write_json(run/"job.json",dict(status="running"))
    config=tmp_path/"config.json";write_json(config,dict(source_run=str(run)))
    with pytest.raises(ValueError,match="actually finish"):preflight(config)
    write_json(run/"job.json",dict(status="complete",**identity()))
    target=tmp_path/"new.json"
    args=SimpleNamespace(source_run=run,training_config=ROOT/"configs/phase6/missing-seed-source-fixture.json",point="large-1000000000")
    with pytest.raises(ValueError,match="actually finish"):freeze(target,args)
    assert not target.exists()


def test_unfinished_replicate_review_cannot_publish_confirmation(tmp_path):
    run=tmp_path/"replicate";run.mkdir();write_json(run/"job.json",dict(status="running"))
    path=tmp_path/"config.json";write_json(path,dict(output=str(run)))
    with pytest.raises(ValueError,match="actually finish"):review(path,tmp_path/"notes.json")
    assert not (run/"review.json").exists() and not (run/"annotations.json").exists()


def test_actual_cpu_zero_and_learning_counters_prove_distinct_seed_and_reject_lost_history(tmp_path,monkeypatch):
    monkeypatch.setattr(torch.cuda,"is_available",lambda:False)
    _,original,shard,binding,_=fixture(tmp_path)
    path=tmp_path/"initial43.pt";zero=make_zero_parent(original,shard,path,seed=43)
    validate_zero(zero,original,43)
    invalid=copy.deepcopy(zero);invalid["model"]=original["model"]
    with pytest.raises(AssertionError):validate_zero(invalid,original,43)
    invalid=copy.deepcopy(zero);invalid["rng"]=original["rng"]
    with pytest.raises(AssertionError):validate_zero(invalid,original,43)
    parent=dict(path=str(path),sha256=sha256(path),update=0,tokens_seen=0)
    b=dict(binding,training_seed=43,parent=parent)
    trainer=SeededThreeSourceTrainer(zero,shard,shard,"shuffle",dict(web=0,short=2000),b,device="cpu")
    history=[]
    while trainer.sampler.source_teachers["short"]<2000:history.append(trainer.step())
    final=tmp_path/"final43.pt";trainer.save(final)
    state=torch.load(final,map_location="cpu",weights_only=False)
    record=dict(checkpoint=str(final),checkpoint_sha256=sha256(final),binding=b,
        additional_supervised_tokens=state["supervised_tokens"],additional_input_tokens=state["tokens"],
        physical_input_tokens=sum(state["sampler"]["source_physical_tokens"].values()),
        genre_teachers=state["sampler"]["genre_teachers"],genre_eos=state["sampler"]["genre_eos"],
        training_step_seconds=sum(r["seconds"] for r in history))
    config=dict(parent=parent,peak_lr=.002,warmup_updates=2,decay_teacher_tokens=1000)
    audit_replicate_checkpoint(record,history,config,"stable",2000,b["config_sha256"])
    with pytest.raises(AssertionError):audit_replicate_checkpoint(record,history[:-1],config,"stable",2000,b["config_sha256"])
    with pytest.raises(AssertionError):audit_replicate_checkpoint(record,history,config,"stable",2001,b["config_sha256"])
