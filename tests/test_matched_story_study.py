from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_matched_story_study import budget_settings
from review_matched_story_study import quality_gates
from run_eos_short_pilot import routes
from jmicro.eos_pilot import pilot_lr

def fixture(count):
    return {str(i):dict(coherence=2 if i<count else 0,completion=0,relevance=2) for i in range(80)}

def evaluation(bpb=1,eos=40,repeat=12):
    return dict(body=dict(bpb=bpb),greedy_rates=dict(eos=eos,repetition=repeat,empty=0,role_leak=0,unicode_failure=0))

def test_amount_common_prefix_routes_and_constant_schedule():
    c=budget_settings('amount');r=routes(c['updates_per_arm'],c['short_updates'])
    assert r[:15259]==routes(15259,3051) and sum(r[15259:])==3051
    spec=dict(pilot_schedule=dict(parent_update=305176,stable_updates=c['stable_updates'],decay_updates=c['decay_updates']))
    assert all(pilot_lr(spec,step)==1 for step in (305176,320435,335694))

def test_paired_quality_requires_real_gain_not_EOS_alone():
    result=quality_gates(evaluation(),evaluation(eos=60),fixture(19),fixture(19),'content')
    assert not result['passed'] and result['difference_count']==0

def test_amount_BPB_nonworsening_and_content_one_percent_distinct():
    args=(evaluation(),evaluation(bpb=1.005),fixture(19),fixture(35))
    assert quality_gates(*args,'content')['passed']
    assert not quality_gates(*args,'amount')['passed']

def test_coherence_loss_and_repetition_cannot_pass():
    result=quality_gates(evaluation(),evaluation(repeat=20),fixture(30),fixture(10),'content')
    assert not result['passed'] and not result['checks']['repetition_nonworsening'] and result['CI95'][1]<0
