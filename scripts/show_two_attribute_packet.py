"""Display every actual message without adding any scoring rules."""
import argparse
import json
from two_attribute_contract import RUN
from answer_learning_common import read_json,ref

p=argparse.ArgumentParser();p.add_argument('suite');p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40);a=p.parse_args()
path=RUN/'public100/D/packet.json' if a.suite=='public100' else RUN/'evaluation/D'/a.suite/'packet.json'
packet=read_json(path);raw=path.with_name('raw.json' if a.suite=='public100' else 'result.json')
assert packet['raw']==ref(raw) if a.suite=='public100' else packet['evaluation_sha256']==ref(raw)['sha256']
print(json.dumps(dict(pending=len(packet['pending']),reused=len(packet['reused']))))
for ordinal,(key,row) in enumerate(list(packet['pending'].items())[a.start:a.start+a.count],a.start):
    value=dict(i=ordinal,key=key,H=[(m['role'],m.get('content',m.get('text'))) for m in row['messages']])
    if a.suite=='public100':value.update(raw_index=int(key),expected=row['expected'],objective=row['objective'],A=row['response']['text'],stop=row['response']['stop_reason'])
    else:value.update(A=row['response'],stop=row['stop'])
    print(json.dumps(value,ensure_ascii=False,separators=(',',':')))
