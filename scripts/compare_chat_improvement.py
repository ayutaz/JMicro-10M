"""CPU final-point paired comparison/selection; all saved points stay visible."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review,paired_chat_comparison
from chat_improvement_contract import RUN,preflight,reference
from review_chat_improvement import get_items


def reviewed(arm,point,suite):
    path=RUN/'evaluation'/arm/point/suite/'greedy/result.json'
    evaluation,items=get_items(path);notes=read_json(path.with_name('notes.json'))
    review=content_review(evaluation,sha256(path),notes,items)
    assert json.loads(json.dumps(review))==read_json(path.with_name('review.json'))
    return evaluation,items,review


def absolute_checks(ev,review):
    primary=ev['primary'];own=ev['own_history_all_turns'];content=review['summaries']
    return dict(joint56of80=content['primary']['joint_grammar_relevance_score2']>=56,
        own_context15of24=content['own_history_final24']['context_score2']>=15,
        primary_stop76of80=primary['stop']>=76,own_stop57of59=own['stop']>=57,
        primary_empty_at_most4=primary['empty']<=4,own_empty_at_most2=own['empty']<=2,
        primary_role0=primary['role_leak']==0,own_role0=own['role_leak']==0,
        primary_raw_unicode0=primary['unicode_failure']==0,own_raw_unicode0=own['unicode_failure']==0,
        primary_full_history=primary['trimmed_history']==0,own_full_history=own['trimmed_history']==0)


def main():
    p=argparse.ArgumentParser();p.add_argument('--point',choices=('t1','t3'),required=True);args=p.parse_args()
    c,_,_=preflight(ROOT/'configs/phase7/chat-improvement-20261012.json')
    arms={};paired={};summary={}
    for suite in ('new','old'):
        data={arm:reviewed(arm,args.point,suite) for arm in ('C0','C1')}
        comp=paired_chat_comparison(data['C0'][0],data['C1'][0],data['C0'][1],data['C1'][1],data['C0'][2],data['C1'][2])
        comp.update(difference_direction='C1 minus C0; positive failure difference is worse',
            summaries=dict(C0=data['C0'][2]['summaries'],C1=data['C1'][2]['summaries']),
            dev_screens=dict(C0=data['C0'][2]['dev_screen_passed'],C1=data['C1'][2]['dev_screen_passed']),
            status='exploratory_family_paired_comparison_no_adoption',pending=['conditional retention/sampling if final eligible','independent trained seed/human blind/fullDEV/protectedTEST'])
        paired[suite]=comp
        for arm,(ev,items,review) in data.items():
            checks=absolute_checks(ev,review)
            summary.setdefault(arm,{})[suite]=dict(content=review['summaries'],mechanical={k:ev[k] for k in ('primary','role_control','own_history_all_turns','own_history_final24')},
                absolute_checks=checks,absolute_passed=all(checks.values()))
    repeats={suite:all(summary['C1'][suite]['mechanical'][k]['repetition']<=summary['C0'][suite]['mechanical'][k]['repetition']
        for k in ('primary','own_history_all_turns')) for suite in ('new','old')}
    eligible={arm:all(summary[arm][suite]['absolute_passed'] for suite in ('new','old')) and (arm=='C0' or all(repeats.values())) for arm in ('C0','C1')}
    selected=None
    if args.point=='t3':
        candidates=[arm for arm in ('C0','C1') if eligible[arm]]
        if candidates:
            def rank(arm):
                s=summary[arm]['new'];return (s['content']['primary']['joint_grammar_relevance_score2'],
                    s['content']['own_history_final24']['context_score2'],-s['mechanical']['primary']['repetition'],
                    -s['mechanical']['own_history_all_turns']['repetition'],arm=='C0')
            selected=max(candidates,key=rank)
    output=dict(config_sha256=c['config_sha256'],source_sha256=sha256(Path(__file__)),point=args.point,summary=summary,paired=paired,
        eligibility=eligible,C1_repetition_not_increased_vs_C0=repeats,eligible_candidate=selected,
        both_suites_passed=selected is not None,selection='final-only: new joint, new final context, fewer repetitions, tie C0',
        independent_family_units='80 new and80 old separately; own24 subsets overlap provided80; repeated saved points are not extra families',
        exploratory_nonblind=True,independent_trained_seed=False,human_blind=False,protected_TEST_used=False,
        Base_adopted=False,Chat_adopted=False,completed_at=now())
    atomic_json(RUN/('selection.json' if args.point=='t3' else 'intermediate_screen.json'),output)
    print('Final eligible candidate: '+str(selected) if args.point=='t3' else 'Both-arm intermediate screen recorded without final selection')

if __name__=='__main__':main()
