"""All64 raw-bound content observations and inherited weak<=10 acceptance."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive


def main(revision):
    suffix='' if revision=='v1' else '-v2'
    data=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-transfer-curriculum-20261006'+suffix)
    run=ROOT/('reports/phase6/condition-transfer-curriculum-20261006'+suffix)
    job=read_json(run/'job.json');manifest=read_json(data/'manifest.json');pilot=read_json(data/'content-pilot.json')
    note_path=data/'content-notes.json';raw_notes=read_json(note_path);notes=raw_notes['notes']
    if (job['status']!='complete_pending_fixed64_content' or alive(job)
            or job['manifest_sha256']!=sha256(data/'manifest.json')
            or manifest['pilot_sha256']!=sha256(data/'content-pilot.json')
            or raw_notes['pilot_sha256']!=manifest['pilot_sha256'] or not raw_notes['all64_individually_read']
            or len(notes)!=64 or len({n['id'] for n in notes})!=64
            or {n['id'] for n in notes}!={r['id'] for r in pilot['rows']}):
        raise ValueError('Actual terminal fixed64 and every raw-bound observation required')
    rows={r['id']:r for r in pilot['rows']}
    for n in notes:
        r=rows[n['id']]
        if (n['text_sha256']!=r['text_sha256'] or n['paired_condition_outcome'] not in (0,1,2)
                or type(n['weak_document']) is not bool or n['weak_document']!=(n['paired_condition_outcome']!=2)
                or type(n['unresolved_grammar_issue']) is not bool or len(n['reason'])<12
                or r['text']!=r['prefix']+r['outcome'] or r['outcome']!=r['choices'][r['label']]):
            raise ValueError('Explicit same content rubric and raw continuation required')
    weak=sum(n['weak_document'] for n in notes);grammar=sum(n['unresolved_grammar_issue'] for n in notes)
    review=dict(status='all64_generated_content_review_complete',created_at=now(),all64_read=True,weak_documents=weak,
        maximum_weak_documents=10,paired_content_gate_passed=weak<=10,unresolved_grammar_documents=grammar,
        training_pool_accepted=weak<=10 and grammar==0,pilot_sha256=manifest['pilot_sha256'],manifest_sha256=sha256(data/'manifest.json'),
        notes_sha256=sha256(note_path),notes=notes,independent_human_blind=False,external_fact_certification=False,
        rubric='Original weak<=10 retained. Explicit proposal also rejects unresolved grammar defects; logical source-state consistency is separate from fluent wording. Opposed sibling documents share candidates and differ in a stated local condition. Device rules are local definitions.',
        generated_local_source=True,scientific_teacher_tokens=0,actual_GPU_seconds=0,protected_test_used=False,
        Base_adopted=False,Chat_started=False,quantization_started=False,
        limitations='Codex nonblind first64,32 paired families,24 authored forms. Not independent human evaluation or2048 semantic domains. Do not reroll pilot or infer global real-world fact correctness.')
    atomic_json(data/'content-review.json',review);atomic_json(run/'content-review.json',review)
    atomic_json(ROOT/f'reports/phase6/condition_source_transfer_{revision}_content_review.json',review)
    print(dict(reviewed=64,weak_documents=weak,unresolved_grammar_documents=grammar,training_pool_accepted=review['training_pool_accepted']))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();p.add_argument('--revision',choices=('v1','v2'),required=True);a=p.parse_args();main(a.revision)
