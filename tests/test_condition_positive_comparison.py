import copy
import sys

import pytest
from jmicro.experiment import ROOT

sys.path.insert(0, str(ROOT / 'scripts'))
import run_condition_positive_comparison as study


def test_measured_both_arm_budget_includes_warmup_saves_and_evaluation():
    rows = [dict(seconds=.2 if i < 8 else .05) for i in range(32)]
    measured = dict(timings={arm: dict(histories=rows, verification_teacher_tokens=32000*32,
                                    terminal_save_seconds=.2) for arm in study.GOALS})
    timings, seconds = study.estimate_training(measured)
    assert timings['control']['estimated_updates'] == 782
    assert timings['positive4']['warmup_seconds'] == pytest.approx(1.2)
    assert timings['control']['save_seconds'] == pytest.approx(1.)
    assert seconds == pytest.approx(2 * (782*.05 + 1.2 + 1.) * 1.3 + 600)
    with pytest.raises(ValueError):
        study.estimate_training(dict(timings={'control': measured['timings']['control']}))


def test_scope_refuses_changed_teachers_weights_shape_and_later_stages():
    config = dict(research_kind='same_input_positive_outcome_CE', arms=copy.deepcopy(study.GOALS),
        teachers_per_arm=25000000, total_new_GPU_ceiling_seconds=1800, peak_lr=.0002,
        optimizer_policy='inherit', outcome_weights=study.FACTORS,
        loss='normalized positive-outcome CE body+EOS', protected_test_used=False, Base_adopted=False,
        Chat_adopted=False, requested_five_steps_complete=False, quality_criteria_unchanged=True,
        shapes=dict(context=1024, batch=32, accumulation=1, backend='flash', compile_mode='reduce-overhead', dtype='bf16'))
    study.validate_scope(config)
    for change in (dict(teachers_per_arm=50000000), dict(outcome_weights=dict(control=1, positive4=3)),
                   dict(shapes=dict(config['shapes'], batch=111)), dict(Chat_adopted=True)):
        with pytest.raises(ValueError):
            study.validate_scope(dict(config, **change))
