"""Preserve actual ended probe evidence and a live scientific launch snapshot."""
import gzip
import io
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import probe_base_on_policy_teacher as probe
import run_base_on_policy_teacher as science

if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
report=ROOT/'reports/phase6';out=report/'base_on_policy_teacher_probe_launch.json'
if out.exists():raise ValueError('Preserve actual original launch snapshot')
c,p=read_json(probe.CONFIG),read_json(probe.RUN/'result.json');pj=read_json(probe.RUN/'job.json')
if alive(pj) or pj['status']!='complete' or not p['passed'] or not p['science_budget_eligible']:
    raise ValueError('Actual ended eligible on-policy CUDA gate required')
if not all(p['initial_checks'].values()) or not all(p['all_resume_and_source_checks'].values()):
    raise ValueError('Complete actual finite/state/source/teacher gates required')
for name,digest in c['source_sha256'].items():
    if sha256(ROOT/name)!=digest:raise ValueError('Frozen actual probe source changed')
for key in probe.REF_KEYS:
    if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen actual probe refs changed')
sc=read_json(science.CONFIG);job=read_json(science.RUN/'job.json')
for name,digest in sc['source_sha256'].items():
    if sha256(ROOT/name)!=digest:raise ValueError('Frozen scientific implementation changed')
for key in ('probe_result','probe_job','probe_config','proposal','control_CE','CPU_run_tests'):
    if sha256(Path(sc[key]['path']))!=sc[key]['sha256']:raise ValueError('Frozen scientific refs changed')
if (not alive(job) or job['status']!='running' or job['stage']!='on_policy_teacher-training' or
    job['config_sha256']!=sha256(science.CONFIG) or not job['original_teachers']>0):
    raise ValueError('Actual live scientific learning identity/increased teachers required')
if science.science_budget(p)!=sc['GPU_budget_seconds']:raise ValueError('Measured science budget differs')
policy=ROOT/'configs/phase6/base_on_policy_teacher_review.json'
if read_json(policy)['config_sha256']!=sha256(science.CONFIG):raise ValueError('Unchanged scientific quality policy required')
snapshot=report/'base_on_policy_teacher_science_launch_snapshot.json';atomic_json(snapshot,job)
result=dict(created_at=now(),status='actual_on_policy_native_teacher_probe_passed_and_scientific100M_started',
    probe_actual_identity=p['actual_identity'],probe_actual_process_ended=True,probe_config_sha256=sha256(probe.CONFIG),
    scientific_config_sha256=sha256(science.CONFIG),quality_policy_sha256=sha256(policy),
    probe_GPU_seconds=p['GPU_occupancy_seconds'],scientific_budget_seconds=sc['GPU_budget_seconds'],
    total_prospective_GPU_cap_seconds=7200,scientific_forecast_including_probe=sc['GPU_budget_seconds']+p['GPU_occupancy_seconds'],
    actual_CUDA_resume_source_checks=p['all_resume_and_source_checks'],initial_teacher_checks=p['initial_checks'],
    capacity=p['capacity'],verification_updates=p['verification_updates'],
    verification_original_gold_positions=p['verification_original_teacher_positions'],
    verification_distribution_positions=p['verification_distribution_positions'],
    postwarmup_total32_step_seconds=p['postwarmup_total32_step_seconds'],
    actual_scheduled_rollout_step_seconds=p['rollout_step_seconds'],
    nominal_normal_step_median_is_not_the_forecast=True,
    scientific_launch_snapshot=dict(path=str(snapshot),sha256=sha256(snapshot)),
    scientific_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},science_live_at_recording=True,
    probe_weights_discarded=True,new_corpus_tokens=0,cached_control_GPU_repeated=False,cached_control_ratings_repeated=False,
    auxiliary_distribution_positions_not_original_gold=True,
    preparation_failures_preserved='First prospective metadata reference used a nonexistent shortened completion filename and was corrected before saving any proposal. Initial three CPU head-selection assertions rejected target_first0; old proposal and failed XML kept. Corrected existing document-head metadata/target_first1 before any GPU, not quality-driven source or setting selection.',
    prior_closed_gold_prefix_KD_not_restarted=True,prior_compiler_numeric_guard_not_weakened=True,
    Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False,
    quality_criteria_unchanged=True,
    next_action='Monitor this exact actual science identity/checkpoints without duplicate jobs. Complete exact100M/own auxiliary fullstate and allJapanese/commonDEV256/native80, read all80 and apply frozen matched/strong/absolute/historicalWeb gates. No unrelated research while this job is active. Qualified candidate only gets independent learnedseed/fullDEV/protectedTEST/adoption; notify and stop when Base completed.')
atomic_json(out,result)
paths={Path(__file__).resolve(),out,snapshot,probe.CONFIG,science.CONFIG,policy}
paths.update(ROOT/name for name in (*c['source_sha256'],*sc['source_sha256']) if 'base_on_policy_teacher' in name)
paths.update(report.glob('base_on_policy_teacher_proposal*.json'))
paths.update(report.glob('base_on_policy_teacher*tests*.xml'))
paths.update(probe.RUN.glob('*.json'))
paths.update((ROOT/'scripts').glob('define_base_on_policy_teacher*.py'))
target=report/'base_on_policy_teacher_probe_launch_evidence.tar.gz';entries=[]
with target.open('xb') as stream,gzip.GzipFile(fileobj=stream,mode='wb',mtime=0) as compressed,tarfile.open(fileobj=compressed,mode='w|') as tar:
    for path in sorted(paths):
        data=path.read_bytes();name=path.relative_to(ROOT).as_posix();info=tarfile.TarInfo(name);info.size=len(data);info.mtime=0
        tar.addfile(info,io.BytesIO(data));entries.append(dict(path=name,bytes=len(data),sha256=sha256(path)))
manifest=dict(created_at=now(),files=entries,text_files=len(entries),text_bytes=sum(x['bytes'] for x in entries),
    archive=dict(path=str(target),bytes=target.stat().st_size,sha256=sha256(target)),tensor_checkpoints_on_WSL=True,Base_complete=False)
atomic_json(report/'base_on_policy_teacher_probe_launch_evidence_manifest.json',manifest)
print(json.dumps(dict(status=result['status'],actual_science_pid=job['pid'],observed_gold_positions=job['original_teachers'],
    scientific_budget_seconds=sc['GPU_budget_seconds'],archive=manifest['archive'])))
