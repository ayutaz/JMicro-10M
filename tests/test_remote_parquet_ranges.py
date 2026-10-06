import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import pyarrow as pa
import pyarrow.parquet as pq
import pytest
from remote_parquet_ranges import RangeBudget, RangeFile


def opener_for(data, calls, status=206):
    def opener(request, timeout):
        start, end = map(int, request.headers['Range'].removeprefix('bytes=').split('-'))
        calls.append((start, end + 1))
        response = io.BytesIO(data[start:end+1])
        response.status = status
        response.headers = {'Content-Range': f'bytes {start}-{end}/{len(data)}'}
        return response
    return opener


def test_seek_cache_and_remote_ceiling():
    calls = []
    budget = RangeBudget(5, 10, opener_for(b'abcdefghij', calls))
    stream = RangeFile('https://example.invalid/pinned', 10, budget)
    assert stream.read(4) == b'abcd'
    stream.seek(1)
    assert stream.read(2) == b'bc' and len(calls) == 1
    stream.seek(-3, io.SEEK_END)
    with pytest.raises(ValueError, match='ceiling'):
        stream.read(3)
    assert len(calls) == 1 and budget.bytes == 4


def test_ignored_range_rejected_before_body_read():
    class Response:
        status = 200
        headers = {}
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def read(self, count): raise AssertionError('Ignored range body must not be read')
    budget = RangeBudget(100, 10, lambda *args, **kwargs: Response())
    with pytest.raises(ValueError, match='exact pinned'):
        RangeFile('https://example.invalid/pinned', 100, budget).read(4)
    assert budget.bytes == 0


def test_real_parquet_selected_column_skips_large_embedding():
    sink = io.BytesIO()
    # Large uncompressed field makes the footer read separate from embedding chunks.
    table = pa.table({'text': ['source A', 'source B'], 'embeddings': [b'a'*200000, b'b'*200000]})
    pq.write_table(table, sink, compression=None, use_dictionary=False, write_statistics=False)
    data = sink.getvalue(); calls = []
    budget = RangeBudget(100000, 10, opener_for(data, calls))
    parquet = pq.ParquetFile(RangeFile('https://example.invalid/pinned', len(data), budget), pre_buffer=False)
    assert parquet.read_row_group(0, columns=['text']).to_pydict() == {'text': ['source A', 'source B']}
    column = parquet.metadata.row_group(0).column(1)
    start, end = column.data_page_offset, column.data_page_offset + column.total_compressed_size
    assert not any(a <= start and end <= b for a,b in calls)
    assert budget.bytes < 100000
