"""Scope/budget/evidence gates without CUDA or real held-out inputs."""
import copy
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from probe_context_likelihood import assert_scope, passed_tests


def scope():
    return dict(kind='owned_native_context_likelihood_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, timed_updates=32, continuous_updates=6, split_updates=[3, 3],
        capacity_shape=[48, 1024], auxiliary_capacity_shape=[96, 512], main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0, Base_adopted=False, TEST_prepared=False)


def test_fixed_probe_scope_is_accepted():
    assert_scope(scope())


@pytest.mark.parametrize('field,value', [('GPU_ceiling_seconds', 181), ('batch', 64),
    ('split_updates', [2, 4]), ('scientific_teacher_positions', 1), ('TEST_prepared', True)])
def test_changed_scope_rejected(field, value):
    c = scope()
    c[field] = value
    with pytest.raises(ValueError): assert_scope(c)


def test_CPU_results_count_and_skips_are_checked(tmp_path):
    path = tmp_path / 'tests.xml'
    path.write_text('<testsuites><testsuite tests="12" failures="0" errors="0" skipped="0"/></testsuites>')
    passed_tests(path, 12)
    with pytest.raises(ValueError): passed_tests(path, 11)
    path.write_text('<testsuites><testsuite tests="12" failures="0" errors="0" skipped="1"/></testsuites>')
    with pytest.raises(ValueError): passed_tests(path, 12)


def test_missing_CPU_evidence_rejected(tmp_path):
    with pytest.raises(FileNotFoundError): passed_tests(tmp_path / 'missing.xml', 12)
