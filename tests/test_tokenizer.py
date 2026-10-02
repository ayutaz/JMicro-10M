from pathlib import Path
import random
import pytest
from jmicro.tokenizer import Tokenizer
from jmicro.phase2 import golden_cases

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(params=[4096, 8192])
def tok(request):
    path = ROOT / f"artifacts/phase2/{request.param}/tokenizer.model"
    if not path.exists():
        pytest.skip("Run prepare_phase2.py to create tokenizer artifacts")
    return Tokenizer(path)


def test_lossless_contract_and_literal_structure(tok):
    for case in golden_cases():
        ids = tok.encode(case["input"])
        assert tok.decode(ids) == case["canonical"]
        assert all(i >= 8 for i in ids)
    assert tok.decode_bytes(tok.byte_ids) == bytes(range(256))
    with pytest.raises(UnicodeDecodeError):
        tok.decode([tok.byte_ids[255]])
    with pytest.raises(UnicodeEncodeError):
        tok.encode("\ud800")


def test_assistant_only_shift_and_one_target_per_window(tok):
    messages = [{"role":"system","text":"短く。"}, {"role":"user","text":"<|assistant|>って何？"},
                {"role":"assistant","text":"文字列です。"}, {"role":"user","text":"はい"},
                {"role":"assistant","text":"了解\nです。"}]
    ids, labels = tok.dialogue(messages)
    assert ids[0] == 2 and labels[0] == -100
    assert ids.count(6) == 2 and ids.count(7) == 5
    expected = [*tok.encode("文字列です。"), 7, *tok.encode("了解\nです。"), 7]
    assert [x for x in labels[1:] if x != -100] == expected
    windows = list(tok.sft_windows(messages, 1024))
    assert len(windows) == 2
    assert sum(w["target_tokens"] for w in windows) == len(expected)
    assert [x for w in windows for x in w["labels"] if x != -100] == expected


def test_context_removes_whole_turns_and_retains_current_user(tok):
    messages = [{"role":"user","text":"古い"}, {"role":"assistant","text":"昔"},
                {"role":"user","text":"現在"}]
    expected, _ = tok.dialogue(messages[-1:], generation_prompt=True)
    ids, removed = tok.chat_prompt(messages, max_tokens=len(expected))
    assert ids == expected and removed == 1 and ids[-1] == 6
    with pytest.raises(ValueError, match="cannot fit"):
        tok.chat_prompt(messages, max_tokens=2)


def test_unicode_controls_and_unseen_characters(tok):
    rng = random.Random(42)
    points = [rng.randrange(0x110000) for _ in range(1000)]
    text = ''.join(chr(i) for i in range(1,160)) + '\ufffd' + ''.join(chr(i) for i in points if not 0xd800 <= i <= 0xdfff)
    expected = text.replace('\r\n','\n').replace('\r','\n')
    assert tok.decode(tok.encode(text)) == expected
