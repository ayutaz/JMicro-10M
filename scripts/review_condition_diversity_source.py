"""All fixed64 added originals; retain the existing paired-content gate."""
import hashlib
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from prepare_condition_diversity_source import OUT,SMALL,nested


def main():
    result=read_json(OUT/'result.json'); job=read_json(OUT/'job.json')
    if (job['status']!='complete' or alive(job) or result['documents']!=2048 or not result['supply_target_met']
            or result['selector_changed'] or result['source_pairs_sha256']!=sha256(OUT/'source-pairs.json')
            or result['content_pilot_sha256']!=sha256(OUT/'content-pilot.json')
            or result['small_source_sha256']!=sha256(SMALL/'source-pairs.json')):
        raise ValueError('Terminal adequate immutable nested source required')
    all_rows=read_json(OUT/'source-pairs.json')['rows']; nested(all_rows,read_json(SMALL/'source-pairs.json')['rows'])
    rows=read_json(OUT/'content-pilot.json')['rows']; notes=[]
    allowed={'negation','quantity','time','comparison','entity','causality'}
    for line in (OUT/'content-notes.tsv').read_text().splitlines():
        ident,score,weak,dimensions,issue,reason=line.split('\t',5)
        if (score not in ('0','1','2') or weak not in ('true','false') or issue not in ('true','false')
                or (weak=='true')!=(score!='2') or len(reason)<12 or not set(dimensions.split(','))<=allowed):
            raise ValueError('Same explicit paired-target rubric required')
        notes.append(dict(id=ident,paired_condition_outcome=int(score),weak_pair=weak=='true',
            dimensions=dimensions.split(','),potential_content_issue=issue=='true',reason=reason))
    if (len(rows)!=64 or len(notes)!=64 or len({n['id'] for n in notes})!=64
            or {n['id'] for n in notes}!={r['id'] for r in rows} or all_rows[512:576]!=rows):
        raise ValueError('Every fixed first64 newly added original must be read')
    for row in rows:
        text=row['original_text']
        if hashlib.sha256(text.encode()).hexdigest()!=row['decoded_body_sha256']: raise ValueError('Original bytes differ')
        for b in row['branches']:
            if b['prefix']!=text[:b['cut']] or b['outcome']!=text[b['cut']:b['end']]: raise ValueError('Original branch span differs')
    weak=sum(n['weak_pair'] for n in notes)
    report=dict(status='all64_new_nested_condition_content_review_complete',created_at=now(),
        all64_read=True,weak_pairs=weak,maximum_weak_pairs=10,paired_content_gate_passed=weak<=10,
        supply_target_met=True,training_pool_accepted=weak<=10,notes=notes,
        notes_sha256=sha256(OUT/'content-notes.tsv'),source_pairs_sha256=result['source_pairs_sha256'],
        content_pilot_sha256=result['content_pilot_sha256'],preparation_result_sha256=sha256(OUT/'result.json'),
        documents=2048,old512_retained_exactly=True,selector_changed=False,
        independent_human_blind=False,external_fact_certification=False,newly_prepared_original_tokens=0,
        scientific_teacher_tokens=0,actual_GPU_seconds=0,protected_test_used=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,
        rubric='Unchanged paired target2: two text-explicit conditions on coherent shared topic with concrete differing outcomes.1: weak/nested/same-condition or unspecified second outcome.0: lexical/rhetorical/question parse lacks real paired conditions. Weak is target<2, not whole-text invalidity. Domain claims, Korean fragments and strong factual assertions flagged separately, not reclassified to pass/fail pair gate. Neither outcome is an incompatible hard negative.',
        next_action='Original train IDs and masks preparation; known old8+new weak spans focus-disabled while whole ordinary CE retained; weight1 comparison only after commands/resume/measurement freeze.',
        limitations='Codex nonblind selected64 new examples, no global/source-family/near-duplicate/factual guarantee. All512 originals remain identical; global2B original corpus unchanged. No automatic reroll of this sample or selector revision.')
    atomic_json(OUT/'content-review.json',report)
    print(dict(reviewed=64,weak_pairs=weak,training_pool_accepted=weak<=10))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
