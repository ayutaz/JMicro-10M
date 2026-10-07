"""Science budget, terminal identity/ledger and completed-update history."""
import json
from pathlib import Path
import sys
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from run_base_parallel_residual import science_budget
from review_base_parallel_residual import audit_terminal,audit_history


def probe():
    return dict(timing={a:dict(total_seconds=1.,total_original_gold=100000)
        for a in ('sequential','parallel')},GPU_seconds=15,
        forecast_arm_seconds=dict(sequential=26900,parallel=26900),
        forecast_all_new_GPU_seconds=53815,science_budget_eligible=True)


def test_two_measured_arms_required_not_cached_native():
    assert science_budget(probe())==dict(sequential=26900,parallel=26900)
    p=probe();del p['timing']['sequential']
    with pytest.raises(ValueError):science_budget(p)


def test_changed_forecast_or_total_cap_refused():
    p=probe();p['timing']['parallel']['total_seconds']=3.
    with pytest.raises(ValueError):science_budget(p)
    p=probe();p['science_budget_eligible']=False
    with pytest.raises(ValueError):science_budget(p)


def terminal():
    identity=dict(pid=100,boot_id='fixture',start_ticks='123')
    job=dict(status='complete',**identity,config_sha256='fixed',GPU_occupancy_seconds=200,cumulative_GPU_ledger_closed=True)
    result=dict(status='complete',actual_identity=identity,config_sha256='fixed',GPU_occupancy_seconds=200,
        total_GPU_seconds_including_probe=215,scientific_CE_teacher_tokens=4000000000,
        results=dict(sequential={},parallel={}),Base_complete=False,Chat_started=False,quantization_started=False)
    return job,result,dict(GPU_budget_seconds=7000,probe_GPU_seconds=15)


def test_terminal_live_job_or_unclosed_ledger_refused():
    job,result,c=terminal();audit_terminal(job,result,c,'fixed',False)
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',True)
    job['cumulative_GPU_ledger_closed']=False
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)


def test_one_arm_missing_or_changed_process_identity_refused():
    job,result,c=terminal();del result['results']['sequential']
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)
    job,result,c=terminal();result['actual_identity']['start_ticks']='124'
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)


def test_probe_cannot_be_dropped_from_occupancy():
    job,result,c=terminal();result['total_GPU_seconds_including_probe']=200
    with pytest.raises(ValueError):audit_terminal(job,result,c,'fixed',False)


def test_each_update_and_final_counters_required(tmp_path):
    from base_parallel_residual_model import POLICY
    rows=[dict(update=i,supervised_tokens=i*10,CE_loss=2.,gradient_norm=1.,lr=.002*i*10/100,
        arm='sequential',residual_policy=POLICY['kind'],committed_update=True) for i in (1,2)]
    path=tmp_path/'metrics-fixture.jsonl';path.write_text('\n'.join(json.dumps(r) for r in rows))
    state=dict(counters=dict(update=2,supervised_tokens=20),
        scheduler=dict(warmup=100,peak=.002,final=1e-5,total=1000))
    audit_history(tmp_path,state,'sequential')
    path.write_text(json.dumps(rows[1]))
    with pytest.raises(ValueError):audit_history(tmp_path,state,'sequential')
    rows[0]['lr']=1e-5
    path.write_text('\n'.join(json.dumps(r) for r in rows))
    with pytest.raises(ValueError):audit_history(tmp_path,state,'sequential')


def test_finished_science_cannot_be_restarted(monkeypatch,tmp_path):
    import run_base_parallel_residual as run
    config=tmp_path/'config.json';config.write_text('{}')
    folder=tmp_path/'science';folder.mkdir();(folder/'result.json').write_text('{}')
    monkeypatch.setattr(run,'CONFIG',config);monkeypatch.setattr(run,'RUN',folder)
    with pytest.raises(ValueError,match='finished science'):run.inspect()


def test_readonly_CPU_reader_refuses_wrong_scientific_precision_before_construction():
    from review_base_parallel_residual import CPU_reader
    with pytest.raises(ValueError,match='Actual scientific CUDA BF16/Flash'):
        CPU_reader(None,None,None,None,dict(dtype='fp32',backend='math'))


def test_exact_JSON_spec_values_ignore_serialization_tuple_only_and_refuse_changed_beta():
    from review_base_parallel_residual import metadata_equal
    state=dict(kind='fixture',optimizer_recipe=dict(betas=(.9,.999),lr=1e-5))
    record=json.loads(json.dumps(state))
    assert metadata_equal(state,record)
    record['optimizer_recipe']['betas'][1]=.998
    assert not metadata_equal(state,record)


def test_fresh_binding_has_no_parent_and_cannot_reuse_probe_weights():
    from run_base_parallel_residual import study_binding
    binding=study_binding(dict(source_binding=dict(pool='fixture'),source_sha256=dict(code='fixed')),'config')
    assert 'parent' not in binding
    assert not binding['learned_parent_weights_used'] and not binding['probe_weights_used']
    assert binding['weights_role']=='scientific_fresh_paired_residual'
