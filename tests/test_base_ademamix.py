"""Independent optimizer arithmetic and actual native completed-state fixtures."""
import copy
import math
import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from base_ademamix_trainer import DenseAdEMAMix, coefficients, AdEMAMixTrainer, POLICY
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


def test_against_independent_scalar_recurrence_including_uncorrected_slow():
    p = torch.tensor([1.2, -.7], dtype=torch.float64, requires_grad=True)
    opt = DenseAdEMAMix([p], lr=.01, weight_decay=.1, warmup=7)
    expected = p.detach().tolist()
    moments = [[0., 0., 0.] for _ in expected]
    for step in range(1, 13):
        gradient = [.2*(-1)**step, step/17]
        a = 2*min(step/7, 1)
        beta = .9999 if step >= 7 else math.exp(math.log(.5) / (
            (1-step/7)*math.log(.5)/math.log(.9+1e-8) + step/7*math.log(.5)/math.log(.9999+1e-8)))
        for i, g in enumerate(gradient):
            fast, slow, variance = moments[i]
            fast = .9*fast + .1*g
            slow = beta*slow + (1-beta)*g
            variance = .999*variance + .001*g*g
            moments[i] = [fast, slow, variance]
            direction = (fast/(1-.9**step) + a*slow) / (math.sqrt(variance/(1-.999**step)) + 1e-8)
            expected[i] -= .01*(direction+.1*expected[i])
        p.grad = torch.tensor(gradient, dtype=torch.float64); opt.step()
        assert p.detach().tolist() == pytest.approx(expected, abs=2e-13)
        for key, column in (('fast', 0), ('slow', 1), ('variance', 2)):
            assert opt.state[p][key].tolist() == pytest.approx([m[column] for m in moments], abs=1e-14)


def test_zero_slow_weight_matches_actual_adamw():
    p = torch.tensor([1., 2.], dtype=torch.float64, requires_grad=True)
    q = p.detach().clone().requires_grad_()
    a, b = DenseAdEMAMix([p], alpha=0.), torch.optim.AdamW([q], lr=1e-5, weight_decay=.1)
    for step in range(1, 13):
        p.grad = q.grad = torch.tensor([step/31, -1/step], dtype=torch.float64)
        a.step(); b.step()
        assert torch.allclose(p, q, atol=2e-14, rtol=0)


def test_half_life_schedule_and_real_saved_resume_across1000_transition(tmp_path):
    assert coefficients(1000, POLICY['betas'], 2., 1000) == (2., .9999)
    betas = [coefficients(i, POLICY['betas'], 2., 1000)[1] for i in (1, 200, 999, 1000, 1001)]
    assert betas == sorted(betas) and betas[-2:] == [.9999, .9999]
    p = torch.tensor([.7], requires_grad=True)
    a = DenseAdEMAMix([p])
    for i in range(998):
        p.grad = torch.tensor([(-1)**i*.2]); a.step()
    saved = tmp_path / 'moments.pt'; torch.save(dict(parameter=p.detach(), optimizer=a.state_dict()), saved)
    loaded = torch.load(saved, weights_only=False)
    q = loaded['parameter'].clone().requires_grad_(); b = DenseAdEMAMix([q]); b.load_state_dict(loaded['optimizer'])
    for i in range(998, 1003):
        p.grad = q.grad = torch.tensor([(-1)**i*.2]); a.step(); b.step()
        assert torch.equal(p, q) and equal_state(a.state_dict(), b.state_dict())


def test_nonfinite_and_missing_gradients_rejected_before_any_mutation():
    p, q = (torch.tensor([1.], requires_grad=True) for _ in range(2))
    opt = DenseAdEMAMix([p, q]); p.grad = torch.ones_like(p)
    before = copy.deepcopy(opt.state_dict())
    with pytest.raises(ValueError): opt.step()
    q.grad = torch.full_like(q, float('nan'))
    with pytest.raises(ValueError): opt.step()
    assert equal_state(before, opt.state_dict()) and p.item() == q.item() == 1.


@pytest.fixture
def builders(tmp_path):
    torch.set_num_threads(2)
    pool = tmp_path / 'pool'; manifest = fixture_pool(pool); saved = parent()
    def source():
        return OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
    def build():
        return AdEMAMixTrainer(saved, source(), dict(parent='fixture'), batch=4, device='cpu')
    return saved, source, build


def test_initial_parent_native_tie_rng_optimizer_and_original_masks(builders):
    saved, source, build = builders
    a = build()
    b = NaturalCorpusTrainer(saved, source(), dict(parent='fixture'), batch=4, contrast=False, device='cpu')
    assert equal_state(a.model.state_dict(), saved['model'])
    assert a.model.lm_head.weight is a.model.model.embed_tokens.weight
    assert [id(p) for p in a.model.parameters()] == [id(p) for g in a.optimizer.param_groups for p in g['params']]
    for index in range(4):
        left, right = a.step(), b.step()
        if index == 0:
            assert left['CE_loss'] == right['CE_loss']
        for key in (*a.counters, 'draw_trace', 'lr'):
            assert equal_state(left[key], right[key]), key
        assert equal_state(a.sampler.state_dict(), b.sampler.state_dict())
    assert not equal_state(a.model.state_dict(), b.model.state_dict())


def test_real_four_vs_two_save_plus_two_all_state_and_history(builders, tmp_path):
    _, _, build = builders
    a = build(); ah = [a.step() for _ in range(4)]; expected = host(a.state_dict())
    b = build(); bh = [b.step() for _ in range(2)]; saved = tmp_path / 'full.pt'; b.save(saved)
    b = build(); b.load(saved); bh += [b.step() for _ in range(2)]
    assert equal_state(expected, host(b.state_dict()))
    for left, right in zip(ah, bh, strict=True):
        assert equal_state({k: v for k, v in left.items() if k not in ('seconds', 'data_wait_seconds')},
                           {k: v for k, v in right.items() if k not in ('seconds', 'data_wait_seconds')})


@pytest.mark.parametrize('field', ['kind', 'recipe', 'step', 'shape', 'variance', 'nonfinite', 'source', 'scheduler', 'tie'])
def test_corrupted_full_state_rejected_before_model_mutation(builders, tmp_path, field):
    _, _, build = builders
    a = build(); a.step(); state = copy.deepcopy(host(a.state_dict()))
    moment = next(iter(state['optimizer']['state'].values()))
    if field == 'kind': state['kind'] = 'AdamW'
    if field == 'recipe': state['optimizer']['param_groups'][0]['alpha'] = 3.
    if field == 'step': moment['step'] = 0
    if field == 'shape': moment['slow'] = torch.zeros(1)
    if field == 'variance': moment['variance'].fill_(-1.)
    if field == 'nonfinite': moment['fast'].fill_(float('nan'))
    if field == 'source': state['sampler']['consumed']['web'] += 1
    if field == 'scheduler': state['scheduler']['last_epoch'] += 1
    if field == 'tie': state['model']['lm_head.weight'] = state['model']['lm_head.weight'].clone()+1
    saved = tmp_path / 'bad.pt'; torch.save(state, saved)
    b = build(); before = host(b.model.state_dict())
    with pytest.raises(ValueError): b.load(saved)
    assert equal_state(before, host(b.model.state_dict()))


def test_partial_optimizer_update_cannot_save_continue_and_can_restore_clean_checkpoint(builders, tmp_path):
    _, _, build = builders
    a = build(); a.step(); saved = tmp_path / 'valid.pt'; a.save(saved)
    expected = host(a.state_dict()); original = a.optimizer.step
    def fail():
        original(); raise RuntimeError('Fixture failure after actual moment/weight mutation')
    a.optimizer.step = fail
    with pytest.raises(RuntimeError): a.step()
    with pytest.raises(ValueError): a.save(tmp_path / 'partial.pt')
    with pytest.raises(ValueError): a.step()
    a.optimizer.step = original; a.load(saved)
    assert equal_state(expected, host(a.state_dict()))
    a.step()
