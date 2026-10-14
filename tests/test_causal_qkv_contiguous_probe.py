"""Scope and actual CPU prerequisites for a NEW implementation probe."""
from pathlib import Path
import sys

import pytest

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from probe_causal_qkv_contiguous import assert_scope,passed_tests,check_cache,IMPLEMENTATION


def scope():
    prior=19.769017330021597
    return dict(kind='owned_same_math_causal_QKV_contiguous_CUDA_v1',batch=48,seed=42,
        timed_updates=32,continuous_updates=6,split_updates=[3,3],reference_comparison_updates=3,
        reference_start_update=3,capacity_shape=[48,1024],candidate_parameters=10014464,
        main_teacher_goal=100000000,combined_technical_GPU_cap_seconds=180,
        maximum_new_GPU_seconds=4800,scientific_teacher_positions=0,Base_adopted=False,TEST_prepared=False,
        runtime_implementation=IMPLEMENTATION,prior_reference_GPU_seconds=prior,current_GPU_ceiling_seconds=180-prior)


def test_exact_scope_accepted():
    assert_scope(scope())


@pytest.mark.parametrize('key,value',[
    ('prior_reference_GPU_seconds',0.),('current_GPU_ceiling_seconds',180.),
    ('combined_technical_GPU_cap_seconds',181),('maximum_new_GPU_seconds',4801),
    ('reference_comparison_updates',2),('runtime_implementation','unbound')])
def test_cannot_reset_technical_ledger_expand_caps_or_skip_actual_comparison(key,value):
    c=scope()
    c[key]=value
    with pytest.raises(ValueError): assert_scope(c)


def test_CPU_report_count_and_no_skips_required(tmp_path):
    path=tmp_path/'actual.xml'
    path.write_text('<testsuites><testsuite tests="15" failures="0" errors="0" skipped="0"/></testsuites>')
    passed_tests(path,15)
    with pytest.raises(ValueError): passed_tests(path,14)
    path.write_text('<testsuites><testsuite tests="15" failures="0" errors="0" skipped="1"/></testsuites>')
    with pytest.raises(ValueError): passed_tests(path,15)


def test_missing_actual_CPU_evidence_rejected(tmp_path):
    with pytest.raises(FileNotFoundError): passed_tests(tmp_path/'missing.xml',15)


def test_generic_raw_cache_gate_unchanged_in_optimized_runtime():
    from types import SimpleNamespace
    import torch
    from jmicro.causal_qkv_contiguous import ContiguousCausalQKVModel
    from jmicro.phase5 import equal_state
    from test_value_residual import native
    model=ContiguousCausalQKVModel.from_native(native()).train()
    with torch.no_grad():
        for layer in model.model.layers:
            for name in ('q_lag','k_lag','v_lag'): getattr(layer.self_attn,name).fill_(.2)
    before={k:v.clone() for k,v in model.state_dict().items()}
    result=check_cache(SimpleNamespace(model=model,device=torch.device('cpu')),dict(input_ids=[65,66,67]*342))
    assert result['passed'] and result['raw_projected_history_passed'] and result['optimizer_updates']==0
    assert model.training and equal_state(before,model.state_dict())


def test_remaining_time_is_the_original180_minus_consumed_reference():
    c=scope()
    assert 0<c['current_GPU_ceiling_seconds']<180
    assert c['current_GPU_ceiling_seconds']+c['prior_reference_GPU_seconds']==180
