"""Four original absolute screens and prespecified unseen family paired CI."""
import argparse
from chat_lr_contract import RUN, SUITES, preflight, reference
from jmicro.experiment import read_json, now, sha256
from jmicro.training import atomic_json
from jmicro.chat_review import content_review, paired_chat_comparison
from review_chat_lr import get_items
from compare_chat_semantic import absolute_checks


def reviewed(arm, point, suite):
    path = RUN / 'evaluation' / arm / point / suite / 'greedy/result.json'
    evaluation, items = get_items(path)
    notes = read_json(path.with_name('notes.json'))
    review = content_review(evaluation, sha256(path), notes, items)
    return evaluation, notes, review, items


def calculate(point, c):
    summaries, paired, repetitions = {}, {}, {}
    for suite in SUITES:
        data = {arm: reviewed(arm, point, suite) for arm in ('S0', 'S1')}
        paired[suite] = paired_chat_comparison(data['S0'][0], data['S1'][0], data['S0'][1], data['S1'][1],
                                             data['S0'][3], data['S1'][3])
        paired[suite]['difference_direction'] = 'S1 LR3e-5 minus S0 historical LR1e-4; positive failure difference worse'
        for arm, (evaluation, _, review, _) in data.items():
            checks = absolute_checks(evaluation, review)
            summaries.setdefault(arm, {})[suite] = dict(content=review['summaries'],
                mechanical={key: evaluation[key] for key in ('primary', 'role_control', 'own_history_final24', 'own_history_all_turns')},
                absolute_checks=checks, absolute_passed=all(checks.values()))
        repetitions[suite] = all(summaries['S1'][suite]['mechanical'][key]['repetition'] <=
                                 summaries['S0'][suite]['mechanical'][key]['repetition']
                                 for key in ('primary', 'own_history_all_turns'))
    absolute = {arm: all(summaries[arm][suite]['absolute_passed'] for suite in SUITES) for arm in ('S0', 'S1')}
    lower = paired['new']['paired']['primary']['joint_grammar_relevance']['ci95'][0]
    eligible = absolute['S1'] and all(repetitions.values()) and lower > 0 and point == 't3'
    return dict(config_sha256=c['config_sha256'], point=point, summary=summaries, paired=paired,
        absolute_eligibility=absolute, S1_repetition_not_increased_vs_S0=repetitions,
        new_joint_CI_lower=lower, prespecified_new_joint_improvement=lower > 0,
        candidate_eligible=eligible, eligible_candidate='S1' if eligible else None,
        all_suites_passed=eligible, Base_adopted=False, Chat_adopted=False, quality_complete=False,
        protected_TEST_used=False, original_Chat_TEST_preparation_exposure_recorded=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--point', choices=('t1', 't2', 't3'), default='t3')
    args = p.parse_args()
    c, _, _ = preflight()
    result = calculate(args.point, c)
    result['completed_at'] = now()
    result['source'] = reference(__file__)
    atomic_json(RUN / ('selection.json' if args.point == 't3' else args.point + '_comparison.json'), result)
    print({key: result[key] for key in ('point', 'absolute_eligibility', 'new_joint_CI_lower', 'eligible_candidate')})
