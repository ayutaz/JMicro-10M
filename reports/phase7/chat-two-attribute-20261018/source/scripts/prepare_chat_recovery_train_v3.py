"""Clarify deferred literal requests before TRAIN freeze; retain v1/v2."""
import argparse
import copy
import hashlib
import prepare_chat_recovery_train_v2 as v2
from answer_learning_common import ROOT,save,ref,bound,read_json,now

original=v2.original
BASE=ROOT/'reports/phase7/chat-recovery-20261018'
original.RUN=BASE/'input-v3-preparation'
original.DATA=original.DATA.parent/'input-v3'


def rewrite(old,index):
    row=v2.rewrite(old,index)
    if row['family']=='literal':
        text=row['messages'][0]['text'];assert text.startswith('次の返事に指定する語は')
        row['messages'][0]['text']=text.replace('次の返事に','後で一語の返事を頼みます。',1)
        row['normalized_pair_sha256']=hashlib.sha256('\n'.join(m['text'] for m in row['messages']).encode()).hexdigest()
        assert original.oracle('literal',row['messages'])==old['messages'][-1]['text']
    return row


original.rewrite=rewrite


def prepare():
    prior_path=BASE/'input-v2-preparation/TRAIN_proposal_receipt.json';prior=read_json(prior_path)
    assert prior['source']==ref(ROOT/'scripts/prepare_chat_recovery_train.py') and prior['wrapper']==ref(ROOT/'scripts/prepare_chat_recovery_train_v2.py')
    assert not (original.DATA.parent/'input-v2/manifest.json').exists()
    original.prepare();path=original.RUN/'TRAIN_proposal_receipt.json';current=read_json(path)
    current.update(wrapper=ref(__file__),prior_wrapper=ref(ROOT/'scripts/prepare_chat_recovery_train_v2.py'),previous_unfrozen_proposal=ref(prior_path));save(path,current)
    old_rows=[original.json.loads(l) for l in bound(prior['records']).read_text().splitlines()]
    new_rows=[original.json.loads(l) for l in bound(current['records']).read_text().splitlines()];changed=0
    for old,new in zip(old_rows,new_rows,strict=True):
        expected=copy.deepcopy(old)
        if old['family']=='literal':
            expected['messages'][0]['text']=expected['messages'][0]['text'].replace('次の返事に','後で一語の返事を頼みます。',1)
            expected['normalized_pair_sha256']=hashlib.sha256('\n'.join(m['text'] for m in expected['messages']).encode()).hexdigest();changed+=1
        assert expected==new
    assert changed==256
    save(BASE/'input_v3_request_clarification.json',dict(created_at=now(),old_proposal=ref(prior_path),new_proposal=ref(path),wrapper=ref(__file__),changed_rows=256,
        change='Literal first User explicitly defers one-word request; intervening acknowledgement no longer ambiguous as a failed immediate request',
        old_QA_not_accepted=True,all_other_rows_unchanged=True,answers_IDs_source_quota_numeric_recipe_unchanged=True,
        new_training_updates=0,new_GPU=0,new_DEV_not_authored=True))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','packet','package','replay']);p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=16);a=p.parse_args()
    if a.mode=='prepare':prepare()
    else:
        record=read_json(original.RUN/'TRAIN_proposal_receipt.json')
        assert record['wrapper']==ref(__file__) and record['prior_wrapper']==ref(ROOT/'scripts/prepare_chat_recovery_train_v2.py')
        if a.mode=='packet':original.packet(a.start,a.count)
        elif a.mode=='package':original.package()
        else:original.replay()
