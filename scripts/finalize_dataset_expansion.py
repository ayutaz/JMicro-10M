"""Save plan58 judgment and descriptive categories from the completed primary review."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import read_json, write_json, sha256, now
from run_dataset_expansion import RUN

def main():
    assert sys.version_info[:3] == (3, 12, 7)
    review = read_json(RUN / 'review.json')
    assert review['status'] == 'passed' and all(review['checks'].values())
    # This execution follows the frozen ineligible branch; no full job is launched.
    assert not review['eligible_for_full']
    assert not (RUN / 'full/full-job.json').exists()
    categories = {}
    semantic_families = {}
    for arm, rows in review['scored_outputs'].items():
        categories[arm] = {}
        for category in sorted({r['category'] for r in rows}):
            selected = [r for r in rows if r['category'] == category]
            categories[arm][category] = dict(count=len(selected),
                coherence2=sum(r['coherence'] == 2 for r in selected),
                relevance2=sum(r['relevance'] == 2 for r in selected),
                appropriate_EOS=sum(r['completion'] for r in selected))
        semantic_rows = read_json(RUN / 'evaluation' / arm / 'evaluation/semantics.json')['rows']
        families = {}
        for r in semantic_rows:
            families.setdefault(r['family'], []).append(r['credit'])
        assert len(families) == 96 and all(len(v) == 2 for v in families.values())
        semantic_families[arm] = dict(total=96, both_contexts_correct=sum(all(c == 1 for c in v) for v in families.values()))
    write_json(RUN / 'categories.json', dict(categories=categories, semantic_families=semantic_families,
        review_sha256=sha256(RUN / 'review.json'), note='Descriptive categories only; not new acceptance gates.'))
    write_json(RUN / 'judgment.json', dict(candidate_adopted=False, quality_targets_achieved=False,
        primary_review_sha256=sha256(RUN / 'review.json'), judged_at=now(),
        branch='Primary ineligible; conditional full evaluation not launched',
        failed_quality_gates=[k for k, v in review['quality_comparison']['checks'].items() if not v],
        failed_practical_gates=[k for k, v in review['practical'].items() if not v],
        observed='JCQA +3.530pp with paired CI above zero; no demonstrated semantic/grammar gain; EOS34 to25 and diagnosed coherence15 to9.',
        interpretation=review['comparison_interpretation'],
        limitations=['Single training seed', 'Codex nonblind diagnosis, no independent human blind review',
            'Repeated dev use; no protected test evaluation', 'Main Web independent overlap audit incomplete',
            'Mixed synthetic source, length and EOS density; not amount-only causality'],
        next_proposal='Before further bulk expansion, inspect condition/reference failures and compare source quality/length/EOS-matched small train-only pools at a bounded equal budget. Proposal only; not launched.',
        scientific_tokens=2000027648, verification_tokens=262144, protected_test_used=False,
        stop_boundary='Finish report/completion/local commit/original10B UI and stop',
        finalizer_sha256=sha256(Path(__file__))))
    print(json.dumps(dict(categories=categories, semantic_families=semantic_families), ensure_ascii=False))

if __name__ == '__main__':
    main()
