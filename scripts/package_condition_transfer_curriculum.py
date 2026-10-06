"""Portable raw native preparation, including generated arrays; no model tensors."""
from pathlib import Path
import shutil
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json


def main():
    paths=set()
    for suffix in ('','-v2'):
        native=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-transfer-curriculum-20261006'+suffix)
        run=ROOT/('reports/phase6/condition-transfer-curriculum-20261006'+suffix)
        manifest=read_json(native/'manifest.json');review=read_json(native/'content-review.json')
        if (review['manifest_sha256']!=sha256(native/'manifest.json') or manifest['arrays_sha256']!=sha256(native/'train.npz')
                or review['notes_sha256']!=sha256(native/'content-notes.json')
                or review['training_pool_accepted']!=(suffix=='-v2')):
            raise ValueError('Actual preserved v1 failure/v2 accepted raw data required')
        for relative,digest in manifest['source_sha256'].items():
            target=run/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():
                if sha256(target)!=digest:raise ValueError('Historical generator source changed')
            else:
                if sha256(ROOT/relative)!=digest:raise ValueError('Current source differs from frozen preparation')
                shutil.copyfile(ROOT/relative,target)
        portable=run/'data';portable.mkdir(exist_ok=True)
        for source in native.iterdir():
            if source.is_file() and source.suffix in ('.json','.npz'):
                target=portable/source.name
                if target.exists() and sha256(target)!=sha256(source):raise ValueError('Portable immutable data differs')
                if not target.exists():shutil.copyfile(source,target)
        paths.update(p for p in run.rglob('*') if p.is_file() and p.suffix in ('.json','.npz','.py','.ps1','.xml'))
    paths.update(ROOT/relative for relative in ('reports/phase6/condition_source_transfer_proposal.json',
        'reports/phase6/condition_source_transfer_preparation.json','reports/phase6/condition_source_transfer_v2_preparation.json',
        'reports/phase6/condition_source_transfer_v1_content_review.json','reports/phase6/condition_source_transfer_v2_content_review.json',
        'reports/phase6/condition_source_transfer_tests.xml','reports/phase6/condition_source_transfer_v2_tests.xml',
        'reports/phase6/condition_source_transfer_tests_initial_assertion_failure.xml','scripts/prepare_condition_transfer_inputs.py',
        'scripts/package_condition_transfer_curriculum.py','tests/test_condition_transfer_curriculum.py'))
    target=ROOT/'reports/phase6/condition-transfer-curriculum-20261006_evidence.tar.gz'
    if target.exists():raise ValueError('Preserve completed portable package')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target)
    result=dict(created_at=now(),entries=entries,files=len(entries),uncompressed_bytes=sum(r['bytes'] for r in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),model_checkpoint_tensors_included=False,
        generated_training_arrays_included=True,raw_generator_and_prior_failure_preserved=True,actual_GPU_seconds=0,scientific_teacher_tokens=0)
    atomic_json(ROOT/'reports/phase6/condition_source_transfer_evidence_manifest.json',result)
    print({k:v for k,v in result.items() if k!='entries'})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
