import math
from pathlib import Path
import shutil

import pytest

from jmicro.evaluation import bits_per_byte, canonicalize_text
from jmicro.experiment import ROOT, read_json, write_json
from jmicro.validation import validate_phase0


def test_bpb_uses_bytes_and_natural_log_conversion():
    assert bits_per_byte(12 * math.log(2), 6) == pytest.approx(2)
    text = "あ"
    assert len(text.encode("utf-8")) == 3
    assert bits_per_byte(6 * math.log(2), len(text.encode("utf-8"))) == pytest.approx(2)


@pytest.mark.parametrize("nll,size", [(math.nan, 1), (math.inf, 1), (-1, 1), (1, 0), (1, -1), (1, True), (1, 1.5)])
def test_bpb_rejects_invalid_measurements(nll, size):
    with pytest.raises(ValueError):
        bits_per_byte(nll, size)


def test_canonicalization_preserves_chat_symbols_and_combining_characters():
    text = "　ｗｗｗ！！！  か\u3099\t🤔\r\n<|assistant|>\x00"
    assert canonicalize_text(text) == "　ｗｗｗ！！！  か\u3099\t🤔\n<|assistant|>"
    with pytest.raises(UnicodeEncodeError):
        canonicalize_text("\ud800")


def test_complete_phase0_evaluation_contract():
    report = validate_phase0()
    assert report["suites"]["base"]["cases"] == 100
    assert report["suites"]["chat"]["test"] == 20
    assert not report["gpu_verified"]


def test_manifest_catches_changed_evaluation_input(tmp_path):
    for name in ("configs", "schemas", "eval"):
        shutil.copytree(ROOT / name, tmp_path / name)
    target = tmp_path / "eval/chat.jsonl"
    target.write_bytes(target.read_bytes().replace("おはよう".encode(), "こんばんは".encode(), 1))
    with pytest.raises(ValueError, match="checksum mismatch"):
        validate_phase0(tmp_path)
