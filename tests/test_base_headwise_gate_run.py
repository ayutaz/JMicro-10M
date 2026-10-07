"""Science budget, terminal identity/ledger and completed-update history."""
import json
from pathlib import Path
import sys
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from run_base_headwise_gate import science_budget
from review_base_headwise_gate import audit_terminal,audit_history


def probe():
    return dict(arms={a:dict(all32_step_seconds=2.,all32_original_gold=100000)
        for a in ('static_half','query_headwise')},GPU_occupancy_seconds=15,
        science_budget_seconds=dict(static_half=3500,query_headwise=3500),science_budget_eligible=True)


def test_two_measured_arms_required_not_cached_native():
    assert science_budget(probe())==dict(static_half=3500,query_headwise=3500)
    p=probe();del p['arms']['static_half']
    with pytest.raises(ValueError):science_budget(p)


def test_changed_forecast_or_total_cap_refused():
    p=probe();p['arms']['query_headwise']['all32_step_seconds']=3.
    with pytest.raises(ValueError):science_budget(p)
    p=probe();p['science_budget_eligible']=False
    with pytest.raises(ValueError):science_budget(p)


def terminal():
    identity=dict(pid=100,boot_id='fixture',start_ticks='123')
    job=dict(status='complete',**identity,config_sha256='fixed',GPU_occupancy_seconds=200,cumulative_GPU_ledger_closed=True)
    result=dict(status='complete',actual_identity=identity,config_sha256='fixed',GPU_occupancy_seconds=200,
        total_GPU_seconds_including_probe=215,scientific_CE_teacher_tokens=200000000,
        results=dict(static_half={},query_headwise={}),Base_complete=False,Chat_started=False,quantization_started=False)
    return job,result,dict(GPU_budget_seconds=7000,probe_GPU_seconds=15)


def test_terminal_live_job_or_unclosed_ledger_refused():
    job,result,c=terminal();audit_terminal(job,result,c,'fixed',False)
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',True)
    job['cumulative_GPU_ledger_closed']=False
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)


def test_one_arm_missing_or_changed_process_identity_refused():
    job,result,c=terminal();del result['results']['static_half']
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)
    job,result,c=terminal();result['actual_identity']['start_ticks']='124'
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)


def test_probe_cannot_be_dropped_from_occupancy():
    job,result,c=terminal();result['total_GPU_seconds_including_probe']=200
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)


def test_each_update_and_final_counters_required(tmp_path):
    from base_headwise_gate_model import POLICY
    rows=[dict(update=i,supervised_tokens=i*10,CE_loss=2.,lr=1e-5,gate_arm='static_half',
        gate_policy=POLICY['kind'],committed_update=True) for i in (1,2)]
    path=tmp_path/'metrics-fixture.jsonl';path.write_text('\n'.join(json.dumps(r) for r in rows))
    state=dict(counters=dict(update=2,supervised_tokens=20));audit_history(tmp_path,state,'static_half')
    path.write_text(json.dumps(rows[1]))
    with pytest.raises(ValueError):audit_history(tmp_path,state,'static_half')


def test_finished_science_cannot_be_restarted(monkeypatch,tmp_path):
    import run_base_headwise_gate as run
    config=tmp_path/'config.json';config.write_text('{}')
    folder=tmp_path/'science';folder.mkdir();(folder/'result.json').write_text('{}')
    monkeypatch.setattr(run,'CONFIG',config);monkeypatch.setattr(run,'RUN',folder)
    with pytest.raises(ValueError,match='finished science'):run.inspect()
