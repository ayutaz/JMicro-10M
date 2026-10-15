"""No corpus/CUDA: protect exact known-batch identity and scoped CPU attribution."""
import copy
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace as Row

import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from profile_rdrop_input_pack import scope,assert_scope,cpu_oracle,assert_known_next,summarize,SCOPES


@pytest.mark.parametrize('key,value',[
    ('profiled_batches',2),('warmup_batches',1),('next_update',8),('input_shape',[48,1024]),
    ('main_teachers',1),('model_instantiated',True),('forward_calls',1),('backward_calls',1),
    ('optimizer_updates',1),('scientific_teacher_positions',1),('DEV_opened',True),('TEST_opened',True),
    ('weights_saved',True),('science_forecast',True),('raw_text_or_ID_export',True),
    ('CPU_profiler_only',False),('new_GPU_ceiling_seconds',6),('prior_technical_GPU_seconds',0.),
    ('prior_completed_science_GPU_seconds',0.),('prior_total_GPU_seconds',136.72787685703952),
    ('original_technical_cap_seconds',181),('original_total_GPU_cap_seconds',4801),
])
def test_single_known_batch_no_learning_no_retiming_no_budget_reset(key,value):
    c=copy.deepcopy(scope())
    assert_scope(c)
    c[key]=value
    with pytest.raises(ValueError): assert_scope(c)


def test_oracle_preserves_overlap_holes_original_EOS_and_right_PAD():
    rows=[dict(input_ids=[2,8,9,10],target_ids=[-100,9,-100,3]),
          dict(input_ids=[2,17],target_ids=[17,3])]
    before=copy.deepcopy(rows)
    ids,targets=cpu_oracle(rows)
    assert ids.tolist()==[[2,8,9,10],[2,17,0,0]]
    assert targets.tolist()==[[-100,9,-100,3],[17,3,-100,-100]]
    assert rows==before and ids.dtype==targets.dtype==torch.long
    for bad in ([],[dict(input_ids=[],target_ids=[])],[dict(input_ids=[2],target_ids=[3,3])]):
        with pytest.raises(ValueError): cpu_oracle(bad)


def known():
    rows=[dict(input_ids=[2]+[8]*582,target_ids=[-100]*453+[8]*129+[3],
        index_byte_position=i,index_record_sha256='a'*64,target_first=1,target_end=584,
        teacher_tokens=130) for i in range(48)]
    rows[-1]['teacher_tokens']=163
    rows[-1]['target_ids']=[-100]*420+[8]*162+[3]
    state=dict(counters=dict(update=6,token_digest='0'*64))
    trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows]
    stream=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
    want=dict(update=7,draw_trace=json.loads(json.dumps(trace)),
        token_digest=hashlib.sha256(bytes.fromhex('0'*64)+stream).hexdigest(),
        source_teachers=dict(web=8),CE_targets_this_update=6273,main_physical_inputs_this_update=48*583)
    return state,rows,dict(consumed=dict(web=8)),want


def test_exact_known_stream_not_just_shape_or_teacher_count():
    state,rows,after,want=known()
    assert_known_next(state,rows,after,want)
    rows[0]['input_ids'][1]=9
    with pytest.raises(ValueError): assert_known_next(state,rows,after,want)
    state,rows,after,want=known()
    after['consumed']['web']+=1
    with pytest.raises(ValueError): assert_known_next(state,rows,after,want)
    state,rows,after,want=known()
    want['draw_trace'][0][0]+=1
    with pytest.raises(ValueError): assert_known_next(state,rows,after,want)


def event(name,parent=None,cpu=1.,inclusive=2.,device='DeviceType.CPU'):
    return Row(name=name,cpu_parent=parent,self_cpu_time_total=cpu,cpu_time_total=inclusive,device_type=device)


def test_nested_copies_attributed_to_correct_scope_no_inclusive_double_count():
    a,b=event(SCOPES[0]),event(SCOPES[1])
    target_parent=event('aten::to',b)
    events=[a,b,event('aten::_to_copy',a),target_parent,
        event('aten::_to_copy',target_parent),event('aten::_to_copy',target_parent,cpu=-.1),event('outside')]
    rows=summarize(events)
    copies=[r for r in rows if r['scope']==SCOPES[1] and r['name']=='aten::_to_copy']
    assert copies==[dict(scope=SCOPES[1],name='aten::_to_copy',count=2,CPU_self_us=.9,CPU_inclusive_us=4.)]
    assert any(r['scope']=='outside_scopes' for r in rows)
    with pytest.raises(ValueError): summarize([event('cuda',device='DeviceType.CUDA')])
    with pytest.raises(ValueError): summarize([event('nonfinite',cpu=float('nan'))])
