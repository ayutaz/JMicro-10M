"""Bounded both-arm technical protocol, not CUDA readiness evidence."""
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from probe_forgetting_attention_shared_rope import assert_scope, forecast, independent_attention
from jmicro.forgetting_attention_shared_rope import ARMS, IMPLEMENTATION
from probe_forgetting_attention_shared_rope import validate_numeric_descriptors
from jmicro.experiment import sha256


def contract():
    return dict(kind='owned_forgetting_shared_rope_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, prior_technical_GPU_seconds=51.175101520027965, timed_updates_per_arm=32,
        continuous_updates_per_arm=6, split_updates=[3, 3], capacity_shape=[48, 1024],
        candidate_parameters=10014516, main_teachers_per_scientific_arm=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0,
        native_function_parity_expected=False, attention_implementation=IMPLEMENTATION,
        capacity_before_any_optimizer_update=True, Base_adopted=False, TEST_prepared=False,
        operator_lengths=[17,64], operator_absolute_tolerance=1e-2,
        operator_relative_tolerance=0., operator_all_QKV_log_gate_gradients=True,
        verify_matched_initial_states=True, preserve_verification6_before_cache=True, compare_saved_original3_numeric_state=True, compare_prefetch3_6_38_and_all32_history=True)


def test_exact_owned_scope_accepts_only_proposed_boundary():
    assert_scope(contract())


@pytest.mark.parametrize('bad', [None, 'missing_arm', 'missing_update', 'changed_bytes'])
def test_complete_numeric_descriptors_use_real_path_hashes_before_GPU(tmp_path, bad):
    path = tmp_path/'fixture.pt'
    path.write_bytes(b'unit fixture, no model or corpus')
    groups = {arm: {u: dict(path=str(path), sha256=sha256(path)) for u in ('3', '6', '38')}
              for arm in ARMS}
    if bad == 'missing_arm': del groups[ARMS[0]]
    elif bad == 'missing_update': del groups[ARMS[1]]['6']
    elif bad == 'changed_bytes': path.write_bytes(b'changed')
    if bad is None: validate_numeric_descriptors(groups)
    else:
        with pytest.raises(ValueError): validate_numeric_descriptors(groups)


@pytest.mark.parametrize('field,value', [
    ('GPU_ceiling_seconds', 181), ('maximum_new_GPU_seconds', 4801),
    ('batch', 24), ('capacity_shape', [48, 512]), ('prior_technical_GPU_seconds', 1),
    ('native_function_parity_expected', True), ('capacity_before_any_optimizer_update', False),
    ('attention_implementation', 'reference'), ('scientific_teacher_positions', 1),
    ('main_teachers_per_scientific_arm', True),
    ('preserve_verification6_before_cache', False), ('compare_saved_original3_numeric_state', False),
    ('compare_prefetch3_6_38_and_all32_history', False),
])
def test_no_budget_geometry_precision_runtime_or_science_rebinding(field, value):
    c = contract()
    c[field] = value
    with pytest.raises(ValueError): assert_scope(c)


def test_forecast_charges_both_scientific_arms_and_both_evaluation_reserves():
    timings = {a: [dict(seconds=.05)]*32 for a in ARMS}
    assert forecast(timings) == 3501
    slow = {a: [dict(seconds=.1)]*32 for a in ARMS}
    assert forecast(slow) > 4800


@pytest.mark.parametrize('bad', ['missing_arm', 'partial', 'nan', 'negative'])
def test_forecast_cannot_skip_arm_or_bad_measurements(bad):
    timings = {a: [dict(seconds=.05)]*32 for a in ARMS}
    if bad == 'missing_arm': del timings[ARMS[1]]
    elif bad == 'partial': timings[ARMS[1]] = timings[ARMS[1]][:31]
    elif bad == 'nan': timings[ARMS[1]][0] = dict(seconds=float('nan'))
    else: timings[ARMS[1]][0] = dict(seconds=-1)
    with pytest.raises(ValueError): forecast(timings)


@pytest.mark.parametrize('field,value', [
    ('prior_technical_GPU_seconds', 0), ('operator_absolute_tolerance', .1),
    ('operator_relative_tolerance', .1), ('operator_all_QKV_log_gate_gradients', False),
    ('operator_lengths', [64]),
])
def test_prior_gpu_and_all_gradient_precision_cannot_be_skipped(field, value):
    c = contract()
    c[field] = value
    with pytest.raises(ValueError): assert_scope(c)


def test_independent_dense_reference_gate_interval_and_GQA_mapping_on_CPU():
    q = torch.zeros(1, 2, 2, 64, requires_grad=True)
    k = torch.zeros(1, 1, 2, 64, requires_grad=True)
    v = torch.ones(1, 1, 2, 64)
    v[:, :, 0] = -1
    v.requires_grad_()
    gates = torch.full((1, 2, 2), -torch.log(torch.tensor(2.)).item(), requires_grad=True)
    out = independent_attention(q, k, v, gates)
    torch.testing.assert_close(out[:, :, 0], torch.full((1, 2, 64), -1.), atol=0, rtol=0)
    torch.testing.assert_close(out[:, :, 1], torch.full((1, 2, 64), 1/3), atol=1e-6, rtol=1e-6)
    out.sum().backward()
    assert all(x.grad is not None and torch.isfinite(x.grad).all() for x in (q, k, v, gates))
    assert gates.grad[:, :, 1].abs().sum() > 0
