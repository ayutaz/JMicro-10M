"""Bind observations to the failed bounded V1 supply; never admit it for training."""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json


def main():
    folder = ROOT / 'reports/phase6/source-condition-pairs-20261006'
    result = read_json(folder / 'result.json')
    if result['source_pairs_sha256'] != sha256(folder / 'source-pairs.json'):
        raise ValueError('Original V1 supply changed')
    rows = read_json(folder / 'source-pairs.json')['rows']
    observations = []
    allowed = {'clear_contrast', 'overlapping', 'parse_error', 'needs_context'}
    for line in (folder / 'observations.tsv').read_text(encoding='utf-8').splitlines():
        identifier, category, reason = line.split('\t', 2)
        if category not in allowed or len(reason) < 12:
            raise ValueError('Explicit observation category and rationale required')
        observations.append(dict(id=identifier, category=category, reason=reason))
    if (len(rows) != 48 or len(observations) != 48
            or len({r['id'] for r in rows}) != 48
            or len({n['id'] for n in observations}) != 48
            or {r['id'] for r in rows} != {n['id'] for n in observations}):
        raise ValueError('All48 V1 observations required')
    for row in rows:
        text = row['original_text']
        if hashlib.sha256(text.encode('utf-8')).hexdigest() != row['decoded_body_sha256']:
            raise ValueError('Original normalized text differs')
        if row['source'] != 'textbook' or row['split'] != 'train':
            raise ValueError('Only selected train material may be inspected')
        if len(row['branches']) != 2 or row['choices'] != [b['outcome'] for b in row['branches']]:
            raise ValueError('Original two branches and choices required')
        for branch in row['branches']:
            if (branch['prefix'] != text[:branch['cut']]
                    or branch['outcome'] != text[branch['cut']:branch['end']]):
                raise ValueError('Original contiguous branch spans differ')
    if result['supply_target_met'] or result['pairs'] != 48:
        raise ValueError('This review records the failed48/512 supply, not a new run')
    write_json(folder / 'content-review.json', dict(
        status='all48_V1_observations_complete_supply_inadequate_not_admitted',
        created_at=now(), source_pairs_sha256=result['source_pairs_sha256'],
        prior_result_sha256=sha256(folder / 'result.json'),
        observations_sha256=sha256(folder / 'observations.tsv'), observations=observations,
        category_counts={c: sum(n['category'] == c for n in observations) for c in sorted(allowed)},
        all48_read=True, required_fixed_pilot_documents=64, actual_pilot_documents=48,
        target_pairs=512, actual_pairs=48, supply_target_met=False,
        training_pool_accepted=False, independent_human_blind=False,
        external_fact_certification=False, actual_GPU_seconds=0, scientific_teacher_tokens=0,
        newly_prepared_original_tokens=0, protected_test_used=False, Base_adopted=False,
        conclusion='Do not train V1: insufficient supply and lexical/contrast extraction failures. Clear textual contrasts do not certify alternative negatives or source factual truth.',
        next_action='One evidence-supported parser revision before a bounded new supply run: disambiguate lexical markers, reject progressive phrases, choose nearby conditions and preserve original spans. Freeze a new seed and exclude reviewed96+48; retain unchanged fixed64 content gate before learning.',
        limitations='Nonblind Codex observations of selected normalized train texts. No whole-corpus rates, source-family independence or verified hard negatives. No quality threshold changed. Base-only scope; Chat and quantization deferred.'))
    print(json.dumps(dict(reviewed=len(observations), supply_target_met=False,
                         training_pool_accepted=False, GPU_seconds=0)), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
