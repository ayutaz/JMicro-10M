"""Close the actual FFN budget failure, preserving all native checkpoints."""
import json
from pathlib import Path
import sys
import tarfile
from urllib.request import urlopen

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import math
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from jmicro.phase5 import equal_state
from phase6_performance import alive
import probe_base_relu_squared as probe


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def main():
    output = ROOT / 'reports/phase6/base_relu_squared_probe_completion.json'
    if output.exists():
        raise ValueError('Preserve completed fixed FFN probe')
    c = probe.inspect(permit_existing=True)
    job = read_json(probe.RUN / 'job.json')
    r = read_json(probe.RUN / 'result.json')
    if (job['status'] != 'complete' or alive(job) or alive(r['actual_identity'])
            or r['config_sha256'] != sha256(probe.CONFIG) or r['status'] != 'complete'
            or not r['passed'] or r['science_budget_eligible']
            or r['GPU_seconds'] != job['GPU_seconds']
            or not 0 < r['GPU_seconds'] <= c['resource']['probe_GPU_cap_seconds']
            or r['scientific_gold_tokens'] or r['probe_weights_used_for_science']
            or not all(r['initial_checks'].values()) or not r['original_stream_parity']):
        raise ValueError('Actual exited passed-numerics/failed-budget one-shot probe required')
    timings = {}
    total_caps = 0
    keys = ('source_teachers', 'source_EOS', 'CE_input_tokens', 'physical_input_tokens',
            'original_body_bytes', 'token_digest', 'draw_trace', 'lr')
    for a, b in zip(r['timing']['SwiGLU']['timed_updates'], r['timing']['ReLU_squared']['timed_updates'], strict=True):
        if not all(equal_state(a[k], b[k]) for k in keys):
            raise ValueError('All32 actual timed batches must share identical original stream')
    for arm in probe.ARMS:
        if not all(r['resume'][arm]['checks'].values()):
            raise ValueError('All actual full-state/history CUDA checks required')
        cap = r['capacity'][arm]
        if (not cap['passed'] or not cap['weights_unchanged_by_stress'] or cap['optimizer_updates']
                or cap['context'] != 1024 or cap['teachers'] != 40960
                or cap['peak_VRAM_bytes'] >= r['memory_policy']['allocator_allowance_bytes']):
            raise ValueError('Actual resident80x1024/512 finite unchanged-weight stress required')
        rows = r['timing'][arm]['timed_updates']
        if len(rows) != 32:
            raise ValueError('All32 measured updates, no favorable timing subset')
        seconds = sum(x['seconds'] for x in rows)
        teachers = sum(x['CE_targets_this_update'] for x in rows)
        wait = sum(x['data_wait_seconds'] for x in rows)
        estimated = math.ceil(300000000 * seconds / teachers * 1.3 + 900)
        if (seconds != r['timing'][arm]['total_seconds'] or teachers != r['timing'][arm]['total_original_gold']
                or estimated != r['timing'][arm]['science_cap_seconds']):
            raise ValueError('Original frozen wall-time budget math differs')
        total_caps += estimated
        timings[arm] = dict(total_step_seconds=seconds, original_gold=teachers,
            sampler_wait_seconds=wait, remaining_step_seconds=seconds - wait,
            step_timing_excludes_no_wait_for_budget=True, forecast_cap_seconds=estimated,
            original_gold_per_second=teachers / seconds)
    forecast = total_caps + r['GPU_seconds']
    if forecast != r['forecast_all_new_GPU_seconds'] or forecast <= c['resource']['total_GPU_cap_seconds']:
        raise ValueError('Actual unchanged14400s forecast must exceed cap')
    if r['verification_updates'] != 86 or r['verification_original_gold'] != sum(
            x['CE_targets_this_update'] for h in r['histories'].values() for x in h):
        raise ValueError('Actual86 verification updates/source teachers required')
    server = read_json(ROOT / 'reports/local/webui/server.json')
    with urlopen('http://127.0.0.1:7860/api/model', timeout=3) as response:
        model = json.load(response)
    if (server['status'] != 'running' or not alive(server)
            or model['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or model['busy'] or model['training_tokens'] != 10000007168):
        raise ValueError('Original10B UI exact process and parent API must be restored')
    # Only new text evidence; never move/delete model/data or earlier records.
    paths = [ROOT / s for s in probe.SOURCES]
    paths += [probe.CONFIG, Path(c['proposal']['path']), Path(c['CPU_tests']['path']),
              Path(c['initial_failed_CPU_tests']['path']), Path(__file__)]
    paths += [p for p in probe.RUN.rglob('*') if p.is_file() and p.suffix in ('.json', '.py', '.ps1', '.xml', '.lock')]
    launcher = ROOT / 'reports/phase6/base-relu-squared-probe-launcher-20261007'
    paths += [launcher / n for n in ('launcher.json', 'stdout.log', 'stderr.log', 'result.json')]
    if read_json(launcher / 'result.json')['status'] != 'complete':
        raise ValueError('Actual durable launcher has not finished')
    paths = sorted(set(paths))
    manifest = ROOT / 'reports/phase6/base_relu_squared_probe_evidence_manifest.json'
    archive = ROOT / 'reports/phase6/base_relu_squared_probe_evidence.tar.gz'
    if archive.exists() or manifest.exists():
        raise ValueError('Preserve prior evidence archive')
    files = [dict(path=p.relative_to(ROOT).as_posix(), sha256=sha256(p), bytes=p.stat().st_size) for p in paths]
    atomic_json(manifest, dict(created_at=now(), files=files, tensors_and_corpus_excluded=True))
    temporary = archive.with_suffix('.tmp')
    with tarfile.open(temporary, 'w:gz') as tar:
        for p in (*paths, manifest):
            tar.add(p, arcname=p.relative_to(ROOT).as_posix(), recursive=False)
    temporary.replace(archive)
    atomic_json(output, dict(status='actual_FFN_probe_complete_science_closed_budget_exceeded', created_at=now(),
        config=ref(probe.CONFIG), result=ref(probe.RUN / 'result.json'), proposal=c['proposal'],
        CPU_tests=c['CPU_tests'], initial_failed_CPU_tests=c['initial_failed_CPU_tests'],
        initial_test_failure_fixed_without_numeric_or_quality_threshold_change=True,
        actual_identity=r['actual_identity'], actual_process_absent_verified=True,
        initial_GPU_checks=r['initial_checks'], all_resume_checks={a: r['resume'][a]['checks'] for a in probe.ARMS},
        capacity=r['capacity'], parameter_counts=c['parameter_counts'], same_all32_timed_source_batches=True,
        GPU_seconds=r['GPU_seconds'], verification_updates=r['verification_updates'],
        verification_original_gold=r['verification_original_gold'], stress_backward_positions=81920,
        stress_optimizer_updates=0, scientific_gold_tokens=0, new_unique_dataset_tokens=0,
        new_model_quality_evaluations=0, forecast_all_new_GPU_seconds=forecast,
        fixed_all_new_GPU_cap_seconds=c['resource']['total_GPU_cap_seconds'], science_budget_eligible=False,
        fixed300M_per_arm_FFN_protocol_closed=True, no_cap_increase_or_teacher_batch_rescue=True,
        timing_breakdown=timings,
        timing_limitation='SwiGLU always measured first and ReLU_squared second on identical source batches; no randomized/interleaved order or cold-cache control. Sampler waiting differs strongly. The12percent wall-throughput difference does not prove architectural acceleration. Remaining-step time includes collation/transfers/optimizer/CPU and is not a pure GPU profiler measurement.',
        original_UI=dict(identity={k: server[k] for k in ('pid', 'boot_id', 'start_ticks')}, API=model,
                         actual_alive_verified=True),
        archive=dict(**ref(archive), bytes=archive.stat().st_size, text_files=len(files),
                     uncompressed_text_bytes=sum(x['bytes'] for x in files), manifest=ref(manifest)),
        native_checkpoints_preserved=True, old_MHA_budget_failure_and_science0_preserved=True,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_used=False, quality_criteria_unchanged=True,
        next_action='Use saved paired timing rows to define a bounded independent data-wait/benchmark-validity investigation before selecting another Base learning comparison. Do not reopen the fixed failed FFN/MHA caps or claim quality from verification.'))
    print('Actual FFN numerics/resume pass; fixed budget fails; science0; original UI verified; text archive saved')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
