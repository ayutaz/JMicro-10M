import copy
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_base_on_policy_teacher import science_budget,matched_control_checks
from review_base_on_policy_teacher import audit_rollout_history
from test_base_on_policy_teacher_probe import timings
from test_base_on_policy_teacher import build_factory


def budget_record():
    return dict(GPU_occupancy_seconds=20.,histories={'timing':[{}]*3+timings()},
        science_budget_seconds=3920,science_budget_eligible=True)


def test_science_forecast_uses_two_actual_sampling_costs():
    assert science_budget(budget_record())==3920


@pytest.mark.parametrize('mutation',['forecast','ineligible','unbounded','slow'])
def test_changed_forecast_ineligible_or_exhausted_budget_rejected(mutation):
    r=budget_record()
    if mutation=='forecast':r['science_budget_seconds']+=1
    if mutation=='ineligible':r['science_budget_eligible']=False
    if mutation=='unbounded':r['GPU_occupancy_seconds']=181
    if mutation=='slow':
        for h in r['histories']['timing'][3:]:h['seconds']*=5
        from probe_base_on_policy_teacher import forecast
        r['science_budget_seconds']=forecast(r['histories']['timing'][3:])
    with pytest.raises(ValueError):science_budget(r)


def test_gold_count_alone_cannot_hide_changed_original_stream_or_full_sampler():
    counters=dict(update=4,token_digest='exact',supervised_tokens=100,source_teachers={'web':75,'textbook':20,'story':5},
        source_EOS={'web':1,'textbook':1,'story':1},CE_input_tokens=110,original_body_bytes=200,
        auxiliary_input_tokens=0,auxiliary_pairs=0,physical_input_tokens=200)
    r=dict(counters=counters,sampler=dict(consumed=counters['source_teachers'],RNG=[1,2,3],pending=[]))
    assert all(matched_control_checks(r,r).values())
    wrong=copy.deepcopy(r);wrong['sampler']['RNG'].reverse()
    assert not matched_control_checks(r,wrong)['full_sampler']
    wrong=copy.deepcopy(r);wrong['counters']['token_digest']='different'
    assert not matched_control_checks(r,wrong)['token_digest']


def test_saved_generated_IDs_reconstruct_inputs_positions_and_digest(tmp_path):
    build,_=build_factory(tmp_path);t=build();history={}
    for _ in range(16):
        row=t.step();history[row['update']]=row
    audit_rollout_history(history,t.on_policy)
    broken=copy.deepcopy(history);broken[16]['on_policy_teacher']['teacher_physical_inputs']+=1
    with pytest.raises(ValueError):audit_rollout_history(broken,t.on_policy)
    broken=copy.deepcopy(history);broken[16]['rollout_records'][0]['generated']=[3,8]
    with pytest.raises(ValueError):audit_rollout_history(broken,t.on_policy)
