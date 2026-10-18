"""Literal240 review with every actual generated-history token/byte validated."""
import argparse
import hashlib
import json
from two_attribute_contract import RUN,CONFIG,preflight
from answer_learning_common import read_json,save,ref,now
from review_chat_natural import validate_reply

def items():
    c,tok,rows=preflight();out=[]
    for point,expected_count in (('before',64),('after',176)):
        path=RUN/f'diagnosis/{point}.json';raw=read_json(path)
        assert raw['status']=='complete_pending_literal_review' and raw['config_sha256']==c['config_sha256'] and len(raw['responses'])==expected_count
        dev=read_json(c['DEV']['path']);groups={'TRAIN':rows}
        if point=='after':groups.update(dev['groups'])
        expected=[]
        for group,cases in groups.items():
            for case in cases:expected.append((group,case.get('id',case.get('doc_id')),case,case['messages'][:-1] if group=='TRAIN' else case['messages']))
        for i,(group,uid,case,messages) in enumerate(expected):
            r=raw['responses'][i];assert r['case']==case and r['group']==group and r['id']==uid and r['messages']==messages
            validate_reply(r['response'],tok,messages,True)
            out.append(dict(index=len(out),point=point,raw=ref(path),raw_index=i,group=group,id=uid,case=case,expected=case['expected'],messages=messages,response=r['response']))
        if point=='after':
            offset=len(expected)
            for case in dev['own']:
                history=[]
                for turn,target in enumerate(case['turns'],1):
                    history.append(dict(role='user',content=target['user']));r=raw['responses'][offset]
                    assert r['case']==case and r['id']==case['id'] and r['turn']==turn and r['target']==target and r['messages']==history and r['final']==(turn==3)
                    validate_reply(r['response'],tok,history,True)
                    out.append(dict(index=len(out),point=point,raw=ref(path),raw_index=offset,group='own',id=r['id'],turn=turn,final=turn==3,case=case,target=target,expected=target['expected'],messages=[dict(m) for m in history],response=r['response']))
                    history.append(dict(role='assistant',content=r['response']['text']));offset+=1
            assert offset==176
    assert len(out)==240;return out

def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['packet','finish']);p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=32);a=p.parse_args();rows=items();path=RUN/'diagnosis/notes.json'
    if a.mode=='packet':
        for row in rows[a.start:a.start+a.count]:
            print(json.dumps(dict(i=row['index'],point=row['point'],group=row['group'],id=row['id'],turn=row.get('turn'),expected=row['expected'],
                messages=row['messages'],reply=row['response']['text'],stop=row['response']['stop_reason'],UTF8=row['response']['valid_utf8']),ensure_ascii=False))
        return
    assert not path.exists();authored={}
    scorepath=RUN/'diagnosis/authored.tsv'
    for line in scorepath.read_text().splitlines():
        i,g,r,c,f,reason=line.split('\t',5);i=int(i);assert i not in authored and g in '012' and r in '012' and c in '012' and f in ('0','1','-') and len(reason)>=12
        authored[i]=dict(grammar=int(g),relevance=int(r),context=int(c),factual_correct=None if f=='-' else f=='1',rationale=reason)
    assert set(authored)==set(range(240));notes=[]
    for row in rows:
        n=authored[row['index']];objective=not(row['group']=='own' and row['turn']==1)
        assert (n['factual_correct'] is not None)==objective
        if objective and all(n[k]==2 for k in ('grammar','relevance','context')):assert n['factual_correct']
        notes.append(dict(row,judgment=n))
    save(path,dict(created_at=now(),config=ref(CONFIG),reviewer_source=ref(__file__),authored=ref(scorepath),
        judgments=notes,total=240,all_actual_histories_IDs_bytes_verified=True,reviewer='Codex nonblind, not independent human',new_TEST=False))
    print('All240 literal judgments bound to raw outputs')

if __name__=='__main__':main()
