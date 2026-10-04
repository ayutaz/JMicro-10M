from pathlib import Path
import sys
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from run_story10_comparison import selection_checks
from run_eos_short_pilot import routes


def inputs():
    a=dict(greedy_rates=dict(eos=0,repetition=60,empty=0,role_leak=0,unicode_failure=0),body={'bpb':1.0},generation={'outputs':[]})
    b=dict(greedy_rates=dict(eos=12,repetition=40,empty=0,role_leak=0,unicode_failure=0),body={'bpb':1.005},generation={'outputs':[]})
    scores_a={str(i):{'coherence':0} for i in range(80)}
    scores_b={str(i):{'coherence':2 if i<10 else 0} for i in range(80)}
    return a,b,scores_a,scores_b


def test_ten_percent_routes_keep_equal_tokens_and_reuse_pool_without_wrap():
    choice=routes(3052,305)
    assert len(choice)==3052 and sum(choice)==305
    assert sum(choice)*32768==9994240<25000067
    assert (len(choice)-sum(choice))*32768==90013696


def test_content_improvement_and_existing_loss_stopping_rules_are_joint():
    a,b,sa,sb=inputs()
    assert selection_checks(a,b,sa,sb)['eligible_for_full']
    b['body']['bpb']=1.02
    assert not selection_checks(a,b,sa,sb)['eligible_for_full']


def test_loss_pass_cannot_waive_raw_failure():
    a,b,sa,sb=inputs()
    b['greedy_rates']['unicode_failure']=1
    assert not selection_checks(a,b,sa,sb)['eligible_for_full']


def test_eos_pass_cannot_waive_no_content_gain():
    a,b,sa,_=inputs()
    assert not selection_checks(a,b,sa,sa)['eligible_for_full']


def test_comparison_requires_same_complete_prompt_set():
    a,b,sa,sb=inputs()
    sb.pop('1')
    with pytest.raises(AssertionError): selection_checks(a,b,sa,sb)
