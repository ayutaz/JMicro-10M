"""Fixed64 nonblind source review; do not confuse readiness with Base quality."""
import argparse
import hashlib
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from prepare_livedoor_leads import inspect,RUN,DATA,family_split,reference


def main(observations):
    c=inspect();job=read_json(RUN/'job.json');ready=read_json(RUN/'ready.json')
    destination=RUN/'content-review.json'
    if destination.exists():raise ValueError('Preserve original fixed64 review')
    if (job['status']!='complete' or alive(job) or ready['config_sha256']!=sha256(ROOT/'configs/phase6/livedoor_leads_preparation.json')
            or ready['source_heldout_bodies_decoded'] or ready['protected_test_used']):raise ValueError('Actually completed TRAIN-only news preparation required')
    sample_path=Path(ready['sample']['path'])
    if sha256(sample_path)!=ready['sample']['sha256']:raise ValueError('Original fixed64 sample differs')
    rows=read_json(sample_path);notes={}
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields=line.split('\t')
        if len(fields)!=3 or fields[0] in notes or fields[1] not in ('0','1') or len(fields[2])<12:
            raise ValueError('One individual bound weak0/1 and rationale required')
        notes[fields[0]]=dict(weak=fields[1]=='1',rationale=fields[2])
    if len(rows)!=64 or len(notes)!=64 or set(notes)!={r['doc_id'] for r in rows}:raise ValueError('Complete original64, no replacements required')
    for row in rows:
        if (row['split']!='train' or family_split(row['article_id'])!='train'
                or hashlib.sha256(row['text'].encode()).hexdigest()!=row['canonical_sha256']):raise ValueError('Raw original TRAIN paragraph binding differs')
        notes[row['doc_id']].update(canonical_sha256=row['canonical_sha256'],original_article_sha256=row['original_article_sha256'],source_URL=row['source_URL'])
    index=read_json(Path(ready['pool'])/'train.index.json');train={r['doc_id'] for r in index}
    heldout=read_json(DATA/'heldout_article_ids.json')
    if train & {'livedoor-'+r['article_id'] for r in heldout} or any(family_split(r['article_id'])!=r['split'] for r in heldout):
        raise ValueError('Actual source article families must remain separate')
    weak=sum(n['weak'] for n in notes.values());passed=weak<=c['maximum_weak_documents']
    report=dict(status='fixed64_authored_news_content_reviewed',created_at=now(),documents=64,weak_documents=weak,
        maximum_weak_documents=c['maximum_weak_documents'],passed=passed,quality_accepted=passed,
        sample=ready['sample'],ready=reference(RUN/'ready.json'),observations=reference(observations),notes=notes,
        individually_read64=True,reviewer='Codex nonblind',independent_human_blind=False,
        rubric='Standalone coherent first paragraph with usable Japanese and no essential dangling reference; introductions/questions are allowed and need not provide the whole article. Major grammar, disconnected topic, dangling here/see-results or unqualified medical promotion are weak. Dated reported events are not automatically errors, and factual authenticity is not independently certified.',
        prepared_train_documents=len(index),prepared_body_tokens=ready['distinct_prepared_body_tokens'],prepared_stream_tokens=ready['splits']['train']['tokens'],
        scientific_teacher_tokens=0,GPU_seconds=0,source_heldout_bodies_decoded=False,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        limitations='Single nonblind fixed64 sample is a readiness screen, not all5050 paragraph audit or Base quality evidence. Advertisements, dated facts and introductory rather than full-article closure remain. Old Web overlap/global audit incomplete.',
        next_action='Accepted material permits a separate native10M same-d18/Web75M+news25M pilot, own CUDA resume/timing and forecast within1800 before scientific freeze; reused full100M controls, unchanged quality gates.' if passed else 'End this news source branch; no post-review selector/paragraph/reroll rescue.')
    atomic_json(destination,report);atomic_json(ROOT/'reports/phase6/livedoor_leads_content_review.json',report)
    print(dict(weak_documents=weak,passed=passed,body_tokens=report['prepared_body_tokens']))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('observations',type=Path);main(p.parse_args().observations)
