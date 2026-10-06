"""Archive immutable preparation or terminal read-only comparison evidence."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
import run_early_exposure_comparison as study


def archive(mode):
    c=read_json(study.CONFIG)
    paths={study.CONFIG,study.PROPOSAL,ROOT/'reports/phase6/early_exposure_comparison_tests.xml',
        ROOT/'reports/phase6/original_Web_early_checkpoint_inventory.json',Path(c['references']['final_notes']['path']),
        Path(c['references']['final_generation']['path']),ROOT/'scripts/prepare_early_exposure_review.py',Path(__file__)}
    paths.update(ROOT/p for p in study.SOURCES)
    paths.update(p for p in (study.RUN/'source').rglob('*') if p.is_file())
    if mode=='terminal':
        job=read_json(study.RUN/'job.json');review=read_json(study.RUN/'review.json')
        if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json'):
            raise ValueError('Terminal actual raw-bound content review required')
        paths.update(p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.xml','.py','.ps1'))
        paths.update((ROOT/'reports/phase6/early_exposure_notes.json',ROOT/'reports/phase6/early_exposure_observations.tsv',
            ROOT/'reports/phase6/early_exposure_comparison_review.json'))
    if any(not p.is_file() for p in paths):raise ValueError('Required evidence absent')
    stem='early_exposure_'+('preparation' if mode=='prepare' else 'comparison')
    target=ROOT/f'reports/phase6/{stem}_evidence.tar.gz'
    if target.exists():raise ValueError('Preserve immutable evidence archive')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target)
    manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),checkpoint_tensors_included=False)
    atomic_json(ROOT/f'reports/phase6/{stem}_evidence_manifest.json',manifest)
    print({k:v for k,v in manifest.items() if k!='entries'})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('prepare','terminal'),required=True)
    archive(p.parse_args().mode)
