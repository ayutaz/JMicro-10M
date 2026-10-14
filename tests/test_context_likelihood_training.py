"""Actual CPU CE/auxiliary/Adam and full-state resume, not model quality."""
import copy
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from context_likelihood_trainer import ContextLikelihoodTrainer, committed_state, suffix_scores
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.experiment import sha256
from jmicro.phase5 import equal_state
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.model import JMicroModel
from test_natural_context_contrast_corpus import FixtureCodec, parent


def builders(tmp_path):
    pool = tmp_path / 'pool'
    pool.mkdir()
    records, tokens = [], []
    for genre in ('web', 'textbook', 'story'):
        for i in range(8):
            text = chr(65 + i) * 32 + '\n' + chr(97 + i) * 32
            body = list(text.encode())
            records.append(dict(source=genre, split='train', source_family=f'{genre}-{i}',
                canonical_sha256=hashlib.sha256(text.encode()).hexdigest(), body_tokens=len(body), offset=len(tokens)))
            tokens.extend([2] + body + [3])
    np.array(tokens, dtype='<u2').tofile(pool / 'train.bin')
    (pool / 'train.index.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in records))
    (pool / 'manifest.json').write_text(json.dumps(dict(splits=dict(train=dict(
        tokens=len(tokens), index_sha256=sha256(pool / 'train.index.jsonl'))))))
    manifest = sha256(pool / 'manifest.json')
    stat = (pool / 'train.index.jsonl').stat()
    ready = pool / ('.compact-index-' + manifest[:16])
    ready.mkdir()
    (ready / 'ready.json').write_text(json.dumps(dict(source_hash_verified_during_single_parse=True,
        binding=dict(manifest_sha256=manifest, index_sha256=sha256(pool / 'train.index.jsonl'),
                     index_size=stat.st_size, index_mtime_ns=stat.st_mtime_ns))))
    p = parent()
    binding = dict(parent={'sha256': 'fixture-parent'}, weights_role='verification_only')
    def build(enabled=True, legacy=False):
        sampler = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7000, textbook=2000, story=1000))
        if legacy:
            return NaturalCorpusTrainer(p, sampler, binding, batch=6, contrast=False, device='cpu')
        return ContextLikelihoodTrainer(p, sampler, binding, batch=6, device='cpu', enabled=enabled)
    return p, build


def test_disabled_new_objective_matches_actual_legacy_CE_weights_Adam_RNG_and_source(tmp_path):
    p, build = builders(tmp_path)
    current = build(False)
    zero = host(current.state_dict())
    assert equal_state(p['model'], host(current.model.state_dict()))
    snapshots, history = [], []
    for _ in range(4):
        history.append(current.step())
        snapshots.append(host(current.state_dict()))
    legacy = build(legacy=True)
    assert all(equal_state(zero[k], host(legacy.state_dict())[k]) for k in ('model', 'optimizer', 'scheduler', 'RNG'))
    for a, saved in zip(history, snapshots):
        b = legacy.step()
        for key in ('supervised_tokens', 'source_teachers', 'source_EOS', 'CE_input_tokens',
                    'original_body_bytes', 'token_digest', 'draw_trace', 'CE_loss', 'gradient_norm', 'lr'):
            assert equal_state(a[key], b[key]), key
        old_state = host(legacy.state_dict())
        assert all(equal_state(saved[k], old_state[k]) for k in ('model', 'optimizer', 'scheduler', 'RNG', 'sampler'))
    assert committed_state(current.state_dict())


def test_suffix_scores_agree_with_independent_native_likelihood_and_ignore_prefix(tmp_path):
    p = parent()
    model = JMicroModel(p['model_config'])
    model.load_state_dict(p['model'])
    model.eval()
    prefix, suffix = [65] * 20, [66] * 20
    positive = dict(input_ids=[2] + prefix + suffix[:-1], target_ids=[-100] * 20 + suffix)
    negative = dict(input_ids=[2] + [67] * 20 + suffix[:-1], target_ids=[-100] * 20 + suffix)
    left, right, counts = suffix_scores(model, [dict(positive=positive, negative=negative)], 'cpu')
    encoded = [dict(ids=row['input_ids'] + [suffix[-1]], context_tokens=21,
                    target_ids=suffix, target_bytes=20) for row in (positive, negative)]
    expected = NativeLikelihood(model, FixtureCodec(), device='cpu').score_encoded(encoded)
    assert float(left.detach()) == pytest.approx(expected[0]['log_likelihood'], abs=2e-5)
    assert float(right.detach()) == pytest.approx(expected[1]['log_likelihood'], abs=2e-5)
    assert counts == dict(valid_inputs=80, physical_inputs=80, target_evaluations=40)


def test_enabled_auxiliary_uses_vocabulary_gradients_and_preserves_main_stream(tmp_path):
    _, build = builders(tmp_path)
    current, legacy = build(), build(legacy=True)
    gradients = []
    for _ in range(6):
        a, b = current.step(), legacy.step()
        for key in ('supervised_tokens', 'source_teachers', 'source_EOS', 'CE_input_tokens',
                    'original_body_bytes', 'token_digest', 'draw_trace', 'lr'):
            assert equal_state(a[key], b[key]), key
        assert equal_state(current.sampler.state_dict(), legacy.sampler.state_dict())
        gradients.append(a['auxiliary_gradient_norm'])
    assert any(g > 0 for g in gradients)
    assert a['auxiliary_pairs'] > 0 and a['auxiliary_target_evaluations'] >= 32 * a['auxiliary_pairs']
    assert not equal_state(current.model.state_dict(), legacy.model.state_dict())
    assert current.model.lm_head.weight is current.model.model.embed_tokens.weight
    assert committed_state(current.state_dict())


def test_actual_continuous6_vs3_save3_full_state_FIFO_and_history(tmp_path):
    _, build = builders(tmp_path)
    continuous = build()
    history = [continuous.step() for _ in range(6)]
    expected = host(continuous.state_dict())
    split = build()
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path / 'split.pt')
    resumed = build()
    resumed.load(tmp_path / 'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected, host(resumed.state_dict()))
    omit = ('seconds', 'data_wait_seconds')
    assert all(equal_state({k: v for k, v in a.items() if k not in omit},
                           {k: v for k, v in b.items() if k not in omit}) for a, b in zip(history, actual))


@pytest.mark.parametrize('bad', ['FIFO', 'source_RNG', 'clock', 'kind', 'optimizer', 'nonfinite'])
def test_invalid_checkpoint_rejected_before_state_mutation(tmp_path, bad):
    _, build = builders(tmp_path)
    source = build()
    source.step()
    state = host(source.state_dict())
    if bad == 'FIFO': state['context_FIFO']['entries'][0]['prefix_ids'][0] = 8
    elif bad == 'source_RNG': state['sampler']['RNG'] = 'INVALID'
    elif bad == 'clock': state['counters']['supervised_tokens'] += 1
    elif bad == 'kind': state['kind'] = 'legacy_forgery'
    elif bad == 'optimizer': state['optimizer']['param_groups'][0]['lr'] = .002
    else: state['model']['lm_head.weight'][0, 0] = float('nan')
    path = tmp_path / 'bad.pt'
    torch.save(state, path)
    receiver = build()
    before = host(receiver.state_dict())
    with pytest.raises(ValueError): receiver.load(path)
    assert equal_state(before, host(receiver.state_dict()))


def test_interrupted_optimizer_cannot_commit_FIFO_save_or_retry_and_can_restore(tmp_path, monkeypatch):
    _, build = builders(tmp_path)
    trainer = build()
    trainer.step()
    trainer.save(tmp_path / 'good.pt')
    previous_FIFO = trainer.context_FIFO.state_dict()
    def fail(): raise RuntimeError('fixture-Adam-interruption')
    with monkeypatch.context() as patch:
        patch.setattr(trainer.optimizer, 'step', fail)
        with pytest.raises(RuntimeError): trainer.step()
        assert trainer.context_FIFO.state_dict() == previous_FIFO
        with pytest.raises(ValueError): trainer.save(tmp_path / 'invalid.pt')
        with pytest.raises(ValueError): trainer.step()
    assert not (tmp_path / 'invalid.pt').exists()
    trainer.load(tmp_path / 'good.pt')
    trainer.step()
    assert committed_state(trainer.state_dict())
