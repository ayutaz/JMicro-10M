"""Scientific launch, matched stream and additional-head finite-state guards."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
import run_base_next_two_token as runner


def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value))


def test_terminal_label_cannot_bypass_actual_live_probe(tmp_path,monkeypatch):
    monkeypatch.setattr(runner,'CONFIG',tmp_path/'config.json');monkeypatch.setattr(runner,'PROBE',tmp_path/'probe')
    monkeypatch.setattr(runner,'alive',lambda _:True)
    write(runner.PROBE/'job.json',dict(status='complete'));write(runner.PROBE/'result.json',dict(passed=True))
    with pytest.raises(ValueError,match='Actual completed'):runner.freeze()
    assert not runner.CONFIG.exists()


def test_live_science_rejected_before_reference_or_UI_access(tmp_path,monkeypatch):
    monkeypatch.setattr(runner,'CONFIG',tmp_path/'config.json');monkeypatch.setattr(runner,'RUN',tmp_path/'run')
    monkeypatch.setattr(runner,'alive',lambda _:True)
    write(runner.CONFIG,{});write(runner.RUN/'job.json',dict(status='running'))
    with pytest.raises(ValueError,match='already alive'):runner.inspect()


def test_control_requires_original_physical_counts_and_complete_sampler():
    counts=dict(update=3,token_digest='bound',supervised_tokens=100,source_teachers={},source_EOS={},
        CE_input_tokens=110,original_body_bytes=300,auxiliary_input_tokens=0,auxiliary_pairs=0,physical_input_tokens=180)
    a=dict(counters=counts,sampler=dict(cursor=9,RNG=[1,2]))
    assert all(runner.matched_control_checks(a,a).values())
    b=copy.deepcopy(a);b['counters']['physical_input_tokens']+=1
    assert not runner.matched_control_checks(a,b)['physical_input_tokens']
    b=copy.deepcopy(a);b['sampler']['RNG'][1]+=1
    assert not runner.matched_control_checks(a,b)['full_sampler']


def test_actual_budget_formula_accepts_measured_next_two_only_within_original_cap():
    assert runner.budget_from_speed(44940.797203392896)==3793
    for speed in (40980.,0,float('nan'),float('inf')):
        with pytest.raises(ValueError):runner.budget_from_speed(speed)


def test_native_and_auxiliary_finite_and_separate_future_mass_required(monkeypatch):
    monkeypatch.setattr(runner,'finite_state',lambda _:True)
    state=dict(kind=runner.KIND,spec=dict(next_two_coefficient=.1,contrast=False),
        model_config=dict(dropout=0,expected_parameter_count=10001152),auxiliary_model=dict(weight=torch.ones(1)),
        counters=dict(supervised_tokens=100,next_two_teacher_positions=98,source_next_two_teachers={'web':98},
            next_two_EOS_targets=2,source_next_two_EOS={'web':2},next_two_target_mass=.1*98,
            auxiliary_input_tokens=0,auxiliary_pairs=0,auxiliary_digest='0'*64))
    assert runner.finite_next_two_state(state)
    changed=copy.deepcopy(state);changed['auxiliary_model']['weight'][0]=float('nan')
    assert not runner.finite_next_two_state(changed)
    changed=copy.deepcopy(state);changed['counters']['next_two_target_mass']+=1
    assert not runner.finite_next_two_state(changed)
