"""Actual tagged model/gradient/cache boundaries on CPU, not Japanese quality."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

from jmicro.forgetting_attention import (TAG, ForgettingModel, ForgettingKVCache,
                                         added_parameters, native_config, tagged_config)
from jmicro.model import JMicroModel, KVCache, rope
from jmicro.phase5 import equal_state
from test_value_residual import native, config


def active():
    model = ForgettingModel.from_native(native())
    with torch.no_grad():
        for i, block in enumerate(model.model.layers):
            p = block.self_attn.forget_proj
            p.weight.copy_(torch.linspace(-.2, .3, p.weight.numel()).reshape_as(p.weight))
            p.bias.copy_(torch.linspace(-.4, .5, p.bias.numel()) + .1*i)
    return model


def explicit_model(model, ids):
    """Independent per-(query,key) gate PRODUCT, not a cumulative log bias."""
    batch, length = ids.shape
    positions = torch.arange(length)[None].expand(batch, -1)
    x = model.model.embed_tokens(ids)
    for block in model.model.layers:
        a = block.self_attn
        z = block.input_layernorm(x)
        q = rope(a.q_norm(a.q_proj(z).view(batch, length, 4, 8).transpose(1, 2)), positions, a.theta)
        k = rope(a.k_norm(a.k_proj(z).view(batch, length, 2, 8).transpose(1, 2)), positions, a.theta)
        v = a.v_proj(z).view(batch, length, 2, 8).transpose(1, 2).repeat_interleave(2, 1)
        scores = q @ k.repeat_interleave(2, 1).transpose(-1, -2) * a.scale
        gates = a.forget_proj(z).float().transpose(1, 2).sigmoid()
        queries = []
        for i in range(length):
            parts = []
            for j in range(i+1):
                factor = torch.ones_like(gates[:, :, 0])
                for t in range(j+1, i+1):
                    factor = factor * gates[:, :, t]
                parts.append(factor)
            weights = scores[:, :, i, :i+1].softmax(-1) * torch.stack(parts, -1)
            weights = weights / weights.sum(-1, keepdim=True)
            queries.append((weights[..., None] * v[:, :, :i+1]).sum(2))
        out = torch.stack(queries, 2).transpose(1, 2).reshape(batch, length, 32)
        x = x + a.o_proj(out)
        x = x + block.mlp(block.post_attention_layernorm(x))
    return model.lm_head(model.model.norm(x)).float()


def test_real_architecture_meta_count_and_strict_tag_roundtrip():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    assert added_parameters(c) == 13364
    with torch.device('meta'):
        model = ForgettingModel(tagged_config(c))
    assert sum(p.numel() for p in model.parameters()) == 10014516
    assert sum(p.numel() for p in model.parameters() if p.requires_grad) == 10014516
    assert native_config(model.config) == c
    assert model.lm_head.weight is model.model.embed_tokens.weight
    bad = copy.deepcopy(model.config)
    bad['expected_parameter_count'] += 1
    with pytest.raises(ValueError):
        native_config(bad)
    with pytest.raises(ValueError):
        tagged_config(model.config)


def test_matched_conversion_exact_native_tensors_rng_tie_but_different_native_function():
    original = native()
    rng = torch.get_rng_state().clone()
    a = ForgettingModel.from_native(original)
    b = ForgettingModel.from_native(original, 'static_half_forget')
    assert torch.equal(rng, torch.get_rng_state())
    assert a.lm_head.weight is a.model.embed_tokens.weight
    current = dict(a.named_parameters())
    assert all(torch.equal(p, current[n]) and p.data_ptr() != current[n].data_ptr()
               for n, p in original.named_parameters())
    assert equal_state(a.state_dict(), b.state_dict())
    ids = torch.tensor([[2, 11, 12, 13, 3]])
    assert torch.equal(a(ids).logits, b(ids).logits)
    assert not torch.equal(original(ids).logits, a(ids).logits)


def test_independent_whole_model_product_logits_and_all_parameter_gradients():
    model = active()
    oracle = copy.deepcopy(model)
    ids = torch.tensor([[2, 11, 12, 13, 3], [2, 21, 22, 23, 3]])
    actual, expected = model(ids).logits, explicit_model(oracle, ids)
    torch.testing.assert_close(actual, expected, atol=2e-6, rtol=2e-5)
    F.cross_entropy(actual.flatten(0, 1), ids.flatten()).backward()
    F.cross_entropy(expected.flatten(0, 1), ids.flatten()).backward()
    for (n, p), (on, op) in zip(model.named_parameters(), oracle.named_parameters(), strict=True):
        assert n == on and p.grad is not None and op.grad is not None
        torch.testing.assert_close(p.grad, op.grad, atol=2e-6, rtol=3e-5, msg=n)


@pytest.mark.parametrize('mask', [
    [[1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0]],
    [[0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1]],
    [[0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1]],
    [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1]],
])
def test_active_full_and_real_typed_chunk_cache_with_padding_holes_and_allPAD(mask):
    model = active()
    ids = torch.tensor([[2, 11, 12, 13, 14, 3], [2, 21, 22, 23, 24, 3]])
    valid = torch.tensor(mask, dtype=torch.bool)
    full = model(ids, attention_mask=valid, use_cache=True)
    cache, pieces = None, []
    for start, end in ((0, 2), (2, 3), (3, 6)):
        out = model(ids[:, start:end], attention_mask=valid[:, start:end], cache=cache, use_cache=True)
        pieces.append(out.logits)
        cache = out.cache
    torch.testing.assert_close(torch.cat(pieces, 1), full.logits, atol=3e-6, rtol=2e-5)
    assert type(cache) is ForgettingKVCache
    assert torch.equal(cache.valid, valid)
    assert torch.equal(cache.positions, full.cache.positions)
    assert torch.count_nonzero(full.logits[~valid]) == 0 and torch.isfinite(full.logits).all()
    for logs, want, kv, fullkv in zip(cache.log_gates, full.cache.log_gates, cache.layers, full.cache.layers, strict=True):
        torch.testing.assert_close(logs, want, atol=2e-6, rtol=2e-5)
        assert logs.dtype == torch.float32
        assert torch.count_nonzero(logs.masked_select(~valid[:, None].expand_as(logs))) == 0
        for t, expected in zip(kv, fullkv, strict=True):
            torch.testing.assert_close(t, expected, atol=3e-6, rtol=2e-5)


def test_future_row_and_masked_input_invariance():
    model = active()
    ids = torch.tensor([[2, 11, 12, 13, 14], [2, 21, 22, 23, 24]])
    changed = ids.clone()
    changed[0, 3:] = 100
    changed[1] = 105
    assert torch.equal(model(ids).logits[0, :3], model(changed).logits[0, :3])
    valid = torch.tensor([[1, 0, 1, 0, 1], [0, 1, 0, 1, 0]], dtype=torch.bool)
    changed = ids.clone()
    changed[~valid] = 110
    assert torch.equal(model(ids, attention_mask=valid).logits[valid],
                       model(changed, attention_mask=valid).logits[valid])


def test_real_cache_history_gradients_match_full_forward():
    full, chunked = active(), active()
    ids = torch.tensor([[2, 11, 12, 13, 14, 3]])
    valid = torch.tensor([[1, 0, 1, 1, 0, 1]], dtype=torch.bool)
    a = full(ids, attention_mask=valid).logits[:, 3:]
    prefix = chunked(ids[:, :3], attention_mask=valid[:, :3], use_cache=True)
    b = chunked(ids[:, 3:], attention_mask=valid[:, 3:], cache=prefix.cache).logits
    a.square().sum().backward()
    b.square().sum().backward()
    for (n, p), (other, q) in zip(full.named_parameters(), chunked.named_parameters(), strict=True):
        assert n == other
        torch.testing.assert_close(p.grad, q.grad, atol=3e-6, rtol=4e-5, msg=n)


def test_allPAD_query_rows_have_finite_backward():
    model = active().train()
    ids = torch.tensor([[2, 11, 12], [2, 21, 22]])
    valid = torch.tensor([[0, 0, 0], [0, 1, 1]], dtype=torch.bool)
    result = model(ids, attention_mask=valid)
    assert torch.count_nonzero(result.logits[0]) == 0
    result.logits.square().sum().backward()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())


def test_full_selected_CE_fast_path_native_helper_and_real_gate_gradients():
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
    from natural_context_contrast_trainer import right_padded_hidden
    model = active().train()
    ids = torch.tensor([[2, 11, 12, 13, 3], [2, 21, 22, 3, 0]])
    hidden = model.right_padded_hidden(ids)
    assert torch.equal(hidden, right_padded_hidden(model, ids))
    logits = model.lm_head(hidden).float()
    assert torch.equal(logits, model(ids, training_fast_path=True).logits)
    labels = ids.clone()
    labels[1, -1] = -100
    selected = labels[:, 1:] != -100
    loss = F.cross_entropy(logits[:, :-1][selected], labels[:, 1:][selected])
    torch.testing.assert_close(model(ids, labels=labels).loss, loss, atol=1e-6, rtol=1e-6)
    loss.backward()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() and p.grad.abs().sum() > 0
               for n, p in model.named_parameters() if '.forget_proj.' in n)
    assert torch.isfinite(model.clip_grad_norm(1.))
    next(model.parameters()).grad.fill_(float('inf'))
    with pytest.raises(RuntimeError):
        model.clip_grad_norm(1.)


def test_static_added_coordinates_have_real_zero_gradients_and_do_not_update():
    model = ForgettingModel.from_native(native(), 'static_half_forget').train()
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=.1)
    ids = torch.tensor([[2, 11, 12, 13, 3]])
    old = model.model.layers[0].self_attn.q_proj.weight.detach().clone()
    for _ in range(3):
        optimizer.zero_grad(set_to_none=True)
        model(ids, labels=ids).loss.backward()
        for n, p in model.named_parameters():
            if '.forget_proj.' in n:
                assert p.grad is not None and torch.count_nonzero(p.grad) == 0
        model.clip_grad_norm(1.)
        optimizer.step()
    assert not torch.equal(old, model.model.layers[0].self_attn.q_proj.weight)
    assert all(torch.count_nonzero(p) == 0 for n, p in model.named_parameters() if '.forget_proj.' in n)


def test_cache_rejects_native_wrong_arm_shape_positions_and_nonfinite_history():
    model = active()
    ids = torch.tensor([[2, 11, 12]])
    cache = model(ids, use_cache=True).cache
    bads = [KVCache(cache.layers, cache.valid, cache.positions)]
    for edit in ('arm', 'length', 'positions', 'positive', 'nonfinite', 'precision'):
        bad = ForgettingKVCache(
            [(k.detach().clone(), v.detach().clone()) for k, v in cache.layers],
            cache.valid.clone(), cache.positions.clone(), [x.detach().clone() for x in cache.log_gates], cache.arm)
        if edit == 'arm': bad.arm = 'static_half_forget'
        if edit == 'length': bad.log_gates[0] = bad.log_gates[0][..., :-1]
        if edit == 'positions': bad.positions[0, 0] = 99
        if edit == 'positive': bad.log_gates[0][0, 0, 0] = .1
        if edit == 'nonfinite': bad.log_gates[0][0, 0, 0] = float('nan')
        if edit == 'precision': bad.log_gates[0] = bad.log_gates[0].double()
        bads.append(bad)
    for bad in bads:
        with pytest.raises(ValueError):
            model(ids[:, :1], cache=bad)


def test_strict_state_validation_before_mutation_and_export_refusal(tmp_path):
    model = active()
    state = copy.deepcopy(model.state_dict())
    for edit in ('missing', 'nan', 'tie', 'shape'):
        bad = copy.deepcopy(state)
        if edit == 'missing': del bad['model.layers.0.self_attn.forget_proj.bias']
        if edit == 'nan': bad['model.layers.0.self_attn.forget_proj.bias'][0] = float('nan')
        if edit == 'tie': bad['lm_head.weight'] = bad['lm_head.weight'].clone() + 1
        if edit == 'shape': bad['model.layers.0.self_attn.forget_proj.bias'] = torch.zeros(5)
        with pytest.raises(ValueError): model.load_state_dict(bad)
        assert equal_state(model.state_dict(), state)
    static = ForgettingModel.from_native(native(), 'static_half_forget')
    with pytest.raises(ValueError): static.load_state_dict(state)
    with pytest.raises(ValueError): model.load_state_dict(state, strict=False)
    model.load_state_dict(state)
    with pytest.raises(ValueError): model.save(tmp_path)
    with pytest.raises(ValueError): model.hf_reference()
    with pytest.raises(ValueError): ForgettingModel.load(tmp_path)
