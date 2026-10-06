"""One bounded CPU analysis of already scored gold/foil likelihood changes; no model execution."""
import time
START=time.perf_counter()
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import math
import statistics
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_anchored_context_outcome_comparison as study


def ref(path):return dict(path=str(path),sha256=sha256(path))


def check():
    if time.perf_counter()-START>10:raise TimeoutError('Fixed10second cached-score CPU analysis ceiling exhausted')


def main():
    target=ROOT/'reports/phase6/anchored_context_outcome_absolute_likelihood.json'
    if target.exists():raise ValueError('Preserve completed direction analysis')
    current=read_json(study.RUN/'compare-result.json');old=read_json(study.MECHANISM_RUN/'compare-result.json')
    config=read_json(study.CONFIG);oldconfig=read_json(study.base_study.CONFIG)
    if config['implementation']!=oldconfig['implementation']:raise ValueError('Same likelihood implementation required')
    for run in (study.RUN,study.MECHANISM_RUN):
        job=read_json(run/'job.json')
        if job['status']!='complete' or alive(job):raise ValueError('Actual terminal scored runs required')
    rows=[];summaries={};raw_refs=[]
    for suite,key in (('bridge','transfer'),('retention','retention')):
        cases_key='source_cases' if suite=='bridge' else 'retention_cases'
        cases_ref=config['references'][cases_key]
        if cases_ref!=oldconfig['references'][cases_key]:raise ValueError('Exact same paired candidate targets required')
        study.check_reference(cases_ref);prepared=read_json(Path(cases_ref['path']))
        scored={}
        for name,run,arm,result,cfg in (('context_ranking_control',study.MECHANISM_RUN,study.MECHANISM_ARM,old,study.base_study.CONFIG),
                                      ('positive_anchor',study.RUN,study.ARM,current,study.CONFIG)):
            terminal=result[key][arm];cp=result['checkpoints'][arm]
            if terminal['checkpoint_sha256']!=cp['checkpoint_sha256'] or not all(terminal['checks'].values()):
                raise ValueError('Read-only checkpoint-bound scores required')
            scored[name]=[]
            for start in range(0,512,16):
                check();path=run/'transfer'/suite/arm/f'{start:04d}.json';batch=read_json(path)
                if (batch['config_sha256']!=sha256(cfg) or batch['checkpoint_sha256']!=cp['checkpoint_sha256']
                        or batch['cases_sha256']!=cases_ref['sha256']):raise ValueError('Cached batch binding differs')
                study.ranking.validate_scores(batch['rows'],prepared['cases'][start:start+16])
                raw_refs.append(ref(path));scored[name].extend(batch['rows'])
            if terminal['summary']!=study.summarize_transfer(scored[name],prepared):raise ValueError('Whole suite score aggregation differs')
            scored[name]={v['index']:v for v in scored[name]}
        by_family={}
        for case in prepared['cases']:
            if case['label']!=case['branch']:raise ValueError('Fixed opposed labels required')
            by_family.setdefault(case['family'],{})[case['branch'],case['candidate']]=case
        for family in prepared['families']:
            group=by_family[family['index']]
            if set(group)!={(b,k) for b in (0,1) for k in (0,1)}:raise ValueError('Whole opposed family required')
            for branch in (0,1):
                gold,foil=group[branch,branch],group[branch,1-branch]
                values={}
                for name,indexed in scored.items():
                    g,f=indexed[gold['index']],indexed[foil['index']]
                    if (g['target_ids']!=gold['target_ids'] or f['target_ids']!=foil['target_ids']
                            or not math.isclose(-sum(g['token_nll']),g['log_likelihood'],abs_tol=1e-9)
                            or not math.isclose(-sum(f['token_nll']),f['log_likelihood'],abs_tol=1e-9)):
                        raise ValueError('Exact complete token-NLL decomposition required')
                    values[name]=dict(gold_NLL=-g['log_likelihood'],foil_NLL=-f['log_likelihood'],
                        gold_mean_token_NLL=-g['log_likelihood']/g['target_tokens'],
                        foil_mean_token_NLL=-f['log_likelihood']/f['target_tokens'],
                        gold_first_token_NLL=g['token_nll'][0],foil_first_token_NLL=f['token_nll'][0],
                        correct_margin=g['log_likelihood']-f['log_likelihood'])
                a,b=values['context_ranking_control'],values['positive_anchor']
                delta_g=b['gold_NLL']-a['gold_NLL'];delta_f=b['foil_NLL']-a['foil_NLL']
                margin=b['correct_margin']-a['correct_margin']
                if not math.isclose(margin,delta_f-delta_g,abs_tol=1e-9):raise ValueError('Margin direction identity differs')
                rows.append(dict(suite=suite,family=family['id'],split=family['split'],category=family['category'],branch=branch,
                    gold_tokens=len(gold['target_ids']),foil_tokens=len(foil['target_ids']),
                    gold_bytes=gold['target_bytes'],foil_bytes=foil['target_bytes'],values=values,
                    gold_NLL_change=delta_g,foil_NLL_change=delta_f,correct_margin_change=margin,
                    gold_likelihood_worse=delta_g>1e-9,foil_likelihood_worse=delta_f>1e-9,
                    margin_improved=margin>1e-9,
                    both_likelihoods_worse_but_margin_improved=delta_g>1e-9 and delta_f>1e-9 and margin>1e-9))
        summaries[suite]={}
        for split in ('all128','lexical_holdout','structural_holdout'):
            selected=[v for v in rows if v['suite']==suite and (split=='all128' or v['split']==split)]
            if len(selected)!=(256 if split=='all128' else 128):raise ValueError('Fixed paired branch coverage required')
            total_g=sum(v['gold_tokens'] for v in selected);total_f=sum(v['foil_tokens'] for v in selected)
            if total_g!=total_f or sum(v['gold_bytes'] for v in selected)!=sum(v['foil_bytes'] for v in selected):
                raise ValueError('Complete two-pole gold and foil target budgets differ')
            numbers=dict(families=len(selected)//2,correlated_context_poles=len(selected),gold_and_foil_tokens_each=total_g,
                gold_likelihood_worse=sum(v['gold_likelihood_worse'] for v in selected),
                gold_likelihood_better=sum(v['gold_NLL_change']<-1e-9 for v in selected),
                foil_likelihood_worse=sum(v['foil_likelihood_worse'] for v in selected),
                margin_improved=sum(v['margin_improved'] for v in selected),
                both_likelihoods_worse_but_margin_improved=sum(v['both_likelihoods_worse_but_margin_improved'] for v in selected))
            for name in scored:
                numbers[name]=dict(gold_mean_token_NLL=sum(v['values'][name]['gold_NLL'] for v in selected)/total_g,
                    foil_mean_token_NLL=sum(v['values'][name]['foil_NLL'] for v in selected)/total_f,
                    mean_gold_first_token_NLL=statistics.mean(v['values'][name]['gold_first_token_NLL'] for v in selected),
                    mean_foil_first_token_NLL=statistics.mean(v['values'][name]['foil_first_token_NLL'] for v in selected))
            summaries[suite][split]=numbers
    check()
    report=dict(status='actual_cached_BF16_gold_foil_direction_analysis_complete',created_at=now(),
        question='Does the added positive likelihood term improve absolute gold likelihood versus completed ranking, and is that accompanied by useful generated text?' ,
        fixed_comparison='Terminal ranking versus terminal ranking plus one conditional-nonEOS positive CE anchor; all256 fixed families/two context poles, no selection or new scoring.',
        CPU_ceiling_seconds=10,CPU_elapsed_seconds=time.perf_counter()-START,GPU_seconds=0,
        optimizer_updates=0,newly_prepared_corpus_tokens=0,forward_requests=0,raw_requests_reused=2048,
        terminal_result_refs=[ref(study.MECHANISM_RUN/'compare-result.json'),ref(study.RUN/'compare-result.json')],
        implementation_sha256=sha256(Path(__file__)),precision='Both previously saved CUDA BF16/math NativeLikelihood runs. No CPU FP32 score subtraction or new inference.',
        summaries=summaries,rows=rows,raw_score_refs=raw_refs,
        limits=['Whole-candidate likelihood and first gold token NLL are teacher-forced diagnostics; not top1 ranks or independent generated-context success.',
                'Correlated context poles and shared-generator local probes are not independent natural-language samples.',
                'Margin changes are the foil NLL change minus gold NLL change; this arithmetic does not establish the unique causal training mechanism.',
                'The selected candidate can remain relatively preferred even while its absolute probability decreases; adoption/generation metrics are unchanged.'],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        quality_criteria_unchanged=True)
    atomic_json(target,report)
    print({k:v['all128'] for k,v in summaries.items()},flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
