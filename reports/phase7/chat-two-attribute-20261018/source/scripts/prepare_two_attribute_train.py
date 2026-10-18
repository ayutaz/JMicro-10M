"""Author only TRAIN64, independently check labels and replay full teacher budget."""
import argparse
import hashlib
import json
import time
from pathlib import Path
from answer_learning_common import ROOT,save,ref,bound,read_json,now
from jmicro.tokenizer import Tokenizer
from jmicro.teacher_chat_training import TeacherBudgetSampler,teacher_lr

RUN=ROOT/'reports/phase7/chat-two-attribute-20261018'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-two-attribute-20261018')
PLAN=ROOT/'docs/164_chat_two_attribute_diagnosis_execution.md'
OLD=ROOT/'configs/phase7/chat-input-structure-20261018.json'
BUDGET=250000
# Two field labels, initial values, and the replacement for exactly one field.
FACTS=[
    ('自己紹介',('名前','好きな花'),('ミナ','すみれ'),0,'ユイ'),
    ('荷物',('品物','色'),('手帳','紫'),1,'橙'),
    ('旅程',('行き先','出発時刻'),('長野','九時'),0,'金沢'),
    ('当番',('担当者','持ち物'),('ナオ','笛'),1,'縄'),
    ('注文',('飲み物','温度'),('ほうじ茶','常温'),0,'豆乳'),
    ('飼育',('動物','頭数'),('羊','二頭'),1,'四頭'),
    ('相談会',('集合場所','集合時刻'),('南口','八時'),0,'北門'),
    ('読書',('本の題名','著者'),('星の庭','アヤ'),1,'リオ'),
]
NEUTRALS=['今日は棚を拭きました。先ほどの情報は変えません。',
          '外では風が吹いています。最初の情報には変更はありません。',
          'さきほど紙をそろえました。伝えた内容はそのままです。']

def messages_for(family,correction,two,distant):
    topic,labels,values,changed,replacement=FACTS[family]
    facts=''.join(f'{k}は{v}です。' for k,v in zip(labels,values))
    messages=[dict(role='user',text=f'{topic}の情報を覚えてください。'+facts),dict(role='assistant',text='わかりました。')]
    if correction:
        messages.extend([dict(role='user',text=f'{labels[changed]}だけ訂正します。{labels[changed]}は{replacement}です。もう一方は変えません。'),dict(role='assistant',text='訂正を確認しました。')])
    if distant:
        for text in NEUTRALS:messages.extend([dict(role='user',text=text),dict(role='assistant',text='承知しました。')])
    requested=list(labels) if two else [labels[family%2]]
    messages.append(dict(role='user',text='今の'+ 'と'.join(requested)+'を短く教えてください。'))
    latest=dict(zip(labels,values))
    if correction:latest[labels[changed]]=replacement
    answer=''.join(f'{k}は{latest[k]}です。' for k in requested)
    messages.append(dict(role='assistant',text=answer))
    return messages,requested,latest

def oracle(messages,labels):
    # Parse the literal User assertions, rather than trusting generation metadata.
    import re
    latest={}
    for message in messages[:-1]:
        if message['role']!='user':continue
        for label in labels:
            found=re.findall(re.escape(label)+r'は([^。]+)です。',message['text'])
            if found:latest[label]=found[-1]
    question=messages[-2]['text'];requested=[label for label in labels if label in question]
    assert requested and set(latest)==set(labels)
    return ''.join(f'{label}は{latest[label]}です。' for label in requested)

def prepare():
    assert not DATA.exists() and not (RUN/'TRAIN_proposal.json').exists()
    DATA.mkdir(parents=True);c=read_json(OLD);tok=Tokenizer(bound(c['tokenizer']));rows=[]
    for f in range(8):
        for correction in (False,True):
            for two in (False,True):
                for distant in (False,True):
                    messages,requested,latest=messages_for(f,correction,two,distant)
                    assert oracle(messages,FACTS[f][1])==messages[-1]['text']
                    target=tok.encode(messages[-1]['text'])+[7]
                    assert 2<=len(target)<=32,(f,len(target),messages[-1])
                    assert tok.decode(target)==messages[-1]['text']
                    windows=list(tok.sft_windows(messages,1025));w=windows[-1]
                    assert all(w['removed_turns']==0 for w in windows)
                    assert [v for v in w['labels'] if v!=-100]==target
                    row=dict(doc_id=f'two-attribute-train:{len(rows):02d}',family_id=f'train-f{f}',source='Authored_two_attribute_TRAIN',split='train',
                        family=f,correction=correction,two=two,distant=distant,messages=messages,target_message_indices=[len(messages)-1],
                        requested=requested,latest=latest,expected=messages[-1]['text'],teacher_ids=target,prompt_ids=tok.chat_prompt(messages[:-1],992)[0])
                    rows.append(row)
    path=DATA/'TRAIN.jsonl';path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
    save(RUN/'TRAIN_proposal.json',dict(created_at=now(),source=ref(__file__),plan=ref(PLAN),records=ref(path),rows=64,independent_fact_families=8,
        all64_oracles_and_complete_masks=True,all_teacher_lengths_le32=True,no_history_trim=True,DEV_authored=False,TEST_created=False,new_GPU=0))
    for i,r in enumerate(rows):print(json.dumps(dict(i=i,flags=[r[k] for k in ('family','correction','two','distant')],messages=r['messages'],teachers=len(r['teacher_ids'])),ensure_ascii=False))

def freeze():
    proposal=read_json(RUN/'TRAIN_proposal.json');assert proposal['source']==ref(__file__)
    qa=read_json(RUN/'TRAIN_review.json');assert qa['proposal']==ref(RUN/'TRAIN_proposal.json')
    rows=[json.loads(l) for l in bound(proposal['records']).read_text().splitlines()]
    assert qa['all64_directly_read'] and len(qa['judgments'])==64 and all(r['accepted'] for r in qa['judgments'])
    assert [r['id'] for r in qa['judgments']]==[r['doc_id'] for r in rows] and not (DATA/'manifest.json').exists()
    tok=Tokenizer(bound(read_json(OLD)['tokenizer']));s=TeacherBudgetSampler(rows,tok,1024,42,BUDGET,512,32)
    history=[];token_digest='00'*32;teacher_digest=hashlib.sha256();started=time.monotonic()
    while s.teacher_tokens<BUDGET:
        before=s.teacher_tokens;batches,n,body_bytes=s.next_update();digest=hashlib.sha256(bytes.fromhex(token_digest))
        for x,y in batches:
            digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
            teacher_digest.update(y[y!=-100].numpy().astype('<i8').tobytes())
        token_digest=digest.hexdigest()
        history.append(dict(update=len(history)+1,teachers=s.teacher_tokens,teachers_this_update=n,microbatches=len(batches),
            lr=teacher_lr(before,n,BUDGET,1e-4),token_digest=token_digest,body_bytes=body_bytes,**s.state_dict()))
    assert BUDGET<=s.teacher_tokens<=BUDGET+31 and s.removed_turns==0
    replay=RUN/'TRAIN_CPU_replay.json';save(replay,dict(records=proposal['records'],sampler_binding=s.binding,updates=len(history),actual_teachers=s.teacher_tokens,
        physical_microbatches=sum(h['microbatches'] for h in history),sampler_terminal=s.state_dict(),history=history,
        teacher_stream_sha256=teacher_digest.hexdigest(),CPU_seconds=time.monotonic()-started,no_history_trim=True))
    save(DATA/'manifest.json',dict(status='TRAIN_frozen_before_DEV',created_at=now(),records=proposal['records'],proposal=ref(RUN/'TRAIN_proposal.json'),
        review=ref(RUN/'TRAIN_review.json'),replay=ref(replay),rows=64,independent_fact_families=8,budget=BUDGET,DEV_authored=False,TEST_created=False))
    save(RUN/'TRAIN_manifest_ref.json',ref(DATA/'manifest.json'))
    print('TRAIN64 frozen, all CPU consumption replayed',len(history),s.teacher_tokens)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','freeze']);a=p.parse_args()
    prepare() if a.mode=='prepare' else freeze()
