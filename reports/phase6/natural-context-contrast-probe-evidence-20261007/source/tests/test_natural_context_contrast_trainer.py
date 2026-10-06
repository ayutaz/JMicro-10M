"""Protocol fixtures; these are not native GPU learning/quality evidence."""
import hashlib
import json
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from natural_context_contrast_trainer import (FixedPairSampler, NaturalContextTrainer,
    host, right_pad, right_padded_hidden, symmetric_InfoNCE)
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state

torch.set_num_threads(2)


def fixture():
    config = json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config.update(num_hidden_layers=2, hidden_size=32, head_dim=8, rotary_dim=8,
                  attention_scale=8**-0.5, intermediate_size=64,
                  vocab_size=100, qk_norm_type='none')
    torch.manual_seed(3)
    model = JMicroModel(config)
    parent = dict(model_config=config, model=host(model.state_dict()), update=5, tokens=90,
                  supervised_tokens=80)
    rows = []
    for i in range(4):
        body = [10+i, 20+i, 30+i, 40+i, 50+i][:3+i%3]
        rows.append(dict(index=i, source_family=f'family-{i}',
            full_original_body_sha256=hashlib.sha256(bytes(body)).hexdigest(),
            full_body_ids=body, prefix_ids=body[:2], suffix_ids=body[2:], body_UTF8_bytes=len(body)*3))
    return model, parent, rows


def test_right_padding_matches_masked_native_valid_logits_without_aux_head():
    model, _, _ = fixture()
    ids, lengths = right_pad([[2, 8, 9, 10], [2, 11]], 'cpu')
    valid = torch.arange(ids.shape[1])[None] < lengths[:, None]
    reference = model(ids, valid).logits
    calls = []
    hook = model.lm_head.register_forward_hook(lambda *args: calls.append(1))
    hidden = right_padded_hidden(model, ids)
    assert calls == []
    hook.remove()
    actual = model.lm_head(hidden)
    torch.testing.assert_close(actual[valid], reference[valid], rtol=1e-5, atol=1e-6)


def test_InfoNCE_observed_pairing_and_two_sided_gradient():
    left = torch.eye(4, requires_grad=True)
    right = (torch.eye(4)+0.1).requires_grad_()
    loss, stats = symmetric_InfoNCE(left, right)
    permuted, _ = symmetric_InfoNCE(left, right.flip(0))
    assert loss < permuted
    assert stats['positive_cosine'] > stats['distractor_cosine']
    assert stats['representation_variance'] > 0
    loss.backward()
    assert left.grad.norm() > 0 and right.grad.norm() > 0


@pytest.mark.parametrize('contrast', [False, True])
def test_full_state_resume_and_full_body_EOS_accounting(tmp_path, contrast):
    _, parent, rows = fixture()
    binding = dict(parent={'sha256': 'fixture-parent'}, sample_sha256='fixture-original-TRAIN')
    def build():
        return NaturalContextTrainer(parent, rows, binding, batch=2, contrast=contrast, device='cpu')
    continuous = build()
    history = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = build()
    actual = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = build()
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(2))
    assert equal_state(expected, host(resumed.state_dict()))
    assert all(equal_state({k: v for k, v in a.items() if k != 'seconds'},
                           {k: v for k, v in b.items() if k != 'seconds'})
               for a, b in zip(history, actual, strict=True))
    assert expected['counters']['supervised_tokens'] == sum(
        len(rows[i]['full_body_ids'])+1 for step in history for i in step['draw_indices'])
    assert expected['counters']['auxiliary_pairs'] == (8 if contrast else 0)
    assert expected['counters']['CE_input_tokens'] == expected['counters']['supervised_tokens']


def test_duplicate_family_cannot_be_a_retrieval_negative():
    _, _, rows = fixture()
    rows[1]['source_family'] = rows[0]['source_family']
    with pytest.raises(ValueError, match='Distinct original families'):
        FixedPairSampler(rows)
