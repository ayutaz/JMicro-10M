"""Fixed train calibration, not acceptance grading or a semantic classifier."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.condition_story_quality import exclusion_reasons as v1
from jmicro.condition_story_quality_v2 import exclusion_reasons as v2
from prepare_condition_v2 import DATA, RUN


def main():
    assert sys.version_info[:3] == (3, 12, 7)
    calibration = read_json(DATA / 'calibration.json')
    notes_path = ROOT / 'reports/phase6/condition_v2_calibration_notes.json'
    authored = read_json(notes_path)
    notes = authored['notes']
    assert len(notes) == len(calibration['rows']) == 32
    assert [n[0] for n in notes] == list(range(32))
    assert all(type(n[1]) is bool and len(n[2]) >= 15 for n in notes)
    known = set(calibration['previous_inspected_hashes'])
    assert not known.intersection(r['text_sha256'] for r in calibration['rows'])
    rows = [dict(row, weak_example=weak, rationale=reason,
        v1_reasons=v1(row['text']), v2_reasons=v2(row['text']))
        for row, (_, weak, reason) in zip(calibration['rows'], notes)]
    assert all(not r['v1_reasons'] for r in rows), 'Calibration samples must meet frozen v1'
    counts = dict(total=32, weak_examples=sum(r['weak_example'] for r in rows),
        v2_excluded_weak=sum(r['weak_example'] and bool(r['v2_reasons']) for r in rows),
        v2_excluded_valid=sum(not r['weak_example'] and bool(r['v2_reasons']) for r in rows),
        v2_remaining_weak=sum(r['weak_example'] and not r['v2_reasons'] for r in rows),
        v2_remaining_valid=sum(not r['weak_example'] and not r['v2_reasons'] for r in rows))
    result = dict(status='calibration_completed', counts=counts, rows=rows,
        sampling=calibration['sampling'], calibration_sha256=sha256(DATA / 'calibration.json'),
        notes_sha256=sha256(notes_path), selector_sha256=sha256(ROOT / 'src/jmicro/condition_story_quality_v2.py'),
        reviewer_sha256=sha256(Path(__file__)), reviewer=authored['reviewer'], rubric=authored['rubric'],
        interpretation='Train calibration used to develop rules; counts are training diagnostics, not held-out estimates. Frozen unseen40 each decide preparation readiness.',
        not_covered=['general arithmetic/size reasoning','all implicit reference chains','unusual lexical/world-knowledge correctness'],
        additional_scientific_training_tokens=0, protected_test_used=False, checked_at=now())
    DATA.mkdir(parents=True, exist_ok=True); RUN.mkdir(parents=True, exist_ok=True)
    write_json(DATA / 'calibration-review.json', result)
    print(json.dumps(dict(status=result['status'], counts=counts, excluded_examples=[r['calibration_index'] for r in rows if r['v2_reasons']])))


if __name__ == '__main__':
    main()
