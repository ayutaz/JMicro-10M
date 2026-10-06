"""Strict, bounded HTTP ranges for selected Parquet columns, with no credentials."""
import io
import re
import time
import urllib.request


class RangeBudget:
    def __init__(self, maximum_bytes, seconds, opener=None):
        self.maximum_bytes = maximum_bytes
        self.deadline = time.monotonic() + seconds
        self.bytes = 0
        self.requests = 0
        self.opener = opener or urllib.request.urlopen

    def fetch(self, url, start, length, size):
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError('Bounded remote retrieval deadline exhausted')
        if length <= 0 or start < 0 or start + length > size:
            raise ValueError('Invalid bounded range')
        if self.bytes + length > self.maximum_bytes:
            raise ValueError('Remote byte ceiling exhausted before request')
        request = urllib.request.Request(url, headers={
            'Range': f'bytes={start}-{start + length - 1}',
            'User-Agent': 'JMicro-10M bounded local Base source inspection'})
        self.requests += 1
        with self.opener(request, timeout=min(15, remaining)) as response:
            expected = f'bytes {start}-{start + length - 1}/{size}'
            # Reject an ignored/incorrect range BEFORE reading any large body.
            if response.status != 206 or response.headers.get('Content-Range') != expected:
                raise ValueError('Server did not return the exact pinned file range')
            result = response.read(length)
            self.bytes += len(result)
            if len(result) != length:
                raise ValueError('Truncated remote range')
        if time.monotonic() > self.deadline:
            raise TimeoutError('Remote retrieval deadline exceeded')
        return result


class RangeFile(io.RawIOBase):
    def __init__(self, url, size, budget):
        super().__init__()
        self.url, self.size, self.budget = url, size, budget
        self.position = 0
        self.cache = []

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.position

    def seek(self, offset, whence=io.SEEK_SET):
        origin = {io.SEEK_SET: 0, io.SEEK_CUR: self.position, io.SEEK_END: self.size}
        if whence not in origin or origin[whence] + offset < 0:
            raise ValueError('Invalid seek')
        self.position = origin[whence] + offset
        return self.position

    def read(self, length=-1):
        if self.closed:
            raise ValueError('Closed range file')
        length = min(self.size - self.position, length if length >= 0 else self.size)
        if length <= 0:
            return b''
        start = self.position
        for offset, content in self.cache:
            if offset <= start and start + length <= offset + len(content):
                result = content[start - offset:start - offset + length]
                self.position += length
                return result
        result = self.budget.fetch(self.url, start, length, self.size)
        self.cache.append((start, result))
        self.position += length
        return result


def observed_size(content_range):
    match = re.fullmatch(r'bytes 0-3/(\d+)', content_range or '')
    if not match:
        raise ValueError('Exact observed header range required')
    return int(match.group(1))
