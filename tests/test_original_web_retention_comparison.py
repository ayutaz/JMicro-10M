import copy
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0, str(ROOT / 'scripts'))
import run_original_web_retention_comparison as study
from review_original_web_retention_comparison import retained_sources


def test_scope_and_measured_budget_keep_base_only_and_exact_quotas():
    c = dict(research_kind=study.KIND, arms={study.ARM:study.GOALS}, outcome_weights={study.ARM:1},
        teachers_per_new_arm=study.TOTAL, total_comparison_teachers=2*study.TOTAL,
        total_new_GPU_ceiling_seconds=study.CEILING, peak_lr=.0002, optimizer_policy='inherit',
        shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),
        loss='ordinary original body+EOS CE, outcome weight1', Base_adopted=False, Chat_adopted=False,
        quantization_started=False,protected_test_used=False,requested_five_steps_complete=False,quality_criteria_unchanged=True)
    study.scope(c)
    for key,value in (('Chat_adopted',True),('quantization_started',True),('protected_test_used',True),
                      ('quality_criteria_unchanged',False),('peak_lr',.002),('total_comparison_teachers',100000000)):
        bad=copy.deepcopy(c);bad[key]=value
        with pytest.raises(ValueError,match='scope'): study.scope(bad)
    timing=dict(histories=[dict(seconds=.05)]*32,verification_teacher_tokens=32*32000,terminal_save_seconds=.1)
    measured,estimate=study.estimate_training(dict(timing=timing))
    assert measured['estimated_updates']==3125 and 350 < estimate < study.CEILING
    timing['histories'][0]['seconds']=float('nan')
    with pytest.raises(ValueError,match='Actual32'): study.estimate_training(dict(timing=timing))


def test_retained_short_cursors_and_parent_web_wrap_are_required():
    initial=dict(seed=42,context=8,blocks=100,epoch=2,position=99)
    parent=dict(sampler=initial,shard_manifest_sha256='original')
    sources=('story','ordinary_textbook','conditional_textbook')
    sampler=dict(streams={s:dict(cursor=3) for s in sources})
    for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):
        sampler[key]={s:5 for s in sources}
    control=dict(sampler=copy.deepcopy(sampler))
    sampler['streams']['web']=dict(kind='actual-parent-Web-block-cursor-v1',manifest_sha256='original',
        sampler=dict(initial,epoch=3,position=2))
    sampler['source_tokens']['web']=24
    state=dict(sampler=sampler)
    assert retained_sources(parent,state,control)['Web_blocks_consumed']==3
    bad=copy.deepcopy(state);bad['sampler']['streams']['story']['cursor']=4
    with pytest.raises(ValueError,match='short source'):retained_sources(parent,bad,control)
    bad=copy.deepcopy(state);bad['sampler']['streams']['web']['sampler']['position']=3
    with pytest.raises(ValueError,match='cursor advance'):retained_sources(parent,bad,control)
