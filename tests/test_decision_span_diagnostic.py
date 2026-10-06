import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from decision_span_diagnostic import compare,aggregate


def case(target):
    return dict(prefix='same-context',context_tokens=2,ids=[2,8,*target],target_ids=target,target_bytes=len(target)*3)


def score(target,nll,greedy=False):
    return dict(target_ids=target,target_tokens=len(target),target_bytes=len(target)*3,
        token_nll=nll,log_likelihood=-sum(nll),is_greedy=greedy)


def test_first_distinct_same_input_full_rank_can_hide_bad_decision_and_nongreedy_body():
    a,b=case([9,10,12]),case([9,11,12])
    row=compare(a,b,score(a['target_ids'],[.1,3,.1]),score(b['target_ids'],[.1,1,8]))
    assert row['decision_index']==1 and row['shared_target_tokens']==1
    assert row['decision_margin']==-2
    assert row['full_margins']['sum_log_likelihood']>0
    assert row['full_sum_correct_but_decision_wrong']
    assert row['full_sum_correct_but_gold_body_not_greedy']
    paired=[dict(row,family='one',branch=i) for i in (0,1)]
    s=aggregate(paired)
    assert s['full_candidate']['sum_log_likelihood']['both_correct']==1
    assert s['decision_both_correct']==s['gold_exact_greedy_body_both_poles']==0
    assert s['full_sum_correct_but_decision_wrong']==2
    bad={**b,'ids':[2,13,*b['target_ids']]}
    with pytest.raises(ValueError,match='Same context'):compare(a,bad,score(a['target_ids'],[.1,3,.1]),score(b['target_ids'],[.1,1,8]))


def test_prefix_inclusion_is_explicitly_unscorable_and_argmax_is_not_candidate_preference():
    a,b=case([9]),case([9,10])
    row=compare(a,b,score(a['target_ids'],[.2],True),score(b['target_ids'],[.2,.3]))
    assert row['decision_margin'] is None
    s=aggregate([dict(row,family='one',branch=i) for i in (0,1)])
    assert s['unscorable_context_poles']==2 and s['decision_accuracy_over_scorable'] is None
    assert s['gold_exact_greedy_body_both_poles']==1
    bad=score(a['target_ids'],[.2]);bad['is_greedy']=1
    with pytest.raises(ValueError,match='argmax'):compare(a,b,bad,score(b['target_ids'],[.2,.3]))
