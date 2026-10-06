"""Real CPU fork state and transfer accounting; no GPU-quality claims."""
import copy
import sys
import pytest
import torch
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
import run_condition_transfer_comparison as study
from test_condition_positive_trainer import positive_fixture
from test_story_weight_comparison import fixture
from run_eos_short_pilot import equal_state


def test_actual_CPU_curriculum_fork_saves_all_state_and_rejects_changed_provenance(tmp_path,monkeypatch):
    pool,parent,b=fixture(tmp_path);positive=positive_fixture(tmp_path)
    monkeypatch.setattr(study,'GOALS',dict(web=400,story=200,ordinary_textbook=200,conditional_textbook=200))
    binding=dict(b,study_kind=study.KIND,arm=study.ARM)
    build=lambda:study.trainer_for(parent,pool,positive,binding,'cpu',8,3)
    t=build();left=[t.step() for _ in range(4)];t.save(tmp_path/'continuous.pt')
    t=build();right=[t.step() for _ in range(2)];t.save(tmp_path/'split.pt');t=build();t.load(tmp_path/'split.pt')
    right.extend(t.step() for _ in range(2));t.save(tmp_path/'resumed.pt')
    a=torch.load(tmp_path/'continuous.pt',weights_only=False);b=torch.load(tmp_path/'resumed.pt',weights_only=False)
    for key in ('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens','body_bytes','token_digest','focus_token_digest','study_binding','spec'):
        assert equal_state(a[key],b[key]),key
    assert [r['loss'] for r in left]==[r['loss'] for r in right]
    assert a['spec']['research_kind']==study.KIND and a['spec']['outcome_weight']==1
    assert a['weighted_teacher_mass']==a['supervised_tokens']-parent['supervised_tokens']
    wrong=study.trainer_for(parent,pool,positive,dict(binding,study_kind='original_natural'),'cpu',8,3)
    with pytest.raises(ValueError):wrong.load(tmp_path/'split.pt')


def test_measured_budget_counts_all_three_weight_transfer_probes_and_one_full_evaluation():
    timing=dict(histories=[dict(seconds=.2 if i<8 else .05) for i in range(32)],verification_teacher_tokens=32000*32,terminal_save_seconds=.2)
    detail,total=study.estimate_training(dict(timing=timing))
    assert detail['estimated_updates']==3125
    assert total==pytest.approx((3125*.05+1.2+2.8)*1.3+340)
    timing['histories'].pop()
    with pytest.raises(ValueError):study.estimate_training(dict(timing=timing))


def test_transfer_opposed_family_credit_common_targets_and_ties():
    prepared=dict(families=[],cases=[]);rows=[]
    for f,split in enumerate(('lexical_holdout','structural_holdout')):
        prepared['families'].append(dict(index=f,id=str(f),split=split,category='negation'))
        for b in (0,1):
            for k in (0,1):
                i=len(rows);prepared['cases'].append(dict(index=i,family=f,branch=b,candidate=k,target_ids=[8,9],target_bytes=4))
                loss=(2 if b==k else 4) if f==0 else 3
                rows.append(dict(index=i,target_ids=[8,9],target_tokens=2,target_bytes=4,token_nll=[loss/2,loss/2],log_likelihood=-loss))
    result=study.summarize_transfer(rows,prepared)['aggregate']
    assert result['sum_log_likelihood']['lexical_holdout']['both_correct']==1
    assert result['sum_log_likelihood']['structural_holdout']['accuracy']==.5
    assert result['sum_log_likelihood']['all128']['accuracy']==.75
    rows[0]['target_ids']=[8,10]
    with pytest.raises(ValueError):study.summarize_transfer(rows,prepared)


def test_scope_rejects_unequal_learning_changed_loss_or_later_stages():
    c=dict(research_kind=study.KIND,arms={study.ARM:study.GOALS},outcome_weights={study.ARM:1},teachers_per_new_arm=100000000,
        total_comparison_teachers=200000000,total_new_GPU_ceiling_seconds=900,peak_lr=.0002,optimizer_policy='inherit',
        shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),
        loss='ordinary original body+EOS CE, outcome weight1',Base_adopted=False,Chat_adopted=False,protected_test_used=False,
        requested_five_steps_complete=False,quality_criteria_unchanged=True)
    study.scope(c)
    for change in (dict(teachers_per_new_arm=25000000),dict(Chat_adopted=True),dict(outcome_weights={study.ARM:4}),dict(protected_test_used=True)):
        with pytest.raises(ValueError):study.scope(dict(c,**change))
