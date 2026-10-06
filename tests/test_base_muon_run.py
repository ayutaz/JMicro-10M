import copy
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_base_muon import science_budget, matched_control_checks


def test_measured_speed_requires_fixed_total_budget_and_positive_finite_values():
    valid=dict(median_original_teachers_per_second=50000,GPU_occupancy_seconds=15,
               science_budget_seconds=3500,science_budget_eligible=True)
    assert science_budget(valid)==3500
    for speed in (0,-1,float('nan'),float('inf'),20000):
        bad=valid|{'median_original_teachers_per_second':speed}
        with pytest.raises(ValueError): science_budget(bad)


@pytest.mark.parametrize('field', ['science_budget_seconds','science_budget_eligible','GPU_occupancy_seconds'])
def test_forecast_altered_or_probe_unbounded_rejected(field):
    row=dict(median_original_teachers_per_second=50000,GPU_occupancy_seconds=15,
             science_budget_seconds=3500,science_budget_eligible=True)
    row[field]={'science_budget_seconds':3501,'science_budget_eligible':False,'GPU_occupancy_seconds':181}[field]
    with pytest.raises(ValueError): science_budget(row)


def test_matching_teachers_alone_does_not_hide_changed_digest_or_sampler():
    counters=dict(update=4,token_digest='exact',supervised_tokens=100,source_teachers={'web':75,'textbook':20,'story':5},
        source_EOS={'web':1,'textbook':1,'story':1},CE_input_tokens=110,original_body_bytes=200,
        auxiliary_input_tokens=0,auxiliary_pairs=0,physical_input_tokens=200)
    record=dict(counters=counters,sampler={'consumed':counters['source_teachers'],'RNG':[1,2,3],'pending':[]})
    assert all(matched_control_checks(record,record).values())
    for key in ('token_digest','supervised_tokens'):
        changed=copy.deepcopy(record); changed['counters'][key]='changed'
        assert not all(matched_control_checks(record,changed).values())
    changed=copy.deepcopy(record); changed['sampler']['RNG'].reverse()
    assert not matched_control_checks(record,changed)['full_sampler']
