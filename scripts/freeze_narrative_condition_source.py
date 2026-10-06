"""Bind the one source preparation before actual pilot creation/review."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from prepare_narrative_condition_source import FREEZE, PROPOSAL, SOURCES, DATA, RUN


def main():
    if FREEZE.exists() or DATA.exists() or (RUN / 'job.json').exists():
        raise ValueError('Preserve the existing fixed source; do not refreeze/reroll')
    tests = ROOT / 'reports/phase6/narrative_condition_source_tests.xml'
    suite = ET.parse(tests).getroot().find('testsuite')
    if suite is None or int(suite.attrib['tests']) != 4 or any(int(suite.attrib[k]) for k in ('errors', 'failures', 'skipped')):
        raise ValueError('Four successful semantic/codec/continuation/content-protocol tests required')
    p = read_json(PROPOSAL)
    for ref in (p['source']['manifest'], p['source']['train_source'], p['source']['accepted_review']):
        if sha256(Path(ref['path'])) != ref['sha256']: raise ValueError('Original source differs')
    atomic_json(FREEZE, dict(status='TRAIN_narrative_renderer_input_sampling_frozen_before_actual_source', created_at=now(),
        proposal_sha256=sha256(PROPOSAL), source_sha256={s: sha256(ROOT / s) for s in SOURCES},
        tests=dict(path=str(tests), sha256=sha256(tests), count=4, CPU_seconds=float(suite.attrib['time']), GPU_seconds=0),
        original_TRAIN_source=p['source'], seed=2026100691, CPU_ceiling_seconds=60,
        prospective_documents=16384, content_pilot_documents=64,
        selection='All48 category/surface cells fixed seed draws then16 additional unique TRAIN draws; no reroll/filter',
        no_actual_pilot_created_or_content_read_yet=True, actual_GPU_seconds=0, scientific_teacher_tokens=0,
        Base_complete=False, Chat_started=False, quantization_started=False, protected_test_used=False))
    print(dict(status='frozen', freeze_sha256=sha256(FREEZE)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
