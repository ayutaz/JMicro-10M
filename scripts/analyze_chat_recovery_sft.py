"""Fixed primary-point comparison of all3466 main responses and432 NLL targets."""
import json
import numpy as np
from chat_recovery_contract import ROOT,RUN,CONFIG,SUITES
from answer_learning_common import save,ref,bound,read_json,now
from review_chat_recovery_sft import wire
from review_chat_recovery_public100 import validate as public_validate
import analyze_chat_natural as original
from jmicro.chat_review import paired_chat_comparison


def public_comparison():
    evidence={}
    for arm in ('C0','C1'):
        path,raw,_=public_validate(arm);notes=read_json(path.with_name('notes.json'));summary=read_json(path.with_name('summary.json'))
        assert notes['raw']==summary['raw']==ref(path) and summary['notes']==ref(path.with_name('notes.json'))
        assert len(notes['judgments'])==200 and all(n['raw_fingerprint'] for n in notes['judgments'])
        evidence[arm]=(raw,notes,summary)
    a,b=evidence['C0'][1]['judgments'],evidence['C1'][1]['judgments']
    assert [(n['id'],n['turn']) for n in a]==[(n['id'],n['turn']) for n in b]
    finals=[i for i,n in enumerate(a) if n['final']];assert len(finals)==100
    differences=np.asarray([int(b[i]['task_pass'])-int(a[i]['task_pass']) for i in finals])
    rng=np.random.default_rng(42);bootstrap=differences[rng.integers(0,100,size=(10000,100))].mean(1)
    return dict(summaries={arm:v[2] for arm,v in evidence.items()},
        final100_task_pass_difference=float(differences.mean()),paired_case_bootstrap_ci95=np.quantile(bootstrap,[.025,.975]).tolist(),
        bootstrap_seed=42,bootstrap_draws=10000,unit='case; final reply only',not_primary_DEV=True)


def main():
    target=RUN/'final_analysis.json';assert not target.exists();c=read_json(CONFIG);wire()
    original.RUN=RUN;original.CONFIG=CONFIG;original.SUITES=SUITES;original.require_ref=bound;original.ref=ref
    summaries={};comparisons={};count=0
    for arm in ('C0','C1'):
        audit=read_json(RUN/arm/'training_audit.json');assert audit['passed'] and audit['config']==ref(CONFIG);bound(audit['checkpoint'])
    for suite in SUITES:
        left=original.evidence('C0',suite,c);right=original.evidence('C1',suite,c)
        paired=paired_chat_comparison(left[0],right[0],left[1],right[1],left[2],right[2])
        summaries[suite]=dict(C0=left[3],C1=right[3]);comparisons[suite]=dict(paired=paired['paired'],statistical_note=paired['statistical_note'],
            difference_direction='New C1 varied input structures minus new C0 fixed inputs, same answers/order/teachers')
        count+=len(left[2]['judgments'])+len(right[2]['judgments'])
        print(json.dumps(dict(suite=suite,C0=left[3]['primary']['joint_grammar_relevance_score2'],C1=right[3]['primary']['joint_grammar_relevance_score2'],
            own_C0=left[3]['own_final24']['context_score2'],own_C1=right[3]['own_final24']['context_score2']),ensure_ascii=False),flush=True)
    assert count==3066;public=public_comparison();regressions={}
    for suite,entry in summaries.items():
        a,b=entry['C0'],entry['C1'];regressions[suite]=dict(content=b['primary']['joint_grammar_relevance_score2']<a['primary']['joint_grammar_relevance_score2'],
            own_context=b['own_final24']['context_score2']<a['own_final24']['context_score2'],
            primary_stops=b['mechanical']['primary']['stop']<a['mechanical']['primary']['stop'],
            own_stops=b['mechanical']['own']['stop']<a['mechanical']['own']['stop'])
        for metric in ('repetition','empty','role_leak','unicode_failure'):
            regressions[suite][metric]=any(b['mechanical'][mode][metric]>a['mechanical'][mode][metric] for mode in ('primary','own'))
    positive=comparisons['new']['paired']['primary']['joint_grammar_relevance']['ci95'][0]>0
    no_regression=not any(any(v.values()) for v in regressions.values());nll={}
    for arm,points in (('parent',['t0']),('C0',['250000','500000','1000000']),('C1',['250000','500000','1000000'])):
        nll[arm]={}
        for point in points:
            path=RUN/'NLL'/arm/f'{point}.json';value=read_json(path)
            assert value['status']=='complete' and value['binding']['config_sha256']==ref(CONFIG)['sha256'] and len(value['targets'])==432
            nll[arm][point]=dict(source=ref(path),summaries=value['summaries'])
    save(target,dict(status='all3466_content_reviews_and_matched_comparison_complete',created_at=now(),config=ref(CONFIG),
        judgments=3466,suite_judgments=count,public_judgments=400,summaries=summaries,comparisons=comparisons,regressions=regressions,NLL=nll,public100=public,
        NLL_label_semantics='Historical320 labels preserved by DEV preparation; transformed TRAIN32 and current DEV80 separate. Historical arm labels do not identify current arms.',
        new_content_CI_positive=positive,no_count_regression_across_seven_suites=no_regression,
        candidate_improvement_demonstrated=positive and no_regression,
        candidate_all_absolute_DEV_screens_pass=all(v['C1']['formal_absolute_pass'] for v in summaries.values()),
        formal_quality_gates=c['quality_gates'],primary_point=1000000,reviewer='Codex nonblind, no independent human',
        source=ref(__file__),Chat_adopted=False,Base_adopted=False,protected_TEST_used=False,
        UI_and_conditional_seed43_still_required=True))


if __name__=='__main__':main()
