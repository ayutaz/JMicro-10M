"""Prospective paired budgets and full original-stream comparison refusals."""
import copy
import math
import sys
from pathlib import Path
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from probe_base_headwise_gate import forecast,paired_budget,source_checks,comparable_history


def arms(seconds=5,gold=300000):
    return {a:dict(all32_step_seconds=seconds,all32_original_gold=gold)
        for a in ('static_half','query_headwise')}


def test_all32_sum_formula_both_arms_and_probe_included():
    sample=arms();sample['query_headwise']['all32_step_seconds']=6
    budget,eligible=paired_budget(sample,20)
    assert budget==dict(static_half=math.ceil(100000000*5/300000*1.3+900),
                        query_headwise=math.ceil(100000000*6/300000*1.3+900))
    assert eligible
    budget,eligible=paired_budget(arms(10),20)
    assert sum(budget.values())+20>9000 and not eligible


@pytest.mark.parametrize('seconds,gold',[(0,1),(-1,2),(float('nan'),2),(float('inf'),2),(1,0),(1,True)])
def test_invalid_aggregate_refused(seconds,gold):
    with pytest.raises(ValueError):forecast(seconds,gold)


@pytest.mark.parametrize('elapsed',[0,181,float('nan')])
def test_probe_time_cap_not_waived(elapsed):
    with pytest.raises(ValueError):paired_budget(arms(),elapsed)


def test_control_required_and_timing_only_ignored():
    sample=arms();del sample['static_half']
    with pytest.raises(ValueError):paired_budget(sample,5)
    left=[dict(update=1,CE_loss=2,seconds=1,data_wait_seconds=.2)]
    right=[dict(update=1,CE_loss=2,seconds=4,data_wait_seconds=.8)]
    assert comparable_history(left,right)
    right[0]['CE_loss']=3
    assert not comparable_history(left,right)
    assert not comparable_history(left,[])


def test_full_sampler_and_each_original_counter_required():
    keys=('update','token_digest','supervised_tokens','source_teachers','source_EOS',
          'CE_input_tokens','original_body_bytes','auxiliary_input_tokens','auxiliary_pairs','physical_input_tokens')
    left=dict(counters={k:1 for k in keys},sampler=dict(prefix=[1],RNG=[2]))
    right=copy.deepcopy(left)
    assert all(source_checks(left,right).values())
    right['sampler']['prefix']=[3]
    assert not source_checks(left,right)['full_sampler']
    right['counters']['token_digest']=2
    assert not source_checks(left,right)['token_digest']
