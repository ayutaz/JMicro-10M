"""One bounded CPU diagnosis of existing BF16 scores; no model or new inference."""
import time
START=time.perf_counter()
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from decision_span_diagnostic import compare,aggregate

PROPOSAL=ROOT/'reports/phase6/decision_span_diagnostic_proposal.json'
TARGET=ROOT/'reports/phase6/decision_span_diagnostic_result.json'


def ref(path):return dict(path=str(path),sha256=sha256(path))


def check():
    if time.perf_counter()-START>10:raise TimeoutError('Fixed10second cached decision-span CPU ceiling exhausted')


def verify(reference):
    check()
    if sha256(Path(reference['path']))!=reference['sha256']:raise ValueError('Frozen diagnostic input differs: '+reference['path'])


def run():
    if TARGET.exists():raise ValueError('Preserve completed decision-span result')
    p=read_json(PROPOSAL)
    if (p['CPU_ceiling_seconds']!=10 or set(p['models'])!={'strong_staged_CE','relative_ranking','positive_anchor'}
            or p['GPU_seconds'] or p['forward_requests'] or p['optimizer_updates'] or p['protected_test_used']
            or not p['quality_criteria_unchanged']):raise ValueError('One fixed cached-only diagnostic required')
    for r in (*p['trigger'].values(),p['source_cases'],p['retention_cases'],p['scorer_implementation']):verify(r)
    rows=[];summaries={};raw_refs=[];requests=0;implementation=None
    for name,model in p['models'].items():
        run_path=Path(model['run']);job=read_json(run_path/'job.json')
        if job['status']!='complete' or alive(job):raise ValueError('Actually terminal cached model required')
        for key in ('config','result','checkpoint'):verify(model[key])
        c=read_json(Path(model['config']['path']));r=read_json(Path(model['result']['path']));arm=model['arm']
        if implementation is None:implementation=c['implementation']
        if c['implementation']!=implementation or r['config_sha256']!=model['config']['sha256']:
            raise ValueError('Matched native implementation/config required')
        cp=r['checkpoints'][arm]
        if (cp['checkpoint'],cp['checkpoint_sha256'])!=(model['checkpoint']['path'],model['checkpoint']['sha256']):
            raise ValueError('Actual terminal checkpoint identity differs')
        summaries[name]={}
        for suite,key,case_key in (('bridge','transfer','source_cases'),('retention','retention','retention_cases')):
            if c['references'][case_key]!=p[case_key]:raise ValueError('Same encoded candidate targets required')
            prepared=read_json(Path(p[case_key]['path']));terminal=r[key][arm];scored={}
            if (terminal['config_sha256']!=model['config']['sha256'] or terminal['checkpoint_sha256']!=model['checkpoint']['sha256']
                    or terminal['cases_sha256']!=p[case_key]['sha256'] or terminal['evaluated_requests']!=512
                    or terminal['optimizer_updates'] or terminal['scientific_teacher_tokens'] or terminal['protected_test_used']
                    or not all(terminal['checks'].values())):raise ValueError('Bound read-only full512 score requests required')
            for start in range(0,512,16):
                check();path=run_path/f'transfer/{suite}/{arm}/{start:04d}.json';batch=read_json(path)
                if any(batch[k]!=terminal[k] for k in ('config_sha256','checkpoint_sha256','cases_sha256')):
                    raise ValueError('Cached score batch identity differs')
                expected=prepared['cases'][start:start+16]
                if [v['index'] for v in batch['rows']]!=[v['index'] for v in expected]:raise ValueError('Whole fixed request order required')
                for v in batch['rows']:
                    if v['index'] in scored:raise ValueError('Duplicate score request')
                    scored[v['index']]=v
                raw_refs.append(ref(path));requests+=len(batch['rows'])
            families={}
            for case in prepared['cases']:
                if case['label']!=case['branch']:raise ValueError('Original opposed labels required')
                families.setdefault(case['family'],{})[case['branch'],case['candidate']]=case
            suite_rows=[]
            if len(prepared['families'])!=128 or len(scored)!=512:raise ValueError('All128 complete families required')
            for family in prepared['families']:
                group=families[family['index']]
                if set(group)!={(b,k) for b in (0,1) for k in (0,1)}:raise ValueError('All four candidate/context rows required')
                for branch in (0,1):
                    gold,foil=group[branch,branch],group[branch,1-branch]
                    v=dict(model=name,suite=suite,family=family['id'],split=family['split'],category=family['category'],branch=branch,
                        **compare(gold,foil,scored[gold['index']],scored[foil['index']]))
                    rows.append(v);suite_rows.append(v)
            sums={}
            for split in ('all128','lexical_holdout','structural_holdout'):
                selected=[v for v in suite_rows if split=='all128' or v['split']==split]
                if len(selected)!=(256 if split=='all128' else 128):raise ValueError('Fixed cohort coverage differs')
                sums[split]=aggregate(selected)
                for metric,values in sums[split]['full_candidate'].items():
                    if values!=terminal['summary']['aggregate'][metric][split]:raise ValueError('Existing full-candidate scorer aggregation differs')
            sums['categories']={cat:aggregate([v for v in suite_rows if v['category']==cat]) for cat in sorted({v['category'] for v in suite_rows})}
            summaries[name][suite]=sums
    check()
    if requests!=3072 or len(rows)!=1536:raise ValueError('Every model/suite/family must be accounted')
    result=dict(status='all3_cached_same_input_decision_and_exact_greedy_body_diagnostic_complete',created_at=now(),
        proposal=ref(PROPOSAL),source_sha256={v:sha256(ROOT/v) for v in ('scripts/decision_span_diagnostic.py','scripts/run_decision_span_diagnostic.py','tests/test_decision_span_diagnostic.py')},
        CPU_tests=ref(ROOT/'reports/phase6/decision_span_diagnostic_tests.xml'),CPU_ceiling_seconds=10,CPU_elapsed_seconds=time.perf_counter()-START,
        GPU_seconds=0,forward_requests=0,optimizer_updates=0,new_original_corpus_tokens=0,
        raw_requests_reused=requests,correlated_context_pair_rows=len(rows),raw_score_refs=raw_refs,
        summaries=summaries,rows=rows,precision='Existing native CUDA BF16/math full-vocabulary token NLL and all-target greedy conjunction; no re-inference or mixed precision.',
        limits=p['limits'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True)
    atomic_json(TARGET,result)
    print({name:{suite:dict(full_both=v['all128']['full_candidate']['sum_log_likelihood']['both_correct'],
        decision_both=v['all128']['decision_both_correct'],exact_greedy_both=v['all128']['gold_exact_greedy_body_both_poles'],
        hidden_decision_errors=v['all128']['full_sum_correct_but_decision_wrong']) for suite,v in suites.items()} for name,suites in summaries.items()})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    try:run()
    except BaseException as error:
        path=ROOT/'reports/phase6/decision_span_diagnostic_failure.json'
        if not path.exists():atomic_json(path,dict(status='cached_CPU_diagnostic_failed_no_model_execution',error=repr(error),created_at=now(),
            CPU_elapsed_seconds=time.perf_counter()-START,CPU_ceiling_seconds=10,GPU_seconds=0,forward_requests=0,optimizer_updates=0))
        raise
