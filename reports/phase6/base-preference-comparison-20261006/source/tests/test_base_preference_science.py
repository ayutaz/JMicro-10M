import copy
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from test_base_preference_trainer import fixture
from base_preference_trainer import CommonWebTrainer,PairPreferenceTrainer,PairQuotaSampler,build_reference
from base_preference_accounting import accounting,matched_exposure
import run_base_preference_comparison as study


def test_measured_budget_includes_probe_and_rejects_exhaustion(monkeypatch):
    monkeypatch.setattr(study.probe,'estimate_training',lambda r:({'measured':True},759.4))
    assert study.measured_budget({'GPU_seconds':36.1})==({'measured':True},759.4,36.1,1763.9)
    with pytest.raises(ValueError):study.measured_budget({'GPU_seconds':1041.})
    with pytest.raises(ValueError):study.measured_budget({'GPU_seconds':float('nan')})


def test_actual_common_native_terminal_accounting_and_cursor_tamper(tmp_path):
    web,parent,b,pairs=fixture(tmp_path);t=CommonWebTrainer(parent,web,95,b,'cpu',8,3);rows=[]
    while t.sampler.source_teachers!=t.sampler.goals:rows.append(t.step())
    cp=tmp_path/'common.pt';t.save(cp);state=torch.load(cp,weights_only=False);record=study.detail(t,cp,b,sum(r['seconds'] for r in rows))
    assert accounting(parent,state,record,rows,95,b)['positive_teacher_tokens']==95
    bad=copy.deepcopy(state);bad['sampler']['streams']['web']['sampler']['position']+=1
    changed=copy.deepcopy(record);changed['sampler']=bad['sampler']
    with pytest.raises(ValueError):accounting(parent,bad,changed,rows,95,b)


def test_actual_both_pair_quota_auxiliary_accounting_and_matched_stream(tmp_path):
    web,parent,b,pairs=fixture(tmp_path);common=CommonWebTrainer(parent,web,50,b,'cpu',8,3)
    while common.sampler.source_teachers!=common.sampler.goals:common.step()
    common.save(tmp_path/'common.pt');parent=torch.load(tmp_path/'common.pt',weights_only=False)
    ref=build_reference(common.model,PairQuotaSampler(pairs,37,2,web.byte_lengths,'unused'),'cpu','fp32');histories=[]
    for coefficient in (0.,.1):
        t=PairPreferenceTrainer(parent,web,pairs,37,coefficient,ref,b,'cpu',2);rows=[]
        while t.sampler.teachers!=37:rows.append(t.step())
        cp=tmp_path/f'{coefficient}.pt';t.save(cp);state=torch.load(cp,weights_only=False);record=study.detail(t,cp,b,sum(r['seconds'] for r in rows))
        assert accounting(parent,state,record,rows,37,b,pairs,web.byte_lengths)['positive_teacher_tokens']==37
        bad=copy.deepcopy(rows);bad[-1]['scored_rejected_positions']+=1
        with pytest.raises(ValueError):accounting(parent,state,record,bad,37,b,pairs,web.byte_lengths)
        histories.append(rows)
    assert matched_exposure(*histories)['exact_same_CE_input_and_auxiliary_exposure']
    histories[1][-1]['token_digest']='00'*32
    with pytest.raises(ValueError):matched_exposure(*histories)
