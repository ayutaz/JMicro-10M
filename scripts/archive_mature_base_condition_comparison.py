"""Archive terminal raw content/state evidence without model/Adam tensors."""
import sys
from pathlib import Path
import tarfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
import run_mature_base_condition_comparison as study

if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    job, review = read_json(study.RUN / 'job.json'), read_json(study.RUN / 'review.json')
    if (job['status'] != 'complete' or alive(job)
            or review['result_sha256'] != sha256(study.RUN / 'compare-result.json')
            or review['status'] != 'mature_parent_matched300M_all320_read_and_reviewed'):
        raise ValueError('Actual terminal raw-bound all320 review required')
    paths = {p for p in study.RUN.rglob('*') if p.is_file()
             and p.suffix in ('.json', '.jsonl', '.py', '.ps1', '.xml', '.lock', '.tsv')}
    paths.update((study.CONFIG, study.PROBE_CONFIG, study.PROPOSAL,
        ROOT / 'reports/phase6/mature_base_condition_preparation.json',
        ROOT / 'reports/phase6/mature_base_condition_comparison_tests.xml',
        ROOT / 'reports/phase6/mature_base_condition_pair_analysis.json'))
    for arm in ('parent10B', *study.ARMS): paths.add(ROOT / f'reports/phase6/mature_base_{arm}_notes.json')
    for name in ('prepare_mature_base_content_review.py','analyze_mature_base_condition_pairs.py','archive_mature_base_condition_comparison.py'):
        paths.add(ROOT / 'scripts' / name)
    target = ROOT / 'reports/phase6/mature-base-condition-comparison-20261006_evidence.tar.gz'
    if target.exists(): raise ValueError('Preserve immutable completed archive')
    entries = [dict(path=p.relative_to(ROOT).as_posix(), sha256=sha256(p), bytes=p.stat().st_size) for p in sorted(paths)]
    temporary = target.with_suffix('.tmp')
    with tarfile.open(temporary, 'w:gz', compresslevel=1) as stream:
        for p in sorted(paths): stream.add(p, arcname=p.relative_to(ROOT).as_posix(), recursive=False)
    temporary.replace(target)
    manifest = dict(stage='terminal_same300M_all320_content_evidence_not_Base_adoption', entries=entries,
        files=len(entries), uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(target), sha256=sha256(target), bytes=target.stat().st_size), checkpoint_tensors_included=False,
        Base_adopted=False, Chat_started=False, quantization_started=False)
    atomic_json(ROOT / 'reports/phase6/mature_base_condition_evidence_manifest.json', manifest)
    print({k:v for k,v in manifest.items() if k != 'entries'})
