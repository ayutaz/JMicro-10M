"""Durable fresh FIM10000-update pilot; all verification weights are excluded."""
import argparse
import copy
import json
import math
import os
from pathlib import Path
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from probe_base_fim import PROPOSAL,build,initial_weights_digest,assert_contract
from base_fim_trainer import committed_state
from base_fim_pilot_protocol import DEV_PIN,UPDATES,TEACHERS,validate_body,validate_raw
from evaluate_base_fim_pilot import evaluate
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.tokenizer import Tokenizer
from jmicro.experiment import sha256,now
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json,gpu_lock
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive

CONFIG=ROOT/'configs/phase6/base_fim_pilot_20261015.json'
RUN=ROOT/'reports/phase6/base-fim-pilot-20261015'
PROBE=ROOT/'reports/phase6/base-fim-probe-20261015'
SOURCES=('scripts/run_base_fim_pilot.py','scripts/run_base_fim_pilot.ps1','scripts/review_base_fim_pilot.py',
    'scripts/evaluate_base_fim_pilot.py','scripts/base_fim_pilot_protocol.py','tests/test_base_fim_pilot.py',
    'scripts/base_fim_sampler.py','scripts/base_fim_trainer.py','scripts/probe_base_fim.py',
    'scripts/isolated_base_evaluation.py','src/jmicro/evaluation_boundary.py','src/jmicro/fim_compatibility.py',
    'src/jmicro/model.py','src/jmicro/tokenizer.py','src/jmicro/training.py','src/jmicro/shards.py',
    'src/jmicro/readiness.py','scripts/base_kv_allocation_trainer.py','scripts/base_parallel_residual_trainer.py',
    'scripts/base_parallel_residual_model.py','scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py','uv.lock')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def budget(probe):
    times=probe['all32_timing_seconds'];elapsed=probe['GPU_occupancy_seconds']
    if (len(times)!=32 or any(not math.isfinite(t) or t<=0 for t in times)
            or not 0<elapsed<=120 or probe['passed']is not True
            or probe['all_state_and_history_resume_equal']is not True):raise ValueError('Owned actual CUDA measurements required')
    forecast=math.ceil(UPDATES/32*sum(times)*1.3+600)
    if forecast!=probe['science_forecast_seconds'] or forecast+elapsed>3600 or not probe['science_budget_eligible']:
        raise ValueError('Frozen FIM pilot forecast exceeds3600s; no cap rescue')
    return forecast


def binding(pin,c):
    return dict(config_sha256=pin,proposal_sha256=c['proposal']['sha256'],
        source_binding=c['source_binding'],weights_role='scientific_fresh_FIM_pilot',
        training_seed=42,learned_parent_weights_used=False,probe_weights_used=False)


def matched(control,candidate):
    fields=('update','supervised_tokens','source_teachers','source_EOS','original_body_bytes')
    checks={k:equal_state(control['counters'][k],candidate['counters'][k]) for k in fields}
    a,b=control['sampler'],candidate['sampler']
    checks['full_original_sampler']=all(equal_state(a[k],b[k]) for k in a if k!='kind')
    checks['original_input_and_gold_stream_digest']=control['counters']['token_digest']==b['FIM_counters']['native_stream_digest']
    checks['same_actual_scheduler']=equal_state(control['scheduler'],candidate['scheduler'])
    checks['native_model_config']=control['model_config']==candidate['model_config']
    checks['actual_FIM_active']=b['FIM_counters']['applied_rows']>0
    return checks


def inspect():
    c=json.loads(CONFIG.read_text());p=json.loads(PROPOSAL.read_text());assert_contract(p)
    if (c['kind']!='fresh_FIM_scientific_pilot_v1' or c['updates']!=UPDATES or c['teachers']!=TEACHERS
            or c['total_GPU_cap_seconds']!=3600 or c['scientific_GPU_cap_seconds']!=budget(json.loads(Path(c['probe']['path']).read_text()))
            or c['DEV_manifest']['sha256']!=DEV_PIN or c['TEST_prepared']is not False
            or c['Base_adopted']is not False):raise ValueError('Exact frozen pilot scope required')
    for key in ('proposal','probe','probe_config','CPU_tests','base_config','control_checkpoint','control_evaluation','control_notes'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen pilot reference differs: '+key)
    for path,pin in c['sources'].items():
        if sha256(ROOT/path)!=pin:raise ValueError('Frozen pilot source changed: '+path)
    load_dev_suite(Path(c['DEV_manifest']['path']),DEV_PIN)
    job_path=RUN/'job.json'
    if (RUN/'result.json').exists():raise ValueError('Finished pilot cannot be relaunched')
    if job_path.exists():
        job=json.loads(job_path.read_text())
        if alive(job):raise ValueError('Pilot is currently live; observe same process')
        if job['status']!='interrupted' or not job['cumulative_GPU_ledger_closed']:
            raise ValueError('Resume only valid interrupted checkpoint with closed cumulative ledger')
        if job['GPU_occupancy_seconds']>=c['scientific_GPU_cap_seconds']:
            raise ValueError('Frozen cumulative science budget exhausted; no resume or cap expansion')
    return c,p


def freeze():
    if os.environ.get('CUDA_VISIBLE_DEVICES')!='':raise ValueError('Freeze is CPU-only')
    if CONFIG.exists() or (RUN/'job.json').exists():raise ValueError('Do not refreeze a pilot')
    p=json.loads(PROPOSAL.read_text());assert_contract(p)
    probe=json.loads((PROBE/'result.json').read_text());job=json.loads((PROBE/'job.json').read_text())
    if job['status']!='complete' or alive(job) or not job['cumulative_GPU_ledger_closed']:
        raise ValueError('Owned CUDA probe must actually end before science')
    probe_config=ROOT/'configs/phase6/base_fim_probe_20261015.json'
    old_probe=json.loads(probe_config.read_text())
    for name,pin in old_probe['sources'].items():
        if sha256(ROOT/name)!=pin:raise ValueError('CUDA-tested source changed: '+name)
    from probe_base_fim import passed_tests
    tests=ROOT/'reports/phase6/fim-feasibility-20261015/CPU_pilot_tests.xml';passed_tests(tests,13)
    base_path=ROOT/'configs/phase6/base_parallel_residual_comparison.json';base=json.loads(base_path.read_text())
    suite=load_dev_suite(ROOT/'eval/isolated-base-dev-v1/base.dev.manifest.json',DEV_PIN)
    control=json.loads(Path(p['matched_control']['evaluation']['path']).read_text())
    validate_body(control['body']);validate_raw(control['outputs'],Tokenizer(ROOT/p['tokenizer']['path']),suite)
    if [(r['id'],r['prefix']) for r in control['outputs']]!=[(r['id'],r['prefix']) for r in suite.cases]:
        raise ValueError('Historical DEV requests differ')
    c=dict(kind='fresh_FIM_scientific_pilot_v1',proposal=ref(PROPOSAL),probe=ref(PROBE/'result.json'),
        probe_config=ref(probe_config),CPU_tests=ref(tests),base_config=ref(base_path),
        control_checkpoint=p['matched_control']['checkpoint'],control_evaluation=p['matched_control']['evaluation'],
        control_notes=p['matched_control']['notes'],source_binding=p['source_binding'],
        DEV_manifest=dict(path=str(ROOT/'eval/isolated-base-dev-v1/base.dev.manifest.json'),sha256=DEV_PIN),
        DEV_shards=dict(path=base['dev_shards'],manifest_sha256=base['dev_manifest_sha256']),
        initial_weights_sha256=old_probe['initial_weights_sha256'],updates=UPDATES,teachers=TEACHERS,
        scientific_GPU_cap_seconds=budget(probe),probe_GPU_seconds=probe['GPU_occupancy_seconds'],
        total_GPU_cap_seconds=3600,sources={s:sha256(ROOT/s) for s in SOURCES},
        evaluation_scope='sameDEV256_472055bytes_and_isolated80greedy64_only',
        TEST_prepared=False,Base_adopted=False,quality_criteria_unchanged=True,created_at=now())
    atomic_json(CONFIG,c);inspect()
    print('Frozen exact fresh FIM pilot; no scientific training during freeze',flush=True)


def run():
    c,p=inspect();pin=sha256(CONFIG);b=binding(pin,c)
    RUN.mkdir(parents=True,exist_ok=True);path=RUN/'job.json'
    prior=json.loads(path.read_text())['GPU_occupancy_seconds'] if path.exists() else 0
    job=dict(status='starting',**identity(),config_sha256=pin,started_at=now(),GPU_occupancy_seconds=prior,
        cumulative_GPU_ledger_closed=False,binding=b,new_scientific_teacher_positions=0)
    atomic_json(path,job);started=None;t=None;log=None
    def check(*args):
        if args or (started is not None and prior+time.monotonic()-started>c['scientific_GPU_cap_seconds']):
            raise TimeoutError('Frozen FIM pilot ceiling/interruption; retain valid checkpoint and ledger')
    def beat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=prior+time.monotonic()-started,**extra)
        atomic_json(path,job)
    def save():
        checkpoint=RUN/f"checkpoint-{t.counters['update']:08d}.pt";t.save(checkpoint)
        latest=dict(path=str(checkpoint),sha256=sha256(checkpoint),update=t.counters['update'],binding=b)
        atomic_json(RUN/'latest.json',latest);return latest
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGTERM,check);signal.signal(signal.SIGINT,check)
            configure_resident_memory(17791499264);job['status']='running'
            t=build(p,'cuda',b)
            if (RUN/'latest.json').exists():
                latest=json.loads((RUN/'latest.json').read_text())
                if latest['binding']!=b or sha256(Path(latest['path']))!=latest['sha256']:raise ValueError('Valid same-condition checkpoint required')
                t.load(latest['path'])
                # Remove only uncommitted suffix metrics, preserving them separately.
                rows=[json.loads(line) for line in (RUN/'metrics.jsonl').read_text().splitlines()]
                kept=[r for r in rows if r['update']<=t.counters['update']]
                if len(kept)!=t.counters['update']:raise ValueError('All completed-update metrics required')
                if len(rows)!=len(kept):
                    atomic_json(RUN/f"uncommitted-metrics-{job['pid']}.json",dict(rows=rows[len(kept):]))
                    job['discarded_completed_teacher_exposure']=sum(r['CE_targets_this_update'] for r in rows[len(kept):])
                    (RUN/'metrics.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in kept))
            else:
                if initial_weights_digest(t.state_dict())!=c['initial_weights_sha256']:
                    raise ValueError('Science must start from exact fresh native weights, never probe')
                save()
            log=(RUN/'metrics.jsonl').open('a',buffering=1)
            while t.counters['update']<UPDATES:
                check();row=t.step();log.write(json.dumps(row)+'\n')
                if row['update']%2000==0:save()
                if row['update']%25==0:beat('learning',new_scientific_teacher_positions=row['supervised_tokens'],update=row['update'])
            log.close();log=None;latest=save();state=host(t.state_dict())
            control=torch.load(c['control_checkpoint']['path'],map_location='cpu',weights_only=False)
            checks=matched(control,state)
            if not all(checks.values()) or state['counters']['supervised_tokens']!=TEACHERS:
                raise ValueError('Terminal original stream/control/teacher scope differs')
            record=dict(status='complete',checkpoint=latest['path'],checkpoint_sha256=latest['sha256'],binding=b,
                counters=state['counters'],FIM_counters=state['sampler']['FIM_counters'],matched_checks=checks,
                model_config=state['model_config'],spec=state['spec'],lineage=state['lineage'])
            atomic_json(RUN/'training.json',record);beat('evaluation')
            ev=evaluate(t,c,record,RUN/'evaluation',beat,check)
            check();elapsed=prior+time.monotonic()-started
            result=dict(status='complete',config_sha256=pin,binding=b,actual_identity=identity(),training=record,
                evaluation=ev,scientific_teacher_positions=TEACHERS,GPU_occupancy_seconds=elapsed,
                total_GPU_seconds_including_probe=elapsed+c['probe_GPU_seconds'],
                content_review_completed=False,Base_adopted=False,TEST_opened=False)
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed,cumulative_GPU_ledger_closed=True,
                result_sha256=sha256(RUN/'result.json'),update=UPDATES,new_scientific_teacher_positions=TEACHERS)
            atomic_json(path,job);print('Fresh FIM pilot learning/evaluation complete; all80 review pending',flush=True)
    except BaseException as e:
        if log is not None:log.close()
        if t is not None and not t._step_in_progress:
            try:
                if committed_state(t.state_dict()):save()
            except Exception:pass
        elapsed=prior+(time.monotonic()-started if started is not None else 0)
        job.update(status='interrupted',error=repr(e),ended_at=now(),GPU_occupancy_seconds=elapsed,cumulative_GPU_ledger_closed=True)
        atomic_json(path,job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=('freeze','inspect','run'));a=parser.parse_args()
    if a.action=='freeze':freeze()
    elif a.action=='inspect':inspect();print('Frozen FIM pilot inspected; GPU0')
    else:run()
