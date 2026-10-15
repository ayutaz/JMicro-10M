"""Consume/speculate/save/load/end/failure using real original TRAIN sampler."""
import copy
from pathlib import Path
import sys
import threading

import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from forgetting_attention_prefetch_loader import PrefetchedOriginalSampler, stage_original_rows
from natural_context_contrast_trainer import right_pad
from jmicro.phase5 import equal_state
from test_pseudo_repetition_training import builders


def test_staged_values_targets_physical_shape_equal_independent_original_construction():
    rows = [dict(input_ids=[2, 11, 12, 13], target_ids=[-100, 12, 13, 3]),
            dict(input_ids=[2, 21], target_ids=[21, 3])]
    ids, target = stage_original_rows(rows)
    old, _ = right_pad([r['input_ids'] for r in rows], 'cpu')
    assert torch.equal(ids, old)
    assert torch.equal(target, torch.tensor([[-100, 12, 13, 3], [21, 3, -100, -100]]))
    assert ids.device.type == target.device.type == 'cpu'
    assert ids.dtype == target.dtype == torch.long and ids.is_contiguous() and target.is_contiguous()


@pytest.mark.parametrize('rows', [[], [dict(input_ids=[], target_ids=[])],
    [dict(input_ids=[2, 11], target_ids=[3])]])
def test_bad_rows_fail_before_device_work(rows):
    with pytest.raises(ValueError): stage_original_rows(rows)


def sources(tmp_path):
    _, build = builders(tmp_path)
    return build(legacy=True).sampler, build(legacy=True).sampler


def test_real_original_rows_and_complete_logical_state_equal_while_next_batch_is_queued(tmp_path):
    synchronous, source = sources(tmp_path)
    with PrefetchedOriginalSampler(source, 6) as queued:
        before = torch.get_rng_state().clone()
        for _ in range(6):
            rows, ids, targets = queued.take_staged(6)
            original = synchronous.take(6)
            assert equal_state(rows, original)
            assert equal_state(queued.state_dict(), synchronous.state_dict())
            assert queued.consumed == synchronous.consumed
            want_ids, want_targets = stage_original_rows(original)
            assert torch.equal(ids, want_ids) and torch.equal(targets, want_targets)
            if queued.future is not None:
                queued.future.result(timeout=5)
                # Source may be ahead; checkpoint MUST remain on consumed rows.
                assert equal_state(queued.state_dict(), synchronous.state_dict())
        assert torch.equal(before, torch.get_rng_state())
    synchronous.handle.close()


def test_restore_discards_already_prepared_batch_and_reproduces_without_skip_or_duplicate(tmp_path):
    synchronous, source = sources(tmp_path)
    with PrefetchedOriginalSampler(source, 6) as queued:
        queued.take(6)
        synchronous.take(6)
        saved = queued.state_dict()
        queued.future.result(timeout=5)
        advanced = source.state_dict()
        assert not equal_state(saved, advanced)
        queued.take(6)
        queued.load_state_dict(saved)
        assert equal_state(queued.state_dict(), saved)
        for _ in range(4):
            assert equal_state(queued.take(6), synchronous.take(6))
            assert equal_state(queued.state_dict(), synchronous.state_dict())
    synchronous.handle.close()


def test_producer_failure_propagates_without_changing_last_logical_state_and_load_recovers(tmp_path):
    synchronous, source = sources(tmp_path)
    take = source.take
    source.take = lambda _: (_ for _ in ()).throw(RuntimeError('explicit producer failure'))
    with PrefetchedOriginalSampler(source, 6) as queued:
        before = queued.state_dict()
        with pytest.raises(RuntimeError, match='producer failure'): queued.take(6)
        assert equal_state(before, queued.state_dict())
        with pytest.raises(ValueError): queued.take(6)
        source.take = take
        queued.load_state_dict(before)
        assert equal_state(queued.take(6), synchronous.take(6))
    synchronous.handle.close()


def test_depth_one_and_checkpoint_does_not_wait_for_speculative_next_rows(tmp_path):
    synchronous, source = sources(tmp_path)
    take = source.take
    started, release = threading.Event(), threading.Event()
    calls = []
    def bounded(size):
        calls.append(size)
        if len(calls) == 2:
            started.set()
            if not release.wait(timeout=5): raise RuntimeError('test failed to release producer')
        return take(size)
    source.take = bounded
    queued = PrefetchedOriginalSampler(source, 6)
    try:
        queued.take(6)
        synchronous.take(6)
        assert started.wait(timeout=5)
        assert calls == [6, 6]
        assert equal_state(queued.state_dict(), synchronous.state_dict())
        assert not queued.future.done()
    finally:
        release.set()
        queued.close()
        synchronous.handle.close()
    assert source.handle.closed and queued.closed and queued.executor is None
    with pytest.raises(ValueError): queued.take(6)


def test_end_of_original_quota_no_overdraw_or_foreign_batch_and_no_state_alias(tmp_path):
    synchronous, source = sources(tmp_path)
    # Explicit fixture-only small exact source goals; real science keeps100M.
    source.goals = synchronous.goals = dict(web=70, textbook=24, story=12)
    with PrefetchedOriginalSampler(source, 6) as queued:
        with pytest.raises(ValueError): queued.take(3)
        while not synchronous.exhausted:
            assert equal_state(queued.take(6), synchronous.take(6))
        assert queued.exhausted and queued.future is None
        assert equal_state(queued.state_dict(), synchronous.state_dict())
        saved = queued.state_dict()
        saved['consumed']['web'] = 0
        assert queued.consumed['web'] == 70
        with pytest.raises(ValueError): queued.take(6)
    synchronous.handle.close()
