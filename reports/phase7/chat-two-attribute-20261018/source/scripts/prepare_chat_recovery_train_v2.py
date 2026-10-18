"""Repair an unfrozen TRAIN renderer typo; preserve the rejected v1 preparation."""
import argparse
import hashlib
import copy
import prepare_chat_recovery_train as original
from answer_learning_common import ROOT,save,ref,bound,read_json,now

BASE=ROOT/'reports/phase7/chat-recovery-20261018'
original.RUN=BASE/'input-v2-preparation'
original.DATA=original.DATA/'input-v2'
unrepaired=original.rewrite


def rewrite(old,index):
    row=unrepaired(old,index)
    if row['family']=='correction':
        texts=[m['text'] for m in row['messages']]
        assert sum('公園ですです。' in t for t in texts)==1
        row['messages'][0]['text']=row['messages'][0]['text'].replace('公園ですです。','公園です。')
        assert original.oracle(row['family'],row['messages'])==old['messages'][-1]['text']
        row['normalized_pair_sha256']=hashlib.sha256('\n'.join(m['text'] for m in row['messages']).encode()).hexdigest()
    return row


original.rewrite=rewrite


def prepare():
    prior=read_json(BASE/'TRAIN_proposal_receipt.json')
    assert prior['source']==ref(ROOT/'scripts/prepare_chat_recovery_train.py')
    assert not (original.DATA.parent/'manifest.json').exists()
    original.prepare()
    path=original.RUN/'TRAIN_proposal_receipt.json';current=read_json(path)
    current.update(wrapper=ref(__file__),previous_unfrozen_proposal=ref(BASE/'TRAIN_proposal_receipt.json'))
    save(path,current)
    old_rows=[original.json.loads(l) for l in bound(prior['records']).read_text().splitlines()]
    new_rows=[original.json.loads(l) for l in bound(current['records']).read_text().splitlines()]
    changed=0
    for old,new in zip(old_rows,new_rows,strict=True):
        expected=copy.deepcopy(old)
        if old['family']=='correction':
            expected['messages'][0]['text']=expected['messages'][0]['text'].replace('公園ですです。','公園です。')
            expected['normalized_pair_sha256']=hashlib.sha256('\n'.join(m['text'] for m in expected['messages']).encode()).hexdigest()
            changed+=1
        assert new==expected
        assert all('ですです' not in m['text'] for m in new['messages'])
    assert changed==256
    save(BASE/'input_v2_render_repair.json',dict(created_at=now(),old_proposal=ref(BASE/'TRAIN_proposal_receipt.json'),
        new_proposal=ref(path),wrapper=ref(__file__),changed_rows=256,all_other_rows_unchanged=True,
        change='Remove duplicated copula in park-place rendering only; old source, data and QA packet retained',
        teacher_answers_IDs_source_quota_numeric_recipe_unchanged=True,old_QA_not_accepted=True,
        new_training_updates=0,new_GPU=0,new_DEV_not_authored=True))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','packet','package','replay']);p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=16);a=p.parse_args()
    if a.mode=='prepare':prepare()
    else:
        assert read_json(original.RUN/'TRAIN_proposal_receipt.json')['wrapper']==ref(__file__)
        if a.mode=='packet':original.packet(a.start,a.count)
        elif a.mode=='package':original.package()
        else:original.replay()
