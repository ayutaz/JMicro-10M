"""Research scope, missing-cache, and measured-budget guards; no GPU claims."""
import sys
from types import SimpleNamespace

import pytest
from jmicro.experiment import ROOT

sys.path.insert(0,str(ROOT/'scripts'))
from run_textbook_coverage import validate_scope,cached_index_record,estimate_training,validate_timing


def scope():
    return dict(research_kind='same_material_teacher_coverage',target_teachers=2000000000,
        decay_teacher_tokens=20000000,parent_point='large-1000000000',candidate_point='large-2000000000',
        total_new_GPU_ceiling_seconds=2700,quality_criteria_unchanged=True,protected_test_used=False,
        Base_adopted=False,Chat_adopted=False,requested_five_steps_complete=False,historical_quality_extension_refusal_preserved=True)


@pytest.mark.parametrize('field,value',[
    ('target_teachers',5000000000),('decay_teacher_tokens',25000000),('quality_criteria_unchanged',False),
    ('protected_test_used',True),('historical_quality_extension_refusal_preserved',False),('Base_adopted',True)])
def test_research_cannot_silently_expand_or_claim_quality(field,value):
    plan=scope();validate_scope(plan);plan[field]=value
    with pytest.raises(ValueError,match='contract differs'):validate_scope(plan)


def test_missing_cache_refuses_before_original_index_read(tmp_path):
    with pytest.raises(ValueError,match='do not rescan'):
        cached_index_record(dict(pools=dict(large=dict(pool=str(tmp_path),manifest_sha256='f'*64))))
    assert not list(tmp_path.iterdir())


def test_budget_uses_all12_steady_updates_and_counts_decay():
    rows=[dict(seconds=100. if i<4 else .05) for i in range(16)]
    measurement=dict(histories=rows,verification_teacher_tokens=520000)
    timing,estimate=estimate_training(measurement)
    assert timing['stable_updates']==30770 and timing['decay_updates']==616
    assert timing['estimated_step_seconds']==31386*.05
    assert estimate==31386*.05*1.3+480+60
    with pytest.raises(AssertionError):estimate_training(dict(measurement,histories=rows[:-1]))


def test_timing_row_is_not_a_checkpoint_or_nonfinite_evidence():
    rows=[dict(update=10+i,supervised_tokens=100+i,seconds=.1,loss=1.,gradient_norm=1.,lr=.002,data_wait_seconds=.01) for i in range(16)]
    # Missing model/optimizer must not be accepted as full finite checkpoint state.
    with pytest.raises(KeyError):validate_timing(rows,dict(update=9,supervised_tokens=99),rows[-1])
