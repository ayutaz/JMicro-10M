"""Freeze only after actual authored content notes and complete sampler gate."""
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import now,read_json,sha256
from jmicro.training import atomic_json
from jmicro.chat_generalization_curriculum import semantic_check
from prepare_chat_generalization_train import DATA,D0,RUN,dump_jsonl,content_binding,WEIGHTS


def main():
    assert not (DATA/'manifest.json').exists() and not (DATA/'dev.jsonl').exists()
    candidate=DATA/'candidate.train.jsonl';packet=DATA/'train_review_packet.jsonl'
    review=read_json(RUN/'train_content_review_final.json')
    assert review['status']=='fixed_sample_passed' and review['samples']==280 and review['errors']==0
    assert review['candidate_sha256']==sha256(candidate) and review['packet_sha256']==sha256(packet)
    rows=[json.loads(l) for l in candidate.read_text().splitlines()];by_id={r['doc_id']:r for r in rows}
    assert len(by_id)==len(rows)
    selected=[json.loads(l) for l in packet.read_text().splitlines()]
    assert len(selected)==len(review['judgments'])==280
    notes={r['doc_id']:r for r in review['judgments']};assert len(notes)==280
    for r in selected:
        assert r==by_id[r['doc_id']]
        assert notes[r['doc_id']]['passed'] and notes[r['doc_id']]['content_sha256']==r['content_sha256']
        assert len(notes[r['doc_id']]['rationale'])>=12
    for r in rows:
        assert r['content_sha256']==content_binding(r)
        if r['source']=='project-authored-plan133-train':assert semantic_check(r)
    dry=read_json(RUN/'consumption_dry_run.json')
    assert dry['status']=='passed' and all(dry['checks'].values())
    assert dry['D1']['source_sha256']==sha256(candidate)
    counts=Counter(r['category'] for r in rows);teachers=sum(r['teacher_tokens'] for r in rows)
    single=sum(len(r['messages'])==2 for r in rows)
    assert single/len(rows)>=.50,'First-turn coverage must actually improve'
    dump_jsonl(DATA/'train.jsonl',rows);assert sha256(DATA/'train.jsonl')==sha256(candidate)
    manifest=dict(created_at=now(),status='reviewed_TRAIN_frozen_before_new_DEV',vocab_size=4096,
        train=dict(path=str(DATA/'train.jsonl'),sha256=sha256(DATA/'train.jsonl'),targets=len(rows),teachers_per_pass=teachers),
        design_freeze=dict(path=str(RUN/'train_design_freeze.json'),sha256=sha256(RUN/'train_design_freeze.json')),
        review=dict(path=str(RUN/'train_content_review_final.json'),sha256=sha256(RUN/'train_content_review_final.json')),
        consumption=dict(path=str(RUN/'consumption_dry_run.json'),sha256=sha256(RUN/'consumption_dry_run.json')),
        categories=dict(counts),single_User_targets=single,single_User_fraction=single/len(rows),
        parameter_change=False,independent_human_review=False,all_TRAIN_human_certified=False,
        protected_TEST_used=False,Base_adopted=False,Chat_adopted=False)
    atomic_json(DATA/'manifest.json',manifest)
    atomic_json(RUN/'train_preparation.json',dict(manifest,manifest_path=str(DATA/'manifest.json'),manifest_sha256=sha256(DATA/'manifest.json')))
    print(json.dumps(manifest['train'],ensure_ascii=False))


if __name__=='__main__':main()
