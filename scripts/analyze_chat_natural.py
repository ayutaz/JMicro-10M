"""Final matched comparison, using all2190 authored raw-bound judgments."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.chat_review import content_review,paired_chat_comparison
from jmicro.experiment import read_json,sha256,now
from jmicro.training import atomic_json
from chat_natural_contract import RUN,CONFIG,SUITES,GATES,ref,require_ref
from review_chat_natural import get_items


def evidence(arm,suite,c):
    path=RUN/'evaluation'/arm/suite/'result.json'
    raw,view,items=get_items(path)
    notes=read_json(path.with_name('notes.json'))
    review=content_review(view,sha256(path),notes,items)
    assert json.loads(json.dumps(review))==read_json(path.with_name('review.json'))
    # Derived common protocol fields come from validated raw/config references,
    # not edited historical outputs. Keep the actual32-token generation policy.
    binding=dict(view['binding'],tokenizer_sha256=c['tokenizer']['sha256'],suite_sha256=c['suites'][suite]['sha256'],
        model_context=1024,evaluation_seed=42,source_sha256=c['source_sha256'],implementation=c['implementation'],
        scored_split='dev',protected_test_used=False,protocol='provided80 suppressed + unsuppressed80 +59 own-history;32 tokens')
    view=dict(view,binding=binding)
    formal=dict(content56=review['summaries']['primary']['joint_grammar_relevance_score2']>=56,
        own_context15=review['summaries']['own_history_final24']['context_score2']>=15,
        primary_stop76=raw['primary']['stop']>=76,own_stop57=raw['own_history']['stop']>=57,
        primary_empty4=raw['primary']['empty']<=4,own_empty2=raw['own_history']['empty']<=2,
        role_leak0=raw['primary']['role_leak']==raw['own_history']['role_leak']==0,
        unicode0=raw['primary']['unicode_failure']==raw['own_history']['unicode_failure']==0,
        trim0=raw['primary']['trimmed_history']==raw['own_history']['trimmed_history']==0)
    summary=dict(raw=ref(path),notes=ref(path.with_name('notes.json')),review=ref(path.with_name('review.json')),
        primary=review['summaries']['primary'],own_final24=review['summaries']['own_history_final24'],
        mechanical=dict(primary=raw['primary'],unsuppressed=raw['unsuppressed'],own=raw['own_history']),
        formal_screen=formal,formal_absolute_pass=all(formal.values()))
    return view,items,review,summary


def main():
    target=RUN/'final_analysis.json'
    assert not target.exists(),'Do not overwrite completed comparison'
    c=read_json(CONFIG)
    summaries={};comparisons={};raw_judgments=0
    for arm in ('C0','C1'):
        audit=read_json(RUN/arm/'training_audit.json')
        assert audit['passed'] and audit['config']['sha256']==sha256(CONFIG)
        require_ref(audit['checkpoint'])
    for suite in SUITES:
        left=evidence('C0',suite,c);right=evidence('C1',suite,c)
        paired=paired_chat_comparison(left[0],right[0],left[1],right[1],left[2],right[2])
        summaries[suite]=dict(C0=left[3],C1=right[3])
        comparisons[suite]=dict(paired=paired['paired'],difference_direction='C1 broader conversation recipe minus C0 matched pilot recipe',
            statistical_note=paired['statistical_note'])
        raw_judgments+=len(left[2]['judgments'])+len(right[2]['judgments'])
        print(json.dumps(dict(suite=suite,C0_content=left[3]['primary']['joint_grammar_relevance_score2'],
            C1_content=right[3]['primary']['joint_grammar_relevance_score2'],
            C0_own_context=left[3]['own_final24']['context_score2'],C1_own_context=right[3]['own_final24']['context_score2'],
            content_delta=paired['paired']['primary']['joint_grammar_relevance']),ensure_ascii=False),flush=True)
    assert raw_judgments==2190
    regressions={}
    for suite,entry in summaries.items():
        left,right=entry['C0'],entry['C1']
        regressions[suite]=dict(
            content=right['primary']['joint_grammar_relevance_score2']<left['primary']['joint_grammar_relevance_score2'],
            own_context=right['own_final24']['context_score2']<left['own_final24']['context_score2'],
            primary_stops=right['mechanical']['primary']['stop']<left['mechanical']['primary']['stop'],
            own_stops=right['mechanical']['own']['stop']<left['mechanical']['own']['stop'],
            repetition=any(right['mechanical'][m]['repetition']>left['mechanical'][m]['repetition'] for m in ('primary','own')),
            empty=any(right['mechanical'][m]['empty']>left['mechanical'][m]['empty'] for m in ('primary','own')),
            role_leak=any(right['mechanical'][m]['role_leak']>left['mechanical'][m]['role_leak'] for m in ('primary','own')),
            unicode=any(right['mechanical'][m]['unicode_failure']>left['mechanical'][m]['unicode_failure'] for m in ('primary','own')))
    ci_positive=comparisons['new']['paired']['primary']['joint_grammar_relevance']['ci95'][0]>0
    no_known_regression=not any(any(row.values()) for row in regressions.values())
    absolute=all(entry['C1']['formal_absolute_pass'] for entry in summaries.values())
    nll={}
    for arm,points in (('parent',('t0',)),('C0',('250000','500000','1000000')),('C1',('250000','500000','1000000'))):
        nll[arm]={}
        for point in points:
            path=RUN/'NLL'/arm/f'{point}.json';row=read_json(path)
            assert row['status']=='complete' and row['binding']['config_sha256']==sha256(CONFIG) and len(row['targets'])==208
            nll[arm][point]=dict(source=ref(path),summaries=row['summaries'])
    result=dict(status='all2190_content_reviews_and_matched_comparison_complete',created_at=now(),config=ref(CONFIG),
        judgments=raw_judgments,summaries=summaries,comparisons=comparisons,regressions=regressions,NLL=nll,
        new_content_CI_positive=ci_positive,no_count_regression_across_five_suites=no_known_regression,
        candidate_improvement_demonstrated=ci_positive and no_known_regression,
        candidate_all_absolute_DEV_screens_pass=absolute,formal_quality_gates=GATES,
        primary_point=1000000,previous64_token_results_unchanged=True,
        reviewer='Codex nonblind, same evaluator and authored DEV; no independent human or blind TEST',
        qualification='This local matched SFT trial does not certify Base retention, fresh full-pipeline independence or final adoption',
        diagnostic_points_not_used_to_replace_primary=True,Chat_adopted=False,Base_adopted=False,
        protected_TEST_used=False,source=ref(Path(__file__)))
    atomic_json(target,result)


if __name__=='__main__':main()
