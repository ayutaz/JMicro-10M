"""Compact read-only display: every actual message retained; no scoring logic."""
import argparse
import json
from chat_recovery_contract import RUN
from answer_learning_common import read_json,ref

p=argparse.ArgumentParser();p.add_argument('kind',choices=['suite','public']);p.add_argument('arm',choices=['C0','C1']);p.add_argument('--suite',default='new');p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=30);a=p.parse_args()
path=RUN/'evaluation'/a.arm/a.suite/'packet.json' if a.kind=='suite' else RUN/'public100'/a.arm/'packet.json'
packet=read_json(path)
raw=path.with_name('result.json' if a.kind=='suite' else 'raw.json')
assert (packet['evaluation_sha256']==ref(raw)['sha256']) if a.kind=='suite' else packet['raw']==ref(raw)
print(json.dumps(dict(total_pending=len(packet['pending']),total_reused=len(packet['reused']))))
for ordinal,(key,row) in enumerate(list(packet['pending'].items())[a.start:a.start+a.count],a.start):
    value=dict(i=ordinal,key=key,H=[(m['role'],m['content']) for m in row['messages']])
    if a.kind=='suite':value.update(A=row['response'],stop=row['stop'])
    else:value.update(raw_index=int(key),expected=row['expected'],objective=row['objective'],A=row['response']['text'],stop=row['response']['stop_reason'])
    print(json.dumps(value,ensure_ascii=False,separators=(',',':')))
