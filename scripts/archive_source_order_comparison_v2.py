"""Portable text evidence only; model/optimizer states remain on the WSL disk."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
import run_source_order_condition_comparison_v2 as study


def archive(mode):
    files={Path(__file__),study.PROPOSAL,study.PROBE_CONFIG,study.CONFIG,
        ROOT/'scripts/implement_source_order_comparison.py',ROOT/'scripts/implement_source_order_comparison_v2.py',
        ROOT/'scripts/prepare_source_order_content_review_v2.py'}
    files.update(ROOT/p for p in study.SOURCES)
    for name in ('source_order_condition_tests.xml','source_order_comparison_tests.xml','source_order_budget_v2_tests.xml',
                 'source_order_budget_evidence.json','source_order_budget_rejection_v1.json'):
        files.add(ROOT/'reports/phase6'/name)
    files.update(p for p in study.PROBE_RUN.rglob('*') if p.is_file() and p.suffix in ('.py','.ps1','.json','.jsonl','.xml'))
    if mode=='terminal':
        job=read_json(study.RUN/'job.json'); review=read_json(study.RUN/'review.json')
        if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json'):
            raise ValueError('Actual terminal/all80 reviewed evidence required')
        files.update(p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.py','.ps1','.json','.jsonl','.xml'))
        for name in ('source_order_condition_notes.json','source_order_condition_observations.tsv',
                     'source_order_condition_comparison_v2_review.json','source_order_condition_comparison_completion.json',
                     'source_order_followup_diagnostic_proposal.json'):
            files.add(ROOT/'reports/phase6'/name)
    if any(not p.is_file() for p in files):raise ValueError('Required text evidence absent')
    stem='source_order_condition_'+('preparation' if mode=='prepare' else 'comparison')
    target=ROOT/f'reports/phase6/{stem}_evidence.tar.gz'
    if target.exists():raise ValueError('Preserve immutable archive')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(files)]
    temp=target.with_suffix('.tmp')
    with tarfile.open(temp,'w:gz',compresslevel=1) as stream:
        for p in sorted(files):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
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
