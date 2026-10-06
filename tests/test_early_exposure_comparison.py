import copy
import sys
import pytest
import torch
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
import run_early_exposure_comparison as study
from review_early_exposure_comparison import fit_summary


def test_read_only_scope_rejects_training_or_stage_changes():
    c=dict(research_kind='earliest_saved8M_vs_nested100M_read_only',GPU_limit_seconds=450,new_scientific_teacher_tokens=0,
        optimizer_updates=0,reused_scientific_trajectory_tokens=100000000,early=dict(additional_teachers=8150782,
        additional_inputs=8192000,update=305426,sampler_position=250),quality_criteria_unchanged=True,
        Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    study.scope(c)
    for key,value in (('optimizer_updates',1),('new_scientific_teacher_tokens',1),('Chat_started',True),
        ('quantization_started',True),('protected_test_used',True),('quality_criteria_unchanged',False)):
        bad=copy.deepcopy(c);bad[key]=value
        with pytest.raises(ValueError,match='scope'):study.scope(bad)
    bad=copy.deepcopy(c);bad['early']['sampler_position']=500
    with pytest.raises(ValueError,match='scope'):study.scope(bad)


def test_body_and_eos_loss_denominators_exclude_mask_and_pool_counts():
    y=torch.tensor([[8,3,-100],[9,10,3]])
    ce=torch.tensor([[1.,2.,100.],[3.,5.,4.]])
    parts=study.loss_parts(ce,y)
    assert parts==dict(full_CE=3.,body_CE=3.,EOS_CE=3.,teachers=5,body_teachers=3,EOS_teachers=2)
    rows=[]
    for source in ('web','story','ordinary_textbook','conditional_textbook'):
        for draw in range(4):rows.append(dict(source=source,draw=draw,teachers=draw+2,EOS_teachers=1,full_CE=float(draw+1),EOS_CE=.5))
    r=fit_summary(rows)['web']
    assert r['full_CE']==40/14 and r['body_CE']==38/10 and r['EOS_CE']==.5
    y[0,0]=2
    with pytest.raises(ValueError,match='masks'):study.loss_parts(ce,y)
