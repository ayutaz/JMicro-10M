"""Preserve one ended, ineligible compiler condition without inventing gates."""
import gzip
import io
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from probe_base_native_teacher_KD_compile import CONFIG,RUN,REF_KEYS


def main():
    report=ROOT/'reports/phase6'
    output=report/'base_native_teacher_KD_compile_completion.json'
    if output.exists():raise ValueError('Keep original one-shot compiler closeout')
    c,j=read_json(CONFIG),read_json(RUN/'job.json')
    if alive(j) or j['status'] not in ('failed','complete'):
        raise ValueError('Ended actual compiler process required')
    if j['config_sha256']!=sha256(CONFIG):raise ValueError('Actual config binding differs')
    for p,digest in c['source_sha256'].items():
        if sha256(ROOT/p)!=digest:raise ValueError('Frozen source changed: '+p)
    for key in REF_KEYS:
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen reference changed: '+key)
    def optional(name):
        path=RUN/name
        return read_json(path) if path.exists() else None
    r=optional('result.json')
    if r is not None and r['science_budget_eligible']:
        raise ValueError('Eligible condition requires science followup, not negative closeout')
    if (ROOT/'configs/phase6/base_native_teacher_KD_comparison.json').exists():
        raise ValueError('Ineligible condition cannot start science')
    numeric=optional('numeric_checks.json')
    ui=read_json(ROOT/'reports/local/webui/server.json')
    if not alive(ui):raise ValueError('Restored original UI actual process required')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        model=json.load(response)
    # Preserve actual endpoint data, rather than guessing the current API schema.
    if c['parent']['sha256'] not in json.dumps(model) or '10000007168' not in json.dumps(model):
        raise ValueError('Original ten-billion checkpoint UI binding required')
    consumed=j['GPU_occupancy_seconds']
    result=dict(created_at=now(),status='native_KD_compiler_condition_closed_no_science',
        actual_identity={k:j[k] for k in ('pid','boot_id','start_ticks')},actual_process_ended=True,
        config_sha256=sha256(CONFIG),actual_terminal_status=j['status'],terminal_stage=j['stage'],
        error=j.get('error'),prior_probe_GPU_seconds=c['prior_probe_GPU_seconds'],
        cumulative_probe_GPU_seconds=consumed,additional_compiler_probe_wall_seconds=consumed-c['prior_probe_GPU_seconds'],
        prospective_probe_cap_seconds=180,prospective_total_GPU_cap_seconds=3600,
        cap_exceeded=consumed>180,all_compilation_and_failed_work_counted=True,
        numeric_checks=numeric,completed_numeric_sources=list(numeric or {}),
        resume_checks=optional('resume_checks.json'),capacity=optional('capacity.json'),
        initial_checks=optional('initial_checks.json'),compiled_result=r,
        hidden_invocations=optional('hidden_invocations.json'),compiler_statistics=optional('compiler_statistics.json'),
        missing_gates_not_treated_as_pass=True,science_budget_eligible=False,science_started=False,
        scientific_gold_positions=0,scientific_distribution_positions=0,new_data_tokens=0,
        new_generation_quality_evaluations=0,probe_weights_used_for_science=False,
        no_eager_fallback_or_backend_mode_shape_batch_dtype_cap_sweep=True,
        scope='Compiler implementation/support/numerics/budget condition only; not a new model quality result or proof that native teacher KD cannot help.',
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},model_endpoint=model),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_scored=False,quality_criteria_unchanged=True,
        next_action='Keep this fixed compiler condition closed. Reconcile measured failures and remaining Base hypotheses before selecting a distinct finite learning comparison; do not relaunch compiler tuning or claim Base completion.')
    atomic_json(output,result)
    paths={Path(__file__).resolve(),CONFIG,Path(c['compile_proposal']['path']),Path(c['CPU_tests']['path']),output}
    paths.update(ROOT/p for p in c['source_sha256'] if 'base_native_teacher_KD' in p)
    paths.update(RUN.glob('*.json'))
    target=report/'base_native_teacher_KD_compile_evidence.tar.gz';entries=[]
    with target.open('xb') as stream,gzip.GzipFile(fileobj=stream,mode='wb',mtime=0) as compressed,tarfile.open(fileobj=compressed,mode='w|') as tar:
        for path in sorted(paths):
            data=path.read_bytes();name=path.relative_to(ROOT).as_posix();info=tarfile.TarInfo(name);info.size=len(data);info.mtime=0
            tar.addfile(info,io.BytesIO(data));entries.append(dict(path=name,bytes=len(data),sha256=sha256(path)))
    manifest=dict(created_at=now(),files=entries,text_files=len(entries),text_bytes=sum(x['bytes'] for x in entries),
        archive=dict(path=str(target),bytes=target.stat().st_size,sha256=sha256(target)),tensor_checkpoints_on_WSL=True,Base_complete=False)
    atomic_json(report/'base_native_teacher_KD_compile_evidence_manifest.json',manifest)
    print(json.dumps(dict(status=result['status'],stage=j['stage'],GPU_seconds=consumed,archive=manifest['archive'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
