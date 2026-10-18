"""Check the new diagnosis boundary and independently replay selected teachers."""
import copy
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import pytest
from prepare_two_attribute_train import FACTS,messages_for,oracle
from jmicro.teacher_chat_training import TeacherBudgetSampler
from two_attribute_contract import preflight,BUDGET

@pytest.fixture(scope='module')
def prepared():return preflight()

def test_all64_current_labels_and_complete_target_masks(prepared):
    _,tok,rows=prepared
    for row in rows:
        assert oracle(row['messages'],FACTS[row['family']][1])==row['expected']
        w=list(tok.sft_windows(row['messages'],1025))[-1]
        assert [v for v in w['labels'] if v!=-100]==tok.encode(row['expected'])+[7]
        assert 2<=len(row['teacher_ids'])<=32 and w['removed_turns']==0

def test_correction_changes_only_intended_field():
    for f in range(8):
        for two in (False,True):
            _,_,before=messages_for(f,False,two,False);_,_,after=messages_for(f,True,two,True)
            changed=FACTS[f][1][FACTS[f][3]]
            assert [k for k in before if before[k]!=after[k]]==[changed]

def test_sampler_rejects_dev_and_duplicate(prepared):
    _,tok,rows=prepared
    changed=copy.deepcopy(rows[:1]);changed[0]['split']='dev'
    with pytest.raises(ValueError):TeacherBudgetSampler(changed,tok,1024,42,BUDGET,512,32)
    with pytest.raises(ValueError):TeacherBudgetSampler(rows[:1]*2,tok,1024,42,BUDGET,512,32)

def test_history_is_conditioning_not_extra_teacher(prepared):
    _,tok,rows=prepared;s=TeacherBudgetSampler(rows,tok,1024,42,BUDGET,512,32)
    assert len(s.windows)==64
    for w in s.windows:
        row=next(r for r in rows if r['doc_id']==w['doc_id'])
        assert w['target_message_index']==len(row['messages'])-1

def test_actual_dev_is_after_frozen_train_and_distinct(prepared):
    c,tok,rows=prepared
    from answer_learning_common import bound,read_json
    train=read_json(bound(c['TRAIN_manifest']));dev=read_json(bound(c['DEV']))
    assert train['created_at']<dev['created_at']
    train_prompts={tuple(r['prompt_ids']) for r in rows}
    assert all(tuple(tok.chat_prompt(r['messages'],992)[0]) not in train_prompts for group in dev['groups'].values() for r in group)
    assert len(dev['own'])==16 and all(len(r['turns'])==3 for r in dev['own'])

def test_finite_budgets_and_original_recipe(prepared):
    c,_,_=prepared
    assert c['teacher_budget']==250000 and c['limits_seconds']==dict(probe=600.,training=1800.,diagnosis=1800.,regression=10800.)
    assert c['max_new_tokens']==32 and c['spec']['batch']==32 and c['spec']['context']==1024
    assert c['parameter_count']==10001152 and not c['new_TEST_created'] and not c['Chat_adopted']

def test_cpu_sampler_resume_all_counters(prepared):
    _,tok,rows=prepared;a=TeacherBudgetSampler(rows,tok,1024,42,BUDGET,512,32)
    for _ in range(3):a.next_update()
    b=TeacherBudgetSampler(rows,tok,1024,42,BUDGET,512,32);b.load_state_dict(a.state_dict())
    aa,an,ab=a.next_update();bb,bn,bbt=b.next_update()
    assert (an,ab,a.state_dict())==(bn,bbt,b.state_dict())
    assert all((x==xx).all() and (y==yy).all() for (x,y),(xx,yy) in zip(aa,bb,strict=True))
