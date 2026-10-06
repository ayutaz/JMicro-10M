"""Freeze and execute one bounded native CUDA gradient/capacity/resume probe."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, sha256
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json, gpu_lock
from natural_context_contrast_trainer import NaturalContextTrainer, host, KIND, TEMPERATURE, COEFFICIENT
from phase6_performance import identity, alive, finite_state

CONFIG = ROOT/'configs/phase6/natural_context_contrast_probe.json'
RUN = ROOT/'reports/phase6/natural-context-contrast-probe-20261007'
PROPOSAL = ROOT/'reports/phase6/natural_context_contrast_proposal.json'
PREPARATION = ROOT/'reports/phase6/natural_context_contrast_preparation.json'
TESTS = ROOT/'reports/phase6/natural_context_contrast_tests.xml'
SOURCES = ('scripts/natural_context_contrast_trainer.py', 'scripts/probe_natural_context_contrast.py',
    'scripts/probe_natural_context_contrast.ps1', 'tests/test_natural_context_contrast_trainer.py',
    'src/jmicro/model.py', 'src/jmicro/training.py', 'src/jmicro/phase5.py',
    'scripts/phase6_performance.py', 'uv.lock')


def reference(path):
    return dict(path=str(path), sha256=sha256(path))


def prepare():
    if CONFIG.exists():
        raise ValueError('Preserve frozen one-shot protocol; inspect instead of refreezing')
    p = json.loads(PROPOSAL.read_text())
    prep = json.loads(PREPARATION.read_text())
    suites = list(ET.parse(TESTS).getroot().iter('testsuite'))
    if (sum(int(s.attrib['tests']) for s in suites) != 5
            or any(int(s.attrib[k]) for s in suites for k in ('failures', 'errors', 'skipped'))):
        raise ValueError('Five actual protocol CPU checks required')
    if (p['objective']['temperature'] != TEMPERATURE or p['objective']['loss_coefficient'] != COEFFICIENT
            or p['bounded_next_probe']['GPU_seconds_maximum'] != 180
            or prep['sample']['sha256'] != p['fixed_probe_sample_sha256']):
        raise ValueError('Fixed prior objective/inputs/budget required')
    parent_path = ROOT/p['parent_checkpoint']
    if sha256(parent_path) != p['parent_sha256']:
        raise ValueError('Unchanged native10M original parent required')
    sample_path = Path(prep['sample']['path'])
    if sha256(sample_path) != prep['sample']['sha256']:
        raise ValueError('Fixed original TRAIN64 differs')
    stat = parent_path.stat()
    c = dict(kind=KIND, created_at=now(), proposal=reference(PROPOSAL), preparation=reference(PREPARATION),
        sample=prep['sample'], parent=reference(parent_path), parent_size=stat.st_size,
        parent_mtime_ns=stat.st_mtime_ns, CPU_tests=reference(TESTS),
        sources={s: sha256(ROOT/s) for s in SOURCES}, GPU_limit_seconds=180,
        batch_candidates=[16, 32, 64], warmup_updates=3, timed_updates=5,
        resume_continuous_updates=4, resume_split_after=2,
        arms=['full_CE', 'CE_plus_native_contrast'],
        temperature=TEMPERATURE, coefficient=COEFFICIENT, seed=42,
        batch_choice='Highest minimum-of-both-arms median CE targets/second; tie favors larger measured batch',
        capacity_limit='Fixed64 distinct probe families limit the measured batch to64. This is not an RTX4090 maximum-capacity claim. Actual scientific-source larger-batch/length capacity must be measured before science.',
        scientific_teacher_tokens=0, probe_weights_discarded=True, protected_dev_test_used=False,
        Base_complete=False, Chat_started=False, quantization_started=False)
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(CONFIG, c)
    print(json.dumps(dict(status='frozen_GPU_not_started', config_sha256=sha256(CONFIG))))


def inspect():
    c = json.loads(CONFIG.read_text())
    for key in ('proposal', 'preparation', 'sample', 'CPU_tests'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Fixed probe reference changed: '+key)
    for name, expected in c['sources'].items():
        if sha256(ROOT/name) != expected:
            raise ValueError('Frozen probe source changed: '+name)
    stat = Path(c['parent']['path']).stat()
    if (stat.st_size, stat.st_mtime_ns) != (c['parent_size'], c['parent_mtime_ns']):
        raise ValueError('Parent identity changed after actual SHA verification')
    return c


def run():
    c = inspect()
    if (RUN/'job.json').exists():
        raise ValueError('Inspect saved identity/results; do not rerun completed or failed one-shot')
    if not torch.cuda.is_available():
        raise RuntimeError('Actual CUDA hardware required; no CPU substitution')
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
        scientific_teacher_tokens=0, Base_complete=False, Chat_started=False, quantization_started=False,
        restart_command='scripts/probe_natural_context_contrast.ps1 -Worker; inspect job first; completed/failed one-shot is never blindly restarted')
    atomic_json(RUN/'job.json', job)
    started = None
    all_histories, timings, gates = {}, {}, {}

    def check():
        if started is not None and time.monotonic()-started > c['GPU_limit_seconds']:
            raise TimeoutError('Native contrast probe GPU180s exhausted')

    def heartbeat(stage, **data):
        check()
        job.update(stage=stage, heartbeat_at=now(), **data)
        if started is not None:
            job['GPU_occupancy_seconds'] = time.monotonic()-started
        atomic_json(RUN/'job.json', job)

    def deadline(*args):
        raise TimeoutError('Native contrast probe GPU180s hard deadline')

    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        rows = json.loads(Path(c['sample']['path']).read_text())['rows']
        if len(rows) != 64:
            raise ValueError('Fixed64 required')
        for name in (*SOURCES, CONFIG.relative_to(ROOT).as_posix()):
            target = RUN/'source'/name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/name, target)
        binding = dict(parent=c['parent'], sample=c['sample'], sources=c['sources'], config_sha256=sha256(CONFIG))

        def build(batch, contrast):
            trainer = NaturalContextTrainer(parent, rows, binding, batch=batch, contrast=contrast)
            if sum(p.numel() for p in trainer.model.parameters()) != 10001152:
                raise ValueError('Original tied native10M parameter count required')
            return trainer

        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM, deadline)
            signal.alarm(c['GPU_limit_seconds'])
            job['status'] = 'running'
            for batch in c['batch_candidates']:
                for contrast in (False, True):
                    arm = 'CE_plus_native_contrast' if contrast else 'full_CE'
                    key = f'{arm}-batch{batch}'
                    heartbeat(key)
                    trainer = build(batch, contrast)
                    history = []
                    all_histories[key] = history
                    torch.cuda.reset_peak_memory_stats()
                    try:
                        with (RUN/(key+'.jsonl')).open('x', buffering=1) as log:
                            for _ in range(c['warmup_updates']+c['timed_updates']):
                                check()
                                row = trainer.step()
                                history.append(row)
                                log.write(json.dumps(row, allow_nan=False)+'\n')
                                heartbeat(key, completed_updates=len(history))
                        if not finite_state(host(trainer.state_dict())):
                            raise ValueError('Nonfinite actual trained model/optimizer')
                        measured = history[c['warmup_updates']:]
                        timings[key] = dict(stable=True, batch=batch, arm=arm,
                            median_CE_targets_per_second=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in measured),
                            median_physical_inputs_per_second=statistics.median(r['physical_inputs_this_update']/r['seconds'] for r in measured),
                            peak_VRAM_bytes=torch.cuda.max_memory_allocated(), history=history)
                    except torch.cuda.OutOfMemoryError as exc:
                        timings[key] = dict(stable=False, batch=batch, arm=arm, error=str(exc),
                            completed_updates=len(history), history=history)
                        atomic_json(RUN/'partial.json', dict(timings=timings, histories=all_histories))
                    finally:
                        del trainer
                        gc.collect()
                        torch.cuda.empty_cache()
                    atomic_json(RUN/'partial.json', dict(timings=timings, histories=all_histories))
            stable = [b for b in c['batch_candidates'] if all(
                timings[f'{arm}-batch{b}']['stable'] for arm in c['arms'])]
            if not stable:
                raise ValueError('No finite stable native CE/contrast batch')
            best = max(stable, key=lambda b: (min(timings[f'{arm}-batch{b}']['median_CE_targets_per_second']
                                                for arm in c['arms']), b))
            for contrast in (False, True):
                arm = 'CE_plus_native_contrast' if contrast else 'full_CE'
                folder = RUN/arm/'resume-gate'
                folder.mkdir(parents=True, exist_ok=True)
                states, histories = [], []
                for route in ('continuous', 'resumed'):
                    key = arm+'-resume-'+route
                    heartbeat(key)
                    trainer = build(best, contrast)
                    history = []
                    all_histories[key] = history
                    for update in range(4):
                        check()
                        history.append(trainer.step())
                        if route == 'resumed' and update == 1:
                            trainer.save(folder/'split.pt')
                            del trainer
                            gc.collect()
                            torch.cuda.empty_cache()
                            trainer = build(best, contrast)
                            trainer.load(folder/'split.pt')
                    trainer.save(folder/(route+'.pt'))
                    states.append(torch.load(folder/(route+'.pt'), map_location='cpu', weights_only=False))
                    histories.append(history)
                    del trainer
                    gc.collect()
                    torch.cuda.empty_cache()
                checks = {k: equal_state(states[0][k], states[1][k]) for k in states[0]}
                checks['finite'] = all(finite_state(s) for s in states)
                checks['all_history_except_timing'] = all(equal_state(
                    {k: v for k, v in a.items() if k != 'seconds'},
                    {k: v for k, v in b.items() if k != 'seconds'})
                    for a, b in zip(*histories, strict=True))
                gates[arm] = dict(passed=all(checks.values()), checks=checks, histories=histories,
                    checkpoints={route: reference(folder/(route+'.pt')) for route in ('continuous', 'resumed')})
                atomic_json(folder/'result.json', gates[arm])
                if not all(checks.values()):
                    raise ValueError('Actual full CUDA state/history resume differs: '+repr(checks))
                del states
            check()
            elapsed = time.monotonic()-started
            result = dict(status='complete', passed=True, config_sha256=sha256(CONFIG), actual_identity=identity(),
                selected_measured_batch=best, maximum_stable_measured_batch=max(stable),
                fixed_sample_capacity_limit=64, actual_GPU_maximum_claimed=False, timings=timings, gates=gates,
                verification_optimizer_updates=sum(len(h) for h in all_histories.values()),
                verification_CE_teacher_tokens=sum(r['CE_targets_this_update'] for h in all_histories.values() for r in h),
                verification_auxiliary_input_tokens=sum(r['auxiliary_inputs_this_update'] for h in all_histories.values() for r in h),
                verification_physical_inputs=sum(r['physical_inputs_this_update'] for h in all_histories.values() for r in h),
                GPU_occupancy_seconds=elapsed, GPU_limit_seconds=180, probe_weights_discarded=True,
                scientific_teacher_tokens=0, Base_complete=False, Chat_started=False, quantization_started=False,
                next_action='Implement the full accepted TRAIN corpus sampler and matched CE/auxiliary accounting. Measure larger-batch/long-unit scientific-source capacity once, then freeze measured scientific budget and common sources/evaluation before the proposed two100M CE runs. No science is authorized merely by the fixed64 probe.',
                limitations='Finite gradients, stable fixed64 batches and exact resume do not prove generative quality or whole-corpus throughput. Probe units are old accepted TRAIN, not new supply; auxiliary distractors are not logically false labels. Full Base gates unchanged.')
            atomic_json(RUN/'result.json', result)
            job.update(status='complete', ended_at=now(), GPU_occupancy_seconds=elapsed,
                verification_optimizer_updates=result['verification_optimizer_updates'])
            atomic_json(RUN/'job.json', job)
            print(json.dumps(dict(status='complete', measured_batch=best, GPU_occupancy_seconds=elapsed)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted', error=repr(exc), ended_at=now(),
            GPU_occupancy_seconds=time.monotonic()-started if started is not None else 0,
            completed_verification_updates=sum(len(h) for h in all_histories.values()))
        atomic_json(RUN/'job.json', job)
        atomic_json(RUN/'failure-partial.json', dict(timings=timings, gates=gates, histories=all_histories))
        raise
    finally:
        signal.alarm(0)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser()
    flags = parser.add_mutually_exclusive_group()
    flags.add_argument('--prepare', action='store_true')
    flags.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    if args.prepare:
        prepare()
    elif args.inspect:
        inspect()
        print('Fixed native probe source/input references verified; GPU0')
    else:
        run()
