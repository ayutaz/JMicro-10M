import sys
from pathlib import Path

import pytest
import torch
import torch.nn.functional as F

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from condition_positive_loss import positive_weighted_ce


def test_control_ordinary_ce_and_gradient_identical_with_ignored_targets():
    logits = torch.arange(36, dtype=torch.float64).reshape(1, 3, 12).clone().requires_grad_()
    labels = torch.tensor([[8, 3, -100]])
    mask = torch.tensor([[True, False, True]])
    loss, counts = positive_weighted_ce(logits, labels, mask, 1)
    reference = F.cross_entropy(logits.reshape(-1, 12), labels.reshape(-1),
                                ignore_index=-100, reduction='sum') / 2
    assert torch.equal(loss, reference)
    assert torch.equal(torch.autograd.grad(loss, logits)[0], torch.autograd.grad(reference, logits)[0])
    assert counts['ordinary_teacher_tokens'] == 2
    assert counts['weighted_teacher_mass'] == 2


def test_focus_changes_positive_gradient_all_teachers_and_eos_remain_supervised():
    logits = torch.zeros(1, 3, 12, dtype=torch.float64, requires_grad=True)
    labels = torch.tensor([[8, 9, 3]])
    loss, counts = positive_weighted_ce(logits, labels, torch.tensor([[True, False, False]]), 4)
    gradient = torch.autograd.grad(loss, logits)[0]
    expected = logits.softmax(-1).detach()
    expected[0, torch.arange(3), labels[0]] -= 1
    expected *= torch.tensor([4., 1., 1.], dtype=torch.float64).reshape(1, 3, 1) / 6
    torch.testing.assert_close(gradient, expected, rtol=1e-14, atol=1e-14)
    assert counts['ordinary_teacher_tokens'] == 3
    assert counts['outcome_focus_teacher_tokens'] == 1
    assert counts['weighted_teacher_mass'] == 6
    assert gradient[0, 2, 3] < 0


def test_no_structural_boost_or_empty_learning_objective():
    with pytest.raises(ValueError, match='Structural'):
        positive_weighted_ce(torch.zeros(1, 1, 12), torch.tensor([[3]]), torch.tensor([[True]]), 4)
    with pytest.raises(ValueError, match='ordinary teacher'):
        positive_weighted_ce(torch.zeros(1, 1, 12), torch.tensor([[-100]]), torch.tensor([[False]]), 4)
