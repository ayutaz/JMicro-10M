"""Durable original25M RDrop candidate versus accepted native25M; TEST unopened."""
import argparse
import json
import os
from pathlib import Path
from urllib.request import urlopen
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
import torch
from probe_document_progress import GOALS
SCIENCE_TEST_COUNT = 35
from jmicro.experiment import sha256, now
from jmicro.training import atomic_json, gpu_lock
from jmicro.tokenizer import Tokenizer
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.evaluation_choice_boundary import load_choices
from jmicro.isolated_japanese_scoring import load_unigram
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from rdrop_target_batch_trainer import TargetBatchRDropTrainer,committed_state
from jmicro.rdrop import POLICY as RECIPE
from document_progress_trainer import committed_state as control_committed
from rdrop_science_protocol import science_budget, matched_original, validate_history, paired_history
from evaluate_context_likelihood import evaluate
from phase6_performance import identity, alive
from probe_context_likelihood import weights_digest, passed_tests

RUN = ROOT / 'reports/phase6/rdrop-science-20261016'
CONFIG = ROOT / 'configs/phase6/rdrop_science_20261016.json'
PROBE = ROOT / 'reports/phase6/rdrop-target-batch-probe-20261015'
PREP = ROOT / 'reports/phase6/rdrop-science-preparation-20261016'
SOURCES = ('scripts/run_rdrop_science.py', 'scripts/run_rdrop_science.ps1',
    'scripts/review_rdrop_science.py', 'scripts/evaluate_context_likelihood.py',
    'scripts/rdrop_science_protocol.py', 'tests/test_rdrop_science.py',
    'scripts/pseudo_repetition_science_protocol.py',
    'src/jmicro/isolated_japanese_scoring.py', 'src/jmicro/evaluation_choice_boundary.py',
    'src/jmicro/evaluation_boundary.py', 'src/jmicro/evaluation_memory.py',
    'src/jmicro/japanese_evaluation.py', 'src/jmicro/readiness.py', 'src/jmicro/shards.py',
    'scripts/isolated_base_evaluation.py', 'scripts/base_fim_pilot_protocol.py',
    'scripts/review_matched_story_study.py', 'scripts/run_eos_complete_100m.py')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def binding(c, pin):
    return dict(config_sha256=pin, parent=c['parent'], source_binding=c['source_binding'],
                training_seed=42, weights_role='scientific_rdrop_target_batch25M', probe_weights_used=False)


def build(c, b):
    parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
    codec = Tokenizer(c['tokenizer']['path'])
    source = c['source_binding']
    sampler = OriginalTrainCorpusSampler(source['pool'], source['manifest_sha256'], codec, c['goals'], seed=42)
    if sampler.binding != source:
        raise ValueError('Accepted original TRAIN identity differs')
    return TargetBatchRDropTrainer(parent, sampler, b, batch=48, device='cuda', seed=42)


def freeze():
    if CONFIG.exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve frozen/started new scientific condition')
    authorization_path = PREP/'authorization.json'
    authorization = json.loads(authorization_path.read_text())
    probe = json.loads((PROBE/'result.json').read_text())
    completion = json.loads((PROBE/'completion.json').read_text())
    job = json.loads((PROBE/'job.json').read_text())
    if job['status'] != 'complete' or alive(job) or completion['new_scientific_teachers'] != 0:
        raise ValueError('Only exited technical proof with no scientific learning may be reused')
    if completion['ALL32_non_time_history_exact_to_stored_prior'] is not True:
        raise ValueError('Stored ALL32 original histories required')
    budget = science_budget(probe,authorization)
    pc = ROOT/'configs/phase6/rdrop_target_batch_probe_20261015.json'
    p = json.loads(pc.read_text())
    if probe['config_sha256'] != sha256(pc):
        raise ValueError('Original technical contract changed')
    for path,pin in p['sources'].items():
        if sha256(ROOT/path) != pin:
            raise ValueError('CUDA-verified numerical source changed: '+path)
    workflow = PREP/'science_CPU_tests.xml'
    passed_tests(workflow,SCIENCE_TEST_COUNT)
    template_path = ROOT/'configs/phase6/scalegrad_science_20261015.json'
    template = json.loads(template_path.read_text())
    cp = Path(template['control_checkpoint']['path'])
    stat = cp.stat()
    if stat.st_size != template['control_checkpoint_size'] or stat.st_mtime_ns != template['control_checkpoint_mtime_ns']:
        raise ValueError('Accepted full native25M control identity changed')
    control = torch.load(cp,map_location='cpu',weights_only=False)
    if (not control_committed(control) or control['spec']['progress_arm'] != 'native_CE_control'
            or control['counters']['supervised_tokens'] != 25000000
            or torch.count_nonzero(control['progress_head']['weight'])):
        raise ValueError('Actual matched native25M control required, never initializer')
    c = dict(template,kind='frozen_native_original25M_RDrop_science_v1',created_at=now(),
        proposal=ref(PREP/'proposal.json'),resource_authorization=ref(authorization_path),
        evaluation_template=ref(template_path),probe_config=ref(pc),probe_result=ref(PROBE/'result.json'),
        probe_completion=ref(PROBE/'completion.json'),recipe=RECIPE,
        initial_weights_sha256=probe['initial_native_weights_sha256'],
        scientific_GPU_cap_seconds=budget,total_GPU_cap_seconds=None,
        technical_GPU_seconds=authorization['prior_technical_GPU_seconds'],
        carried_total_GPU_seconds=authorization['prior_total_GPU_seconds'],
        carried_completed_science_GPU_seconds=authorization['prior_completed_science_GPU_seconds'],
        worst_measured_peak_bytes=probe['capacity']['peak_VRAM_bytes'],
        sources={**template['sources'],**p['sources'],**{path:sha256(ROOT/path) for path in SOURCES}},
        CPU_workflow_tests=ref(workflow),
        comparison_RNG='Dropout advances training RNG; original material/schedule match, within-arm resume exact.',
        scope='First RDrop scientific25M under explicit new resource authorization; not a completed pilot/probe relaunch. All original Base stages pending.',
        failure='Close on numerical/resource/quality failure; no coefficient/teachers/decoder/quality rescue or per-run extension.')
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='RDrop25M_science_frozen_not_started',science_GPU_seconds=budget,
        ALL_carried_seconds=c['carried_total_GPU_seconds'],global_cap=None)),flush=True)


def inspect():
    c = json.loads(CONFIG.read_text())
    if (c['kind'] != 'frozen_native_original25M_RDrop_science_v1' or c['recipe'] != RECIPE
            or c['batch'] != 48 or c['seed'] != 42 or c['goals'] != GOALS or c['main_teacher_goal'] != 25000000
            or c['native_parameters'] != 10001152 or c['training_parameters'] != 10001152 or c['train_only_parameters'] != 0
            or c['TEST_prepared'] is not False or c['Base_adopted'] is not False
            or c['quality_criteria_unchanged'] is not True or c['total_GPU_cap_seconds'] is not None):
        raise ValueError('Exact original RDrop25M scope and explicit unlimited cumulative authorization required')
    for path,pin in c['sources'].items():
        if sha256(ROOT/path) != pin:
            raise ValueError('Frozen source changed: '+path)
    for key in ('proposal','resource_authorization','evaluation_template','probe_config','probe_result','probe_completion',
                'tokenizer','CPU_workflow_tests','control_training','control_result','control_metrics','control_raw','control_notes'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Frozen evidence changed: '+key)
    passed_tests(c['CPU_workflow_tests']['path'],SCIENCE_TEST_COUNT)
    auth = json.loads(Path(c['resource_authorization']['path']).read_text())
    if (science_budget(json.loads(Path(c['probe_result']['path']).read_text()),auth) != c['scientific_GPU_cap_seconds']
            or c['carried_total_GPU_seconds'] != auth['prior_total_GPU_seconds']
            or c['technical_GPU_seconds'] != auth['prior_technical_GPU_seconds']
            or c['carried_completed_science_GPU_seconds'] != auth['prior_completed_science_GPU_seconds']):
        raise ValueError('Original measured per-run cap and ALL latest carried costs required')
    for key in ('parent','control_checkpoint'):
        stat = Path(c[key]['path']).stat()
        if stat.st_size != c[key+'_size'] or stat.st_mtime_ns != c[key+'_mtime_ns']:
            raise ValueError('Accepted numerical state identity changed')
    for row in c['references'].values():
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Original baseline reference changed')
    load_dev_suite(c['DEV_manifest']['path'],c['DEV_manifest']['sha256'])
    if (RUN/'job.json').exists():
        job = json.loads((RUN/'job.json').read_text())
        if (alive(job) or job['status'] != 'interrupted' or not job['cumulative_GPU_ledger_closed']
                or job['config_sha256'] != sha256(CONFIG) or job['GPU_occupancy_seconds'] >= c['scientific_GPU_cap_seconds']):
            raise ValueError('Only valid signal interruption under same remaining per-run budget may resume')
    return c

def observe_ui():
    saved = json.loads((ROOT/'reports/local/webui/server.json').read_text())
    if not alive(saved):
        raise ValueError('Original UI is not actually alive')
    with urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:
        ui = json.load(response)
    if (ui['busy'] or ui['parameters'] != 10001152
            or ui['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or ui['tokenizer_sha256'] != 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'):
        raise ValueError('Original idle native parent/Tokenizer HTTP required')
    stat = (Path(os.environ.get('JMICRO_DATA_ROOT',str(Path.home()/'jmicro-data')))/'gpu.lock').stat()
    inode = f'{os.major(stat.st_dev):02x}:{os.minor(stat.st_dev):02x}:{stat.st_ino}'
    rows = [r for r in Path('/proc/locks').read_text().splitlines()
        if inode in r and 'FLOCK' in r and f'WRITE {saved["pid"]} ' in r]
    if len(rows) != 1:
        raise ValueError('Actual original UI kernel FLOCK required')
    out = dict(observed_at=now(),identity=identity(saved['pid']),HTTP=ui,actual_lock_inode=inode,kernel_FLOCK=rows)
    atomic_json(ROOT/'reports/phase6/rdrop-science-launcher-20261016/UI_observation.json',out)
    return out


class StopRequested(Exception):
    pass


def run():
    c = inspect()
    pin = sha256(CONFIG)
    b = binding(c, pin)
    RUN.mkdir(parents=True, exist_ok=True)
    previous = json.loads((RUN / 'job.json').read_text()) if (RUN / 'job.json').exists() else None
    prior = previous['GPU_occupancy_seconds'] if previous else 0
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=pin, binding=b,
        GPU_occupancy_seconds=prior, cumulative_GPU_ledger_closed=False, update=0, main_teacher_positions=0)
    atomic_json(RUN / 'job.json', job)
    started = None
    trainer = log = None
    def check():
        if started is not None and prior + time.monotonic() - started > c['scientific_GPU_cap_seconds']:
            raise TimeoutError('Frozen scientific GPU budget exhausted; no extension')
    def stop(*args):
        raise StopRequested('External signal; preserve completed-update state and exact budget')
    def beat(stage, **extra):
        check()
        job.update(stage=stage, heartbeat_at=now(), GPU_occupancy_seconds=prior + time.monotonic() - started, **extra)
        atomic_json(RUN / 'job.json', job)
    def save():
        path = RUN / f"checkpoint-{trainer.counters['update']:08d}.pt"
        trainer.save(path)
        latest = dict(path=str(path), sha256=sha256(path), binding=b, update=trainer.counters['update'])
        atomic_json(RUN / 'latest.json', latest)
        return latest
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM, stop)
            signal.signal(signal.SIGINT, stop)
            configure_resident_memory(c['worst_measured_peak_bytes'])
            job['status'] = 'running'
            trainer = build(c, b)
            metrics = RUN / 'metrics.jsonl'
            if (RUN / 'latest.json').exists():
                latest = json.loads((RUN / 'latest.json').read_text())
                if latest['binding'] != b or sha256(Path(latest['path'])) != latest['sha256']:
                    raise ValueError('Frozen valid checkpoint required')
                trainer.load(latest['path'])
                rows = [json.loads(line) for line in metrics.read_text().splitlines()] if metrics.exists() else []
                retained = [r for r in rows if r['update'] <= trainer.counters['update']]
                validate_history(retained, trainer.state_dict())
                if len(retained) != len(rows):
                    atomic_json(RUN / f"discarded-post-checkpoint-metrics-{job['pid']}.json", dict(rows=rows[len(retained):]))
                    metrics.write_text(''.join(json.dumps(row) + '\n' for row in retained))
            else:
                if previous or weights_digest(trainer.state_dict()) != c['initial_weights_sha256']:
                    raise ValueError('Science starts only from original parent, never verification weights')
                save()
            log = metrics.open('a', buffering=1)
            while not trainer.sampler.exhausted:
                check()
                row = trainer.step()
                log.write(json.dumps(row) + '\n')
                if row['update'] % 500 == 0:
                    save()
                if row['update'] % 20 == 0:
                    beat('learning', update=row['update'], main_teacher_positions=row['supervised_tokens'])
            log.close()
            log = None
            latest = save()
            state = host(trainer.state_dict())
            rows = [json.loads(line) for line in metrics.read_text().splitlines()]
            physical = validate_history(rows, state)
            control = torch.load(c['control_checkpoint']['path'], map_location='cpu', weights_only=False)
            checks = matched_original(state,control)
            paired_history(rows,[json.loads(line) for line in Path(c['control_metrics']['path']).read_text().splitlines()])
            if not all(checks.values()) or state['counters']['supervised_tokens'] != 25000000:
                raise ValueError('Terminal exact original25M/control stream differs')
            record = dict(status='complete', checkpoint=latest['path'], checkpoint_sha256=latest['sha256'], binding=b,
                counters=state['counters'], original_CE_match=checks, physical_rollup=physical,
                auxiliary_digest=state['counters']['auxiliary_digest'],
                model_config=state['model_config'], spec=state['spec'], lineage=state['lineage'])
            atomic_json(RUN / 'training.json', record)
            beat('evaluation')
            ev = evaluate(trainer, c, record, RUN / 'evaluation', beat, check)
            check()
            elapsed = prior + time.monotonic() - started
            result = dict(status='complete', config_sha256=pin, binding=b, actual_identity=identity(),
                training=record, evaluation=ev, scientific_CE_teacher_positions=25000000,
                GPU_occupancy_seconds=elapsed, cumulative_total_GPU_seconds=elapsed + c['carried_total_GPU_seconds'],
                content_review_completed=False, TEST_opened=False, Base_qualified=False, Base_adopted=False)
            atomic_json(RUN / 'result.json', result)
            job.update(status='complete', ended_at=now(), GPU_occupancy_seconds=elapsed,
                       cumulative_GPU_ledger_closed=True, update=trainer.counters['update'], main_teacher_positions=25000000,
                       cumulative_total_GPU_seconds=elapsed+c['carried_total_GPU_seconds'])
            atomic_json(RUN / 'job.json', job)
            print('Original25M learning/isolated evaluation complete; all80 content review pending', flush=True)
    except BaseException as error:
        if log is not None:
            log.close()
        if trainer is not None and not trainer._step_in_progress:
            try:
                save()
            except Exception:
                pass
        elapsed = prior + (time.monotonic() - started if started is not None else 0)
        job.update(status='interrupted' if isinstance(error, StopRequested) else 'failed',
            error_type=type(error).__name__, error=str(error), ended_at=now(), GPU_occupancy_seconds=elapsed,
            cumulative_GPU_ledger_closed=True,cumulative_total_GPU_seconds=elapsed+c['carried_total_GPU_seconds'])
        atomic_json(RUN / 'job.json', job)
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('freeze','inspect','observe-ui','run'))
    args = parser.parse_args()
    if args.action == 'freeze':
        freeze()
    elif args.action == 'inspect':
        inspect()
        print('Frozen scientific preflight passed; no GPU')
    elif args.action == 'observe-ui':
        inspect()
        print(json.dumps(observe_ui()),flush=True)
    else:
        run()
