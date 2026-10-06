"""Archive text, raw review and source freezes; retain tensor states in WSL."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
import run_historical_parent_condition_comparison_v3 as study


def archive(mode):
    paths={Path(__file__),study.PROPOSAL,study.PROBE_CONFIG,
        ROOT/'reports/phase6/base_parent_baseline_audit.json',
        ROOT/'reports/phase6/base_parent_baseline_audit_proposal.json',
        ROOT/'reports/phase6/base_parent_baseline_tests.xml',
        ROOT/'reports/phase6/historical_parent_condition_v2_tests.xml',
        ROOT/'reports/phase6/historical_parent_condition_v3_tests.xml',
        ROOT/'reports/phase6/historical_parent_initial_probe_failure.json',
        ROOT/'reports/phase6/historical_parent_v2_probe_failure.json',
        ROOT/'scripts/prepare_historical_parent_v3_repair.py'}
    paths.update(ROOT/p for p in study.SOURCES)
    for version in ('','_v2'):
        paths.update(ROOT/f'scripts/{prefix}historical_parent_condition_comparison{version}.{suffix}'
            for prefix,suffix in (('run_','py'),('run_','ps1'),('review_','py')))
        paths.add(ROOT/f'reports/phase6/historical_parent_condition_comparison{version}_proposal.json')
        paths.add(ROOT/f'configs/phase6/historical_parent_condition_probe{version}.json')
    for folder in ('historical-parent-condition-comparison-20261006','historical-parent-condition-comparison-v2-20261006'):
        paths.update(p for p in (ROOT/'reports/phase6'/folder).rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1'))
    paths.update(p for p in (study.RUN/'probe').rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1'))
    if mode=='terminal':
        job=read_json(study.RUN/'job.json');review=read_json(study.RUN/'review.json')
        if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json'):
            raise ValueError('Actual complete reviewed all80 evidence required')
        paths.update((study.CONFIG,ROOT/'scripts/prepare_historical_parent_content_review.py',
            ROOT/'reports/phase6/historical_parent_condition_notes.json',
            ROOT/'reports/phase6/historical_parent_condition_observations.tsv',
            ROOT/'reports/phase6/historical_parent_condition_comparison_v3_review.json'))
        paths.update(p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml'))
    if any(not p.is_file() for p in paths):raise ValueError('Required evidence absent')
    stem='historical_parent_condition_'+('preparation' if mode=='prepare' else 'comparison')
    target=ROOT/f'reports/phase6/{stem}_evidence.tar.gz'
    if target.exists():raise ValueError('Preserve immutable archive')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temp=target.with_suffix('.tmp')
    with tarfile.open(temp,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temp.replace(target)
    manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),
        checkpoint_tensors_included=False,raw_training_arrays_included=False)
    atomic_json(ROOT/f'reports/phase6/{stem}_evidence_manifest.json',manifest)
    print({k:v for k,v in manifest.items() if k!='entries'})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('prepare','terminal'),required=True)
    archive(p.parse_args().mode)
