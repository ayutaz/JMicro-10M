"""Preserve terminal readonly diagnostic and allocation proposal evidence."""
import json
from pathlib import Path
import shutil
import sys
import tarfile
import urllib.request

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    phase = ROOT/'reports/phase6'
    run = phase/'base-kv-head-gradient-diagnostic-20261007'
    output = phase/'base_kv_head_gradient_completion.json'
    if output.exists():
        raise ValueError('Preserve completed one-shot record')
    job = json.loads((run/'job.json').read_text())
    result = json.loads((run/'result.json').read_text())
    proposal = json.loads((phase/'base_kv_allocation_proposal.json').read_text())
    config = ROOT/'configs/phase6/base_kv_head_gradient_diagnostic.json'
    if (job['status'] != 'complete' or alive(job)
            or sha256(config) != job['config_sha256']
            or not all(all(e['native_checks'].values()) for e in result['endpoints'].values())
            or result['optimizer_updates'] != 0 or result['scientific_CE_teachers'] != 0):
        raise ValueError('Unchanged native terminal evidence required')
    ui = json.loads((ROOT/'reports/local/webui/server.json').read_text())
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=10) as response:
        model = json.load(response)
    if (not alive(ui) or model['busy'] or model['training_tokens'] != 10000007168
            or model['checkpoint_sha256'] != result['endpoints']['parent']['checkpoint']['sha256']):
        raise ValueError('Original UI process and HTTP identity required')
    record = dict(status='readonly_KV_head_diagnostic_complete_allocation_proposed_not_trained',
        created_at=now(), actual_identity=result['actual_identity'], actual_process_absent_verified=True,
        config=dict(path=str(config), sha256=sha256(config)),
        result_reference=dict(path=str(run/'result.json'), sha256=sha256(run/'result.json')),
        source_aggregates=proposal['head_conflict_marker'],
        severe_interference_at_both_endpoints=result['severe_interference_at_both_endpoints'],
        native_checks={name:e['native_checks'] for name,e in result['endpoints'].items()},
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'], GPU_limit_seconds=180,
        diagnostic_target_positions=result['diagnostic_target_positions'],
        optimizer_updates=0, scientific_CE_teacher_tokens=0, new_model_quality_evaluations=0,
        fixed_diagnostic_closed=True, no_head_gradient_surgery=True,
        interpretation=proposal['causal_limit'],
        allocation_proposal=dict(path=str(phase/'base_kv_allocation_proposal.json'),
            sha256=sha256(phase/'base_kv_allocation_proposal.json')),
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')}, actual_alive=True, model=model),
        quality_criteria_unchanged=True, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False,
        independent_human_review=False, next_action=proposal['next_action'])
    atomic_json(output, record)
    files = [output, config, phase/'base_kv_head_gradient_result.json',
        phase/'base_kv_allocation_proposal.json', phase/'base_post_smoothing_root_synthesis.json',
        phase/'base_kv_head_gradient_tests.xml', phase/'base_embedding_gradient_payload.json',
        Path(__file__), ROOT/'scripts/prepare_base_kv_allocation_proposal.py',
        ROOT/'scripts/base_kv_head_gradient_diagnostic.py', ROOT/'scripts/diagnose_base_kv_head_gradients.py',
        ROOT/'scripts/diagnose_base_kv_head_gradients.ps1', ROOT/'tests/test_base_kv_head_gradient_diagnostic.py']
    files.extend(p for p in sorted(run.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.log','.py','.ps1','.xml','.txt'))
    launcher = phase/'base-kv-head-gradient-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    if any(not p.is_file() for p in files):
        raise ValueError('Missing text evidence; do not claim complete archive')
    folder = phase/'base-kv-head-gradient-evidence-20261007'
    folder.mkdir(exist_ok=False)
    entries = []
    for source in files:
        relative = source.relative_to(ROOT)
        target = folder/relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        entries.append(dict(path=str(relative), bytes=target.stat().st_size, sha256=sha256(target)))
    atomic_json(folder/'manifest.json', dict(created_at=now(), files=entries, tensor_or_corpus_included=False))
    bundle = phase/'base_kv_head_gradient_evidence.tar.gz'
    with tarfile.open(bundle.with_suffix('.tmp'), 'w:gz') as archive:
        archive.add(folder, arcname=folder.name)
    bundle.with_suffix('.tmp').replace(bundle)
    # Archive contains the pre-bundle completion; this final record binds the lossless bundle separately.
    record['archive'] = dict(path=str(folder), files=len(entries), bytes=sum(e['bytes'] for e in entries),
        manifest_sha256=sha256(folder/'manifest.json'), compressed_bundle=dict(path=str(bundle),
            bytes=bundle.stat().st_size, sha256=sha256(bundle)),
        archived_completion_is_pre_bundle_record=True)
    atomic_json(output, record)
    print(json.dumps(dict(status=record['status'], UI_pid=ui['pid'], archive_files=len(entries),
        bundle_bytes=bundle.stat().st_size, GPU_seconds=record['GPU_occupancy_seconds'], Base_complete=False)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
