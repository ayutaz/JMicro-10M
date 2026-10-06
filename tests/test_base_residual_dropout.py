"""Real CPU protocol checks for dropout, native inference and resumed RNG."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
from base_residual_dropout import ResidualDropoutTrainer, install_training_dropout
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import FixtureCodec, fixture_pool, parent


def builders(tmp_path):
    pool = tmp_path / 'pool'
    manifest = fixture_pool(pool)
    original = parent()
    binding = dict(parent={'sha256': 'CPU-fixture'}, weights_role='verification_only')

    def build(dropout=True):
        source = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(),
                                            dict(web=7500, textbook=2000, story=500))
        cls = ResidualDropoutTrainer if dropout else NaturalCorpusTrainer
        return cls(original, source, binding, batch=4, contrast=False, device='cpu')
    return original, build


def test_eval_initial_weights_logits_parameters_and_rng_identical(tmp_path):
    original, build = builders(tmp_path)
    control = build(False)
    control.model.eval()
    ids = torch.tensor([[2, 65, 66, 67]])
    expected = control.model(ids).logits.detach()
    rng = torch.get_rng_state().clone()
    trained = build()
    trained.model.eval()
    assert torch.equal(rng, torch.get_rng_state())
    assert equal_state(original['model'], host(trained.model.state_dict()))
    assert trained.model.lm_head.weight is trained.model.model.embed_tokens.weight
    assert sum(p.numel() for p in trained.model.parameters()) == sum(p.numel() for p in control.model.parameters())
    assert torch.equal(expected, trained.model(ids).logits.detach())
    assert torch.equal(rng, torch.get_rng_state())
    assert len(trained.model._residual_dropout_hooks) == 1 + 2 * original['model_config']['num_hidden_layers']


def test_training_masks_are_active_seeded_and_disable_for_native_reload(tmp_path):
    original, build = builders(tmp_path)
    trainer = build()
    ids = torch.tensor([[2, 65, 66, 67]])
    torch.manual_seed(17)
    rng = torch.get_rng_state().clone()
    first = trainer.model(ids).logits.detach()
    assert not torch.equal(rng, torch.get_rng_state())
    second = trainer.model(ids).logits.detach()
    assert not torch.equal(first, second)
    torch.manual_seed(17)
    assert torch.equal(first, trainer.model(ids).logits.detach())
    trainer.model.eval()
    native = JMicroModel(original['model_config']).eval()
    native.load_state_dict(trainer.model.state_dict(), strict=True)
    assert torch.equal(native(ids).logits, trainer.model(ids).logits)
    assert not hasattr(native, '_residual_dropout_hooks')


def test_same_teacher_stream_source_eos_sampler_and_no_extra_inputs(tmp_path):
    _, build = builders(tmp_path)
    trainer, control = build(), build(False)
    for _ in range(4):
        noisy, baseline = trainer.step(), control.step()
        for key in ('token_digest', 'auxiliary_digest', 'source_teachers', 'source_EOS',
                    'supervised_tokens', 'CE_input_tokens', 'original_body_bytes',
                    'physical_input_tokens', 'draw_trace'):
            assert equal_state(noisy[key], baseline[key]), key
        assert noisy['auxiliary_input_tokens'] == noisy['auxiliary_pairs'] == 0
        assert noisy['gradient_norm'] > 0
        assert torch.isfinite(torch.tensor(noisy['CE_loss']))
    assert equal_state(trainer.sampler.state_dict(), control.sampler.state_dict())
    assert not equal_state(host(trainer.model.state_dict()), host(control.model.state_dict()))


def test_continuous_vs_resumed_all_state_and_masks_exact(tmp_path):
    _, build = builders(tmp_path)
    continuous = build()
    expected_rows = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = build()
    actual_rows = [split.step() for _ in range(2)]
    split.save(tmp_path / 'split.pt')
    resumed = build()
    resumed.load(tmp_path / 'split.pt')
    actual_rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected, host(resumed.state_dict()))
    for a, b in zip(expected_rows, actual_rows, strict=True):
        assert equal_state({k: v for k, v in a.items() if k not in ('seconds', 'data_wait_seconds')},
                           {k: v for k, v in b.items() if k not in ('seconds', 'data_wait_seconds')})


def test_reject_reinterpreted_checkpoint_disabled_training_and_double_hooks(tmp_path):
    _, build = builders(tmp_path)
    trainer = build()
    state = copy.deepcopy(host(trainer.state_dict()))
    state['spec']['regularization']['probability'] = 0.2
    torch.save(state, tmp_path / 'changed.pt')
    with pytest.raises(ValueError, match='binding'):
        trainer.load(tmp_path / 'changed.pt')
    with pytest.raises(ValueError, match='install once'):
        install_training_dropout(trainer.model)
    with pytest.raises(ValueError, match='Finite'):
        install_training_dropout(JMicroModel(trainer.model.config), float('nan'))
    trainer.model.eval()
    with pytest.raises(ValueError, match='model.train'):
        trainer.step()
