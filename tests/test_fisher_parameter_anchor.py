"""Exact conditional expectations and real tiny native states; no quality claim."""
import copy
import itertools
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import torch
from jmicro.training import rng_state

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from fisher_parameter_anchor import (sampled_score_loss, normalize_field, validate_field,
    weighted_parameter_penalty, estimate_field, tensor_digest, FisherAnchorTrainer)
from parameter_displacement_anchor_trainer import parameter_penalty
from test_parameter_displacement_anchor import mixed_fixture
from run_eos_short_pilot import equal_state


def test_exhaustive_conditional_expectation_is_token_mean_not_square_of_GT_mean():
    # Two contexts with respectively two and one body positions, same parameter.
    # Independent model labels have zero expected score; cross terms cancel.
    theta = torch.tensor(.7, dtype=torch.float64, requires_grad=True)
    coefficients = torch.tensor([1., 2., -1.], dtype=torch.float64)
    logits = torch.stack([torch.zeros(3, dtype=torch.float64), theta*coefficients], dim=-1)
    probability = logits.detach().softmax(-1)[:, 1]
    exact = 0.
    for draw in itertools.product((0, 1), repeat=3):
        labels = torch.tensor(draw)
        mass = float(torch.where(labels.bool(), probability, 1-probability).prod())
        first = sampled_score_loss(logits[:2], labels[:2], torch.ones(2, dtype=torch.bool), 3)
        last = sampled_score_loss(logits[2:], labels[2:], torch.ones(1, dtype=torch.bool), 3)
        gradients = [torch.autograd.grad(loss, theta, retain_graph=True)[0] for loss in (first, last)]
        exact += mass*sum(float(g.square()) for g in gradients)
    expected = float((coefficients.square()*probability*(1-probability)).sum()/3)
    assert exact == pytest.approx(expected, rel=1e-12)


def test_weighted_objective_matches_uniform_control_and_tied_parameter_gradient():
    module = torch.nn.Module()
    module.a = torch.nn.Linear(2, 2, bias=False)
    module.b = module.a
    with torch.no_grad(): module.a.weight.fill_(2.)
    named = list(module.named_parameters())
    assert len(named) == 1
    anchor = {k: torch.zeros_like(p) for k, p in named}
    uniform = {k: torch.ones_like(p) for k, p in named}
    assert torch.equal(weighted_parameter_penalty(named, anchor, uniform, .5), parameter_penalty(named, anchor, .5))
    raw = {named[0][0]: torch.tensor([[0., 1.], [2., 5.]], dtype=torch.float64)}
    field, stats = normalize_field(named, raw)
    penalty = weighted_parameter_penalty(named, anchor, field, .5)
    penalty.backward()
    assert stats['normalized_coordinate_mean'] == 1
    assert torch.equal(named[0][1].grad, field[named[0][0]])
    assert torch.count_nonzero(anchor[named[0][0]]) == 0
    for bad in (torch.zeros(2, 2), torch.full((2, 2), float('nan')), -torch.ones(2, 2)):
        with pytest.raises(ValueError): validate_field(named, {named[0][0]: bad})
    with pytest.raises(ValueError): validate_field(named+named, uniform)
    with pytest.raises(ValueError): normalize_field(named, {})


def test_estimator_reproducibility_masks_private_RNG_weights_and_parameter_grads():
    class Tiny(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.weight = torch.nn.Parameter(torch.tensor([.2, -.1]))
        def forward(self, x, **_):
            logits = self.weight.expand(*x.shape, 2)
            return SimpleNamespace(logits=logits)
    model = Tiny()
    model.weight.grad = torch.ones_like(model.weight)
    memory = dict(x=torch.tensor([[1, 8, 9], [1, 8, 9]]), y=torch.tensor([[8, 9, 3], [8, 3, 3]]))
    state, rng, gradient = copy.deepcopy(model.state_dict()), rng_state(), model.weight.grad.clone()
    first = estimate_field(model, memory, 123, replicates=2)
    second = estimate_field(model, memory, 123, replicates=2)
    assert first['field_tensor_digest'] == second['field_tensor_digest']
    assert torch.equal(first['sampled_labels'], second['sampled_labels'])
    assert first['accounting'] == dict(score_gradient_calls=4, sampled_score_labels=6,
        physical_context_tokens=12, ordinary_source_CE_teacher_tokens=0, optimizer_updates=0)
    assert equal_state(rng_state(), rng) and equal_state(model.state_dict(), state)
    assert torch.equal(model.weight.grad, gradient) and model.training
    # Actual body support contains only 3 positions, sampled IDs use full p (0/1).
    assert first['sampled_labels'].max() < 2
    assert torch.count_nonzero(first['sampled_labels'][~first['support_mask'].repeat(2, 1)]) == 0


def test_native_weighted_fullstate_resume_binding_and_immutable_anchor_and_field(tmp_path):
    pool, parent, binding, positive = mixed_fixture(tmp_path)
    goals = dict(web=19, story=11, ordinary_textbook=7, conditional_textbook=80)
    from parameter_displacement_anchor_trainer import ParameterAnchorTrainer
    prototype = ParameterAnchorTrainer(parent, pool, pool, positive, goals, binding, .04161064039180984, 'cpu', 8, 3)
    named = list(prototype.model.named_parameters())
    raw = {k: torch.arange(p.numel(), dtype=torch.float64).reshape(p.shape)+1 for k, p in named}
    field, _ = normalize_field(named, raw)
    fb = dict(parent=binding['parent'], field_tensor_digest=tensor_digest(field), artifact_sha256='fixed-fixture')
    def build(f=field, field_binding=fb):
        return FisherAnchorTrainer(parent, pool, pool, positive, goals, binding, .04161064039180984,
                                   f, field_binding, 'cpu', 8, 3)
    whole = build()
    assert equal_state(whole.optimizer.state_dict(), parent['optimizer'])
    assert equal_state(whole.scheduler.state_dict(), parent['scheduler'])
    assert equal_state(whole.model.state_dict(), parent['model'])
    assert equal_state(rng_state(), parent['rng'])
    left = [whole.step() for _ in range(4)]
    whole.save(tmp_path/'whole.pt')
    split = build()
    right = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    split = build()
    split.load(tmp_path/'split.pt')
    right += [split.step() for _ in range(2)]
    split.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'whole.pt', weights_only=False), torch.load(tmp_path/'resumed.pt', weights_only=False))
    for key in ('CE_loss', 'parameter_penalty', 'loss', 'gradient_norm', 'token_digest', 'source_teachers'):
        assert [v[key] for v in left] == [v[key] for v in right]
    assert left[0]['parameter_penalty'] == 0 and left[-1]['parameter_penalty'] > 0
    assert all(r['lr'] == .00001 and r['parameter_penalty_teacher_tokens'] == 0 for r in left)
    changed = build()
    changed.field[next(iter(changed.field))].add_(1)
    with pytest.raises(ValueError, match='field'): changed.save(tmp_path/'bad.pt')
    with pytest.raises(ValueError, match='field'): changed.load(tmp_path/'split.pt')
    changed = build()
    changed.anchor[next(iter(changed.anchor))].add_(1)
    with pytest.raises(ValueError, match='anchor'): changed.save(tmp_path/'bad.pt')
    with pytest.raises(ValueError, match='different parent'): build(field_binding=dict(fb, parent={'wrong': 'parent'}))
    with pytest.raises(ValueError, match='digest'): build(field_binding=dict(fb, field_tensor_digest='wrong'))
    changed = build(field_binding=dict(fb, artifact_sha256='another-fixture'))
    with pytest.raises(ValueError, match='identity'): changed.load(tmp_path/'split.pt')
