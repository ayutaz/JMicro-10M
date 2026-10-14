"""Architecture/gradient/cache fixtures; not trained Japanese quality evidence."""
import copy
import json
import math
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

from jmicro.cross_gqa_map import (ARMS, TAG, CrossGQAMapModel, cross_map_attention,
                                 native_config, tagged_config)
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state

torch.set_num_threads(2)


def config():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    c.update(num_hidden_layers=2, hidden_size=32, head_dim=8, rotary_dim=8,
        attention_scale=8**-.5, intermediate_size=64, vocab_size=128, qk_norm_type='none')
    with torch.device('meta'):
        model = JMicroModel(c)
    c['expected_parameter_count'] = sum(p.numel() for p in model.parameters())
    return c


def native():
    torch.manual_seed(13)
    return JMicroModel(config()).eval()


def test_independent_attention_matrix_formula_and_signed_coefficients():
    torch.manual_seed(11)
    q, k, v = [torch.randn(2, 4, 6, 8, dtype=torch.float64) for _ in range(3)]
    raw = torch.tensor([-.4, .2, .7, -.8], dtype=torch.float64)
    actual = cross_map_attention(q, k, v, raw, causal=True, scale=.3)
    mask = torch.ones(6, 6, dtype=torch.bool).tril()
    maps = ((q @ k.transpose(-1, -2))*.3).masked_fill(~mask, -torch.inf).softmax(-1)
    expected = torch.empty_like(actual)
    for h in range(4):
        expected[:, h] = (maps[:, h] - raw[h].tanh()*maps[:, (h+2)%4]) @ v[:, h]
    assert torch.allclose(actual, expected, atol=1e-14, rtol=1e-13)


def test_cross_group_on_current_values_is_not_fixed_mixing_of_original_head_outputs():
    # Native heads all emit zero. No fixed linear readout of them can produce
    # nonzero. The other-group map applied to current V does produce nonzero.
    q = torch.zeros(1, 4, 1, 1, dtype=torch.float64)
    k = torch.zeros(1, 4, 2, 1, dtype=torch.float64)
    v = torch.zeros_like(k)
    q[:, 2:] = 1
    k[:, 2:, 0] = math.log(9)/2
    k[:, 2:, 1] = -math.log(9)/2
    v[:, :2, 0] = 1
    v[:, :2, 1] = -1
    standard = F.scaled_dot_product_attention(q, k, v, scale=1.)
    assert torch.count_nonzero(standard) == 0
    raw = torch.tensor([math.atanh(.5), 0, 0, 0], dtype=torch.float64)
    actual = cross_map_attention(q, k, v, raw, scale=1.)
    assert actual[0, 0, 0, 0].item() == pytest.approx(-.4, abs=1e-14)
    assert torch.count_nonzero(actual) == 1


def test_zero_map_coefficient_exact_native_output_and_original_gradients():
    torch.manual_seed(3)
    inputs = [torch.randn(1, 4, 5, 8, dtype=torch.float64, requires_grad=True) for _ in range(3)]
    q, k, v = inputs
    raw = torch.zeros(4, dtype=torch.float64, requires_grad=True)
    original = F.scaled_dot_product_attention(q, k, v, is_causal=True)
    expected_grad = torch.autograd.grad(original.square().sum(), inputs)
    actual = cross_map_attention(q, k, v, raw, causal=True)
    actual.square().sum().backward()
    assert torch.equal(actual, original)
    assert all(torch.equal(x.grad, g) for x, g in zip(inputs, expected_grad))
    assert torch.isfinite(raw.grad).all() and raw.grad.abs().sum() > 0


@pytest.mark.parametrize('arm', ARMS)
def test_conversion_preserves_actual_parent_weights_logits_ties_RNG_count_and_input(arm):
    original = native()
    before = {k:v.clone() for k,v in original.state_dict().items()}
    rng = torch.get_rng_state().clone()
    candidate = CrossGQAMapModel.from_native(original, arm)
    assert torch.equal(rng, torch.get_rng_state())
    assert equal_state(before, original.state_dict())
    assert all(torch.equal(candidate.state_dict()[k], v) for k, v in before.items())
    assert candidate.lm_head.weight is candidate.model.embed_tokens.weight
    assert sum(p.numel() for p in candidate.parameters()) == sum(p.numel() for p in original.parameters())+8
    assert native_config(candidate.config) == original.config
    ids = torch.tensor([[2, 65, 66, 67, 68], [2, 70, 71, 72, 73]])
    assert torch.equal(candidate(ids).logits, original(ids).logits)
    with pytest.raises(ValueError): candidate.hf_reference()
    with pytest.raises(ValueError): candidate.save('unused')
    with pytest.raises(ValueError): candidate.load('unused')


@pytest.mark.parametrize('active', [False, True])
def test_padding_chunk_cache_and_fast_path_preserve_positions_and_causality(active):
    candidate = CrossGQAMapModel.from_native(native())
    if active:
        with torch.no_grad():
            for layer in candidate.model.layers:
                layer.self_attn.cross_raw.copy_(torch.tensor([.4, -.3, .2, -.1]))
    ids = torch.tensor([[2, 65, 66, 67, 68, 69, 70, 71], [2, 75, 76, 77, 78, 79, 0, 0]])
    valid = ids.ne(0)
    full = candidate(ids, attention_mask=valid, use_cache=True)
    first = candidate(ids[:, :4], attention_mask=valid[:, :4], use_cache=True)
    second = candidate(ids[:, 4:], attention_mask=valid[:, 4:], cache=first.cache, use_cache=True)
    assert torch.allclose(full.logits[:, 4:], second.logits, atol=3e-7, rtol=2e-6)
    assert torch.equal(full.cache.valid, second.cache.valid)
    assert torch.equal(full.cache.positions, second.cache.positions)
    assert all(k.shape[1] == v.shape[1] == 2 for k, v in second.cache.layers)
    for (a,b), (c,d) in zip(full.cache.layers, second.cache.layers):
        assert torch.allclose(a, c, atol=3e-7, rtol=2e-6)
        assert torch.allclose(b, d, atol=3e-7, rtol=2e-6)
    changed = ids.clone()
    changed[0, 5:] = torch.tensor([90, 91, 92])
    assert torch.equal(full.logits[0, :5], candidate(changed, attention_mask=valid).logits[0, :5])
    unpadded = ids[:1]
    assert torch.allclose(candidate(unpadded).logits,
                         candidate(unpadded, training_fast_path=True).logits, atol=3e-7, rtol=2e-6)
    sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
    from natural_context_contrast_trainer import right_padded_hidden
    assert torch.allclose(candidate.lm_head(right_padded_hidden(candidate, ids))[valid],
                          full.logits[valid], atol=3e-7, rtol=2e-6)


def test_active_lambda_gets_gradients_without_new_projections_or_teacher_targets():
    candidate = CrossGQAMapModel.from_native(native()).train()
    ids = torch.tensor([[2, 65, 66, 67, 68]])
    loss = F.cross_entropy(candidate(ids).logits[0], torch.tensor([65, 66, 67, 68, 3]))
    loss.backward()
    extra = [(name,p) for name,p in candidate.named_parameters() if name.endswith('.cross_raw')]
    assert len(extra) == 2 and sum(p.numel() for _, p in extra) == 8
    assert all(p.grad is not None and torch.isfinite(p.grad).all() and p.grad.abs().sum() > 0 for _,p in extra)
    assert all(layer.self_attn.q_proj.weight.grad.abs().sum() > 0 for layer in candidate.model.layers)
    # Technical static branch has same tensors/compute but exactly zero lambda gradient.
    static = CrossGQAMapModel.from_native(native(), 'static_zero').train()
    F.cross_entropy(static(ids).logits[0], torch.tensor([65,66,67,68,3])).backward()
    assert all(torch.count_nonzero(layer.self_attn.cross_raw.grad) == 0 for layer in static.model.layers)


@pytest.mark.parametrize('bad', ['policy', 'count', 'arm', 'nativeQK'])
def test_tagged_architecture_contract_rejects_undeclared_changes(bad):
    c = tagged_config(config(), 'cross_learned')
    if bad == 'policy': c[TAG]['policy']['head_mapping'] = [1, 0, 3, 2]
    elif bad == 'count': c['expected_parameter_count'] += 1
    elif bad == 'arm': c[TAG]['arm'] = 'other'
    else: c['qk_norm_type'] = 'rms_head_shared'
    with pytest.raises(ValueError): CrossGQAMapModel(c)


@pytest.mark.parametrize('bad', ['missing', 'nan', 'dtype', 'tie', 'static_nonzero'])
def test_bad_checkpoint_rejected_before_parent_or_model_mutation(bad):
    candidate = CrossGQAMapModel.from_native(native(), 'static_zero' if bad == 'static_nonzero' else 'cross_learned')
    state = {k:v.clone() for k,v in candidate.state_dict().items()}
    if bad == 'missing': del state['model.layers.0.self_attn.cross_raw']
    elif bad == 'nan': state['model.layers.0.self_attn.cross_raw'][0] = torch.nan
    elif bad == 'dtype': state['model.norm.weight'] = state['model.norm.weight'].double()
    elif bad == 'tie': state['lm_head.weight'][0,0] += 1
    else: state['model.layers.0.self_attn.cross_raw'][0] = 1
    before = {k:v.clone() for k,v in candidate.state_dict().items()}
    with pytest.raises(ValueError): candidate.load_state_dict(state)
    assert equal_state(before, candidate.state_dict())


def test_strict_valid_tagged_state_roundtrip():
    first = CrossGQAMapModel.from_native(native())
    with torch.no_grad():
        first.model.layers[0].self_attn.cross_raw[:] = .2
    second = CrossGQAMapModel(copy.deepcopy(first.config))
    second.load_state_dict(first.state_dict())
    assert equal_state(first.state_dict(), second.state_dict())
