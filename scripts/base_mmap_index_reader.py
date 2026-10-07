"""Read-only bounded-line adapter; original byte-index sampling is unchanged."""
import mmap
import operator
from pathlib import Path

from base_kv_allocation_trainer import CEOnlyOriginalSampler


class MMapIndexReader:
    """Binary seek/tell/readline semantics, including the caller's byte limit."""
    def __init__(self, path):
        self.file = Path(path).open('rb')
        self.size = Path(path).stat().st_size
        self.mapping = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ) if self.size else None
        self.position = 0
        self.closed = False

    def _open(self):
        if self.closed:
            raise ValueError('I/O operation on closed index reader')

    def seek(self, offset, whence=0):
        self._open()
        offset, whence = operator.index(offset), operator.index(whence)
        if whence not in (0, 1, 2):
            raise ValueError('Unsupported seek origin')
        position = offset + (0 if whence == 0 else self.position if whence == 1 else self.size)
        if position < 0:
            raise ValueError('Negative seek position')
        self.position = position
        return position

    def tell(self):
        self._open()
        return self.position

    def readline(self, size=-1):
        self._open()
        size = -1 if size is None else operator.index(size)
        if size == 0 or self.position >= self.size:
            return b''
        end = self.size if size < 0 else min(self.size, self.position + size)
        newline = self.mapping.find(b'\n', self.position, end)
        if newline != -1:
            end = newline + 1
        result = self.mapping[self.position:end]
        self.position = end
        return result

    def close(self):
        if not self.closed:
            if self.mapping is not None:
                self.mapping.close()
            self.file.close()
            self.closed = True

    def __enter__(self):
        self._open()
        return self

    def __exit__(self, *args):
        self.close()


def mapped_sampler(*args, **kwargs):
    """Replace only the reader after the existing source binding validation."""
    sampler = CEOnlyOriginalSampler(*args, **kwargs)
    old = sampler.handle
    try:
        reader = MMapIndexReader(sampler.index)
        reader.seek(old.tell())
    except BaseException:
        old.close()
        raise
    old.close()
    sampler.handle = reader
    return sampler
