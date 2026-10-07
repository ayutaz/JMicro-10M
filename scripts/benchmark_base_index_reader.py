"""Prospective, bounded CPU reader comparison; never launches learning."""
import argparse
import hashlib
import json
import signal
import statistics
import sys
import time
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from base_mmap_index_reader import mapped_sampler
from phase6_performance import identity

CONFIG = ROOT / 'configs/phase6/base_index_reader_benchmark.json'
RESULT = ROOT / 'reports/phase6/base_index_reader_benchmark_result.json'
SOURCES = ('scripts/benchmark_base_index_reader.py', 'scripts/base_mmap_index_reader.py',
           'scripts/base_kv_allocation_trainer.py', 'scripts/natural_context_contrast_corpus.py',
           'tests/test_base_mmap_index_reader.py', 'src/jmicro/model.py', 'uv.lock')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def prepare():
    if CONFIG.exists() or RESULT.exists():
        raise ValueError('Preserve prospective config and completed results')
    old_path = ROOT / 'configs/phase6/base_relu_squared_probe.json'
    old = read_json(old_path)
    tests = ROOT / 'reports/phase6/base_mmap_index_reader_tests.xml'
    import xml.etree.ElementTree as ET
    suite = ET.parse(tests).getroot().find('testsuite')
    if (suite is None or int(suite.attrib['tests']) != 8
            or int(suite.attrib['errors']) or int(suite.attrib['failures']) or int(suite.attrib['skipped'])):
        raise ValueError('Eight actual reader/whole-state/dual-direction resume CPU tests required')
    atomic_json(CONFIG, dict(created_at=now(), kind='bounded_counterbalanced_original_index_reader_CPU_v1',
        source_binding=old['source_binding'], tokenizer=old['tokenizer'],
        tokenizer_sha256=old['tokenizer_sha256'], goals=old['goals'], seed=42,
        schedule=['buffered', 'mmap', 'mmap', 'buffered', 'mmap', 'buffered', 'buffered', 'mmap'],
        warmup_batches=3, measured_batches=32, batch=80, CPU_cap_seconds=30,
        select_trials=[4, 5, 6, 7], minimum_fractional_speedup=.1,
        selection='Last BAAB cycle: mapped median supply seconds <=0.9 * buffered median, plus every row/full state identical in all trials and all32 draw traces match the earlier GPU probe.',
        timing='Only sampler.take(80) is timed. Setup, serialization and equality checks excluded; all included in CPU process cap. No model forward/backward, CUDA or learning.',
        cache='First ABBA cycle descriptive. Cache not flushed or controlled; repeat the identical finite cohort. Results do not predict cold-cache, full-corpus, GPU or long-training throughput.',
        limitations='One seed/cohort and two warm-cache repeats/backend. Original byte-weighted draws/accepted train/body+EOS/masks/quota/RNG/kind remain unchanged. New unique data and learning0.',
        failure='No changed trial subset, cap, threshold, seed, source, variants or automatic old FFN/MHA scientific budget reopening.',
        reference_GPU_result=old['proposal'],
        paired_GPU_result=dict(path=str(ROOT / 'reports/phase6/base-relu-squared-probe-20261007/result.json'),
            sha256=sha256(ROOT / 'reports/phase6/base-relu-squared-probe-20261007/result.json')),
        prior_probe_config=dict(path=str(old_path), sha256=sha256(old_path)),
        CPU_tests=dict(path=str(tests), sha256=sha256(tests)),
        source_sha256={name: sha256(ROOT / name) for name in SOURCES},
        new_GPU_seconds=0, new_scientific_gold_tokens=0, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False))
    print('Frozen CPU30s ABBA/BAAB reader benchmark; GPU/learning0')


def run():
    if RESULT.exists():
        raise ValueError('Preserve measured result; no automatic retries')
    c = read_json(CONFIG)
    for name, expected in c['source_sha256'].items():
        if sha256(ROOT / name) != expected:
            raise ValueError('Frozen benchmark source differs: ' + name)
    prior = c['paired_GPU_result']
    if sha256(Path(prior['path'])) != prior['sha256']:
        raise ValueError('Earlier paired GPU evidence differs')
    old = read_json(Path(prior['path']))
    reference = old['timing']['SwiGLU']['timed_updates']
    start = time.monotonic()
    def timeout(*args):
        raise TimeoutError('Fixed CPU30s exhausted; do not increase cap or retry unchanged')
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(c['CPU_cap_seconds'])
    job = dict(created_at=now(), status='running', actual_identity=identity(),
               config_sha256=sha256(CONFIG), GPU_seconds=0, learning_updates=0)
    job_path = RESULT.with_name('base_index_reader_benchmark_job.json')
    atomic_json(job_path, job)
    trials, baseline_rows, baseline_state = [], None, None
    try:
        codec = Tokenizer(ROOT / c['tokenizer'])
        if sha256(codec.path) != c['tokenizer_sha256']:
            raise ValueError('Pinned tokenizer identity differs')
        for index, backend in enumerate(c['schedule']):
            make = CEOnlyOriginalSampler if backend == 'buffered' else mapped_sampler
            b = c['source_binding']
            sampler = make(b['pool'], b['manifest_sha256'], codec, c['goals'], seed=c['seed'])
            try:
                if sampler.binding != b:
                    raise ValueError('Accepted original source binding differs')
                for _ in range(c['warmup_batches']):
                    sampler.take(c['batch'])
                batches, seconds = [], []
                for _ in range(c['measured_batches']):
                    tick = time.monotonic()
                    rows = sampler.take(c['batch'])
                    seconds.append(time.monotonic() - tick)
                    batches.append(rows)
                state = sampler.state_dict()
                if index == 0:
                    baseline_rows, baseline_state = batches, state
                rows_equal = equal_state(batches, baseline_rows)
                state_equal = equal_state(state, baseline_state)
                traces = [[[r['index_byte_position'], r['index_record_sha256'], r['target_first'],
                            r['target_end'], r['teacher_tokens']] for r in rows] for rows in batches]
                trace_equal = traces == [r['draw_trace'] for r in reference]
                gold = sum(r['teacher_tokens'] for rows in batches for r in rows)
                if not rows_equal or not state_equal or not trace_equal or gold != 308066:
                    raise ValueError('Original rows, full sampler, old draw trace or exact gold differs')
                trials.append(dict(index=index, backend=backend, batch_seconds=seconds,
                    supply_seconds=sum(seconds), original_gold=gold,
                    original_gold_per_supply_second=gold/sum(seconds),
                    rows_sha256=digest(batches), sampler_state_sha256=digest(state),
                    all_original_rows_equal=rows_equal, full_sampler_state_equal=state_equal,
                    all32_prior_GPU_draw_traces_equal=trace_equal,
                    source_teachers=state['consumed'], draws=state['draws'],
                    original_EOS_targets=sum(r['original_EOS_targets'] for rows in batches for r in rows),
                    valid_input_positions=sum(len(r['input_ids']) for rows in batches for r in rows)))
            finally:
                sampler.handle.close()
                sampler.tokens._mmap.close()
        selected = [trials[i] for i in c['select_trials']]
        medians = {kind: statistics.median(t['supply_seconds'] for t in selected if t['backend'] == kind)
                   for kind in ('buffered', 'mmap')}
        ratio = medians['mmap'] / medians['buffered']
        result = dict(created_at=now(), status='completed', config_sha256=sha256(CONFIG),
            actual_identity=job['actual_identity'], trials=trials, selected_trial_indices=c['select_trials'],
            warm_cycle_median_supply_seconds=medians, mmap_to_buffered_ratio=ratio,
            mmap_reader_selection_eligible=ratio <= 1-c['minimum_fractional_speedup'],
            actual_CPU_wall_seconds=time.monotonic()-start, CPU_cap_seconds=c['CPU_cap_seconds'],
            all_semantic_and_full_state_checks_passed=True,
            scientific_learning_updates=0, new_scientific_gold_tokens=0, new_unique_dataset_tokens=0,
            new_GPU_seconds=0, Base_complete=False, Base_adopted=False,
            Chat_started=False, quantization_started=False, protected_test_used=False,
            limitations=c['limitations'] + ' ' + c['cache'],
            old_FFN_and_MHA_caps_remain_closed=True,
            next_action='Retain only an eligible read-only input prototype; no automatic scientific launch. Select an independently justified Base comparison with its own frozen contract.')
        if result['actual_CPU_wall_seconds'] > c['CPU_cap_seconds']:
            timeout()
        atomic_json(RESULT, result)
        job.update(status='completed', exit_code=0, result_sha256=sha256(RESULT))
        atomic_json(job_path, job)
        print(json.dumps({k: result[k] for k in ('status', 'warm_cycle_median_supply_seconds',
            'mmap_to_buffered_ratio', 'mmap_reader_selection_eligible', 'actual_CPU_wall_seconds')}))
    except BaseException as error:
        job.update(status='failed', error=repr(error), actual_CPU_wall_seconds=time.monotonic()-start)
        atomic_json(job_path, job)
        raise
    finally:
        signal.alarm(0)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('prepare', 'run'))
    args = parser.parse_args()
    (prepare if args.mode == 'prepare' else run)()
