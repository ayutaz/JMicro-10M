"""All2628 exact32-token raw reviews using unchanged literal content rubric."""
import argparse
from pathlib import Path
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
from answer_learning_common import ref,bound
import review_chat_natural as original


def wire():
    original.CONFIG=CONFIG;original.RUN=RUN;original.SUITES=contract.SUITES
    original.read_dev=contract.read_dev;original.require_ref=bound


def main():
    wire();p=argparse.ArgumentParser()
    p.add_argument('mode',choices=['packet','finish']);p.add_argument('arm',choices=['C0','C1']);p.add_argument('suite',choices=contract.SUITES)
    p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40);a=p.parse_args()
    path=RUN/'evaluation'/a.arm/a.suite/'result.json'
    if a.mode=='finish':original.finish(path,path.with_name('authored_indices.tsv'))
    else:
        import json
        packet=original.packet(path)
        print(json.dumps(dict(total=219,manual_pending=packet['manual_pending'],reused=len(packet['reused']))))
        for i,(key,row) in enumerate(list(packet['pending'].items())[a.start:a.start+a.count],a.start):
            print(json.dumps(dict(index=i,key=key,**row),ensure_ascii=False))


if __name__=='__main__':main()
