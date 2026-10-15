"""Independent mathematical oracle and real-only cached quiet model proof."""
import copy
import json
import math
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

from jmicro.model import JMicroModel, rope
from jmicro.phase5 import equal_state
from jmicro.quiet_attention import (ARMS, TAG, QuietCache, QuietModel,
    native_config, quiet_attention, tagged_config)
from test_value_residual import native


def dense(q, k, v, mask, scale):
    # Compute null probability via logaddexp rather than the production SDPA
    # concatenation; include null score0 in the maximum for numerical stability.
    scores = ((q @ k.transpose(-1, -2))*scale).masked_fill(~mask, -torch.inf)
    log_z = torch.logaddexp(torch.zeros_like(scores[..., 0]), torch.logsumexp(scores, -1))
    return torch.exp(scores-log_z[..., None]) @ v


@pytest.mark.parametrize('causal', [True, False])
def test_dense_independent_value_and_ALL_QKV_gradients(causal):
    torch.manual_seed(9)
    q, k, v = [torch.randn(2, 4, 7, 8, dtype=torch.float64, requires_grad=True) for _ in range(3)]
    mask = torch.ones(2, 1, 7, 7, dtype=torch.bool).tril() if causal else torch.rand(2, 1, 7, 7) > .4
    actual = quiet_attention(q, k, v, causal=causal, mask=None if causal else mask, scale=.3)
    expected = dense(q, k, v, mask, .3)
    torch.testing.assert_close(actual, expected, atol=2e-14, rtol=2e-13)
    weight = torch.linspace(-1, 2, actual.numel(), dtype=torch.float64).reshape_as(actual)
    a = torch.autograd.grad((actual*weight).sum(), (q, k, v), retain_graph=True)
    b = torch.autograd.grad((expected*weight).sum(), (q, k, v))
    for x, y in zip(a, b, strict=True):
        torch.testing.assert_close(x, y, atol=2e-13, rtol=2e-12)


def test_absolute_real_logit_shift_changes_quiet_not_native_or_query_only_gate():
    q = torch.ones(1, 1, 1, 1, dtype=torch.float64)
    k = torch.zeros(1, 1, 2, 1, dtype=torch.float64)
    v = torch.full_like(k, 3.)
    native_a = F.scaled_dot_product_attention(q, k, v, scale=1.)
    native_b = F.scaled_dot_product_attention(q, k+math.log(2), v, scale=1.)
    assert torch.equal(native_a, native_b)
    # Same query, values and native normalized map/output; mass differs solely
    # because every real score competes against a fixed external zero logit.
    a = quiet_attention(q, k, v, scale=1.)
    b = quiet_attention(q, k+math.log(2), v, scale=1.)
    torch.testing.assert_close(a, torch.full_like(a, 2.), atol=1e-14, rtol=0)
    torch.testing.assert_close(b, torch.full_like(b, 2.4), atol=1e-14, rtol=0)


@pytest.mark.parametrize('score', [-1000., -100., 0., 100., 1000.])
def test_large_absolute_logits_stable_and_zero_option_negative_limit(score):
    q = torch.ones(1, 1, 1, 1, dtype=torch.float64)
    k = torch.full((1, 1, 2, 1), score, dtype=torch.float64)
    v = torch.full_like(k, 3.)
    actual = quiet_attention(q, k, v, scale=1.)
    expected = 3.*torch.sigmoid(torch.tensor(score+math.log(2), dtype=torch.float64))
    torch.testing.assert_close(actual, expected.expand_as(actual), atol=1e-14, rtol=1e-12)
    assert torch.isfinite(actual).all()


def test_single_real_token_causal_alignment_not_null_only():
    q, k = torch.zeros(1, 1, 1, 1), torch.zeros(1, 1, 1, 1)
    v = torch.full_like(k, 4.)
    assert torch.equal(quiet_attention(q, k, v, causal=True), torch.full_like(q, 2.))


def test_all_real_masked_returns_zero_finite_ALL_gradients():
    q, k, v = [torch.randn(2, 4, 3, 8, requires_grad=True) for _ in range(3)]
    mask = torch.zeros(2, 1, 3, 3, dtype=torch.bool)
    out = quiet_attention(q, k, v, mask=mask)
    assert torch.count_nonzero(out) == 0
    out.sum().backward()
    assert all(t.grad is not None and torch.isfinite(t.grad).all() and not torch.count_nonzero(t.grad) for t in (q, k, v))


@pytest.mark.parametrize('arm', ARMS)
def test_conversion_original_tensors_parameter_names_count_tie_RNG(arm):
    original = native()
    before = copy.deepcopy(original.state_dict())
    rng = torch.get_rng_state().clone()
    model = QuietModel.from_native(original, arm)
    assert torch.equal(rng, torch.get_rng_state()) and not torch.cuda.is_initialized()
    assert equal_state(original.state_dict(), before)
    assert all(torch.equal(model.state_dict()[k], v) for k, v in before.items())
    assert [n for n, _ in model.named_parameters()] == [n for n, _ in original.named_parameters()]
    assert sum(p.numel() for p in model.parameters()) == sum(p.numel() for p in original.parameters())
    assert model.lm_head.weight is model.model.embed_tokens.weight
    assert native_config(model.config) == original.config
    ids = torch.tensor([[2, 11, 12, 13, 3]])
    if arm == 'disabled_native':
        assert torch.equal(original(ids).logits, model(ids).logits)
        assert torch.equal(original(ids, training_fast_path=True).logits, model(ids, training_fast_path=True).logits)
    else:
        assert not torch.equal(original(ids).logits, model(ids).logits)
        torch.testing.assert_close(model(ids).logits, model(ids, training_fast_path=True).logits, atol=2e-6, rtol=2e-5)


def test_actual_meta_count_stays_native10001152():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/phase6/base_10b.json').read_text())['model_config']
    with torch.device('meta'):
        model = QuietModel(tagged_config(c))
    assert sum(p.numel() for p in model.parameters()) == 10001152
    assert sum(p.numel() for p in model.parameters() if p.requires_grad) == 10001152
    assert native_config(model.config) == c


@pytest.mark.parametrize('mask', [
    [[1,1,1,1,1,1],[1,1,1,0,0,0]],
    [[0,0,1,1,1,1],[1,0,1,0,1,1]],
    [[0,0,0,0,0,0],[0,1,0,1,0,1]],
])
def test_cache_full_chunks_tokens_holes_allPAD_real_history_and_no_recompute(mask):
    model = QuietModel.from_native(native())
    ids = torch.tensor([[2,11,12,13,14,3],[2,21,22,23,24,3]])
    valid = torch.tensor(mask, dtype=torch.bool)
    full = model(ids, attention_mask=valid, use_cache=True)
    prefix = model(ids[:, :3], attention_mask=valid[:, :3], use_cache=True)
    observed = []
    h = model.model.embed_tokens.register_forward_pre_hook(lambda _, args: observed.append(args[0].shape[1]))
    try:
        suffix = model(ids[:, 3:], attention_mask=valid[:, 3:], cache=prefix.cache, use_cache=True)
    finally:
        h.remove()
    assert observed == [3]
    torch.testing.assert_close(torch.cat((prefix.logits, suffix.logits), 1), full.logits, atol=3e-6, rtol=2e-5)
    pieces, cache = [], None
    for i in range(6):
        out = model(ids[:, i:i+1], attention_mask=valid[:, i:i+1], cache=cache, use_cache=True)
        pieces.append(out.logits)
        cache = out.cache
    torch.testing.assert_close(torch.cat(pieces, 1), full.logits, atol=3e-6, rtol=2e-5)
    assert type(cache) is QuietCache and not hasattr(cache, 'layers')
    assert torch.equal(cache.valid, valid) and torch.equal(cache.positions, full.cache.positions)
    for pair, expected in zip(cache.real, full.cache.real, strict=True):
        assert pair[0].shape[2] == pair[1].shape[2] == 6
        for x, y in zip(pair, expected, strict=True):
            torch.testing.assert_close(x, y, atol=3e-6, rtol=2e-5)
    assert torch.isfinite(full.logits).all() and not torch.count_nonzero(full.logits[~valid])


def test_whole_model_independent_dense_reference_ALL_parameter_gradients():
    model = QuietModel.from_native(native())
    oracle = copy.deepcopy(model)
    ids = torch.tensor([[2,11,12,13,3]])
    batch, length = ids.shape
    positions = torch.arange(length)[None]
    mask = torch.ones(length, length, dtype=torch.bool).tril()
    x = oracle.model.embed_tokens(ids)
    for block in oracle.model.layers:
        a, z = block.self_attn, block.input_layernorm(x)
        project = lambda m, h: m(z).view(batch, length, h, 8).transpose(1, 2)
        q, k = [rope(project(m, h), positions, a.theta) for m, h in ((a.q_proj,4),(a.k_proj,2))]
        v = project(a.v_proj, 2).repeat_interleave(2, 1)
        value = dense(q, k.repeat_interleave(2, 1), v, mask, a.scale)
        x = x+a.o_proj(value.transpose(1,2).reshape(batch,length,32))
        x = x+block.mlp(block.post_attention_layernorm(x))
    expected = oracle.lm_head(oracle.model.norm(x)).float()
    actual = model(ids).logits
    torch.testing.assert_close(actual, expected, atol=2e-6, rtol=2e-5)
    actual.square().sum().backward()
    expected.square().sum().backward()
    for (n,p),(other,q) in zip(model.named_parameters(), oracle.named_parameters(), strict=True):
        assert n == other and p.grad is not None and torch.isfinite(p.grad).all()
        torch.testing.assert_close(p.grad, q.grad, atol=3e-6, rtol=4e-5, msg=n)


def test_cache_ALL_parameter_history_gradients_match_full_with_allPAD():
    full = QuietModel.from_native(native())
    chunked = copy.deepcopy(full)
    ids = torch.tensor([[2,11,12,13,14,3],[2,21,22,23,24,3]])
    valid = torch.tensor([[1,0,1,1,0,1],[0,0,0,0,0,0]], dtype=torch.bool)
    a = full(ids, attention_mask=valid).logits[:,3:]
    prefix = chunked(ids[:,:3], attention_mask=valid[:,:3], use_cache=True)
    b = chunked(ids[:,3:], attention_mask=valid[:,3:], cache=prefix.cache).logits
    a.square().sum().backward()
    b.square().sum().backward()
    for (n,p),(other,q) in zip(full.named_parameters(), chunked.named_parameters(), strict=True):
        assert n == other and torch.isfinite(p.grad).all()
        torch.testing.assert_close(p.grad, q.grad, atol=3e-6, rtol=4e-5, msg=n)


def test_shifted_gold_loss_and_all_masked_labels_refusal():
    model = QuietModel.from_native(native())
    ids = torch.tensor([[2,11,12,3]])
    labels = ids.clone()
    labels[:,1] = -100
    out = model(ids, labels=labels)
    expected = F.cross_entropy(out.logits[:,:-1].reshape(-1,128), labels[:,1:].reshape(-1), ignore_index=-100)
    assert torch.equal(out.loss, expected)
    with pytest.raises(ValueError):
        model(ids, labels=torch.full_like(ids,-100))
    with pytest.raises(ValueError):
        model(ids[:,:1], cache=model(ids,use_cache=True).cache, labels=ids[:,:1])


@pytest.mark.parametrize('bad', ['native','arm','runtime','shape','nan','positions'])
def test_foreign_corrupt_cache_refusal_before_model_mutation(bad):
    model = QuietModel.from_native(native())
    ids = torch.tensor([[2,11,12]])
    cache = model(ids,use_cache=True).cache
    if bad == 'native': cache = native()(ids,use_cache=True).cache
    elif bad == 'arm': cache.arm = 'disabled_native'
    elif bad == 'runtime': cache.implementation = 'wrong'
    elif bad == 'shape': cache.real[0] = (cache.real[0][0][:,:,:1], cache.real[0][1])
    elif bad == 'nan': cache.real[0][0][0,0,0,0] = torch.nan
    else: cache.positions[0,0] = 99
    before = copy.deepcopy(model.state_dict())
    with pytest.raises(ValueError): model(ids[:,:1],cache=cache)
    assert equal_state(before,model.state_dict())


@pytest.mark.parametrize('bad', ['native','arm','nan','tie','count','policy'])
def test_strict_state_configuration_no_partial_mutation(bad):
    model = QuietModel.from_native(native())
    before = copy.deepcopy(model.state_dict())
    state = copy.deepcopy(before)
    if bad in ('count','policy'):
        c = copy.deepcopy(model.config)
        if bad == 'count': c['expected_parameter_count'] += 1
        else: c[TAG]['policy']['phantom_logit'] = 1.
        with pytest.raises(ValueError): QuietModel(c)
    else:
        if bad == 'native': del state['quiet_runtime']
        elif bad == 'arm': state['quiet_runtime'][1] = 1
        elif bad == 'nan': state['model.norm.weight'][0] = torch.nan
        else: state['lm_head.weight'] = state['lm_head.weight'].clone()+1
        with pytest.raises(ValueError): model.load_state_dict(state)
    assert equal_state(before,model.state_dict())
    model.load_state_dict(before)
    assert equal_state(before,model.state_dict())


def test_native_helpers_export_cache_context_and_fast_arguments_refused():
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
    from natural_context_contrast_trainer import right_padded_hidden
    model = QuietModel.from_native(native())
    ids = torch.tensor([[2,11,12,3]])
    with pytest.raises(ValueError,match='model-owned'): right_padded_hidden(model,ids)
    with pytest.raises(AttributeError): native()(ids[:,:1],cache=model(ids,use_cache=True).cache)
    with pytest.raises(ValueError): model.hf_reference()
    with pytest.raises(ValueError): model.save('unused')
    with pytest.raises(ValueError): QuietModel.load('unused')
    with pytest.raises(ValueError): model(ids,attention_mask=torch.ones_like(ids),training_fast_path=True)
    with pytest.raises(ValueError): model(torch.ones(1,1025,dtype=torch.long),training_fast_path=True)


@pytest.mark.parametrize('bad', ['causal_rectangle','causal_mask','float_mask','wrong_shape','dtype'])
def test_attention_rejects_invalid_contract(bad):
    q,k,v = [torch.ones(1,4,3,8) for _ in range(3)]
    kw = {}
    if bad == 'causal_rectangle': q=q[:,:,:1]; kw['causal']=True
    elif bad == 'causal_mask': kw=dict(causal=True,mask=torch.ones(1,1,3,3,dtype=torch.bool))
    elif bad == 'float_mask': kw['mask']=torch.ones(1,1,3,3)
    elif bad == 'wrong_shape': kw['mask']=torch.ones(1,1,3,2,dtype=torch.bool)
    else: k=k.double(); v=v.double()
    with pytest.raises(ValueError): quiet_attention(q,k,v,**kw)
