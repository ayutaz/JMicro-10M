"""Secondary fixed dev192 context-pair analysis; reuse scores, no new GPU."""
import json
import math
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from analyze_condition_positive_pairs import pair_categories
import run_condition_source_learning as study


def main():
    started=time.monotonic();job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'compare-result.json');review=read_json(study.RUN/'review.json')
    if (job['status']!='complete' or alive(job) or r['scientific_teacher_tokens']!=200000000
            or review['result_sha256']!=sha256(study.RUN/'compare-result.json') or review['protected_test_used']):
        raise ValueError('Actual completed reviewed two100M study required')
    c=read_json(study.CONFIG);base=read_json(Path(c['original_config']['path']));suite=ROOT/'eval/japanese_semantics_v2_1.jsonl'
    if sha256(suite)!=base['evaluation']['semantic_sha256']:raise ValueError('Fixed dev suite changed')
    cases={v['id']:v for v in (json.loads(s) for s in suite.read_text().splitlines()) if v['split']=='dev'}
    old=read_json(Path(c['references']['previous25M_result']['path']));paths={}
    for arm in study.ARMS:paths[arm+'100M']=(study.RUN/f'evaluation/{arm}/evaluation/semantics.json',r['checkpoints'][arm]['checkpoint_sha256'])
    paths['small51225M']=(study.prior.prior.RUN/'evaluation/control/evaluation/semantics.json',old['checkpoints']['control']['checkpoint_sha256'])
    paths['large204825M']=(study.prior.RUN/'evaluation/large2048/evaluation/semantics.json',old['checkpoints']['large2048']['checkpoint_sha256'])
    paths['parent2B']=(ROOT/'reports/phase6/textbook-coverage-2b-20261006/evaluation/large-2000000000/evaluation/semantics.json',c['parent']['sha256'])
    models={};refs={}
    for arm,(path,cp) in paths.items():
        raw=read_json(path);rows=raw['rows'];binding=json.loads(raw['binding'])
        if (not raw['complete'] or raw['expected']!=192 or len(rows)!=192 or len({v['id'] for v in rows})!=192
                or {v['id'] for v in rows}!=set(cases) or binding['checkpoint_sha256']!=cp
                or any(any(v[k]!=cases[v['id']][k] for k in ('family','category','split','context','choices','label')) for v in rows)):
            raise ValueError('Same actual192 contexts/choices/weights required')
        models[arm]=pair_categories(rows)
        if (set(models[arm])!={'negation','quantity','time','comparison','coreference','causality'}
                or any(v['families']!=16 for v in models[arm].values())
                or not math.isclose(sum(v['credit'] for v in rows)/192,raw['summary']['primary']['accuracy']['point'],abs_tol=1e-12)):
            raise ValueError('Six categories/96 complete paired families required')
        refs[arm]=dict(path=str(path),sha256=sha256(path),checkpoint_sha256=cp)
    report=dict(status='actual_two100M_fixed_dev_condition_pairs_reaggregated',created_at=now(),models=models,references=refs,
        study_review_sha256=sha256(study.RUN/'review.json'),suite_sha256=sha256(suite),script_sha256=sha256(Path(__file__)),
        pair_analysis_source_sha256=sha256(ROOT/'scripts/analyze_condition_positive_pairs.py'),CPU_seconds=time.monotonic()-started,
        actual_GPU_seconds=0,scientific_teacher_tokens=0,new_original_tokens=0,protected_test_used=False,
        Base_adopted=False,Chat_started=False,quantization_started=False,requested_five_steps_complete=False,
        limitations='Same previously inspected fixeddev96 families, one learned seed. Descriptive context response, not independent generalization, fluent continuation, certified capacity or causal diagnosis. Historical25M and new100M terminal budget masks differ; do not claim exact trajectory-prefix comparisons. No dev text enters learning.')
    atomic_json(ROOT/'reports/phase6/condition_source_learning_condition_pair_analysis.json',report)
    print(json.dumps({a:{k:{x:v for x,v in g.items() if x!='pairs'} for k,g in groups.items()} for a,groups in models.items()}),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
