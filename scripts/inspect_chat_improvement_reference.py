"""One bounded pass over accepted RPC TRAIN: target lengths and daily candidates."""
import json
from pathlib import Path
import re
import sys
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006')
RUN=ROOT/'reports/phase7/chat-improvement-20261012'
def main():
    assert sys.version_info[:3] == (3,12,7)
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    records=[json.loads(line) for line in (DATA/'train.jsonl').read_text().splitlines()]
    assert len(records)==2688 and all(r['split']=='train' for r in records)
    lengths=Counter();daily=Counter();count=0
    for record in records:
        messages=json.loads(record['messages_json'])
        for i,m in enumerate(messages):
            if m['role']!='assistant':continue
            n=len(tok.encode(m['text']))+1
            lengths[n]+=1;count+=1
            text=m['text']
            if (not re.search(r'私|僕|俺|うち|住ん|勤務|飼|妻|夫|子供|息子|娘|フィジー|戦争|医|薬|病|治療|<|[A-Za-z]{2,}',text)
                and re.search(r'ですね|ですか[？?]|ますか[？?]|大変|楽しみ|嬉しい|いいですね|素敵|よかった|お疲れ|こんにちは|こんばんは|よろしく|ありがとう',text)
                and len(text)<=65):daily[n]+=1
    bounds=((2,8),(9,16),(17,32),(33,65))
    bins=[sum(v for k,v in lengths.items() if lo<=k<=hi) for lo,hi in bounds]
    teachers=sum(k*v for k,v in lengths.items())
    result=dict(status='accepted_reference_quantities_reused_and_extended',created_at=now(),
        source_sha256=sha256(DATA/'train.jsonl'),targets=count,teachers=teachers,EOT_fraction=count/teachers,
        length_histogram=dict(sorted(lengths.items())),bins=bins,bin_fractions=[v/count for v in bins],
        bounded_daily_candidate_count=sum(daily.values()),daily_candidate_histogram=dict(sorted(daily.items())),
        daily_filter='conservative lexical screening only; requires source-context content review; not semantic certification',
        whole_web_corpus_scan=False,new_training_tokens=0,protected_test_used=False)
    assert count==40366 and teachers==633185
    atomic_json(RUN/'reference_targets.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
