"""Head attribution must preserve native values, masks, weights and dispatch."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.model import JMicroModel
import base_kv_head_gradient_diagnostic as diagnostic


def fixture_model():
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    c.update(hidden_size=32, num_attention_heads=4, num_key_value_heads=2, head_dim=8,
        rotary_dim=8, num_hidden_layers=2, intermediate_size=40, vocab_size=64, qk_norm_type='none')
    torch.manual_seed(42)
    model = JMicroModel(c).eval()
    ids = torch.tensor([[2, 8, 9, 10, 0], [2, 11, 12, 13, 14]])
    targets = torch.tensor([[8, 9, 10, 3, -100], [-100, -100, 13, 14, 3]])
    return model, ids, targets


def test_exact_native_head_decomposition_preserves_all_state_and_masks():
    model, ids, targets = fixture_model()
    saved = copy.deepcopy(model.state_dict()); rng = torch.get_rng_state().clone()
    with sdpa_kernel(SDPBackend.MATH):
        stats, a, b = diagnostic.decompose(model, ids, targets)
    assert stats['teachers'] == 7 and stats['EOS_teachers'] == 2
    assert stats['logit_max_error'] == 0 and stats['decomposition_relative_error'] < 1e-5
    assert a.shape == b.shape == (64, 32) and len(stats['groups']) == 4
    assert [r['query_heads'] for r in stats['groups']] == [[0, 1], [2, 3]]*2
    assert torch.equal(rng, torch.get_rng_state())
    assert all(torch.equal(saved[k], v) for k, v in model.state_dict().items())
    assert all(p.grad is None for p in model.parameters())
    assert all('forward' not in block.self_attn.__dict__ for block in model.model.layers)


def test_offsets_are_removed_even_when_second_forward_fails(monkeypatch):
    model, ids, targets = fixture_model()
    original = diagnostic.right_padded_hidden
    calls = 0
    def fail_on_split(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError('synthetic attribution failure')
        return original(*args)
    monkeypatch.setattr(diagnostic, 'right_padded_hidden', fail_on_split)
    with pytest.raises(RuntimeError, match='synthetic'):
        diagnostic.decompose(model, ids, targets)
    assert calls == 2
    assert all('forward' not in block.self_attn.__dict__ for block in model.model.layers)
    assert all(p.grad is None for p in model.parameters())


def test_statistics_separate_opposition_from_plain_orthogonal_cancellation():
    a = torch.tensor([[1., 0.]])
    opposed = diagnostic.path_statistics(a, -a)
    orthogonal = diagnostic.path_statistics(a, torch.tensor([[0., 1.]]))
    assert opposed['cosine'] == -1 and opposed['cancellation_ratio'] == 0
    assert orthogonal['cosine'] == 0 and orthogonal['cancellation_ratio'] < .9
    with pytest.raises(ValueError):
        diagnostic.path_statistics(a, torch.zeros_like(a))


def test_predeclared_broad_conflict_screen_requires_two_sources():
    weak = dict(cosine=0., cancellation_ratio=.7)
    strong = dict(cosine=-.2, cancellation_ratio=.7)
    assert not diagnostic.interference_screen(dict(web=strong, textbook=weak, story=weak))['passed']
    row = diagnostic.interference_screen(dict(web=strong, textbook=strong, story=weak))
    assert row['passed'] and not row['causal_proof'] and not row['Base_quality_gate']
    with pytest.raises(ValueError):
        diagnostic.interference_screen(dict(web=strong))


def test_wrong_norm_or_group_count_cannot_be_reinterpreted_as_native_assay():
    model, ids, targets = fixture_model()
    model.config['qk_norm_type'] = 'rms_head_shared'
    with pytest.raises(ValueError, match='NoNorm GQA2'):
        diagnostic.decompose(model, ids, targets)
    model.config['qk_norm_type'] = 'none'
    model.model.layers[0].self_attn.kvheads = 4
    with pytest.raises(ValueError, match='NoNorm GQA2'):
        diagnostic.decompose(model, ids, targets)
