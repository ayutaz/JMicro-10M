import copy
import sys
import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT,sha256,write_json
sys.path.insert(0,str(ROOT/'scripts'))
import run_condition_diversity_comparison as study
from condition_positive_trainer import PositiveTrainView
from test_condition_positive_trainer import positive_fixture
from test_story_weight_comparison import fixture
from run_eos_short_pilot import equal_state


def expanded_fixture(path,small):
    path.mkdir(); tokens=np.r_[small.tokens,np.asarray(sum(([2,45+i,54,55,3] for i in range(8)),[]),dtype='<u2')]
    focus=np.r_[small.focus,np.tile([0,0,1,0,0],8).astype(bool)]
    np.savez(path/'train.npz',tokens=tokens.astype('<u2'),focus=focus.astype('u1'),offsets=np.arange(16,dtype='<i8')*5,lengths=np.full(16,5,dtype='<i4'))
    write_json(path/'manifest.json',dict(kind='original_train_positive_condition_outcome_spans',newly_prepared_original_tokens=0,
        arrays_sha256=sha256(path/'train.npz'),documents=16,serialized_tokens=80,outcome_focus_body_targets=16))
    return PositiveTrainView(path,sha256(path/'manifest.json'))


def test_changed_conditional_source_retains_exact_three_ordinary_supervised_sequences(tmp_path,monkeypatch):
    pool,_,_=fixture(tmp_path); small=positive_fixture(tmp_path); large=expanded_fixture(tmp_path/'large',small)
    monkeypatch.setattr(study,'GOALS',dict(web=217,story=109,ordinary_textbook=113,conditional_textbook=111))
    a=study.ordinary_stream_digest(pool,small); b=study.ordinary_stream_digest(pool,large)
    for key in ('target_sha256','teachers','EOS','body_bytes'): assert a[key]==b[key]


def test_actual_CPU_expanded_trainer_continuous_resume_and_wrong_source_rejected(tmp_path,monkeypatch):
    pool,parent,binding=fixture(tmp_path); small=positive_fixture(tmp_path); large=expanded_fixture(tmp_path/'large',small)
    monkeypatch.setattr(study,'GOALS',dict(web=200,story=100,ordinary_textbook=100,conditional_textbook=100))
    build=lambda data=large: study.trainer_for(parent,pool,data,binding,'cpu',8,3)
    a=build(); left=[a.step() for _ in range(4)]; a.save(tmp_path/'a/checkpoint.pt')
    b=build(); right=[b.step() for _ in range(2)]; b.save(tmp_path/'split/checkpoint.pt')
    b=build(); b.load(tmp_path/'split/checkpoint.pt'); right.extend(b.step() for _ in range(2)); b.save(tmp_path/'b/checkpoint.pt')
    x=torch.load(tmp_path/'a/checkpoint.pt',map_location='cpu',weights_only=False)
    y=torch.load(tmp_path/'b/checkpoint.pt',map_location='cpu',weights_only=False)
    for key in ('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens','body_bytes','token_digest','focus_token_digest','spec','study_binding'):
        assert equal_state(x[key],y[key]),key
    assert [r['loss'] for r in left]==[r['loss'] for r in right]
    assert x['spec']['research_kind']=='nested_condition_source_quantity' and x['weighted_teacher_mass']==x['supervised_tokens']-parent['supervised_tokens']
    with pytest.raises(ValueError): build(small).load(tmp_path/'split/checkpoint.pt')


def test_measured_budget_includes_warmup_saving_and_only_one_new_evaluation():
    timing=dict(histories=[dict(seconds=.2 if i<8 else .05) for i in range(32)],verification_teacher_tokens=32000*32,terminal_save_seconds=.2)
    out,total=study.estimate_training(dict(timing=timing))
    assert out['estimated_updates']==782 and out['warmup_seconds']==pytest.approx(1.2)
    assert total==pytest.approx((782*.05+1.2+1.)*1.3+300)
    with pytest.raises(ValueError): study.estimate_training(dict(timing=dict(timing,histories=timing['histories'][:-1])))


def test_same_teachers_weight1_and_Base_only_scope():
    c=dict(research_kind='nested_condition_source_quantity',arms={study.ARM:study.GOALS},outcome_weights={study.ARM:1},
        teachers_per_new_arm=25000000,total_comparison_teachers=50000000,total_new_GPU_ceiling_seconds=900,
        peak_lr=.0002,optimizer_policy='inherit',shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),
        loss='ordinary original body+EOS CE, outcome weight1',Base_adopted=False,Chat_adopted=False,protected_test_used=False,
        requested_five_steps_complete=False,quality_criteria_unchanged=True)
    study.scope(c)
    for change in (dict(outcome_weights={study.ARM:4}),dict(teachers_per_new_arm=50000000),dict(Chat_adopted=True)):
        with pytest.raises(ValueError): study.scope(dict(c,**change))
