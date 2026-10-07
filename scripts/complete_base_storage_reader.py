"""Record actual storage/UI and completed CPU reader evidence without learning."""
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    output = ROOT / 'reports/phase6/base_storage_reader_completion_20261007.json'
    if output.exists():
        raise ValueError('Preserve completed evidence')
    result_path = ROOT / 'reports/phase6/base_index_reader_benchmark_result.json'
    result = read_json(result_path)
    job = read_json(ROOT / 'reports/phase6/base_index_reader_benchmark_job.json')
    config = read_json(ROOT / 'configs/phase6/base_index_reader_benchmark.json')
    if (result['status'] != 'completed' or job['exit_code'] != 0 or alive(job['actual_identity'])
            or not result['all_semantic_and_full_state_checks_passed']
            or result['actual_CPU_wall_seconds'] > config['CPU_cap_seconds']
            or result['config_sha256'] != sha256(ROOT / 'configs/phase6/base_index_reader_benchmark.json')
            or job['result_sha256'] != sha256(result_path)):
        raise ValueError('Actual finite completed reader benchmark required')
    server = read_json(ROOT / 'reports/local/webui/server.json')
    identity = {key: server[key] for key in ('pid', 'boot_id', 'start_ticks')}
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=10) as response:
        model = json.load(response)
    expected = '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    if (not alive(identity) or model['checkpoint_sha256'] != expected
            or model['training_tokens'] != 10000007168 or model['busy']):
        raise ValueError('Original unadopted10B UI actual identity/HTTP required')
    storage = shutil.disk_usage('/home/aihub_ubuntu/jmicro-data')
    if storage.free < 900 * 1024**3:
        raise ValueError('Actual expanded filesystem free capacity missing')
    environment = read_json(ROOT / 'reports/phase6/wsl-storage-expansion-20261007/environment-after.json')
    if (environment['platform']['python'] != '3.12.7' or not environment['platform']['is_wsl']
            or not environment['torch_probe']['cuda_available']
            or not environment['torch_probe']['bf16_supported']):
        raise ValueError('WSL pinned interpreter/CUDA/BF16 unavailable after restart')
    uv = subprocess.run(['/home/aihub_ubuntu/.local/bin/uv', '--version'], capture_output=True, text=True, check=True)
    process = subprocess.run(['ps', '-eo', 'pid,args'], capture_output=True, text=True, check=True)
    script_processes = [line for line in process.stdout.splitlines() if 'scripts/' in line and 'python' in line]
    atomic_json(output, dict(created_at=now(), status='storage_expanded_reader_comparison_complete',
        WSL_distribution='Ubuntu', disk_command='wsl --manage Ubuntu --resize 2TB',
        disk_official_instructions='https://learn.microsoft.com/en-us/windows/wsl/disk-space',
        disk_target='2TB', disk=dict(total_bytes=storage.total, used_bytes=storage.used, available_bytes=storage.free),
        disk_limit_not_physical_preallocation=True, rebooted_boot_id=identity['boot_id'],
        uv_absolute_version=uv.stdout.strip(),
        environment_observation='Capture used absolute uv launcher; PATH-only uv/powershell availability probes are false. Native execution snapshot Git HEAD is not Windows authoritative Git HEAD. Neither is a failed CUDA/BF16 or interpreter probe.',
        environment=dict(path=str(ROOT / 'reports/phase6/wsl-storage-expansion-20261007/environment-after.json'),
            sha256=sha256(ROOT / 'reports/phase6/wsl-storage-expansion-20261007/environment-after.json')),
        accepted_source_binding_after_restart=config['source_binding'],
        accepted_source_identity_checked_by_all8_samplers=True, corpus_rescan_or_rehash=False,
        reader_result=dict(path=str(result_path), sha256=sha256(result_path)),
        reader_actual_identity=job['actual_identity'], reader_actual_process_absent_verified=True,
        warm_cycle_median_supply_seconds=result['warm_cycle_median_supply_seconds'],
        mmap_to_buffered_ratio=result['mmap_to_buffered_ratio'],
        mmap_reader_selection_eligible=result['mmap_reader_selection_eligible'],
        reader_adopted_for_training=False,
        decision='Prototype failed the prospective10% speedup criterion on this cohort; retain existing buffered reader. No universal mmap failure claim or architecture timing claim.',
        actual_script_processes=script_processes, UI=dict(actual_identity=identity, actual_alive_verified=True,
            HTTP_model=model, checkpoint_rehash=False),
        new_scientific_gold_tokens=0, new_unique_dataset_tokens=0, new_GPU_training_seconds=0,
        independent_trained_seed_done=False, full_dev_done=False, protected_test_used=False,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        old_FFN_and_MHA_caps_remain_closed=True,
        next_action='Choose an independently justified Base comparison from the archived failures. Do not change thresholds or automatically retry closed recipes. Only a quality-qualified candidate proceeds to independent trained seed/full DEV/protected TEST/adoption; then notify and stop.'))
    print('Completed: ~968GiB free, original UI alive, source binding retained, reader unadopted, Base incomplete')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
