import pytest
import torch

from jmicro.phase5 import equal_state
from jmicro.stable_extension import StableExtensionTrainer
from jmicro.training import Trainer, rng_state
from test_training import shard, config, spec


def parent_checkpoint(shard, tmp_path):
    parent = Trainer(config(), shard, spec(scheduler='wsd', warmup=1))
    for _ in range(3):
        parent.step()
    path = tmp_path / 'parent/checkpoint.pt'
    parent.save(path)
    return path


def test_extension_preserves_all_state_and_matches_resume(shard, tmp_path):
    path = parent_checkpoint(shard, tmp_path)
    saved = torch.load(path, weights_only=False)
    extended = dict(saved['spec'], schedule_updates=12)
    continuous = StableExtensionTrainer(config(), shard, extended)
    continuous.load_extension(path)
    assert equal_state(continuous.model.state_dict(), saved['model'])
    assert equal_state(continuous.optimizer.state_dict(), saved['optimizer'])
    assert equal_state(continuous.scheduler.state_dict(), saved['scheduler'])
    assert equal_state(continuous.sampler.state_dict(), saved['sampler'])
    assert equal_state(rng_state(), saved['rng'])
    assert (continuous.update, continuous.tokens, continuous.supervised_tokens,
            continuous.body_bytes, continuous.token_digest) == (
        saved['update'], saved['tokens'], saved['supervised_tokens'], saved['body_bytes'], saved['token_digest'])
    history = [continuous.step() for _ in range(4)]
    expected_rng = rng_state()
    paused = StableExtensionTrainer(config(), shard, extended)
    paused.load_extension(path)
    actual = [paused.step() for _ in range(2)]
    mid = tmp_path / 'fork/checkpoint.pt'
    paused.save(mid)
    resumed = StableExtensionTrainer(config(), shard, extended)
    resumed.load(mid)
    actual += [resumed.step() for _ in range(2)]
    for key in ('loss', 'lr', 'token_digest', 'tokens_seen'):
        assert [r[key] for r in history] == [r[key] for r in actual]
    for name in ('model', 'optimizer', 'scheduler', 'sampler'):
        left = getattr(continuous, name).state_dict()
        right = getattr(resumed, name).state_dict()
        assert equal_state(left, right), name
    assert equal_state(expected_rng, rng_state())
    assert resumed.lineage == continuous.lineage
    # Ordinary resume still rejects a changed budget.
    invalid = StableExtensionTrainer(config(), shard, dict(extended, schedule_updates=13))
    with pytest.raises(ValueError, match='configuration'):
        invalid.load(mid)


@pytest.mark.parametrize('change', [dict(schedule_updates=6), dict(lr=.0002), dict(scheduler='cosine')])
def test_extension_rejects_non_budget_changes(shard, tmp_path, change):
    path = parent_checkpoint(shard, tmp_path)
    extended = spec(scheduler='wsd', warmup=1, schedule_updates=12)
    extended.update(change)
    trainer = StableExtensionTrainer(config(), shard, extended)
    with pytest.raises(ValueError, match='only a larger'):
        trainer.load_extension(path)


def test_extension_rejects_decay_and_changed_parent(shard, tmp_path):
    path = parent_checkpoint(shard, tmp_path)
    trainer = StableExtensionTrainer(config(), shard, spec(scheduler='wsd', schedule_updates=12))
    with pytest.raises(ValueError, match='checksum'):
        trainer.load_extension(path, '00' * 32)
    state = torch.load(path, weights_only=False)
    state['spec'].update(scheduler='wsd_decay', branch_at=3, decay_updates=3, minimum_lr_ratio=.1)
    altered = tmp_path / 'decay.pt'
    torch.save(state, altered)
    with pytest.raises(ValueError, match='stable WSD'):
        trainer.load_extension(altered)
