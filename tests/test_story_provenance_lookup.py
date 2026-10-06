"""Seek boundaries and byte caps protect exact metadata without whole scan."""
import io
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import pytest
from story_provenance_lookup import Reader, lookup


def test_first_middle_last_utf8_records_and_exact_missing_key():
    rows = [dict(offset=i*97, text='日本語の原文。'+('あ'*((i%13)+1))) for i in range(5000)]
    raw = b''.join(json.dumps(r, ensure_ascii=False).encode('utf-8')+b'\n' for r in rows)
    reader = Reader(io.BytesIO(raw), byte_limit=200000, line_limit=256)
    for i in (0, 1, 2417, 4998, 4999): assert lookup(reader, i*97, len(raw)) == rows[i]
    with pytest.raises(ValueError, match='absent'): lookup(reader, 2417*97+1, len(raw))
    assert reader.bytes_read < len(raw)//10


def test_no_unbounded_scan_long_line_or_approximate_substitution():
    raw = b'{"offset":0,"text":"'+b'x'*2000+b'"}\n'
    with pytest.raises(ValueError, match='line exceeds'):
        lookup(Reader(io.BytesIO(raw), line_limit=64), 0, len(raw))
    raw = b''.join(json.dumps(dict(offset=i)).encode()+b'\n' for i in range(100))
    with pytest.raises(ValueError, match='byte budget'):
        lookup(Reader(io.BytesIO(raw), byte_limit=10), 99, len(raw))
    with pytest.raises(ValueError, match='nonnegative integer'):
        lookup(Reader(io.BytesIO(raw)), True, len(raw))
