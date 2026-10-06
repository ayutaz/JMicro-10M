import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from hard_body_web_replay import body_gold_ce
from eos_decoupled_web_kl_preservation import body_parent_kl


def test_actual_gold_targets_mask_parent_detach_and_direct_EOS_gradient():
    g = torch.Generator().manual_seed(42)
    parent = torch.randn(2, 4, 11, generator=g, requires_grad=True)
    student = torch.randn(2, 4, 11, generator=g, requires_grad=True)
    labels = torch.tensor([[8, 3, 9, -100], [2, 10, 8, 7]])
    loss, counts = body_gold_ce(student, parent, labels)
    # Explicit scalar probability formula, using original gold IDs, not a teacher argmax.
    values = []
    for i in range(2):
        for j in range(4):
            gold = int(labels[i, j])
            if gold >= 8:
                probs = student[i, j, [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]].softmax(-1)
                weight = 1 - parent[i, j].softmax(-1)[3]
                values.append(weight * -probs[gold-1].log())
    assert loss.item() == pytest.approx(torch.stack(values).mean().item(), abs=1e-6)
    _, prior = body_parent_kl(student, parent, labels)
    assert counts['non_EOS_teacher_probability_mass'] == prior['non_EOS_teacher_probability_mass']
    assert counts['hard_body_teacher_tokens'] == 4
    assert counts['ignored_special_positions'] == 4
    assert counts['physical_reference_input_tokens'] == 8
    assert counts['new_main_ordinary_CE_teacher_tokens'] == 0
    loss.backward()
    assert parent.grad is None
    assert student.grad[..., 3].eq(0).all()
    assert student.grad[labels < 8].eq(0).all()
    assert student.grad[..., 8:].abs().sum() > 0
    with pytest.raises(ValueError):
        body_gold_ce(student, parent, torch.full_like(labels, 3))
    with pytest.raises(ValueError):
        body_gold_ce(student, parent, torch.full_like(labels, 11))


def test_gold_targets_do_not_copy_parent_distribution_and_EOS_only_change_is_invariant():
    parent = torch.zeros(1, 2, 11)
    parent[..., 8] = 4
    student = parent.clone()
    labels = torch.full((1, 2), 10)
    same, _ = body_gold_ce(student, parent, labels)
    assert same.item() > 0  # Same weights still incur actual gold CE, unlike KL.
    right_labels = torch.full_like(labels, 8)
    right, _ = body_gold_ce(student, parent, right_labels)
    assert right.item() < same.item()
    changed = student.clone()
    changed[..., 3] += 100
    after, _ = body_gold_ce(changed, parent, labels)
    assert same.item() == after.item()
    # Control the weight exactly in FP32 while changing teacher argmax 8 -> 9.
    # A generic permutation changes reduction rounding and is not bitwise invariant.
    teacher = torch.full_like(parent, -100.)
    teacher[..., 8] = 100.
    permuted = torch.full_like(parent, -100.)
    permuted[..., 9] = 100.
    first, first_counts = body_gold_ce(student, teacher, labels)
    other, other_counts = body_gold_ce(student, permuted, labels)
    assert first_counts['non_EOS_teacher_probability_mass'] == 2.
    assert other_counts['non_EOS_teacher_probability_mass'] == 2.
    assert other.item() == first.item()
