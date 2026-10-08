"""Accounting, contradictory histories and exact resume; not model quality."""
from pathlib import Path
import json
from types import SimpleNamespace
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
import pytest
import torch
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from natural_context_contrast_trainer import host
from run_base_residual_capacity import Trainer, pack, validate_rows, conflicting_histories, accuracy


def rows():
    return [dict(id=str(i),source='train',input_ids=[2,8+i,14,15],gold_targets=[8+i,14,15,3],
        teacher_tokens=4,prompt_ids=[2,8+i],continuation_gold_ids=[14,15,3],
        actual_first_window_body_bytes_hex='6162') for i in range(6)]


def parent():
    config=json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config.update(vocab_size=32,hidden_size=16,intermediate_size=32,num_hidden_layers=1,
        num_attention_heads=2,num_key_value_heads=1,head_dim=8,rotary_dim=8,
        attention_scale=8**-.5,max_position_embeddings=64,qk_norm_type='none')
    model=JMicroModel(config)
    return dict(model_config=model.config,model=host(model.state_dict()))


def test_partial_budget_keeps_original_shift_and_never_creates_EOS():
    x,y,stats,cursor=pack(rows(),0,80,5,'cpu')
    assert stats['supervised_tokens']==5 and stats['EOS_targets']==1 and cursor==80
    assert y[0].tolist()==[8,14,15,3] and y[1].tolist()==[9,-100,-100,-100]
    assert int((y!=-100).sum())==5 and stats['completed_original_body_bytes']==2
    assert stats['source_teacher_tokens']=={'train':5}


def test_cycle_covers_each_unit_equally_after_three_batch80_updates():
    counts={str(i):0 for i in range(6)}
    cursor=0
    for _ in range(3):
        _,_,stats,cursor=pack(rows(),cursor,80,999999,'cpu')
        for unit,count in stats['draws']:
            counts[unit]+=1
            assert count==4
    assert set(counts.values())=={40} and cursor==240
    invalid=rows(); invalid[0]['gold_targets'][-1]=8
    with pytest.raises(ValueError,match='shift'):
        validate_rows(invalid)


def test_same_BOS_conflicts_prove_full_target100percent_impossible():
    conflicts=conflicting_histories(rows())
    assert len(conflicts)==1 and conflicts[0]['input_history']==[2]
    assert conflicts[0]['unavoidable_argmax_errors']==5
    assert all(pos< len(rows()[int(unit)]['prompt_ids'])-1
               for c in conflicts for unit,pos,_ in c['positions'])
    class ConditionalExact(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.anchor=torch.nn.Parameter(torch.zeros(1))
        def forward(self,x):
            logits=torch.zeros(1,4,32)
            for i,value in enumerate([8,14,15,3]): logits[0,i,value]=1
            return SimpleNamespace(logits=logits)
    measured=accuracy(ConditionalExact(),rows(),lambda:None)
    assert sum(r['correct'] for r in measured)==19
    assert not all(r['all_targets_exact'] for r in measured)
    assert all(r['all_conditioned_targets_exact'] for r in measured)


def test_completed_update_exact_resume_includes_fresh_Adam_cycle_and_partial_budget(tmp_path):
    torch.set_num_threads(1)
    p=parent(); units=rows()
    a=Trainer(p,units,{'probe':True},device='cpu',batch=8)
    h=[a.step(),a.step(7)]; expected=a.state()
    b=Trainer(p,units,{'probe':True},device='cpu',batch=8)
    assert equal_state(h[0],b.step())
    b.save(tmp_path/'saved.pt')
    c=Trainer(p,units,{'probe':True},device='cpu',batch=8); c.load(tmp_path/'saved.pt')
    assert equal_state(h[1],c.step(7))
    assert equal_state(expected,c.state())
    assert c.counters['supervised_tokens']==39 and c.cursor==16
