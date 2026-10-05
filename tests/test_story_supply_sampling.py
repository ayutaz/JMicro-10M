"""Byte-position sampling math, not material quality or unique capacity evidence."""
import io
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0, str(ROOT/"scripts"))
from probe_larger_story_supply import containing_line


def test_containing_record_includes_newline_and_handles_first_last_offsets():
    data = b"first\nsecond-longer\nlast"
    for offset in range(len(data)):
        line, start = containing_line(io.BytesIO(data), offset, len(data))
        assert start <= offset < start+len(line)
        assert line in (b"first\n", b"second-longer\n", b"last")
    with pytest.raises(ValueError, match="bounded"):
        containing_line(io.BytesIO(b"x"*100), 50, 100, window=4)


def test_probability_proportional_to_bytes_ratio_recovers_token_total():
    data = b"tiny\n"+b"a-much-longer-record\n"
    tokens = {b"tiny\n":100, b"a-much-longer-record\n":7}
    rates = []
    for offset in range(len(data)):
        line, _ = containing_line(io.BytesIO(data), offset, len(data))
        rates.append(tokens[line]/len(line))
    assert sum(rates) == pytest.approx(107)
    assert sum(rates)/len(data)*len(data) == pytest.approx(107)
