"""Portable bounded CPU/GPU diagnostic evidence; no checkpoint tensors."""
from pathlib import Path
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    folders=[ROOT/'reports/phase6/base-retention-endpoint-diagnostic-20261006',
             ROOT/'reports/phase6/source-gradient-interference-20261006']
    for folder in folders:
        job=read_json(folder/'job.json')
        if job['status']!='complete' or alive(job):raise ValueError('Both actual diagnostic jobs must be terminal')
    result=read_json(folders[1]/'result.json')
    if result['config_sha256']!=sha256(ROOT/'configs/phase6/source_gradient_interference.json'):
        raise ValueError('Frozen diagnostic binding differs')
    names=['scripts/diagnose_base_retention_endpoints.py','scripts/diagnose_source_gradient_interference.py',
        'scripts/diagnose_source_gradient_interference.ps1','scripts/source_gradient_geometry.py',
        'scripts/archive_base_source_diagnostics.py','tests/test_base_retention_endpoints.py','tests/test_source_gradient_geometry.py',
        'configs/phase6/source_gradient_interference.json','reports/phase6/base_retention_endpoint_diagnostic.json',
        'reports/phase6/base_retention_endpoint_diagnostic_proposal.json','reports/phase6/source_gradient_interference_diagnostic.json',
        'reports/phase6/source_gradient_interference_proposal.json','reports/phase6/base_source_gradient_tests.xml',
        'reports/phase6/base_retention_endpoint_tests.xml']
    paths={p for folder in folders for p in folder.rglob('*') if p.is_file() and p.suffix in ('.json','.xml','.py','.ps1')}
    paths.update(ROOT/n for n in names)
    if any(not p.exists() for p in paths):raise ValueError('Required diagnostic evidence absent')
    archive=ROOT/'reports/phase6/base_source_diagnostics_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve immutable archive')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=archive.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(archive)
    manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(archive),sha256=sha256(archive),bytes=archive.stat().st_size),checkpoint_tensors_included=False)
    atomic_json(ROOT/'reports/phase6/base_source_diagnostics_evidence_manifest.json',manifest)
    print({k:v for k,v in manifest.items() if k!='entries'})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
