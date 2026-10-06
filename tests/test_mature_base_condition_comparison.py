import copy
import sys

import pytest
from jmicro.experiment import ROOT
sys.path.insert(0, str(ROOT / 'scripts'))
import run_mature_base_condition_comparison as study


def recipe():
    return dict(research_kind=study.KIND, arms=copy.deepcopy(study.ARMS), teachers_per_arm=study.TOTAL,
        scientific_teacher_tokens=3*study.TOTAL, total_new_GPU_ceiling_seconds=study.CEILING,
        peak_lr=.0002, optimizer_policy='inherit', outcome_weight=1,
        shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),
        comparisons=['curriculum-vs-web','relation-vs-web','relation-vs-curriculum-secondary'],
        Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        quality_criteria_unchanged=True)


def test_scope_rejects_new_data_ratios_parent_stages_and_criteria():
    c=recipe(); study.scope(c)
    for key,value in (('Chat_started',True),('quantization_started',True),('protected_test_used',True),
                      ('quality_criteria_unchanged',False),('peak_lr',.002),('scientific_teacher_tokens',100000000)):
        bad=copy.deepcopy(c);bad[key]=value
        with pytest.raises(ValueError,match='scope'):study.scope(bad)
    bad=copy.deepcopy(c);bad['arms']['web']['story']=1
    with pytest.raises(ValueError,match='scope'):study.scope(bad)


def test_budget_requires_three_actual32_timings_and_four_evaluations():
    measured=dict(arms={arm:dict(timing=dict(histories=[dict(seconds=.05)]*32,
        verification_teacher_tokens=32*32000,terminal_save_seconds=.1)) for arm in study.ARMS})
    timings,estimate=study.estimate_training(measured)
    assert set(timings)==set(study.ARMS)
    assert estimate>1300 and estimate<study.CEILING
    del measured['arms']['web']
    with pytest.raises(ValueError,match='All3'):study.estimate_training(measured)
    measured['arms']['web']=dict(timing=dict(histories=[dict(seconds=float('nan'))]*32,
        verification_teacher_tokens=32*32000,terminal_save_seconds=.1))
    with pytest.raises(ValueError,match='Actual32'):study.estimate_training(measured)
