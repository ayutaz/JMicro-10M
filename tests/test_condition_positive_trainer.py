import copy
import sys

import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT, sha256, write_json
from jmicro.training import rng_state

sys.path.insert(0, str(ROOT / 'scripts'))
from condition_positive_trainer import PositiveTrainView, PositiveStream, ConditionQuotaSampler, ConditionPositiveTrainer
from run_eos_short_pilot import equal_state
from test_story_weight_comparison import fixture


def positive_fixture(tmp_path):
    directory = tmp_path / 'positive'
    directory.mkdir()
    tokens = np.asarray(sum(([2, 30, 31 + i, 40, 3] for i in range(8)), []), dtype='<u2')
    focus = np.tile([0, 0, 1, 0, 0], 8).astype(np.uint8)
    np.savez(directory / 'train.npz', tokens=tokens, focus=focus,
             offsets=np.arange(8, dtype='<i8') * 5, lengths=np.full(8, 5, dtype='<i4'))
    write_json(directory / 'manifest.json', dict(kind='original_train_positive_condition_outcome_spans',
        newly_prepared_original_tokens=0, arrays_sha256=sha256(directory / 'train.npz'),
        documents=8, serialized_tokens=40, outcome_focus_body_targets=8))
    return PositiveTrainView(directory, sha256(directory / 'manifest.json'))


def test_shifted_original_focus_stream_and_exact_four_quotas(tmp_path):
    view, _, _ = fixture(tmp_path)
    positive = positive_fixture(tmp_path)
    stream = PositiveStream(positive)
    x, y, focused = stream.block(8)
    assert np.all(y[focused] >= 8) and not np.any(focused & (y == 3))
    saved = copy.deepcopy(stream.state_dict())
    expected = stream.block(8)
    restored = PositiveStream(positive)
    restored.load_state_dict(saved)
    assert all(np.array_equal(a, b) for a, b in zip(expected, restored.block(8)))
    goals = dict(web=17, story=9, ordinary_textbook=13, conditional_textbook=11)
    sampler = ConditionQuotaSampler(view, positive, goals, context=8)
    teachers = body = focus_count = inputs = 0
    while sampler.source_teachers != goals:
        x, y, byte_count, mask = sampler.batch(3)
        assert not x.eq(0).any() and not y.eq(2).any()
        assert not (mask & y.lt(8)).any()
        teachers += int(y.ne(-100).sum())
        body += byte_count
        focus_count += int(mask.sum())
        inputs += x.numel()
    assert teachers == 50
    assert body == teachers - sum(sampler.source_eos.values())
    assert focus_count == sum(sampler.source_focus_teachers.values()) > 0
    assert inputs == sum(sampler.source_tokens.values())
    with pytest.raises(ValueError, match='exhausted'):
        sampler.batch(3)


@pytest.mark.parametrize('factor', (1, 4))
def test_real_CPU_fullstate_continuous_and_resumed_positive_training(tmp_path, factor):
    view, parent, binding = fixture(tmp_path)
    positive = positive_fixture(tmp_path)
    goals = dict(web=200, story=100, ordinary_textbook=100, conditional_textbook=100)
    build = lambda weight=factor: ConditionPositiveTrainer(parent, view, positive, goals, weight, binding, 'cpu', 8, 3)
    trainer = build()
    assert equal_state(trainer.optimizer.state_dict(), parent['optimizer'])
    assert equal_state(trainer.model.state_dict(), parent['model']) and equal_state(rng_state(), parent['rng'])
    left = [trainer.step() for _ in range(4)]
    trainer.save(tmp_path / 'continuous/checkpoint.pt')
    resumed = build()
    right = [resumed.step() for _ in range(2)]
    resumed.save(tmp_path / 'split/checkpoint.pt')
    restarted = build()
    restarted.load(tmp_path / 'split/checkpoint.pt')
    right.extend(restarted.step() for _ in range(2))
    restarted.save(tmp_path / 'resumed/checkpoint.pt')
    a = torch.load(tmp_path / 'continuous/checkpoint.pt', map_location='cpu', weights_only=False)
    b = torch.load(tmp_path / 'resumed/checkpoint.pt', map_location='cpu', weights_only=False)
    for key in ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'lineage', 'tokens', 'supervised_tokens',
                'body_bytes', 'token_digest', 'focus_token_digest', 'focus_teacher_tokens',
                'weighted_teacher_mass', 'spec', 'study_binding', 'update'):
        assert equal_state(a[key], b[key]), key
    for key in ('loss', 'gradient_norm', 'token_digest', 'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass'):
        assert [r[key] for r in left] == [r[key] for r in right]
    with pytest.raises(ValueError, match='identity/source/recipe'):
        build(4 if factor == 1 else 1).load(tmp_path / 'split/checkpoint.pt')


def test_both_arms_match_inputs_and_teachers_but_change_actual_updates(tmp_path):
    view, parent, binding = fixture(tmp_path)
    positive = positive_fixture(tmp_path)
    goals = dict(web=200, story=100, ordinary_textbook=100, conditional_textbook=100)
    controls = []
    states = []
    for factor in (1, 4):
        trainer = ConditionPositiveTrainer(parent, view, positive, goals, factor, binding, 'cpu', 8, 3)
        controls.append([trainer.step() for _ in range(4)])
        states.append(copy.deepcopy(trainer.model.state_dict()))
    for key in ('token_digest', 'focus_token_digest', 'source_teachers', 'source_eos', 'source_input_tokens', 'source_body_bytes', 'source_focus_teachers'):
        assert [r[key] for r in controls[0]] == [r[key] for r in controls[1]], key
    assert not equal_state(states[0], states[1])
