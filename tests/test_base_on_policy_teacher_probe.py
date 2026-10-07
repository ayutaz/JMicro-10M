import copy
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from probe_base_on_policy_teacher import forecast


def timings():
    return [dict(seconds=.1 if i not in (12,28) else .6,
        rollout_records=[{'fixture':True}] if i in (12,28) else []) for i in range(32)]


def test_forecast_includes_actual_rare_rollout_cost_instead_of_median():
    rows=timings()
    # 30*.1 + 2*.6 = 4.2s. Cached exact17698 updates, margin and eval reserve.
    assert forecast(rows)==3920


@pytest.mark.parametrize('mutation',['missing_step','missing_rollout','nonfinite'])
def test_incomplete_timing_or_missing_auxiliary_cannot_authorize_science(mutation):
    rows=copy.deepcopy(timings())
    if mutation=='missing_step':rows.pop()
    if mutation=='missing_rollout':rows[12]['rollout_records']=[]
    if mutation=='nonfinite':rows[0]['seconds']=float('nan')
    with pytest.raises(ValueError):forecast(rows)
