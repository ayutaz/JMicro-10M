"""Resume only a completed corpus export with unchanged serial audit checks."""
import argparse
from datetime import datetime, timezone
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.cached_corpus_audit import audit_with_cache
from jmicro.corpus_state import read_json, write_json
from jmicro.experiment import ROOT, now, sha256
from jsonschema import Draft202012Validator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT/'configs/phase6/corpus_10b.json')
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    c = read_json(args.config)
    Draft202012Validator(read_json(ROOT/'schemas/configs/phase6/corpus_10b.schema.json')).validate(c)
    with (args.output/'pipeline.lock').open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        prior = read_json(args.output/'job.json')
        boot = Path('/proc/sys/kernel/random/boot_id').read_text().strip()
        proc = Path(f'/proc/{prior["pid"]}/stat')
        if proc.exists() and boot == prior['boot_id'] and proc.read_text().split()[21] == prior['start_ticks']:
            raise RuntimeError('The identified prior pipeline is still alive')
        if prior['config_sha256'] != sha256(args.config):
            raise ValueError('Frozen configuration differs')
        for snapshot in ('source_snapshot.json', 'execution_v3_snapshot.json'):
            for relative, expected in read_json(args.output/snapshot).items():
                if sha256(ROOT/relative) != expected:
                    raise ValueError(f'Frozen source changed: {relative}')
        built = read_json(args.output/'manifest.json')
        if (built['config_sha256'] != sha256(args.config) or not built['target_met'] or
            built['splits']['train']['tokens'] < c['minimum_train_stream_tokens']):
            raise ValueError('A complete at-least10B export is required before audit handoff')
        Path(built['artifact_directory']).resolve().relative_to(args.output.resolve())
        probe = read_json(ROOT/'reports/phase6/corpus_10b_feature_cache_probe.json')
        integration = read_json(ROOT/'reports/phase6/corpus_10b_feature_cache_integration.json')
        if (not probe['sampled_adoption_gate_passed'] or not integration['adoption_gate_passed'] or
            not integration['groups_exact'] or not integration['duplicates_exact'] or
            integration['records'] != 1000000 or integration['bands'] != 32 or
            any(m['candidate_pairs'] != 524480 for m in integration['measurements']) or
            len({m['score_stream_sha256'] for m in integration['measurements']}) != 1 or
            sha256(ROOT/'src/jmicro/feature_cache.py') != probe['feature_cache_source_sha256']):
            raise ValueError('Measured cache equivalence gates have not passed')
        used = prior.get('cumulative_seconds')
        if used is None:
            # A crashed process may not have saved its final elapsed time.
            age = (datetime.now(timezone.utc)-datetime.fromisoformat(prior['started_at'])).total_seconds()
            used = prior.get('prior_cumulative_seconds', 0) + max(0, age)
        if used >= c['runtime_budget_seconds']:
            raise TimeoutError('Cumulative24hour preparation budget exhausted')
        if shutil.disk_usage(args.output).free < c['minimum_free_bytes']:
            raise RuntimeError('Insufficient disk reserve')
        extra = ['src/jmicro/feature_cache.py', 'src/jmicro/cached_corpus_audit.py',
                 'scripts/run_corpus_10b_cached_audit.py', 'scripts/run_corpus_10b_cached_audit.sh',
                 'reports/phase6/corpus_10b_feature_cache_probe.json',
                 'reports/phase6/corpus_10b_feature_cache_integration.json',
                 'reports/phase6/corpus_10b_feature_cache_integration.py']
        destination = args.output/'execution_v4_snapshot'
        hashes = {}
        for relative in extra:
            target = destination/relative
            if target.exists() and sha256(target) != sha256(ROOT/relative):
                raise ValueError(f'Audit execution source changed: {relative}')
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                shutil.copyfile(ROOT/relative, target)
            hashes[relative] = sha256(target)
        write_json(args.output/'execution_v4_snapshot.json', hashes)
        record = dict(status='running', pid=os.getpid(), started_at=now(), command=sys.argv,
                      config_sha256=sha256(args.config), execution='bounded_feature_cache_audit_v4',
                      boot_id=boot, start_ticks=Path('/proc/self/stat').read_text().split()[21],
                      prior_cumulative_seconds=used, stage='full_independent_serial_audit',
                      heartbeat_at=now())
        started = time.monotonic()

        def interrupted(signum, frame):
            raise InterruptedError(f'Audit interrupted by signal{signum}; preserve completed export')

        def exhausted(signum, frame):
            raise TimeoutError('Cumulative24hour preparation budget exhausted')

        signal.signal(signal.SIGINT, interrupted)
        signal.signal(signal.SIGTERM, interrupted)
        signal.signal(signal.SIGALRM, exhausted)
        signal.alarm(max(1, int(c['runtime_budget_seconds']-used)))
        write_json(args.output/'job.json', record)
        try:
            existing = args.output/'corpus_audit.json'
            if existing.exists():
                report = read_json(existing)
                if report['status'] != 'passed' or report['manifest_sha256'] != sha256(args.output/'manifest.json'):
                    raise ValueError('Existing full audit binding differs')
                record['feature_cache_used'] = False
            else:
                spec = importlib.util.spec_from_file_location('original_corpus_auditor', ROOT/'scripts/audit_corpus_10b.py')
                auditor = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(auditor)
                report = audit_with_cache(auditor, args.config, args.raw, args.output, c['workers'])
                record['feature_cache_used'] = True
            record.update(status='complete', completed_at=now())
            print(json.dumps({'status':'complete', 'train_tokens':report['splits']['train']['tokens']}), flush=True)
        except Exception as exc:
            record.update(status='failed', completed_at=now(), failure=f'{type(exc).__name__}: {exc}')
            raise
        finally:
            record['cumulative_seconds'] = used + time.monotonic()-started
            signal.alarm(0)
            write_json(args.output/'job.json', record)


if __name__ == '__main__':
    main()
