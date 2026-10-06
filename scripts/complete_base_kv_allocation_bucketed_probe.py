"""Preserve the one original-budget PAD-efficiency prototype and UI state."""
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
    phase=ROOT/'reports/phase6';run=phase/'base-kv-allocation-bucketed-probe-20261007'
    target=phase/'base_kv_allocation_bucketed_completion.json'
    if target.exists():raise ValueError('Preserve completed single speed prototype')
    result=json.loads((run/'result.json').read_text());job=json.loads((run/'job.json').read_text())
    config=ROOT/'configs/phase6/base_kv_allocation_bucketed_probe.json'
    if (job['status']!='complete' or alive(job) or not result['passed'] or sha256(config)!=result['config_sha256']
            or not result['all_original_logical_streams_identical'] or not result['full_original_source_sampler_identical']
            or not all(n['passed'] for n in result['numerical'].values())
            or not all(all(r['checks'].values()) for r in result['resume'].values())
            or result['total_actual_prototype_GPU_seconds']>180):
        raise ValueError('Terminal unchanged original protocol and own numerical/resume evidence required')
    ui=json.loads((ROOT/'reports/local/webui/server.json').read_text())
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:model=json.load(response)
    if not alive(ui) or model['busy'] or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Original UI actual process/HTTP identity required')
    speed={}
    for arm in ('GQA','MHA'):
        a,b=result['timings'][arm+'-flat'],result['timings'][arm+'-bucketed']
        speed[arm]=dict(flat_median_original_teachers_per_second=a['median_original_teachers_per_second'],
            grouped_median_original_teachers_per_second=b['median_original_teachers_per_second'],
            measured_ratio=b['median_original_teachers_per_second']/a['median_original_teachers_per_second'],
            flat_physical_inputs=a['total_physical_inputs'],grouped_physical_inputs=b['total_physical_inputs'],
            timed_original_teacher_positions=b['total_original_teacher_positions'],all_timing_steps_per_route=32,
            grouped_data_wait_median_seconds=b['median_data_wait_seconds'])
    eligible=result['science_budget_eligible']
    record=dict(status='grouped_native_speed_prototype_complete_science_budget_ready' if eligible else 'grouped_native_speed_prototype_complete_budget_not_ready',
        created_at=now(),actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        config=dict(path=str(config),sha256=sha256(config)),result_reference=dict(path=str(run/'result.json'),sha256=sha256(run/'result.json')),
        fixed_batch=result['batch'],actual_paired_speed=speed,native_numerical=result['numerical'],
        native_full_context_capacity=result['capacity'],all_resume_checks={a:r['checks'] for a,r in result['resume'].items()},
        all_original_logical_streams_identical=True,full_original_source_sampler_identical=True,
        physical_padding_work_differs=True,bit_identical_old_CUDA_update_claimed=False,
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],
        total_actual_prototype_GPU_seconds=result['total_actual_prototype_GPU_seconds'],fixed_total_prototype_GPU_ceiling=180,
        forecast_all_new_GPU_seconds=result['forecast_all_new_GPU_seconds'],fixed_all_new_GPU_ceiling=9000,
        science_caps_seconds=result['science_caps_seconds'],science_budget_eligible=eligible,
        no_hidden_teacher_reduction_or_cap_increase=True,verification_updates=result['verification_updates'],
        verification_teacher_positions=result['verification_teacher_positions'],scientific_teacher_positions=0,
        new_model_quality_evaluations=0,probe_weights_used_for_science=False,
        interpretation='Measured objective-preserving PAD efficiency on fixed32-step streams; floating accumulation differs within frozen native numerical tolerance. First-source short timing is a budget forecast, not full300M measurement or learned model quality. Flat-budget failure remains preserved.',
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_used=False,next_action=result['next_action'])
    atomic_json(target,record)
    files=[target,config,Path(__file__),phase/'base_kv_allocation_proposal.json',
        phase/'base_kv_allocation_probe_completion.json',phase/'base_kv_allocation_bucketed_tests.xml',
        phase/'base_kv_allocation_trainer_tests.xml']
    files.extend(p for p in sorted(run.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.log','.py','.ps1','.xml','.txt','.lock'))
    launcher=phase/'base-kv-allocation-bucketed-probe-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    if any(not p.is_file() for p in files):raise ValueError('Missing portable evidence')
    folder=phase/'base-kv-allocation-bucketed-evidence-20261007';folder.mkdir(exist_ok=False)
    entries=[]
    for source in files:
        relative=source.relative_to(ROOT);dest=folder/relative;dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,dest);entries.append(dict(path=str(relative),bytes=dest.stat().st_size,sha256=sha256(dest)))
    atomic_json(folder/'manifest.json',dict(created_at=now(),files=entries,tensor_or_corpus_included=False))
    bundle=phase/'base_kv_allocation_bucketed_evidence.tar.gz'
    with tarfile.open(bundle.with_suffix('.tmp'),'w:gz') as archive:archive.add(folder,arcname=folder.name)
    bundle.with_suffix('.tmp').replace(bundle)
    record['archive']=dict(path=str(folder),files=len(entries),bytes=sum(e['bytes'] for e in entries),
        manifest_sha256=sha256(folder/'manifest.json'),archived_completion_is_pre_bundle_record=True,
        compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle)))
    atomic_json(target,record)
    print(json.dumps(dict(status=record['status'],speed=speed,GPU_seconds=record['GPU_occupancy_seconds'],
        total_prototype_GPU_seconds=record['total_actual_prototype_GPU_seconds'],
        forecast_GPU_seconds=record['forecast_all_new_GPU_seconds'],UI_pid=ui['pid'],archive_files=len(entries))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
