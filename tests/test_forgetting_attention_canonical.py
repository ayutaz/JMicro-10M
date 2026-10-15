"""Independent arithmetic and real incremental cache checks; CPU evidence only."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

from jmicro.forgetting_attention_canonical import (
    BLOCK, IMPLEMENTATION, RUNTIME_KEY, TAG, CanonicalForgettingModel as Model,
    CanonicalKVCache, added_parameters, canonical_attention, native_config,
    packed_pointwise, tagged_config,
)
from jmicro.forgetting_attention_fused import FusedForgettingModel
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_value_residual import config
from test_forgetting_attention_fused import explicit_model


def original():
    torch.manual_seed(13)
    c = config()
    c['max_position_embeddings'] = 128
    return JMicroModel(c).eval()


def active(arm='learned_forget'):
    model = Model.from_native(original(), arm)
    if arm == 'learned_forget':
        with torch.no_grad():
            for i, block in enumerate(model.model.layers):
                p = block.self_attn.forget_proj
                p.weight.copy_(torch.linspace(-.2, .3, p.weight.numel()).reshape_as(p.weight))
                p.bias.copy_(torch.linspace(-.4, .5, p.bias.numel())+.1*i)
    return model


@pytest.mark.parametrize('shape', [(5, 7), (2, 1, 7), (2, 64, 7), (2, 65, 7), (1, 131, 7)])
def test_packed_pointwise_values_and_all_derivatives_against_direct_linear(shape):
    torch.manual_seed(9)
    x = torch.randn(shape, dtype=torch.float64, requires_grad=True)
    w = torch.randn(11, 7, dtype=torch.float64, requires_grad=True)
    b = torch.randn(11, dtype=torch.float64, requires_grad=True)
    observed = []
    def operation(work):
        observed.append(tuple(work.shape))
        return F.linear(work, w, b).tanh()
    actual = packed_pointwise(x, operation)
    expected = F.linear(x, w, b).tanh()
    torch.testing.assert_close(actual, expected, atol=1e-14, rtol=1e-14)
    weights = torch.linspace(-1., 2., actual.numel(), dtype=torch.float64).reshape_as(actual)
    a = torch.autograd.grad((actual*weights).sum(), (x, w, b), retain_graph=True)
    e = torch.autograd.grad((expected*weights).sum(), (x, w, b))
    for got, want in zip(a, e, strict=True):
        torch.testing.assert_close(got, want, atol=1e-12, rtol=1e-12)
    assert all(s == (shape[0] if len(shape) == 3 else 1, BLOCK, 7) for s in observed)


def test_pack_rejects_wrong_rank_empty_nonfloat_or_nonpointwise_output():
    for x in (torch.zeros(3), torch.zeros(2, 0, 3), torch.ones(2, 3, dtype=torch.long)):
        with pytest.raises(ValueError): packed_pointwise(x, lambda z: z)
    with pytest.raises(ValueError): packed_pointwise(torch.ones(2, 3), lambda z: z.sum(1))


def test_attention_against_independent_gate_product_values_and_QKV_gate_derivatives():
    torch.manual_seed(10)
    q, k, v = [torch.randn(2, 4, 7, 8, requires_grad=True) for _ in range(3)]
    gate = torch.randn(2, 4, 7, requires_grad=True)
    valid = torch.tensor([[1, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0]], dtype=torch.bool)
    allowed = valid[:, :, None] & valid[:, None, :] & torch.ones(7, 7, dtype=torch.bool).tril()
    logs = torch.where(valid[:, None], F.logsigmoid(gate), 0.)
    actual = canonical_attention(q, k, v, logs, allowed, 128, 8**-.5)
    scores = q @ k.transpose(-1, -2) * 8**-.5
    # An independent PRODUCT of the real intervening gates (no log cumsum).
    rows = []
    for i in range(7):
        factors = []
        for j in range(i+1):
            factor = torch.ones(2, 4)
            for t in range(j+1, i+1):
                factor = factor*torch.where(valid[:, t, None], gate[:, :, t].sigmoid(), 1.)
            factors.append(factor)
        weights = scores[:, :, i, :i+1].softmax(-1)*torch.stack(factors, -1)
        weights = weights*allowed[:, None, i, :i+1]
        denominator = weights.sum(-1, keepdim=True)
        weights = weights/torch.where(denominator > 0, denominator, 1.)
        rows.append((weights[..., None]*v[:, :, :i+1]).sum(2))
    expected = torch.stack(rows, 2)
    torch.testing.assert_close(actual, expected, atol=2e-6, rtol=2e-5)
    weight = torch.linspace(-1, 2, actual.numel()).reshape_as(actual)
    a = torch.autograd.grad((actual*weight).sum(), (q, k, v, gate), retain_graph=True)
    e = torch.autograd.grad((expected*weight).sum(), (q, k, v, gate))
    for got, want in zip(a, e, strict=True):
        assert torch.isfinite(got).all()
        torch.testing.assert_close(got, want, atol=2e-6, rtol=3e-5)


def test_whole_model_against_independent_product_logits_and_all_parameter_gradients():
    model = active()
    oracle = copy.deepcopy(model)
    ids = torch.tensor([[2, 11, 12, 13, 3], [2, 21, 22, 23, 3]])
    actual, expected = model(ids).logits, explicit_model(oracle, ids)
    torch.testing.assert_close(actual, expected, atol=2e-6, rtol=2e-5)
    F.cross_entropy(actual.flatten(0, 1), ids.flatten()).backward()
    F.cross_entropy(expected.flatten(0, 1), ids.flatten()).backward()
    for (name, p), (other, op) in zip(model.named_parameters(), oracle.named_parameters(), strict=True):
        assert name == other and p.grad is not None and op.grad is not None
        torch.testing.assert_close(p.grad, op.grad, atol=2e-6, rtol=3e-5, msg=name)


@pytest.mark.parametrize('arm', ['learned_forget', 'static_half_forget'])
@pytest.mark.parametrize('split', [1, 32, 63, 64, 65])
def test_real_cache_across_workspace_boundary_no_past_decoder_recomputation(arm, split):
    model = active(arm)
    ids = (torch.arange(69)[None].repeat(2, 1)%110)+2
    valid = torch.ones_like(ids, dtype=torch.bool)
    valid[0, ::5] = False
    valid[1] = False
    full = model(ids, attention_mask=valid, use_cache=True)
    prefix = model(ids[:, :split], attention_mask=valid[:, :split], use_cache=True)
    current_lengths = []
    handle = model.model.embed_tokens.register_forward_pre_hook(
        lambda module, args: current_lengths.append(args[0].shape[1]))
    try:
        suffix = model(ids[:, split:], attention_mask=valid[:, split:], cache=prefix.cache, use_cache=True)
    finally:
        handle.remove()
    assert current_lengths == [69-split], 'Past token decoder states must never be recomputed'
    torch.testing.assert_close(torch.cat((prefix.logits, suffix.logits), 1), full.logits, atol=3e-5, rtol=2e-5)
    assert type(suffix.cache) is CanonicalKVCache
    assert torch.equal(suffix.cache.valid, valid)
    assert torch.equal(suffix.cache.positions, full.cache.positions)
    assert torch.isfinite(suffix.logits).all() and torch.count_nonzero(suffix.logits[1]) == 0
    for row, logs, want in zip(suffix.cache.layers, suffix.cache.log_gates, full.cache.log_gates, strict=True):
        assert row[0].shape[2] == row[1].shape[2] == logs.shape[2] == 69
        assert logs.dtype == torch.float32
        torch.testing.assert_close(logs, want, atol=3e-5, rtol=2e-5)
        assert torch.count_nonzero(logs.masked_select(~valid[:, None].expand_as(logs))) == 0


def test_real_cache_gradients_and_allPAD_backward_finite():
    full, chunked = active(), active()
    ids = torch.tensor([[2, 11, 12, 13, 14, 3], [2, 21, 22, 23, 24, 3]])
    valid = torch.tensor([[1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0]], dtype=torch.bool)
    a = full(ids, attention_mask=valid).logits[:, 3:]
    prefix = chunked(ids[:, :3], attention_mask=valid[:, :3], use_cache=True)
    b = chunked(ids[:, 3:], attention_mask=valid[:, 3:], cache=prefix.cache).logits
    a.square().sum().backward()
    b.square().sum().backward()
    for (name, p), (other, q) in zip(full.named_parameters(), chunked.named_parameters(), strict=True):
        assert name == other and p.grad is not None and torch.isfinite(p.grad).all()
        torch.testing.assert_close(p.grad, q.grad, atol=3e-6, rtol=4e-5, msg=name)


def test_selected_CE_model_owned_traversal_and_native_helper_refused():
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
    from natural_context_contrast_trainer import right_padded_hidden
    model = active().train()
    ids = torch.tensor([[2, 11, 12, 13, 3], [2, 21, 22, 3, 0]])
    hidden = model.right_padded_hidden(ids)
    torch.testing.assert_close(model.lm_head(hidden), model(ids, training_fast_path=True).logits,
                               atol=0, rtol=0)
    selected = ids != 0
    loss = F.cross_entropy(model.lm_head(hidden[selected]), ids[selected])
    loss.backward()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())
    assert any(torch.count_nonzero(p.grad) for n, p in model.named_parameters() if '.forget_proj.' in n)
    with pytest.raises(ValueError, match='model-owned'): right_padded_hidden(model, ids)


def test_future_and_masked_rows_invariance():
    model = active()
    ids = torch.tensor([[2, 11, 12, 13, 14]])
    changed = ids.clone()
    changed[:, 3:] = 100
    assert torch.equal(model(ids).logits[:, :3], model(changed).logits[:, :3])
    valid = torch.tensor([[1, 0, 1, 0, 1]], dtype=torch.bool)
    changed = ids.clone()
    changed[~valid] = 110
    assert torch.equal(model(ids, attention_mask=valid).logits[valid],
                       model(changed, attention_mask=valid).logits[valid])


def test_exact_real_architecture_count_tie_rng_conversion_and_runtime_roundtrip():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    assert added_parameters(c) == 13364
    with torch.device('meta'): real = Model(tagged_config(c))
    assert sum(p.numel() for p in real.parameters()) == 10014516
    assert native_config(real.config) == c and real.lm_head.weight is real.model.embed_tokens.weight
    original_model = original()
    rng = torch.get_rng_state().clone()
    a, b = [Model.from_native(original_model, arm) for arm in ('learned_forget', 'static_half_forget')]
    assert torch.equal(rng, torch.get_rng_state())
    assert equal_state(a.state_dict(), b.state_dict())
    params = dict(a.named_parameters())
    for n, p in original_model.named_parameters():
        assert torch.equal(p, params[n]) and p.data_ptr() != params[n].data_ptr()
    ids = torch.tensor([[2, 11, 12, 3]])
    assert torch.equal(a(ids).logits, b(ids).logits)
    assert not torch.equal(a(ids).logits, original_model(ids).logits)


def test_old_cache_and_marker_refused_both_directions_and_strict_state_before_mutation(tmp_path):
    model, old = active(), FusedForgettingModel.from_native(original())
    ids = torch.tensor([[2, 11, 12]])
    a, b = model(ids, use_cache=True), old(ids, use_cache=True)
    with pytest.raises(ValueError): model(ids[:, :1], cache=b.cache)
    with pytest.raises(ValueError): old(ids[:, :1], cache=a.cache)
    a.cache.implementation = 'wrong'
    with pytest.raises(ValueError): model(ids[:, :1], cache=a.cache)
    for marker in (None, 'wrong'):
        c = copy.deepcopy(model.config)
        if marker is None: del c[RUNTIME_KEY]
        else: c[RUNTIME_KEY] = marker
        with pytest.raises(ValueError): Model(c)
    state = copy.deepcopy(model.state_dict())
    for edit in ('missing', 'nan', 'tie', 'shape'):
        bad = copy.deepcopy(state)
        key = 'model.layers.0.self_attn.forget_proj.bias'
        if edit == 'missing': del bad[key]
        if edit == 'nan': bad[key][0] = float('nan')
        if edit == 'tie': bad['lm_head.weight'] = bad['lm_head.weight'].clone()+1
        if edit == 'shape': bad[key] = torch.zeros(5)
        with pytest.raises(ValueError): model.load_state_dict(bad)
        assert equal_state(model.state_dict(), state)
    with pytest.raises(ValueError): model.save(tmp_path)
    with pytest.raises(ValueError): model.hf_reference()
    with pytest.raises(ValueError): Model.load(tmp_path)
    with pytest.raises(ValueError): model.load_state_dict(state, strict=False)
    assert model.config[RUNTIME_KEY] == IMPLEMENTATION
