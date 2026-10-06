import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from diagnose_base_transfer_margins import decomposition, validate_rows


def test_context_effect_and_preference_are_distinguished():
    d = decomposition([8., 2.])
    assert d['candidate_preference_component'] == 5
    assert d['aligned_context_component'] == 3
    assert d['same_candidate'] and d['aligned_but_preference_dominates']
    assert not d['both_correct'] and d['credits'] == [1., 0.]
    assert decomposition([3., -2.])['both_correct']
    assert decomposition([-3., 2.])['neither_correct']
    assert decomposition([0., -2.])['any_tie']
    assert not decomposition([0., -2.])['same_candidate']


def test_missing_duplicate_and_changed_raw_targets_are_rejected():
    c = dict(index=0, target_ids=[10, 11], target_bytes=6)
    r = dict(index=0, target_ids=[10, 11], target_tokens=2, target_bytes=6,
             token_nll=[1., 2.], log_likelihood=-3.)
    assert validate_rows([r], [c])[0] == r
    with pytest.raises(ValueError):
        validate_rows([], [c])
    with pytest.raises(ValueError):
        validate_rows([r, r], [c, c])
    with pytest.raises(ValueError):
        validate_rows([{**r, 'target_ids': [10, 12]}], [c])
    with pytest.raises(ValueError):
        validate_rows([{**r, 'log_likelihood': -2.}], [c])
