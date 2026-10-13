"""Full four-suite Chat evaluation and2634 fixed targets, exact historical reuse."""
import argparse
from collections import Counter
import gc
import hashlib
import json
import math
from pathlib import Path
import signal
import time
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from chat_lr_contract import RUN, OLD, B, SUITES, LIMITS, CONFIG, preflight, load_parent, GPU_stage, reference, require_ref, suite_ref, SPEC, CONTROL_SPEC
from jmicro.experiment import read_json, now
from jmicro.training import atomic_json, seed_all
from jmicro.model import JMicroModel
from phase6_performance import finite_state, alive
import evaluate_chat_semantic as core

core.RUN, core.SUITES, core.suite_ref = RUN, SUITES, suite_ref


def checkpoint(c, arm, point):
    if arm == 'parent':
        assert point == 't0'
        return load_parent(c), c['parent']
    if arm == 'S0':
        history = read_json(require_ref(c['historical_control_evidence']))
        ref = history['checkpoints'][point]
        job = read_json(require_ref(history['original_job']))
        assert job['status'] == 'learning_complete' and not alive(job)
    else:
        job = read_json(RUN / arm / 'job.json')
        assert not alive(job) and job['config_sha256'] == c['config_sha256']
        ref = read_json(RUN / arm / 'checkpoints.json')[point]
    state = torch.load(require_ref(ref), map_location='cpu', weights_only=False)
    assert finite_state(state) and state['implementation_sha256'] == c['implementation']
    assert state['lineage']['base_checkpoint'] == c['parent'] and state['lineage']['optimizer_policy'] == 'fresh'
    expected = CONTROL_SPEC if arm == 'S0' else SPEC
    assert {key: state['spec'][key] for key in expected} == expected
    assert state['spec']['teacher_chat']['budget'] == B
    assert state['spec']['teacher_chat']['data_binding'] == c['sampler_binding']
    assert state['supervised_tokens'] == ref['Assistant_teachers'] and state['update'] == ref['update']
    return state, ref


def nll_windows(c, tok):
    rows = []
    for line in require_ref(c['fixed_NLL']).read_text().splitlines():
        record = json.loads(line)
        window = list(tok.sft_windows(record['messages'], context=1025))[-1]
        digest = hashlib.sha256(json.dumps(window, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        assert digest == record['window_binding']
        ids, labels = np.asarray(window['input_ids'][:-1]), np.asarray(window['labels'][1:])
        assert int((labels != -100).sum()) == record['teachers'] and labels[labels != -100][-1] == 7
        rows.append((record, ids, labels))
    assert len(rows) == 2634 and len({r[0]['id'] for r in rows}) == 2634
    return rows


def fixed_nll(model, c, tok, arm, point, ref, left, heartbeat, stopped):
    path = RUN / 'NLL' / arm / (point + '.json')
    binding = dict(config_sha256=c['config_sha256'], checkpoint=ref, fixed_targets=c['fixed_NLL'])
    if path.exists():
        done = read_json(path)
        assert done['binding'] == binding and done['status'] == 'complete'
        return
    windows = nll_windows(c, tok)
    reused, sources = {}, []
    if arm in ('parent', 'S0'):
        old_arm = 'parent' if arm == 'parent' else 'S1'
        old_path = OLD / 'NLL' / old_arm / (point + '.json')
        old = read_json(old_path)
        old_ref = old['binding']['checkpoint']
        assert old['status'] == 'complete' and old_ref['sha256'] == ref['sha256']
        old_fixed = [json.loads(line) for line in require_ref(read_json(require_ref(c['old_config']))['fixed_NLL']).read_text().splitlines()]
        templates = {row['id']: row for row in old_fixed}
        measured = {row['id']: row for row in old['targets']}
        assert len(templates) == len(measured) == 2554
        for target, _, _ in windows:
            if target['id'] not in templates:
                continue
            previous = templates[target['id']]
            assert all(previous[k] == target[k] for k in ('messages', 'window_binding', 'teachers', 'body_bytes'))
            actual = measured[target['id']]
            assert actual['body_teachers'] + actual['EOT_teachers'] == target['teachers']
            assert actual['body_bytes'] == target['body_bytes'] and actual['EOT_teachers'] == 1
            reused[target['id']] = dict(actual, dataset=target['dataset'])
        assert len(reused) == 2554
        sources.append(dict(source=reference(old_path), old_fixed=read_json(require_ref(c['old_config']))['fixed_NLL'],
                            exact_checkpoint_window_ID_bytes_teachers=True, rows=2554, new_GPU_updates=0))
    fresh = [window for window in windows if window[0]['id'] not in reused]
    progress = path.with_suffix('.progress.json')
    saved = read_json(progress) if progress.exists() else dict(binding=binding, rows=[])
    assert saved['binding'] == binding and len(saved['rows']) <= len(fresh)
    assert [row['id'] for row in saved['rows']] == [row[0]['id'] for row in fresh[:len(saved['rows'])]]
    for start in range(len(saved['rows']), len(fresh), 32):
        if stopped[0] or left() < 10:
            raise InterruptedError('NLL stops between full batches')
        batch = fresh[start:start + 32]
        losses = core.nll_batch(model, batch)
        for (target, _, _), (body, eot) in zip(batch, losses, strict=True):
            saved['rows'].append(dict(id=target['id'], dataset=target['dataset'], body_NLL=body, EOT_NLL=eot,
                body_teachers=target['teachers'] - 1, EOT_teachers=1, body_bytes=target['body_bytes']))
        atomic_json(progress, saved)
        heartbeat(stage='NLL', arm=arm, point=point, completed=len(saved['rows']))
    indexed = dict(reused)
    for row in saved['rows']:
        assert row['id'] not in indexed
        indexed[row['id']] = row
    ordered = [indexed[w[0]['id']] for w in windows]
    assert len(indexed) == len(ordered) == 2634
    summaries = {}
    for dataset in sorted({row['dataset'] for row in ordered}):
        items = [r for r in ordered if r['dataset'] == dataset]
        sums = {key: sum(r[key] for r in items) for key in ('body_NLL', 'EOT_NLL', 'body_teachers', 'EOT_teachers', 'body_bytes')}
        assert all(math.isfinite(v) and v >= 0 for v in sums.values())
        summaries[dataset] = dict(sums, targets=len(items), body_mean_NLL=sums['body_NLL'] / sums['body_teachers'],
            EOT_mean_NLL=sums['EOT_NLL'] / sums['EOT_teachers'], body_BPB=sums['body_NLL'] / sums['body_bytes'] / math.log(2))
    atomic_json(path, dict(status='complete', binding=binding, summaries=summaries, targets=ordered,
        historical_exact_NLL_reuse=sources, new_GPU_NLL_targets=len(fresh), completed_at=now(),
        provided_gold_history=True, own_generated_quality=False, protected_test_used=False))


def forecast(model, c, tok, left, heartbeat):
    path = RUN / 'evaluation_forecast.json'
    assert not path.exists(), 'Completed forecast retained'
    prompts = []
    for suite in SUITES:
        cases, contexts = core.load_cases(suite_ref(c, suite)['path'], tok)
        prompts += [case['messages'] for case in cases]
        for case in contexts:
            prompts.append([dict(m) if m['role'] == 'user' else dict(role='assistant', content='あ' * 64) for m in case['messages']])
    selected = sorted(prompts, key=lambda ms: len(tok.chat_prompt(ms, 960)[0]), reverse=True)[:5]
    timings, raw = [], []
    for i, messages in enumerate([selected[0]] + selected * 2):
        assert left() > 15
        started = time.monotonic()
        reply = core.generate_reply(model, tok, messages, 'cuda', 'bf16', 64, True, lambda: None)
        torch.cuda.synchronize()
        seconds = time.monotonic() - started
        timings.append(dict(phase='cold' if i == 0 else 'steady', seconds=seconds,
                            tokens=reply['generated_tokens'], seconds_per_token=seconds / reply['generated_tokens']))
        raw.append(dict(messages=messages, response=reply, timing_only=True))
        heartbeat(stage='forecast', completed=len(timings))
    windows = nll_windows(c, tok)
    times = []
    for start in (0, 0, 112, 224):
        started = time.monotonic()
        core.nll_batch(model, windows[start:start + 32])
        torch.cuda.synchronize()
        times.append(time.monotonic() - started)
    registration = read_json(RUN / 'historical_control_registration.json')
    assert registration['passed'] and registration['known_suite_judgments_reused'] == 2628
    # Full initial28 suites less12 exact reuses, plus qualified4x3 sampling.
    outputs = 28 * 219 - 2628 + 12 * 219
    batches = 3 * math.ceil(2634 / 32) + 4 * math.ceil(80 / 32)
    assert outputs == 6132 and batches == 261
    rate = max(row['seconds_per_token'] for row in timings[1:])
    generation = rate * 64 * outputs * 1.5
    nll = max(times[1:]) * batches * 1.5
    invocations = 16
    cold = invocations * (max(0., timings[0]['seconds'] - rate * timings[0]['tokens']) + max(0., times[0] - max(times[1:])))
    estimate = generation + nll + cold + 600.
    report = dict(passed=estimate <= LIMITS['evaluation'], config_sha256=c['config_sha256'], timings=timings,
        raw_timing_only=raw, NLL_batch_seconds=times, maximum_required_responses=outputs,
        maximum_new_NLL_batches=batches, maximum_tokens_per_response=64, planned_maximum_model_invocations=invocations,
        conservative_generation_seconds=generation, conservative_NLL_seconds=nll, cold_overhead_seconds=cold,
        forecast_evaluation_seconds=estimate, limit_seconds=LIMITS['evaluation'],
        includes_all28_greedy_suites_and_qualified12_sampling_suites=True,
        quality_evidence=False, completed_at=now())
    atomic_json(path, report)
    assert report['passed'], 'Full mandatory and conditional evaluation exceeds frozen allocation'
    print(json.dumps({key: report[key] for key in ('passed', 'maximum_required_responses', 'forecast_evaluation_seconds')}))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--config', type=Path, required=True)
    p.add_argument('--mode', choices=('forecast', 'evaluate'), required=True)
    p.add_argument('--arm', choices=('parent', 'S0', 'S1'), default='parent')
    p.add_argument('--points', nargs='+', choices=('t0', 't1', 't2', 't3'), default=['t0'])
    p.add_argument('--suites', nargs='+', choices=SUITES, default=list(SUITES))
    p.add_argument('--decoding', choices=('greedy', 'sampling'), default='greedy')
    p.add_argument('--inspect', action='store_true')
    args = p.parse_args()
    c, tok, _ = preflight(args.config)
    for suite in args.suites:
        core.load_cases(suite_ref(c, suite)['path'], tok)
    if args.inspect:
        print('LR-only four-suite evaluation preflight passed; GPU0')
        return
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    seed_all(42)
    stopped = [False]
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    if args.decoding == 'sampling':
        selection = read_json(RUN / 'selection.json')
        assert selection['eligible_candidate'] == args.arm and args.points == ['t3']
    with GPU_stage('evaluation', args.mode + '-' + args.arm, c['config_sha256']) as (left, heartbeat), sdpa_kernel(SDPBackend.MATH):
        for point in args.points:
            assert (args.arm == 'parent') == (point == 't0')
            state, ref = checkpoint(c, args.arm, point)
            model = JMicroModel(state['model_config']).cuda().eval()
            model.load_state_dict(state['model'], strict=True)
            del state
            assert sum(p.numel() for p in model.parameters() if p.requires_grad) == 10001152
            if args.mode == 'forecast':
                forecast(model, c, tok, left, heartbeat)
            else:
                for suite in args.suites:
                    for seed in ([42] if args.decoding == 'greedy' else [42, 43, 44]):
                        core.chat(model, c, tok, args.arm, point, ref, suite, seed, args.decoding, left, heartbeat, stopped)
                fixed_nll(model, c, tok, args.arm, point, ref, left, heartbeat, stopped)
            del model
            gc.collect()
            torch.cuda.empty_cache()


if __name__ == '__main__':
    main()
