"""Display complete UTF8 characters without changing raw generation evidence."""
import codecs


def decode_display(raw: bytes, stop_reason: str) -> dict:
    legacy = raw.decode('utf-8', errors='replace')
    decoder = codecs.getincrementaldecoder('utf-8')(errors='strict')
    error = None
    try:
        visible = decoder.decode(raw, final=False)
        pending, _ = decoder.getstate()
        raw_valid = not pending
        truncated = bool(pending) and stop_reason == 'max_new_tokens'
        if pending and not truncated:
            decoder.decode(b'', final=True)
    except UnicodeDecodeError as exc:
        # Only an incomplete cap-tail may be omitted; other failures stay explicit.
        visible, pending, raw_valid, truncated = legacy, b'', False, False
        error = {'reason': exc.reason, 'start': exc.start, 'end': exc.end}
    return {'text': visible, 'display_text': visible, 'raw_text': legacy,
            'valid_utf8': raw_valid, 'raw_valid_utf8': raw_valid,
            'truncated_utf8_tail': truncated, 'pending_utf8_bytes_hex': pending.hex(),
            'utf8_error': error}
