"""New typed model boundary and unchanged canonical CPU inference evidence."""
import copy
import json
from pathlib import Path

import pytest
import torch

from jmicro.forgetting_attention_shared_rope import (
    SharedRopeForgettingModel as Model, SharedRopeKVCache, IMPLEMENTATION,
    TAG, RUNTIME_KEY, native_config, tagged_config,
)
from jmicro.forgetting_attention_canonical import CanonicalForgettingModel as Reference
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_forgetting_attention_canonical import original


@pytest.mark.parametrize('arm', ['learned_forget', 'static_half_forget'])
def test_conversion_original_tensors_rng_tie_count_and_initial_function_exact_to_canonical(arm):
    parent = original()
    before = torch.get_rng_state().clone()
    a, b = Model.from_native(parent, arm), Reference.from_native(parent, arm)
    assert torch.equal(before, torch.get_rng_state())
    assert equal_state(a.state_dict(), b.state_dict())
    assert list(dict(a.named_parameters())) == list(dict(b.named_parameters()))
    assert a.lm_head.weight is a.model.embed_tokens.weight
    assert not list(a.named_buffers())
    assert native_config(a.config) == parent.config
    ids = torch.tensor([[2, 11, 12, 13, 3]])
    assert torch.equal(a(ids).logits, b(ids).logits)
    assert torch.equal(a(ids, training_fast_path=True).logits, b(ids, training_fast_path=True).logits)


def active_pair():
    parent = original()
    a, b = Model.from_native(parent), Reference.from_native(parent)
    with torch.no_grad():
        for i, block in enumerate(a.model.layers):
            gate = block.self_attn.forget_proj
            gate.weight.copy_(torch.linspace(-.2, .3, gate.weight.numel()).reshape_as(gate.weight))
            gate.bias.fill_(.1*i)
    b.load_state_dict(a.state_dict())
    return a, b


@pytest.mark.parametrize('split', [1, 32, 63, 64, 65])
def test_active_inference_exact_to_canonical_with_real_cache_no_table_state(split):
    a, b = active_pair()
    ids = torch.arange(69)[None].repeat(2, 1)%110+2
    valid = torch.ones_like(ids, dtype=torch.bool)
    valid[0, ::5] = False
    valid[1] = False
    full = a(ids, attention_mask=valid, use_cache=True)
    expected = b(ids, attention_mask=valid, use_cache=True)
    assert torch.equal(full.logits, expected.logits)
    prefix = a(ids[:, :split], attention_mask=valid[:, :split], use_cache=True)
    suffix = a(ids[:, split:], attention_mask=valid[:, split:], cache=prefix.cache, use_cache=True)
    assert type(suffix.cache) is SharedRopeKVCache
    torch.testing.assert_close(torch.cat((prefix.logits, suffix.logits), 1), full.logits, atol=3e-5, rtol=2e-5)
    assert set(vars(suffix.cache)) == {'layers', 'valid', 'positions', 'log_gates', 'arm', 'implementation'}
    assert all(k.shape[2] == v.shape[2] == 69 for k, v in suffix.cache.layers)
    assert torch.equal(suffix.cache.positions, full.cache.positions)
    assert torch.equal(suffix.cache.valid, valid)
    assert not list(a.named_buffers())


def test_actual_architecture_count_and_markers():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    with torch.device('meta'):
        model = Model(tagged_config(c))
    assert sum(p.numel() for p in model.parameters()) == 10014516
    assert native_config(model.config) == c
    assert model.config[RUNTIME_KEY] == IMPLEMENTATION
    for marker in (None, 'wrong'):
        bad = copy.deepcopy(model.config)
        if marker is None: del bad[RUNTIME_KEY]
        else: bad[RUNTIME_KEY] = marker
        with pytest.raises(ValueError): Model(bad)


def test_old_cache_refused_both_directions_and_native_traversal_cannot_bypass_shared_runtime():
    a, b = active_pair()
    ids = torch.tensor([[2, 11, 12]])
    new, old = a(ids, use_cache=True), b(ids, use_cache=True)
    with pytest.raises(ValueError): a(ids[:, :1], cache=old.cache)
    with pytest.raises(ValueError): b(ids[:, :1], cache=new.cache)
    new.cache.implementation = 'wrong'
    with pytest.raises(ValueError): a(ids[:, :1], cache=new.cache)
    attention = a.model.layers[0].self_attn
    with pytest.raises(ValueError): attention.shared_full_prefix(torch.zeros(1, 3, 32), torch.arange(3)[None], ())
    with pytest.raises(ValueError): attention(torch.zeros(1, 3, 32), torch.arange(3)[None], None, None)


def test_active_CPU_all_parameter_gradients_and_three_Adam_updates_exact_to_canonical():
    a, b = active_pair()
    optimizers = [torch.optim.AdamW(m.parameters(), lr=1e-5, weight_decay=.1) for m in (a, b)]
    ids = torch.tensor([[2, 11, 12, 13, 3]])
    for _ in range(3):
        for m, opt in zip((a, b), optimizers, strict=True):
            opt.zero_grad(set_to_none=True)
            m(ids, labels=ids).loss.backward()
        for (n, p), (other, q) in zip(a.named_parameters(), b.named_parameters(), strict=True):
            assert n == other and p.grad is not None and torch.equal(p.grad, q.grad)
        for m, opt in zip((a, b), optimizers, strict=True):
            m.clip_grad_norm(1.)
            opt.step()
        assert equal_state(a.state_dict(), b.state_dict())
        assert equal_state(optimizers[0].state_dict(), optimizers[1].state_dict())
