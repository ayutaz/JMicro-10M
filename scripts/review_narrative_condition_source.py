"""Raw-bound all64 content decision, without source correction or selection."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from narrative_condition_source import DATA, NarrativeTrainView
from prepare_narrative_condition_source import RUN


def validate_notes(pilot, raw, pilot_sha256):
    notes = raw['notes']; rows = {r['id']: r for r in pilot['rows']}
    if (raw['pilot_sha256'] != pilot_sha256 or not raw['all64_individually_read'] or len(notes) != 64
            or len({n['id'] for n in notes}) != 64 or {n['id'] for n in notes} != set(rows)):
        raise ValueError('Every fixed64 text individually read and raw-bound required')
    for note in notes:
        row = rows[note['id']]
        if (note['text_sha256'] != row['text_sha256'] or type(note['paired_condition_outcome']) is not int
                or note['paired_condition_outcome'] not in (0, 1, 2) or type(note['weak_document']) is not bool
                or note['weak_document'] != (note['paired_condition_outcome'] != 2)
                or type(note['unresolved_grammar_issue']) is not bool or type(note['unresolved_grounding_issue']) is not bool
                or len(note['reason']) < 12):
            raise ValueError('Exact raw content/rubric/individual reason required')
    return dict(weak_documents=sum(n['weak_document'] for n in notes),
                unresolved_grammar_documents=sum(n['unresolved_grammar_issue'] for n in notes),
                unresolved_grounding_documents=sum(n['unresolved_grounding_issue'] for n in notes))


def main():
    if (DATA / 'content-review.json').exists(): raise ValueError('Preserve actual terminal content decision')
    job = read_json(RUN / 'job.json'); manifest = read_json(DATA / 'manifest.json'); pilot = read_json(DATA / 'content-pilot.json')
    notes_path = DATA / 'content-notes.json'; raw = read_json(notes_path)
    if (job['status'] != 'complete_pending_fixed64_content' or alive(job)
            or job['manifest_sha256'] != sha256(DATA / 'manifest.json')
            or manifest['pilot_sha256'] != sha256(DATA / 'content-pilot.json')):
        raise ValueError('Terminal source preparation/exact fixed64 required')
    counts = validate_notes(pilot, raw, manifest['pilot_sha256'])
    accepted = counts['weak_documents'] <= 10 and counts['unresolved_grammar_documents'] == counts['unresolved_grounding_documents'] == 0
    report = dict(status='all64_narrative_TRAIN_source_review_complete', created_at=now(), all64_read=True,
        **counts, maximum_weak_documents=10, training_pool_accepted=accepted,
        manifest_sha256=job['manifest_sha256'], pilot_sha256=manifest['pilot_sha256'], notes_sha256=sha256(notes_path),
        notes=raw['notes'], independent_human_blind=False, reviewer='Codex nonblind', external_fact_certification=False,
        rubric='Condition preserved and naturally progressing complete prose2; weak0/1. Grammar and grounding separate; weak<=10 and both unresolved0.',
        limitations='Fixed64 of local compositional fiction; no independent human or Base model quality proof. No post-pilot renderer/filter/reroll.',
        actual_GPU_seconds=0, scientific_teacher_tokens=0, protected_test_used=False,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False)
    atomic_json(DATA / 'content-review.json', report); atomic_json(RUN / 'content-review.json', report)
    atomic_json(ROOT / 'reports/phase6/narrative_condition_source_content_review.json', report)
    if accepted: NarrativeTrainView(DATA, job['manifest_sha256'])
    print(dict(**counts, training_pool_accepted=accepted))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
