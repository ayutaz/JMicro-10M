"""Close the actual eager KD budget condition after all remaining CUDA gates."""
import gzip
import io
import json
import math
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive

if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
report=ROOT/'reports/phase6';run=report/'base-native-teacher-KD-probe-v2-20261007'
out=report/'base_native_teacher_KD_probe_completion.json'
if out.exists():raise ValueError('Existing eager KD closeout retained')
cpath=ROOT/'configs/phase6/base_native_teacher_KD_probe_v2.json';c=read_json(cpath)
j,r=read_json(run/'job.json'),read_json(run/'result.json')
if alive(j) or j['status']!='complete' or r['status']!='complete' or not r['passed'] or r['science_budget_eligible']:
    raise ValueError('Actual exited verified-but-over-budget eager KD result required')
if not all(r['initial_checks'].values()) or not all(r['all_resume_and_source_checks'].values()):raise ValueError('All recorded CUDA gates required')
if r['config_sha256']!=sha256(cpath) or j['config_sha256']!=r['config_sha256']:raise ValueError('Actual source config binding required')
if r['science_budget_seconds']!=math.ceil(100000000/r['median_original_teachers_per_second']*1.3+900):raise ValueError('Original measured forecast required')
if r['science_budget_seconds']+r['GPU_occupancy_seconds']<=3600 or not 0<r['GPU_occupancy_seconds']<=180:raise ValueError('Prospective unchanged caps required')
for name,digest in c['source_sha256'].items():
    if sha256(ROOT/name)!=digest:raise ValueError('Frozen corrected source changed')
for key in ('proposal','CPU_tests','payload','control_CE','control_result','previous_config','previous_job','previous_timings'):
    if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen prior/current evidence changed')
if (ROOT/'configs/phase6/base_native_teacher_KD_comparison.json').exists():raise ValueError('Over-budget condition cannot be frozen as science')
old=read_json(Path(c['previous_job']['path']))
if alive(old) or old['status']!='failed' or old['GPU_occupancy_seconds']!=c['prior_probe_GPU_seconds']:raise ValueError('Preserved actual first failure required')
ui=read_json(ROOT/'reports/local/webui/server.json')
if not alive(ui):raise ValueError('Actual restored original WebUI required')
result=dict(created_at=now(),status='eager_native_teacher_KD_CUDA_gate_passed_scientific_budget_condition_closed',
    actual_identity=r['actual_identity'],actual_process_ended=True,config_sha256=sha256(cpath),result_sha256=sha256(run/'result.json'),
    cumulative_probe_GPU_seconds=r['GPU_occupancy_seconds'],prior_failed_probe_GPU_seconds=r['prior_probe_GPU_seconds'],
    additional_corrected_probe_GPU_seconds=r['additional_probe_GPU_seconds'],
    median_original_gold_positions_per_second=r['median_original_teachers_per_second'],
    scientific_forecast_seconds=r['science_budget_seconds'],total_forecast_including_probe=r['science_budget_seconds']+r['GPU_occupancy_seconds'],
    prospective_total_GPU_cap_seconds=3600,prospective_probe_cap_seconds=180,science_budget_eligible=False,
    verification_updates=r['verification_updates'],verification_original_gold_positions=r['verification_original_teacher_positions'],
    verification_distribution_target_positions=r['verification_KD_positions'],capacity=r['capacity'],
    actual_CUDA_checks=r['all_resume_and_source_checks'],initial_and_immutable_teacher_checks=r['initial_checks'],
    original_timing_teacher_equality_bool_not_persisted=True,
    correction='JSON reader accepts Path, not string. Preserve failed original script/config/job/35 histories, cast existing cached payload string to Path in V2, reuse all35 original timings without rerun, count original7.3496477s under unchanged total caps. Remaining stress/resume/control gates completed, no source/teacher/objective/seed/batch/shape/cap changes.',
    science_started=False,scientific_gold_positions=0,scientific_distribution_positions=0,new_data_tokens=0,
    optimizer_policy='Probe updates only, discarded; no scientific optimizer checkpoint',
    UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True),
    Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False,
    quality_criteria_unchanged=True,
    next_action='Keep eager science condition closed. One separately frozen implementation-performance check may compile the same native hidden forward at dynamic original shapes. Same teacher/targets/loss/seed/batch/physical grouping, same total3600/probe180 caps including previous12.282s; compilation cost and actual fullstate/source/memory/speed required before any new science. No algorithm/cap/shape rescue or claim of quality failure.')
atomic_json(out,result)
paths={Path(__file__).resolve(),ROOT/'configs/phase6/base_native_teacher_KD_probe.json',cpath}
paths.update(report.glob('base_native_teacher_KD*.json'));paths.update(report.glob('base_native_teacher_KD*.xml'))
paths.update((ROOT/'scripts').glob('*base_native_teacher_KD*.py'));paths.update((ROOT/'scripts').glob('*base_native_teacher_KD*.ps1'))
paths.update((ROOT/'tests').glob('*base_native_teacher_KD*.py'))
for folder in ('base-native-teacher-KD-probe-20261007','base-native-teacher-KD-probe-v2-20261007'):
    paths.update((report/folder).glob('*.json'))
target=report/'base_native_teacher_KD_probe_evidence.tar.gz';entries=[]
with target.open('xb') as stream,gzip.GzipFile(fileobj=stream,mode='wb',mtime=0) as compressed,tarfile.open(fileobj=compressed,mode='w|') as tar:
    for path in sorted(paths):
        data=path.read_bytes();name=path.relative_to(ROOT).as_posix();info=tarfile.TarInfo(name);info.size=len(data);info.mtime=0
        tar.addfile(info,io.BytesIO(data));entries.append(dict(path=name,bytes=len(data),sha256=sha256(path)))
manifest=dict(created_at=now(),files=entries,text_files=len(entries),text_bytes=sum(x['bytes'] for x in entries),
    archive=dict(path=str(target),bytes=target.stat().st_size,sha256=sha256(target)),tensor_checkpoints_on_WSL=True,Base_complete=False)
atomic_json(report/'base_native_teacher_KD_probe_evidence_manifest.json',manifest)
print(json.dumps(dict(status=result['status'],GPU_seconds=r['GPU_occupancy_seconds'],forecast_total_seconds=result['total_forecast_including_probe'],archive=manifest['archive'])))
