import copy
import sys
from pathlib import Path
from types import SimpleNamespace
import pytest
import torch
from torch.nn import functional as F
from jmicro.japanese_evaluation import NativeLikelihood
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from context_prior_analysis import request, family_rows, compare_rows, comparison_counts, index_cases


class PositionSensitiveModel:
    config = dict(max_position_embeddings=1024)
    def __call__(self, ids, attention_mask=None):
        logits = torch.zeros((*ids.shape,32))
        logits.scatter_(-1,((ids+1)%32).unsqueeze(-1),3.)
        return SimpleNamespace(logits=logits)


def test_neutral_transform_preserves_target_span_EOS_and_actual_native_loss():
    row = dict(ids=[2,8,9,10,3],context_tokens=3,target_ids=[10,3],target_bytes=4,prefix='prefix',index=0)
    saved = copy.deepcopy(row)
    neutral = request(row,True)
    assert row == saved
    assert neutral['ids'] == [2,10,3]
    assert neutral['context_tokens'] == 1
    assert neutral['target_ids'] == [10,3]  # EOS isn't silently dropped.
    model = PositionSensitiveModel()
    score = NativeLikelihood(model,None,'cpu','fp32').score_encoded([neutral])[0]
    logits = model(torch.tensor([[2,10]])).logits
    expected = F.cross_entropy(logits[0],torch.tensor([10,3]),reduction='none')
    assert score['target_tokens'] == 2
    assert score['target_bytes'] == 4
    assert score['token_nll'] == expected.tolist()
    assert score['log_likelihood'] == -sum(expected.tolist())
    for change in (dict(context_tokens=2),dict(target_ids=[10]),dict(target_bytes=0),dict(ids=[8,8,9,10,3])):
        with pytest.raises(ValueError):
            request({**row,**change},True)


def fixture(full,prior):
    cases = []
    for branch in (0,1):
        for candidate in (0,1):
            ids = [8+candidate]
            cases.append(dict(index=len(cases),family=0,branch=branch,candidate=candidate,label=branch,
                ids=[2,12+branch,*ids],context_tokens=2,target_ids=ids,target_bytes=3,outcome=str(candidate)))
    families = [dict(index=0,id='one',split='lexical_holdout',category='negation')]
    def scores(margins):
        return [dict(index=c['index'],target_ids=c['target_ids'],target_tokens=1,target_bytes=3,
            token_nll=[10-margins[c['branch']] if c['candidate']==0 else 10.],
            log_likelihood=-(10-margins[c['branch']] if c['candidate']==0 else 10.)) for c in cases]
    return family_rows(scores(full),scores(prior),dict(cases=cases,families=families)),cases


def test_prior_offset_and_context_response_are_separate_and_arithmetic_swaps_not_adoption():
    old,cases = fixture([2.,-2.],[0.,0.])
    prior_changed,_ = fixture([5.,1.],[3.,3.])
    delta = compare_rows(old,prior_changed)
    summary = comparison_counts([r for r in delta if r['metric']=='sum_log_likelihood'])
    assert summary['lost_both_correct'] == 1
    assert summary['arithmetic_prior_change_only_loses'] == 1
    assert delta[0]['signed_context_separation_change'] == 0
    assert prior_changed[0]['diagnostic_context_only_both_correct']
    context_changed,_ = fixture([2.,1.],[0.,0.])
    summary = comparison_counts([r for r in compare_rows(old,context_changed) if r['metric']=='sum_log_likelihood'])
    assert summary['arithmetic_context_change_only_loses'] == 1
    bad = copy.deepcopy(cases)
    bad[-1]['target_ids'] = [10]
    bad[-1]['ids'][-1] = 10
    with pytest.raises(ValueError,match='Same candidates'):
        index_cases(bad,1)
