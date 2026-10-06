"""Bind the complete fixed64 whole-prose review, independently of volume."""
from collections import Counter
import json
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT, read_json, sha256, write_json, now
from phase6_performance import alive
from prepare_public_magpie_prose import RUN, DATA, PROPOSAL, split_family


def main():
    job = read_json(RUN/'job.json'); result = read_json(RUN/'result.json')
    manifest = read_json(DATA/'manifest.json'); samples = read_json(RUN/'fixed64.json')
    observations = ROOT/'reports/phase6/public_magpie_prose_observations.tsv'
    output = ROOT/'reports/phase6/public_magpie_prose_content_review.json'
    if job['status'] != 'complete' or alive(job) or result['GPU_seconds'] or result['student_scientific_teacher_tokens']:
        raise ValueError('Actual terminal CPU-only preparation required')
    if (sha256(DATA/'manifest.json') != result['manifest_sha256'] or sha256(RUN/'fixed64.json') != result['fixed64_sha256']
            or sha256(PROPOSAL) != manifest['proposal_sha256'] or sha256(DATA/'train-source.jsonl') != manifest['source_text_sha256']):
        raise ValueError('Frozen preparation binding differs')
    selected = {r['id']: r for r in (json.loads(line) for line in (DATA/'train-source.jsonl').read_text().splitlines())}
    notes = []
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields = line.split('\t')
        if len(fields) != 4:
            raise ValueError('Four explicit observation fields required')
        name, weak, categories, rationale = fields
        if weak not in ('0', '1') or len(rationale.strip()) < 12:
            raise ValueError('Explicit weak flag and individual rationale required')
        categories = categories.split('|')
        if bool(int(weak)) != (categories != ['none']):
            raise ValueError('Weak/category flags differ')
        notes.append(dict(id=name, weak=bool(int(weak)), categories=categories, rationale=rationale))
    if len(notes) != 64 or len({n['id'] for n in notes}) != 64 or {n['id'] for n in notes} != {r['id'] for r in samples}:
        raise ValueError('All64 fixed raw source observations required')
    for row in samples:
        if selected.get(row['id']) != row or row['split'] != 'train' or int(row['family'][:8],16)%10 == 0:
            raise ValueError('Raw selected whole body or source family differs')
    weak = sum(n['weak'] for n in notes)
    categories = Counter(c for n in notes for c in n['categories'] if c != 'none')
    content_pass = weak <= 10
    review = dict(status='actual_fixed64_public_magpie_prose_review_complete', created_at=now(),
        preparation_result_sha256=sha256(RUN/'result.json'), manifest_sha256=result['manifest_sha256'],
        fixed64_sha256=result['fixed64_sha256'], observations_sha256=sha256(observations),
        notes=notes, weak=weak, maximum_weak=10, categories=dict(categories),
        unresolved_retained_grammar_errors=0, content_gate_passed=content_pass,
        volume_gate_passed=result['source_volume_target_reached'],
        accepted=content_pass and result['source_volume_target_reached'],
        source_serialized_tokens=manifest['serialized_tokens'], source_body_tokens=manifest['body_tokens'],
        source_full_CE_teachers=manifest['full_CE_teachers'], source_documents=manifest['documents'],
        reviewer='Codex nonblind; all64 individually read', independent_human_blind=False,
        scope='Fixed uniform-document sample only. Assess standalone text, grammar and internal coherence; no comprehensive external factual verification. Unflagged rows are not certified factual ground truth. No sampled weak row is used for student learning; overall rejected source stays quarantined.',
        CPU_preparation_seconds=result['CPU_seconds'], GPU_seconds=0, student_scientific_teacher_tokens=0,
        optimizer_updates=0, protected_test_used=False, Chat_started=False, quantization_started=False,
        Base_complete=False, Base_adopted=False, quality_criteria_unchanged=True)
    if output.exists():
        raise ValueError('Preserve completed source review')
    write_json(output, review)
    print(json.dumps({k:v for k,v in review.items() if k not in ('notes','scope')},ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python required')
    main()
