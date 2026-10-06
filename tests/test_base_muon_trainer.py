import copy
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from base_muon_trainer import MuonTrainer, finite_muon_state
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


def builders(tmp_path):
    pool = tmp_path / 'pool'
    manifest = fixture_pool(pool)
    p = parent()
    def build(muon=True):
        sampler = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
        return (MuonTrainer if muon else NaturalCorpusTrainer)(p, sampler,
            dict(parent={'sha256':'fixture'}, weights_role='verification_only'), batch=4, contrast=False, device='cpu')
    return p, build


def test_exact_native_partition_tied_vocab_and_identical_initial_outputs(tmp_path):
    p, build = builders(tmp_path)
    t, control = build(), build(False)
    vocab = t.model.model.embed_tokens.weight
    assert vocab is t.model.lm_head.weight
    assert t.optimizer.names['adamw'][0] == 'model.embed_tokens.weight'
    assigned = [v for g in t.optimizer.param_groups for v in g['params']]
    assert len(assigned) == len({id(v) for v in assigned}) == len(list(t.model.parameters()))
    assert all(v.ndim == 2 and v is not vocab for v in t.optimizer.muon.param_groups[0]['params'])
    assert equal_state(p['model'], host(t.model.state_dict()))
    t.model.eval(); control.model.eval()
    assert torch.equal(t.model(torch.tensor([[2,65,66]])).logits, control.model(torch.tensor([[2,65,66]])).logits)


def test_same_original_gold_stream_counters_and_finite_hybrid_state(tmp_path):
    _, build = builders(tmp_path)
    t, control = build(), build(False)
    for _ in range(4):
        a, b = t.step(), control.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens',
                    'original_body_bytes','token_digest','auxiliary_digest','draw_trace','lr'):
            assert equal_state(a[key], b[key]), key
    assert finite_muon_state(t.state_dict())
    assert equal_state(t.sampler.state_dict(), control.sampler.state_dict())
    assert not equal_state(t.model.state_dict(), control.model.state_dict())


def test_continuous_vs_full_hybrid_checkpoint_resume_and_history(tmp_path):
    _, build = builders(tmp_path)
    continuous = build(); expected_rows = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = build(); rows = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = build(); resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected, host(resumed.state_dict()))
    for a, b in zip(expected_rows, rows, strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


@pytest.mark.parametrize('mutation', ['partition','updates','scheduler','source'])
def test_mismatched_recipe_or_uncommitted_accounting_rejected(tmp_path, mutation):
    _, build = builders(tmp_path)
    t = build(); t.step(); state = host(t.state_dict())
    if mutation == 'partition': state['optimizer']['names']['muon'].reverse()
    if mutation == 'updates': state['optimizer']['completed_steps'] += 1
    if mutation == 'scheduler': state['scheduler']['position'] += 1
    if mutation == 'source': state['counters']['source_teachers']['web'] += 1
    torch.save(state, tmp_path/'bad.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'bad.pt')
