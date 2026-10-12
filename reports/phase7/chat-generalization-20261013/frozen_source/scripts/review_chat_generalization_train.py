"""Expose actual fixed TRAIN samples and bind explicit authored QA notes."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import read_json,sha256,now
from jmicro.training import atomic_json
from prepare_chat_generalization_train import DATA,RUN


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('packet','finish'))
    p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=40)
    p.add_argument('--compact',action='store_true')
    p.add_argument('--notes',type=Path);args=p.parse_args()
    packet=DATA/'train_review_packet.jsonl';candidate=DATA/'candidate.train.jsonl'
    rows=[json.loads(l) for l in packet.read_text().splitlines()];assert len(rows)==280
    if args.mode=='packet':
        for index,r in enumerate(rows[args.start:args.start+args.count],args.start):
            if args.compact:
                print(json.dumps([index,r['category'],[m['text'] for m in r['messages']]],ensure_ascii=False));continue
            print(json.dumps(dict(index=index,doc_id=r['doc_id'],category=r['category'],
                messages=r['messages'],target=r['target_message_indices'],
                content_sha256=r['content_sha256']),ensure_ascii=False))
    else:
        assert args.notes is not None and not (RUN/'train_content_review_final.json').exists()
        notes=[]
        for line in args.notes.read_text().splitlines():
            if not line.strip():continue
            index,passed,reason=line.split('\t',2);index=int(index)
            assert passed in ('0','1') and len(reason)>=12
            r=rows[index];notes.append(dict(index=index,doc_id=r['doc_id'],
                content_sha256=r['content_sha256'],passed=passed=='1',rationale=reason))
        assert len(notes)==len({r['index'] for r in notes})==280
        assert set(r['index'] for r in notes)==set(range(280))
        errors=sum(not r['passed'] for r in notes)
        reuse_path=RUN/'train_review_reuse.json';reuse=None
        if reuse_path.exists():
            data=read_json(reuse_path)
            assert data['current_packet']['sha256']==sha256(packet) and data['current_candidate_sha256']==sha256(candidate)
            by_index={n['index']:n for n in notes}
            for old in data['reused']:
                actual=by_index[old['index']]
                assert actual['content_sha256']==old['content_sha256'] and actual['passed']==old['original_judgment']['passed']
                assert actual['rationale']==old['original_judgment']['rationale']
            reuse=dict(path=str(reuse_path),sha256=sha256(reuse_path),count=data['reused_count'],
                newly_reviewed=data['changed_count'])
        atomic_json(RUN/'train_content_review_final.json',dict(created_at=now(),
            status='fixed_sample_passed' if errors==0 else 'candidate_content_failed',
            samples=280,errors=errors,judgments=sorted(notes,key=lambda r:r['index']),
            candidate_sha256=sha256(candidate),packet_sha256=sha256(packet),
            authored_notes=dict(path=str(args.notes.resolve()),sha256=sha256(args.notes)),
            source_sha256=sha256(Path(__file__)),prior_actual_review_reuse=reuse,reviewer='Codex nonblind',
            independent_human=False,all_TRAIN_human_certified=False,automatic_semantic_grader=False))
        print(json.dumps(dict(samples=280,errors=errors)))


if __name__=='__main__':main()
