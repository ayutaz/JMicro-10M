"""Own one-arm total uses32 timings; field/probe cannot be spent twice."""
import copy
import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_fisher_parameter_anchor import estimate_training,ARMS,CEILING


def test_one_arm_measured_budget_and_missing_timing_rejection():
    assert ARMS == ('fisher_anchor',)
    record=dict(timings={'fisher_anchor':dict(histories=[dict(seconds=.2 if i<8 else .05) for i in range(32)],
        verification_teacher_tokens=32000*32,terminal_save_seconds=.2)})
    evidence,total=estimate_training(record)
    assert evidence['fisher_anchor']['estimated_updates']==3125
    assert total==pytest.approx((3125*.05+1.2+2.8)*1.3+200)
    field,probe=3.6230295989953447,25.
    remaining=CEILING-field-probe
    assert remaining+field+probe==CEILING and total<=remaining
    bad=copy.deepcopy(record);bad['timings']['fisher_anchor']['histories'].pop()
    with pytest.raises(ValueError):estimate_training(bad)
