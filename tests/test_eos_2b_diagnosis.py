"""Checks for the diagnostic decoder's EOS exemption and scoring behavior."""
from pathlib import Path
import sys

import pytest
import torch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from investigate_eos_2b import penalize


def test_penalty_sign_unique_history_and_untouched_eos():
    scores = torch.tensor([0., 0., 0., 2., 0., 0., 0., 0., 4., -2., 1.])
    actual = penalize(scores, [3, 8, 8, 9], 2)
    assert actual[3] == 2 and actual[8] == 2 and actual[9] == -4 and actual[10] == 1
    assert scores[8] == 4 and scores[9] == -2


def test_plain_greedy_and_natural_eos_selection():
    scores = torch.tensor([0., 0., 0., 2., 0., 0., 0., 0., 4.])
    plain = penalize(scores, [8], 1)
    assert plain.argmax().item() == 8
    assert torch.isneginf(plain[[0, 1, 2, 4, 5, 6]]).all()
    adjusted = penalize(scores, [8], 3)
    assert adjusted.argmax().item() == 3 and adjusted[3] == scores[3]


def test_invalid_penalty_is_rejected():
    with pytest.raises(ValueError):
        penalize(torch.zeros(10), [], .9)
