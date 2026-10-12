"""Compare frozen evidence with explicit provenance for Codex phase labels.

The historical control's reviewer display name is plan131; new reviews use
plan133. Both are Codex nonblind, under the same exact rubric. This observer
preserves every original note, rating, fingerprint and frozen source. It does
not assert independent or blind agreement between the historical judgments.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import compare_chat_generalization as frozen
from jmicro.chat_review import RUBRIC, paired_chat_comparison
from jmicro.experiment import read_json, sha256, now
from jmicro.training import atomic_json

LABELS = {'Codex plan131 reviewer', 'Codex plan133 reviewer'}
PROTOCOL = dict(kind='codex_nonblind', independent_human=False, blind=False)


def canonical_review(review):
    reviewer = review['reviewer']
    assert set(reviewer) == set(PROTOCOL) | {'identity'}
    assert {k: reviewer[k] for k in PROTOCOL} == PROTOCOL
    assert reviewer['identity'] in LABELS, 'Unknown reviewer alias: do not normalize'
    assert review['rubric'] == RUBRIC
    return dict(review, reviewer=dict(PROTOCOL, identity='Codex'))


def main():
    observations = []

    def compare(*args):
        control, candidate = args[-2:]
        normalized = (canonical_review(control), canonical_review(candidate))
        result = paired_chat_comparison(*args[:-2], *normalized)
        labels = dict(control=control['reviewer'], candidate=candidate['reviewer'])
        observations.append(labels)
        result['reviewer_label_provenance'] = labels
        result['limitation_historical_review_not_repeated_or_blind'] = True
        return result

    frozen.paired_chat_comparison = compare
    frozen.main()
    point = sys.argv[sys.argv.index('--point') + 1]
    path = frozen.RUN / ('selection.json' if point == 't3' else 'intermediate_screen.json')
    result = read_json(path)
    refs = {}
    for arm in ('D0', 'D1'):
        for suite in ('new', 'old'):
            note = frozen.RUN / 'evaluation' / arm / point / suite / 'greedy' / 'notes.json'
            refs[f'{arm}-{suite}'] = dict(path=str(note), sha256=sha256(note))
    result['comparison_observer'] = dict(
        path=str(Path(__file__)), sha256=sha256(Path(__file__)), observed_at=now(),
        original_reviewer_labels=observations, original_notes=refs,
        matched_rubric_and_nonblind_protocol=True, scores_or_raw_changed=False,
        frozen_sources_changed=False,
        rationale='Explicit Codex phase display aliases only; original note provenance retained',
        limitation='Historical Codex judgments are not newly reviewed independent human or blind evidence')
    atomic_json(path, result)


if __name__ == '__main__':
    main()
