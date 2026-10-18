"""Unchanged literal rubric; exact raw/history reuse from validated old studies."""
import argparse
import json
from pathlib import Path
from two_attribute_contract import CONFIG,RUN,preflight
from answer_learning_common import ROOT,read_json,ref,bound,save,now
from chat_recovery_contract import read_dev
import review_chat_natural as suite_review
import review_chat_recovery_public100 as public_review
from jmicro.tokenizer import Tokenizer

OLD_CONFIG=ROOT/'configs/phase7/chat-input-structure-20261018.json'
OLD_RUN=ROOT/'reports/phase7/chat-recovery-20261018/input-structure-main'
NATIVE_PUBLIC_INDEX=public_review.old_index

def wire(config=CONFIG,run=RUN):
    suite_review.CONFIG=config;suite_review.RUN=run;suite_review.SUITES=tuple(read_json(config)['suites']);suite_review.read_dev=read_dev;suite_review.require_ref=bound

def reuse_index():
    index={};ambiguous=set()
    for config,run in ((OLD_CONFIG,OLD_RUN),(CONFIG,RUN)):
        wire(config,run)
        for path in sorted((run/'evaluation').glob('*/*/notes.json')):
            raw,view,items=suite_review.get_items(path.with_name('result.json'));notes=read_json(path)
            suite_review.content_review(view,ref(path.with_name('result.json'))['sha256'],notes,items)
            for note in notes['judgments']:
                fp=suite_review.fingerprint(items[note['key']]);rating={k:note[k] for k in ('grammar','relevance','context','rationale')}
                if fp in ambiguous:continue
                if fp in index and any(index[fp][k]!=rating[k] for k in ('grammar','relevance','context')):
                    ambiguous.add(fp);index.pop(fp);continue
                index.setdefault(fp,dict(rating,source_notes=dict(ref(path),key=note['key']),fingerprint=fp))
    wire();return index

def public_validate(arm):
    c,tok,_=preflight();path=RUN/'public100'/arm/'raw.json';raw=read_json(path)
    assert arm=='D' and raw['status']=='complete_pending_literal_review' and raw['config_sha256']==c['config_sha256']
    assert raw['checkpoint']==read_json(RUN/'learning_complete.json')['checkpoint'];bound(raw['checkpoint'])
    assert raw['cases']==c['public100'] and raw['device']=='cuda' and raw['precision']=='BF16/math'
    offset=0
    for case in read_json(bound(c['public100']))['cases']:
        history=[dict(m) for m in case['history']]
        for turn,target in enumerate(case['turns'],1):
            r=raw['responses'][offset];history.append(dict(role='user',content=target['user']))
            assert all(r[k]==case[k] for k in ('id','category','mode'))
            assert r['turn']==turn and r['final']==(turn==len(case['turns'])) and r['expected']==target['expected'] and r['objective']==target['objective'] and r['messages']==history
            suite_review.validate_reply(r['response'],tok,history,True);history.append(dict(role='assistant',content=r['response']['text']));offset+=1
    assert offset==len(raw['responses'])==200;return path,raw,tok

def public_index(tok):
    index=NATIVE_PUBLIC_INDEX(tok);ambiguous=set()
    for arm in ('C0','C1'):
        path=OLD_RUN/'public100'/arm/'raw.json';raw=read_json(path);notes=read_json(path.with_name('notes.json'))
        assert notes['raw']==ref(path) and len(notes['judgments'])==len(raw['responses'])==200
        for i,(r,n) in enumerate(zip(raw['responses'],notes['judgments'],strict=True)):
            suite_review.validate_reply(r['response'],tok,r['messages'],True);fp=public_review.fingerprint(r);assert n['raw_fingerprint']==fp
            if fp in ambiguous:continue
            if fp in index and any(index[fp][k]!=n[k] for k in ('grammar','relevance','context','factual_correct')):
                ambiguous.add(fp);index.pop(fp);continue
            index.setdefault(fp,dict({k:n[k] for k in ('grammar','relevance','context','factual_correct','rationale')},source_notes=dict(ref(path.with_name('notes.json')),index=i),fingerprint=fp))
    return index

def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['packet','finish']);p.add_argument('suite');p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40);a=p.parse_args()
    preflight()
    if a.suite=='public100':
        public_review.CONFIG=CONFIG;public_review.RUN=RUN;public_review.validate=public_validate;public_review.old_index=public_index
        if a.mode=='packet':public_review.packet('D',a.start,a.count)
        else:public_review.finish('D')
    else:
        wire();suite_review.reuse_index=reuse_index;path=RUN/'evaluation/D'/a.suite/'result.json'
        if a.mode=='finish':suite_review.finish(path,path.with_name('authored_indices.tsv'))
        else:
            packet=suite_review.packet(path);print(json.dumps(dict(total=219,pending=packet['manual_pending'],reused=len(packet['reused']))))
            for i,(key,row) in enumerate(list(packet['pending'].items())[a.start:a.start+a.count],a.start):
                print(json.dumps(dict(i=i,key=key,**row),ensure_ascii=False))

if __name__=='__main__':main()
