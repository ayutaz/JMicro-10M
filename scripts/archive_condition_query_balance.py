"""Portable text evidence; keep full optimizer/checkpoint tensors in native WSL."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parents[1] / 'scripts')]
from prepare_condition_query_balance import ROOT, RUN as PREP, DATA, sha, read, write
import run_condition_query_balance_comparison as study
from phase6_performance import alive


def archive(mode):
    paths = {study.PROPOSAL, ROOT / 'reports/phase6/base_transfer_margin_diagnostic.json',
        ROOT / 'scripts/diagnose_base_transfer_margins.py', ROOT / 'tests/test_base_transfer_margins.py',
        ROOT / 'reports/phase6/base_transfer_margin_tests.xml', ROOT / 'reports/phase6/query_balance_preparation_tests.xml',
        ROOT / 'reports/phase6/query_balance_comparison_tests.xml', ROOT / 'reports/phase6/condition_query_balance_preparation.json',
        ROOT / 'reports/phase6/condition_query_balance_content_review.json', study.PROBE_CONFIG, Path(__file__)}
    paths.update(ROOT / p for p in study.SOURCES)
    paths.update(p for p in PREP.rglob('*') if p.is_file() and p.suffix == '.json')
    for filename in ('transfer-probes.json', 'retention-probes.json'):
        (PREP / filename).write_bytes((DATA / filename).read_bytes())
        paths.add(PREP / filename)
    if mode == 'terminal':
        job, review = read(study.RUN / 'job.json'), read(study.RUN / 'review.json')
        if job['status'] != 'complete' or alive(job) or review['result_sha256'] != sha(study.RUN / 'compare-result.json'):
            raise ValueError('Terminal actual reviewed all80 evidence required')
        paths.update((study.CONFIG, ROOT / 'reports/phase6/condition_query_balance_notes.json',
                      ROOT / 'reports/phase6/condition_query_balance_comparison_review.json'))
        paths.update(p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.xml','.ps1'))
    if any(not p.is_file() for p in paths):
        raise ValueError('Required evidence file absent')
    stem = 'condition_query_balance_' + ('preparation' if mode == 'prepare' else 'comparison')
    target = ROOT / f'reports/phase6/{stem}_evidence.tar.gz'
    if target.exists():
        raise ValueError('Preserve immutable archive')
    entries = [dict(path=p.relative_to(ROOT).as_posix(), sha256=sha(p), bytes=p.stat().st_size) for p in sorted(paths)]
    temp = target.with_suffix('.tmp')
    with tarfile.open(temp, 'w:gz', compresslevel=1) as stream:
        for p in sorted(paths):
            stream.add(p, arcname=p.relative_to(ROOT).as_posix(), recursive=False)
    temp.replace(target)
    manifest = dict(entries=entries, text_files=len(entries), uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(target),sha256=sha(target),bytes=target.stat().st_size), checkpoint_tensors_included=False,
        raw_training_arrays_included=False, native_training_array_sha256=read(DATA / 'manifest.json')['arrays_sha256'])
    write(ROOT / f'reports/phase6/{stem}_evidence_manifest.json', manifest)
    print({k:v for k,v in manifest.items() if k != 'entries'})


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser(); p.add_argument('--mode',choices=('prepare','terminal'),required=True)
    archive(p.parse_args().mode)
