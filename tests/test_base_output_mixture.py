"""Independent probability formula, native paths, actual resume and full gold."""
import copy
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
from base_output_mixture_model import ARMS, POLICY, TAG, OutputMixtureHead, OutputMixtureModel
from base_output_mixture_trainer import OutputMixtureTrainer
from base_output_mixture_evaluation import typed_native_evaluation, validate_record
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


@pytest.fixture
def initial():
    state = parent()
    with torch.device('meta'):
        state['model_config']['expected_parameter_count'] = sum(
            p.numel() for p in JMicroModel(state['model_config']).parameters())
    return state


@pytest.fixture
def build(initial, tmp_path):
    pool = tmp_path / 'pool'
    manifest = fixture_pool(pool)
    def constructor(arm=ARMS[1]):
        sampler = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(),
                    dict(web=7500, textbook=2000, story=500))
        return OutputMixtureTrainer(initial, sampler, dict(parent=dict(path='fixture', sha256='fixed')),
                                    arm, batch=4, device='cpu')
    return constructor


def test_initial_prediction_native_parent_RNG_tie_count_and_identical_new_parameters(initial):
    native = JMicroModel(initial['model_config'])
    native.load_state_dict(initial['model'])
    original = host(native.state_dict())
    before = torch.get_rng_state()
    models = [OutputMixtureModel.from_native(native, arm) for arm in ARMS]
    assert torch.equal(before, torch.get_rng_state())
    assert equal_state(original, host(native.state_dict()))
    assert equal_state(host(models[0].state_dict()), host(models[1].state_dict()))
    ids = torch.tensor([[2, 8, 9, 10]])
    p = native(ids).logits.softmax(-1)
    for model in models:
        assert model.lm_head.weight is model.model.embed_tokens.weight
        h = native.config['hidden_size']
        assert sum(x.numel() for x in model.parameters()) == native.config['expected_parameter_count'] + 2*(2*h*32+h+1)
        torch.testing.assert_close(model(ids).logits.softmax(-1), p, atol=1e-6, rtol=1e-6)


@pytest.mark.parametrize('arm', ARMS)
def test_independent_formula_after_nonzero_context_updates_and_finite_gradient(arm):
    torch.manual_seed(7)
    weight = torch.nn.Parameter(torch.randn(11, 4))
    head = OutputMixtureHead(weight, arm)
    with torch.no_grad():
        for up in head.up:
            up.weight.normal_(std=.3)
        head.prior.weight.normal_(std=.2)
    x = torch.randn(7, 4, requires_grad=True)
    contexts = head.contexts(x)
    prior = F.linear(x, head.prior.weight, head.prior.bias).softmax(-1)
    if arm == ARMS[0]:
        expected = F.linear(sum(prior[:, k:k+1] * c for k, c in enumerate(contexts)), weight).softmax(-1)
    else:
        expected = sum(prior[:, k:k+1] * F.linear(c, weight).softmax(-1)
                       for k, c in enumerate(contexts))
    actual = head(x).softmax(-1)
    torch.testing.assert_close(actual, expected, atol=1e-7, rtol=1e-6)
    F.nll_loss(actual.log(), torch.arange(7)).backward()
    assert torch.isfinite(x.grad).all()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in head.parameters())
    assert any(torch.count_nonzero(up.weight.grad) for up in head.up)


def test_MoS_can_exceed_single_softmax_rank_in_independent_toy_not_student_quality():
    torch.manual_seed(713)
    weight = torch.nn.Parameter(torch.randn(8, 2))
    a = OutputMixtureHead(weight, ARMS[0])
    with torch.no_grad():
        for down, up in zip(a.down, a.up):
            down.weight.normal_(std=.7)
            up.weight.normal_(std=.6)
        a.prior.weight.normal_(std=.6)
    b = OutputMixtureHead(weight, ARMS[1])
    b.load_state_dict(a.state_dict())
    x = torch.randn(24, 2)
    moc = a(x).log_softmax(-1).double()
    mos = b(x).log_softmax(-1).double()
    # Float32 arithmetic noise is excluded with a fixed explicit toy tolerance.
    assert int(torch.linalg.matrix_rank(moc, atol=1e-5, rtol=0)) <= 3
    assert int(torch.linalg.matrix_rank(mos, atol=1e-5, rtol=0)) > 3


@pytest.mark.parametrize('arm', ARMS)
def test_same_head_used_by_full_causal_padded_and_cached_paths_after_training(build, arm):
    t = build(arm)
    t.step()
    model = t.model.eval()
    ids = torch.tensor([[2, 8, 9, 10, 11]])
    full = model(ids).logits
    torch.testing.assert_close(model(ids, training_fast_path=True).logits, full, atol=2e-5, rtol=1e-5)
    first = model(ids[:, :2], use_cache=True)
    tail = model(ids[:, 2:], cache=first.cache, use_cache=True)
    torch.testing.assert_close(tail.logits, full[:, 2:], atol=2e-5, rtol=1e-5)
    padded = torch.tensor([[2, 8, 9, 10, 11], [2, 8, 9, 0, 0]])
    logits = model(padded, attention_mask=padded.ne(0)).logits
    torch.testing.assert_close(logits[1, :3], model(padded[1:2, :3]).logits[0], atol=2e-5, rtol=1e-5)
    assert not torch.count_nonzero(logits[1, 3:])
    clone = OutputMixtureModel(model.config)
    clone.load_state_dict(model.state_dict())
    torch.testing.assert_close(clone(ids).logits, full, atol=0, rtol=0)


def test_paired_original_teacher_masks_EOS_digest_full_sampler_and_optimizer_once(build):
    a, b = [build(arm) for arm in ARMS]
    for _ in range(4):
        ar, br = a.step(), b.step()
        for key in (*a.counters, 'draw_trace', 'lr'):
            assert equal_state(ar[key], br[key]), key
        assert equal_state(a.sampler.state_dict(), b.sampler.state_dict())
        assert ar['auxiliary_pairs'] == br['auxiliary_pairs'] == 0
    assert not equal_state(host(a.model.state_dict()), host(b.model.state_dict()))
    for t in (a, b):
        assert [id(p) for p in t.model.parameters()] == [id(p) for g in t.optimizer.param_groups for p in g['params']]
        assert all(float(m['step']) == 4 for m in t.optimizer.state.values())
        assert not t.lineage['original_parent_optimizer_reused']


@pytest.mark.parametrize('arm', ARMS)
def test_continuous_four_vs_two_save_two_all_optimizer_scheduler_RNG_sampler_history(build, tmp_path, arm):
    a = build(arm)
    ah = [a.step() for _ in range(4)]
    expected = host(a.state_dict())
    b = build(arm)
    bh = [b.step() for _ in range(2)]
    cp = tmp_path / 'checkpoint.pt'
    b.save(cp)
    b = build(arm)
    b.load(cp)
    bh.extend(b.step() for _ in range(2))
    assert equal_state(expected, host(b.state_dict()))
    for left, right in zip(ah, bh, strict=True):
        assert equal_state({k:v for k,v in left.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in right.items() if k not in ('seconds','data_wait_seconds')})


@pytest.mark.parametrize('problem', ('arm', 'moment', 'sampler', 'tie', 'partition'))
def test_bad_fullstate_is_refused_before_mutation(build, tmp_path, problem):
    a = build()
    a.step()
    state = copy.deepcopy(host(a.state_dict()))
    if problem == 'arm': state['spec']['mixture_arm'] = ARMS[0]
    elif problem == 'moment': next(iter(state['optimizer']['state'].values()))['step'].zero_()
    elif problem == 'sampler': state['sampler']['consumed']['web'] += 1
    elif problem == 'tie': state['model']['lm_head.weight'] += 1
    else: state['optimizer']['param_groups'][0]['params'].append(0)
    cp = tmp_path / 'invalid.pt'
    torch.save(state, cp)
    b = build()
    before = host(b.model.state_dict())
    with pytest.raises(ValueError): b.load(cp)
    assert equal_state(before, host(b.model.state_dict()))


def test_partial_update_refused_and_valid_resume_restores_all_state(build, tmp_path):
    a = build()
    a.step()
    cp = tmp_path / 'valid.pt'
    a.save(cp)
    expected = host(a.state_dict())
    original = a.optimizer.step
    def broken():
        original()
        raise RuntimeError('After actual optimizer mutation')
    a.optimizer.step = broken
    with pytest.raises(RuntimeError): a.step()
    with pytest.raises(ValueError): a.state_dict()
    with pytest.raises(ValueError): a.step()
    a.optimizer.step = original
    a.load(cp)
    assert equal_state(expected, host(a.state_dict()))


def test_explicit_evaluator_record_and_factory_restoration(build, tmp_path):
    t = build()
    record = dict(model_config=t.model.config, spec=t.spec, mixture_arm=ARMS[1],
                  mixture_policy=POLICY, mixture_model_class='OutputMixtureModel')
    validate_record(ARMS[1], record)
    wrong = copy.deepcopy(record)
    wrong['mixture_arm'] = ARMS[0]
    with pytest.raises(ValueError): validate_record(ARMS[1], wrong)
    import run_complete_text_comparison as native
    old = native.JMicroModel, native.RUN
    with pytest.raises(RuntimeError):
        with typed_native_evaluation(tmp_path):
            model = native.JMicroModel(t.model.config)
            assert model.config[TAG]['arm'] == ARMS[1]
            raise RuntimeError('Read-only scope fixture')
    assert (native.JMicroModel, native.RUN) == old
