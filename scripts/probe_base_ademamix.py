"""Bounded, durable CUDA validation of the prospective dual-gradient-EMA study."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state
from base_ademamix_trainer import AdEMAMixTrainer, finite_tree, POLICY
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host, right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity, alive

CONFIG = ROOT / 'configs/phase6/base_ademamix_probe.json'
RUN = ROOT / 'reports/phase6/base-ademamix-probe-20261007'
PROPOSAL = ROOT / 'reports/phase6/base_ademamix_proposal.json'
SOURCES = ('scripts/base_ademamix_trainer.py', 'scripts/probe_base_ademamix.py',
    'scripts/probe_base_ademamix.ps1', 'scripts/prepare_base_ademamix_proposal.py',
    'tests/test_base_ademamix.py', 'scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py', 'scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/training.py', 'src/jmicro/tokenizer.py', 'uv.lock')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def prepare():
    if CONFIG.exists():
        raise ValueError('Preserve frozen dual-EMA probe')
    old = read_json(ROOT / 'configs/phase6/base_muon_probe.json')
    proposal = read_json(PROPOSAL)
    tests = ROOT / 'reports/phase6/base_ademamix_CPU_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if (sum(int(s.attrib['tests']) for s in suites) != 16
            or any(int(s.attrib[k]) for s in suites for k in ('failures', 'errors', 'skipped'))):
        raise ValueError('Sixteen actual independent arithmetic/state CPU tests required')
    actual = dict(POLICY)
    expected = proposal['optimizer']
    if (actual['lr'] != expected['lr'] or actual['weight_decay'] != expected['weight_decay']
            or list(actual['betas']) != expected['betas'] or actual['alpha'] != expected['alpha']
            or actual['eps'] != expected['epsilon'] or actual['warmup'] != expected['alpha_warmup_updates']
            or actual['warmup'] != expected['beta3_half_life_warmup_updates']):
        raise ValueError('Implemented optimizer differs from prospective recipe')
    fields = ('parent', 'parent_size', 'parent_mtime_ns', 'source_binding', 'goals', 'tokenizer',
              'tokenizer_sha256', 'dev_shards', 'dev_manifest_sha256', 'suite_sha256', 'evaluation', 'control_CE')
    atomic_json(CONFIG, dict(**{key: old[key] for key in fields}, created_at=now(),
        proposal=ref(PROPOSAL), CPU_tests=ref(tests), payload=old['payload'],
        source_sha256={name: sha256(ROOT / name) for name in SOURCES},
        resource=proposal['resource'], optimizer=actual, batch=48, seed=42,
        source_policy='OriginalTrainCorpusSampler including full legacy prefix/suffix metadata; CE-only objective. mmap and abbreviated metadata not used, permitting exact full sampler comparison.',
        Base_complete=False, Chat_started=False, quantization_started=False))
    print('Frozen own CUDA180s/full-state/source/shape/all32 timing gate; scientific learning0')


def inspect():
    c = read_json(CONFIG)
    if (RUN / 'job.json').exists():
        raise ValueError('Inspect existing one-shot GPU evidence; do not rerun')
    for name in ('proposal', 'CPU_tests', 'payload', 'control_CE'):
        reference = c[name]
        if sha256(Path(reference['path'])) != reference['sha256']:
            raise ValueError('Frozen reference differs: ' + name)
    for name, digest in c['source_sha256'].items():
        if sha256(ROOT / name) != digest:
            raise ValueError('Frozen source differs: ' + name)
    stat = Path(c['parent']['path']).stat()
    if (stat.st_size, stat.st_mtime_ns) != (c['parent_size'], c['parent_mtime_ns']):
        raise ValueError('Accepted parent identity differs')
    payload = read_json(Path(c['payload']['path']))['window']
    if len(payload['input_ids']) != 1024 or sum(i != -100 for i in payload['target_ids']) != 512:
        raise ValueError('Accepted original maximum1024/512 window required')
    # Inspect current actual processes, not historical records or a stale lock.
    for folder in Path('/proc').iterdir():
        if not folder.name.isdecimal() or int(folder.name) == os.getpid():
            continue
        try:
            command = (folder / 'cmdline').read_bytes().split(b'\0')
            executable = command[0].decode() if command else ''
            if 'python' in Path(executable).name and any(
                arg.startswith((b'scripts/run_', b'scripts/probe_')) for arg in command[1:]):
                raise ValueError('Another actual project experiment process exists: ' + folder.name)
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            continue
    return c


def run():
    c = inspect()
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='running', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
               scientific_teacher_positions=0, Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(RUN / 'job.json', job)
    started, histories = None, {}
    def clear():
        gc.collect(); torch.cuda.empty_cache()
    def beat(stage):
        job.update(stage=stage, heartbeat_at=now())
        if started is not None:
            job['GPU_occupancy_seconds'] = time.monotonic()-started
        atomic_json(RUN / 'job.json', job)
    def timeout(*args):
        raise TimeoutError('Fixed GPU180s probe exhausted; no cap or recipe rescue')
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        codec = Tokenizer(ROOT / c['tokenizer'])
        if sha256(codec.path) != c['tokenizer_sha256']:
            raise ValueError('Pinned tokenizer differs')
        binding = dict(parent=c['parent'], config_sha256=sha256(CONFIG), weights_role='verification_only')
        def build(candidate=True):
            b = c['source_binding']
            sampler = OriginalTrainCorpusSampler(b['pool'], b['manifest_sha256'], codec, c['goals'], c['seed'])
            if sampler.binding != b:
                raise ValueError('Accepted original source binding differs')
            if candidate:
                return AdEMAMixTrainer(parent, sampler, binding, batch=c['batch'], seed=c['seed'])
            return NaturalCorpusTrainer(parent, sampler, binding, batch=c['batch'], seed=c['seed'], contrast=False)
        for name in (*SOURCES, CONFIG.relative_to(ROOT).as_posix()):
            destination = RUN / 'source' / name
            destination.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(ROOT / name, destination)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM, timeout); signal.alarm(c['resource']['probe_GPU_cap_seconds'])
            memory = configure_resident_memory(0)
            a = build(); rng = host(rng_state()); b = build(False)
            initial = dict(native_parent_weights=equal_state(parent['model'], host(a.model.state_dict())),
                candidate_control_initial_weights=equal_state(a.model.state_dict(), b.model.state_dict()),
                global_RNG_equal=equal_state(rng, host(rng_state())),
                tied_native_vocab=a.model.lm_head.weight is a.model.model.embed_tokens.weight,
                exact10M_parameters=sum(p.numel() for p in a.model.parameters()) == 10001152,
                all_parameters_once=[id(p) for p in a.model.parameters()] ==
                    [id(p) for group in a.optimizer.param_groups for p in group['params']],
                fresh_optimizer_empty=not a.optimizer.state and a.optimizer.completed_steps == 0,
                sampler_full_initial_state_equal=equal_state(a.sampler.state_dict(), b.sampler.state_dict()))
            del a, b; clear()
            states, logs = [], []
            for route in ('continuous', 'resumed'):
                beat(route); t = build(); history = []; histories[route] = history
                for index in range(4):
                    history.append(t.step())
                    if route == 'resumed' and index == 1:
                        t.save(RUN / 'split.pt'); del t; clear(); t = build(); t.load(RUN / 'split.pt')
                t.save(RUN / (route + '.pt'))
                states.append(host(t.state_dict())); logs.append(history)
                del t; clear()
            checks = {key: equal_state(states[0][key], states[1][key]) for key in states[0]}
            checks['finite_model_and_three_moments'] = all(finite_tree(s['model']) and finite_tree(s['optimizer']) for s in states)
            checks['all_history_except_timing'] = all(equal_state(
                {k: v for k, v in left.items() if k not in ('seconds', 'data_wait_seconds')},
                {k: v for k, v in right.items() if k not in ('seconds', 'data_wait_seconds')})
                for left, right in zip(*logs, strict=True))
            beat('matched-original-source'); control = build(False)
            histories['control'] = [control.step() for _ in range(4)]
            keys = (*control.counters, 'draw_trace', 'lr')
            checks['same_original_source_digest_masks_EOS'] = all(equal_state(left[k], right[k])
                for left, right in zip(logs[0], histories['control'], strict=True) for k in keys)
            checks['full_sampler_matches_AdamW'] = equal_state(states[0]['sampler'], control.sampler.state_dict())
            checks['initial_actual_CE_equal'] = logs[0][0]['CE_loss'] == histories['control'][0]['CE_loss']
            if not all(initial.values()) or not all(checks.values()):
                raise ValueError('Actual native/dual-moment/full-state/source CUDA gate failed')
            del control, states, logs; clear()
            beat('worst1024-and-all32-timing'); t = build()
            histories['timing'] = [t.step() for _ in range(c['resource']['warmup_updates'])]
            window = read_json(Path(c['payload']['path']))['window']
            ids = torch.tensor([window['input_ids']]*c['batch'], device='cuda')
            targets = torch.tensor([window['target_ids']]*c['batch'], device='cuda')
            frozen = host(t.model.state_dict()); optimizer_steps = t.optimizer.completed_steps
            t.optimizer.zero_grad(set_to_none=True); torch.cuda.reset_peak_memory_stats()
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION), torch.autocast('cuda', dtype=torch.bfloat16):
                selected = targets.ne(-100)
                loss = F.cross_entropy(t.model.lm_head(right_padded_hidden(t.model, ids)[selected]).float(), targets[selected])
                loss.backward()
            gradient = torch.nn.utils.clip_grad_norm_(t.model.parameters(), 1., error_if_nonfinite=True)
            torch.cuda.synchronize()
            capacity = dict(batch=c['batch'], context=1024, teacher_stride=512,
                backward_original_positions=int(selected.sum()), peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                loss=float(loss.detach()), gradient_norm=float(gradient), optimizer_updates=0,
                weights_unchanged=equal_state(frozen, host(t.model.state_dict())),
                optimizer_steps_unchanged=t.optimizer.completed_steps == optimizer_steps)
            if (not math.isfinite(capacity['loss']) or not 0 < capacity['gradient_norm'] < float('inf')
                    or not capacity['weights_unchanged'] or not capacity['optimizer_steps_unchanged']
                    or capacity['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']):
                raise ValueError('Resident finite maximum original shape required')
            del ids, targets, loss, frozen; clear()
            measured = [t.step() for _ in range(c['resource']['timed_updates'])]
            histories['timing'] += measured
            seconds = sum(row['seconds'] for row in measured)
            gold = sum(row['CE_targets_this_update'] for row in measured)
            t.validate_committed(t.state_dict())
            elapsed = time.monotonic()-started
            budget = math.ceil(100000000*seconds/gold*1.3+900)
            result = dict(status='complete', passed=True, actual_identity=identity(), config_sha256=sha256(CONFIG),
                initial_checks=initial, all_resume_and_source_checks=checks, capacity=capacity, memory_policy=memory,
                all32_step_seconds=seconds, all32_original_gold=gold,
                original_gold_per_second=gold/seconds,
                all32_data_wait_seconds=sum(row['data_wait_seconds'] for row in measured),
                GPU_occupancy_seconds=elapsed, probe_GPU_cap_seconds=c['resource']['probe_GPU_cap_seconds'],
                science_budget_seconds=budget, science_budget_eligible=budget+elapsed <= c['resource']['total_GPU_cap_seconds'],
                total_GPU_cap_seconds=c['resource']['total_GPU_cap_seconds'], histories=histories,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_teacher_positions=sum(row['CE_targets_this_update'] for h in histories.values() for row in h),
                scientific_teacher_positions=0, probe_weights_used_for_science=False,
                Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
                next_action='Implement durable scientific runner/evaluator/reviewer, freeze original quality policy and launch only if actual measured budget eligible. Never use probe weights as scientific parent.')
            if elapsed > c['resource']['probe_GPU_cap_seconds']:
                timeout()
            atomic_json(RUN / 'result.json', result)
            job.update(status='complete', ended_at=now(), GPU_occupancy_seconds=elapsed)
            atomic_json(RUN / 'job.json', job); signal.alarm(0)
            print(json.dumps({key: result[key] for key in ('status', 'original_gold_per_second',
                'GPU_occupancy_seconds', 'science_budget_seconds', 'science_budget_eligible')}))
    except BaseException as error:
        signal.alarm(0)
        job.update(status='failed', error=repr(error), ended_at=now(),
                   GPU_occupancy_seconds=time.monotonic()-started if started else 0)
        atomic_json(RUN / 'job.json', job); atomic_json(RUN / 'partial_histories.json', histories)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('prepare', 'inspect', 'run'))
    args = parser.parse_args()
    {'prepare': prepare, 'inspect': inspect, 'run': run}[args.mode]()
