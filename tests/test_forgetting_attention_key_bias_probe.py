"""Bounded both-arm technical protocol, not CUDA readiness evidence."""
from pathlib import Path
import sys

import pytest

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from probe_forgetting_attention_key_bias import assert_scope, forecast
from jmicro.forgetting_attention_key_bias import ARMS, IMPLEMENTATION


def contract():
    return dict(kind='owned_forgetting_key_bias_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, prior_technical_GPU_seconds=0, timed_updates_per_arm=32,
        continuous_updates_per_arm=6, split_updates=[3, 3], capacity_shape=[48, 1024],
        candidate_parameters=10014516, main_teachers_per_scientific_arm=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0,
        native_function_parity_expected=False, attention_implementation=IMPLEMENTATION,
        capacity_before_any_optimizer_update=True, Base_adopted=False, TEST_prepared=False)


def test_exact_owned_scope_accepts_only_proposed_boundary():
    assert_scope(contract())


@pytest.mark.parametrize('field,value', [
    ('GPU_ceiling_seconds', 181), ('maximum_new_GPU_seconds', 4801),
    ('batch', 24), ('capacity_shape', [48, 512]), ('prior_technical_GPU_seconds', 1),
    ('native_function_parity_expected', True), ('capacity_before_any_optimizer_update', False),
    ('attention_implementation', 'reference'), ('scientific_teacher_positions', 1),
    ('main_teachers_per_scientific_arm', True),
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
