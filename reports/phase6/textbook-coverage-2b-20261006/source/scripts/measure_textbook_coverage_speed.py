"""Bounded paired save-cadence measurement; all optimizer updates are discarded."""
import gc
import json
import statistics
import sys
import time
from pathlib import Path

import run_textbook_coverage as coverage
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, gpu_lock
from phase6_performance import alive, identity, finite_state
from run_eos_short_pilot import equal_state

RUN = ROOT / 'reports/phase6/textbook-coverage-save-cadence-20261006'
UPDATES = 64
GPU_LIMIT = 120


def main():
    assert sys.version_info[:3] == (3, 12, 7)
    config, base, parent, _ = coverage.inspect(coverage.PROBE_CONFIG)
    prior = coverage.probe_evidence()
    RUN.mkdir(parents=True, exist_ok=True)
    job_path = RUN / 'job.json'
    if job_path.exists():
        raise ValueError('Inspect existing measurement; do not overwrite or duplicate')
    job = dict(status='setup', **identity(), started_at=now(), GPU_budget_seconds=GPU_LIMIT,
               original_probe_config_sha256=sha256(coverage.PROBE_CONFIG),
               original_probe_result_sha256=sha256(coverage.RUN/'probe/result.json'),
               source_sha256=sha256(Path(__file__)), scientific_teacher_tokens=0,
               weights_discarded_for_science=True)
    atomic_json(job_path, job)
    (RUN/'source').mkdir(exist_ok=True)
    (RUN/'source'/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    started = None
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        web = coverage.TrainView(base['web_shards'], base['web_manifest_sha256'])
        pool = coverage.TrainView(config['pool']['pool'], config['pool']['manifest_sha256'])
        pool.index = coverage.CachedThreeSourceIndex(pool)
        assert pool.index.cache_reused
        zero = torch.load(base['parent']['path'], map_location='cpu', weights_only=False)
        binding = coverage.stable_binding(config, coverage.PROBE_CONFIG, parent)
        records, states = {}, []
        with gpu_lock('cuda'):
            started = time.monotonic()
            for route in ('continuous', 'save_every_update'):
                folder = RUN/route
                folder.mkdir(exist_ok=True)
                trainer = coverage.ExtendedCurveTrainer(zero, web, pool, 'shuffle',
                    dict(web=0, short=coverage.TARGET), binding)
                trainer.load_extension(config['parent']['path'])
                rows, save_seconds = [], 0.
                route_started = time.monotonic()
                with (folder/'metrics.jsonl').open('w', buffering=1) as stream:
                    for index in range(UPDATES):
                        if time.monotonic()-started > GPU_LIMIT:
                            raise TimeoutError('Save-cadence measurement GPU budget exhausted')
                        row = trainer.step()
                        rows.append(row)
                        stream.write(json.dumps(row, allow_nan=False)+'\n')
                        if route == 'save_every_update':
                            save_seconds += trainer.save(folder/'checkpoint.pt')
                        if (index+1) % 16 == 0:
                            job.update(status='running', stage=route, updates=index+1,
                                heartbeat_at=now(), GPU_elapsed_seconds=time.monotonic()-started)
                            atomic_json(job_path, job)
                            print(json.dumps(dict(route=route, updates=index+1,
                                seconds=row['seconds'], data_wait=row['data_wait_seconds'])), flush=True)
                wall_seconds = time.monotonic()-route_started
                checkpoint = folder/'checkpoint.pt'
                if route == 'continuous':
                    trainer.save(checkpoint)
                state = torch.load(checkpoint, map_location='cpu', weights_only=False)
                assert finite_state(state)
                assert all(equal_state(row[k], old[k]) for row, old in
                    zip(rows[:16], prior['timing']['histories'], strict=True)
                    for k in ('loss','gradient_norm','lr','token_digest','source_teachers',
                              'valid_input_tokens','physical_input_tokens'))
                states.append(state)
                records[route] = dict(histories=rows, checkpoint=str(checkpoint),
                    checkpoint_sha256=sha256(checkpoint), GPU_optimizer_updates=UPDATES,
                    verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                    median_step_seconds=statistics.median(r['seconds'] for r in rows[16:]),
                    median_data_wait_seconds=statistics.median(r['data_wait_seconds'] for r in rows[16:]),
                    measured_warmup_updates=16, measured_steady_updates=48,
                    save_seconds=save_seconds, wall_seconds=wall_seconds,
                    peak_allocated_VRAM_bytes=torch.cuda.max_memory_allocated())
                del trainer
                gc.collect()
                torch.cuda.empty_cache()
            checks = {key: equal_state(states[0][key], states[1][key]) for key in
                ('model','optimizer','scheduler','rng','sampler','lineage','tokens',
                 'supervised_tokens','body_bytes','token_digest','update','spec',
                 'model_config','pilot_binding')}
            checks['finite'] = all(finite_state(state) for state in states)
            assert all(checks.values()), checks
            elapsed = time.monotonic()-started
            assert elapsed <= GPU_LIMIT
            result = dict(job, status='paired_save_cadence_measurement_complete',
                records=records, checks=checks, passed=True, GPU_seconds=elapsed,
                verification_teacher_tokens=sum(r['verification_teacher_tokens'] for r in records.values()),
                scientific_teacher_tokens=0, weights_discarded_for_science=True)
            atomic_json(RUN/'result.json', result)
            job.update(status='complete', GPU_elapsed_seconds=elapsed, completed_at=now())
    except BaseException as error:
        job.update(status='failed', error=repr(error))
        if started is not None:
            job['GPU_elapsed_seconds'] = time.monotonic()-started
        raise
    finally:
        atomic_json(job_path, job)


if __name__ == '__main__':
    main()
