"""Archive actual native/auxiliary probe and its measured budget decision."""
import json
from pathlib import Path
import shutil
import sys
import tarfile
import urllib.request

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    phase=ROOT/'reports/phase6';run=phase/'base-next-two-token-probe-20261007'
    target=phase/'base_next_two_token_probe_completion.json'
    if target.exists():raise ValueError('Preserve actual native/auxiliary probe completion')
    result=json.loads((run/'result.json').read_text());job=json.loads((run/'job.json').read_text())
    config=ROOT/'configs/phase6/base_next_two_token_probe.json'
    if (job['status']!='complete' or alive(job) or not result['passed'] or sha256(config)!=result['config_sha256']
            or not all(result['initial_checks'].values()) or not all(result['all_resume_and_source_checks'].values())
            or len(result['all32_timing_speeds'])!=32):
        raise ValueError('Actual exited native/auxiliary/source protocol and all32 timings required')
    ui=json.loads((ROOT/'reports/local/webui/server.json').read_text())
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:model=json.load(response)
    if not alive(ui) or model['busy'] or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Actual original UI process/HTTP identity required')
    eligible=result['science_budget_eligible']
    record=dict(status='native_next_two_probe_complete_science_budget_ready' if eligible else 'native_next_two_probe_complete_fixed_budget_not_ready',
        created_at=now(),actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        config=dict(path=str(config),sha256=sha256(config)),result_reference=dict(path=str(run/'result.json'),sha256=sha256(run/'result.json')),
        initial_checks=result['initial_checks'],all_resume_and_source_checks=result['all_resume_and_source_checks'],
        capacity=result['capacity'],matched_batch=48,median_original_teachers_per_second=result['median_original_teachers_per_second'],
        all_timing_updates=32,GPU_occupancy_seconds=result['GPU_occupancy_seconds'],GPU_limit_seconds=180,
        science_cap_seconds=result['science_cap_seconds'],maximum_scientific_GPU_seconds=3965,
        science_budget_eligible=eligible,fixed_next_two_protocol_closed=not eligible,
        verification_updates=result['verification_updates'],
        verification_original_teacher_positions=result['verification_original_teacher_positions'],
        verification_next_two_positions=result['verification_next_two_positions'],scientific_teacher_positions=0,
        new_model_quality_evaluations=0,probe_weights_used_for_science=False,
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_used=False,
        interpretation='Actual native and train-only head forward/backward, all-state save/resume and original stream evidence only. Short measured median is a budget forecast, not science completion or Japanese generation improvement. Include additional future positions/parameters/compute separately.',
        next_action=result['next_action'])
    atomic_json(target,record)
    files=[target,config,Path(__file__),phase/'base_next_two_token_proposal.json',phase/'base_next_two_token_trainer_tests.xml']
    files.extend(p for p in sorted(run.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.log','.py','.ps1','.xml','.lock','.txt'))
    launcher=phase/'base-next-two-token-probe-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    if any(not p.is_file() for p in files):raise ValueError('Missing actual portable text evidence')
    folder=phase/'base-next-two-token-probe-evidence-20261007';folder.mkdir(exist_ok=False);entries=[]
    for source in files:
        relative=source.relative_to(ROOT);dest=folder/relative;dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,dest);entries.append(dict(path=str(relative),bytes=dest.stat().st_size,sha256=sha256(dest)))
    atomic_json(folder/'manifest.json',dict(created_at=now(),files=entries,tensor_or_corpus_included=False))
    bundle=phase/'base_next_two_token_probe_evidence.tar.gz'
    with tarfile.open(bundle.with_suffix('.tmp'),'w:gz') as archive:archive.add(folder,arcname=folder.name)
    bundle.with_suffix('.tmp').replace(bundle)
    record['archive']=dict(path=str(folder),files=len(entries),bytes=sum(e['bytes'] for e in entries),
        manifest_sha256=sha256(folder/'manifest.json'),archived_completion_is_pre_bundle_record=True,
        compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle)))
    atomic_json(target,record)
    print(json.dumps(dict(status=record['status'],GPU_seconds=record['GPU_occupancy_seconds'],
        median_original_teachers_per_second=record['median_original_teachers_per_second'],science_cap_seconds=record['science_cap_seconds'],
        UI_pid=ui['pid'],archive_files=len(entries))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
