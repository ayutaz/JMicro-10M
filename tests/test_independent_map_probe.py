"""CPU-only gate integrity: original scope, forecast and cache subchecks."""
from pathlib import Path
import sys
from types import SimpleNamespace as Row

import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from probe_independent_map import assert_scope,forecast,cache_observations,IMPLEMENTATION


def contract():
    return dict(kind='owned_native_independent_rank8_map_CUDA_technical_v1',batch=48,seed=42,
        GPU_ceiling_seconds=180,prior_technical_GPU_seconds=72.56365345604718,
        timed_updates=32,continuous_updates=6,split_updates=[3,3],disabled_native_updates=3,
        capacity_shape=[48,1024],candidate_parameters=10067764,main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800,scientific_teacher_positions=0,attention_implementation=IMPLEMENTATION,
        capacity_before_any_optimizer=True,preserve_actual6_and_all_cache_subchecks=True,
        Base_adopted=False,TEST_prepared=False)


def test_exact_original_cumulative_scope():
    assert_scope(contract())


@pytest.mark.parametrize('key,value',[
    ('prior_technical_GPU_seconds',0.),('GPU_ceiling_seconds',181),('maximum_new_GPU_seconds',4801),
    ('capacity_shape',[48,512]),('candidate_parameters',10001204),('main_teacher_goal',50000000),
    ('scientific_teacher_positions',1),('capacity_before_any_optimizer',False),
    ('preserve_actual6_and_all_cache_subchecks',False),('disabled_native_updates',0),
    ('attention_implementation','cross_map'),('batch',24),
])
def test_no_rank_geometry_control_evidence_or_budget_rescue(key,value):
    c=contract()
    c[key]=value
    with pytest.raises(ValueError): assert_scope(c)


def test_original100M_forecast_charges_all32_times_safety_margin_and_evaluation_reserve():
    assert forecast([dict(seconds=.05)]*32)==1751
    for rows in ([dict(seconds=.05)]*31,[dict(seconds=-1.)]*32,[dict(seconds=float('nan'))]*32):
        with pytest.raises(ValueError): forecast(rows)


def pair():
    def cache():
        return Row(secondary=[torch.zeros(1,2,4,8)],valid=torch.ones(1,4,dtype=torch.bool),positions=torch.arange(4)[None])
    return Row(logits=torch.zeros(1,4,10),cache=cache()),Row(logits=torch.zeros(1,2,10),cache=cache())


def test_cache_original_combined_tolerance_not_absolute_only_and_bounded_failure_values():
    a,b=pair()
    a.logits[:,-2:]=10
    b.logits[:]=10.0001
    assert cache_observations(a,b,True)['passed']
    b.logits[:]=11
    r=cache_observations(a,b,True)
    assert not r['passed'] and r['outside_original_logit_tolerance']==20 and len(r['first_eight_outside'])==8
    assert r['first_eight_outside'][0]['absolute_difference']>r['first_eight_outside'][0]['allowed_error']


@pytest.mark.parametrize('bad',['K2','positions','valid','RNG'])
def test_secondary_cache_and_metadata_failures_are_recorded_individually(bad):
    a,b=pair()
    if bad=='K2': b.cache.secondary[0][0,0,0,0]=.01
    elif bad=='positions': b.cache.positions[0,0]=99
    elif bad=='valid': b.cache.valid[0,0]=False
    r=cache_observations(a,b,bad!='RNG')
    assert not r['passed'] and sum(not v for v in r['subchecks'].values())==1
