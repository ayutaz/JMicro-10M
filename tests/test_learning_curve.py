import copy
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from jmicro.learning_curve import MilestoneMixture, LazyDocumentBlocks, curve_lr
from jmicro.packing_study import ShuffledDocumentBlocks
from jmicro.shards import BlockSampler


def shard():
    ids = [2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 3]
    return SimpleNamespace(split="train", tokens=np.asarray(ids * 1024, dtype="<u2"),
        index=[dict(offset=i*len(ids), body_tokens=len(ids)-2) for i in range(1024)],
        byte_lengths=np.asarray([0]*8+[1]*4088))


def test_boundaries_complete_updates_exact_teachers_and_resume_cursor():
    source = shard()
    parent = BlockSampler(source, 1024, 42).state_dict()
    continuous = MilestoneMixture(source, source, parent, [5, 12, 25])
    x, y, _ = continuous.batch(1)
    assert y.ne(-100).sum() == 5 and x.numel() == 1024
    assert continuous.source_teachers["short"] == 5
    saved = copy.deepcopy(continuous.state_dict())
    resumed = MilestoneMixture(source, source, parent, [5, 12, 25])
    resumed.load_state_dict(saved)
    for target, count in [(12, 7), (25, 13)]:
        a, b = continuous.batch(1), resumed.batch(1)
        assert a[1].ne(-100).sum() == count
        assert torch.equal(a[0], b[0]) and torch.equal(a[1], b[1]) and a[2] == b[2]
        assert continuous.source_teachers["short"] == target
        assert continuous.state_dict() == resumed.state_dict()
    assert continuous.source_tokens["short"] == continuous.source_physical_tokens["short"] == 3072
    with pytest.raises(ValueError, match="exhausted"):
        continuous.batch(1)
    with pytest.raises(ValueError, match="differ"):
        MilestoneMixture(source, source, parent, [5, 13, 25]).load_state_dict(saved)


def test_stable_lr_has_no_terminal_decay_and_equal_decay_branches():
    peak = .002
    assert all(curve_lr(n, peak) == peak for n in (0, 100000000, 500000000, 1000000000, 2000000000))
    # Every checkpoint receives the same20M decay, independent of parent age.
    expected = [peak, peak * .55, peak * .1]
    assert [curve_lr(n, peak, "decay", 20000000) for n in (0, 10000000, 20000000)] == expected
    with pytest.raises(ValueError):
        curve_lr(1, peak, "decay", 0)


def test_lazy_document_shuffle_matches_legacy_across_epochs_and_resume():
    source = shard()
    lazy, old = LazyDocumentBlocks(source,1024,42), ShuffledDocumentBlocks(source,1024,42)
    # Three batches cross the epoch boundary, including a saved mid-epoch cursor.
    for _ in range(3):
        a, b = lazy.batch(8), old.batch(8)
        assert torch.equal(a[0],b[0]) and torch.equal(a[1],b[1]) and a[2] == b[2]
    saved = lazy.state_dict()
    restored = LazyDocumentBlocks(source,1024,42); restored.load_state_dict(saved)
    a,b = lazy.batch(8),restored.batch(8)
    assert torch.equal(a[0],b[0]) and torch.equal(a[1],b[1]) and a[2] == b[2]
    assert lazy.state_dict() == restored.state_dict()
