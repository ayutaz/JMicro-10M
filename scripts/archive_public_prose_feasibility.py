"""Preserve rejected source pilots and actual process/UI evidence."""
import json
from pathlib import Path
import sys
import tarfile
from urllib.request import urlopen
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from phase6_performance import identity,alive


def main():
    runs=['public-prose-teacher-recovery-20261006','public-prose-teacher-probe-20261006',
          'public-magpie-source-recovery-20261006','public-magpie-prose-20261006']
    jobs={name:read_json(ROOT/'reports/phase6'/name/'job.json') for name in runs}
    if any(j['status']!='complete' or alive(j) for j in jobs.values()):
        raise ValueError('All four actual jobs must have exited')
    teacher=read_json(ROOT/'reports/phase6/public_prose_teacher_content_review.json')
    magpie=read_json(ROOT/'reports/phase6/public_magpie_prose_content_review.json')
    if teacher['accepted'] or magpie['accepted']:
        raise ValueError('This terminal bundle preserves both rejected pilots')
    ui=identity(578328)
    with urlopen('http://127.0.0.1:7860/api/model',timeout=15) as response:
        model=json.load(response)
    if model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290' or model['busy']:
        raise ValueError('Original idle10B UI required')
    completion_path=ROOT/'reports/phase6/public_prose_feasibility_completion.json'
    archive_path=ROOT/'reports/phase6/public_prose_feasibility_evidence.tar.gz'
    if completion_path.exists() or archive_path.exists():
        raise ValueError('Preserve completed archive')
    completion=dict(status='both_public_prose_source_pilots_complete_rejected_Base_pending',created_at=now(),
        jobs=jobs,actual_processes_absent=True,ui=dict(**ui,model=model),
        teacher_review_sha256=sha256(ROOT/'reports/phase6/public_prose_teacher_content_review.json'),
        magpie_review_sha256=sha256(ROOT/'reports/phase6/public_magpie_prose_content_review.json'),
        local_teacher=dict(weak=teacher['weak'],cases=64,GPU_seconds=teacher['GPU_seconds'],
                           raw10M_body_seconds=teacher['extrapolated_raw10M_student_body_seconds'],accepted=False),
        public_magpie=dict(weak=magpie['weak'],cases=64,source_serialized_tokens=magpie['source_serialized_tokens'],
                          CPU_preparation_seconds=magpie['CPU_preparation_seconds'],accepted=False),
        student_scientific_teacher_tokens=0,optimizer_updates=0,project_Chat_started=False,
        student_quantization_started=False,Base_complete=False,Base_adopted=False,protected_test_used=False,
        limits='Source feasibility evidence only; nonblind64 source samples, no independent human or comprehensive factual audit. No new student checkpoint or quality gain. Rejected text/weights/arrays remain in WSL and cannot be counted as accepted material.',
        next_action='Bounded source registry discovery: at most4 new public Japanese short-story/plain-prose candidates, metadata/card only, no bulk recovery or GPU. Record license, gated access, language, upstream teacher, independent whole-document size/split, novelty versus project registry. Freeze one supply/content pilot only if a materially new source can plausibly supply10M serialized source tokens; otherwise preserve none-feasible without repeated filters or source sweeps.')
    write_json(completion_path,completion)
    paths={completion_path,Path(__file__),ROOT/'reports/phase6/base_failure_route_synthesis.json'}
    names=['inspect_public_prose_teacher','recover_public_prose_teacher','probe_public_prose_teacher',
           'review_public_prose_teacher','inspect_public_magpie_source','recover_public_magpie_source',
           'prepare_public_magpie_prose','review_public_magpie_prose','synthesize_base_failure_routes']
    for name in names:
        for ext in ('.py','.ps1'):
            p=ROOT/'scripts'/f'{name}{ext}'
            if p.exists():paths.add(p)
    for stem in ('public_prose_teacher','public_magpie'):
        paths.update(p for p in (ROOT/'reports/phase6').glob(stem+'*') if p.is_file() and p.suffix in ('.json','.tsv','.xml'))
    for name in runs:
        paths.update(p for p in (ROOT/'reports/phase6'/name).rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1'))
    paths.update(ROOT/p for p in ('tests/test_public_prose_teacher_requests.py','tests/test_public_magpie_prose.py',
        'src/jmicro/experiment.py','src/jmicro/tokenizer.py','scripts/phase6_performance.py'))
    paths.add(Path('/home/aihub_ubuntu/jmicro-data/phase6/public-magpie-prose-20261006/manifest.json'))
    if any(not p.is_file() for p in paths):raise ValueError('Required terminal evidence absent')
    def relative(p):
        return p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else 'external/public-magpie-prose/manifest.json'
    entries=[dict(path=relative(p),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temp=archive_path.with_suffix('.tmp')
    with tarfile.open(temp,'w:gz',compresslevel=1) as archive:
        for p in sorted(paths):archive.add(p,arcname=relative(p),recursive=False)
    temp.replace(archive_path)
    manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(archive_path),sha256=sha256(archive_path),bytes=archive_path.stat().st_size),
        teacher_weights_included=False,bulk_public_source_included=False,training_arrays_included=False,
        source_hashes_and_native_paths_retained=True)
    write_json(ROOT/'reports/phase6/public_prose_feasibility_evidence_manifest.json',manifest)
    print(json.dumps({k:v for k,v in manifest.items() if k!='entries'}))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
