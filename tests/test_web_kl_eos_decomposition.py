import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from web_kl_eos_decomposition import decompose


def test_chain_rule_and_EOS_gradient_on_body_only_targets():
    generator = torch.Generator().manual_seed(42)
    parent = torch.randn(1, 5, 11, generator=generator, dtype=torch.float64)
    student = torch.randn(1, 5, 11, generator=generator, dtype=torch.float64, requires_grad=True)
    labels = torch.tensor([[8, 3, 9, -100, 10]])
    values = decompose(parent, student, labels)
    assert len(values['full_KL']) == 3
    assert torch.allclose(values['full_KL'], values['EOS_mass_KL'] + values['weighted_conditional_non_EOS_KL'], atol=1e-12)
    values['full_KL'].sum().backward()
    assert torch.allclose(student.grad[labels >= 8, 3], values['EOS_logit_KL_derivative'], atol=1e-12)
    assert student.grad[labels < 8].eq(0).all()
    assert values['EOS_logit_KL_derivative'].abs().max() > 0
    with pytest.raises(ValueError):
        decompose(parent, student, torch.full_like(labels, 3))


def test_changed_EOS_mass_with_identical_conditional_vocabulary_is_separable():
    p = torch.full((1, 1, 11), .09, dtype=torch.float64); p[..., 3] = .1
    q = torch.full((1, 1, 11), .06, dtype=torch.float64); q[..., 3] = .4
    result = decompose(p.log(), q.log(), torch.tensor([[8]]))
    assert result['weighted_conditional_non_EOS_KL'].abs().max() < 1e-12
    assert result['full_KL'].item() == pytest.approx(result['EOS_mass_KL'].item())
    assert result['EOS_logit_KL_derivative'].item() == pytest.approx(.3)
