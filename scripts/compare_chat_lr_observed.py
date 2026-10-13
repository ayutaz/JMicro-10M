"""Correct original paired-review API binding; same unchanged four-suite gates."""
import argparse
import copy
import json
from pathlib import Path
from chat_lr_contract import RUN, SUITES, preflight, reference
from compare_chat_lr import reviewed, absolute_checks
from jmicro.experiment import read_json, now
from jmicro.training import atomic_json
from jmicro.chat_review import paired_chat_comparison, RUBRIC


def calculate(point, c):
    summaries, paired, repetitions = {}, {}, {}
    for suite in SUITES:
        data = {arm: reviewed(arm, point, suite) for arm in ('S0', 'S1')}
        canonical = {}
        for arm, (evaluation, notes, review, items) in data.items():
            path = RUN / 'evaluation' / arm / point / suite / 'greedy/review.json'
            assert json.loads(json.dumps(review)) == read_json(path)
            assert review['reviewer']['kind'] == 'codex_nonblind' and not review['reviewer']['blind']
            assert not review['reviewer']['independent_human'] and review['rubric'] == RUBRIC
            canonical[arm] = copy.deepcopy(review)
            canonical[arm]['reviewer']['identity'] = 'Codex nonblind matched protocol'
            checks = absolute_checks(evaluation, review)
            summaries.setdefault(arm, {})[suite] = dict(content=review['summaries'],
                mechanical={key: evaluation[key] for key in ('primary', 'role_control', 'own_history_final24', 'own_history_all_turns')},
                absolute_checks=checks, absolute_passed=all(checks.values()))
        paired[suite] = paired_chat_comparison(data['S0'][0], data['S1'][0], data['S0'][3], data['S1'][3],
                                             canonical['S0'], canonical['S1'])
        paired[suite]['difference_direction'] = 'S1 LR3e-5 minus S0 historical LR1e-4; positive failure difference worse'
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
    result.update(completed_at=now(), source=reference(Path(__file__)),
                  frozen_comparison_source=reference(Path(__file__).with_name('compare_chat_lr.py')),
                  adapter_scope='Argument order and nonblind reviewer metadata only; original rubric/CI/gates unchanged')
    atomic_json(RUN / ('selection.json' if args.point == 't3' else args.point + '_comparison.json'), result)
    print({key: result[key] for key in ('point', 'absolute_eligibility', 'new_joint_CI_lower', 'eligible_candidate')})
