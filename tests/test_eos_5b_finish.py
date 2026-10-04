from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from run_eos_5b_finish import safe_control


def test_parent_unicode_failure_does_not_relax_original_zero_failure_gate():
    # The parent has one cap-tail failure; corrected display must not make it eligible.
    rates = dict(repetition=59, empty=0, role_leak=0, unicode_failure=1)
    assert not safe_control(rates,59)
    rates['unicode_failure'] = 0
    assert safe_control(rates,59)


def test_exact_eight_repeat_regression_is_ineligible():
    rates = dict(repetition=67, empty=0, role_leak=0, unicode_failure=0)
    assert not safe_control(rates,59)
    rates['repetition'] = 66
    assert safe_control(rates,59)
