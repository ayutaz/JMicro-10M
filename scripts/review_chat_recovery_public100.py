"""Bind400 public diagnostic reviews to actual new GPU outputs and histories."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from collections import Counter
from chat_recovery_contract import ROOT,RUN,CONFIG
from answer_learning_common import read_json,save,ref,bound,now
from jmicro.tokenizer import Tokenizer
from review_chat_natural import validate_reply


def fingerprint(row):
    value={k:row[k] for k in ('id','category','mode','turn','final','objective','expected','messages')}
    # Execution duration is preserved in raw and is not a content judgment.
    # Every other response field, including IDs/bytes/prompt/mechanics, must match.
    value['response']={k:v for k,v in row['response'].items() if k!='seconds'}
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def old_index(tok):
    index={};ambiguous=set()
    for directory in (ROOT/'reports/phase7/chat-quality-100-20261017',ROOT/'reports/phase7/chat-recovery-20261018/control100'):
        raw=read_json(directory/'raw.json');notes=read_json(directory/'notes.json')
        assert notes['raw_sha256']==ref(directory/'raw.json')['sha256'] and len(notes['all200_literal_judgments'])==200
        for r,note in zip(raw['responses'],notes['all200_literal_judgments'],strict=True):
            value={k:r[k] for k in ('id','category','mode','turn','final','objective','expected')}
            value.update(messages=r['request']['messages'],response=r['answer']['response']);validate_reply(value['response'],tok,value['messages'],True)
            assert note['id']==r['id'] and note['turn']==r['turn']
            fp=fingerprint(value);rating={k:note[k] for k in ('grammar','relevance','context','factual_correct','rationale')}
            if fp in ambiguous:continue
            if fp in index and any(index[fp][k]!=rating[k] for k in ('grammar','relevance','context','factual_correct')):
                ambiguous.add(fp);index.pop(fp);continue
            index.setdefault(fp,dict(rating,source_notes=dict(ref(directory/'notes.json'),index=note['index']),fingerprint=fp))
    return index


def validate(arm):
    c=read_json(CONFIG);path=RUN/'public100'/arm/'raw.json';raw=read_json(path)
    assert raw['status']=='complete_pending_literal_review' and raw['config_sha256']==ref(CONFIG)['sha256']
    assert raw['device']=='cuda' and raw['precision']=='BF16/math' and raw['decoding']=='greedy' and raw['max_new_tokens']==32
    result=read_json(RUN/arm/'result.json');assert result['status']=='learning_complete' and raw['checkpoint']==result['checkpoint'];bound(raw['checkpoint'])
    assert raw['cases']==c['public100'];cases=read_json(bound(c['public100']))['cases'];tok=Tokenizer(bound(c['tokenizer']))
    offset=0
    for case in cases:
        history=[dict(m) for m in case['history']]
        for turn,target in enumerate(case['turns'],1):
            r=raw['responses'][offset];history.append(dict(role='user',content=target['user']))
            assert all(r[k]==case[k] for k in ('id','category','mode'))
            assert r['turn']==turn and r['final']==(turn==len(case['turns'])) and r['objective']==target['objective'] and r['expected']==target['expected'] and r['messages']==history
            validate_reply(r['response'],tok,history,True);history.append(dict(role='assistant',content=r['response']['text']));offset+=1
    assert offset==len(raw['responses'])==200
    return path,raw,tok


def packet(arm,start,count):
    path,raw,tok=validate(arm);target=path.with_name('packet.json')
    if target.exists():
        p=read_json(target);assert p['raw']==ref(path) and p['reviewer']==ref(__file__)
    else:
        index=old_index(tok);pending={};reused={}
        for i,row in enumerate(raw['responses']):
            fp=fingerprint(row)
            if fp in index:reused[str(i)]=index[fp]
            else:pending[str(i)]=dict(row,fingerprint=fp)
        p=dict(created_at=now(),raw=ref(path),reviewer=ref(__file__),pending=pending,reused=reused,
            rubric='Grammar/relevance/context0/1/2 and factual bool for objective only; all3=2 is task success',
            reuse='Full actual messages/expected/response dictionary except execution seconds exact; conflicting old grades require fresh review',
            no_keyword_semantic_scores=True);save(target,p)
    print(json.dumps(dict(total=200,pending=len(p['pending']),reused=len(p['reused']))))
    for ordinal,(index,row) in enumerate(list(p['pending'].items())[start:start+count],start):
        print(json.dumps(dict(pending_ordinal=ordinal,index=int(index),id=row['id'],turn=row['turn'],objective=row['objective'],expected=row['expected'],messages=row['messages'],response=row['response']['text']),ensure_ascii=False))


def finish(arm):
    path,raw,tok=validate(arm);p=read_json(path.with_name('packet.json'));assert p['raw']==ref(path) and p['reviewer']==ref(__file__)
    assert not path.with_name('notes.json').exists();notes={}
    for line in path.with_name('authored_indices.tsv').read_text(encoding='utf-8').splitlines():
        i,g,r,c,f,reason=line.split('\t',5);assert i in p['pending'] and i not in notes and g in '012' and r in '012' and c in '012' and f in ('0','1','-') and len(reason)>=12
        notes[i]=dict(grammar=int(g),relevance=int(r),context=int(c),factual_correct=None if f=='-' else f=='1',rationale=reason)
    assert set(notes)==set(p['pending'])
    for i,n in p['reused'].items():
        prior=read_json(bound(n['source_notes']));old=prior['all200_literal_judgments'][n['source_notes']['index']]
        assert all(old[k]==n[k] for k in ('grammar','relevance','context','factual_correct','rationale'))
        assert fingerprint(raw['responses'][int(i)])==n['fingerprint']
        notes[i]={k:n[k] for k in ('grammar','relevance','context','factual_correct','rationale')};notes[i]['reuse']=n
    assert set(notes)=={str(i) for i in range(200)}
    ordered=[]
    for i,row in enumerate(raw['responses']):
        n=notes[str(i)];assert (n['factual_correct'] is not None)==row['objective']
        passed=all(n[k]==2 for k in ('grammar','relevance','context'));assert not(passed and row['objective']) or n['factual_correct']
        ordered.append(dict(index=i,id=row['id'],turn=row['turn'],final=row['final'],category=row['category'],task_pass=passed,raw_fingerprint=fingerprint(row),**n))
    def summarize(indices):
        ns=[ordered[i] for i in indices];rs=[raw['responses'][i]['response'] for i in indices]
        return dict(n=len(ns),task_pass=sum(n['task_pass'] for n in ns),natural_grammar=sum(n['grammar']==2 for n in ns),
            objective=sum(n['factual_correct'] is not None for n in ns),factual_correct=sum(n['factual_correct'] is True for n in ns),
            natural_stops=sum(r['stop_reason'] in ('eot','eos') for r in rs),repetition_flag=sum(r['repetition'] for r in rs),
            empty=sum(r['empty_response'] for r in rs),invalid_UTF8=sum(not r['valid_utf8'] for r in rs),role_leak=sum(r['role_leak'] for r in rs),trim=sum(r['removed_turns']>0 for r in rs))
    finals=[i for i,r in enumerate(raw['responses']) if r['final']];assert len(finals)==100
    loops=[]
    for case_id in dict.fromkeys(r['id'] for r in raw['responses'] if r['mode']=='own'):
        sequence=[r['response']['text'] for r in raw['responses'] if r['id']==case_id];longest=run=1
        for a,b in zip(sequence,sequence[1:]):run=run+1 if a==b else 1;longest=max(longest,run)
        loops.append(dict(id=case_id,longest_identical_streak=longest))
    save(path.with_name('notes.json'),dict(created_at=now(),raw=ref(path),packet=ref(path.with_name('packet.json')),source=ref(__file__),
        authored=ref(path.with_name('authored_indices.tsv')),judgments=ordered,reviewer='Codex nonblind, not independent human'))
    save(path.with_name('summary.json'),dict(created_at=now(),raw=ref(path),notes=ref(path.with_name('notes.json')),final100=summarize(finals),all200=summarize(list(range(200))),
        categories={category:summarize([i for i in finals if raw['responses'][i]['category']==category]) for category in dict.fromkeys(r['category'] for r in raw['responses'])},
        cross_turn_loops=loops,loop_cases=sum(r['longest_identical_streak']>=3 for r in loops),all_actual_histories_IDs_bytes_verified=True,
        manual=len(p['pending']),reused=len(p['reused']),precision='GPU BF16/math; distinct from earlier CPU diagnostic'))
    print(json.dumps(read_json(path.with_name('summary.json'))['final100']))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['packet','finish']);p.add_argument('arm',choices=['C0','C1']);p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=20);a=p.parse_args()
    if a.mode=='packet':packet(a.arm,a.start,a.count)
    else:finish(a.arm)
