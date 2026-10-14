"""CPU output equivalence to legacy semantics using synthetic inputs only."""
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest
import torch

from jmicro.continuation_requests import requests
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.isolated_continuations import generate_isolated_continuations, raw_record, sample_token
from jmicro.training import rng_state
from jmicro.phase5 import equal_state
from test_continuation_requests import fixture


class Codec:
    vocab_size = 16
    def encode(self, text): return [8 + len(text) % 3]
    def decode_bytes(self, ids):
        if 1 in ids: raise ValueError('UNK')
        return b''.join(b'a' if i == 8 else b'\xc3' if i == 9 else b'b' if i >= 8 else b'' for i in ids)


class Model:
    config = dict(max_position_embeddings=1024)
    training = False
    calls = 0
    def eval(self): self.training = False; return self
    def train(self, mode=True): self.training = mode; return self
    def __call__(self, current, cache=None, use_cache=True):
        self.calls += 1
        logits = torch.full((1, current.shape[1], 16), -2.)
        logits[:, :, 1] = 1.5
        logits[:, :, 7] = 1.1
        logits[:, :, 8] = 1.2
        logits[:, :, 9] = .8
        logits[:, :, 3] = .2
        return SimpleNamespace(logits=logits, cache=0)


def test_actual_CPU_adapter_matches_legacy400_and_long40_on_fixture(tmp_path, monkeypatch):
    import jmicro.training as legacy
    from jmicro.japanese_evaluation import NativeLikelihood
    mp, pin, cases = fixture(tmp_path)
    old_eval = tmp_path / 'eval'
    old_eval.mkdir()
    old = old_eval / 'base.jsonl'
    # A fake TEST row makes the legacy file mixed; no actual TEST is opened.
    old.write_text(''.join(json.dumps(r) + '\n' for r in cases + [dict(cases[0], id='fake-test', split='test')]))
    monkeypatch.setattr(legacy, 'ROOT', tmp_path)
    with patch.object(torch, 'is_inference_mode_enabled', wraps=torch.is_inference_mode_enabled):
        expected = legacy.generate_suite(Model(), Codec(), 'cpu', 'fp32', sampling=True)
    allowed = {mp, tmp_path / 'base.dev.jsonl'}
    original_open = Path.open
    def guarded(p, *a, **k):
        assert p in allowed, 'Mixed/TEST reader called'
        return original_open(p, *a, **k)
    before = rng_state()
    with patch.object(Path, 'open', guarded):
        result = generate_isolated_continuations(Model(), Codec(), mp, pin, lambda: None, lambda *a: None, device='cpu')
    assert equal_state(before, rng_state())
    for left, right in zip(result['standard']['outputs'], expected['outputs']):
        assert all(left[k] == value for k, value in right.items())
    assert len(result['standard']['outputs']) == 400 and len(result['long']['rows']) == 40
    for row in result['long']['rows']:
        baseline = NativeLikelihood(Model(), Codec(), device='cpu').generate(row['prefix'], row['max_new_tokens'])
        assert all(row[k] == value for k, value in baseline.items())
    assert any(row['role_leak'] for row in result['standard']['outputs'])
    assert any(not row['valid_utf8'] for row in result['standard']['outputs'])
    assert result['content_review_completed'] is False and result['Base_qualified'] is False


def test_unknown_UTF8_and_role_failures_preserve_raw_IDs(tmp_path):
    mp, pin, _ = fixture(tmp_path)
    request = requests(load_dev_suite(mp, pin))[1]
    row = raw_record(request, [8, 1, 7, 3], Codec())
    assert row['generated_ids'] == [8, 1, 7, 3] and not row['valid_utf8']
    assert row['unknown_id_present'] and row['role_leak'] and row['raw_utf8_hex'] == ''
    row = raw_record(request, [9, 3], Codec())
    assert not row['valid_utf8'] and row['raw_utf8_hex'] == 'c3'


def test_training_model_and_context_overflow_rejected_before_forward(tmp_path):
    mp, pin, _ = fixture(tmp_path)
    model = Model()
    model.train()
    with pytest.raises(ValueError):
        generate_isolated_continuations(model, Codec(), mp, pin, lambda: None, lambda *a: None, device='cpu')
    assert model.calls == 0
    model.eval()
    class Oversize(Codec):
        def encode(self, text): return [8] * 512
    with pytest.raises(ValueError):
        generate_isolated_continuations(model, Oversize(), mp, pin, lambda: None, lambda *a: None, device='cpu')
    assert model.calls == 0


def test_expired_budget_and_nonfinite_logits_do_not_claim_complete(tmp_path):
    mp, pin, _ = fixture(tmp_path)
    def expire(): raise TimeoutError('fixture')
    with pytest.raises(TimeoutError):
        generate_isolated_continuations(Model(), Codec(), mp, pin, expire, lambda *a: None, device='cpu')
    class Bad(Model):
        def __call__(self, *a, **k):
            result = super().__call__(*a, **k)
            result.logits[0, 0, 0] = float('nan')
            return result
    with pytest.raises(ValueError, match='Nonfinite'):
        generate_isolated_continuations(Bad(), Codec(), mp, pin, lambda: None, lambda *a: None, device='cpu')
