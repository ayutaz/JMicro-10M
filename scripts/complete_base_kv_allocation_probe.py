"""Bind actual terminal paired probe, budget decision and restored UI."""
import json
from pathlib import Path
import shutil
import sys
import tarfile
import urllib.request

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    phase = ROOT/'reports/phase6'
    run = phase/'base-kv-allocation-probe-20261007'
    result = json.loads((run/'result.json').read_text())
    job = json.loads((run/'job.json').read_text())
    target = phase/'base_kv_allocation_probe_completion.json'
    if target.exists():
        raise ValueError('Preserve actual completed probe')
    if (job['status'] != 'complete' or alive(job) or not result['passed']
            or not result['original_stream_parity']
            or not all(all(r['checks'].values()) for r in result['resume'].values())):
        raise ValueError('Terminal native CUDA protocol and original stream parity required')
    config = ROOT/'configs/phase6/base_kv_allocation_probe.json'
    if sha256(config) != result['config_sha256']:
        raise ValueError('Fixed native CUDA probe config differs')
    ui = json.loads((ROOT/'reports/local/webui/server.json').read_text())
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        model = json.load(response)
    expected = '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    if not alive(ui) or model['busy'] or model['checkpoint_sha256'] != expected:
        raise ValueError('Restored original UI identity required')
    eligible = result['science_budget_eligible']
    record = dict(status='paired_native_probe_complete_science_ready' if eligible else 'paired_native_probe_complete_300M_protocol_closed_budget_exceeded',
        created_at=now(),actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        config=dict(path=str(config),sha256=sha256(config)),
        result_reference=dict(path=str(run/'result.json'),sha256=sha256(run/'result.json')),
        selected_common_batch=result['selected_common_batch'],
        common_resident_candidates=result['common_resident_candidates'],
        all_resume_checks={a:r['checks'] for a,r in result['resume'].items()},
        original_source_stream_parity=True,GPU_occupancy_seconds=result['GPU_occupancy_seconds'],
        forecast_all_new_GPU_seconds=result['forecast_all_new_GPU_seconds'],fixed_all_new_GPU_ceiling=9000,
        science_budget_eligible=eligible,fixed_300M_allocation_protocol_closed=not eligible,
        no_cap_increase_or_hidden_teacher_reduction=True,
        verification_updates=result['verification_updates'],verification_teacher_positions=result['verification_teacher_positions'],
        scientific_teacher_positions=0,new_model_quality_evaluations=0,probe_weights_used_for_science=False,
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_used=False,
        interpretation='Native finite capacity/resume evidence is not learned model quality. Short first-source timings are a forecast; they do not prove full300M duration. Keep measured ceilings and all quality gates.',
        next_action=result['next_action'])
    atomic_json(target,record)
    files = [target,config,Path(__file__),phase/'base_kv_allocation_proposal.json',phase/'base_kv_allocation_trainer_tests.xml']
    files.extend(p for p in sorted(run.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.log','.py','.ps1','.xml','.txt','.lock'))
    launcher = phase/'base-kv-allocation-probe-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    if any(not p.is_file() for p in files):
        raise ValueError('Missing text evidence')
    folder = phase/'base-kv-allocation-probe-evidence-20261007'
    folder.mkdir(exist_ok=False)
    entries = []
    for source in files:
        relative = source.relative_to(ROOT)
        dest = folder/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,dest)
        entries.append(dict(path=str(relative),bytes=dest.stat().st_size,sha256=sha256(dest)))
    atomic_json(folder/'manifest.json',dict(created_at=now(),files=entries,tensor_or_corpus_included=False))
    bundle = phase/'base_kv_allocation_probe_evidence.tar.gz'
    with tarfile.open(bundle.with_suffix('.tmp'),'w:gz') as archive:
        archive.add(folder,arcname=folder.name)
    bundle.with_suffix('.tmp').replace(bundle)
    record['archive'] = dict(path=str(folder),files=len(entries),bytes=sum(e['bytes'] for e in entries),
        manifest_sha256=sha256(folder/'manifest.json'),archived_completion_is_pre_bundle_record=True,
        compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle)))
    atomic_json(target,record)
    print(json.dumps(dict(status=record['status'],selected_batch=record['selected_common_batch'],
        forecast_GPU_seconds=record['forecast_all_new_GPU_seconds'],UI_pid=ui['pid'],archive_files=len(entries))))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
