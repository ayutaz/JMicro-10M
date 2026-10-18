"""Author separate DEV only after the TRAIN64 manifest has been frozen."""
import copy
import json
from prepare_two_attribute_train import RUN,DATA,OLD,FACTS,messages_for,oracle
import prepare_two_attribute_train as train
from answer_learning_common import save,ref,bound,read_json,now
from jmicro.tokenizer import Tokenizer

VALUES=[(('サキ','つばき'),'エマ'),(('帽子','緑'),'白'),(('松本','十時'),'高山'),(('レナ','鈴'),'紐'),
        (('煎茶','熱め'),'甘酒'),(('山羊','三頭'),'五頭'),(('西門','六時'),'裏口'),(('雪の丘','セナ'),'ルカ')]

def main():
    manifest=DATA/'manifest.json';m=read_json(manifest);assert m['status']=='TRAIN_frozen_before_DEV'
    assert not (DATA/'DEV.json').exists();tok=Tokenizer(bound(read_json(OLD)['tokenizer']));groups={}
    original=copy.deepcopy(FACTS)
    for group in ('unseen_values','unseen_structure'):
        rows=[]
        for f in range(8):
            for correction in (False,True):
                for two in (False,True):
                    if group=='unseen_values':
                        topic,labels,_,changed,_=original[f];values,replacement=VALUES[f]
                        train.FACTS[f]=(topic,labels,values,changed,replacement)
                    else:train.FACTS[f]=original[f]
                    messages,requested,latest=messages_for(f,correction,two,bool((f+int(correction))%2))
                    if group=='unseen_structure':
                        topic,labels,values,changed,replacement=original[f]
                        messages[0]['text']=f'{topic}について伝えます。'+''.join(f'{k}は{v}です。' for k,v in reversed(list(zip(labels,values))))
                        for message in messages:
                            if message['role']=='assistant' and message is not messages[-1]:message['text']='はい、伺いました。'
                        q='、'.join(reversed(requested))
                        messages[-2]['text']=f'これまでの訂正も踏まえ、{q}について現在の内容を答えてください。'
                        messages[-2:-2]=[dict(role='user',text='ノートを閉じました。情報の変更はありません。'),dict(role='assistant',text='はい、伺いました。')]
                    assert oracle(messages,train.FACTS[f][1])==messages[-1]['text']
                    assert tok.chat_prompt(messages[:-1],992)[1]==0 and len(tok.encode(messages[-1]['text']))+1<=32
                    rows.append(dict(id=f'{group}:{len(rows):02d}',family_id=f'dev-f{f}',split='dev',family=f,correction=correction,two=two,
                        messages=messages[:-1],expected=messages[-1]['text'],requested=requested,latest=latest))
        assert len(rows)==32;groups[group]=rows
    train.FACTS[:]=original;own=[]
    for f in range(8):
        topic,labels,_,changed,_=original[f];values,replacement=VALUES[f]
        for correction in (False,True):
            latest=dict(zip(labels,values));first=f'{topic}を覚えてください。'+''.join(f'{k}は{v}です。' for k,v in latest.items())
            requested=[labels[f%2]]
            if correction:
                latest[labels[changed]]=replacement
                second=f'{labels[changed]}だけ訂正します。{labels[changed]}は{replacement}です。もう一方は変えません。'
            else:second='先ほど伝えた情報に変更はありません。'
            second+='今の'+requested[0]+'を短く教えてください。'
            third='今の'+'と'.join(labels)+'を短く教えてください。'
            own.append(dict(id=f'own:{len(own):02d}',family=f,correction=correction,split='dev',turns=[
                dict(user=first,requested=[],latest=dict(zip(labels,values)),expected='情報を受け取ったことを自然に返す。創作しない。'),
                dict(user=second,requested=requested,latest=dict(latest),expected=''.join(f'{k}は{latest[k]}です。' for k in requested)),
                dict(user=third,requested=list(labels),latest=dict(latest),expected=''.join(f'{k}は{latest[k]}です。' for k in labels))]))
    all_train=[json.loads(l) for l in bound(m['records']).read_text().splitlines()]
    assert not {tuple(tok.chat_prompt(r['messages'],992)[0]) for rows in groups.values() for r in rows}&{tuple(r['prompt_ids']) for r in all_train}
    save(DATA/'DEV.json',dict(created_at=now(),TRAIN_manifest=ref(manifest),TRAIN_frozen_before_DEV=True,groups=groups,own=own,
        dev_not_sealed_TEST=True,independent_fact_families_per_group=8,unseen_values_not_new_fields=True,
        structure_changes_bundled=True,own_uses_unseen_values=True))
    save(RUN/'DEV_preparation.json',dict(created_at=now(),source=ref(__file__),TRAIN_manifest=ref(manifest),DEV=ref(DATA/'DEV.json'),
        responses=240,new_TEST_created=False))
    print(json.dumps(dict(groups={k:len(v) for k,v in groups.items()},own=len(own),TRAIN_before_DEV=m['created_at']),ensure_ascii=False))

if __name__=='__main__':main()
