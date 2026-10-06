"""Real small CPU optimizer trajectories; fixtures are not quality/CUDA evidence."""
import copy
import sys
from types import SimpleNamespace

import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256
from jmicro.training import Trainer, rng_state

sys.path.insert(0, str(ROOT / 'scripts'))
from story_weight_trainer import GenreStream, GenreQuotaSampler, StoryWeightTrainer
from run_eos_short_pilot import equal_state
import run_story_weight_comparison as study


def fixture(tmp_path):
    torch.set_num_threads(2)
    directory = tmp_path / 'data'; directory.mkdir()
    write_json(directory / 'manifest.json', dict(vocab_size=64))
    documents = [[2, 8 + tag, 12 + doc, 20, 3] for tag in range(3) for doc in range(8)]
    tokens = np.asarray(sum(documents, []), dtype='<u2')
    view = SimpleNamespace(directory=directory, split='train', tokens=tokens,
        manifest=dict(vocab_size=64), byte_lengths=np.array([0] * 8 + [1] * 56),
        index=SimpleNamespace(offsets=np.arange(24) * 5, lengths=np.array([3] * 24),
                              sources=np.repeat(np.arange(3), 8)))
    config = read_json(ROOT / 'configs/models/t4k.json')
    config.update(vocab_size=64, hidden_size=32, num_attention_heads=2, num_key_value_heads=1,
        head_dim=16, rotary_dim=16, num_hidden_layers=1, intermediate_size=48,
        attention_scale=.25, qk_norm_type='none')
    spec = dict(seed=42, context=8, batch=3, accumulation=1, lr=.0002, weight_decay=.1,
        warmup=0, schedule_updates=1000, scheduler='wsd', dtype='fp32', compile=False,
        backend='math', training_fast_path=True)
    trainer = Trainer(config, view, spec); trainer.step()
    path = tmp_path / 'parent/checkpoint.pt'; trainer.save(path)
    parent = torch.load(path, map_location='cpu', weights_only=False)
    b = dict(parent=dict(path=str(path), sha256=sha256(path)), config_sha256='CPU-fixture-only', arm='test')
    return view, parent, b


def test_genre_stream_overlap_whole_documents_and_resume(tmp_path):
    view, _, _ = fixture(tmp_path)
    stream = GenreStream(view, 'story', 42)
    x, y = stream.block(8)
    state = copy.deepcopy(stream.state_dict())
    expected_x, expected_y = stream.block(8)
    assert expected_x[0] == (2 if y[-1] == -100 else y[-1])
    restored = GenreStream(view, 'story', 42); restored.load_state_dict(state)
    actual_x, actual_y = restored.block(8)
    assert np.array_equal(actual_x, expected_x) and np.array_equal(actual_y, expected_y)
    assert (x == 9).any() and not (x == 8).any() and not (x == 10).any()
    invalid = dict(state, token_offset=5)
    with pytest.raises(ValueError): restored.load_state_dict(invalid)


def test_exact_three_quotas_EOS_BOS_and_terminal_masking(tmp_path):
    view, _, _ = fixture(tmp_path)
    goals = dict(web=17, story=9, textbook=13)
    sampler = GenreQuotaSampler(view, goals, context=8)
    teachers = eos = body = inputs = 0
    while sampler.source_teachers != goals:
        x, y, byte_count = sampler.batch(3)
        assert x.shape == y.shape == (3, 8) and not (x == 0).any() and not (y == 2).any()
        teachers += int(y.ne(-100).sum()); eos += int(y.eq(3).sum())
        body += byte_count; inputs += x.numel()
    assert teachers == 39 and eos == sum(sampler.source_eos.values())
    assert body == teachers - eos == sum(sampler.source_body_bytes.values())
    assert inputs == sum(sampler.source_tokens.values())
    with pytest.raises(ValueError, match='exhausted'): sampler.batch(3)
    with pytest.raises(ValueError, match='recipe differs'):
        GenreQuotaSampler(view, dict(goals, story=10), 8).load_state_dict(sampler.state_dict())


def test_inherited_Adam_RNG_constant_LR_and_actual_continuous_resume(tmp_path):
    view, parent, b = fixture(tmp_path); goals = dict(web=90, story=40, textbook=70)
    build = lambda binding=b: StoryWeightTrainer(parent, view, goals, binding, 'cpu', context=8, batch=3)
    trainer = build()
    assert equal_state(trainer.optimizer.state_dict(), parent['optimizer'])
    assert equal_state(trainer.model.state_dict(), parent['model']) and equal_state(rng_state(), parent['rng'])
    left = [trainer.step() for _ in range(4)]
    trainer.save(tmp_path / 'continuous/checkpoint.pt')
    resumed = build(); right = [resumed.step() for _ in range(2)]
    resumed.save(tmp_path / 'split/checkpoint.pt')
    restarted = build(); restarted.load(tmp_path / 'split/checkpoint.pt')
    right += [restarted.step() for _ in range(2)]
    restarted.save(tmp_path / 'resumed/checkpoint.pt')
    a = torch.load(tmp_path / 'continuous/checkpoint.pt', map_location='cpu', weights_only=False)
    z = torch.load(tmp_path / 'resumed/checkpoint.pt', map_location='cpu', weights_only=False)
    for key in ('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens',
                'body_bytes','token_digest','spec','study_binding','update'):
        assert equal_state(a[key], z[key]), key
    for key in ('loss','gradient_norm','lr','token_digest','source_teachers','source_eos'):
        assert [r[key] for r in left] == [r[key] for r in right]
    assert all(r['lr'] == .0002 for r in left)
    with pytest.raises(ValueError, match='identity/source/recipe'):
        build(dict(b, config_sha256='changed')).load(tmp_path / 'split/checkpoint.pt')


def test_measured_budget_counts_both_arms_warmup_saving_and_eval():
    rows = [dict(seconds=.2 if i < 8 else .05) for i in range(32)]
    measurement = dict(timings={arm:dict(histories=rows,verification_teacher_tokens=32000*32,terminal_save_seconds=.2)
                               for arm in study.GOALS})
    timing, estimate = study.estimate_training(measurement)
    assert set(timing) == {'control', 'story20'}
    assert timing['control']['estimated_updates'] == 3125
    assert timing['control']['warmup_seconds'] == pytest.approx(1.2)
    assert timing['control']['save_seconds'] == pytest.approx(2.8)
    assert estimate == pytest.approx(2*(3125*.05+1.2+2.8)*1.3+600)
    with pytest.raises(ValueError):
        study.estimate_training(dict(timings={'control':measurement['timings']['control']}))
