"""Persist actual middle-supervision CUDA gate and live scientific identity."""
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
import probe_base_middle_supervision as probe
import run_base_middle_supervision as science


def main():
    phase=ROOT/'reports/phase6'
    output=phase/'base_middle_supervision_probe_launch.json'
    bundle=phase/'base_middle_supervision_probe_launch_evidence.tar.gz'
    manifest=phase/'base_middle_supervision_probe_launch_evidence_manifest.json'
    descriptor=phase/'base_middle_supervision_probe_launch_archive.json'
    if any(p.exists() for p in (output,bundle,manifest,descriptor)):
        raise ValueError('Preserve original launch evidence')
    p,result,job=read_json(probe.CONFIG),read_json(probe.RUN/'result.json'),read_json(probe.RUN/'job.json')
    c,live=read_json(science.CONFIG),read_json(science.RUN/'job.json')
    if (alive(job) or job['status']!='complete' or not result['passed'] or not result['science_budget_eligible'] or
        result['config_sha256']!=sha256(probe.CONFIG) or
        result['actual_identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')} or
        not all(result['initial_checks'].values()) or not all(result['all_resume_and_source_checks'].values()) or
        not result['capacity']['unchanged_weights'] or result['capacity']['decoder_forwards']!=1 or
        result['capacity']['original_target_positions']!=result['capacity']['middle_gold_evaluations'] or
        not 0<result['GPU_occupancy_seconds']==job['GPU_occupancy_seconds']<=180 or
        science.science_budget(result)!=c['GPU_budget_seconds']):
        raise ValueError('Actual exited bounded full CUDA/source gate required')
    for name,digest in {**p['source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/name)!=digest: raise ValueError('Verified source changed')
    for record in [*[p[k] for k in ('proposal','CPU_tests','payload','control_CE','control_result')],
                   *[c[k] for k in ('probe_result','probe_job','probe_config','proposal','control_CE','CPU_run_tests')]]:
        if sha256(Path(record['path']))!=record['sha256']: raise ValueError('Actual reference changed')
    policy=ROOT/'configs/phase6/base_middle_supervision_review.json'
    if (not alive(live) or live['status']!='running' or live['stage']!='middle_supervision-training' or
        live['original_teachers']<=0 or live['config_sha256']!=sha256(science.CONFIG) or
        read_json(policy)['config_sha256']!=sha256(science.CONFIG)):
        raise ValueError('Actual live learning scientific identity and fixed quality policy required')
    snapshot=phase/'base_middle_supervision_science_launch_snapshot.json'; atomic_json(snapshot,live)
    record=dict(created_at=now(),status='actual_middle_CUDA_gate_passed_native100M_science_live',
        probe_actual_identity=result['actual_identity'],probe_actual_process_absent=True,
        scientific_actual_identity={k:live[k] for k in ('pid','boot_id','start_ticks')},science_live_at_recording=True,
        scientific_config_sha256=sha256(science.CONFIG),quality_policy_sha256=sha256(policy),
        probe_GPU_seconds=result['GPU_occupancy_seconds'],scientific_GPU_cap_seconds=c['GPU_budget_seconds'],
        total_GPU_cap_seconds=4800,forecast_with_probe=result['GPU_occupancy_seconds']+c['GPU_budget_seconds'],
        initial_checks=result['initial_checks'],resume_and_source_checks=result['all_resume_and_source_checks'],
        capacity=result['capacity'],verification_updates=result['verification_updates'],
        verification_original_teacher_positions=result['verification_original_teacher_positions'],
        verification_middle_gold_evaluations=result['verification_middle_gold_evaluations'],
        all32_step_seconds=result['all32_timing_seconds'],
        median_speed_diagnostic_not_forecast=result['median_original_teachers_per_second'],
        exact_planned_completed_updates=17698,scientific_original_teacher_positions=100000000,
        scientific_middle_gold_evaluations=100000000,
        snapshot=dict(path=str(snapshot),sha256=sha256(snapshot)),probe_weights_discarded=True,
        new_unique_corpus=0,extra_parameters=0,cached_control_GPU_repeated=False,cached_control_ratings_repeated=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_scored=False,quality_criteria_unchanged=True,
        next_action='Monitor this exact PID/checkpoints, finish original100M and separately counted middle head100M/full state; evaluate Japanese192/331/1119/commonDEV256/native80; individually read and apply unchanged matched/strong/absolute/historicalWeb gates. Qualified candidate only gets independent learnedseed/fullDEV/protected finalTEST/adoption. Notify and stop after Base completion. No duplicate GPU or unrelated research while live.')
    atomic_json(output,record)
    paths={Path(__file__).resolve(),output,snapshot,probe.CONFIG,science.CONFIG,policy,Path(p['proposal']['path'])}
    paths.update(probe.RUN.glob('*.json'))
    paths.update(ROOT/name for name in (*p['source_sha256'],*c['source_sha256']) if 'base_middle_supervision' in name)
    paths.update(phase.glob('base_middle_supervision*tests.xml'))
    entries=[dict(path=path.relative_to(ROOT).as_posix(),bytes=path.stat().st_size,sha256=sha256(path)) for path in sorted(paths)]
    atomic_json(manifest,dict(created_at=now(),files=entries,tensor_or_corpus_included=False,probe_checkpoints_preserved_native=True))
    with tarfile.open(bundle,'x:gz') as archive:
        for path in [*sorted(paths),manifest]: archive.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    archive=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle))
    atomic_json(descriptor,dict(created_at=now(),archive=archive,files=len(paths)+1,Base_complete=False))
    print(json.dumps(dict(status=record['status'],actual_pid=live['pid'],observed_gold=live['original_teachers'],archive=archive)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
