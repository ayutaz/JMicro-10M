"""Bounded binary JSONL position diagnostics; no dataset or model imports.

Historical samplers stay frozen. These helpers distinguish the containing
record from their actual next-record mapping, including the special byte zero.
"""

MAX_RECORD_BYTES = 16384


def containing_record(handle, position, size, limit=MAX_RECORD_BYTES):
    """Return (start, original line) containing the byte, including its LF.

    At an exact record start return that record, not its successor. Refuse a
    line exceeding the frozen bound rather than scanning an unbounded prefix.
    """
    if (type(position) is not int or type(size) is not int
            or not 0 <= position < size or type(limit) is not int or limit < 1):
        raise ValueError('An in-range byte position and positive bound are required')
    left = max(0, position - limit)
    handle.seek(left)
    prefix = handle.read(position - left)
    if len(prefix) != position - left:
        raise ValueError('Index changed or short read')
    newline = prefix.rfind(b'\n')
    if newline >= 0:
        start = left + newline + 1
    elif left == 0:
        start = 0
    else:
        raise ValueError('Containing record exceeds the bounded prefix')
    handle.seek(start)
    raw = handle.readline(limit + 1)
    if (not raw or len(raw) > limit or not raw.endswith(b'\n')
            or not start <= position < start + len(raw)
            or start + len(raw) > size):
        raise ValueError('Bounded, LF-terminated containing record is required')
    return start, raw


def legacy_next_record(handle, position, size, limit=MAX_RECORD_BYTES):
    """Mirror the two frozen samplers' seek/skip/read, without JSON parsing.

    (size, b'') is a terminal rejection, not a wrap to the first record.
    """
    if type(position) is not int or not 0 <= position < size:
        raise ValueError('An in-range byte position is required')
    handle.seek(position)
    if position:
        handle.readline(limit)
    start = handle.tell()
    return start, handle.readline(limit + 1)


def legacy_record_weight(handle, start, size, limit=MAX_RECORD_BYTES):
    """Number of byte positions mapping to this record before genre rejection.

    First record: one byte. Second record: first line length minus one.
    Later records: preceding line length. Final line bytes map to EOF.
    """
    if start == 0:
        return 1
    previous_start, previous_raw = containing_record(handle, start - 1, size, limit)
    if previous_start + len(previous_raw) != start:
        raise ValueError('An exact record start is required')
    return len(previous_raw) - int(previous_start == 0)
