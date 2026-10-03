import numpy as np
import pytest

from jmicro.repetition_diagnosis import consumed_targets, paired_transitions, target_block_counts


def test_boundary_targets_and_incomplete_tail():
    # Position 0 is never a teacher; position context is taught by block 0.
    counts = target_block_counts([0, 1, 4, 5, 8, 9], blocks=2, context=4)
    assert counts.tolist() == [2, 2]
    sampler = {'blocks': 2, 'position': 1, 'epoch': 3, 'seed': 42}
    assert consumed_targets(counts, sampler) == 14


def test_replay_matches_explicit_multiepoch_sampler():
    counts = np.arange(13)
    seed, epoch, position = 7, 2, 5
    explicit = []
    for e in range(epoch+1):
        order = np.random.default_rng(np.random.SeedSequence([seed, e])).permutation(13)
        explicit.extend(order if e < epoch else order[:position])
    assert consumed_targets(counts, dict(blocks=13, seed=seed, epoch=epoch, position=position)) == sum(counts[i] for i in explicit)


def test_paired_failures_preserve_resolved_cases_and_reject_mismatch():
    rows = [dict(id=str(i), decoding='greedy', suppressed=True, seed=42, repetition=bool(i%2)) for i in range(4)]
    other = [{**row, 'repetition': i < 2} for i, row in enumerate(rows)]
    result = paired_transitions(rows, other)['greedy-suppressed1']
    assert [result[k] for k in ('neither', 'new_only', 'old_only', 'both')] == [1, 1, 1, 1]
    with pytest.raises(ValueError):
        paired_transitions(rows, other[:-1])
