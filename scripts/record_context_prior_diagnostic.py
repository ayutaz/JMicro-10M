"""Retain full read-only diagnostic and category/failure tables without adoption."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import csv
import json
import tarfile
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive

RUN = ROOT/'reports/phase6/context-prior-diagnostic-20261006'


def ref(path):
    return dict(path=str(path),sha256=sha256(path))


def main():
    result = read_json(RUN/'result.json');job=read_json(RUN/'job.json')
    if (job['status']!='complete' or alive(job) or result['total_scored_requests']!=8192
            or job['CPU_elapsed_seconds']>180 or not all(all(v.values()) for v in result['all_readonly_checks'].values())):
        raise ValueError('Actual completed bounded4-model diagnostic required')
    rows = []
    for model,suites in result['aggregates'].items():
        for suite,metrics in suites.items():
            for metric,groups in metrics.items():
                for group,values in [('all128',groups['all128']),*groups['by_category'].items()]:
                    rows.append(dict(model=model,suite=suite,metric=metric,group=group,**values))
    table = ROOT/'reports/phase6/context_prior_categories.tsv'
    if table.exists():raise ValueError('Preserve diagnostic tables')
    with table.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)
    family = read_json(RUN/'family-rows.json')
    losses = []
    for suite,pairs in family['comparisons']['conditional_KL'].items():
        prepared = read_json(RUN/f'{suite}-prepared.json')
        by_id = {f['id']:f for f in prepared['families']}
        for row in pairs:
            if row['metric']!='sum_log_likelihood' or not row['lost_both_correct']:continue
            f=by_id[row['id']]
            losses.append(dict(suite=suite,**row,
                exact_family_branches=f['branches'],
                limit='Component swaps are arithmetic proxies, not independently modified models; not causal proof.'))
    atomic_json(ROOT/'reports/phase6/context_prior_lost_families.json',dict(rows=losses))
    bridge=result['comparisons']['conditional_KL']['bridge']['sum_log_likelihood']['all128']
    retention=result['comparisons']['conditional_KL']['retention']['sum_log_likelihood']['all128']
    target=ROOT/'reports/phase6/context_prior_diagnostic_completion.json'
    if target.exists():raise ValueError('Preserve diagnostic completion')
    report=dict(status='actual_context_prior_diagnostic_complete_prior_only_explanation_not_supported',created_at=now(),
        result=ref(RUN/'result.json'),config=result['config'],job=ref(RUN/'job.json'),
        categories=ref(table),lost_families=ref(ROOT/'reports/phase6/context_prior_lost_families.json'),
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        CPU_elapsed_seconds=job['CPU_elapsed_seconds'],CPU_ceiling_seconds=180,GPU_seconds=0,
        original_requests=4096,neutral_requests=4096,total_scored_requests=8192,
        all4_readonly_checks=result['all_readonly_checks'],
        conditional_to_gold_bridge=bridge,conditional_to_gold_retention=retention,
        interpretation='Under identical CPU FP32 scoring, bridge loses13/gains0 families and10of13 losses are reproduced by the context-contribution change alone. No bridge loss is prior-change-only. Retention loses13/gains3,11of13 context-change-only and1prior-change-only. Common continuation-prior offset alone is not the main explanation in this local decomposition. Context separation weakens; do not claim zero context use or causal parameter attribution.',
        precision_limit='CPU FP32 bridge53to40/retention32to22 differ slightly from GPU BF16 bridge54to40/retention33to20. Within-diagnostic subtraction uses only CPU FP32; adoption evidence retains actual GPU outcomes.',
        next_action='Define one context-sensitive outcome-ranking auxiliary comparison using existing TRAIN family pairs, with100M mainCE and existing conditional parentKL replay held fixed. All dev/probe/test material stays outside learning. No prior-adjusted decoder, metric replacement, hard-replay variants or automatic volume extension.',
        limitations=result['limitations'],arithmetic_limit=result['arithmetic_limit'],
        newly_prepared_source_tokens=0,optimizer_updates=0,scientific_teacher_tokens=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True)
    atomic_json(target,report)
    extensions={'.json','.jsonl','.py','.ps1','.xml','.tsv','.md','.toml','.log','.lock'}
    files={p for p in RUN.rglob('*') if p.is_file() and p.suffix in extensions}
    files.update(p for p in (ROOT/'reports/phase6').glob('context_prior_*') if p.suffix in extensions)
    files.update((ROOT/'scripts').glob('*context_prior*'));files.update((ROOT/'tests').glob('test_context_prior*.py'))
    files.update((ROOT/'configs/phase6').glob('context_prior_*.json'))
    files=sorted(p for p in files if p.suffix in extensions and p.name!='context_prior_diagnostic_portable.json')
    manifest={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/context_prior_diagnostic_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve diagnostic archive')
    with tarfile.open(archive,'w:gz',compresslevel=5) as stream:
        for p in files:stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/context_prior_diagnostic_portable.json',dict(files=manifest,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in manifest.values()),archive=ref(archive),archive_bytes=archive.stat().st_size,
        checkpoint_tensors_and_corpus_arrays_excluded=True))
    print({k:report[k] for k in ('status','CPU_elapsed_seconds','total_scored_requests')},flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
