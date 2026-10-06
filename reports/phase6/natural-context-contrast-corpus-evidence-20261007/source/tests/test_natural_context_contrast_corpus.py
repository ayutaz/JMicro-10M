"""Original source/window/quota protocol fixtures, not quality evidence."""
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pytest
import torch
from torch.nn import functional as F

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from natural_context_contrast_corpus import (OriginalTrainCorpusSampler, NaturalCorpusTrainer,
    document_windows, observed_pair)
from natural_context_contrast_trainer import host, right_pad
from jmicro.experiment import sha256
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state

torch.set_num_threads(2)


class FixtureCodec:
    vocab_size = 128
    def encode(self, text):
        return list(text.encode())
    def decode_bytes(self, ids):
        return bytes(i for i in ids if i >= 8)


def fixture_pool(path):
    path.mkdir()
    records, tokens = [], []
    for genre, chars in (('web', ('A','B')), ('textbook', ('C','D')), ('story', ('E','F'))):
        for i in range(3):
            length = 750 if genre == 'web' and i == 2 else 33+i
            text = chars[0]*length+'\n'+chars[1]*length
            body = list(text.encode())
            records.append(dict(source=genre, split='train', source_family=f'{genre}-{i}',
                canonical_sha256=hashlib.sha256(text.encode()).hexdigest(), body_tokens=len(body), offset=len(tokens)))
            tokens.extend([2]+body+[3])
    np.array(tokens, dtype='<u2').tofile(path/'train.bin')
    (path/'train.index.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in records))
    index_sha = sha256(path/'train.index.jsonl')
    manifest = dict(splits=dict(train=dict(tokens=len(tokens), index_sha256=index_sha)))
    (path/'manifest.json').write_text(json.dumps(manifest))
    manifest_sha = sha256(path/'manifest.json')
    stat = (path/'train.index.jsonl').stat()
    cache = path/('.compact-index-'+manifest_sha[:16])
    cache.mkdir()
    (cache/'ready.json').write_text(json.dumps(dict(source_hash_verified_during_single_parse=True,
        binding=dict(manifest_sha256=manifest_sha, index_sha256=index_sha,
                     index_size=stat.st_size, index_mtime_ns=stat.st_mtime_ns))))
    return manifest_sha


def parent():
    config = json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config.update(num_hidden_layers=2, hidden_size=32, head_dim=8, rotary_dim=8,
                  attention_scale=8**-0.5, intermediate_size=64, vocab_size=128, qk_norm_type='none')
    torch.manual_seed(13)
    model = JMicroModel(config)
    return dict(model_config=config, model=host(model.state_dict()), update=5, tokens=90, supervised_tokens=80)


def test_long_original_targets_and_EOS_exactly_once_without_fragment_boundaries():
    body = [65]*2500
    windows = list(document_windows(body))
    assert [i for w in windows for i in w['target_ids'] if i != -100] == body+[3]
    assert all(len(w['input_ids']) <= 1024 and 3 not in w['input_ids'] for w in windows)
    assert sum(w['input_ids'].count(2) for w in windows) == 2  # Original BOS in overlapping contexts only.
    assert any(-100 in w['target_ids'] for w in windows)


def test_exact_genre_teacher_quotas_and_sampler_restart(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    goals = dict(web=1300, textbook=300, story=120)
    def build():
        return OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), goals)
    sampler = build()
    sampler.take(4)
    resumed = build()
    resumed.load_state_dict(sampler.state_dict())
    assert equal_state(sampler.take(4), resumed.take(4))
    assert equal_state(sampler.state_dict(), resumed.state_dict())
    rows = []
    while not sampler.exhausted:
        rows.extend(sampler.take(4))
    assert sampler.consumed == goals
    assert all(len(r['input_ids']) == len(r['target_ids']) for r in rows)


@pytest.mark.parametrize('contrast', [False, True])
def test_full_corpus_CPU_state_resume_and_accounting(tmp_path, contrast):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    p = parent()
    binding = dict(parent={'sha256':'fixture-parent'}, weights_role='verification_only')
    def build():
        source = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
        return NaturalCorpusTrainer(p, source, binding, batch=4, contrast=contrast, device='cpu')
    continuous = build()
    history = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = build()
    actual = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = build()
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(2))
    assert equal_state(expected, host(resumed.state_dict()))
    omitted = ('seconds','data_wait_seconds')
    assert all(equal_state({k:v for k,v in a.items() if k not in omitted},
                           {k:v for k,v in b.items() if k not in omitted})
               for a,b in zip(history,actual,strict=True))
    counters = expected['counters']
    assert counters['supervised_tokens'] == sum(counters['source_teachers'].values())
    assert counters['source_teachers'] == expected['sampler']['consumed']
    assert counters['CE_input_tokens'] >= counters['supervised_tokens']
    assert sum(counters['source_EOS'].values()) > 0
    assert counters['auxiliary_pairs'] > 0 if contrast else counters['auxiliary_pairs'] == 0


def test_ineligible_pair_does_not_exclude_CE_unit():
    body = [65]*70
    raw, left, right, reason = observed_pair(body, FixtureCodec())
    assert raw == bytes(body) and not left and not right
    assert reason == 'no_original_codec_stable_sentence_pair'
    assert [i for w in document_windows(body) for i in w['target_ids'] if i != -100] == body+[3]


def test_only_supervised_head_rows_equal_native_masked_CE(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    p = parent()
    source = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
    state = source.state_dict()
    rows = source.take(4)
    source.load_state_dict(state)
    trainer = NaturalCorpusTrainer(p, source, dict(parent={'sha256':'fixture'}), batch=4, contrast=False, device='cpu')
    ids, lengths = right_pad([r['input_ids'] for r in rows], 'cpu')
    valid = torch.arange(ids.shape[1])[None] < lengths[:,None]
    labels = torch.full_like(ids,-100)
    for i,row in enumerate(rows):
        labels[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'])
    expected = F.cross_entropy(trainer.model(ids, valid).logits.reshape(-1,128), labels.reshape(-1), ignore_index=-100)
    actual = trainer.step()
    assert actual['CE_loss'] == pytest.approx(float(expected.detach()), abs=1e-6)
