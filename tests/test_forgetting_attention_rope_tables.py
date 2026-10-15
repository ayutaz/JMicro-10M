"""Exact original CPU Q/K values and derivatives for shared constant tables."""
import pytest
import torch

from jmicro.forgetting_attention_rope_tables import original_rope_tables, apply_original_rope_tables
from jmicro.model import rope

torch.set_num_threads(2)


@pytest.mark.parametrize('dtype', [torch.float32, torch.bfloat16])
@pytest.mark.parametrize('length', [1, 7, 64, 65, 1024])
def test_shared_QK_original_order_values_and_all_input_gradients_exact(dtype, length):
    generator = torch.Generator().manual_seed(42)
    positions = torch.arange(length)[None].repeat(2, 1)
    positions[1] = positions[1]//3  # Includes repeated/irregular original valid positions.
    q = torch.randn((2, 4, length, 64), generator=generator).to(dtype).requires_grad_()
    k = torch.randn((2, 2, length, 64), generator=generator).to(dtype).requires_grad_()
    before = torch.get_rng_state().clone()
    tables = original_rope_tables(positions, 64, 10000., dtype)
    assert not any(t.requires_grad for t in tables)
    for x in (q, k):
        old = rope(x, positions, 10000.)
        new = apply_original_rope_tables(x, tables)
        assert torch.equal(old, new)
        weight = torch.randn(x.shape, generator=generator).to(dtype)
        a = torch.autograd.grad(new, x, weight, retain_graph=True)[0]
        b = torch.autograd.grad(old, x, weight)[0]
        assert torch.equal(a, b) and torch.isfinite(a).all()
    assert torch.equal(before, torch.get_rng_state()) and not torch.cuda.is_initialized()


def test_shared_tables_under_CPU_autocast_keep_original_BF16_rounding():
    positions = torch.tensor([[0, 0, 1, 2, 2, 3, 7]])
    x = torch.arange(7*64).reshape(1, 1, 7, 64).to(torch.bfloat16)/100
    with torch.autocast('cpu', dtype=torch.bfloat16):
        tables = original_rope_tables(positions, 64, 10000., x.dtype)
        assert torch.equal(apply_original_rope_tables(x, tables), rope(x, positions, 10000.))


def test_wrong_precision_shape_or_learned_tables_refused():
    positions = torch.arange(7)[None]
    with pytest.raises(ValueError): original_rope_tables(positions.float(), 64, 10000., torch.float32)
    with pytest.raises(ValueError): original_rope_tables(positions, 63, 10000., torch.float32)
    with pytest.raises(ValueError): original_rope_tables(positions, 64, 10000., torch.float16)
    x = torch.zeros(1, 4, 7, 64)
    tables = original_rope_tables(positions, 64, 10000., x.dtype)
    with pytest.raises(ValueError): apply_original_rope_tables(x[:, :, :3], tables)
    tables[0].requires_grad_()
    with pytest.raises(ValueError): apply_original_rope_tables(x, tables)
