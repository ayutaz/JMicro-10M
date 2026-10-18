"""All1973 literal judgments, fixed gates and descriptive historical regressions."""
import csv
import json
from two_attribute_contract import ROOT,RUN,CONFIG,preflight
from answer_learning_common import save,ref,read_json,bound,now
from jmicro.chat_evaluation import summarize_chat
from jmicro.japanese_evaluation import clustered_ci
from review_two_attribute_regression import wire,OLD_CONFIG,OLD_RUN,public_validate
import review_chat_natural as review

def evidence(config,run,arm,suite):
    wire(config,run);path=run/'evaluation'/arm/suite/'result.json';raw,view,items=review.get_items(path)
    notes=read_json(path.with_name('notes.json'));content=review.content_review(view,ref(path)['sha256'],notes,items)
    assert content==read_json(path.with_name('review.json'));return raw,items,content

def score_diagnosis(rows):
    rs=[r['response'] for r in rows];ns=[r['judgment'] for r in rows]
    return dict(n=len(rows),grammar=sum(n['grammar']==2 for n in ns),relevance=sum(n['relevance']==2 for n in ns),
        context=sum(n['context']==2 for n in ns),content=sum(n['grammar']==n['relevance']==2 for n in ns),
        all3=sum(all(n[k]==2 for k in ('grammar','relevance','context')) for n in ns),
        values=sum(n['factual_correct'] is True for n in ns),mechanical=summarize_chat(rs))

def main():
    c,_,_=preflight();target=RUN/'final_analysis.json';assert not target.exists()
    d=read_json(RUN/'diagnosis/notes.json');assert d['config']==ref(CONFIG) and len(d['judgments'])==240
    diagnosis={}
    for point,group in (('before','TRAIN'),('after','TRAIN'),('after','unseen_values'),('after','unseen_structure'),('after','own')):
        selected=[r for r in d['judgments'] if r['point']==point and r['group']==group];diagnosis[point+'_'+group]=score_diagnosis(selected)
    own=[r for r in d['judgments'] if r['group']=='own' and r['final']];diagnosis['own_final16']=score_diagnosis(own)
    breakdown={}
    for group in ('TRAIN','unseen_values','unseen_structure'):
        for name,field,value in [('single','two',False),('two','two',True),('memory','correction',False),('correction','correction',True)]:
            selected=[r for r in d['judgments'] if r['point']=='after' and r['group']==group and r['case'][field]==value]
            breakdown[group+'_'+name]=score_diagnosis(selected)
    trained=diagnosis['after_TRAIN'];mechanics=trained['mechanical']
    learning=trained['values']==64 and mechanics['stop']==64 and all(mechanics[k]==0 for k in ('unicode_failure','role_leak','trimmed_history'))
    transfer=diagnosis['after_unseen_values']['content']>=24 and diagnosis['after_unseen_structure']['content']>=24 and diagnosis['own_final16']['context']>=12
    branch='prepare_new_matched_main_SFT' if learning and transfer else 'investigate_transfer_before_main_SFT' if learning else 'investigate_TRAIN_fit_before_main_SFT'
    regressions={};summaries={};exports=[];manual=0;reused=0
    for suite in c['suites']:
        candidate=evidence(CONFIG,RUN,'D',suite);ns={n['key']:n for n in candidate[2]['judgments']};rs=candidate[0]
        summaries[suite]=dict(candidate=candidate[2]['summaries'],mechanical=dict(primary=rs['primary'],own=rs['own_history']),baselines={})
        packet=read_json(RUN/'evaluation/D'/suite/'packet.json');manual+=len(packet['pending']);reused+=len(packet['reused'])
        comparisons={}
        for arm in ('C0','C1'):
            baseline=evidence(OLD_CONFIG,OLD_RUN,arm,suite);bn={n['key']:n for n in baseline[2]['judgments']}
            summaries[suite]['baselines'][arm]=dict(content=baseline[2]['summaries'],mechanical=dict(primary=baseline[0]['primary'],own=baseline[0]['own_history']))
            comparisons[arm]={}
            for condition in ('primary','own_final24'):
                keys=[k for k,v in candidate[1].items() if (v['condition']=='suppressed' if condition=='primary' else v['condition']=='own-history' and v['final_turn'])]
                deltas=[]
                for key in keys:
                    left,right=baseline[1][key],candidate[1][key]
                    assert all(left[k]==right[k] for k in ('id','family_id','category','checks','condition'))
                    if condition=='primary':assert left['messages']==right['messages']
                    b=bn[key];n=ns[key]
                    bv=(b['grammar']==b['relevance']==2) if condition=='primary' else b['context']==2
                    nv=(n['grammar']==n['relevance']==2) if condition=='primary' else n['context']==2
                    deltas.append(dict(id=right['id'],family=right['family_id'],difference=int(nv)-int(bv)))
                comparisons[arm][condition]=clustered_ci(deltas,key='difference')
        regressions[suite]=comparisons
        for key,item in candidate[1].items():exports.append(dict(section='regression_'+suite,id=key,messages=item['messages'],expected=item['checks'],response=item['response'],judgment=ns[key]))
    path,public,_=public_validate('D');pubnotes=read_json(path.with_name('notes.json'));pubsummary=read_json(path.with_name('summary.json'))
    assert pubnotes['raw']==ref(path) and pubsummary['notes']==ref(path.with_name('notes.json'))
    pp=read_json(path.with_name('packet.json'));manual+=len(pp['pending']);reused+=len(pp['reused'])
    for row,n in zip(public['responses'],pubnotes['judgments'],strict=True):exports.append(dict(section='public100',id=f'{row["id"]}:{row["turn"]}',messages=row['messages'],expected=row['expected'],response=row['response'],judgment=n))
    assert len(exports)==1733 and manual+reused==1733
    for row in d['judgments']:exports.append(dict(section=row['point']+'_'+row['group'],id=f'{row["id"]}:{row.get("turn",0)}',messages=row['messages'],expected=row['expected'],response=row['response'],judgment=row['judgment']))
    assert len(exports)==1973
    csvpath=RUN/'all1973_responses.csv'
    with csvpath.open('x',encoding='utf-8-sig',newline='') as stream:
        fields=['section','id','messages','expected','text','stop','UTF8','grammar','relevance','context','factual_correct','reason'];writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
        for row in exports:
            response=row['response'];n=row['judgment']
            writer.writerow(dict(section=row['section'],id=row['id'],messages=json.dumps(row['messages'],ensure_ascii=False),expected=json.dumps(row['expected'],ensure_ascii=False),text=response['text'],
                stop=response['stop_reason'],UTF8=response['valid_utf8'],grammar=n['grammar'],relevance=n['relevance'],context=n['context'],factual_correct=n.get('factual_correct'),reason=n['rationale']))
    public_baselines={arm:read_json(OLD_RUN/'public100'/arm/'summary.json') for arm in ('C0','C1')}
    formal={suite:dict(content56=v['candidate']['primary']['joint_grammar_relevance_score2']>=56,
        own_context15=v['candidate']['own_history_final24']['context_score2']>=15,
        stop76=v['mechanical']['primary']['stop']>=76,own_stop57=v['mechanical']['own']['stop']>=57,
        empty4=v['mechanical']['primary']['empty']<=4,own_empty2=v['mechanical']['own']['empty']<=2,
        role0=v['mechanical']['primary']['role_leak']==v['mechanical']['own']['role_leak']==0,
        UTF8_0=v['mechanical']['primary']['unicode_failure']==v['mechanical']['own']['unicode_failure']==0,
        trim0=v['mechanical']['primary']['trimmed_history']==v['mechanical']['own']['trimmed_history']==0) for suite,v in summaries.items()}
    save(target,dict(created_at=now(),source=ref(__file__),config=ref(CONFIG),diagnosis=diagnosis,breakdown=breakdown,
        learning_gate=learning,transfer_gate=transfer,branch=branch,regression=summaries,historical_paired_differences=regressions,
        historical_comparison_is_not_new_matched_ablation=True,
        historical_comparison_limitations='Current small64 curriculum/250003 teachers versus prior mixed curriculum/1000000 teachers. Data composition and teacher budget both differ; descriptive regression, not isolated answer-style effect.',
        public100=dict(candidate=pubsummary,baselines=public_baselines),formal_absolute_screens=formal,
        all1973_actual_histories_IDs_bytes_reviewed=True,judgments=1973,new_literal_reviews=240+manual,exact_raw_history_reused=reused,export=ref(csvpath),
        reviewer='Codex nonblind, not independent human',Chat_adopted=False,Base_adopted=False,new_TEST=False))
    print(json.dumps(dict(diagnosis=diagnosis,branch=branch,manual=240+manual,reused=reused),ensure_ascii=False))

if __name__=='__main__':main()
