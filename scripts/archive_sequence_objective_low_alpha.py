"""Archive actual low-alpha text evidence and the reused CE control references."""
import json
from pathlib import Path
import sys
import tarfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from phase6_performance import alive
from run_sequence_objective_low_alpha import RUN,CONFIG,PROBE_CONFIG,inspect
import run_sequence_objective_comparison as old


def archive():
    c,_,_,_=inspect(CONFIG);job=read_json(RUN/'job.json');review=read_json(RUN/'review.json')
    assert job['status']=='complete' and not alive(job)
    assert review['status']=='matched_reused_CE_and_actual_low_alpha25M_all80_complete'
    assert review['result_sha256']==sha256(RUN/'compare-result.json')
    notes=ROOT/'reports/phase6/sequence_objective_low_alpha_notes.json'
    assert review['notes_sha256']==sha256(notes)
    assert not review['protected_test_used'] and review['new_scientific_teacher_tokens']==25000000
    paths=[p for p in RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml')]
    paths.extend([CONFIG,PROBE_CONFIG,notes,ROOT/'reports/phase6/sequence_objective_low_alpha_content_review.json',
        ROOT/'reports/phase6/sequence_objective_low_alpha_tests.xml',ROOT/'scripts/archive_sequence_objective_low_alpha.py',
        Path(c['prior_config']['path']),Path(c['prior_result']['path']),Path(c['prior_review']['path']),
        Path(c['diagnosis']['path']),Path(c['control_notes']['path']),Path(c['control_generation']['path']),
        old.RUN/'CE/training/metrics.jsonl'])
    paths=sorted(set(paths));assert all(p.is_file() for p in paths)
    entries=[dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha256(p)) for p in paths]
    manifest=ROOT/'reports/phase6/sequence_objective_low_alpha_evidence_manifest.json'
    write_json(manifest,dict(status='completed_text_evidence_archive',entries=entries,text_files=len(entries),
        uncompressed_bytes=sum(e['bytes'] for e in entries),checkpoint_tensors_included=False,native_checkpoints_retained=True,
        new_scientific_teacher_tokens=25000000,reused_control_teacher_tokens=25000000,
        verification_teacher_tokens=review['verification_teacher_tokens'],created_at=now()))
    output=ROOT/'reports/phase6/sequence-objective-low-alpha-20261006_evidence.tar.gz'
    assert not output.exists(),'Completed archive is immutable'
    temporary=output.with_suffix(output.suffix+'.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for path in (*paths,manifest):stream.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(output)
    print(json.dumps(dict(path=str(output),sha256=sha256(output),bytes=output.stat().st_size,
        text_files=len(entries),uncompressed_bytes=sum(e['bytes'] for e in entries))))


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    archive()
