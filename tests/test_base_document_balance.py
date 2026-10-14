from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from base_document_balance_trainer import (DocumentBalancedTrainer, document_balanced_loss,
    document_losses, committed_state)
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler, document_windows
from natural_context_contrast_trainer import host, right_padded_hidden
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


def builders(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    p = parent()
    def build(weighted=True):
        sampler = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
        return (DocumentBalancedTrainer if weighted else NaturalCorpusTrainer)(p, sampler,
            dict(parent={'sha256': 'fixture'}, weights_role='verification_only'), batch=4, contrast=False, device='cpu')
    return p, build


def test_independent_probability_loss_and_logit_gradient():
    scores = torch.tensor([[2., -.5, .3], [-1., .7, 1.4]], requires_grad=True)
    gold = torch.tensor([0, 2])
    lengths = torch.tensor([4, 10])
    ce, mean_weight, weighted, ratio = document_balanced_loss(scores, gold, lengths)
    values = scores.detach().double()
    exp = (values-values.max(-1, keepdim=True).values).exp()
    probability = exp/exp.sum(-1, keepdim=True)
    weights = torch.tensor([1/4, 1/10], dtype=torch.float64)
    terms = -probability[torch.arange(2), gold].log()
    expected = (terms*weights).sum()/weights.sum()
    assert abs(float(weighted.detach())-float(expected)) < 1e-6
    assert abs(float(ce.detach())-float(terms.mean())) < 1e-6
    assert abs(float(mean_weight)-.175) < 1e-7 and float(ratio) == 2.5
    gradient = probability.clone()
    gradient[torch.arange(2), gold] -= 1
    gradient *= (weights/weights.sum())[:, None]
    assert torch.allclose(torch.autograd.grad(weighted, scores)[0].double(), gradient, atol=1e-7, rtol=1e-6)


def test_equal_lengths_reduce_to_token_CE_and_scale_invariance():
    torch.manual_seed(7)
    logits = torch.randn(7, 13, requires_grad=True)
    gold = torch.arange(7)
    lengths = torch.full((7,), 12)
    result = document_balanced_loss(logits, gold, lengths)
    plain = F.cross_entropy(logits, gold)
    assert torch.allclose(result[2], plain, atol=1e-7)
    assert torch.allclose(torch.autograd.grad(result[2], logits, retain_graph=True)[0],
        torch.autograd.grad(plain, logits)[0], atol=1e-7)
    varied = torch.arange(2, 9)
    assert torch.allclose(document_balanced_loss(logits, gold, varied)[2],
        document_balanced_loss(logits, gold, varied*2)[2], atol=1e-7)


def test_masked_positions_never_projected_or_supervised():
    p = parent()
    model = JMicroModel(p['model_config'])
    ids = torch.tensor([[2, 65, 66, 67], [2, 68, 0, 0]])
    targets = torch.tensor([[-100, 66, 67, 3], [68, 3, -100, -100]])
    lengths = torch.tensor([12, 4])
    result = document_losses(model, ids, targets, lengths)
    logits = model.lm_head(right_padded_hidden(model, ids)).float()
    terms, weights = [], []
    for row, column in targets.ne(-100).nonzero():
        terms.append(-logits[row, column].log_softmax(0)[targets[row, column]])
        weights.append(1/float(lengths[row]))
    w = torch.tensor(weights)
    assert torch.allclose(result[2], (torch.stack(terms)*w).sum()/w.sum(), atol=1e-6)
    with pytest.raises(ValueError): document_losses(model, ids, torch.full_like(targets, -100), lengths)


def test_whole_document_denominator_survives_overlapping_windows():
    body = list(range(8, 28))
    windows = list(document_windows(body, context=8, stride=4))
    gold = [token for row in windows for token in row['target_ids'] if token != -100]
    assert gold == body+[3]
    assert sum(len([v for v in row['target_ids'] if v != -100])/(len(body)+1) for row in windows) == pytest.approx(1.)
    assert gold.count(3) == 1


def test_original_weights_and_same_stream_with_changed_objective(tmp_path):
    p, build = builders(tmp_path)
    t, control = build(), build(False)
    assert equal_state(p['model'], host(t.model.state_dict()))
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    for _ in range(4):
        a, b = t.step(), control.step()
        for key in ('supervised_tokens', 'source_teachers', 'source_EOS', 'CE_input_tokens',
                    'physical_input_tokens', 'original_body_bytes', 'token_digest', 'draw_trace', 'lr'):
            assert equal_state(a[key], b[key]), key
        assert a['balance_positions_this_update'] == a['CE_targets_this_update']
    assert committed_state(t.state_dict())
    assert equal_state(t.sampler.state_dict(), control.sampler.state_dict())
    assert not equal_state(t.model.state_dict(), control.model.state_dict())


def test_continuous_and_saved_resumed_model_Adam_RNG_sampler_and_history(tmp_path):
    _, build = builders(tmp_path)
    continuous = build()
    expected = [continuous.step() for _ in range(4)]
    state = host(continuous.state_dict())
    split = build()
    rows = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = build()
    resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(2))
    assert equal_state(state, host(resumed.state_dict()))
    for a, b in zip(expected, rows, strict=True):
        assert equal_state({k: v for k, v in a.items() if k not in ('seconds', 'data_wait_seconds')},
            {k: v for k, v in b.items() if k not in ('seconds', 'data_wait_seconds')})


@pytest.mark.parametrize('mutation', ['recipe', 'positions', 'optimizer', 'sampler'])
def test_mismatched_or_uncommitted_checkpoint_rejected(tmp_path, mutation):
    _, build = builders(tmp_path)
    t = build()
    t.step()
    state = host(t.state_dict())
    if mutation == 'recipe': state['spec']['document_balance']['denominator'] = 'window_length'
    if mutation == 'positions': state['document_balance']['positions'] += 1
    if mutation == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    if mutation == 'sampler': state['sampler']['consumed']['web'] += 1
    torch.save(state, tmp_path/'bad.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'bad.pt')


def test_interrupted_update_cannot_save_or_continue(tmp_path, monkeypatch):
    _, build = builders(tmp_path)
    t = build()
    import base_document_balance_trainer
    def fail(*args): raise RuntimeError('injected failure')
    monkeypatch.setattr(base_document_balance_trainer, 'document_losses', fail)
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path/'bad.pt')
    with pytest.raises(ValueError): t.step()
