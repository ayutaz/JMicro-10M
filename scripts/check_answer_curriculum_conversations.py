"""Five real two-turn UI conversations; keep actual Assistant history and failures."""
import argparse
import json
from pathlib import Path
import time
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from datetime import datetime,timezone
import hashlib

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'reports/phase7/chat-answer-learning-20261017/curriculum-main-resource-v2'
SHA='e9172f65215fe44f2a94f5c0e9f1429175a27917b3d32b3e09c848cb318e9e46'
CASES=[('greeting',['こんにちは。今日は少し話せますか？','ありがとう、また来ますね。']),
    ('daily',['片付けを始めるきっかけを一つ教えて。','机の上から始めることにしました。']),
    ('memory',['私の飼い猫はスピカという名前です。','うちの猫の名前、何だったか教えて。']),
    ('correction',['打ち合わせは水曜日に行います。','予定が変わって金曜日になりました。今の打ち合わせは何曜日？']),
    ('missing',['私は来週、映画を見に行きます。','映画を見始める時刻は何時ですか？'])]


def main(arm):
    port=7864 if arm=='C1' else 7865;url=f'http://127.0.0.1:{port}';target=RUN/'practical'/arm/'raw.json'
    assert not target.exists(),'Inspect completed/partial real interaction; never overwrite failures'
    with urlopen(url+'/api/model',timeout=5) as response:model=json.load(response)
    assert model['config_sha256']==SHA and model['arm']==arm and model['parameters']==10001152 and model['max_new_tokens']==32
    started=time.monotonic();report=dict(status='running',arm=arm,model=model,generation_cap=32,device='CPU',precision='FP32',
        conversations=[],CPU_wall_limit_seconds=180,semantic_reviews_pending=True,DEV_scores_not_combined=True,
        protected_TEST_used=False,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    def write():
        target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(report,ensure_ascii=False,indent=2))
    write()
    try:
        for category,users in CASES:
            history=[];conversation=dict(category=category,turns=[]);report['conversations'].append(conversation)
            for text in users:
                assert time.monotonic()-started<170;history=history+[dict(role='user',content=text)]
                payload=dict(messages=history,max_new_tokens=32)
                request=Request(url+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
                with urlopen(request,timeout=min(60,180-(time.monotonic()-started))) as response:answer=json.load(response)
                row=answer['response'];assert row['max_new_tokens']==32 and row['generated_tokens']<=32
                conversation['turns'].append(dict(request=payload,response=row));history=history+[dict(role='assistant',content=row['text'])];write()
                print(json.dumps(dict(arm=arm,category=category,user=text,response=row['text'],stop=row['stop_reason']),ensure_ascii=False),flush=True)
        rows=[t['response'] for c in report['conversations'] for t in c['turns']];assert len(rows)==10
        report.update(status='all10_actual_responses_saved_pending_content_notes',CPU_wall_seconds=time.monotonic()-started,
            natural_stops=sum(r['stop_reason'] in ('eot','eos') for r in rows),empty=sum(r['empty_response'] for r in rows),
            unicode_failures=sum(not r['valid_utf8'] for r in rows),repetitions=sum(r['repetition'] for r in rows),
            full_histories=all(r['full_history_retained'] for r in rows))
    except BaseException as error:
        report.update(status='failed_partial_preserved',error=repr(error),CPU_wall_seconds=time.monotonic()-started)
        if isinstance(error,HTTPError):report['HTTP_error_body']=error.read().decode('utf-8',errors='replace')
        raise
    finally:report['updated_at']=datetime.now(timezone.utc).isoformat();write()


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('arm',choices=['C0','C1']);main(p.parse_args().arm)
