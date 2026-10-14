from pathlib import Path
import sys

import pytest

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from probe_pseudo_repetition import assert_scope, passed_tests


def scope():
    return dict(kind='owned_native_sentence_decay_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, timed_updates=32, continuous_updates=6, split_updates=[3, 3],
        capacity_shape=[48, 1024], auxiliary_capacity_shape=[8, 512], main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0, Base_adopted=False, TEST_prepared=False)


def test_fixed_scope_accepted():
    assert_scope(scope())


@pytest.mark.parametrize('key,value', [('GPU_ceiling_seconds', 181), ('batch', 48.0),
    ('split_updates', [2, 4]), ('auxiliary_capacity_shape', [16, 512]),
    ('scientific_teacher_positions', 1), ('TEST_prepared', True)])
def test_changed_scope_rejected(key, value):
    c = scope()
    c[key] = value
    with pytest.raises(ValueError): assert_scope(c)


def test_actual_CPU_results_count_and_skips_required(tmp_path):
    p = tmp_path/'tests.xml'
    p.write_text('<testsuites><testsuite tests="14" failures="0" errors="0" skipped="0"/></testsuites>')
    passed_tests(p, 14)
    with pytest.raises(ValueError): passed_tests(p, 13)
    p.write_text('<testsuites><testsuite tests="14" failures="0" errors="0" skipped="1"/></testsuites>')
    with pytest.raises(ValueError): passed_tests(p, 14)


def test_missing_CPU_evidence_rejected(tmp_path):
    with pytest.raises(FileNotFoundError): passed_tests(tmp_path/'missing.xml', 14)
