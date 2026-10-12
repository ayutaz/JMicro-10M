"""Bounded, versioned C1 TRAIN construction; never reads new/old DEV questions."""
from collections import Counter,defaultdict
import hashlib
import json
from pathlib import Path
import random
import re
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.chat_curriculum import WEIGHTS,render,semantic_check
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json

RPC=Path('/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006')
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-improvement-20261012')
RUN=ROOT/'reports/phase7/chat-improvement-20261012'
BOUNDS=((2,8),(9,16),(17,32),(33,65))
TARGET=660000

def dump_jsonl(path,records):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='\n') as f:
        for r in records:f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')

def content_binding(r):
    return hashlib.sha256(json.dumps(r['messages'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def main():
    assert sys.version_info[:3]==(3,12,7)
    assert not (DATA/'manifest.json').exists(),'Frozen data already exists; inspect instead of overwriting'
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    rpc=[json.loads(l) for l in (RPC/'train.jsonl').read_text().splitlines()]
    rpc_sha=sha256(RPC/'train.jsonl');rpc_by_id={r['doc_id']:r for r in rpc}
    assert len(rpc)==2688 and all(r['split']=='train' for r in rpc)
    sources={p:sha256(ROOT/p) for p in ('src/jmicro/chat_curriculum.py','scripts/prepare_chat_improvement_train.py')}
    # Timestamped design freeze PRECEDES every generated TRAIN target and DEV.
    atomic_json(RUN/'train_design_freeze.json',dict(created_at=now(),sources=sources,
        new_DEV_questions_read=False,old_DEV_copied=False,teacher_mixture=WEIGHTS,
        minimum_teachers_per_pass=650000,target_teachers=TARGET,max_family_teacher_fraction=.05,
        mixture_tolerance_percentage_points=1.0,screening='lexical screen plus fixed 40/category review',
        variants='near and exact-derived variants remain same scenario family; not independent information',
        selected_target='final Assistant only; prior gold Assistant bodies are input, never labels'))
    pools=defaultdict(list);seen=set();reject=Counter()
    def add(r):
        body=r['messages'][-1]['text'];ids=tok.encode(body);n=len(ids)+1
        if not 2<=n<=65:reject['length']+=1;return
        if tok.decode(ids)!=body:reject['roundtrip']+=1;return
        digest=content_binding(r)
        if digest in seen:reject['duplicate_dialogue']+=1;return
        seen.add(digest);r['content_sha256']=digest;r['teacher_tokens']=n
        r['length_bin']=next(i for i,(lo,hi) in enumerate(BOUNDS) if lo<=n<=hi)
        pools[r['category']].append(r)
    # Preserve CC BY-SA provenance; remove preceding human-Assistant persona
    # histories rather than feeding them as gold model context. Selected pairs
    # must stand alone. No new personal facts are added to either speaker.
    for record in rpc:
        messages=json.loads(record['messages_json'])
        for index,m in enumerate(messages):
            if m['role']!='assistant':continue
            body=m['text']
            user=messages[index-1]['text']
            # Natural response screening is intentionally narrow after the
            # reviewed role failures. Entire retained dialogues still need
            # content review; greetings are not broad semantic certification.
            safe_greeting=r'(?:こんにちは|こんばんは|おはようございます|よろしくお願いします|こちらこそ|ありがとうございます|ありがとう|どういたしまして|お疲れさまでした|[。！!、\sー〜])+[。！!]*'
            if index!=1 or not re.fullmatch(safe_greeting,body):continue
            if index!=1 and (not re.search(r'私は|僕は|自分は|今日は|今日の|最近|昨日|今朝',user)
                    or re.search(r'それ|そう|一緒|同じ|さっき|あなた|そちら|ですか|ますか|[？?]',user)):
                continue
            if (re.search(r'私|僕|俺|うち|住ん|勤務|飼|妻|夫|子供|息子|娘|フィジー|戦争|医|薬|病|治療|<|[A-Za-z]{2,}',body)
                or re.search(r'今度|試して|一緒|同じ|入院|退院|実家|毎日|起き|食べま|飲みま|作って|見てま|見てい|楽しみにして|仕事|出かけま',body)
                or not re.search(r'ですね|ですか[？?]|ますか[？?]|大変|楽しみ|嬉しい|いいですね|素敵|よかった|お疲れ|こんにちは|こんばんは|よろしく|ありがとう',body)
                or len(body)>65):continue
            r=dict(doc_id=f"c1-rpc-{record['doc_id']}-{index}",split='train',messages=messages[index-1:index+1],
                target_message_indices=[1],category='daily',family=f"rpc-source-{record['doc_id']}",
                source='RealPersonaChat-selected-unedited',source_doc_id=record['doc_id'],
                source_target_message_index=index,source_sha256=rpc_sha,
                source_revision=record.get('revision'),license=record['license'],bucket=record['bucket'],
                editing_reason='retain current source User/Assistant pair; remove prior human-Assistant persona; lexical screening is not semantic certification')
            add(r)
    natural_pool_teachers=sum(r['teacher_tokens'] for r in pools['daily'])
    for category in WEIGHTS:
        for index in range(24):
            for variant in range(1024):
                r=render(category,index,variant)
                assert semantic_check(r)
                add(r)
    # Family-balanced teacher selection. Length differences are measured, never
    # repaired by cutting an answer. Actual consumption is checked by dry-run.
    rng=random.Random(13142);selected=[];category_counts={};families=defaultdict(Counter)
    for category,weight in WEIGHTS.items():
        records=list(pools[category])
        # Fixed pre-DEV length preference, measured against C0 below. Long
        # answers include requested grounded explanation; no answer truncation.
        preference=(.30,1.,3.,1.)
        records.sort(key=lambda r:rng.expovariate(preference[r['length_bin']]))
        quota=round(TARGET*weight);count=0
        # Each authored family stays <5%, including all wording/slot variants.
        cap=int(quota*.047)
        for record in records:
            n=record['teacher_tokens'];family=record['family']
            if families[category][family]+n>cap:continue
            if count>=quota:break
            selected.append(record);families[category][family]+=n;count+=n
        category_counts[category]=count
        if count<quota:reject[f'insufficient_{category}']+=quota-count
    rng.shuffle(selected)
    # Complete schema/role/grounding checks on every chosen target.
    for record in selected:
        assert record['split']=='train' and record['target_message_indices']==[len(record['messages'])-1]
        assert [m['role'] for m in record['messages']]==['user' if i%2==0 else 'assistant' for i in range(len(record['messages']))]
        assert all(m['text'] and '\ufffd' not in m['text'] and not any(0xD800<=ord(c)<=0xDFFF for c in m['text']) for m in record['messages'])
        if record['source']=='project-authored-plan131-train':assert semantic_check(record)
        else:
            original=rpc_by_id[record['source_doc_id']]
            i=record['source_target_message_index']
            assert record['messages']==json.loads(original['messages_json'])[i-1:i+1]
    teachers=sum(category_counts.values());hist=Counter(r['length_bin'] for r in selected)
    reference=json.loads((RUN/'reference_targets.json').read_text())
    eot=len(selected)/teachers
    fractions=[hist[i]/len(selected) for i in range(4)]
    tv=sum(abs(a-b) for a,b in zip(fractions,reference['bin_fractions']))/2
    eotdiff=abs(eot-reference['EOT_fraction'])
    coverage={k:dict(families=len(families[k]),max_fraction=max(families[k].values())/category_counts[k]) for k in WEIGHTS}
    gates=dict(enough_teachers=teachers>=650000,all_category_quotas=all(category_counts[c]>=round(TARGET*w) for c,w in WEIGHTS.items()),
        family_cap=all(x['max_fraction']<=.05 for x in coverage.values()),EOT_match=eotdiff<=.01,length_TV_match=tv<=.10)
    # Freeze only after manual content review and dry-run; this is a candidate.
    dump_jsonl(DATA/'candidate.train.jsonl',selected)
    packet=[]
    for category in WEIGHTS:
        subset=[r for r in selected if r['category']==category]
        packet.extend(random.Random(1314800+list(WEIGHTS).index(category)).sample(subset,40))
    dump_jsonl(DATA/'train_review_packet.jsonl',packet)
    report=dict(created_at=now(),status='candidate_needs_280_content_reviews_and_consumption_dry_run',
        sources=sources,train_path=str(DATA/'candidate.train.jsonl'),train_sha256=sha256(DATA/'candidate.train.jsonl'),
        selected_targets=len(selected),teachers_per_pass=teachers,category_teachers=category_counts,
        teacher_fractions={k:v/teachers for k,v in category_counts.items()},family_coverage=coverage,
        EOT_fraction=eot,EOT_absolute_difference=eotdiff,length_bins=[hist[i] for i in range(4)],
        length_bin_fractions=fractions,length_TV=tv,gates=gates,rejections=dict(reject),
        natural_pool_teachers=natural_pool_teachers,natural_selected_targets=sum(r['source']!='project-authored-plan131-train' for r in selected),
        review_packet_sha256=sha256(DATA/'train_review_packet.jsonl'),new_DEV_created=False,new_learning_tokens=0,
        full_corpus_scan=False,all_natural_targets_semantically_certified=False)
    atomic_json(RUN/'train_candidate.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
