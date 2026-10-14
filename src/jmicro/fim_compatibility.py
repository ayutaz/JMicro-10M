"""CPU-only FIM serialization feasibility; no learning recipe or file readers.

The fixed vocabulary has no FIM structural IDs. Ordinary body-encoded markers
are an explicit deviation from the paper, never a reuse of dialogue role IDs.
This checks conservation/context costs, not that FIM improves Base generation.
"""
import codecs
from dataclasses import dataclass
import hashlib

MARKERS = ('[FIM_PREFIX]', '[FIM_SUFFIX]', '[FIM_MIDDLE]')


@dataclass(frozen=True)
class FimSerialization:
    ids: tuple[int, ...]
    original_positions: tuple[int | None, ...]
    original_body_sha256: str
    cuts: tuple[int, int]
    original_body_tokens: int
    marker_tokens: int


def utf8_token_boundaries(body, codec):
    """Token endpoints at complete Unicode characters, without retokenizing.

    SentencePiece pieces can be individually valid, whereas byte-fallback
    tokens can end partway through a Japanese character. A strict incremental
    decoder checks the actual concatenated bytes and disallows such cuts.
    """
    if not body or any(type(i) is not int or not 8 <= i < codec.vocab_size for i in body):
        raise ValueError('Nonempty plain original body IDs required')
    decoder = codecs.getincrementaldecoder('utf-8')('strict')
    endpoints = [0]
    for n, token in enumerate(body, 1):
        decoder.decode(codec.decode_bytes([token]), final=False)
        if not decoder.getstate()[0]:
            endpoints.append(n)
    decoder.decode(b'', final=True)
    return tuple(endpoints)


def serialize_psm(body, codec, cuts, context=1024):
    """PSM with full original gold identities retained and one terminal EOS.

    No chopping, invented document EOS, automatic fallback or span retokenizing.
    Gold/loss masks are deliberately not defined: whether to supervise marker
    tokens is a scientific decision to freeze in a future comparison contract.
    EOS ends the reconstructed middle here, not the original document suffix.
    """
    boundaries = utf8_token_boundaries(body, codec)
    if (type(context) is not int or context < 2 or len(cuts) != 2
            or any(type(c) is not int for c in cuts)):
        raise ValueError('Explicit integer cuts and positive context required')
    left, right = cuts
    if not 0 <= left < right <= len(body) or left not in boundaries or right not in boundaries:
        raise ValueError('Nonempty middle with codec-stable cuts required')
    raw = codec.decode_bytes(body)
    text = raw.decode('utf-8')
    if any(marker in text for marker in MARKERS):
        raise ValueError('Original body collides with a literal FIM marker')
    marker_ids = [codec.encode(marker) for marker in MARKERS]
    if any(not m or any(type(i) is not int or not 8 <= i < codec.vocab_size for i in m)
            or codec.decode_bytes(m) != spelling.encode('utf-8')
            for m, spelling in zip(marker_ids, MARKERS)):
        raise ValueError('Markers must round-trip as ordinary body tokens')
    ids, origin = [2], [None]
    for marker, start, end in zip(marker_ids, (0, right, left), (left, len(body), right)):
        ids.extend(marker); origin.extend([None] * len(marker))
        ids.extend(body[start:end]); origin.extend(range(start, end))
    ids.append(3); origin.append(len(body))
    # The model input is serialized[:-1]; its single final label is EOS.
    if len(ids) - 1 > context:
        raise ValueError('Full FIM unit exceeds context; no silent trim or pad')
    return FimSerialization(tuple(ids), tuple(origin), hashlib.sha256(raw).hexdigest(),
                            (left, right), len(body), sum(map(len, marker_ids)))


def restore_original(serialization):
    pairs = [(position, token) for position, token in
             zip(serialization.original_positions, serialization.ids) if position is not None]
    if (len(serialization.ids) != len(serialization.original_positions)
            or sorted(p for p, _ in pairs) != list(range(serialization.original_body_tokens + 1))
            or pairs[-1] != (serialization.original_body_tokens, 3)):
        raise ValueError('Original position identity/EOS conservation differs')
    return [token for _, token in sorted(pairs)]
