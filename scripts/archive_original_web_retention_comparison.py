"""Portable text evidence; native full-state tensors remain in place."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def archive(mode):
    if mode=='diagnostic':
        stem='mature_base_distribution_diagnostic'
        folder=ROOT/'reports/phase6/mature-base-distribution-diagnostic-20261006'
        names=['reports/phase6/mature_base_distribution_diagnostic.json',
            'reports/phase6/mature_base_distribution_diagnostic_proposal.json',
            'reports/phase6/mature_base_distribution_tests.xml',
            'scripts/diagnose_mature_base_distribution.py','tests/test_mature_base_distribution.py']
    else:
        import run_original_web_retention_comparison as study
        stem='original_web_retention_'+('preparation' if mode=='prepare' else 'comparison')
        folder=study.RUN
        names=['reports/phase6/original_web_retention_comparison_proposal.json',
            'reports/phase6/original_web_retention_comparison_tests.xml',
            'configs/phase6/original_web_retention_probe.json',
            'tests/test_original_web_retention_comparison.py','tests/test_original_web_retention_trainer.py',*study.SOURCES]
        if mode=='terminal':
            job=read_json(folder/'job.json');review=read_json(folder/'review.json')
            if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(folder/'compare-result.json'):
                raise ValueError('Actual terminal raw-bound review required')
            names += ['configs/phase6/original_web_retention_comparison.json',
                'reports/phase6/original_web_retention_notes.json',
                'reports/phase6/original_web_retention_comparison_review.json']
        else:
            study.probe_evidence()
    paths={p for p in folder.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.tsv')}
    paths.update(ROOT/n for n in names)
    if any(not p.is_file() for p in paths):raise ValueError('Required evidence file absent')
    job=read_json(folder/'job.json' if mode=='diagnostic' else folder/'probe/job.json')
    if job['status']!='complete' or alive(job):raise ValueError('Completed actual diagnosis/probe required')
    target=ROOT/f'reports/phase6/{stem}_evidence.tar.gz'
    manifest_path=ROOT/f'reports/phase6/{stem}_evidence_manifest.json'
    if target.exists():raise ValueError('Preserve immutable archive')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target)
    manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(r['bytes'] for r in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),checkpoint_tensors_included=False)
    atomic_json(manifest_path,manifest)
    print({k:v for k,v in manifest.items() if k!='entries'})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('diagnostic','prepare','terminal'),required=True)
    archive(p.parse_args().mode)
