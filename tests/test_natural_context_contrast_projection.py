"""Protocol fixtures for separate head/RNG/state and unchanged original CE."""
import sys
from pathlib import Path

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_projection import ProjectedCorpusTrainer, make_projector
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import FixtureCodec, fixture_pool, parent


def builders(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    p = parent()
    binding = dict(parent={'sha256':'fixture-parent'}, weights_role='protocol_fixture')
    def build(projected=True):
        sampler = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7500,textbook=2000,story=500))
        cls = ProjectedCorpusTrainer if projected else NaturalCorpusTrainer
        return cls(p, sampler, binding, batch=4, device='cpu')
    return p, build


def test_actual_head_parameter_count_and_independent_RNG():
    torch.manual_seed(7)
    before = torch.get_rng_state().clone()
    a = make_projector(256, 'cpu')
    assert torch.equal(before, torch.get_rng_state())
    torch.manual_seed(9)
    b = make_projector(256, 'cpu')
    assert equal_state(a.state_dict(), b.state_dict())
    assert sum(p.numel() for p in a.parameters()) == 98304
    assert a(torch.zeros(2,256)).shape == (2,128)
    assert all('bias' not in key for key in a.state_dict())


def test_head_does_not_call_global_CPU_and_CUDA_seed(monkeypatch):
    def forbid(*args, **kwargs):
        raise AssertionError('Global manual_seed would also seed CUDA')
    monkeypatch.setattr(torch, 'manual_seed', forbid)
    assert make_projector(256, 'cpu')(torch.zeros(2,256)).shape == (2,128)


def test_native_initial_logits_state_and_RNG_equal_direct_control(tmp_path):
    p, build = builders(tmp_path)
    direct = build(False)
    rng = torch.get_rng_state().clone()
    ids = torch.tensor([[2,65,66,67]])
    expected = direct.model(ids).logits.detach()
    projected = build()
    assert torch.equal(rng, torch.get_rng_state())
    assert equal_state(p['model'], host(projected.model.state_dict()))
    assert torch.equal(expected, projected.model(ids).logits.detach())
    assert not set(projected.projector.state_dict()).intersection(projected.model.state_dict())
    assert projected.model.lm_head.weight is projected.model.model.embed_tokens.weight


def test_joint_training_and_original_stream_accounting_match_direct(tmp_path):
    _, build = builders(tmp_path)
    projected, direct = build(), build(False)
    before = host(projected.projector.state_dict())
    updates_with_pairs = 0
    for _ in range(4):
        a, b = projected.step(), direct.step()
        for key in ('token_digest','auxiliary_digest','source_teachers','source_EOS',
                    'supervised_tokens','CE_input_tokens','auxiliary_input_tokens',
                    'auxiliary_pairs','physical_input_tokens','original_body_bytes','draw_trace'):
            assert equal_state(a[key],b[key]), key
        if a['auxiliary_pairs_this_update']:
            updates_with_pairs += 1
            assert a['auxiliary_gradient_norm'] > 0 and a['train_only_head_gradient_norm'] > 0
        else:
            assert a['auxiliary_gradient_norm'] == a['train_only_head_gradient_norm'] == 0
    assert updates_with_pairs > 0
    assert not equal_state(before, host(projected.projector.state_dict()))
    state = projected.state_dict()
    assert 'projector' in state and all('projector' not in key for key in state['model'])
    assert len(state['optimizer']['state']) == len(projected.parameters)


def test_exact_four_versus_two_save_resume_two_all_state_and_history(tmp_path):
    _, build = builders(tmp_path)
    continuous = build()
    expected_rows = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = build()
    actual_rows = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = build()
    resumed.load(tmp_path/'split.pt')
    actual_rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected, host(resumed.state_dict()))
    for a,b in zip(expected_rows,actual_rows,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


def test_native_evaluation_cannot_see_changed_discarded_head(tmp_path):
    _, build = builders(tmp_path)
    trainer = build()
    trainer.step()
    ids = torch.tensor([[2,65,66,67]])
    expected = trainer.model(ids).logits.detach()
    with torch.no_grad():
        for parameter in trainer.projector.parameters():
            parameter.fill_(float('nan'))
    assert torch.equal(expected,trainer.model(ids).logits.detach())


def test_reject_changed_checkpoint_geometry_and_non_native_science(tmp_path):
    p, build = builders(tmp_path)
    trainer = build()
    state = host(trainer.state_dict())
    state['spec']['projection']['head_seed'] += 1
    torch.save(state,tmp_path/'changed.pt')
    with pytest.raises(ValueError,match='binding'):
        trainer.load(tmp_path/'changed.pt')
    with pytest.raises(ValueError,match='geometry'):
        ProjectedCorpusTrainer(p, trainer.sampler, dict(parent={}), device='cpu')
    with pytest.raises(ValueError,match='completed CE'):
        ProjectedCorpusTrainer(p, trainer.sampler, trainer.binding, contrast=False, device='cpu')
