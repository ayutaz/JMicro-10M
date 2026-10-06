"""Reject malformed actual completed CPU accounting, not quality assertions."""
import copy
import json
import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from test_parameter_displacement_anchor import mixed_fixture
import review_parameter_displacement_anchor as review


def test_real_CPU_terminal_ledger_anchor_and_full_objective_are_required(tmp_path,monkeypatch):
    s=review.study;pool,parent,b,positive=mixed_fixture(tmp_path)
    goals=dict(web=19,story=11,ordinary_textbook=7,conditional_textbook=16)
    monkeypatch.setattr(s,'GOALS',goals);monkeypatch.setattr(s,'TOTAL',sum(goals.values()))
    cfg=tmp_path/'config.json';cfg.write_text('{}');monkeypatch.setattr(s,'CONFIG',cfg)
    c=dict(parent=b['parent'],coefficients={'parameter_anchor':.04161064039180984},
        positive_data=dict(manifest_sha256=positive.manifest_sha256),original_web=dict(path=str(pool.directory)))
    binding=s.binding(c,cfg,'parameter_anchor')
    t=s.ParameterAnchorTrainer(parent,pool,pool,positive,goals,binding,c['coefficients']['parameter_anchor'],'cpu',8,3)
    history=[]
    while t.sampler.source_teachers!=goals:history.append(t.step())
    cp=tmp_path/'terminal.pt';t.save(cp);state=torch.load(cp,weights_only=False)
    record=dict(s.prior.detail(t,cp,binding,1.),parameter_penalty_teacher_tokens=0,anchor_initial_digest=t.anchor_initial_digest,
        sampler=t.sampler.state_dict(),token_digest=t.token_digest)
    assert review.accounting(parent,state,record,history,c,'parameter_anchor')['teachers']==53
    bad=copy.deepcopy(history);bad[-1]['parameter_penalty_teacher_tokens']=1
    with pytest.raises(ValueError):review.accounting(parent,state,record,bad,c,'parameter_anchor')
    bad=copy.deepcopy(history);bad[-1]['parameter_penalty']+=1
    with pytest.raises(ValueError):review.accounting(parent,state,record,bad,c,'parameter_anchor')
    bad=copy.deepcopy(state);bad['lineage']['anchor_initial_digest']='wrong'
    with pytest.raises(ValueError,match='anchor'):review.accounting(parent,bad,record,history,c,'parameter_anchor')
    with pytest.raises(ValueError):review.accounting(parent,state,record,history[:-1],c,'parameter_anchor')
