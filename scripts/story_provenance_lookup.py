"""Bounded byte-seek lookup in builder's immutable offset-sorted JSONL index."""
import json


class Reader:
    def __init__(self, stream, byte_limit=8*1024*1024, line_limit=16384):
        self.stream, self.byte_limit, self.line_limit = stream, byte_limit, line_limit
        self.bytes_read = 0

    def line(self):
        raw = self.stream.readline(self.line_limit+1)
        self.bytes_read += len(raw)
        if self.bytes_read > self.byte_limit: raise ValueError('Bounded index byte budget exhausted')
        if len(raw) > self.line_limit: raise ValueError('Index line exceeds bounded lookup limit')
        return raw


def lookup(reader, offset, file_size):
    """Requires the recorded builder's sorted unique integer offset contract."""
    if type(offset) is not int or offset < 0 or file_size <= 0:
        raise ValueError('Positive original index and nonnegative integer offset required')
    stream = reader.stream; low, high = 0, file_size
    while high-low > reader.line_limit:
        middle = (low+high)//2; stream.seek(middle)
        if middle: reader.line()  # skip partial record without decoding UTF-8 fragments
        start = stream.tell(); raw = reader.line()
        if not raw:
            high = middle; continue
        row = json.loads(raw)
        current = row['offset']
        if type(current) is not int: raise ValueError('Original offset must be integer')
        if current == offset: return row
        if current < offset: low = start
        else: high = middle
    stream.seek(low)
    while True:
        raw = reader.line()
        if not raw: break
        row = json.loads(raw)
        if row['offset'] == offset: return row
        if row['offset'] > offset: break
    raise ValueError('Requested original offset absent; no approximate record substitution')
