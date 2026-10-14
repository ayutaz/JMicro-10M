"""Real CPU optimizer/resume and original CE stream fixtures, not quality."""
import copy
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
from pseudo_repetition_trainer import (PseudoRepetitionTrainer, committed_state,
                                      auxiliary_scores)
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.experiment import sha256
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.pseudo_repetition import repeat_rows

torch.set_num_threads(2)


class FixtureCodec:
    vocab_size = 4096

    def encode(self, text):
        return [b+8 for b in text.encode()]

    def decode_bytes(self, ids):
        # IDs above263 are unused fixture vocabulary, not actual corpus bytes.
        return b''.join(bytes([i-8]) if i < 264 else b'X' for i in ids if i >= 8)


def builders(tmp_path):
    pool = tmp_path / 'pool'
    pool.mkdir()
    records, tokens, codec = [], [], FixtureCodec()
    for genre in ('web', 'textbook', 'story'):
        for i in range(8):
            text = '初めの説明を書きます。次の文章を続けます。最後の記録は'+genre+str(i)+'です。'
            body = codec.encode(text)
            records.append(dict(source=genre, split='train', source_family=f'{genre}-{i}',
                canonical_sha256=hashlib.sha256(text.encode()).hexdigest(), body_tokens=len(body), offset=len(tokens)))
            tokens.extend([2]+body+[3])
    np.array(tokens, dtype='<u2').tofile(pool/'train.bin')
    (pool/'train.index.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in records))
    (pool/'manifest.json').write_text(json.dumps(dict(splits=dict(train=dict(
        tokens=len(tokens), index_sha256=sha256(pool/'train.index.jsonl'))))))
    manifest = sha256(pool/'manifest.json')
    stat = (pool/'train.index.jsonl').stat()
    ready = pool/('.compact-index-'+manifest[:16])
    ready.mkdir()
    (ready/'ready.json').write_text(json.dumps(dict(source_hash_verified_during_single_parse=True,
        binding=dict(manifest_sha256=manifest, index_sha256=sha256(pool/'train.index.jsonl'),
                     index_size=stat.st_size, index_mtime_ns=stat.st_mtime_ns))))
    config = json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config.update(num_hidden_layers=2, hidden_size=32, head_dim=8, rotary_dim=8,
        attention_scale=8**-.5, intermediate_size=64, vocab_size=4096, qk_norm_type='none')
    torch.manual_seed(13)
    model = JMicroModel(config)
    parent = dict(model_config=config, model=host(model.state_dict()), update=5, tokens=90, supervised_tokens=80)
    binding = dict(parent={'sha256': 'fixture-parent'}, weights_role='verification_only')

    def build(enabled=True, legacy=False):
        sampler = OriginalTrainCorpusSampler(pool, manifest, codec,
            dict(web=7000, textbook=2000, story=1000), seed=42)
        if legacy:
            return NaturalCorpusTrainer(parent, sampler, binding, batch=6, contrast=False, device='cpu')
        return PseudoRepetitionTrainer(parent, sampler, binding, batch=6, device='cpu', enabled=enabled)
    return parent, build


def test_disabled_objective_equals_actual_legacy_CE_model_Adam_schedule_RNG_stream(tmp_path):
    parent, build = builders(tmp_path)
    current = build(False)
    initial = host(current.state_dict())
    assert equal_state(initial['model'], parent['model'])
    history, snapshots = [], []
    for _ in range(4):
        history.append(current.step())
        snapshots.append(host(current.state_dict()))
    old = build(legacy=True)
    assert all(equal_state(initial[k], host(old.state_dict())[k]) for k in ('model', 'optimizer', 'scheduler', 'RNG', 'sampler'))
    for a, saved in zip(history, snapshots):
        b = old.step()
        for key in ('supervised_tokens', 'source_teachers', 'source_EOS', 'CE_input_tokens',
                    'original_body_bytes', 'token_digest', 'draw_trace', 'CE_loss', 'gradient_norm', 'lr'):
            assert equal_state(a[key], b[key]), key
        assert all(equal_state(saved[k], host(old.state_dict())[k])
                   for k in ('model', 'optimizer', 'scheduler', 'RNG', 'sampler'))
    assert committed_state(current.state_dict())


def test_auxiliary_matches_independent_native_forward_probability_formula(tmp_path):
    _, build = builders(tmp_path)
    trainer = build()
    selected = repeat_rows(trainer.sampler.take(6), trainer.sampler.tokenizer)
    assert selected
    loss, counts = auxiliary_scores(trainer.model, selected, 'cpu')
    expected, denominator = 0., 0
    for row in selected:
        ids = torch.tensor([row['input_ids']])
        scores = trainer.model(ids).logits[0].softmax(-1)
        targets = torch.tensor(row['target_ids'])
        chosen = scores.gather(-1, targets[:, None]).squeeze(-1)
        p = chosen[row['current_positions']]
        q = .5*chosen[row['previous_positions']].detach()
        expected += (-torch.log1p(-(p-q).abs())).sum()
        denominator += len(row['current_positions'])
    assert loss.item() == pytest.approx((expected/denominator).item(), abs=1e-7)
    assert counts['comparisons'] == denominator
    assert counts['physical_inputs'] == len(selected)*max(len(r['input_ids']) for r in selected)
    assert counts['valid_inputs'] == sum(len(r['input_ids']) for r in selected)
    assert counts['first_copy_reference_positions'] == sum(r['sentence_tokens'] for r in selected)


def test_enabled_uses_native_gradients_preserves_all_main_stream_and_Adam_clock(tmp_path):
    _, build = builders(tmp_path)
    current, old = build(), build(legacy=True)
    for _ in range(4):
        a, b = current.step(), old.step()
        for key in ('supervised_tokens', 'source_teachers', 'source_EOS', 'CE_input_tokens',
                    'original_body_bytes', 'token_digest', 'draw_trace', 'lr'):
            assert equal_state(a[key], b[key]), key
        assert equal_state(current.sampler.state_dict(), old.sampler.state_dict())
        assert a['auxiliary_gradient_norm'] > 0 and a['pseudo_comparisons_this_update'] > 0
        assert a['physical_input_tokens'] > b['physical_input_tokens']
    assert not equal_state(current.model.state_dict(), old.model.state_dict())
    assert current.model.lm_head.weight is current.model.model.embed_tokens.weight
    assert committed_state(current.state_dict())


def test_continuous6_vs3_save_resume3_exact_all_state_and_history(tmp_path):
    _, build = builders(tmp_path)
    continuous = build()
    expected_history = [continuous.step() for _ in range(6)]
    expected = host(continuous.state_dict())
    split = build()
    actual = [split.step() for _ in range(3)]
    split.save(tmp_path/'split.pt')
    resumed = build()
    resumed.load(tmp_path/'split.pt')
    actual.extend(resumed.step() for _ in range(3))
    assert equal_state(expected, host(resumed.state_dict()))
    omit = ('seconds', 'data_wait_seconds')
    assert all(equal_state({k:v for k,v in a.items() if k not in omit},
                           {k:v for k,v in b.items() if k not in omit})
               for a, b in zip(expected_history, actual))


@pytest.mark.parametrize('bad', ['source_RNG', 'clock', 'kind', 'recipe', 'optimizer',
                                'nonfinite', 'model_dtype', 'material_binding', 'comparison_clock'])
def test_invalid_checkpoint_rejected_before_any_state_mutation(tmp_path, bad):
    _, build = builders(tmp_path)
    source = build()
    source.step()
    state = host(source.state_dict())
    if bad == 'source_RNG': state['sampler']['RNG'] = 'INVALID'
    elif bad == 'clock': state['scheduler']['last_epoch'] += 1
    elif bad == 'kind': state['kind'] = 'legacy'
    elif bad == 'recipe': state['spec']['sentence_decay_recipe']['decay'] = .9
    elif bad == 'optimizer': next(iter(state['optimizer']['state'].values()))['step'] += 1
    elif bad == 'nonfinite': state['model']['model.norm.weight'][0] = torch.nan
    elif bad == 'model_dtype': state['model']['model.norm.weight'] = state['model']['model.norm.weight'].double()
    elif bad == 'material_binding': state['sampler']['binding']['pool'] = 'wrong'
    else: state['counters']['pseudo_comparisons'] = 1
    path = tmp_path/'bad.pt'
    torch.save(state, path)
    target = build()
    before = host(target.state_dict())
    with pytest.raises(ValueError):
        target.load(path)
    assert equal_state(before, host(target.state_dict()))


def test_interrupted_Adam_update_cannot_commit_save_retry_and_valid_load_restores(tmp_path, monkeypatch):
    _, build = builders(tmp_path)
    current = build()
    current.save(tmp_path/'initial.pt')
    original = current.optimizer.step
    def interrupted(*args, **kwargs):
        original(*args, **kwargs)
        raise RuntimeError('after actual Adam mutation')
    monkeypatch.setattr(current.optimizer, 'step', interrupted)
    with pytest.raises(RuntimeError):
        current.step()
    assert current.counters['update'] == 0
    with pytest.raises(ValueError): current.save(tmp_path/'invalid.pt')
    with pytest.raises(ValueError): current.step()
    assert not (tmp_path/'invalid.pt').exists()
    monkeypatch.setattr(current.optimizer, 'step', original)
    current.load(tmp_path/'initial.pt')
    current.step()
    expected = host(current.state_dict())
    clean = build()
    clean.step()
    assert equal_state(expected, host(clean.state_dict()))
