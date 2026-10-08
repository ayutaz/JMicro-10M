"""Bounded read-only teacher/free history diagnostic on six exposed TRAIN units."""
import argparse
from contextlib import nullcontext
import json
from pathlib import Path
import re
import sys
import time
import xml.etree.ElementTree as ET

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, gpu_lock, rng_state
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer, SUPPRESS_IDS
from base_parallel_residual_model import model_from_config
from base_parallel_residual_evaluation import validate_record
from base_parallel_residual_trainer import KIND
from phase6_performance import alive, identity

PHASE = ROOT / 'reports/phase6'
RUN = PHASE / 'base-residual-seen-train-diagnostic-20261008'
CONFIG = ROOT / 'configs/phase6/base_residual_seen_train_diagnostic.json'
PROPOSAL = PHASE / 'base_residual_seen_train_diagnostic_proposal.json'
PREPARATION = PHASE / 'base_residual_seen_train_preparation.json'
SOURCE_NOTES = PHASE / 'base_residual_seen_train_source_notes.json'
OUTPUT = PHASE / 'base_residual_seen_train_diagnostic.json'


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def checked(reference):
    path = Path(reference['path'])
    if sha256(path) != reference['sha256']:
        raise ValueError('Frozen reference differs: ' + str(path))
    return read_json(path)


def freeze():
    if CONFIG.exists():
        raise ValueError('Preserve prospective six-case diagnostic config')
    tests = PHASE / 'base_residual_seen_train_runner_tests.xml'
    cases = ET.parse(tests).findall('.//testcase')
    if len(cases) != 5 or any(r.find(tag) is not None for r in cases for tag in ('failure', 'error', 'skipped')):
        raise ValueError('Five passed CPU history protocol fixtures required')
    proposal, prepared, notes = read_json(PROPOSAL), read_json(PREPARATION), read_json(SOURCE_NOTES)
    if (proposal['GPU_budget_seconds'] != 180 or proposal['scientific_teacher_tokens'] or proposal['optimizer_updates']
            or prepared['proposal_sha256'] != sha256(PROPOSAL) or not prepared['all80_first_draw_trace_exact']
            or not prepared['original_next_token_alignment_verified']
            or notes['preparation_sha256'] != sha256(PREPARATION) or not notes['all6_whole_units_individually_read']
            or len(prepared['selected']) != 6):
        raise ValueError('Bounded prospective comparison and actual consumed six units required')
    if any(p.exists() for p in (OUTPUT, RUN)):
        raise ValueError('Fix the diagnostic protocol before new GPU outputs')
    trained = PHASE / 'base-parallel-residual-comparison-20261007/sequential/train-result.json'
    record = read_json(trained)
    validate_record('sequential', record)
    if record['status'] != 'complete' or record['counters']['supervised_tokens'] != 2000000000:
        raise ValueError('Actual complete fixed sequential2B required')
    old = read_json(ROOT / 'configs/phase6/base_parallel_residual_comparison.json')
    atomic_json(CONFIG, dict(created_at=now(), proposal=ref(PROPOSAL), preparation=ref(PREPARATION),
        source_notes=ref(SOURCE_NOTES), training_record=ref(trained), checkpoint=dict(path=record['checkpoint'], sha256=record['checkpoint_sha256']),
        comparison_completion=ref(PHASE / 'base_parallel_residual_comparison_completion.json'), CPU_tests=ref(tests),
        CPU_tests_scope='History protocol fixtures only; no actual GPU or model quality claim',
        source_sha256={**old['source_sha256'], 'scripts/run_base_residual_seen_train.py': sha256(Path(__file__)),
                       'scripts/run_base_residual_seen_train.ps1': sha256(ROOT / 'scripts/run_base_residual_seen_train.ps1'),
                       'tests/test_base_residual_seen_train.py': sha256(ROOT / 'tests/test_base_residual_seen_train.py')},
        GPU_budget_seconds=180, max_new_tokens=64, dtype='bf16', backend='math', suppressed_ids=sorted(SUPPRESS_IDS),
        actual_model_class='JMicroModel', diagnostic_only=True, scientific_teacher_tokens=0, optimizer_updates=0,
        Base_complete=False, Chat_started=False, quantization_started=False, protected_test_scored=False))
    print('Frozen six exposed units / same sequential2B / teacher vs free history /180seconds/no learning')


def inspect():
    c = read_json(CONFIG)
    for name, digest in c['source_sha256'].items():
        if sha256(ROOT / name) != digest:
            raise ValueError('Frozen diagnostic source differs: ' + name)
    prepared, trained = checked(c['preparation']), checked(c['training_record'])
    checked(c['proposal']); checked(c['source_notes'])
    completed = checked(c['comparison_completion'])
    if (not completed['fixed_parallel_residual_condition_closed'] or completed['Base_complete']
            or c['GPU_budget_seconds'] != 180 or c['max_new_tokens'] != 64
            or c['dtype'] != 'bf16' or c['backend'] != 'math' or c['scientific_teacher_tokens'] or c['optimizer_updates']
            or c['suppressed_ids'] != sorted(SUPPRESS_IDS)):
        raise ValueError('Original failed recipe closed and separate bounded diagnostic required')
    validate_record('sequential', trained)
    if c['checkpoint'] != dict(path=trained['checkpoint'], sha256=trained['checkpoint_sha256']):
        raise ValueError('Fixed actual checkpoint binding required')
    old_job = read_json(PHASE / 'base-parallel-residual-comparison-20261007/job.json')
    if alive(old_job) or old_job['status'] != 'complete':
        raise ValueError('Previous scientific GPU job must be terminal and absent')
    if OUTPUT.exists() or (RUN / 'job.json').exists():
        raise ValueError('Inspect existing diagnostic result/process; no duplicate or reroll')
    lock = Path.home() / 'jmicro-data/gpu.lock'
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    if lock.exists():
        holder = read_json(lock)
        if Path(f"/proc/{holder['pid']}").exists() and (holder['pid'] != ui['pid'] or not alive(ui)):
            raise ValueError('Another actual GPU process exists; no concurrent diagnostic')
    return c, prepared, trained


@torch.inference_mode()
def history(model, codec, unit, forced, device, check):
    gold = unit['continuation_gold_ids']
    current = torch.tensor([unit['prompt_ids']], device=device)
    cache, steps, fed, predicted, reason = None, [], [], [], 'max_new_tokens'
    cap = min(64, len(gold)) if forced else 64
    for index in range(cap):
        check()
        context = torch.autocast('cuda', dtype=torch.bfloat16) if str(device).startswith('cuda') else nullcontext()
        with context:
            output = model(current, cache=cache, use_cache=True)
        cache = output.cache
        logits = output.logits[0, -1].float()
        if not bool(torch.isfinite(logits).all()):
            raise ValueError('Finite actual inference logits required')
        masked = logits.clone(); masked[list(SUPPRESS_IDS)] = -torch.inf
        next_id = int(masked.argmax())
        target = gold[index] if index < len(gold) else None
        logp = logits.log_softmax(-1)
        steps.append(dict(index=index, original_gold_id=target, greedy_id=next_id,
            original_gold_nll=None if target is None else float(-logp[target]),
            original_gold_rank=None if target is None else int((logits > logits[target]).sum()) + 1,
            original_gold_probability=None if target is None else float(logp[target].exp()),
            EOS_probability=float(logp[3].exp()), actual_gold_EOS=target == 3))
        predicted.append(next_id)
        feed = target if forced else next_id
        fed.append(feed)
        if feed == 3:
            reason = 'original_gold_EOS' if forced else 'stop_id'
            break
        current = torch.tensor([[feed]], device=device)
    raw = codec.decode_bytes(fed)
    try:
        text, valid = raw.decode('utf-8'), True
    except UnicodeDecodeError:
        text, valid = raw.decode('utf-8', errors='replace'), False
    return dict(history='gold_forced' if forced else 'free_running', steps=steps, fed_ids=fed,
        predicted_ids=predicted, text=text, raw_UTF8_bytes_hex=raw.hex(), valid_UTF8=valid,
        role_leak=any(i in (4,5,6,7) for i in fed), empty=not text.strip(), stop_reason=reason,
        automatic_repetition=bool(re.search(r'(.{2,}?)\1\1', text, flags=re.DOTALL)),
        concatenated_teacher_predictions_are_not_a_generated_continuation=forced)


def run():
    torch.set_num_threads(2)
    c, prepared, trained = inspect()
    if not torch.cuda.is_available() or not torch.cuda.is_bf16_supported():
        raise RuntimeError('Actual CUDA/BF16 hardware required')
    RUN.mkdir(parents=True)
    job = dict(status='starting', **identity(), config_sha256=sha256(CONFIG), started_at=now(),
               GPU_seconds=0, cumulative_GPU_ledger_closed=False, restart_command='Inspect actual PID/boot/start, partial cases and remaining180-second ledger before any retry; no reroll.')
    atomic_json(RUN / 'job.json', job)
    started = None
    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            def check():
                if time.monotonic() - started >= 180:
                    raise TimeoutError('Frozen cumulative180-second diagnostic cap exhausted')
            checkpoint = Path(c['checkpoint']['path'])
            if sha256(checkpoint) != c['checkpoint']['sha256']:
                raise ValueError('Actual fixed checkpoint differs')
            state = torch.load(checkpoint, map_location='cpu', weights_only=False)
            if (state['kind'] != KIND or state['spec']['arm'] != 'sequential'
                    or state['counters']['supervised_tokens'] != 2000000000
                    or state['model_config'] != trained['model_config']):
                raise ValueError('Typed actual fixed residual2B state required')
            model = model_from_config(state['model_config']).to('cuda').eval()
            model.load_state_dict(state['model'], strict=True)
            if type(model).__name__ != c['actual_model_class'] or sum(p.numel() for p in model.parameters()) != 10001152:
                raise ValueError('Explicit same actual10M residual architecture required')
            before = rng_state()
            codec = Tokenizer(ROOT / read_json(ROOT / 'configs/phase6/base_parallel_residual_comparison.json')['tokenizer'])
            results = []
            with sdpa_kernel(SDPBackend.MATH):
                for unit in prepared['selected']:
                    check()
                    a = history(model, codec, unit, True, 'cuda', check)
                    b = history(model, codec, unit, False, 'cuda', check)
                    if a['steps'][0] != b['steps'][0]:
                        raise ValueError('Teacher/free first identical-prefix prediction differs')
                    row = dict(id=unit['id'], prefix=unit['prefix'], source=unit['source'],
                        teacher=a, free=b, same_first_prefix_prediction_exact=True,
                        original_gold_EOS_within64=3 in unit['continuation_gold_ids'][:64])
                    atomic_json(RUN / (unit['id'] + '.json'), row)
                    results.append(row)
                    job.update(status='running', completed_cases=len(results), GPU_seconds=time.monotonic() - started, heartbeat_at=now())
                    atomic_json(RUN / 'job.json', job)
                    print(json.dumps(dict(case=unit['id'], completed_cases=len(results), GPU_seconds=job['GPU_seconds'])), flush=True)
            torch.cuda.synchronize()
            checks = dict(weights_unchanged=all(torch.equal(v.detach().cpu(), state['model'][k]) for k,v in model.state_dict().items()),
                          RNG_unchanged=equal_state(before, rng_state()), eval_mode_unchanged=not model.training,
                          all6_same_first_prefix_exact=all(r['same_first_prefix_prediction_exact'] for r in results))
            if not all(checks.values()):
                raise ValueError('Read-only actual weights/RNG/mode evidence failed')
            check()
            elapsed = time.monotonic() - started
            result = dict(status='all6_teacher_free_GPU_complete_content_review_pending', created_at=now(),
                actual_identity=identity(), config=ref(CONFIG), proposal=c['proposal'], preparation=c['preparation'],
                checkpoint=c['checkpoint'], source_sha256=c['source_sha256'], checks=checks,
                GPU_seconds=elapsed, GPU_cap_seconds=180, cumulative_GPU_ledger_closed=True,
                teacher_forced_scored_targets=sum(len(r['teacher']['steps']) for r in results),
                free_generated_tokens=sum(len(r['free']['fed_ids']) for r in results), results=results,
                scientific_teacher_tokens=0, optimizer_updates=0, content_individually_read=False,
                Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_scored=False,
                limits='Six previously exposed TRAIN examples, not heldout quality or repeated memorization proof. Gold/free history within the same frozen checkpoint; no artificial EOS. Teacher concatenated predictions are not continuous generated prose.')
            atomic_json(OUTPUT, result)
            job.update(status='complete', ended_at=now(), GPU_seconds=elapsed, cumulative_GPU_ledger_closed=True)
            atomic_json(RUN / 'job.json', job)
    except BaseException as error:
        if started is not None:
            torch.cuda.synchronize()
        job.update(status='failed', ended_at=now(), error=repr(error),
                   GPU_seconds=0 if started is None else time.monotonic() - started, cumulative_GPU_ledger_closed=True)
        atomic_json(RUN / 'job.json', job)
        raise


def wait_ui():
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    start = time.monotonic()
    while alive(ui):
        if time.monotonic() - start >= 30:
            raise TimeoutError('Original UI still live after30seconds; no GPU job started')
        time.sleep(.2)
    print('Actual prior UI PID/boot/start exited')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group()
    g.add_argument('--freeze', action='store_true'); g.add_argument('--inspect', action='store_true'); g.add_argument('--wait-ui', action='store_true')
    a = p.parse_args()
    if a.freeze: freeze()
    elif a.inspect:
        inspect(); print('Frozen six-case diagnostic preflight passed; previous science actual exited')
    elif a.wait_ui: wait_ui()
    else: run()
