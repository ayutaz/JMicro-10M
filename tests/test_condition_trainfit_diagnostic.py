"""Real target alignment/read-only scoring; CPU fixtures are not quality evidence."""
import copy
import json
import sys
import pytest
import torch
from jmicro.experiment import ROOT
from jmicro.model import JMicroModel
sys.path.insert(0, str(ROOT / 'scripts'))
import run_condition_trainfit_diagnostic as study


def test_focus_other_EOS_partition_and_unweighted_original_loss():
    values=torch.tensor([1.,2.,3.,4.]); labels=torch.tensor([8,9,10,3]); focus=torch.tensor([False,True,True,False])
    groups=study.group_losses(values, labels, focus)
    assert groups['focus_body']==dict(tokens=2,nll_sum=5.,mean_nll=2.5)
    assert groups['other_body']==dict(tokens=1,nll_sum=1.,mean_nll=1.)
    assert groups['EOS']==dict(tokens=1,nll_sum=4.,mean_nll=4.)
    assert study.group_losses(values,labels,torch.zeros(4,dtype=torch.bool))['focus_body']['mean_nll'] is None
    for changed in (torch.tensor([False,True,True,True]),):
        with pytest.raises(ValueError): study.group_losses(values,labels,changed)
    bad=values.clone(); bad[0]=float('nan')
    with pytest.raises(ValueError): study.group_losses(bad,labels,focus)


def test_batched_original_shift_padding_and_read_only_model():
    config=json.loads((ROOT/'configs/models/t4k.json').read_text()); config.update(num_hidden_layers=2,vocab_size=300)
    torch.manual_seed(15); model=JMicroModel(config).eval(); before=copy.deepcopy(model.state_dict())
    cases=[dict(index=0,id='a',ids=[2,8,9,3],focus=[False,True,False],target_sha256='a'),
           dict(index=1,id='b',ids=[2,11,12,13,14,3],focus=[True,False,True,False,False],target_sha256='b')]
    batch=study.score_batch(model,cases,'cpu'); single=study.score_batch(model,cases[:1],'cpu')[0]
    assert batch[0]['target_ids']==[8,9,3] and batch[0]['focus']==[False,True,False]
    assert batch[0]['target_nll']==pytest.approx(single['target_nll'],abs=1e-5)
    with torch.inference_mode(): expected=-model(torch.tensor([[2,8,9]])).logits[0,-1].log_softmax(-1)[3]
    assert batch[0]['groups']['EOS']['mean_nll']==pytest.approx(float(expected),abs=1e-5)
    assert all(torch.equal(v,before[k]) for k,v in model.state_dict().items())
    assert all(p.grad is None for p in model.parameters())


def test_summary_requires_all_models_same_targets_and_exact_group_counts():
    base=dict(index=0,id='a',target_sha256='x',target_ids=[8,9,3],focus=[False,True,False],
        groups={g:dict(tokens=1,nll_sum=2.,mean_nll=2.) for g in study.GROUPS})
    rows=[dict(checkpoint=arm,**copy.deepcopy(base)) for arm in study.ARMS]
    c=dict(documents=1,target_counts={g:1 for g in study.GROUPS})
    result=study.summarize(rows,c)
    assert result['paired_deltas']['control->positive4']['focus_body']['token_weighted_delta']==0
    for bad in (rows[:-1],rows+rows[:1]):
        with pytest.raises(ValueError): study.summarize(bad,c)
    changed=copy.deepcopy(rows); changed[1]['target_ids'][0]=10
    with pytest.raises(ValueError): study.summarize(changed,c)
    with pytest.raises(ValueError): study.summarize(rows,dict(c,target_counts={g:2 for g in study.GROUPS}))
