"""Archive actual exited ContextMixing verification and persist the live scientific handoff."""
import json
from pathlib import Path
import sys
import tarfile
import time
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from run_base_context_mixing import CONFIG,RUN,PROBE


def main():
    started=time.monotonic()
    output=ROOT/'reports/phase6/base_context_mixing_probe_completion.json'
    if output.exists(): raise ValueError('Preserve actual ContextMixing probe closeout')
    c=read_json(CONFIG); result=read_json(PROBE/'result.json'); job=read_json(PROBE/'job.json')
    p=read_json(Path(c['probe_config']['path']))
    if (alive(job) or job['status']!='complete' or result['status']!='complete' or not result['passed'] or
        not all(result['initial_checks'].values()) or not all(result['all_resume_and_source_checks'].values()) or
        result['config_sha256']!=sha256(Path(c['probe_config']['path'])) or
        result['actual_identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')} or
        not 0<result['GPU_occupancy_seconds']==job['GPU_occupancy_seconds']<=180 or
        c['probe_GPU_seconds']!=result['GPU_occupancy_seconds'] or c['GPU_budget_seconds']+c['probe_GPU_seconds']>7200):
        raise ValueError('Actual exited bounded CUDA verification required')
    for name,digest in p['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen verified implementation changed')
    science=read_json(RUN/'job.json')
    if not alive(science) or science['config_sha256']!=sha256(CONFIG) or science['stage']!='context_mixing-training':
        raise ValueError('Persist actual live scientific identity and heartbeat')
    start=ROOT/'reports/phase6/base_context_mixing_science_start.json'
    atomic_json(start,dict(created_at=now(),status='native_ContextMixing100M_science_live',actual_identity={k:science[k] for k in ('pid','boot_id','start_ticks')},
        scientific_config=dict(path=str(CONFIG),sha256=sha256(CONFIG)),snapshot= science,
        target_original_teacher_tokens=100000000,control_reused_original_teacher_tokens=100000000,
        new_unique_dataset_tokens=0,additional_parameters=0,GPU_cap_seconds=c['GPU_budget_seconds'],
        cumulative_total_cap_seconds=7200,source_and_native_inference_unchanged=True,
        restart= science['restart_command'],UI='Stopped while science runs; durable launcher restores original10B on exit.',
        Base_complete=False,Chat_started=False,quantization_started=False))
    checkpoint_refs=[]
    for name in ('continuous','resumed'):
        path=PROBE/(name+'.pt'); checkpoint_refs.append(dict(path=str(path),bytes=path.stat().st_size,sha256=sha256(path)))
    completion=dict(created_at=now(),status='ContextMixing_native_CUDA_verification_closed_science_started',actual_identity=result['actual_identity'],
        actual_process_absent=True,result_sha256=sha256(PROBE/'result.json'),initial_checks=result['initial_checks'],
        resume_source_checks=result['all_resume_and_source_checks'],GPU_seconds=result['GPU_occupancy_seconds'],
        verification_updates=result['verification_updates'],verification_original_teacher_positions=result['verification_original_teacher_positions'],
        capacity_forward_backward_original_positions=result['capacity_forward_backward_original_positions'],
        selected_matched_batch=48,median_original_teachers_per_second=result['median_original_teachers_per_second'],
        worst_peak_VRAM_bytes=result['capacity']['peak_VRAM_bytes'],checkpoint_refs=checkpoint_refs,
        total_GPU_cap_seconds=7200,scientific_GPU_cap_seconds=c['GPU_budget_seconds'],
        source_binding=c['source_binding'],parent=c['parent'],probe_weights_used_for_science=False,
        scientific_config_sha256=sha256(CONFIG),science_start_sha256=sha256(start),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_scored=False,
        limitations='Verification updates and worst-shape forward/backward are not scientific teacher budget or model quality. Original gold teachers match CE, but inputs mix5percent predictions and prediction forwards add compute. Different compute; single fixed history-mixing transition; fixed repeated DEV.',
        CPU_closeout_seconds=time.monotonic()-started)
    atomic_json(output,completion)
    paths=[output,start,CONFIG,ROOT/'configs/phase6/base_context_mixing_review.json',Path(c['probe_config']['path']),
        Path(c['proposal']['path']),PROBE/'job.json',PROBE/'result.json',
        ROOT/'reports/phase6/base_context_mixing_trainer_tests.xml',ROOT/'reports/phase6/base_context_mixing_run_tests.xml',
        *[ROOT/name for name in ('scripts/base_context_mixing_trainer.py','scripts/probe_base_context_mixing.py','scripts/probe_base_context_mixing.ps1',
            'scripts/run_base_context_mixing.py','scripts/run_base_context_mixing.ps1','scripts/review_base_context_mixing.py','scripts/complete_base_context_mixing_probe.py',
            'tests/test_base_context_mixing_trainer.py','tests/test_base_context_mixing_run.py','scripts/base_context_mixing_state.py')]]
    manifest=ROOT/'reports/phase6/base_context_mixing_probe_evidence_manifest.json'
    atomic_json(manifest,dict(created_at=now(),files=[dict(path=str(path.relative_to(ROOT)),bytes=path.stat().st_size,sha256=sha256(path)) for path in paths],
        model_checkpoints_in_archive=False,checkpoint_refs=checkpoint_refs))
    archive=ROOT/'reports/phase6/base_context_mixing_probe_evidence.tar.gz'
    with tarfile.open(archive,'w:gz') as target:
        for path in [*paths,manifest]: target.add(path,arcname=str(path.relative_to(ROOT)))
    print(json.dumps(dict(archive_bytes=archive.stat().st_size,archive_sha256=sha256(archive),files=len(paths)+1,
        science_identity={k:science[k] for k in ('pid','boot_id','start_ticks')},snapshot_teachers=science['original_teachers'],Base_complete=False)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
