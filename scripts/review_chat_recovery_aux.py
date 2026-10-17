"""Read and bind every intermediate and actual-browser response literally."""
import argparse
import json
from chat_recovery_contract import RUN,CONFIG
from answer_learning_common import save,ref,bound,read_json,now
from jmicro.tokenizer import Tokenizer
from review_chat_natural import validate_reply
from jmicro.chat_review import RUBRIC


def items(kind,arm,point):
    c=read_json(CONFIG);tok=Tokenizer(bound(c['tokenizer']))
    if kind=='diagnostic':
        path=RUN/'diagnostics'/arm/f'{point}.json';raw=read_json(path)
        assert raw['config_sha256']==ref(CONFIG)['sha256'] and not raw['protected_TEST_used']
        rows=[dict(id=r['case']['id'],messages=r['case']['messages'],response=r['response']) for r in raw['outputs']]
        authored=path.with_name(f'{point}_authored.json');notes=path.with_name(f'{point}_notes.json');expected=10
    else:
        path=RUN/'practical'/arm/'browser.json';raw=read_json(path)
        assert raw['status']=='all18_actual_browser_responses_pending_literal_review'
        assert raw['model']['config_sha256']==ref(CONFIG)['sha256'] and raw['model']['arm']==arm
        assert raw['actual_history_reset_and_DOM_API_verified'] and not raw['mocked_requests']
        assert len(raw['network'])==18 and len(raw['conversations'])==len(raw['fixed_cases'])==3
        rows=[]
        for group,(case,conversation) in enumerate(zip(raw['fixed_cases'],raw['conversations'],strict=True)):
            assert case['name']==conversation['name'] and conversation['reset']['messages']==0
            history=[]
            for turn,(user,ui) in enumerate(zip(case['users'],conversation['turns'],strict=True)):
                r=raw['network'][6*group+turn];history.append(dict(role='user',content=user))
                assert r['request']['messages']==history and r['request']['max_new_tokens']==32 and ui['user']==user
                response=r['response']['response'];assert response['text']==ui['UI']['messages'][-1]['text']
                rows.append(dict(id=f'{case["name"]}-{turn+1}',messages=[dict(m) for m in history],response=response))
                history.append(dict(role='assistant',content=response['text']))
        authored=path.with_name('authored.json');notes=path.with_name('notes.json');expected=18
    assert len(rows)==expected
    for row in rows:validate_reply(row['response'],tok,row['messages'],True)
    return path,rows,authored,notes


def main():
    p=argparse.ArgumentParser();p.add_argument('kind',choices=['diagnostic','practical']);p.add_argument('arm',choices=['C0','C1'])
    p.add_argument('--point',choices=['250000','500000'],default='250000');p.add_argument('--finish',action='store_true');a=p.parse_args()
    path,rows,authored_path,notes_path=items(a.kind,a.arm,a.point)
    if not a.finish:
        print(json.dumps(dict(raw=ref(path),rubric=RUBRIC),ensure_ascii=False))
        for i,row in enumerate(rows):print(json.dumps(dict(index=i,id=row['id'],messages=row['messages'],text=row['response']['text'],stop=row['response']['stop_reason']),ensure_ascii=False))
        return
    assert not notes_path.exists(),'Keep completed notes immutable'
    authored=read_json(authored_path);assert len(authored)==len(rows);judgments=[]
    for row,(g,r,c,reason) in zip(rows,authored,strict=True):
        assert all(type(v) is int and v in (0,1,2) for v in (g,r,c)) and len(reason)>=12
        judgments.append(dict(id=row['id'],grammar=g,relevance=r,context=c,rationale=reason))
    save(notes_path,dict(raw=ref(path),authored=ref(authored_path),all_reviewed=True,responses=len(rows),judgments=judgments,rubric=RUBRIC,
        reviewer='Codex nonblind, actual full history; not independent human',created_at=now(),source=ref(__file__),
        content=sum(n['grammar']==n['relevance']==2 for n in judgments),protected_TEST_used=False,primary_model_selection=False,
        practical_not_combined_with_DEV=a.kind=='practical'))
    print(f'All {len(rows)} literal notes bound: {notes_path}')


if __name__=='__main__':main()
