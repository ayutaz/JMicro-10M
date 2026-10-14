"""Serialization, byte conservation and budget limits; no quality claims."""
from dataclasses import replace
import hashlib
import pytest
from jmicro.fim_compatibility import MARKERS, restore_original, serialize_psm, utf8_token_boundaries


class ByteCodec:
    vocab_size = 264
    def encode(self, text): return [b + 8 for b in text.encode('utf-8')]
    def decode_bytes(self, ids): return bytes(i - 8 for i in ids)


def test_japanese_cuts_cannot_split_fallback_bytes():
    c = ByteCodec(); body = c.encode('朝、雨が降る。')
    ends = utf8_token_boundaries(body, c)
    assert ends == tuple(range(0, len(body) + 1, 3))
    with pytest.raises(ValueError, match='codec-stable'):
        serialize_psm(body, c, (1, 6))
    result = serialize_psm(body, c, (3, 15))
    assert restore_original(result) == body + [3]
    assert result.original_body_sha256 == hashlib.sha256('朝、雨が降る。'.encode()).hexdigest()
    # Assert human-readable order independently of the origin reconstruction.
    content = c.decode_bytes(result.ids[1:-1]).decode()
    assert content == '[FIM_PREFIX]朝[FIM_SUFFIX]る。[FIM_MIDDLE]、雨が降'
    assert len(result.ids) == len(body) + result.marker_tokens + 2
    assert result.ids.count(3) == 1 and not any(i in (4, 5, 6, 7) for i in result.ids)


@pytest.mark.parametrize('cuts', [(0, 3), (3, 6), (0, 6)])
def test_empty_edges_are_allowed_but_middle_is_original_nonempty(cuts):
    c = ByteCodec(); body = c.encode('あい')
    result = serialize_psm(body, c, cuts)
    assert restore_original(result) == body + [3]


@pytest.mark.parametrize('cuts', [(3, 3), (-1, 3), (3, 9), (6, 3), (True, 3)])
def test_bad_cuts_rejected(cuts):
    with pytest.raises(ValueError): serialize_psm(ByteCodec().encode('あい'), ByteCodec(), cuts)


@pytest.mark.parametrize('body', [[], [3, 9], [264], [True], [8 + 0xe3], [8 + 0xff]])
def test_nonbody_and_invalid_or_truncated_utf8_rejected(body):
    with pytest.raises((ValueError, UnicodeDecodeError)):
        utf8_token_boundaries(body, ByteCodec())


@pytest.mark.parametrize('marker', MARKERS)
def test_literal_collision_is_not_escaped_or_silently_reencoded(marker):
    c = ByteCodec(); body = c.encode('文' + marker + '末')
    with pytest.raises(ValueError, match='collides'): serialize_psm(body, c, (0, 3))


def test_context_budget_includes_all_marker_inputs_and_preserves_terminal_eos():
    c = ByteCodec(); body = c.encode('甲乙')
    result = serialize_psm(body, c, (0, 3))
    size = len(result.ids) - 1
    assert serialize_psm(body, c, (0, 3), context=size) == result
    with pytest.raises(ValueError, match='exceeds'): serialize_psm(body, c, (0, 3), context=size - 1)
    damaged = replace(result, original_positions=result.original_positions[:-1] + (0,))
    with pytest.raises(ValueError, match='conservation'): restore_original(damaged)


def test_bad_marker_codec_rejected():
    class Bad(ByteCodec):
        def encode(self, text): return [4]
    with pytest.raises(ValueError, match='ordinary body'):
        serialize_psm(ByteCodec().encode('甲乙'), Bad(), (0, 3))
