"""One actual CUDA source/capacity/RNG-resume probe; no scientific learning."""
import argparse
import gc
import math
import statistics
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'),
                str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, sha256, now
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host, right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from base_label_smoothing import EPSILON, smoothed_teacher_loss
from base_label_smoothing_packed import PackedLabelSmoothingTrainer
from phase6_performance import identity, alive, finite_state

CONFIG = ROOT / 'configs/phase6/base_label_smoothing_packed_probe.json'
RUN = ROOT / 'reports/phase6/base-label-smoothing-packed-probe-20261007'
SOURCES = ('scripts/base_label_smoothing.py', 'scripts/base_label_smoothing_trainer.py', 'scripts/base_label_smoothing_packed.py', 'scripts/probe_base_label_smoothing_packed.py',
           'scripts/probe_base_label_smoothing_packed.ps1',
           'scripts/natural_context_contrast_corpus.py', 'scripts/natural_context_contrast_trainer.py',
           'scripts/natural_context_contrast_memory.py', 'src/jmicro/model.py',
           'src/jmicro/training.py', 'src/jmicro/tokenizer.py',
           'tests/test_base_label_smoothing.py', 'tests/test_base_label_smoothing_trainer.py', 'tests/test_base_label_smoothing_packed.py', 'uv.lock')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def prepare():
    if CONFIG.exists() or (RUN / 'job.json').exists():
        raise ValueError('Preserve frozen or already attempted probe')
    old = json.loads((ROOT / 'configs/phase6/base_residual_dropout_probe.json').read_text())
    proposal = ROOT / 'reports/phase6/base_label_smoothing_proposal.json'
    proposed = json.loads(proposal.read_text())
    if proposed['epsilon'] != EPSILON or proposed['GPU_probe_limit_seconds'] != 180:
        raise ValueError('Fixed epsilon and bounded probe proposal required')
    tests = ROOT / 'reports/phase6/base_label_smoothing_packed_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if not suites or sum(int(s.attrib['tests']) for s in suites) < 2 or any(
            int(s.attrib[k]) for s in suites for k in ('errors', 'failures', 'skipped')):
        raise ValueError('Actual successful CPU protocol tests required')
    previous = ROOT / 'reports/phase6/base_residual_dropout_comparison_completion.json'
    closed = json.loads(previous.read_text())
    if not closed['fixed_recipe_closed'] or not closed['actual_process_absent_verified']:
        raise ValueError('Close preceding experiment first')
    baseline_run = ROOT / 'reports/phase6/base-label-smoothing-probe-20261007'
    timing_run = ROOT / 'reports/phase6/base-label-smoothing-timing-20261007'
    baseline = json.loads((baseline_run / 'result.json').read_text())
    timed = json.loads((timing_run / 'result.json').read_text())
    if alive(json.loads((baseline_run/'job.json').read_text())) or alive(json.loads((timing_run/'job.json').read_text())):
        raise ValueError('Previous actual probe/timing processes must have exited')
    if timed['science_budget_fits'] or not baseline['passed'] or len(timed['all37_samples']) != 37:
        raise ValueError('Preserve original failed budget and passed numerical gate before transfer optimization')
    spent = baseline['GPU_occupancy_seconds'] + timed['GPU_occupancy_seconds']
    c = dict(created_at=now(), proposal=ref(proposal), CPU_tests=ref(tests),
             original_probe_result=ref(baseline_run/'result.json'),
             original4_checkpoint=baseline['resume_checkpoints']['continuous'],
             original32_timing_metrics=ref(timing_run/'metrics.jsonl'),
             prior_probe_GPU_seconds=spent, implementation_change='Same target values/shape, one H2D transfer instead of48; original objective/spec/native parameters unchanged',
             previous_completion=ref(previous), sources={s: sha256(ROOT / s) for s in SOURCES},
             parent=old['parent'], parent_size=old['parent_size'], parent_mtime_ns=old['parent_mtime_ns'],
             source_binding=old['source_binding'], goals=old['goals'], payload=old['payload'],
             tokenizer_sha256=old['tokenizer_sha256'], epsilon=EPSILON,
             native_parameters=10001152, train_only_parameters=0, GPU_limit_seconds=math.floor(180-spent),
             seed=42, batch_candidates=[48], warmup_updates=3, timed_updates=32,
             matched_scientific_batch=48, resident_allocator_fraction=.90,
             policy='Probe original full-source CE; initialize Adam, stress actual longest1024 window, '
                    'stop capacity growth after first OOM. Four continuous versus two-save-resume-two '
                    'checks native/uniform accounting/RNG/state/history. Discard all probe weights. '
                    'No science before persistent command and measured forecast.',
             scientific_teacher_tokens=0, Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(CONFIG, c)
    print(json.dumps(dict(status='smoothing_probe_frozen_GPU0', config_sha256=sha256(CONFIG))))


def inspect():
    c = json.loads(CONFIG.read_text())
    for key in ('proposal', 'CPU_tests', 'previous_completion', 'payload', 'original_probe_result', 'original4_checkpoint', 'original32_timing_metrics'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Frozen reference differs: ' + key)
    for name, digest in c['sources'].items():
        if sha256(ROOT / name) != digest:
            raise ValueError('Frozen source differs: ' + name)
    stat = Path(c['parent']['path']).stat()
    if (stat.st_size, stat.st_mtime_ns) != (c['parent_size'], c['parent_mtime_ns']):
        raise ValueError('Previously SHA-verified parent identity differs')
    if (RUN / 'job.json').exists():
        raise ValueError('Inspect one-shot identity; never retry completed/failed probe blindly')
    return c


def worst_shape(trainer, window, batch):
    trainer.optimizer.zero_grad(set_to_none=True)
    torch.cuda.reset_peak_memory_stats()
    ids = torch.tensor([window['input_ids']] * batch, device=trainer.device)
    targets = torch.tensor([window['target_ids']] * batch, device=trainer.device)
    selected = targets != -100
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION), torch.autocast('cuda', dtype=torch.bfloat16):
        hidden = right_padded_hidden(trainer.model, ids)
        loss, measures = smoothed_teacher_loss(trainer.model.lm_head(hidden[selected]).float(), targets[selected])
        loss.backward()
    gradient = torch.nn.utils.clip_grad_norm_(trainer.model.parameters(), 1., error_if_nonfinite=True)
    torch.cuda.synchronize()
    if not torch.isfinite(loss) or not (0 < float(gradient) < float('inf')):
        raise ValueError('Maximum-context smoothing CE gradient must be finite/nonzero')
    peak = torch.cuda.max_memory_allocated()
    trainer.optimizer.zero_grad(set_to_none=True)
    return dict(passed=True, peak_VRAM_bytes=peak, context=len(window['input_ids']),
                loss=float(loss.detach()), gradient_norm=float(gradient),
                uniform_target_positions=measures['uniform_soft_target_positions'],
                weighted_original_target_mass=measures['weighted_original_target_mass'],uniform_target_mass=measures['uniform_target_mass'],
                optimizer_updates=0, teachers=int(selected.sum()), physical_input_tokens=ids.numel())


def run():
    c = inspect()
    if not torch.cuda.is_available():
        raise RuntimeError('Actual CUDA required')
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
               scientific_teacher_tokens=0, Base_complete=False, Chat_started=False,
               quantization_started=False, restart_command='One-shot probe: inspect actual PID/boot/start '
               'and preserved partial evidence; do not restart a completed or failed probe.')
    atomic_json(RUN / 'job.json', job)
    histories, capacities, timings, initial = {}, {}, {}, {}
    started = None

    def check(*args):
        if args or (started is not None and time.monotonic() - started > c['GPU_limit_seconds']):
            raise TimeoutError('Fixed smoothing GPU180s exhausted')

    def beat(stage):
        check()
        job.update(stage=stage, heartbeat_at=now(), GPU_occupancy_seconds=time.monotonic() - started)
        atomic_json(RUN / 'job.json', job)

    def clear():
        gc.collect()
        torch.cuda.empty_cache()

    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        codec = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
        if sha256(codec.path) != c['tokenizer_sha256']:
            raise ValueError('Pinned tokenizer differs')
        binding = dict(parent=c['parent'], source_binding=c['source_binding'],
                       config_sha256=sha256(CONFIG), weights_role='verification_only', sources=c['sources'])

        def build(batch, smoothing=True):
            source = OriginalTrainCorpusSampler(c['source_binding']['pool'],
                c['source_binding']['manifest_sha256'], codec, c['goals'], 42)
            if source.binding != c['source_binding']:
                raise ValueError('Original accepted TRAIN binding differs')
            cls = PackedLabelSmoothingTrainer if smoothing else NaturalCorpusTrainer
            return cls(parent, source, binding, batch=batch, contrast=False)

        for name in (*SOURCES, CONFIG.relative_to(ROOT).as_posix()):
            target = RUN / 'source' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM, check)
            signal.alarm(c['GPU_limit_seconds'])
            job['status'] = 'running'
            memory = configure_resident_memory(0)
            beat('native-inference-and-initialization')
            t = build(48, False)
            t.model.eval()
            ids = torch.tensor([[2, 8, 9, 10]], device='cuda')
            with torch.no_grad(), sdpa_kernel(SDPBackend.MATH), torch.autocast('cuda', dtype=torch.bfloat16):
                expected = t.model(ids).logits.detach().clone()
            expected_rng = host(rng_state())
            del t
            clear()
            t = build(48)
            t.model.eval()
            initial = dict(native_weights=equal_state(parent['model'], host(t.model.state_dict())),
                           native_parameters=sum(p.numel() for p in t.model.parameters()) == 10001152,
                           native_tied=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                           initialization_RNG=equal_state(expected_rng, host(rng_state())),
                           fixed_epsilon=t.spec['label_smoothing'] == EPSILON,
                           full_vocabulary=t.spec['uniform_vocabulary'] == 4096,
                           no_inference_hooks=not hasattr(t.model, '_residual_dropout_hooks'))
            with torch.no_grad(), sdpa_kernel(SDPBackend.MATH), torch.autocast('cuda', dtype=torch.bfloat16):
                initial['native_logits'] = torch.equal(expected, t.model(ids).logits)
            initial['inference_RNG_unchanged'] = equal_state(expected_rng, host(rng_state()))
            if not all(initial.values()):
                raise ValueError('Native/smoothing initialization checks failed: ' + repr(initial))
            del t, ids, expected
            clear()
            window = json.loads(Path(c['payload']['path']).read_text())['window']
            for batch in c['batch_candidates']:
                beat('capacity-and-source-batch' + str(batch))
                t = build(batch)
                history = []
                histories[str(batch)] = history
                try:
                    history.append(t.step())
                    capacities[str(batch)] = worst_shape(t, window, batch)
                    for _ in range(c['warmup_updates']):
                        check(); history.append(t.step())
                    timed = []; timed_rows = []
                    for _ in range(c['timed_updates']):
                        check(); row = t.step(); history.append(row)
                        timed.append(row['CE_targets_this_update'] / row['seconds']); timed_rows.append(row)
                    timings[str(batch)] = dict(median_CE_targets_per_second=statistics.median(timed),
                                              samples=timed)
                except torch.OutOfMemoryError as exc:
                    capacities[str(batch)] = dict(passed=False, OOM=repr(exc), stop_growth=True)
                    break
                finally:
                    del t; clear()
            batch = c['matched_scientific_batch']
            if str(batch) not in timings or not capacities[str(batch)]['passed']:
                raise ValueError('Cached-control batch48 not resident-stable; do not rerun or change controls')
            best = max((int(b) for b in timings), key=lambda b: timings[str(b)]['median_CE_targets_per_second'])
            folder = RUN / 'resume-gate'
            folder.mkdir(exist_ok=True)
            states, logs = [], []
            for route in ('continuous', 'resumed'):
                beat('full-source-' + route)
                t = build(batch)
                history = []
                histories[route] = history
                for index in range(4):
                    check(); history.append(t.step())
                    if route == 'resumed' and index == 1:
                        t.save(folder / 'split.pt')
                        del t; clear(); t = build(batch); t.load(folder / 'split.pt')
                t.save(folder / (route + '.pt'))
                states.append(torch.load(folder / (route + '.pt'), map_location='cpu', weights_only=False))
                logs.append(history)
                del t; clear()
            checks = {key: equal_state(states[0][key], states[1][key]) for key in states[0]}
            checks['finite'] = all(finite_state(state) for state in states)
            checks['uniform_accounting'] = all(
                s['counters']['uniform_soft_target_positions'] == s['counters']['supervised_tokens']
                and s['counters']['weighted_original_target_mass'] == (1-EPSILON)*s['counters']['supervised_tokens']
                and s['counters']['uniform_target_mass'] == EPSILON*s['counters']['supervised_tokens']
                and s['counters']['auxiliary_input_tokens'] == s['counters']['auxiliary_pairs'] == 0
                for s in states)
            checks['all_history_except_timing'] = all(equal_state(
                {k: v for k, v in a.items() if k not in ('seconds', 'data_wait_seconds')},
                {k: v for k, v in b.items() if k not in ('seconds', 'data_wait_seconds')})
                for a, b in zip(*logs, strict=True))
            original = torch.load(c['original4_checkpoint']['path'], map_location='cpu', weights_only=False)
            checks['cached_original4_state_numeric_parity'] = all(equal_state(states[0][key],original[key]) for key in states[0] if key!='binding')
            baseline_rows = [json.loads(line) for line in Path(c['original32_timing_metrics']['path']).read_text().splitlines()]
            checks['cached32_step_numerical_history_parity'] = len(baseline_rows)==len(timed_rows)==32 and all(equal_state(
                {k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(baseline_rows,timed_rows,strict=True))
            if not all(checks.values()):
                raise ValueError('Packed transfer/full-state numeric CUDA parity differed: '+repr(checks))
            check()
            elapsed = time.monotonic() - started
            result = dict(status='complete', passed=True, actual_identity=identity(), config_sha256=sha256(CONFIG),
                          initial_checks=initial, memory_policy=memory, capacity=capacities, timings=timings,
                          timed32_rows=timed_rows,prior_probe_GPU_seconds=c['prior_probe_GPU_seconds'],
                          total_probe_GPU_seconds=c['prior_probe_GPU_seconds']+elapsed,
                          measured_fastest_resident_batch=best, selected_matched_batch=batch,
                          resume_checks=checks, resume_histories=logs,
                          resume_checkpoints={r: ref(folder / (r + '.pt')) for r in ('continuous', 'resumed')},
                          verification_updates=sum(len(h) for h in histories.values()),
                          verification_CE_teacher_tokens=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                          GPU_occupancy_seconds=elapsed, scientific_teacher_tokens=0, probe_weights_used_for_science=False,
                          Base_complete=False, Chat_started=False, quantization_started=False,
                          next_action='Implement persistent smoothing100M command/evaluation/reviewer, then freeze measured '
                                      'budget using batch48 and completed CE100M control. No scientific work started by this probe.')
            atomic_json(RUN / 'result.json', result)
            job.update(status='complete', stage='complete', ended_at=now(), GPU_occupancy_seconds=elapsed)
            atomic_json(RUN / 'job.json', job)
            print(json.dumps(dict(status='smoothing_probe_complete', batch=batch, fastest=best, GPU_seconds=elapsed)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted', error=repr(exc), ended_at=now(),
                   GPU_occupancy_seconds=time.monotonic() - started if started else 0)
        atomic_json(RUN / 'job.json', job)
        atomic_json(RUN / 'failure-partial.json', dict(initial=initial, capacity=capacities,
                                                    timings=timings, histories=histories))
        raise
    finally:
        signal.alarm(0)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--prepare', action='store_true')
    group.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    if args.prepare:
        prepare()
    elif args.inspect:
        inspect(); print('Frozen smoothing/source inspected; GPU0')
    else:
        run()
