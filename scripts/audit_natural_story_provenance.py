"""One fixed64 provenance decomposition, CPU10s and8MiB index-read ceiling."""
from collections import Counter
from pathlib import Path
import sys
import time
import json
import hashlib
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from story_provenance_lookup import Reader, lookup
from prepare_natural_story_source import RUN, PROPOSAL


def reference(path): return dict(path=str(path), sha256=sha256(path))


def main():
    started = time.monotonic(); destination = ROOT/'reports/phase6/natural_story_provenance_result.json'
    freeze_path = ROOT/'reports/phase6/natural_story_provenance_freeze.json'
    if destination.exists() or freeze_path.exists(): raise ValueError('Preserve actual finite64 provenance audit')
    p = read_json(PROPOSAL); m = read_json(RUN/'manifest.json')
    pilot = read_json(RUN/'content-pilot.json'); review = read_json(RUN/'content-review.json')
    tests = ROOT/'reports/phase6/story_provenance_lookup_tests.xml'; suite = ET.parse(tests).getroot().find('testsuite')
    if int(suite.attrib['tests']) != 2 or any(int(suite.attrib[k]) for k in ('errors','failures','skipped')):
        raise ValueError('Bounded exact byte-seek tests required')
    if (not review['all64_read'] or review['training_pool_accepted'] or len(pilot['rows']) != 64
            or m['pilot_sha256'] != sha256(RUN/'content-pilot.json')
            or review['manifest_sha256'] != sha256(RUN/'manifest.json')):
        raise ValueError('Actual rejected all64 exact raw source required')
    cache = read_json(Path(m['cache']['path'])); index_path = Path(m['pool']['path'])/'train.index.jsonl'
    stat = index_path.stat()
    if (stat.st_size != cache['binding']['index_size'] or stat.st_mtime_ns != cache['binding']['index_mtime_ns']
            or cache['binding']['manifest_sha256'] != m['pool']['manifest_sha256']):
        raise ValueError('Existing immutable builder sorted-index identity differs')
    source_files = ('scripts/story_provenance_lookup.py', 'scripts/audit_natural_story_provenance.py', 'tests/test_story_provenance_lookup.py')
    atomic_json(freeze_path, dict(created_at=now(), CPU_ceiling_seconds=10, index_read_byte_ceiling=8*1024*1024,
        source_sha256={s:sha256(ROOT/s) for s in source_files}, tests=reference(tests),
        pilot=reference(RUN/'content-pilot.json'), content_review=reference(RUN/'content-review.json'),
        request_offsets=[r['offset'] for r in pilot['rows']], requested_records=64,
        source_index_identity=cache['binding'], purpose='All64 provenance/cohort characterization only; no content filter/retry/reroll/newsource/GPU.',
        scientific_teacher_tokens=0, GPU_seconds=0, protected_test_used=False))
    notes = {r['id']:r for r in review['notes']}; rows = []
    with index_path.open('rb') as stream:
        reader = Reader(stream)
        for row in pilot['rows']:
            if time.monotonic()-started > 10: raise TimeoutError('CPU10 second audit ceiling exceeded')
            original = lookup(reader, row['offset'], stat.st_size)
            if (original['offset'] != row['offset'] or original['body_tokens'] != row['body_tokens']
                    or original['split'] != 'train' or original['source'] != 'story'
                    or original['canonical_sha256'] != row['text_sha256']
                    or original.get('text', row['text']) != row['text']):
                raise ValueError('Exact native pilot and original TRAIN metadata must agree')
            family = original['source_family']
            if not isinstance(family, str): raise ValueError('Recorded source-family provenance required')
            rows.append(dict(id=row['id'], text_sha256=row['text_sha256'], original_metadata=original,
                weak_document=notes[row['id']]['weak_document'],
                unresolved_grammar_issue=notes[row['id']]['unresolved_grammar_issue']))
    after = index_path.stat()
    if (after.st_size, after.st_mtime_ns) != (stat.st_size, stat.st_mtime_ns): raise ValueError('Original index changed during read')
    elapsed = time.monotonic()-started
    if elapsed > 10: raise TimeoutError('CPU10 second audit ceiling exceeded')
    fields = sorted({k for r in rows for k in r['original_metadata']})
    atomic_json(destination, dict(status='all64_exact_original_TRAIN_story_provenance_recovered', created_at=now(),
        freeze=reference(freeze_path), CPU_elapsed_seconds=elapsed, CPU_ceiling_seconds=10,
        requested_records=64, recovered_records=64, index_bytes_read=reader.bytes_read,
        original_index_bytes=stat.st_size, index_read_byte_ceiling=8*1024*1024,
        exact_native_text_body_count_and_original_family_alignment=True, rows=rows,
        original_metadata_fields=fields, new_source_records=0, new_forward_requests=0,
        student_scientific_teacher_tokens=0, GPU_seconds=0, protected_test_used=False,
        original_source_and_pilot_unchanged=True, source_acceptance_changed=False,
        limitations='Source metadata are recorded builder provenance, not independent authorship/grammar certification.64 correlated material observations do not prove corpus-wide quality or model effects.'))
    print(json.dumps(dict(status='recovered64', CPU_seconds=elapsed, index_bytes_read=reader.bytes_read,
        metadata_fields=fields, sample_family=rows[0]['original_metadata']['source_family'])))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
