"""Portable complete text evidence; original learned weights remain on WSL."""
from pathlib import Path
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive

if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    run=ROOT/'reports/phase6/material-comparison-20261006';job=read_json(run/'job.json')
    assert job['status']=='complete' and not alive(job) and (run/'review.json').exists()
    files=[p for p in run.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.md')]
    files.extend(ROOT/p for p in ('configs/phase6/material_comparison.json','scripts/review_material_comparison.py','reports/phase6/material_comparison_control_notes.json','reports/phase6/material_comparison_wikipedia_notes.json'))
    target=ROOT/'reports/phase6/material_comparison_evidence.tar.gz'
    with tarfile.open(target,'w:gz',compresslevel=3) as archive:
        for p in sorted(files):archive.add(p,arcname=str(p.relative_to(ROOT)),recursive=False)
    report=dict(path=str(target.relative_to(ROOT)),sha256=sha256(target),bytes=target.stat().st_size,
        members=[dict(path=str(p.relative_to(ROOT)),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(files)],
        limitations='No checkpoint tensors or large shards; they remain at bound WSL paths',created_at=now())
    write_json(ROOT/'reports/phase6/material_comparison_evidence_manifest.json',report);print(f"Archived {len(files)} text evidence files, {report['bytes']} bytes",flush=True)
