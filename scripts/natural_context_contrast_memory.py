"""Process-local allocation guard, with actual worst-shape resident selection."""
import json
from pathlib import Path
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src')]
import torch
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json

FRACTION = .90


def configure_resident_memory(expected_worst_peak):
    properties = torch.cuda.get_device_properties(0)
    if expected_worst_peak >= FRACTION*properties.total_memory:
        raise ValueError('Measured worst-shape allocation exceeds resident CUDA allowance')
    torch.cuda.set_per_process_memory_fraction(FRACTION, 0)
    actual = torch.cuda.memory.get_per_process_memory_fraction(0)
    # The allocator stores an integer byte quota, so the returned fraction
    # differs by its sub-byte truncation; compare the actual byte allowance.
    allowance = round(actual*properties.total_memory)
    if allowance != int(FRACTION*properties.total_memory):
        raise ValueError('Actual native allocator fraction differs')
    return dict(torch_version=torch.__version__, device=properties.name,
        visible_device_bytes=properties.total_memory, process_fraction=actual,
        allocator_allowance_bytes=allowance,
        expected_worst_peak_bytes=expected_worst_peak)


def main():
    output = ROOT/'reports/phase6/natural_context_contrast_memory_policy.json'
    if output.exists():
        raise ValueError('Preserve actual process-local memory-policy evidence')
    result_path = ROOT/'reports/phase6/natural-context-contrast-corpus-probe-20261007/result.json'
    result = json.loads(result_path.read_text())
    if not result['passed']:
        raise ValueError('Passed actual source/capacity/resume probe required')
    batch = result['selected_measured_batch']
    peak = result['capacity'][str(batch)]['peak_VRAM_bytes']
    policy = configure_resident_memory(peak)
    limit = policy['allocator_allowance_bytes']
    resident_candidates = [int(b) for b, values in result['capacity'].items()
        if values.get('passed') and values['peak_VRAM_bytes'] < limit
        and all(result['timings'][f'{arm}-batch{b}']['stable'] for arm in ('CE','contrast'))]
    if batch not in resident_candidates:
        raise ValueError('Measured fastest batch is not resident-eligible')
    atomic_json(output,dict(status='actual_native_process_allocator_guard_verified', created_at=now(),
        probe_result=dict(path=str(result_path),sha256=sha256(result_path)),selected_measured_batch=batch,
        maximum_resident_eligible_measured_batch=max(resident_candidates),policy=policy,
        nominal_maximum_finite_batch=result['maximum_stable_measured_batch'],
        nominal_capacity_peaks={b:v.get('peak_VRAM_bytes') for b,v in result['capacity'].items()},
        scientific_teacher_tokens=0,optimizer_updates=0,model_forward_backward_updates=0,
        OS_or_driver_settings_changed=False,Base_complete=False,Chat_started=False,quantization_started=False,
        inference='Nominal stress96/128 allocated35.6/47.4GiB despite about24GiB CUDA device capacity. This is consistent with Windows driver shared-memory fallback; it does not prove the specific driver setting. Finite CUDA allocation alone is not resident-VRAM evidence. Original outputs/selection remain unchanged; add stricter allocator guard for science.',
        primary_sources=['https://nvidia.custhelp.com/app/answers/detail/a_id/5490',
            'https://docs.pytorch.org/docs/stable/generated/torch.cuda.memory.set_per_process_memory_fraction.html'],
        limitations='The caching allocator guard is process-local and does not cap all non-PyTorch/driver allocations or prove maximum normal-job VRAM utilization. Leave10percent device allowance for those allocations. Actual source median throughput, worst-shape stress and all-state resume are separate evidence; model quality is still unproven.'))
    print(json.dumps(dict(batch=batch,resident_measured=resident_candidates,policy=policy)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
