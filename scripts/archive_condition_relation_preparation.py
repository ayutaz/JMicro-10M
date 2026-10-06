"""Portable actual CPU source/probe acceptance; excludes optimizer tensors."""
import shutil
import tarfile
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from condition_relation_language import DATA,CONTROL_DATA
from prepare_condition_relation_language import RUN,SOURCES,references


def main():
    references();job=read_json(RUN/'job.json');review=read_json(DATA/'content-review.json');m=read_json(DATA/'manifest.json')
    audit=read_json(RUN/'ordinary-stream-audit.json')
    if (job['status']!='complete_pending_fixed64_content' or alive(job) or not review['training_pool_accepted']
            or not review['all64_read'] or review['notes_sha256']!=sha256(DATA/'content-notes.json')
            or not all(audit['checks'].values()) or audit['generated_manifest_sha256']!=sha256(DATA/'manifest.json')):
        raise ValueError('Actual terminal accepted64 and ordinary stream audit required')
    target=ROOT/'reports/phase6/condition-relation-language-20261006_preparation.tar.gz'
    if target.exists():raise ValueError('Retain existing immutable preparation archive')
    for p in DATA.iterdir():
        if p.is_file() and p.suffix in ('.json','.npz'):
            destination=RUN/'data'/p.name;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,destination)
    source_files=(*SOURCES,'scripts/prepare_condition_relation_inputs.py','scripts/archive_condition_relation_preparation.py',
        'tests/test_condition_relation_language.py','tests/test_condition_relation_comparison.py')
    for rel in source_files:
        destination=RUN/'source'/rel;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,destination)
    completion=dict(status='actual_CPU_relation_language2048_fixed64_and_common100M_teachers_complete',created_at=now(),job=job,
        actual_preparation_process_terminal=True,manifest=dict(path=str(DATA/'manifest.json'),sha256=sha256(DATA/'manifest.json')),
        source_replacement=m['replacement_checks'],body_tokens=m['generated_body_tokens'],body_bytes=m['generated_body_bytes'],
        serialized_tokens=m['serialized_tokens'],full_CE_targets=m['full_CE_targets'],EOS=m['EOS_targets'],
        mean_conditional_exposures_at10M=10000000/m['full_CE_targets'],
        original_serialized_tokens=read_json(CONTROL_DATA/'manifest.json')['serialized_tokens'],
        content_review=dict(path=str(DATA/'content-review.json'),sha256=sha256(DATA/'content-review.json'),weak=review['weak_documents'],
            unresolved_grammar=review['unresolved_grammar_documents'],all64_read=True,unchanged42_prior_notes_reused=True),
        ordinary_stream_audit=dict(path=str(RUN/'ordinary-stream-audit.json'),sha256=sha256(RUN/'ordinary-stream-audit.json'),checks=audit['checks'],CPU_seconds=audit['CPU_seconds']),
        CPU_tests=dict(source='reports/phase6/condition_relation_language_tests.xml',count=4,seconds=1.16,
            comparison='reports/phase6/condition_relation_comparison_tests.xml',comparison_count=4,comparison_seconds=2.09),
        scientific_teacher_tokens=0,actual_GPU_seconds=0,new_original_public_corpus_tokens=0,protected_test_used=False,
        Base_adopted=False,Chat_started=False,quantization_started=False,
        limitations='Preparation evidence only. Same original1024 families/2048 documents with684 language replacements; other1364 full texts identical.128 new local probes and128 old retention are not independent natural-language quality. Actual science is recorded separately.')
    atomic_json(RUN/'preparation-completion.json',completion)
    atomic_json(ROOT/'reports/phase6/condition_relation_language_preparation_completion.json',completion)
    paths={p for p in RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.npz','.py','.ps1','.xml')}
    paths.update((ROOT/'reports/phase6/condition_relation_language_proposal.json',
        ROOT/'reports/phase6/condition_relation_language_tests.xml',ROOT/'reports/phase6/condition_relation_comparison_tests.xml'))
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as archive:
        for p in sorted(paths):archive.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target)
    manifest=dict(entries=entries,files=len(entries),uncompressed_bytes=sum(v['bytes'] for v in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),dataset_arrays_included=True,checkpoint_tensors_included=False)
    atomic_json(ROOT/'reports/phase6/condition_relation_language_preparation_manifest.json',manifest)
    print({k:v for k,v in manifest.items() if k!='entries'})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
