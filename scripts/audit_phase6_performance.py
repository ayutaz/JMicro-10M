"""Read-only audit of measured Phase 6 performance and strict training state.

Run through uv after a study completes. Recompute evidence from checkpoints,
metrics, operator traces and source snapshots; do not start CUDA training.
"""
from pathlib import Path
import argparse
import json
import math
import statistics
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jsonschema import validate
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.phase5 import equal_state
from jmicro.training import implementation_hashes


def finite(state):
    values = list(state['model'].values())
    values += [value for item in state['optimizer']['state'].values() for value in item.values()
               if isinstance(value, torch.Tensor)]
    return all(torch.isfinite(value).all().item() for value in values)


def audit(study, destination):
    torch.set_num_threads(2)
    report = read_json(study/'batch_performance_report.json')
    binding = read_json(study/'binding.json')
    plan = read_json(study/'snapshot/configs/phase6/performance.json')
    validate(plan, read_json(study/'snapshot/schemas/configs/phase6/performance.schema.json'))
    checks = {}
    evidence = {'study': str(study), 'report_sha256': sha256(study/'batch_performance_report.json'),
                'binding': binding, 'protocol': plan, 'auditor_sha256': sha256(Path(__file__)), 'exact': {}, 'resource_summary': {}}
    selected_model = read_json(ROOT/'reports/phase5/candidate_configs.json')['100m-no-qknorm']['model_config']
    def check(name, passed):
        checks[name] = bool(passed)
    check('study_complete', read_json(study/'job.json')['status'] == 'complete' and report['status'] == 'passed')
    check('report_binding_exact', report['binding'] == binding)
    check('current_implementation_exact', implementation_hashes() == binding['implementation'])
    check('frozen_plan_exact', sha256(study/'snapshot/configs/phase6/performance.json') == binding['plan_sha256'])
    check('frozen_runner_exact', sha256(study/'snapshot/scripts/phase6_performance.py') == binding['runner_sha256'])
    source_hashes = read_json(study/'source_sha256.json')
    check('all_snapshot_files_exact', all(sha256(study/'snapshot'/name) == expected for name, expected in source_hashes.items()))
    check('data_tokenizer_exact', sha256(Path(plan['shards'])/'manifest.json') == plan['shard_manifest_sha256']
          and sha256(ROOT/plan['tokenizer']) == plan['tokenizer_sha256'])
    gpu = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi', '--query-compute-apps=pid,process_name', '--format=csv,noheader'], text=True, capture_output=True, check=True)
    check('no_active_cuda_compute_job', not gpu.stdout.strip())
    for name in ('pid',):
        job = read_json(study/'job.json')
        proc = Path(f'/proc/{job[name]}/stat')
        original_alive = proc.exists() and proc.read_text().split()[21] == job['start_ticks'] and Path('/proc/sys/kernel/random/boot_id').read_text().strip() == job['boot_id']
        check('supervisor_original_identity_gone', not original_alive)
    check('all_initial_variants_recorded', all((study/'results'/f"initial-{variant['name']}-b8.json").exists() for variant in plan['variants']))
    for result_path in sorted((study/'results').glob('*.json')):
        item = read_json(result_path)
        label = result_path.stem
        request_path = study/'requests'/result_path.name
        request = read_json(request_path)
        check(f'{label}_request_sha', sha256(request_path) == item['request_sha256'])
        check(f'{label}_source_and_plan', request['implementation_sha256'] == binding['implementation'] and request['plan'] == plan)
        check(f'{label}_terminal', item['status'] in ('passed', 'oom', 'failed'))
        if item['status'] != 'passed':
            check(f'{label}_failure_preserved', bool(item.get('failure')) and (study/'logs'/f'{label}.log').exists())
            continue
        check(f'{label}_checkpoint_sha', sha256(Path(item['checkpoint'])) == item['checkpoint_sha256'])
        run_record = read_json(Path(request['run'])/'run.json')
        environment = read_json(Path(request['run'])/'environment.json')
        check(f'{label}_selected_model_and_source', run_record['model_config'] == selected_model
              and run_record['implementation_sha256'] == binding['implementation'])
        check(f'{label}_actual_wsl_cuda_bf16_python', environment['platform']['is_wsl']
              and environment['platform']['system'] == 'Linux' and environment['platform']['python'] == '3.12.7'
              and environment['torch_probe']['cuda_available'] and environment['torch_probe']['bf16_supported']
              and 'RTX 4090' in environment['nvidia_smi']['stdout'])
        check(f'{label}_finite_metrics', all(math.isfinite(item[key]) and item[key] > 0 for key in ('steady_tokens_per_second', 'p95_update_seconds')))
        check(f'{label}_cuda_evaluation_isolated', item['evaluation_state_isolated'] and item['evaluation_documents'] == plan['evaluation_documents'] and item['generation_outputs'] == plan['generation_cases'])
        if request['kind'] in ('probe', 'confirmation'):
            trace = read_json(Path(request['run'])/'attention_profile.json')
            operators = trace['operators']
            actual = operators.get('aten::_scaled_dot_product_flash_attention', 0) > 0 if item['variant']['backend'] == 'flash' else operators.get('aten::_scaled_dot_product_flash_attention', 0) == 0 and operators.get('aten::bmm', 0) > 0
            if not actual and trace.get('generated_code'):
                code_path = Path(trace['generated_code'])
                code = code_path.read_text()
                contains_flash = 'torch.ops.aten._scaled_dot_product_flash_attention.default(' in code
                contains_math = 'extern_kernels.bmm(' in code
                compiled_calls = [name for name in operators if name.startswith('## Call CompiledFxGraph ')]
                actual = bool(compiled_calls and sha256(code_path) == trace['generated_code_sha256']
                    and (contains_flash if item['variant']['backend'] == 'flash' else not contains_flash and contains_math))
            check(f'{label}_actual_attention_backend', actual and trace['requested_backend'] == item['variant']['backend'] and trace['actual_backend_verified'])
            rows = [json.loads(line) for line in (Path(request['run'])/'metrics.jsonl').read_text().splitlines()]
            measured = rows[request['measurement_warmup']:] if request['kind'] == 'probe' else rows[min(20, len(rows)//4):]
            measured = [row for row in measured if not row.get('profiled')]
            check(f'{label}_speed_recomputed_without_profile', statistics.median(row['tokens_per_second'] for row in measured) == item['steady_tokens_per_second'])
            if item['variant']['compile']:
                check(f'{label}_compile_cache_backend_separated', f"jmicro-v1-{item['variant']['backend']}-" in item['compile_cache'] and trace['compile_cache'] == item['compile_cache'])
    common = ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens',
              'body_bytes', 'token_digest', 'spec', 'model_config', 'implementation_sha256', 'update')
    for variant_name, capacity in report['capacity'].items():
        if capacity['status'] == 'rejected_exact_resume':
            check(f'{variant_name}_resume_failure_preserved', capacity['verification']['status'] == 'failed')
            continue
        maximum = capacity['maximum_stable_batch']
        high = capacity['first_oom_batch']
        check(f'{variant_name}_capacity_is_confirmed', str(maximum) in capacity['confirmed'])
        check(f'{variant_name}_boundary_explained', high == maximum+1 if capacity['boundary_exact'] else high is None and maximum == plan['maximum_batch_probe'])
        if high is not None:
            check(f'{variant_name}_boundary_oom_actual', read_json(study/'results'/f'capacity-{variant_name}-b{high}.json')['status'] == 'oom')
        for batch_text, confirmation in capacity['confirmed'].items():
            batch = int(batch_text)
            label = f'{variant_name}-b{batch}'
            directory = study/'exact'/label
            isolated = read_json(directory/'branch-isolation.json')
            check(f'{label}_parent_all_files_isolated', isolated['passed'] and isolated['before'] == isolated['after']
                  and isolated['before'] == read_json(directory/'parent-before-branches.json'))
            check(f'{label}_parent_checkpoint_still_exact', all(sha256(Path(path)) == expected for path, expected in isolated['before'].items() if Path(path).name.startswith('checkpoint-')))
            for prefix in ('stable', 'decay'):
                paths = [directory/f'{prefix}-{suffix}' for suffix in ('continuous', 'resumed')]
                states = [torch.load(path/'checkpoint-00000200.pt', map_location='cpu', weights_only=False) for path in paths]
                for key in common + (('lineage', 'branch_updates', 'branch_tokens') if prefix == 'decay' else ()):
                    check(f'{label}_{prefix}_{key}_exact', equal_state(states[0][key], states[1][key]))
                rows = [[json.loads(line) for line in (path/'metrics.jsonl').read_text().splitlines()] for path in paths]
                check(f'{label}_{prefix}_updates_budget', all(len(values) == (200 if prefix == 'stable' else 100) for values in rows)
                      and all(state['tokens'] == 200*batch*1024 and state['update'] == 200 for state in states))
                for key in ('update', 'loss', 'lr', 'gradient_norm', 'tokens_seen', 'supervised_tokens', 'body_bytes_seen', 'token_digest'):
                    check(f'{label}_{prefix}_{key}_history_exact', [row[key] for row in rows[0]] == [row[key] for row in rows[1]])
                check(f'{label}_{prefix}_finite_all_state', all(finite(state) for state in states))
                if prefix == 'decay':
                    check(f'{label}_independent_decay_budget', all(state['branch_updates'] == 100 and state['branch_tokens'] == 100*batch*1024
                          and sha256(Path(state['lineage']['parent_checkpoint'])) == state['lineage']['parent_sha256'] for state in states))
                del states
            evidence['exact'][label] = {'independently_recomputed': True, 'report': str(directory/'exact_report.json')}
            repetitions = confirmation['confirmations']
            check(f'{label}_three_confirmation_runs', len(repetitions) == 3 and all(row['status'] == 'passed' and row['update'] == 200 for row in repetitions))
            check(f'{label}_median_recomputed', statistics.median(row['steady_tokens_per_second'] for row in repetitions) == confirmation['median_tokens_per_second'])
            telemetry = []
            for repeat in range(3):
                values = read_json(study/'telemetry'/f'confirm-{variant_name}-b{batch}-{repeat}.json')
                valid = [list(map(float, value['gpu_util_memory_mib_power_w'].split(','))) for value in values if value['exit_code'] == 0 and value['gpu_util_memory_mib_power_w']]
                telemetry.extend(valid)
            check(f'{label}_driver_telemetry_actual', bool(telemetry) and all(len(row) == 4 and all(math.isfinite(value) for value in row) for row in telemetry))
            evidence['resource_summary'][label] = {'median_tokens_per_second': confirmation['median_tokens_per_second'],
                'peak_allocated_bytes_including_save_eval': confirmation['peak_vram_bytes'],
                'peak_reserved_bytes_including_save_eval': max(row['peak_vram_reserved_with_evaluation_save'] for row in repetitions),
                'driver_peak_memory_mib': max(row[1] for row in telemetry), 'driver_memory_total_mib': max(row[2] for row in telemetry),
                'gpu_utilization_max_percent': max(row[0] for row in telemetry),
                'gpu_utilization_median_all_samples_percent': statistics.median(row[0] for row in telemetry),
                'power_peak_watts': max(row[3] for row in telemetry),
                'data_wait_fraction': sum(row['data_wait_seconds'] for row in repetitions)/sum(row['measured_seconds'] for row in repetitions),
                'save_seconds': [row['save_seconds'] for row in repetitions],
                'evaluation_seconds': [row['evaluation_seconds'] for row in repetitions],
                'effective_tokens_per_update': batch*1024,
                'telemetry_limit': '2s samples include startup/save/eval; GPU utilization is not MFU'}
    confirmed = [item for capacity in report['capacity'].values() if capacity['status'] == 'verified' for item in capacity['confirmed'].values()]
    check('selected_fastest_fully_verified', report['selected'] == max(confirmed, key=lambda item: item['median_tokens_per_second']))
    check('quality_and_long_training_not_claimed', report['not_achieved'] == ['Base/Chat quality', 'long Base training', 'long-run effective batch/LR/WSD budget freeze'])
    result = {'status': 'passed' if all(checks.values()) else 'failed', 'completed_at': now(), 'checks': checks, 'evidence': evidence}
    write_json(destination, result)
    print(json.dumps({'status': result['status'], 'checks': len(checks), 'failed': [key for key, value in checks.items() if not value]}))
    if result['status'] != 'passed':
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    audit(arguments.study.resolve(), arguments.output.resolve())
