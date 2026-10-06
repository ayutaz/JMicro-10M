import copy
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
import run_source_order_condition_comparison as study
from review_source_order_condition_comparison import retained_sources


def test_fixed_source_order_same_teachers_base_only_and_actual_floor_are_required():
    c=dict(failed_probe_GPU_seconds=0,research_kind=study.KIND,arms={study.ARM:study.GOALS},outcome_weights={study.ARM:1},
        teachers_per_new_arm=100000000,total_comparison_teachers=200000000,total_new_GPU_ceiling_seconds=900,
        peak_lr=.00001,optimizer_policy='inherit',source_order=list(study.SOURCE_ORDER),
        shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),
        loss='ordinary original body+EOS CE, outcome weight1',Base_adopted=False,Chat_adopted=False,
        quantization_started=False,protected_test_used=False,requested_five_steps_complete=False,quality_criteria_unchanged=True)
    study.scope(c)
    for key,value in (('source_order',list(reversed(study.SOURCE_ORDER))),('peak_lr',.0002),
        ('teachers_per_new_arm',500000000),('Chat_adopted',True),('protected_test_used',True)):
        with pytest.raises(ValueError):study.scope({**c,key:value})
    assert study.inherited_lr_preserved(.00001)
    assert not study.inherited_lr_preserved(.0001)


def test_all_four_terminal_cursors_and_counters_must_match_cached_control():
    cursor=dict(seed=42,epoch=2,position=99,context=8,blocks=100)
    parent=dict(sampler=dict(kind='eos-pilot-mixture-v1',position=0,routes=[],short=dict(position=0),
        web=cursor,source_tokens=dict(web=0,short=0),source_eos=dict(web=0,short=0)),
        optimizer=dict(param_groups=[dict(lr=.00001)]),shard_manifest_sha256='web-source')
    sampler=dict(streams={g:dict(cursor=4) for g in study.SOURCE_ORDER})
    sampler['streams']['web']=dict(kind='actual-parent-Web-block-cursor-v1',manifest_sha256='web-source',
        sampler=dict(cursor,epoch=3,position=2))
    for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):
        sampler[key]=dict.fromkeys(study.SOURCE_ORDER,0)
    sampler['source_tokens']['web']=24
    state=dict(sampler=sampler);control=copy.deepcopy(state)
    assert retained_sources(parent,state,control)['all_four_source_cursors_and_accounting_equal']
    for source in study.SOURCE_ORDER:
        bad=copy.deepcopy(state);bad['sampler']['streams'][source]['changed']=True
        with pytest.raises(ValueError):retained_sources(parent,bad,control)
        bad=copy.deepcopy(state);bad['sampler']['source_tokens'][source]+=8
        with pytest.raises(ValueError):retained_sources(parent,bad,control)
