"""Output probability/link/state checks; fixtures do not establish Japanese quality."""
import copy
from pathlib import Path
import sys
import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from base_sigsoftmax_model import LINK, SigSoftmaxModel, install_sigsoftmax, sigsoftmax_logits
from base_sigsoftmax_trainer import SigSoftmaxTrainer, committed_state
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.training import rng_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


def builders(tmp_path):
    pool = tmp_path / 'pool'
    digest = fixture_pool(pool)
    p = parent()
    def build(control=False):
        sampler = OriginalTrainCorpusSampler(pool, digest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
        args = (p, sampler, dict(parent={'sha256': 'fixture'}, weights_role='verification_only'))
        cls = NaturalCorpusTrainer if control else SigSoftmaxTrainer
        return cls(*args, batch=4, contrast=False, device='cpu')
    return p, build


def test_independent_probability_NLL_and_analytical_gradient():
    z = torch.tensor([[-2., -.2, 1.], [2., .3, -1.]], requires_grad=True)
    targets = torch.tensor([2, 0])
    raw = z.detach().double()
    unnormalized = raw.exp() / (1 + (-raw).exp())
    p = unnormalized / unnormalized.sum(-1, keepdim=True)
    scores = sigsoftmax_logits(z)
    assert torch.allclose(F.softmax(scores, -1).double(), p, atol=1e-7)
    loss = F.cross_entropy(scores, targets)
    expected = -p[torch.arange(2), targets].log().mean()
    assert float(loss.detach()) == pytest.approx(float(expected), abs=1e-7)
    loss.backward()
    gradient = (p - F.one_hot(targets, 3)) * (1 + torch.sigmoid(-raw)) / 2
    assert torch.allclose(z.grad.double(), gradient, atol=1e-7)


def test_extreme_logits_finite_gradient_and_FP32_link():
    raw = torch.tensor([[-10000., -100., 0., 100., 10000.]], requires_grad=True)
    loss = F.cross_entropy(sigsoftmax_logits(raw), torch.tensor([0]))
    loss.backward()
    assert torch.isfinite(loss) and torch.isfinite(raw.grad).all()
    assert torch.isfinite(sigsoftmax_logits(raw.detach())).all()
    assert sigsoftmax_logits(raw.detach().bfloat16()).dtype == torch.float32


def test_monotonic_greedy_but_not_common_shift_invariant():
    z = torch.tensor([[-3., -.2, .7, 2.], [0., -4., 4., 1.]])
    assert torch.equal(z.argsort(-1), sigsoftmax_logits(z).argsort(-1))
    assert not torch.allclose(F.softmax(sigsoftmax_logits(z), -1), F.softmax(sigsoftmax_logits(z + 3), -1))


def test_head_parameter_keys_optimizer_and_rng_unchanged(tmp_path):
    p, build = builders(tmp_path)
    t, control = build(), build(True)
    assert equal_state(p['model'], host(t.model.state_dict()))
    assert equal_state(host(t.state_dict())['RNG'], host(control.state_dict())['RNG'])
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    assert sum(v.numel() for v in t.model.parameters()) == sum(v.numel() for v in control.model.parameters())
    assert {id(v) for v in t.model.parameters()} == {id(v) for g in t.optimizer.param_groups for v in g['params']}
    before = rng_state()
    model = control.model
    count = sum(v.numel() for v in model.parameters())
    install_sigsoftmax(model)
    assert equal_state(before, rng_state()) and count == sum(v.numel() for v in model.parameters())
    with pytest.raises(ValueError): install_sigsoftmax(model)


def test_full_padded_fast_and_cache_use_link_exactly_once():
    raw = JMicroModel(parent()['model_config']).eval()
    linked = JMicroModel(raw.config).eval()
    linked.load_state_dict(raw.state_dict())
    install_sigsoftmax(linked)
    ids = torch.tensor([[2, 65, 66, 67], [2, 68, 69, 70]])
    expected = sigsoftmax_logits(raw(ids).logits)
    assert torch.allclose(linked(ids).logits, expected, atol=1e-6)
    assert torch.allclose(linked(ids, training_fast_path=True).logits, expected, atol=1e-6)
    first = linked(ids[:, :2], use_cache=True)
    last = linked(ids[:, 2:], cache=first.cache, use_cache=True)
    assert torch.allclose(torch.cat([first.logits, last.logits], 1), expected, atol=1e-6)
    padded = torch.tensor([[2, 65, 0, 0], [2, 68, 69, 70]])
    mask = padded.ne(0)
    assert torch.allclose(linked(padded, attention_mask=mask).logits[0, :2], linked(padded[:1, :2]).logits[0], atol=1e-6)
    loaded = SigSoftmaxModel(linked.config).eval()
    loaded.load_state_dict(linked.state_dict(), strict=True)
    assert equal_state(loaded(ids).logits, linked(ids).logits)
    with pytest.raises(ValueError): SigSoftmaxModel(raw.config)
    wrong = dict(linked.config, output_probability_link='ordinary_softmax')
    with pytest.raises(ValueError): SigSoftmaxModel(wrong)


def test_same_original_stream_masks_counters_and_sampler(tmp_path):
    _, build = builders(tmp_path)
    t, control = build(), build(True)
    for _ in range(4):
        a, b = t.step(), control.step()
        for key in (*t.counters, 'draw_trace', 'lr'):
            assert equal_state(a[key], b[key]), key
        assert a['sigsoftmax_NLL_loss'] == a['combined_loss'] == a['CE_loss']
        assert a['probability_positions_this_update'] == a['CE_targets_this_update']
        assert a['auxiliary_pairs_this_update'] == 0 and a['committed_update']
    assert committed_state(host(t.state_dict()))
    assert equal_state(t.sampler.state_dict(), control.sampler.state_dict())


def test_actual_saved_four_vs_two_plus_two_full_state_and_history(tmp_path):
    _, build = builders(tmp_path)
    continuous = build()
    full = [continuous.step() for _ in range(4)]
    final = host(continuous.state_dict())
    split = build()
    partial = [split.step() for _ in range(2)]
    path = tmp_path / 'checkpoint.pt'
    split.save(path)
    resumed = build()
    resumed.load(path)
    partial += [resumed.step() for _ in range(2)]
    assert equal_state(final, host(resumed.state_dict()))
    for a, b in zip(full, partial):
        assert equal_state({k: v for k, v in a.items() if k not in ('seconds', 'data_wait_seconds')},
                           {k: v for k, v in b.items() if k not in ('seconds', 'data_wait_seconds')})


@pytest.mark.parametrize('field', ['kind', 'link', 'config', 'Adam', 'sampler', 'nonfinite'])
def test_wrong_or_uncommitted_state_refused(tmp_path, field):
    _, build = builders(tmp_path)
    t = build()
    t.step()
    state = copy.deepcopy(host(t.state_dict()))
    if field == 'kind': state['kind'] = 'ordinary_softmax'
    if field == 'link': state['spec']['sigsoftmax']['effective_logits'] = 'shifted'
    if field == 'config': state['model_config'].pop('output_probability_link')
    if field == 'Adam': next(iter(state['optimizer']['state'].values()))['step'].zero_()
    if field == 'sampler': state['sampler']['consumed']['web'] += 1
    if field == 'nonfinite': next(iter(state['model'].values())).fill_(float('nan'))
    assert not committed_state(state)
    path = tmp_path / 'bad.pt'
    torch.save(state, path)
    with pytest.raises(ValueError): build().load(path)


def test_failure_after_Adam_cannot_save_or_continue(tmp_path):
    _, build = builders(tmp_path)
    t = build()
    original = t.optimizer.step
    def fail(*args, **kwargs):
        original(*args, **kwargs)
        raise RuntimeError('After Adam fixture failure')
    t.optimizer.step = fail
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path / 'partial.pt')
    with pytest.raises(ValueError): t.step()
    assert not (tmp_path / 'partial.pt').exists()
