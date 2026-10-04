"""Prevent weaker growth gates and mismatched evaluation comparisons."""
from copy import deepcopy
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from compare_base_10b import growth_checks, require_alignment


def summary():
    return {'full_dev_BPB': .95, 'fixed80': {'repetition': 57},
            'all400': {'empty': 0, 'role_leak': 0, 'unicode_failure': 0}}


@pytest.mark.parametrize('failure', ['empty', 'role_leak', 'unicode_failure'])
def test_raw_failure_rejects_even_when_reference_also_failed(failure):
    current, parent = summary(), summary()
    current['all400'][failure] = parent['all400'][failure] = 1
    assert not growth_checks(current, parent)['raw_unicode_empty_role_zero_all400']


def test_exact_eight_repetition_regression_rejects():
    current, parent = summary(), summary()
    current['fixed80']['repetition'] += 8
    assert not growth_checks(current, parent)['fixed_repetition_not8_worse']
    current['fixed80']['repetition'] -= 1
    assert growth_checks(current, parent)['fixed_repetition_not8_worse']


def test_BPB_safety_boundary():
    current, parent = summary(), summary()
    current['full_dev_BPB'] = parent['full_dev_BPB'] + .001
    assert growth_checks(current, parent)['full_BPB_no_major_regression']
    current['full_dev_BPB'] += .000001
    assert not growth_checks(current, parent)['full_BPB_no_major_regression']


@pytest.mark.parametrize('change', ['doc', 'coverage', 'seed', 'prefix', 'temperature'])
def test_alignment_rejects_changed_input_or_protocol(change):
    body = {'rows': [{'doc_id': 'd', 'body_bytes': 8, 'body_tokens': 4, 'scored_body_tokens': 4}]}
    gen = {'outputs': [{'id': 'p', 'prefix': '日本語', 'category': 'a', 'decoding': 'sample', 'suppressed': True, 'seed': 42}],
           'suite_sha256': 's', 'max_new_tokens': 64, 'sampling_evaluated': True, 'temperature': .8, 'top_p': .9}
    other_body, other_gen = deepcopy(body), deepcopy(gen)
    require_alignment(body, gen, other_body, other_gen)
    if change == 'doc':
        other_body['rows'][0]['doc_id'] = 'different'
    elif change == 'coverage':
        other_body['rows'][0]['scored_body_tokens'] -= 1
    elif change in ('seed', 'prefix'):
        other_gen['outputs'][0][change] = 44 if change == 'seed' else '違う入力'
    else:
        other_gen['temperature'] = .9
    with pytest.raises(AssertionError):
        require_alignment(body, gen, other_body, other_gen)
