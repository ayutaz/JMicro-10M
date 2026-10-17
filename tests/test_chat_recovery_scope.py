"""Scope and interrupted-output workflow only; fixtures never evidence quality."""
import json
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import chat_recovery_contract as contract
import run_chat_recovery_sft as runner
from answer_learning_common import ref


@pytest.fixture
def owned_dev(tmp_path,monkeypatch):
    directory=tmp_path/'dev_suites';directory.mkdir()
    monkeypatch.setattr(contract,'DATA',tmp_path)
    rows=[]
    for i in range(80):
        n=3 if i<11 else 2 if i<24 else 1
        messages=[dict(role='user' if j%2==0 else 'assistant',content='fixture') for j in range(n*2-1)]
        rows.append(dict(family_id=str(i),split='dev',messages=messages))
    def write(values):
        path=directory/'new.jsonl';path.write_text(''.join(json.dumps(r)+'\n' for r in values),encoding='utf-8');return ref(path)
    return rows,write


def test_valid_exact_shape(owned_dev):
    rows,write=owned_dev;actual,contexts=contract.read_dev(write(rows))
    assert actual==rows and len(contexts)==24


@pytest.mark.parametrize('split',['train','test','mixed'])
def test_reject_non_dev_split(owned_dev,split):
    rows,write=owned_dev;rows[0]['split']=split
    with pytest.raises(AssertionError):contract.read_dev(write(rows))


def test_reject_duplicate_family(owned_dev):
    rows,write=owned_dev;rows[1]['family_id']=rows[0]['family_id']
    with pytest.raises(AssertionError):contract.read_dev(write(rows))


@pytest.mark.parametrize('relative',['TRAIN.jsonl','test/new.jsonl','dev_suites/test.jsonl','dev_suites/unknown.jsonl'])
def test_reject_path_before_open(tmp_path,monkeypatch,relative):
    monkeypatch.setattr(contract,'DATA',tmp_path)
    monkeypatch.setattr(contract,'bound',lambda _:pytest.fail('Rejected path reached a file read'))
    with pytest.raises(AssertionError):contract.read_dev(dict(path=str(tmp_path/relative),sha256='0'*64))


@pytest.fixture
def public_job(tmp_path,monkeypatch):
    monkeypatch.setattr(runner,'RUN',tmp_path/'run')
    cases=[dict(id=f'fixture{i}',history=[],category='fixture',mode='own',turns=[dict(user='a',expected='ok',objective=False),dict(user='b',expected='ok',objective=False)]) for i in range(100)]
    path=tmp_path/'cases.json';path.write_text(json.dumps(dict(cases=cases)),encoding='utf-8')
    c=dict(config_sha256='fixture-only',public100=ref(path));calls=[]
    def generate(*args):calls.append(args[2]);return dict(text='ok')
    monkeypatch.setattr(runner,'generate_reply',generate)
    return c,dict(path='fixture',sha256='fixture'),calls,tmp_path/'run/public100/C0/raw.json'


def test_interruption_resume_never_regenerates(public_job):
    c,checkpoint,calls,path=public_job;count=0
    def stop():
        nonlocal count
        count+=1
        if count==3:raise InterruptedError('fixture stop')
    with pytest.raises(InterruptedError):runner.public100(None,c,None,'C0',checkpoint,stop,lambda **_:None)
    assert len(calls)==2
    runner.public100(None,c,None,'C0',checkpoint,lambda:None,lambda **_:None)
    raw=json.loads(path.read_text());assert raw['status']=='complete_pending_literal_review' and len(raw['responses'])==len(calls)==200
    before=path.read_bytes();runner.public100(None,c,None,'C0',checkpoint,lambda:None,lambda **_:None)
    assert len(calls)==200 and before==path.read_bytes()


def test_failed_condition_refuses_relaunch(public_job):
    c,checkpoint,calls,path=public_job
    def fail():raise RuntimeError('fixture failure')
    with pytest.raises(RuntimeError):runner.public100(None,c,None,'C0',checkpoint,fail,lambda **_:None)
    before=path.read_bytes()
    with pytest.raises(AssertionError):runner.public100(None,c,None,'C0',checkpoint,lambda:None,lambda **_:None)
    assert before==path.read_bytes() and not calls


def test_changed_saved_history_refused(public_job):
    c,checkpoint,calls,path=public_job;count=0
    def stop():
        nonlocal count
        count+=1
        if count==2:raise InterruptedError('fixture stop')
    with pytest.raises(InterruptedError):runner.public100(None,c,None,'C0',checkpoint,stop,lambda **_:None)
    raw=json.loads(path.read_text());raw['responses'][0]['messages'][0]['content']='tampered'
    path.write_text(json.dumps(raw))
    with pytest.raises(AssertionError):runner.public100(None,c,None,'C0',checkpoint,lambda:None,lambda **_:None)
    assert len(calls)==1
