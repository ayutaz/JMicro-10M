"""Frozen rubric, all2628 literal reviews and paired family CI; no posthoc rescue."""
from pathlib import Path
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
from answer_learning_common import save,ref,bound,read_json,now
from review_answer_curriculum import wire
import analyze_chat_natural as original
import review_chat_natural as review
from jmicro.chat_review import paired_chat_comparison


def main():
    target=RUN/'final_analysis.json';assert not target.exists()
    c=read_json(CONFIG);wire()
    original.RUN=RUN;original.CONFIG=CONFIG;original.SUITES=contract.SUITES;original.require_ref=bound;original.ref=ref
    summaries={};comparisons={};count=0
    for arm in ('C0','C1'):
        audit=read_json(RUN/arm/'training_audit.json');assert audit['passed'] and audit['config']==ref(CONFIG);bound(audit['checkpoint'])
    for suite in contract.SUITES:
        left=original.evidence('C0',suite,c);right=original.evidence('C1',suite,c)
        paired=paired_chat_comparison(left[0],right[0],left[1],right[1],left[2],right[2])
        summaries[suite]=dict(C0=left[3],C1=right[3]);comparisons[suite]=dict(paired=paired['paired'],statistical_note=paired['statistical_note'],
            difference_direction='New C1 answer curriculum minus new matched C0, both LR1e-4')
        count+=len(left[2]['judgments'])+len(right[2]['judgments'])
    assert count==2628
    regressions={}
    for suite,entry in summaries.items():
        a,b=entry['C0'],entry['C1'];regressions[suite]=dict(content=b['primary']['joint_grammar_relevance_score2']<a['primary']['joint_grammar_relevance_score2'],
            own_context=b['own_final24']['context_score2']<a['own_final24']['context_score2'],
            primary_stops=b['mechanical']['primary']['stop']<a['mechanical']['primary']['stop'],
            own_stops=b['mechanical']['own']['stop']<a['mechanical']['own']['stop'])
        for metric in ('repetition','empty','role_leak','unicode_failure'):
            regressions[suite][metric]=any(b['mechanical'][mode][metric]>a['mechanical'][mode][metric] for mode in ('primary','own'))
    positive=comparisons['new']['paired']['primary']['joint_grammar_relevance']['ci95'][0]>0
    no_regression=not any(any(v.values()) for v in regressions.values())
    nll={}
    for arm,points in (('parent',['t0']),('C0',['250000','500000','1000000']),('C1',['250000','500000','1000000'])):
        nll[arm]={}
        for point in points:
            path=RUN/'NLL'/arm/f'{point}.json';value=read_json(path)
            assert value['status']=='complete' and value['binding']['config_sha256']==ref(CONFIG)['sha256'] and len(value['targets'])==320
            nll[arm][point]=dict(source=ref(path),summaries=value['summaries'])
    save(target,dict(status='all2628_content_reviews_and_matched_comparison_complete',created_at=now(),config=ref(CONFIG),
        judgments=count,summaries=summaries,comparisons=comparisons,regressions=regressions,NLL=nll,
        new_content_CI_positive=positive,no_count_regression_across_six_suites=no_regression,
        candidate_improvement_demonstrated=positive and no_regression,
        candidate_all_absolute_DEV_screens_pass=all(v['C1']['formal_absolute_pass'] for v in summaries.values()),
        formal_quality_gates=c['quality_gates'],primary_point=1000000,reviewer='Codex nonblind, no independent human',
        resource_plan_changed_before_science=ref(contract.ROOT/'docs/154_curriculum_resource_replan.md'),
        source=ref(__file__),Chat_adopted=False,Base_adopted=False,protected_TEST_used=False,
        UI_and_conditional_seed43_still_required=True))
    print('All2628 comparison complete; promised improvement='+str(positive and no_regression))


if __name__=='__main__':main()
