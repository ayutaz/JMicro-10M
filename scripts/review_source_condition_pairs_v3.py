"""Review the fixed64 V3 paired-target pilot without changing its content gate."""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json


def main():
    folder = ROOT / 'reports/phase6/source-condition-pairs-v3-20261006'
    result = read_json(folder / 'result.json')
    if (result['content_pilot_sha256'] != sha256(folder / 'content-pilot.json')
            or result['source_pairs_sha256'] != sha256(folder / 'source-pairs.json')):
        raise ValueError('Original V3 supply and fixed first64 changed')
    rows = read_json(folder / 'content-pilot.json')['rows']
    notes = []
    allowed = {'negation', 'quantity', 'time', 'comparison', 'entity', 'causality'}
    for line in (folder / 'content-notes.tsv').read_text(encoding='utf-8').splitlines():
        identifier, score, weak, dimensions, issue, reason = line.split('\t', 5)
        if (score not in ('0', '1', '2') or weak not in ('true', 'false')
                or issue not in ('true', 'false') or len(reason) < 12
                or not set(dimensions.split(',')) <= allowed
                or (weak == 'true') != (score != '2')):
            raise ValueError('Explicit paired-target rubric and rationale required')
        notes.append(dict(id=identifier, paired_condition_outcome=int(score), weak_pair=weak == 'true',
                          dimensions=dimensions.split(','), potential_content_issue=issue == 'true', reason=reason))
    if (len(rows) != 64 or len(notes) != 64 or len({n['id'] for n in notes}) != 64
            or {n['id'] for n in notes} != {r['id'] for r in rows}
            or read_json(folder / 'source-pairs.json')['rows'][:64] != rows):
        raise ValueError('All fixed first64 observations required')
    for row in rows:
        text = row['original_text']
        if hashlib.sha256(text.encode('utf-8')).hexdigest() != row['decoded_body_sha256']:
            raise ValueError('Original text differs')
        for branch in row['branches']:
            if branch['prefix'] != text[:branch['cut']] or branch['outcome'] != text[branch['cut']:branch['end']]:
                raise ValueError('Source-original contiguous spans differ')
    weak = sum(n['weak_pair'] for n in notes)
    write_json(folder / 'content-review.json', dict(
        status='fixed64_V3_paired_target_content_review_complete', created_at=now(),
        source_pairs_sha256=result['source_pairs_sha256'], content_pilot_sha256=result['content_pilot_sha256'],
        preparation_result_sha256=sha256(folder / 'result.json'),
        notes_sha256=sha256(folder / 'content-notes.tsv'), notes=notes,
        all64_read=True, weak_pairs=weak, maximum_weak_pairs=10, paired_content_gate_passed=weak <= 10,
        supply_target_met=result['supply_target_met'],
        training_pool_accepted=result['supply_target_met'] and weak <= 10,
        dimensions={d: sum(d in n['dimensions'] for n in notes) for d in sorted(allowed)},
        paired_condition_outcome2=sum(n['paired_condition_outcome'] == 2 for n in notes),
        independent_human_blind=False, external_fact_certification=False,
        newly_prepared_original_tokens=0, scientific_teacher_tokens=0, actual_GPU_seconds=0,
        protected_test_used=False, Base_adopted=False,
        rubric='Paired target2: two text-explicit conditions on a coherent shared topic with concrete differing outcomes.1: weak/nested/same-condition cases or unspecified second outcome.0: lexical/rhetorical/question parse lacks real paired conditions. weak means target<2, not globally bad original text. Potential domain-factual issues are flagged separately; unverified claims alone do not determine pair failure. Neither original outcome is certified an incompatible hard negative.',
        conclusion='Explicit-opposition source-pair pilot: preserve exact weak count and unchanged10/64 gate. Original continuations may support a bounded positive-CE Base study after command/config/GPU budget preparation; no incompatible-negative labels are certified.',
        limitations='Rows retain run-local condition-v2 IDs; bind by this run path and raw hashes. Nonblind selected train normalized text only; no source-family/global dedup/factual/corpus certification. No model-quality gate or scoring changed. Base-only scope.'))
    print(json.dumps(dict(reviewed=64, weak_pairs=weak, maximum_weak_pairs=10,
                         paired_content_gate_passed=weak <= 10, GPU_seconds=0)), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
