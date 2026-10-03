import hashlib
import json
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from jmicro.experiment import ROOT, read_json
from jmicro.model import JMicroModel
from jmicro.phase5 import bootstrap_bpb, score_body
from jmicro.training import evaluate_body


def tiny_config(norm="rms_head_shared"):
    c = read_json(ROOT/"configs/models/t8k.json")
    c.update(hidden_size=32, num_hidden_layers=1, num_attention_heads=2, num_key_value_heads=1,
             head_dim=16, rotary_dim=16, intermediate_size=48, attention_scale=0.25, qk_norm_type=norm)
    return c


def test_norm_free_has_no_gains_and_cache_still_matches():
    torch.manual_seed(42)
    baseline = JMicroModel(tiny_config())
    torch.manual_seed(42)
    ablation = JMicroModel(tiny_config("none")).eval()
    assert sum(p.numel() for p in baseline.parameters())-sum(p.numel() for p in ablation.parameters()) == 32
    assert not any('q_norm.weight' in name or 'k_norm.weight' in name for name in ablation.state_dict())
    ids = torch.tensor([[2,18,40,9,3]])
    full = ablation(ids).logits
    first = ablation(ids[:,:3], use_cache=True)
    last = ablation(ids[:,3:], cache=first.cache, use_cache=True)
    torch.testing.assert_close(full[:,3:], last.logits, atol=1e-5, rtol=1e-4)
    changed = ids.clone(); changed[0,-1] = 7
    torch.testing.assert_close(full[:,:-1], ablation(changed).logits[:,:-1], atol=0, rtol=0)
    ablation(ids, labels=ids).loss.backward()
    assert all(torch.isfinite(p.grad).all() for p in ablation.parameters())
    with pytest.raises(ValueError, match='adapter'):
        ablation.hf_reference()


def test_batched_scoring_matches_serial_with_padding_long_windows_and_rng():
    torch.manual_seed(42)
    model = JMicroModel(tiny_config()).train()
    ids, index = [], []
    for i, count in enumerate([3,9,17,32]):
        index.append(dict(doc_id=str(i), offset=len(ids), body_tokens=count, bytes=count*3))
        ids.extend([2, *([8+i]*count), 3])
    shard = SimpleNamespace(index=index, tokens=np.asarray(ids), split='dev')
    before = torch.get_rng_state().clone()
    batched = score_body(model, shard, 'cpu', 'fp32', context=16, batch=3)
    serial = evaluate_body(model, shard, 'cpu', 'fp32', context=16)
    assert torch.equal(before, torch.get_rng_state()) and model.training
    assert batched['body_bytes'] == serial['body_bytes'] and batched['documents'] == 4
    assert sum(r['scored'] for r in batched['rows']) == 61
    assert batched['body_nll'] == pytest.approx(serial['body_nll'], rel=1e-6)
    assert batched['eos_nll'] == pytest.approx(serial['eos_nll'], rel=1e-6)


def test_bootstrap_rejects_different_populations():
    body = dict(bpb=1.0, rows=[dict(doc_id='a',body_nll=3.,body_bytes=3), dict(doc_id='b',body_nll=6.,body_bytes=6)])
    result = bootstrap_bpb(body, body)
    assert result['ci95'] == [0.,0.]
    other = dict(body, rows=[dict(body['rows'][0],body_bytes=4),body['rows'][1]])
    with pytest.raises(ValueError, match='bytes'):
        bootstrap_bpb(body, other)
