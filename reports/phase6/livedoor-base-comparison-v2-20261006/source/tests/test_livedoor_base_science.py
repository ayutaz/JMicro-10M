import copy
import math
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import run_livedoor_base as study
from livedoor_base_accounting import accounting
from livedoor_base_trainer import NewsBaseTrainer
from test_livedoor_base_trainer import prefix_fixture


def test_measured_total_budget_accounts_failed_verification(monkeypatch):
    monkeypatch.setattr(study.probe, 'estimate_training', lambda _:({'updates':810},449.25))
    timing, estimate, used, budget=study.measured_budget({'GPU_seconds':28.335},1.419)
    assert used==28.335+1.419 and math.isclose(used+budget,1800.) and estimate==449.25
    with pytest.raises(ValueError): study.measured_budget({'GPU_seconds':28.335},1400.)


def test_pure_Web_continuation_reuses_prefix_without_relearning():
    parent={'sampler':{'source_teachers':{'web':study.REUSED}}}
    row=dict(update=322686, source_teachers=dict(web=32000, authored_news=0), tokens_seen=10, supervised_tokens=11,
        body_bytes_seen=12, token_digest='aa', focus_token_digest='bb', lr=.00001, loss=2.5, gradient_norm=.7)
    old=dict(row, source_teachers=dict(web=study.REUSED+32000, story=0, ordinary_textbook=0, conditional_textbook=0))
    assert study.common_web_continuation([row, dict(row, update=322687, source_teachers=dict(web=study.GOALS['web'],authored_news=1))],[old],parent)==1
    bad=copy.deepcopy(old); bad['token_digest']='cc'
    with pytest.raises(ValueError): study.common_web_continuation([row],[bad],parent)


def test_real_CPU_inherited_news_terminal_accounting_and_rejection(tmp_path):
    pool, parent, binding=prefix_fixture(tmp_path); goals=dict(web=11, authored_news=100)
    trainer=NewsBaseTrainer(parent,pool,pool,goals,binding,'cpu',8,3); rows=[]
    while trainer.sampler.source_teachers != goals: rows.append(trainer.step())
    trainer.save(tmp_path/'terminal.pt'); state=torch.load(tmp_path/'terminal.pt',weights_only=False)
    record=dict(binding=binding, additional_supervised_tokens=sum(goals.values()), sampler=state['sampler'],
        token_digest=state['token_digest'], focus_token_digest=state['focus_token_digest'])
    audit=accounting(parent,state,record,rows,goals,binding)
    assert audit['new_teacher_tokens']==111 and audit['native_Adam_and_scheduler_inherited']
    bad=copy.deepcopy(state); bad['optimizer']['param_groups'][0]['lr']=.0001
    with pytest.raises(ValueError): accounting(parent,bad,record,rows,goals,binding)
    bad=copy.deepcopy(rows); bad[-1]['source_teachers']['authored_news']-=1
    with pytest.raises(ValueError): accounting(parent,state,record,bad,goals,binding)
