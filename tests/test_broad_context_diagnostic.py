"""Common-target alignment and genuine isolation, not model-quality fixtures."""
import copy
import json
import sys

import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT
from jmicro.model import JMicroModel

sys.path.insert(0, str(ROOT / 'scripts'))
import run_broad_context_diagnostic as study


def case():
    body = list(range(8, 28))
    return dict(id='train-1', split='train', source='web', body_ids=body,
        prefix_ids=[2, *body[:10]], gold_ids=[*body[10:], 3],
        previous_context_ids=[2, 31, 32, 3], prefix_text='prefix', gold_text='gold')


def test_common_target_reconstruction_and_budget():
    study.validate_case(case())
    for key, value in [('split', 'dev'), ('previous_context_ids', []),
                       ('previous_context_ids', [8] * 960), ('gold_ids', [19, 3]),
                       ('source', 'heldout')]:
        with pytest.raises(ValueError):
            study.validate_case(dict(case(), **{key: value}))


def test_body_loss_excludes_EOS_and_different_prefix_lengths():
    torch.manual_seed(123)
    gold = [9, 12, 3]
    logits = torch.randn(3, 32)
    actual = study.score_targets(logits, gold)
    expected = torch.nn.functional.cross_entropy(logits[:2], torch.tensor(gold[:2]))
    assert actual['body_nll_mean'] == pytest.approx(float(expected))
    assert actual['body_tokens'] == 2
    assert actual['EOS_rank'] == int((logits[-1] > logits[-1, 3]).sum()) + 1
    with pytest.raises(ValueError):
        study.score_targets(logits[:2], gold)
    bad = logits.clone(); bad[0, 0] = float('nan')
    with pytest.raises(ValueError, match='Nonfinite'):
        study.score_targets(bad, gold)


def test_extract_uses_complete_doc_and_preserves_original_context():
    body = list(range(8, 28)); ids = [31, 3, 2, *body, 3, 2]
    x = np.array([ids[:-1]]); y = np.array([ids[1:]]); y[y == 2] = -100
    tags = np.zeros_like(y, dtype=np.uint8)
    class Tok:
        def decode(self, ids): return ''.join(chr(0x4e00 + i) for i in ids)
    location = lambda start: dict(document_index=1, body_tokens=20, block_number=0,
        original_train_offset=2, batch_number=0)
    remaining = dict(web=1, story=0, textbook=0)
    selected, _ = study.extract_cases(x, y, tags, [location], Tok(), remaining, set())
    assert len(selected) == 1
    assert selected[0]['previous_context_ids'] == [31, 3]
    assert selected[0]['body_ids'] == body and selected[0]['gold_ids'][-1] == 3
    assert remaining['web'] == 0


def test_both_contexts_score_same_targets_and_leave_weights_gradients_unchanged():
    config = json.loads((ROOT / 'configs/models/t4k.json').read_text())
    config.update(num_hidden_layers=2, vocab_size=300)
    model = JMicroModel(config).eval()
    before = {k: v.clone() for k, v in model.state_dict().items()}
    class Tok:
        def decode_bytes(self, ids): return bytes(i % 128 for i in ids if i >= 8)
    calls = []
    packed = study.evaluate_case(model, Tok(), case(), 'packed', 'cpu', lambda: calls.append(True))
    single = study.evaluate_case(model, Tok(), case(), 'standalone', 'cpu', lambda: calls.append(True))
    assert packed['scored']['target_ids'] == single['scored']['target_ids'] == case()['gold_ids']
    assert packed['prefix_ids'] == case()['previous_context_ids'] + case()['prefix_ids']
    assert single['prefix_ids'] == case()['prefix_ids']
    # Independently feed the actual first gold prediction without suffix tokens.
    with torch.inference_mode():
        first = model(torch.tensor([packed['prefix_ids']])).logits[0, -1]
    first_nll = -first.log_softmax(-1)[case()['gold_ids'][0]]
    assert packed['scored']['first_target_nll'] == pytest.approx(float(first_nll), abs=1e-5)
    assert all(torch.equal(before[k], v) for k, v in model.state_dict().items())
    assert all(p.grad is None for p in model.parameters()) and calls


def test_summary_refuses_missing_duplicate_or_changed_common_targets():
    cases = [case()]; rows = []
    for arm in ('oneB', 'twoB'):
        for context in ('packed', 'standalone'):
            rows.append(dict(id='train-1', checkpoint=arm, context=context,
                scored=dict(target_ids=case()['gold_ids'], body_tokens=10,
                    body_nll_sum=10 if context == 'packed' else 12,
                    body_nll_mean=1 if context == 'packed' else 1.2, EOS_top1=True),
                EOS=True, repetition=False, valid_utf8=True, role_leak=False, empty=False))
    marker = dict(min_mean_body_nll_advantage_nats=.1, min_fraction_positive=.6)
    summary = study.summarize(rows, cases, marker)
    assert summary['twoB']['local_context_dependence_marker']
    for bad in (rows[:-1], rows + rows[:1]):
        with pytest.raises(ValueError, match='Incomplete or duplicate'):
            study.summarize(bad, cases, marker)
    bad = copy.deepcopy(rows); bad[1]['scored']['target_ids'] = [31, 3]
    with pytest.raises(ValueError, match='different targets'):
        study.summarize(bad, cases, marker)
