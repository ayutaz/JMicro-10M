import ast
import copy
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
import run_source_order_condition_comparison as original
import run_source_order_condition_comparison_v2 as study
import source_order_budget_evidence as evidence


def test_science_bodies_and_scope_identical_with_actual_probe_reuse():
    parse=lambda p:{n.name:ast.dump(n,include_attributes=False) for n in ast.parse(p.read_text()).body if isinstance(n,ast.FunctionDef)}
    a=parse(ROOT/'scripts/run_source_order_condition_comparison.py')
    b=parse(ROOT/'scripts/run_source_order_condition_comparison_v2.py')
    for name in ('scope','binding','trainer_for','resume_gate','source_contract','cpu_state','summarize_transfer','transfer_scores'):
        assert a[name]==b[name],name
    assert study.PROBE_RUN==original.RUN/'probe'
    assert study.PROBE_CONFIG==original.PROBE_CONFIG
    assert study.CEILING==original.CEILING==900


def test_real_timing_and_same_evaluation_evidence_are_required(monkeypatch):
    monkeypatch.setattr(evidence,'alive',lambda _:False)
    ev=dict(checkpoint_sha256='cp',body=dict(documents=256,body_bytes=472055),generation=dict(outputs=[{}]*80),
        diagnostics={k:dict(complete=True,count=n) for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()},protected_test_used=False)
    result=dict(GPU_seconds=120.,checkpoints=dict(arm=dict(training_seconds=30.,additional_supervised_tokens=100000000,checkpoint_sha256='cp')),
        evaluations=dict(arm=ev),transfer=dict(arm=dict(evaluated_requests=512)),retention=dict(arm=dict(evaluated_requests=512)))
    job=dict(status='complete',GPU_elapsed_seconds=120.)
    assert evidence.matched_nontraining_seconds(result,job,'arm',[dict(seconds=10.),dict(seconds=20.)])['nontraining_GPU_occupancy_seconds']==90.
    bad=copy.deepcopy(result);bad['evaluations']['arm']['diagnostics']['jcqa']['count']=1118
    with pytest.raises(ValueError):evidence.matched_nontraining_seconds(bad,job,'arm',[dict(seconds=30.)])
    with pytest.raises(ValueError):evidence.matched_nontraining_seconds(result,job,'arm',[dict(seconds=29.)])


def test_estimate_includes_entire_probe_and_cannot_grow_budget(monkeypatch):
    measured=dict(timing=dict(histories=[dict(seconds=.14)]*32,verification_teacher_tokens=1040000,terminal_save_seconds=.2))
    monkeypatch.setattr(study.budget_evidence,'inspect',lambda:dict(nontraining_reserve_seconds=150.))
    monkeypatch.setattr(study,'sha256',lambda _:'evidence')
    timing,total=study.estimate_training(measured)
    assert total==(timing['estimated_training_seconds']+150.)*1.3+50.
    monkeypatch.setattr(study.budget_evidence,'inspect',lambda:dict(nontraining_reserve_seconds=400.))
    assert study.estimate_training(measured)[1]+20.29770903699682>900
