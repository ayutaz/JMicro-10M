import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analyze_story_weight_condition_pairs import pair_categories


def pair(scores):
    rows = []
    for label, values in enumerate(scores):
        top = max(values); winners = [i for i, v in enumerate(values) if v == top]
        rows.append(dict(id=f'f-{label}', family='f', category='negation', split='dev',
                         context=f'context{label}', choices=['yes', 'no'], label=label,
                         scores=values, credit=int(label in winners) / len(winners)))
    return rows


def test_chance_accuracy_can_hide_same_prediction_despite_context_response():
    result = pair_categories(pair([[3., 0.], [1., 0.]]))['negation']
    assert result['accuracy'] == .5 and result['both_correct'] == 0
    assert result['same_unique_prediction'] == 1 and result['unique_prediction_changes'] == 0
    assert result['aligned_context_margin_shift'] == 1


def test_changing_prediction_is_not_necessarily_correct():
    right = pair_categories(pair([[2., 0.], [0., 2.]]))['negation']
    wrong = pair_categories(pair([[0., 2.], [2., 0.]]))['negation']
    assert right['both_correct'] == 1 and wrong['neither_correct'] == 1
    assert right['unique_prediction_changes'] == wrong['unique_prediction_changes'] == 1
    assert wrong['aligned_context_margin_shift'] == 0


def test_ties_do_not_count_as_correct_pairs_or_unique_predictions():
    result = pair_categories(pair([[0., 0.], [0., 0.]]))['negation']
    assert result['accuracy'] == .5 and result['families_with_ties'] == 1
    assert result['both_correct'] == result['same_unique_prediction'] == result['unique_prediction_changes'] == 0
    rows = pair([[0., 0.], [0., 0.]])
    rows[0]['credit'] = 1
    with pytest.raises(ValueError, match='tie credit'): pair_categories(rows)


def test_incomplete_or_inconsistent_context_pairs_rejected():
    rows = pair([[2., 0.], [0., 2.]])
    with pytest.raises(ValueError, match='Complete opposite'): pair_categories(rows[:1])
    for field, value in [('choices', ['no', 'yes']), ('context', 'context0'), ('id', 'f-0')]:
        changed = copy.deepcopy(rows); changed[1][field] = value
        with pytest.raises(ValueError, match='Complete opposite'): pair_categories(changed)
    changed = copy.deepcopy(rows); changed[1]['scores'][0] = float('nan')
    with pytest.raises(ValueError, match='finite'): pair_categories(changed)
