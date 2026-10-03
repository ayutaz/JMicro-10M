"""Persist a single identity-checked handoff after the complete corpus export."""
import argparse
import fcntl
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.corpus_state import read_json, write_json
from jmicro.experiment import ROOT, now, sha256


def alive(record):
    path = Path(f'/proc/{record["pid"]}/stat')
    try:
        return (Path('/proc/sys/kernel/random/boot_id').read_text().strip() == record['boot_id']
                and path.read_text().split()[21] == record['start_ticks'])
    except FileNotFoundError:
        return False


def ready(output, job):
    path = output/'manifest.json'
    if job['stage'] != 'full_independent_serial_audit' or not path.exists():
        return False
    built = read_json(path)
    config = ROOT/'configs/phase6/corpus_10b.json'
    if (built['config_sha256'] != sha256(config) or not built['target_met'] or
            built['splits']['train']['tokens'] < read_json(config)['minimum_train_stream_tokens']):
        raise ValueError('Completed export does not meet the frozen target')
    artifact = Path(built['artifact_directory']).resolve()
    artifact.relative_to(output.resolve())
    if read_json(artifact/'shards/manifest.json')['splits'] != built['splits']:
        raise ValueError('Completed export and shard counts differ')
    for snapshot in ('source_snapshot.json', 'execution_v3_snapshot.json'):
        for relative, expected in read_json(output/snapshot).items():
            if sha256(ROOT/relative) != expected:
                raise ValueError(f'Frozen source changed: {relative}')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--observe-only', action='store_true')
    args = parser.parse_args()
    expected = read_json(args.output/'job.json')
    if expected['execution'] != 'parallel_bands_v3':
        raise ValueError('This one-time handoff is only for the v3 pipeline')
    if args.observe_only:
        print({'identified_process_live': alive(expected), 'export_ready': ready(args.output, expected)})
        return
    with (args.output/'audit_handoff.lock').open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        record = dict(status='waiting_for_completed_export', pid=os.getpid(), started_at=now(),
                      boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
                      start_ticks=Path('/proc/self/stat').read_text().split()[21],
                      source_sha256=sha256(Path(__file__)), prior_identity=expected)
        destination = args.output/'audit_handoff.json'
        write_json(destination, record)
        try:
            deadline = time.monotonic()+5400
            while time.monotonic() < deadline:
                job = read_json(args.output/'job.json')
                if any(job[k] != expected[k] for k in ('pid', 'boot_id', 'start_ticks', 'execution')):
                    raise RuntimeError('Pipeline identity changed; do not signal or restart')
                if job['status'] == 'complete':
                    record.update(status='prior_pipeline_completed', completed_at=now())
                    return
                if job['status'] != 'running' or not alive(job):
                    raise RuntimeError('Prior pipeline stopped before the handoff; inspect its evidence')
                if ready(args.output, job):
                    break
                time.sleep(10)
            else:
                raise TimeoutError('Export handoff observation exceeded90minutes; no signal sent')
            # Recheck the exact boot/PID/start identity immediately before the one signal.
            if not alive(expected):
                raise RuntimeError('Prior identity disappeared before signal')
            record.update(status='waiting_for_prior_exit', signal_sent_at=now())
            write_json(destination, record)
            os.kill(expected['pid'], signal.SIGINT)
            exit_deadline = time.monotonic()+300
            while alive(expected) and time.monotonic() < exit_deadline:
                time.sleep(1)
            if alive(expected):
                raise TimeoutError('Prior process did not exit after SIGINT; no replacement launched')
            retired = read_json(args.output/'job.json')
            if retired['status'] == 'running' or 'cumulative_seconds' not in retired:
                raise RuntimeError('Prior terminal state/runtime was not persisted')
            write_json(args.output/'job-v3-retired.json', retired)
            record.update(status='cached_audit_running', retired_at=now())
            write_json(destination, record)
            # The existing audit runner rechecks target, source, cache gates and pipeline lock.
            subprocess.run(['bash', str(ROOT/'scripts/run_corpus_10b_cached_audit.sh')], check=True)
            record.update(status='cached_audit_completed', completed_at=now())
        except Exception as exc:
            record.update(status='failed', failure=f'{type(exc).__name__}: {exc}', completed_at=now())
            raise
        finally:
            write_json(destination, record)


if __name__ == '__main__':
    main()
