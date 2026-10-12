"""Evidence-only matching for reuse of already read unchanged TRAIN samples."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import read_json,sha256,now
from jmicro.training import atomic_json
from prepare_chat_generalization_train import DATA,RUN


def main():
    prior_path=RUN/'preparation-attempt-v6/train_content_review_final.json'
    prior=read_json(prior_path);old_packet=DATA/'v6-train_review_packet.jsonl';new_packet=DATA/'train_review_packet.jsonl'
    assert sha256(old_packet)==prior['packet_sha256']
    old=[json.loads(l) for l in old_packet.read_text().splitlines()]
    new=[json.loads(l) for l in new_packet.read_text().splitlines()]
    assert len(old)==len(new)==280
    prior_notes={n['doc_id']:n for n in prior['judgments']};reused=[];changed=[]
    for index,(a,b) in enumerate(zip(old,new,strict=True)):
        identical=all(a.get(k)==b.get(k) for k in ('messages','category','target_message_indices','doc_id','content_sha256'))
        if identical and prior_notes[a['doc_id']]['passed']:
            reused.append(dict(index=index,doc_id=b['doc_id'],content_sha256=b['content_sha256'],
                original_judgment=prior_notes[a['doc_id']]))
        else:changed.append(dict(index=index,doc_id=b['doc_id'],messages=b['messages'],prior_passed=prior_notes.get(a['doc_id'],{}).get('passed')))
    record=dict(created_at=now(),passed=True,source_sha256=sha256(Path(__file__)),
        prior_review=dict(path=str(prior_path),sha256=sha256(prior_path)),
        prior_packet=dict(path=str(old_packet),sha256=sha256(old_packet)),
        current_packet=dict(path=str(new_packet),sha256=sha256(new_packet)),
        current_candidate_sha256=sha256(DATA/'candidate.train.jsonl'),reused=reused,requires_actual_new_review=changed,
        reused_count=len(reused),changed_count=len(changed),automatic_new_content_grading=False)
    atomic_json(RUN/'train_review_reuse.json',record)
    print(json.dumps(dict(reused=len(reused),requires_actual_new_review=len(changed))))
    for r in changed:print(json.dumps(r,ensure_ascii=False))


if __name__=='__main__':main()
