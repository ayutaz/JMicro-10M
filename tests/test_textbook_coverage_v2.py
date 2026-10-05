"""Scientific budget includes actual warmup, save cadence and decay."""
import math
import sys

import pytest
from jmicro.experiment import ROOT

sys.path.insert(0, str(ROOT/'scripts'))
import run_textbook_coverage_v2 as study
from test_textbook_coverage import scope


def measurement():
    return dict(histories=[dict(seconds=.2 if i<16 else .05) for i in range(64)],
                verification_teacher_tokens=2080000,mean_save_seconds=.15,save_every_updates=250)


def test_measurement_budget_counts_warmup_durable_saves_and_decay():
    record, estimate = study.estimate_training(measurement())
    updates, decay = 30770, 616
    assert record['stable_updates']==updates and record['decay_updates']==decay
    assert record['measured_updates']==64 and record['steady_updates']==48
    assert math.isclose(record['estimated_warmup_seconds'], 2.4)
    saves=(math.ceil(updates/250)+math.ceil(decay/250)+2)*.15
    assert record['estimated_save_seconds']==saves
    assert math.isclose(estimate,((updates+decay)*.05+2.4+saves)*1.3+480+60)
    with pytest.raises(AssertionError):
        study.estimate_training(dict(measurement(),histories=measurement()['histories'][:16]))


def test_versioned_budget_preserves_science_and_quality_contract():
    plan=scope()
    with pytest.raises(ValueError):study.validate_scope(plan)
    plan['total_new_GPU_ceiling_seconds']=3000
    study.validate_scope(plan)
    for field, value in [('target_teachers',5000000000),('quality_criteria_unchanged',False),
                         ('protected_test_used',True),('Base_adopted',True)]:
        with pytest.raises(ValueError):study.validate_scope(dict(plan,**{field:value}))


@pytest.mark.parametrize('cost,cadence',[(float('nan'),250),(-1.,250),(.1,1)])
def test_invalid_saving_cost_or_cadence_cannot_shrink_budget(cost,cadence):
    with pytest.raises(AssertionError):
        study.estimate_training(dict(measurement(),mean_save_seconds=cost,save_every_updates=cadence))
