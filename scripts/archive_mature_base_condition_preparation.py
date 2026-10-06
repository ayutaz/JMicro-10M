"""Portable completed CUDA preparation evidence; never claims science complete."""
import sys
from pathlib import Path
import tarfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, sha256
from jmicro.training import atomic_json
import run_mature_base_condition_comparison as study

if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    study.probe_evidence()
    paths = {p for p in (study.RUN / 'probe').rglob('*') if p.is_file()
             and p.suffix in ('.json', '.jsonl', '.py', '.ps1', '.xml', '.lock')}
    paths.update((study.CONFIG, study.PROBE_CONFIG, study.PROPOSAL,
        ROOT / 'reports/phase6/mature_base_condition_preparation.json',
        ROOT / 'reports/phase6/mature_base_condition_comparison_tests.xml'))
    paths.update(ROOT / p for p in study.SOURCES)
    target = ROOT / 'reports/phase6/mature-base-condition-preparation-20261006.tar.gz'
    if target.exists(): raise ValueError('Preserve immutable completed preparation archive')
    entries = [dict(path=p.relative_to(ROOT).as_posix(), sha256=sha256(p), bytes=p.stat().st_size) for p in sorted(paths)]
    temporary = target.with_suffix('.tmp')
    with tarfile.open(temporary, 'w:gz', compresslevel=1) as stream:
        for p in sorted(paths): stream.add(p, arcname=p.relative_to(ROOT).as_posix(), recursive=False)
    temporary.replace(target)
    manifest = dict(stage='preparation_only_scientific_training_and_content_pending', entries=entries,
        files=len(entries), uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(target), sha256=sha256(target), bytes=target.stat().st_size),
        checkpoint_tensors_included=False, scientific_training_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False)
    atomic_json(ROOT / 'reports/phase6/mature_base_condition_preparation_manifest.json', manifest)
    print({k:v for k,v in manifest.items() if k != 'entries'})
