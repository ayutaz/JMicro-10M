"""Read-only process/lock/source observation, without importing ML or parsing TEST."""
import hashlib
import json
import os
from pathlib import Path
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT/'reports/phase6/base-document-balance-comparison-20261014'


def read(path): return json.loads(path.read_text())
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def live(identity):
    proc = Path('/proc')/str(identity['pid'])
    if not proc.exists(): return False
    stat = (proc/'stat').read_text()
    # Fields following ')' start at state, index0; starttime is field22.
    fields = stat[stat.rindex(')')+2:].split()
    return (fields[0] != 'Z' and fields[19] == str(identity['start_ticks'])
        and Path('/proc/sys/kernel/random/boot_id').read_text().strip() == identity['boot_id'])


def main():
    config_path = ROOT/'configs/phase6/base_document_balance_comparison.json'
    c = read(config_path)
    job = read(RUN/'job.json')
    assert job['config_sha256'] == digest(config_path)
    assert all(digest(ROOT/p) == sha for p, sha in c['source_sha256'].items())
    policy_path = ROOT/'configs/phase6/base_document_balance_review.json'
    policy = read(policy_path)
    assert policy['config_sha256'] == digest(config_path)
    assert all(digest(ROOT/p) == sha for p, sha in policy['helper_sha256'].items())
    assert all(digest(Path(ref['path'])) == ref['sha256'] for ref in policy['references'].values())
    probe = read(Path(c['probe_result']['path']))
    assert probe['passed'] and all(probe['all_resume_and_source_checks'].values())
    assert all(probe['initial_checks'].values())
    assert job['GPU_occupancy_seconds'] <= c['GPU_budget_seconds']
    actual_live = live(job)
    lock = Path('/home/aihub_ubuntu/jmicro-data/gpu.lock')
    owners = []
    if lock.exists():
        info = lock.stat()
        key = f'{os.major(info.st_dev):02x}:{os.minor(info.st_dev):02x}:{info.st_ino}'
        owners = [int(parts[4]) for line in Path('/proc/locks').read_text().splitlines()
            if len(parts := line.split()) >= 6 and parts[1] == 'FLOCK' and parts[5] == key]
    if actual_live and job['status'] == 'running':
        assert owners == [job['pid']], ('Expected actual kernel lock owner', owners)
        command = (Path('/proc')/str(job['pid'])/'cmdline').read_bytes()
        assert b'scripts/run_base_document_balance.py' in command
    cp = Path(job['latest_checkpoint']) if job.get('latest_checkpoint') else None
    evidence = dict(observed_at=datetime.now(timezone.utc).isoformat(),
        actual_identity={k: job[k] for k in ('pid','boot_id','start_ticks')},
        actual_process_live=actual_live, kernel_GPU_lock_owners=owners,
        job_status=job['status'], stage=job.get('stage'),
        completed_updates=job.get('completed_updates',0),
        consumed_original_teachers=job.get('original_teachers',0),
        goal_original_teachers=c['scientific_CE_teacher_tokens'],
        GPU_seconds=job['GPU_occupancy_seconds'], GPU_cap_seconds=c['GPU_budget_seconds'],
        checkpoint_path=str(cp) if cp else None,
        checkpoint_exists=cp.is_file() if cp else False,
        checkpoint_bytes=cp.stat().st_size if cp and cp.is_file() else None,
        frozen_scientific_and_review_sources_verified=True,
        original_quality_references_verified=True, CUDA_full_state_gate_verified=True,
        observer_GPU_work=False, observer_TEST_read=False,
        scientific_quality_confirmed=False, requested_six_stages_complete=False,
        Base_adopted=False, Chat_started=False, quantization_started=False,
        next_action='Poll this identity/job; when terminal, audit exact100M state and read all80 raw outputs before frozen policy review. Never relaunch on an observation timeout.')
    destination = RUN/'active_observation.json'
    temporary = destination.with_suffix('.tmp')
    temporary.write_text(json.dumps(evidence, indent=2, ensure_ascii=False)+'\n')
    temporary.replace(destination)
    print(json.dumps(evidence, ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
