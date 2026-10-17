"""All2628 exact32-token raw reviews using unchanged literal content rubric."""
import argparse
from pathlib import Path
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
from answer_learning_common import ROOT,RUN as PARENT_RUN,ref,bound,read_json
import review_chat_natural as original
import chat_natural_contract as historical_contract

BASE_REUSE_INDEX=original.reuse_index
POLICY=PARENT_RUN/'exact_review_reuse_policy.json'


def historical_index():
    policy=read_json(POLICY);old_config=bound(policy['historical_config'])
    assert old_config==ROOT/'configs/phase7/chat-natural-sft-20261017.json'
    assert not policy['rubric_or_gates_changed'] and not policy['new_TEST_read']
    names=('CONFIG','RUN','SUITES','read_dev','require_ref')
    saved={name:getattr(original,name) for name in names}
    try:
        original.CONFIG=old_config
        original.RUN=Path(policy['historical_evaluation_root']).parent
        original.SUITES=historical_contract.SUITES
        original.read_dev=historical_contract.read_dev
        original.require_ref=bound
        # The unchanged function independently validates all old raw and notes
        # under their own frozen config before any current judgment is reused.
        index=BASE_REUSE_INDEX()
        assert len(list((original.RUN/'evaluation').glob('*/*/notes.json')))==10
        return index
    finally:
        for name,value in saved.items():setattr(original,name,value)


def combined_index():
    index=historical_index()
    for fingerprint,value in BASE_REUSE_INDEX().items():
        if fingerprint in index:
            assert all(index[fingerprint][k]==value[k] for k in ('grammar','relevance','context'))
        index[fingerprint]=value
    return index


def wire():
    original.CONFIG=CONFIG;original.RUN=RUN;original.SUITES=contract.SUITES
    original.read_dev=contract.read_dev;original.require_ref=bound
    original.reuse_index=combined_index


def main():
    wire();p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['packet','finish']);p.add_argument('arm',choices=['C0','C1']);p.add_argument('suite',choices=contract.SUITES)
    p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40);a=p.parse_args()
    path=RUN/'evaluation'/a.arm/a.suite/'result.json'
    if a.mode=='finish':original.finish(path,path.with_name('authored_indices.tsv'))
    else:
        import json
        had_packet=path.with_name('packet.json').exists()
        packet=original.packet(path)
        if not had_packet:
            packet.update(exact_reuse_policy=ref(POLICY),review_adapter=ref(__file__),
                historical_config=read_json(POLICY)['historical_config'])
            original.atomic_json(path.with_name('packet.json'),packet)
        print(json.dumps(dict(total=219,manual_pending=packet['manual_pending'],reused=len(packet['reused']))))
        for i,(key,row) in enumerate(list(packet['pending'].items())[a.start:a.start+a.count],a.start):
            print(json.dumps(dict(index=i,key=key,**row),ensure_ascii=False))


if __name__=='__main__':main()
