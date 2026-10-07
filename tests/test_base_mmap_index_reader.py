"""Byte-boundary and original full-sampler parity; no corpus or GPU scan."""
import io
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from base_mmap_index_reader import MMapIndexReader, mapped_sampler
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec


@pytest.mark.parametrize('data', [b'', b'abc', b'\nA\n\nB', b'A'*16384+b'\nB'*3,
                                  '日本語\r\n索引\n末尾'.encode()])
def test_bounded_binary_readline_seek_and_eof_match_independent_bytesio(tmp_path, data):
    path = tmp_path / 'index'; path.write_bytes(data)
    reference = io.BytesIO(data)
    with MMapIndexReader(path) as actual:
        for position in (0, 1, 3, 16383, 16384, len(data), len(data)+8):
            for size in (0, 1, 2, 17, 16384, 16385, -1):
                assert actual.seek(position) == reference.seek(position)
                assert actual.readline(size) == reference.readline(size)
                assert actual.tell() == reference.tell()
        actual.seek(0); reference.seek(0)
        assert actual.seek(2, 1) == reference.seek(2, 1)
        assert actual.seek(-1 if data else 0, 2) == reference.seek(-1 if data else 0, 2)
        assert actual.readline() == reference.readline()
        with pytest.raises(ValueError): actual.seek(-1)
        with pytest.raises(ValueError): actual.seek(0, 3)
        with pytest.raises(TypeError): actual.readline(1.5)
        if data:
            with pytest.raises(TypeError): actual.mapping[0] = 0
    assert path.read_bytes() == data
    with pytest.raises(ValueError): actual.readline()
    with pytest.raises(ValueError): actual.tell()
    actual.close()  # idempotent close


def test_every_original_row_and_full_sampler_state_match_to_exact_goals(tmp_path):
    pool = tmp_path / 'pool'; manifest = fixture_pool(pool)
    goals = dict(web=1300, textbook=300, story=120)
    args = (pool, manifest, FixtureCodec(), goals)
    original, mapped = CEOnlyOriginalSampler(*args), mapped_sampler(*args)
    try:
        while not original.exhausted:
            assert equal_state(original.take(4), mapped.take(4))
            assert equal_state(original.state_dict(), mapped.state_dict())
        assert mapped.consumed == goals
    finally:
        original.handle.close(); mapped.handle.close()


@pytest.mark.parametrize('direction', ['original_to_mapped', 'mapped_to_original'])
def test_resume_across_reader_types_preserves_pending_windows_rng_and_next_batches(tmp_path, direction):
    pool = tmp_path / 'pool'; manifest = fixture_pool(pool)
    args = (pool, manifest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
    constructors = (CEOnlyOriginalSampler, mapped_sampler)
    if direction == 'mapped_to_original':
        constructors = constructors[::-1]
    a, b = (make(*args) for make in constructors)
    try:
        a.take(4); a.take(4)
        b.load_state_dict(a.state_dict())
        for _ in range(4):
            assert equal_state(a.take(4), b.take(4))
            assert equal_state(a.state_dict(), b.state_dict())
    finally:
        a.handle.close(); b.handle.close()
