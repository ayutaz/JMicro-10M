"""Reuse only raw-bound identical prior content judgments; leave new scores blank."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.training import atomic_json
from review_textbook_quantity_comparison import validate_notes
import run_web_kl_comparison as study
import prepare_mature_base_content_review as previous

REFERENCES = (
    ('condition_positive_control', 'condition-positive-comparison-20261006', 'control'),
    ('condition_positive_positive4', 'condition-positive-comparison-20261006', 'positive4'),
    ('story_weight_control', 'story-weight-comparison-20261006', 'control'),
    ('story_weight_story20', 'story-weight-comparison-20261006', 'story20'),
    ('condition_diversity_large2048', 'condition-diversity-comparison-20261006', 'large2048'),
    ('condition_source_learning_small512', 'condition-source-learning-100m-20261006', 'small512'),
    ('condition_source_learning_large2048', 'condition-source-learning-100m-20261006', 'large2048'),
    ('condition_transfer_curriculum', 'condition-transfer-comparison-20261006', 'curriculum'),
    ('condition_relation_language', 'condition-relation-comparison-20261006', 'relation'),
)


def key(row):
    return tuple(row[k] for k in ('id', 'prefix', 'text', 'stop_reason'))


def lookup():
    saved,refs=previous.lookup()
    stage_notes=ROOT/'reports/phase6/source_order_condition_notes.json'
    stage_raw=study.cached.RUN/'evaluation/source_order/evaluation/generation.json'
    generation,notes=read_json(stage_raw),read_json(stage_notes)
    validate_notes(generation['outputs'],notes,sha256(stage_raw))
    indexed={n[0]:n for n in notes['notes']}
    for row in generation['outputs']:
        k=key(row);note=indexed[row['id']]
        if k in saved and saved[k]!=note:raise ValueError('Conflicting exact staged peer notes')
        saved[k]=note
    refs.append(dict(notes=study.reference(stage_notes),generation=study.reference(stage_raw)))
    notes_path=ROOT/'reports/phase6/original_web_retention_notes.json'
    raw=study.previous.RUN/'evaluation/original_web/evaluation/generation.json'
    generation,notes=read_json(raw),read_json(notes_path)
    validate_notes(generation['outputs'],notes,sha256(raw))
    indexed={n[0]:n for n in notes['notes']}
    for row in generation['outputs']:
        k=key(row);note=indexed[row['id']]
        if k in saved and saved[k]!=note:raise ValueError('Conflicting identical peer notes')
        saved[k]=note
    refs.append(dict(notes=study.reference(notes_path),generation=study.reference(raw)))
    early_notes=ROOT/'reports/phase6/early_exposure_notes.json'
    early_raw=ROOT/'reports/phase6/early-exposure-comparison-20261006/evaluation/early8M/evaluation/generation.json'
    raw,notes=read_json(early_raw),read_json(early_notes)
    validate_notes(raw['outputs'],notes,sha256(early_raw))
    indexed={n[0]:n for n in notes['notes']}
    for row in raw['outputs']:
        k=key(row);note=indexed[row['id']]
        if k in saved and saved[k]!=note:raise ValueError('Conflicting identical early peer notes')
        saved[k]=note
    refs.append(dict(notes=study.reference(early_notes),generation=study.reference(early_raw)))
    query_notes=ROOT/'reports/phase6/condition_query_balance_notes.json'
    query_raw=ROOT/'reports/phase6/condition-query-balance-comparison-20261006/evaluation/query_balanced/evaluation/generation.json'
    raw,notes=read_json(query_raw),read_json(query_notes)
    validate_notes(raw['outputs'],notes,sha256(query_raw))
    indexed={n[0]:n for n in notes['notes']}
    for row in raw['outputs']:
        k=key(row);note=indexed[row['id']]
        if k in saved and saved[k]!=note:raise ValueError('Conflicting exact query peer notes')
        saved[k]=note
    refs.append(dict(notes=study.reference(query_notes),generation=study.reference(query_raw)))
    control_notes=ROOT/'reports/phase6/historical_parent_condition_notes.json'
    control_raw=study.cached.cached.RUN/'evaluation/historical_parent/evaluation/generation.json'
    raw,notes=read_json(control_raw),read_json(control_notes)
    validate_notes(raw['outputs'],notes,sha256(control_raw))
    indexed={n[0]:n for n in notes['notes']}
    for row in raw['outputs']:
        k=key(row);note=indexed[row['id']]
        if k in saved and saved[k]!=note:raise ValueError('Conflicting exact historical control notes')
        saved[k]=note
    refs.append(dict(notes=study.reference(control_notes),generation=study.reference(control_raw)))
    return saved,refs


def prepare(arm):
    raw = study.RUN / f'evaluation/{arm}/evaluation/generation.json'
    generation = read_json(raw)
    if len(generation['outputs']) != 80:
        raise ValueError('All80 actual outputs required')
    saved, refs = lookup()
    notes, reused = [], []
    for row in generation['outputs']:
        if key(row) in saved:
            notes.append(saved[key(row)]); reused.append(row['id'])
        else:
            notes.append([row['id'], None, None, None, None, ''])
    folder = study.RUN / 'content-packets'
    path = folder / f'{arm}.json'
    packet = dict(stage='individual_reading_required_not_content_evidence', arm=arm,
        generation=study.reference(raw), references=refs, outputs=generation['outputs'],
        notes=notes, exact_reused_ids=reused, all_current_outputs_individually_read=False)
    if path.exists() and read_json(path) != packet:
        raise ValueError('Preserve existing content packet')
    atomic_json(path, packet)
    print(json.dumps(dict(arm=arm, outputs=80, exact_prior_notes=len(reused), new_notes_required=80-len(reused))))


def finish(arm, observations):
    packet = read_json(study.RUN / f'content-packets/{arm}.json')
    study.check_reference(packet['generation'])
    for ref in packet['references']:
        study.check_reference(ref['notes']); study.check_reference(ref['generation'])
    rows = packet['outputs']
    if read_json(Path(packet['generation']['path']))['outputs'] != rows:
        raise ValueError('Content packet raw outputs differ')
    raw_notes = []
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields = line.split('\t')
        if len(fields) != 6: raise ValueError('One individual six-field observation per output required')
        raw_notes.append([fields[0], *(int(v) for v in fields[1:5]), fields[5]])
    raw = dict(reviewer='Codex nonblind; all80 individually read', independent_human_blind=False,
        generation_sha256=packet['generation']['sha256'], notes=raw_notes)
    validate_notes(rows, raw, packet['generation']['sha256'])
    # A peer arm may finish after this packet was prepared. Keep its exact notes
    # too, so matched arms cannot drift merely because they were read later.
    historical, references = lookup()
    observations_by_id = {n[0]:n for n in raw_notes}
    reused = [r['id'] for r in rows if key(r) in historical]
    raw['notes'] = [historical.get(key(r), observations_by_id[r['id']]) for r in rows]
    raw['rubric_consistency_reuse'] = dict(keys=['id','prefix','text','stop_reason'],
        references=references, reused_ids=reused,
        all_current_outputs_individually_read=True,
        observations=study.reference(observations),
        limitations='Nonblind Codex judgments; fantasy and valid alternate continuations allowed; numeric correctness separated from grammar; EOS alone is not appropriate completion.')
    validate_notes(rows, raw, packet['generation']['sha256'])
    path = ROOT / 'reports/phase6/web_kl_notes.json'
    if path.exists(): raise ValueError('Preserve existing completed notes')
    atomic_json(path, raw)
    print(f'{arm}: all80 individually read; {len(reused)} exact prior notes reused')


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser(); p.add_argument('--arm', choices=(study.ARM,), required=True)
    p.add_argument('--observations', type=Path); args = p.parse_args()
    if args.observations: finish(args.arm, args.observations)
    else: prepare(args.arm)
