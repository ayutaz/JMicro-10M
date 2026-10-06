"""Raw-bound fixed64 review, unchanged weak/grammar acceptance criteria."""
from datetime import datetime, timezone
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
from condition_query_balance import DATA, QueryBalancedTrainView
from prepare_condition_query_balance import RUN, sha, read, write


def main():
    m = read(DATA / 'manifest.json'); pilot = read(DATA / 'content-pilot.json')
    job = read(RUN / 'job.json'); path = DATA / 'content-notes.json'; notes = read(path)
    stat = Path(f"/proc/{job['pid']}/stat")
    if (job['status'] != 'complete_pending_fixed64_content' or job['manifest_sha256'] != sha(DATA / 'manifest.json')
            or (stat.exists() and stat.read_text().split()[21] == str(job['start_ticks']))
            or sha(DATA / 'content-pilot.json') != m['pilot_sha256'] or notes['pilot_sha256'] != m['pilot_sha256']
            or not notes['all64_individually_read'] or not notes['reviewer'] or not notes['nonblind']):
        raise ValueError('Terminal source job and all64 raw-bound reading required')
    by_id = {r['id']: r for r in pilot['rows']}; observed = notes['notes']
    if len(by_id) != 64 or len(observed) != 64 or len({n['id'] for n in observed}) != 64 or {n['id'] for n in observed} != set(by_id):
        raise ValueError('Complete unique64 notes required')
    for n in observed:
        if (n['text_sha256'] != by_id[n['id']]['text_sha256'] or len(n['observation'].strip()) < 12
                or type(n['weak']) is not bool or type(n['unresolved_grammar']) is not bool
                or type(n['pair_state_consistent']) is not bool):
            raise ValueError('Each raw text, grammar, weakness and grounded state observation required')
    weak = sum(n['weak'] for n in observed); errors = sum(n['unresolved_grammar'] for n in observed)
    consistent = all(n['pair_state_consistent'] for n in observed)
    review = dict(created_at=datetime.now(timezone.utc).isoformat(), all64_read=True, weak_documents=weak,
        unresolved_grammar_documents=errors, paired_states_consistent=consistent,
        training_pool_accepted=weak <= 10 and errors == 0 and consistent,
        manifest_sha256=sha(DATA / 'manifest.json'), pilot_sha256=m['pilot_sha256'], notes_sha256=sha(path),
        reviewer=notes['reviewer'], independent_human=False, nonblind=True, Base_adopted=False,
        scientific_teacher_tokens=0, GPU_seconds=0, protected_test_used=False, quality_criteria_unchanged=True)
    write(DATA / 'content-review.json', review); write(RUN / 'content-review.json', review)
    if review['training_pool_accepted']:
        QueryBalancedTrainView(DATA, sha(DATA / 'manifest.json'))
    write(ROOT / 'reports/phase6/condition_query_balance_content_review.json', review)
    print(review)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
