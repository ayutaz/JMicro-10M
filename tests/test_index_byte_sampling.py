"""Exact finite-position probabilities and a real frozen sampler regression."""
from collections import Counter
import hashlib
from io import BytesIO
import json
from pathlib import Path
import sys

import numpy as np
import pytest

from jmicro.index_byte_sampling import (
    containing_record, legacy_next_record, legacy_record_weight)


def test_every_byte_has_its_own_record_including_LF_and_exact_starts():
    lines = [b'{"id":1}\n', b'{"id":"longer"}\n', b'{"id":3}\n']
    data = b''.join(lines)
    counts = Counter(containing_record(BytesIO(data), p, len(data))[0]
                     for p in range(len(data)))
    assert list(counts.values()) == list(map(len, lines))
    for start in (0, len(lines[0]), len(lines[0]) + len(lines[1])):
        assert containing_record(BytesIO(data), start, len(data))[0] == start


@pytest.mark.parametrize('lines', [
    [b'{}\n'], [b'{}\n', b'{"long":"abcdefgh"}\n'],
    [b'{"id":1}\r\n', b'{}\r\n', b'{"id":33333}\r\n']])
def test_legacy_exact_probability_mass_and_terminal_rejections(lines):
    data = b''.join(lines)
    starts = [sum(map(len, lines[:i])) for i in range(len(lines))]
    counts = Counter(legacy_next_record(BytesIO(data), p, len(data))[0]
                     for p in range(len(data)))
    assert [counts[s] for s in starts] == [
        legacy_record_weight(BytesIO(data), s, len(data)) for s in starts]
    expected_eof = len(lines[-1]) - int(len(lines) == 1)
    assert counts[len(data)] == expected_eof
    assert sum(counts.values()) == len(data)


def test_changing_preceding_metadata_changes_legacy_selection_probability():
    target = b'{"id":2}\n'
    first = b'{"id":1}\n'
    longer = b'{"id":1,"metadata":"unrelated-padding"}\n'
    assert legacy_record_weight(BytesIO(first + target), len(first), len(first + target)) == len(first) - 1
    assert legacy_record_weight(BytesIO(longer + target), len(longer), len(longer + target)) == len(longer) - 1
    assert len(containing_record(BytesIO(first + target), len(first), len(first + target))[1]) == len(target)


@pytest.mark.parametrize('position', [-1, 6, True])
def test_reject_invalid_positions(position):
    with pytest.raises(ValueError):
        containing_record(BytesIO(b'{}\n{}\n'), position, 6)


def test_oversize_truncated_and_unterminated_inputs_fail_closed():
    for data, position in ((b'A' * 20 + b'\n', 15), (b'{}', 1)):
        with pytest.raises(ValueError):
            containing_record(BytesIO(data), position, len(data), limit=8)
    with pytest.raises(ValueError):
        containing_record(BytesIO(b'{}\n'), 4, 8)
    with pytest.raises(ValueError):
        legacy_record_weight(BytesIO(b'{}\n{}\n'), 4, 6)


def test_bounded_reads_do_not_scan_full_index():
    class Counting(BytesIO):
        read_bytes = 0
        def read(self, n):
            assert 0 <= n <= 8
            data = super().read(n)
            self.read_bytes += len(data)
            return data
        def readline(self, n):
            assert n == 9
            data = super().readline(n)
            self.read_bytes += len(data)
            return data
    data = b'{}\n' * 100000
    h = Counting(data)
    assert containing_record(h, 270001, len(data), limit=8) == (270000, b'{}\n')
    assert h.read_bytes <= 17


def test_real_frozen_CE_sampler_selects_successor_at_record_start(tmp_path):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
    from base_kv_allocation_trainer import CEOnlyOriginalSampler
    from jmicro.experiment import sha256

    class Codec:
        vocab_size = 128
        def decode_bytes(self, ids):
            return bytes(i for i in ids if i >= 8)

    pool = tmp_path / 'pool'
    pool.mkdir()
    tokens, lines = [], []
    for i in range(3):
        body = [65 + i] * (i + 2)
        record = dict(source='web', split='train', source_family=f'fixture-{i}',
                      canonical_sha256=hashlib.sha256(bytes(body)).hexdigest(),
                      body_tokens=len(body), offset=len(tokens))
        tokens.extend([2] + body + [3])
        lines.append((json.dumps(record) + '\n').encode())
    data = b''.join(lines)
    (pool / 'train.index.jsonl').write_bytes(data)
    np.array(tokens, dtype='<u2').tofile(pool / 'train.bin')
    (pool / 'manifest.json').write_text(json.dumps(dict(splits=dict(train=dict(
        tokens=len(tokens), index_sha256=sha256(pool / 'train.index.jsonl'))))))
    manifest_pin = sha256(pool / 'manifest.json')
    stat = (pool / 'train.index.jsonl').stat()
    cache = pool / ('.compact-index-' + manifest_pin[:16])
    cache.mkdir()
    (cache / 'ready.json').write_text(json.dumps(dict(source_hash_verified_during_single_parse=True,
        binding=dict(manifest_sha256=manifest_pin, index_sha256=sha256(pool / 'train.index.jsonl'),
                     index_size=stat.st_size, index_mtime_ns=stat.st_mtime_ns))))
    sampler = CEOnlyOriginalSampler(pool, manifest_pin, Codec(), dict(web=100, textbook=20, story=10))
    class Position:
        def __init__(self, value):
            self.value = value
        def randrange(self, size):
            assert size == len(data)
            return self.value
    try:
        for position in (0, 1, len(lines[0]) - 1, len(lines[0]),
                         len(lines[0]) + len(lines[1]) - 1):
            sampler.rng = Position(position)
            sampler._draw_document('web')
            expected_start, expected_raw = legacy_next_record(BytesIO(data), position, len(data))
            row = sampler.pending['web'][0]
            assert row['index_byte_position'] == expected_start
            assert row['index_record_sha256'] == hashlib.sha256(expected_raw).hexdigest()
        last_start = len(lines[0]) + len(lines[1])
        sampler.rng = Position(last_start)
        with pytest.raises(RuntimeError, match='Fixed4096'):
            sampler._draw_document('web')
    finally:
        sampler.handle.close()
