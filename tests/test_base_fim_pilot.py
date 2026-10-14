"""Budget, DEV-only opens, exact body scope, raw-bound notes and paired gate."""
import copy
import json
import math
from pathlib import Path
import sys
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_fim_pilot_protocol import validate_body,notes_scores,quality,EvaluationReadGuard
from run_base_fim_pilot import budget,matched


def body():
    rows=[dict(doc_id=str(i),body_tokens=1 if i<255 else 122088,
        scored_body_tokens=1 if i<255 else 122088,body_bytes=1 if i<255 else 471800,
        body_nll=1.,eos_nll=1.) for i in range(256)]
    return dict(split='dev',documents=256,limit_documents=256,context=1024,body_bytes=472055,
        body_tokens=122343,body_nll=256.,bpb=256/math.log(2)/472055,rows=rows)


@pytest.mark.parametrize('field,value',[('documents',255),('split','test'),('body_bytes',472054),('limit_documents',None)])
def test_wrong_corpus_or_partial_fullDEV_claim_rejected(field,value):
    good=body();validate_body(good);good[field]=value
    with pytest.raises(ValueError):validate_body(good)


def probe():
    return dict(all32_timing_seconds=[.1]*32,GPU_occupancy_seconds=9.,passed=True,
        all_state_and_history_resume_equal=True,science_forecast_seconds=1900,science_budget_eligible=True)


def test_budget_uses_all32_actual_timings_and_rejects_rescue():
    p=probe();assert budget(p)==1900
    p['all32_timing_seconds'][0]=1.
    with pytest.raises(ValueError):budget(p)


def test_failed_resume_or_probe_cannot_freeze_science():
    p=probe();p['all_state_and_history_resume_equal']=False
    with pytest.raises(ValueError):budget(p)


def test_sensitive_guard_observes_numpy_and_rejects_TEST_before_read(tmp_path):
    import numpy as np
    dev=tmp_path/'dev.bin';np.array([2,65,3],dtype='<u2').tofile(dev)
    test=tmp_path/'test.jsonl';test.write_text('INVALID_TEST_MUST_NOT_PARSE')
    guard=EvaluationReadGuard([tmp_path],[dev])
    with guard:
        actual=np.memmap(dev,dtype='<u2',mode='r');assert actual.tolist()==[2,65,3]
        with pytest.raises(ValueError,match='Forbidden'):test.read_text()
    assert str(dev.resolve()) in guard.paths and str(test.resolve()) not in guard.paths


def rows():
    return [dict(id=f'base-{i:03d}',stop_reason='stop_id',repetition=False,valid_utf8=True,
        role_leak=False,empty_response=False,text='X') for i in range(80)]


def notes():
    return dict(generation_sha256='pinned',reviewer='CPU fixture, not content evidence',independent_human_blind=False,
        notes=[[r['id'],2,2,2,1,'Fixture justification only; not an actual model judgment.'] for r in rows()])


@pytest.mark.parametrize('bad',['missing','duplicate','wrong_pin'])
def test_missing_duplicate_or_unbound_content_notes_rejected(bad):
    n=notes();notes_scores(rows(),n,'pinned')
    if bad=='missing':n['notes'].pop()
    elif bad=='duplicate':n['notes'][-1]=n['notes'][0]
    else:n['generation_sha256']='foreign'
    with pytest.raises(ValueError):notes_scores(rows(),n,'pinned')


def test_paired_signal_is_separate_from_Base_qualification_and_marker_failure():
    output=rows();old={r['id']:dict(grammar=0,relevance=0,coherence=0,completion=0) for r in output}
    new=copy.deepcopy(old)
    for key in list(new)[:20]:new[key]=dict(grammar=2,relevance=2,coherence=2,completion=1)
    ev=dict(outputs=output,body=dict(bpb=1.))
    q=quality(ev,ev,old,new);assert q['passed'] and not q['Base_qualified']
    contaminated=copy.deepcopy(ev);contaminated['outputs'][0]['text']='[FIM_MIDDLE]'
    assert not quality(ev,contaminated,old,new)['passed']
    assert not quality(ev,ev,old,old)['passed']


def test_content_completion_without_actual_stop_is_rejected():
    r=rows();r[0]['stop_reason']='max_new_tokens'
    with pytest.raises(ValueError):notes_scores(r,notes(),'pinned')


def test_native_stream_not_transformed_stream_must_match():
    c=dict(update=10000,supervised_tokens=94160195,source_teachers={'web':1},source_EOS={'web':1},original_body_bytes=1,token_digest='native')
    original=dict(counters=c,sampler=dict(kind='native',RNG='material'),scheduler=dict(total=2_000_000_000),model_config=dict(native=True))
    candidate=copy.deepcopy(original);candidate['sampler'].update(kind='FIM',FIM_counters=dict(native_stream_digest='native',applied_rows=1))
    assert all(matched(original,candidate).values())
    candidate['sampler']['FIM_counters']['native_stream_digest']='wrong_original_input'
    assert not all(matched(original,candidate).values())
