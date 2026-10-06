import copy
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from review_natural_context_semantic_clusters import paired, summary, validate_cached


def cases(family, credits=(1., 0.), contexts=('yes context', 'no context')):
    return [dict(id=f'{family}-{i}', family=family, category='negation', split='dev', context=context,
                 choices=['yes', 'no'], label=i, credit=credits[i]) for i, context in enumerate(contexts)]


def test_aliases_keep_case_weights_without_inflating_independent_clusters():
    rows = cases('original') + cases('alias') + cases('other', (1., 1.), ('different yes', 'different no'))
    report = summary(rows)
    assert report['cases'] == 6 and report['nominal_families'] == 3
    assert report['exact_content_pair_clusters'] == 2
    assert report['original_nominal_accuracy']['point'] == report['content_cluster_accuracy']['point'] == 4 / 6
    assert report['content_cluster_accuracy']['examples'] == 6
    assert report['content_cluster_accuracy']['units'] == 2
    assert report['both_contexts_hard_correct']['units'] == 2
    improved = [{**r, 'credit': 1.} for r in rows]
    comparison = paired(rows, improved)
    assert comparison['candidate_minus_control']['point'] == 2 / 6
    assert comparison['candidate_minus_control']['units'] == 2


def test_paired_context_and_gold_identity_are_required():
    original = cases('original')
    for key, value in (('context', 'changed'), ('label', 1), ('choices', ['no', 'yes'])):
        other = copy.deepcopy(original)
        other[0][key] = value
        with pytest.raises(ValueError, match='gold labels'):
            paired(original, other)


def test_incomplete_or_test_or_checkpoint_mismatched_cache_is_rejected():
    trained = dict(status='complete', binding={'config': 'fixed'}, checkpoint_sha256='checkpoint')
    cache = dict(complete=True, expected=2, rows=cases('family'),
                 binding=json.dumps(dict(binding=trained['binding'], checkpoint_sha256='checkpoint'), sort_keys=True))
    assert len(validate_cached(cache, trained, 2)) == 2
    for change in ({'complete': False}, {'binding': 'other'}, {'rows': cache['rows'][:1]},
                   {'rows': [{**r, 'split': 'test'} for r in cache['rows']]}):
        with pytest.raises(ValueError, match='DEV semantic cache'):
            validate_cached({**cache, **change}, trained, 2)
