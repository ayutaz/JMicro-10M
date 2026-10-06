"""Audit every frozen source-ranking request; source matching is not Base adoption."""
import argparse
import json
import math
from pathlib import Path
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_condition_source_ranking as study


def audit():
    c,prepared=study.inspect(); job=read_json(study.RUN/'job.json'); result=read_json(study.RUN/'result.json')
    if (job['status']!='complete' or alive(job) or result['config_sha256']!=sha256(study.CONFIG)
            or result['evaluated_requests']!=3072 or not 0<result['GPU_seconds']<=job['GPU_elapsed_seconds']<=60
            or any(result[k] for k in ('optimizer_updates','scientific_teacher_tokens','new_original_tokens','protected_test_used','Base_adopted','Chat_started','quantization_started'))
            or not result['quality_criteria_unchanged'] or not result['old_numerical7_preserved']):
        raise ValueError('Actual complete bounded read-only diagnostic required')
    all_rows=[]
    for arm in study.ARMS:
        checks=result['checks'][arm]
        if (not all(checks[k] for k in ('weights_unchanged','RNG_restored','no_gradients','eval_mode'))
                or not math.isfinite(checks['first_request_batched_vs_single_max_NLL_difference'])):
            raise ValueError('Read-only/finite invariants missing')
        for start in range(0,1024,16):
            saved=read_json(study.RUN/'outputs'/arm/f'{start:04d}.json')
            if (saved['config_sha256']!=sha256(study.CONFIG) or saved['checkpoint_sha256']!=c['checkpoints'][arm]['sha256']
                    or saved['cases_sha256']!=c['references']['cases']['sha256']): raise ValueError('Raw score binding differs')
            study.validate_scores(saved['rows'],prepared['cases'][start:start+16])
            all_rows.extend(dict(checkpoint=arm,**r) for r in saved['rows'])
    if study.summarize(all_rows,prepared)!=result['summary']: raise ValueError('Aggregate/pair scores differ from all raw requests')
    cases=prepared['cases']; families=prepared['families']
    if (len(cases)!=1024 or len(families)!=128 or sum(r['content_annotation']['weak_pair'] for r in families)!=12
            or any(r['source']['split']!='train' for r in families)): raise ValueError('Actual128 and flagged12 train cases required')
    report=dict(status='actual_fixed128_source_ranking_all3072_requests_reviewed',created_at=now(),
        config_sha256=sha256(study.CONFIG),result_sha256=sha256(study.RUN/'result.json'),
        cases_sha256=sha256(study.RUN/'cases.json'),aggregate=result['summary']['aggregate'],checks=result['checks'],
        GPU_seconds=result['GPU_seconds'],GPU_occupation_seconds=job['GPU_elapsed_seconds'],evaluated_requests=3072,
        fixed_train_families=128,known_weak_families=12,nonweak_families=116,
        joint_tokenization_differences=sum(not r['joint_tokenization_equal'] for r in cases),
        optimizer_updates=0,scientific_teacher_tokens=0,new_original_tokens=0,protected_test_used=False,
        Base_adopted=False,Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
        old_numerical7_preserved=True,independent_human_blind=False,requested_five_steps_complete=False,
        protocol_clarification=c['protocol_clarification'],tokenization=c['tokenization'],limitations=c['limitations'])
    atomic_json(study.RUN/'review.json',report);atomic_json(ROOT/'reports/phase6/condition_source_ranking_review.json',report)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],aggregate=report['aggregate']),ensure_ascii=False),flush=True)


def archive():
    c,_=study.inspect(); job=read_json(study.RUN/'job.json'); review=read_json(study.RUN/'review.json')
    if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'result.json'): raise ValueError('Terminal raw review required')
    target=ROOT/'reports/phase6/condition-source-ranking-20261006_evidence.tar.gz'
    if target.exists(): raise ValueError('Evidence archive immutable')
    paths={p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.py','.ps1','.xml')}
    paths.update((study.CONFIG,study.PROPOSAL,ROOT/'reports/phase6/condition_source_ranking_tests.xml'))
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths): stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target)
    manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(r['bytes'] for r in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),checkpoint_tensors_included=False)
    atomic_json(ROOT/'reports/phase6/condition_source_ranking_evidence_manifest.json',manifest)
    print(json.dumps({k:v for k,v in manifest.items() if k!='entries'}),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();p.add_argument('--archive',action='store_true');args=p.parse_args()
    if args.archive: archive()
    else: audit()
