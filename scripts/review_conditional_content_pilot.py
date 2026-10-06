"""Audit all96 content observations; do not certify facts or admit a training pool."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, write_json, now

DIMENSIONS = {'negation', 'quantity', 'time', 'comparison', 'entity', 'causality'}


def summarize(sample, notes, digest):
    rows = sample['rows']; observations = notes['notes']
    if (notes['sample_sha256'] != digest or notes['independent_human_blind'] is not False
            or len(rows) != 96 or len(observations) != 96
            or len({r['id'] for r in rows}) != 96
            or len({n[0] for n in observations}) != 96
            or {n[0] for n in observations} != {r['id'] for r in rows}):
        raise ValueError('All96 unique raw-bound observations required')
    by_id = {r['id']: r for r in rows}
    groups = {}
    for note in observations:
        if (len(note) != 8 or any(type(note[i]) is not int or note[i] not in (0, 1, 2) for i in (1, 2, 4))
                or any(type(note[i]) is not bool for i in (5, 6))
                or not isinstance(note[3], list) or len(set(note[3])) != len(note[3])
                or not set(note[3]) <= DIMENSIONS or not isinstance(note[7], str) or len(note[7]) < 12
                or note[5] and note[4] != 2):
            raise ValueError('Explicit rubric/dimensions/contrast/rationale required')
        groups.setdefault(by_id[note[0]]['genre'], []).append(note)
    if set(groups) != {'web', 'story', 'textbook'} or any(len(g) != 32 for g in groups.values()):
        raise ValueError('Original32/source coverage differs')
    return {genre: dict(documents=len(group), grammar2=sum(n[1] == 2 for n in group),
        standalone2=sum(n[2] == 2 for n in group), concrete_condition_outcome=sum(n[4] == 2 for n in group),
        two_conditions_different_outcomes=sum(n[5] for n in group),
        potential_content_issues=sum(n[6] for n in group),
        dimensions={d: sum(d in n[3] for n in group) for d in sorted(DIMENSIONS)},
        contrast_ids=[n[0] for n in group if n[5]]) for genre, group in sorted(groups.items())}


def main():
    folder = ROOT / 'reports/phase6/conditional-content-pilot-20261006'
    result = read_json(folder / 'result.json')
    if result['sample_sha256'] != sha256(folder / 'source-sample.json') or result['newly_prepared_tokens'] != 0:
        raise ValueError('Original fixed inspection changed')
    summary = summarize(read_json(folder / 'source-sample.json'), read_json(folder / 'content-notes.json'),
                        result['sample_sha256'])
    report = dict(status='all96_normalized_train_content_observations_complete', summary=summary,
        created_at=now(), sample_sha256=result['sample_sha256'],
        notes_sha256=sha256(folder / 'content-notes.json'), prior_result_sha256=sha256(folder / 'result.json'),
        all96_content_review_complete=True, training_pool_accepted=False, independent_human_blind=False,
        external_fact_certification=False, newly_prepared_tokens=0, scientific_teacher_tokens=0,
        actual_GPU_seconds=0, protected_test_used=False, Base_adopted=False, requested_five_steps_complete=False,
        conclusion='Causal/outcome stories are present and mostly locally coherent; the sample does not support calling all training material broken. Explicit alternate conditions with different outcomes are a smaller subset. Next inspect bounded source-grounded paired supply before selecting a conditional-discrimination learning comparison.',
        limitations='Fixed32/source,64..512 tokens, nonblind observations; category absence is not poor text. Local text-internal relation and possible factual/introductory issues are distinct. No whole-corpus prevalence, source-family independence, factual truth or model-capacity proof. No acceptance criterion changed.')
    write_json(folder / 'content-review.json', report)
    print(json.dumps(summary, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
