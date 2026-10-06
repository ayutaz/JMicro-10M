import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_condition_positive_teachers import outcome_token_mask


class ByteTokenizer:
    def __init__(self, pieces):
        self.pieces = pieces

    def decode_bytes(self, ids):
        return b''.join(self.pieces[i] for i in ids)


def test_multibyte_outcome_and_sentence_end_keep_structural_ids_unboosted():
    text = '前後。'
    tok = ByteTokenizer({8: '前'.encode(), 9: '後'.encode()[:1],
                         10: '後'.encode()[1:], 11: '。'.encode()})
    mask = outcome_token_mask(text, [8, 9, 10, 11], tok, [dict(cut=1, end=3)])
    assert mask.tolist() == [0, 0, 1, 1, 1, 0]


def test_original_piece_straddling_byte_cut_uses_declared_overlap_policy():
    tok = ByteTokenizer({8: '前後'.encode(), 9: '。'.encode()})
    mask = outcome_token_mask('前後。', [8, 9], tok, [dict(cut=1, end=2)])
    assert mask.tolist() == [0, 1, 0, 0]
