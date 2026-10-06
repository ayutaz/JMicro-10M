import copy
import sys

import pytest
import torch
from jmicro.experiment import ROOT
from jmicro.training import rng_state

sys.path.insert(0, str(ROOT / 'scripts'))
from mature_condition_trainer import MatureConditionTrainer, MatureQuotaSampler
from condition_positive_trainer import ConditionQuotaSampler
from run_eos_short_pilot import equal_state
from test_story_weight_comparison import fixture
from test_condition_positive_trainer import positive_fixture


@pytest.mark.parametrize('goals', [dict(web=83, story=0, ordinary_textbook=0, conditional_textbook=0),
    dict(web=37, story=11, ordinary_textbook=19, conditional_textbook=16)])
def test_exact_quota_exhaustion_and_inactive_streams(tmp_path, goals):
    view, _, _ = fixture(tmp_path)
    positive = positive_fixture(tmp_path)
    sampler = MatureQuotaSampler(view, positive, goals, 8)
    inactive = {g for g, n in goals.items() if not n}
    assert set(sampler.streams) == set(goals) - inactive
    teachers = inputs = 0
    while sampler.source_teachers != goals:
        x, y, _, focus = sampler.batch(3)
        teachers += int(y.ne(-100).sum())
        inputs += x.numel()
        assert not (focus & y.lt(8)).any()
    assert teachers == sum(goals.values())
    assert inputs == sum(sampler.source_tokens.values()) == sampler.position * 24
    for key in ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes', 'source_focus_teachers'):
        assert all(getattr(sampler, key)[g] == 0 for g in inactive)
    state = sampler.state_dict()
    restored = MatureQuotaSampler(view, positive, goals, 8)
    restored.load_state_dict(state)
    assert equal_state(state, restored.state_dict())
    with pytest.raises(ValueError, match='exhausted'):
        restored.batch(3)
    if inactive:
        bad = copy.deepcopy(state)
        bad['source_tokens'][next(iter(inactive))] = 8
        with pytest.raises(ValueError, match='inactive-source'):
            restored.load_state_dict(bad)
        with pytest.raises(ValueError, match='positive exact'):
            ConditionQuotaSampler(view, positive, goals, 8)


@pytest.mark.parametrize('web_only', [True, False])
def test_full_resume_inherits_adam_rng_and_rejects_changed_source(tmp_path, web_only):
    view, parent, binding = fixture(tmp_path)
    positive = positive_fixture(tmp_path)
    goals = (dict(web=400, story=0, ordinary_textbook=0, conditional_textbook=0) if web_only
        else dict(web=250, story=50, ordinary_textbook=50, conditional_textbook=50))
    def build(b=binding):
        return MatureConditionTrainer(parent, view, positive, goals, b, 'cpu', 8, 3)
    trainer = build()
    assert equal_state(trainer.model.state_dict(), parent['model'])
    assert equal_state(trainer.optimizer.state_dict(), parent['optimizer'])
    assert equal_state(rng_state(), parent['rng'])
    left = [trainer.step() for _ in range(4)]
    trainer.save(tmp_path / 'continuous/checkpoint.pt')
    split = build()
    right = [split.step() for _ in range(2)]
    split.save(tmp_path / 'split/checkpoint.pt')
    resumed = build()
    resumed.load(tmp_path / 'split/checkpoint.pt')
    right.extend(resumed.step() for _ in range(2))
    resumed.save(tmp_path / 'resumed/checkpoint.pt')
    a = torch.load(tmp_path / 'continuous/checkpoint.pt', map_location='cpu', weights_only=False)
    b = torch.load(tmp_path / 'resumed/checkpoint.pt', map_location='cpu', weights_only=False)
    for key in a:
        assert equal_state(a[key], b[key]), key
    for key in ('loss', 'gradient_norm', 'lr', 'token_digest', 'focus_token_digest', 'source_teachers'):
        assert [r[key] for r in left] == [r[key] for r in right]
    changed = dict(binding, source_sha256='changed')
    with pytest.raises(ValueError, match='identity/source/recipe'):
        build(changed).load(tmp_path / 'split/checkpoint.pt')


def test_rejects_empty_negative_boolean_quotas(tmp_path):
    view, _, _ = fixture(tmp_path)
    positive = positive_fixture(tmp_path)
    for n in (0, -1, True):
        with pytest.raises(ValueError, match='Nonnegative'):
            MatureQuotaSampler(view, positive, dict(web=n, story=0, ordinary_textbook=0, conditional_textbook=0), 8)
