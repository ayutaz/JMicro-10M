"""Independent product/gradient and physical-prefix checks, no model/data/GPU."""
import pytest
import torch

from jmicro.forgetting_attention_math import forgetting_bias


def explicit_product_attention(g, valid, scores, values, query_start=0):
    result = []
    for b in range(g.shape[0]):
        heads = []
        for h in range(g.shape[1]):
            queries = []
            for i in range(query_start, g.shape[-1]):
                if not valid[b, i]:
                    queries.append(torch.zeros_like(values[b, h, 0]))
                    continue
                weights, candidates = [], []
                for j in range(i + 1):
                    if not valid[b, j]:
                        continue
                    decay = g.new_ones(())
                    for k in range(j + 1, i + 1):
                        if valid[b, k]:
                            decay = decay * torch.sigmoid(g[b, h, k])
                    weights.append(scores[b, h, i, j].exp() * decay)
                    candidates.append(values[b, h, j])
                weights = torch.stack(weights)
                queries.append((weights[:, None] * torch.stack(candidates)).sum(0) / weights.sum())
            heads.append(torch.stack(queries))
        result.append(torch.stack(heads))
    return torch.stack(result)


def parallel(g, valid, scores, values, query_start=0):
    bias = forgetting_bias(g, valid, query_start)
    # All-invalid queries are made safe only for this algebra fixture.
    active = valid[:, None, query_start:, None]
    logits = torch.where(active, scores[:, :, query_start:] + bias, 0.)
    return (logits.softmax(-1) @ values) * active


@pytest.mark.parametrize('mask', [
    [[1, 1, 1, 1], [1, 1, 1, 1]],
    [[0, 1, 0, 1], [1, 1, 0, 0]],
    [[0, 0, 0, 0], [0, 0, 1, 0]],
])
def test_product_values_and_all_derivatives(mask):
    gen = torch.Generator().manual_seed(71)
    valid = torch.tensor(mask, dtype=torch.bool)
    tensors = [torch.randn(shape, generator=gen, dtype=torch.float64, requires_grad=True)
               for shape in ((2, 2, 4), (2, 2, 4, 4), (2, 2, 4, 3))]
    g, scores, values = tensors
    actual = parallel(g, valid, scores, values)
    expected = explicit_product_attention(g, valid, scores, values)
    torch.testing.assert_close(actual, expected, atol=1e-12, rtol=1e-12)
    a = torch.autograd.grad(actual.square().sum(), tensors)
    # With just one valid key, the product oracle never uses a gate at all.
    # Its mathematically zero derivative must still be compared explicitly.
    e = torch.autograd.grad(expected.square().sum(), tensors,
                            allow_unused=True, materialize_grads=True)
    for got, want in zip(a, e):
        torch.testing.assert_close(got, want, atol=1e-11, rtol=1e-11)


def test_cached_suffix_values_and_gradients_with_holes():
    g = torch.linspace(-3, 3, 16, dtype=torch.float64).reshape(2, 2, 4).requires_grad_()
    valid = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 1]], dtype=torch.bool)
    full = forgetting_bias(g, valid)
    joined = torch.cat((g[..., :2], g[..., 2:]), dim=-1)
    cached = forgetting_bias(joined, torch.cat((valid[:, :2], valid[:, 2:]), dim=-1), 2)
    torch.testing.assert_close(cached, full[:, :, 2:], atol=0, rtol=0)
    finite = torch.isfinite(cached)
    left = torch.autograd.grad(cached[finite].sum(), g, retain_graph=True)[0]
    right = torch.autograd.grad(full[:, :, 2:][finite].sum(), g)[0]
    torch.testing.assert_close(left, right, atol=0, rtol=0)


def test_causality_diagonal_and_padding_invariance():
    valid = torch.tensor([[1, 0, 1, 1]], dtype=torch.bool)
    g = torch.tensor([[[0., 9., -1., 2.]]], requires_grad=True)
    bias = forgetting_bias(g, valid)
    assert bias[0, 0, 2, 2] == 0 and bias[0, 0, 0, 0] == 0
    assert torch.isneginf(bias[0, 0, 0, 2])
    derivative = torch.autograd.grad(bias[0, 0, 2, 0], g)[0]
    assert derivative[0, 0, 1] == 0 and derivative[0, 0, 3] == 0
    changed = g.detach().clone()
    changed[..., 1] = -100.
    torch.testing.assert_close(forgetting_bias(changed, valid), bias, atol=0, rtol=0)


def test_not_post_output_gate_and_row_isolation():
    # Equal scores and V=[-1,1] give zero before an output scalar gate.
    # Decaying the earlier key instead gives a nonzero normalized output.
    g = torch.zeros(2, 1, 2)
    valid = torch.ones(2, 2, dtype=torch.bool)
    values = torch.tensor([[[[-1.], [1.]]], [[[-1.], [1.]]]])
    scores = torch.zeros(2, 1, 2, 2)
    result = parallel(g, valid, scores, values)
    assert result[0, 0, 1, 0] > .3
    ordinary = scores[0, 0, 1].softmax(-1) @ values[0, 0]
    assert ordinary.item() == 0
    g[1] = 20.
    torch.testing.assert_close(parallel(g, valid, scores, values)[0], result[0], atol=0, rtol=0)


def test_malformed_inputs_rejected():
    g = torch.zeros(1, 2, 3)
    valid = torch.ones(1, 3, dtype=torch.bool)
    for bad_g, bad_valid, start in (
        (g, valid.float(), 0), (g, valid[:, :2], 0),
        (g, valid, -1), (g, valid, 3), (g, valid, True),
        (g.long(), valid, 0), (g[..., :0], valid[:, :0], 0),
        (g + float('nan'), valid, 0), (g + float('inf'), valid, 0),
    ):
        with pytest.raises(ValueError):
            forgetting_bias(bad_g, bad_valid, start)
