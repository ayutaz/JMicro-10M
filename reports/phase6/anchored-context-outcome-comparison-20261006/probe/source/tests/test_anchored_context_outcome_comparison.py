import copy
import sys
import pytest
from jmicro.experiment import ROOT,read_json
sys.path.insert(0,str(ROOT/'scripts'))
import run_anchored_context_outcome_comparison as study
from anchored_context_outcome import POLICY as ANCHOR
from context_outcome_ranking import POLICY,OutcomePairSampler
from anchored_context_outcome_accounting import audit_ranking,audit_anchor


def test_single_anchor_strong_quality_Base_only_and_fixed_exposure_scope():
    c=read_json(study.base_study.CONFIG)
    c.update(research_kind=study.KIND,arms={study.ARM:study.GOALS},outcome_weights={study.ARM:1},
        positive_anchor_policy=ANCHOR,prior_probe_GPU_seconds=0)
    study.scope(c)
    for key,value in (('positive_anchor_policy',{**ANCHOR,'coefficient':2}),
            ('ranking_policy',{**POLICY,'families_per_update':4}),('ranking_inputs',dict(path='dev',sha256='dev')),
            ('quality_screen_baseline','weaker_ranking_control'),('Chat_adopted',True),('quantization_started',True),
            ('peak_lr',.00002),('teachers_per_new_arm',50000000)):
        with pytest.raises(ValueError):study.scope({**c,key:value})


def test_actual_fixed_train_exposure_and_separate_hard_teacher_tampering():
    inputs=read_json(study.PROPOSAL)['fixed_pair_inputs']['manifest'];view=study.ranking_view(inputs)
    sampler=OutcomePairSampler(view,2,42);history=[]
    for i in (1,2):
        _,_,_,selected=sampler.next()
        history.append(dict(ranking_family_indices=selected,ranking_digest=sampler.digest,
            **{'ranking_'+k:v for k,v in study.ranking_counts(type('T',(),dict(ranking=sampler))()).items()
               if k not in ('updates','families_seen')},
            main_and_Web_reference_physical_input_tokens=i*40960,
            combined_student_physical_input_tokens=i*40960+sampler.physical_input_positions,
            combined_student_valid_input_tokens=i*40960+sampler.valid_input_tokens,
            positive_anchor_body_teacher_tokens=sampler.gold_body_scored_positions,
            additional_teacher_tokens=i*32000,combined_hard_teacher_positions=i*32000+sampler.gold_body_scored_positions,
            positive_anchor_loss=2.,ranking_loss=.5,combined_pair_loss=2.5,
            ordinary_CE_loss=3.,reference_KL_loss=.1,loss=5.6))
    count=sampler.gold_body_scored_positions
    state=dict(update=320437,supervised_tokens=64010,spec=dict(ranking_policy=POLICY,positive_anchor_policy=ANCHOR),
        lineage=dict(positive_anchor_policy=ANCHOR),
        ranking_state=dict(policy=POLICY,input_binding=view.binding,sampler=sampler.state_dict()),
        positive_anchor_state=dict(policy=ANCHOR,input_binding=view.binding,body_teacher_tokens=count))
    record=dict(ranking_input_binding=view.binding,ranking_policy=POLICY,ranking_sampler=sampler.state_dict(),
        ranking_exposure=study.ranking_counts(type('T',(),dict(ranking=sampler))()),
        main_and_Web_reference_physical_input_tokens=81920,
        combined_student_physical_input_tokens=81920+sampler.physical_input_positions,
        combined_student_valid_input_tokens=81920+sampler.valid_input_tokens,
        positive_anchor_policy=ANCHOR,positive_anchor_body_teacher_tokens=count,combined_hard_teacher_positions=64000+count)
    config=dict(ranking_inputs=inputs,positive_anchor_policy=ANCHOR);parent=dict(update=320435,supervised_tokens=10)
    assert audit_ranking(parent,state,record,history,config)['ranking_exposure']['relational_choice_labels']==8
    assert audit_anchor(parent,state,record,history,config)['positive_anchor_body_teacher_tokens']==count
    for field in ('ranking_foil_body_scored_positions','ranking_valid_input_tokens','combined_student_physical_input_tokens'):
        bad=copy.deepcopy(history);bad[-1][field]+=1
        with pytest.raises(ValueError):audit_ranking(parent,state,record,bad,config)
    for field in ('positive_anchor_body_teacher_tokens','combined_hard_teacher_positions','combined_pair_loss'):
        bad=copy.deepcopy(history);bad[-1][field]+=1
        with pytest.raises(ValueError):audit_anchor(parent,state,record,bad,config)
    bad=copy.deepcopy(state);bad['positive_anchor_state']['body_teacher_tokens']+=1
    with pytest.raises(ValueError):audit_anchor(parent,bad,record,history,config)
    bad=copy.deepcopy(history);bad[0]['ranking_family_indices'].reverse()
    with pytest.raises(ValueError):audit_ranking(parent,state,record,bad,config)

