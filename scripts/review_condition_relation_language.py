"""Fixed64 source acceptance; preserve original weak and grammar criteria."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from condition_relation_language import DATA
from prepare_condition_relation_language import RUN


def main():
    job=read_json(RUN/'job.json'); manifest=read_json(DATA/'manifest.json'); pilot=read_json(DATA/'content-pilot.json')
    path=DATA/'content-notes.json'; raw=read_json(path); notes=raw['notes']
    if (job['status']!='complete_pending_fixed64_content' or alive(job) or job['manifest_sha256']!=sha256(DATA/'manifest.json')
            or manifest['pilot_sha256']!=sha256(DATA/'content-pilot.json') or raw['pilot_sha256']!=manifest['pilot_sha256']
            or not raw['all64_individually_read'] or len(notes)!=64 or len({n['id'] for n in notes})!=64
            or {n['id'] for n in notes}!={r['id'] for r in pilot['rows']}):
        raise ValueError('Terminal fixed64 and every raw-bound observation required')
    rows={r['id']:r for r in pilot['rows']}
    for n in notes:
        r=rows[n['id']]
        if (n['text_sha256']!=r['text_sha256'] or type(n['paired_condition_outcome']) is not int or n['paired_condition_outcome'] not in (0,1,2)
                or type(n['weak_document']) is not bool or n['weak_document']!=(n['paired_condition_outcome']!=2)
                or type(n['unresolved_grammar_issue']) is not bool or len(n['reason'])<12
                or r['text']!=r['prefix']+r['outcome'] or r['outcome']!=r['choices'][r['label']]):
            raise ValueError('Same content rubric and exact continuation required')
    weak=sum(n['weak_document'] for n in notes); grammar=sum(n['unresolved_grammar_issue'] for n in notes)
    report=dict(status='all64_relation_language_source_review_complete',created_at=now(),all64_read=True,
        weak_documents=weak,maximum_weak_documents=10,paired_content_gate_passed=weak<=10,unresolved_grammar_documents=grammar,
        training_pool_accepted=weak<=10 and grammar==0,pilot_sha256=manifest['pilot_sha256'],manifest_sha256=sha256(DATA/'manifest.json'),
        notes_sha256=sha256(path),notes=notes,independent_human_blind=False,external_fact_certification=False,
        rubric='Original weak<=10 and no unresolved grammar. Logical local state and natural wording judged separately; exact unchanged full texts reuse prior notes.',
        generated_local_source=True,scientific_teacher_tokens=0,actual_GPU_seconds=0,protected_test_used=False,
        Base_adopted=False,Chat_started=False,quantization_started=False,
        limitations='Codex nonblind64/32 pairs; local authored material, not independent human or model quality proof.')
    atomic_json(DATA/'content-review.json',report);atomic_json(RUN/'content-review.json',report)
    atomic_json(ROOT/'reports/phase6/condition_relation_language_content_review.json',report)
    print(dict(reviewed=64,weak_documents=weak,unresolved_grammar_documents=grammar,training_pool_accepted=report['training_pool_accepted']))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
