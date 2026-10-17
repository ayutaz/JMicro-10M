"""All3066 suite reviews with exact-history/raw-only reuse and unchanged rubric."""
import argparse
import json
from pathlib import Path
import chat_recovery_contract as current
from answer_learning_common import ROOT,read_json,ref,bound,save,now
import review_chat_natural as original
import chat_natural_contract as first_contract
import answer_curriculum_contract as second_contract

BASE_REUSE=original.reuse_index
POLICY=current.PARENT_RUN/'suite_review_reuse_policy.json'


def historical_index(config,run,reader,suites):
    saved={k:getattr(original,k) for k in ('CONFIG','RUN','SUITES','read_dev','require_ref')}
    try:
        original.CONFIG=config;original.RUN=run;original.SUITES=suites;original.read_dev=reader;original.require_ref=bound
        return BASE_REUSE()
    finally:
        for key,value in saved.items():setattr(original,key,value)


def combined_index():
    policy=read_json(POLICY);index={};ambiguous=set()
    pools=[]
    for p in policy['historical']:
        config=bound(p['config']);run=Path(p['run'])
        reader=first_contract.read_dev if p['kind']=='natural' else second_contract.read_dev
        pools.append(historical_index(config,run,reader,tuple(read_json(config)['suites'])))
    pools.append(BASE_REUSE())
    for pool in pools:
        for fp,value in pool.items():
            if fp in ambiguous:continue
            if fp in index and any(index[fp][k]!=value[k] for k in ('grammar','relevance','context')):
                ambiguous.add(fp);index.pop(fp);continue
            index.setdefault(fp,value)
    return index


def prepare_policy():
    assert not POLICY.exists()
    save(POLICY,dict(created_at=now(),config=ref(current.CONFIG),source=ref(__file__),
        historical=[dict(kind='natural',config=ref(ROOT/'configs/phase7/chat-natural-sft-20261017.json'),run=str(ROOT/'reports/phase7/chat-natural-sft-20261017')),
                    dict(kind='curriculum',config=ref(ROOT/'configs/phase7/answer-curriculum-resource-v2-20261017.json'),run=str(ROOT/'reports/phase7/chat-answer-learning-20261017/curriculum-main-resource-v2'))],
        policy='Validate historical raw under its own config and DEV reader; reuse only identical actual messages/checks/category/condition/IDs/bytes/text/stop/prompt/mechanics. Conflicting grades require fresh review. No model-quality score from keywords.',
        rubric_changed=False,TEST_reads=False))


def wire():
    original.CONFIG=current.CONFIG;original.RUN=current.RUN;original.SUITES=current.SUITES
    original.read_dev=current.read_dev;original.require_ref=bound;original.reuse_index=combined_index


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','packet','finish']);p.add_argument('arm',nargs='?',choices=['C0','C1']);p.add_argument('suite',nargs='?',choices=current.SUITES)
    p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=30);a=p.parse_args()
    if a.mode=='prepare':prepare_policy();return
    assert read_json(POLICY)['source']==ref(__file__)
    wire();path=current.RUN/'evaluation'/a.arm/a.suite/'result.json'
    if a.mode=='finish':
        assert read_json(path.with_name('packet.json'))['review_adapter']==ref(__file__)
        original.finish(path,path.with_name('authored_indices.tsv'));return
    existing=path.with_name('packet.json').exists();packet=original.packet(path)
    if not existing:
        packet.update(review_adapter=ref(__file__),reuse_policy=ref(POLICY));save(path.with_name('packet.json'),packet)
    assert packet['review_adapter']==ref(__file__)
    print(json.dumps(dict(total=219,manual_pending=packet['manual_pending'],reused=len(packet['reused']))))
    for i,(key,row) in enumerate(list(packet['pending'].items())[a.start:a.start+a.count],a.start):print(json.dumps(dict(index=i,key=key,**row),ensure_ascii=False))


if __name__=='__main__':main()
