"""Preflight/accounting guards; fixtures are not actual GPU experiment evidence."""
import sys

import pytest

from jmicro.experiment import ROOT,write_json

sys.path.insert(0,str(ROOT/"scripts"))
import run_sequence_objective_comparison as runner
from review_sequence_objective_comparison import audit_extra


def test_live_source_refuses_plan_without_new_recipe(tmp_path,monkeypatch):
    run=tmp_path/"source";run.mkdir();write_json(run/"job.json",dict(status="complete"))
    monkeypatch.setattr(runner,"SOURCE_RUN",run);monkeypatch.setattr(runner,"alive",lambda _:True)
    monkeypatch.setattr(runner,"PROBE_CONFIG",tmp_path/"not-created.json")
    with pytest.raises(ValueError,match="must finish"):runner.prepare_probe()
    assert not runner.PROBE_CONFIG.exists()


def test_incomplete_source_refuses_plan_without_creating_recipe(tmp_path,monkeypatch):
    run=tmp_path/"source";run.mkdir();write_json(run/"job.json",dict(status="running"))
    monkeypatch.setattr(runner,"SOURCE_RUN",run);monkeypatch.setattr(runner,"alive",lambda _:False)
    monkeypatch.setattr(runner,"PROBE_CONFIG",tmp_path/"not-created.json")
    with pytest.raises(ValueError,match="must finish"):runner.prepare_probe()
    assert not runner.PROBE_CONFIG.exists()


def test_extra_accounting_refuses_hidden_generated_teachers_and_missing_rollout():
    from sequence_objective_trainer import source_binding
    o=dict(alpha=.1,every_updates=4,prefixes=8)
    counters=dict(source_sha256=source_binding(),objective=o,rollout_batches=0,skipped_rollouts=0,
        generated_continuations=0,generated_body_tokens=0,generated_EOS=0,negative_token_positions=0,
        extra_valid_input_tokens=0,extra_physical_input_tokens=0)
    state=dict(lineage=dict(sequence_objective=counters),spec=dict(sequence_objective=o))
    d=dict(binding=dict(arm="CE_UL"),sequence_objective=counters)
    history=[dict(sequence_objective=counters,sequence_UL=0.,optimization_loss=1.,loss=1.)]
    with pytest.raises(AssertionError):audit_extra(state,d,history,dict(objectives=dict(CE_UL=o)))
