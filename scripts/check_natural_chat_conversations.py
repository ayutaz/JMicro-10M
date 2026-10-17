"""Five actual2-turn conversations against a completed CPU trial UI.

Practical checks are separate from the frozen CUDA BF16 DEV comparison.
The client feeds back actual generated text, saves all failures, and never
substitutes canned Assistant replies. No dataset/TEST reader is imported.
"""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import time
from urllib.error import HTTPError
from urllib.request import Request,urlopen

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'reports/phase7/chat-natural-sft-20261017'
CASES=[
    ('greeting',['こんにちは。少しお話ししたいです。','ありがとう。またお話ししましょう。']),
    ('food',['好きな食べ物はありますか？','私はみかんが好きです。みかんは好きですか？']),
    ('hobby',['家でできる趣味を一つ教えてください。','絵を描くことにしました。何を用意すればいいですか？']),
    ('memory',['私の飼っているウサギはソラといいます。','私のウサギの名前を覚えていますか？']),
    ('correction',['待ち合わせは日曜の午後です。','日曜ではなく月曜に変更しました。今の曜日は何ですか？'])]


def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def main(arm):
    port=7862 if arm=='C1' else 7863
    url=f'http://127.0.0.1:{port}'
    target=RUN/'practical'/arm/'raw.json'
    assert not target.exists(),'Preserve completed or failed practical checks before any recovery'
    with urlopen(url+'/api/model',timeout=5) as response:model=json.load(response)
    assert model['name']=='JMicro-10M '+arm and model['parameters']==10001152 and model['max_new_tokens']==32
    assert model['config_sha256']=='ec0b61b2961ef9294cb840cb86ad6f5ba291ea1c4a0213d0404e9fa87cdb464d'
    started=time.monotonic()
    report=dict(status='running',arm=arm,model=model,created_at=datetime.now(timezone.utc).isoformat(),
        generation_cap=32,device='CPU',precision='FP32',conversations=[],CPU_wall_limit_seconds=180,
        semantic_reviews_pending=True,DEV_scores_not_combined=True,protected_TEST_used=False,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    write(target,report)
    try:
        for category,users in CASES:
            history=[];conversation=dict(category=category,turns=[])
            report['conversations'].append(conversation)
            for text in users:
                assert time.monotonic()-started<170
                request_history=history+[dict(role='user',content=text)]
                payload=dict(messages=request_history,max_new_tokens=32)
                request=Request(url+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),
                    headers={'Content-Type':'application/json'},method='POST')
                with urlopen(request,timeout=min(60,180-(time.monotonic()-started))) as response:
                    answer=json.load(response)
                row=answer['response']
                assert row['max_new_tokens']==32 and row['generated_tokens']<=32
                conversation['turns'].append(dict(request=payload,response=row))
                history=request_history+[dict(role='assistant',content=row['text'])]
                write(target,report)
                print(json.dumps(dict(arm=arm,category=category,user=text,response=row['text'],stop=row['stop_reason']),ensure_ascii=False),flush=True)
        rows=[t['response'] for c in report['conversations'] for t in c['turns']]
        assert len(rows)==10
        report.update(status='all10_actual_responses_saved_pending_content_notes',CPU_wall_seconds=time.monotonic()-started,
            natural_stops=sum(r['stop_reason'] in ('eot','eos') for r in rows),
            empty=sum(r['empty_response'] for r in rows),unicode_failures=sum(not r['valid_utf8'] for r in rows),
            repetitions=sum(r['repetition'] for r in rows),full_histories=all(r['full_history_retained'] for r in rows))
    except BaseException as error:
        report.update(status='failed_partial_preserved',error=repr(error),CPU_wall_seconds=time.monotonic()-started)
        if isinstance(error,HTTPError):report['HTTP_error_body']=error.read().decode('utf-8',errors='replace')
        raise
    finally:
        write(target,report)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--arm',choices=('C0','C1'),required=True)
    main(parser.parse_args().arm)
