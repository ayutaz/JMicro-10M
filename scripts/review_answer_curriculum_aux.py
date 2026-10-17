"""Show and bind explicit notes for all40 intermediate and20 actual UI replies."""
import argparse
import json
from answer_learning_common import save,ref,bound,read_json,now
from run_answer_curriculum_resource_v2 import CONFIG,RUN
from jmicro.tokenizer import Tokenizer
from review_chat_natural import validate_reply
from jmicro.chat_review import RUBRIC


def items(kind,arm,point):
    c=read_json(CONFIG);tok=Tokenizer(bound(c['tokenizer']))
    if kind=='diagnostic':
        path=RUN/'diagnostics'/arm/f'{point}.json';raw=read_json(path)
        assert raw['config_sha256']==ref(CONFIG)['sha256'] and len(raw['outputs'])==10 and not raw['protected_TEST_used']
        rows=[dict(id=r['case']['id'],messages=r['case']['messages'],response=r['response']) for r in raw['outputs']]
        authored=path.with_name(f'{point}_authored.json');notes=path.with_name(f'{point}_notes.json')
    else:
        path=RUN/'practical'/arm/'raw.json';raw=read_json(path)
        assert raw['model']['config_sha256']==ref(CONFIG)['sha256'] and raw['model']['arm']==arm
        assert raw['status']=='all10_actual_responses_saved_pending_content_notes'
        rows=[]
        for conversation in raw['conversations']:
            history=[]
            for i,turn in enumerate(conversation['turns'],1):
                messages=turn['request']['messages'];assert messages[:-1]==history
                rows.append(dict(id=f"{conversation['category']}-{i}",messages=messages,response=turn['response']))
                history=messages+[dict(role='assistant',content=turn['response']['text'])]
        authored=path.with_name('authored.json');notes=path.with_name('notes.json')
    assert len(rows)==10
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
    assert not notes_path.exists(),'Do not overwrite completed notes'
    authored=read_json(authored_path);assert len(authored)==10
    judgments=[]
    for row,(g,r,c,reason) in zip(rows,authored,strict=True):
        assert all(type(v) is int and v in (0,1,2) for v in (g,r,c)) and len(reason)>=12
        judgments.append(dict(id=row['id'],grammar=g,relevance=r,context=c,rationale=reason))
    save(notes_path,dict(raw=ref(path),authored=ref(authored_path),all10_reviewed=True,judgments=judgments,rubric=RUBRIC,
        reviewer='Codex nonblind, actual raw and full history; not independent human',created_at=now(),source=ref(__file__),
        content=sum(g['grammar']==g['relevance']==2 for g in judgments),protected_TEST_used=False,
        primary_model_selection=False,practical_not_combined_with_DEV=a.kind=='practical'))
    print('All10 explicit content notes bound: '+str(notes_path))


if __name__=='__main__':main()
