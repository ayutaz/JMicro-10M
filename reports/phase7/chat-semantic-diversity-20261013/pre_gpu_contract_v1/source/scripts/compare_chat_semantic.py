"""All3suite final comparison with explicit nonblind label provenance."""
import argparse
import copy
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from jmicro.chat_review import content_review, paired_chat_comparison, RUBRIC
from chat_semantic_contract import RUN, SUITES, preflight, reference
from review_chat_semantic import get_items
from compare_chat_generalization import absolute_checks

LABELS = ('Codex plan131 reviewer', 'Codex plan133 reviewer', 'Codex plan135 reviewer')


def reviewed(arm, point, suite):
    path = RUN / 'evaluation' / arm / point / suite / 'greedy/result.json'
    evaluation, items = get_items(path)
    notes = read_json(path.with_name('notes.json'))
    review = content_review(evaluation, sha256(path), notes, items)
    assert json.loads(json.dumps(review)) == read_json(path.with_name('review.json'))
    reviewer = review['reviewer']
    assert reviewer == dict(kind='codex_nonblind', identity=reviewer['identity'], independent_human=False, blind=False)
    assert reviewer['identity'] in LABELS and review['rubric'] == RUBRIC
    canonical = copy.deepcopy(review)
    canonical['reviewer']['identity'] = 'Codex nonblind matched protocol'
    return evaluation, items, review, canonical


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--point', choices=('t1', 't2', 't3'), required=True)
    args = parser.parse_args()
    c, _, _ = preflight(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    summaries, paired, repeats, sources = {}, {}, {}, []
    for suite in SUITES:
        data = {arm: reviewed(arm, args.point, suite) for arm in ('S0', 'S1')}
        comp = paired_chat_comparison(data['S0'][0], data['S1'][0], data['S0'][1], data['S1'][1],
                                     data['S0'][3], data['S1'][3])
        comp['difference_direction'] = 'S1 minus latestD1 S0; positive failure difference is worse'
        paired[suite] = comp
        for arm, (evaluation, items, review, canonical) in data.items():
            checks = absolute_checks(evaluation, review)
            summaries.setdefault(arm, {})[suite] = dict(content=review['summaries'],
                                                         mechanical={key: evaluation[key] for key in
                                                                     ('primary', 'role_control', 'own_history_final24', 'own_history_all_turns')},
                                                         absolute_checks=checks, absolute_passed=all(checks.values()))
            sources.append(dict(arm=arm, suite=suite, reviewer=review['reviewer'],
                                notes=reference(RUN / 'evaluation' / arm / args.point / suite / 'greedy/notes.json')))
        repeats[suite] = all(summaries['S1'][suite]['mechanical'][key]['repetition'] <=
                             summaries['S0'][suite]['mechanical'][key]['repetition']
                             for key in ('primary', 'own_history_all_turns'))
    lower = paired['new']['paired']['primary']['joint_grammar_relevance']['ci95'][0]
    improvement = lower > 0
    absolute = {arm: all(summaries[arm][suite]['absolute_passed'] for suite in SUITES) for arm in ('S0', 'S1')}
    eligible = absolute['S1'] and all(repeats.values()) and improvement
    selected = 'S1' if args.point == 't3' and eligible else None
    result = dict(completed_at=now(), config_sha256=c['config_sha256'], point=args.point,
                  summary=summaries, paired=paired, S1_repetition_not_increased_vs_S0=repeats,
                  absolute_eligibility=absolute, new_joint_CI_lower=lower,
                  prespecified_new_joint_improvement=improvement,
                  candidate_eligible=eligible, eligible_candidate=selected,
                  all_suites_passed=selected is not None,
                  selection='S1 only, finalt3, all3 original absolute gates, no repetition increase and new joint CI lower>0',
                  historical_reviewer_labels=sources, canonical_label_for_pairing_only=True,
                  original_notes_or_scores_modified=False, independent_human_blind=False,
                  independent_trained_seed=False, protected_TEST_used=False,
                  Base_adopted=False, Chat_adopted=False, quality_complete=False)
    atomic_json(RUN / ('selection.json' if args.point == 't3' else f'{args.point}_comparison.json'), result)
    print(json.dumps(dict(point=args.point, absolute=absolute, improvement=improvement, final_candidate=selected)))


if __name__ == '__main__':
    main()
