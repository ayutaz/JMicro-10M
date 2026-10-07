"""Close the exited read-only geometry screen, preserving limits and original UI."""
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from base_token_geometry import severe_marker, SOURCES
from probe_base_token_geometry import CONFIG, RUN, PROPOSAL, COMPANION, INPUTS, IMPLEMENTATION, checked


def main():
    phase = ROOT/'reports/phase6'
    output = phase/'base_token_geometry_completion.json'
    bundle = phase/'base_token_geometry_evidence.tar.gz'
    manifest = phase/'base_token_geometry_evidence_manifest.json'
    temporary = bundle.with_suffix('.tmp')
    if any(p.exists() for p in (output,bundle,manifest,temporary)):
        raise ValueError('Preserve existing closure/interrupted archive; no overwrite')
    c,job,result = read_json(CONFIG),read_json(RUN/'job.json'),read_json(RUN/'result.json')
    if (alive(job) or job['status'] != 'complete' or result['status'] != 'complete'
            or result['actual_identity'] != {k:job[k] for k in ('pid','boot_id','start_ticks')}
            or job['config_sha256'] != result['config_sha256'] or result['config_sha256'] != sha256(CONFIG)
            or not 0 < job['GPU_seconds'] == result['GPU_seconds'] <= 120
            or result['optimizer_updates'] != 0 or result['new_scientific_teacher_tokens'] != 0
            or any(not all(v.values()) for v in result['read_only_checks'].values())):
        raise ValueError('Actual exited bounded read-only CUDA proof required')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name) != digest:
            raise ValueError('Frozen scientific geometry source changed')
    for name in ('proposal','companion','payload'):
        checked(c[name])
    if sha256(Path(c['tests']['path'])) != c['tests']['sha256']:
        raise ValueError('CPU proof changed')
    payload = checked(c['payload'])
    if result['decision'] != severe_marker(result['models']):
        raise ValueError('Fixed severe-marker decision changed')
    for name in c['models']:
        observed = result['observations'][name]
        if len(observed) != 12 or any((a['source'],a['body_sha256']) != (b['source'],b['full_original_body_sha256'])
                                     for a,b in zip(observed,payload['rows'],strict=True)):
            raise ValueError('Same12 original TRAIN unit binding differs')
        if set(result['models'][name]) != set(SOURCES) or any(v['documents'] != 4 for v in result['models'][name].values()):
            raise ValueError('All same four units per three sources required')
    ui = read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        model = json.load(response)
    if not alive(ui) or model['busy'] or model['checkpoint_sha256'] != c['models']['parent']['sha256']:
        raise ValueError('Original idle UI process/API must be restored')
    launcher = phase/'base-token-geometry-probe-launcher-20261007'
    launched = read_json(launcher/'result.json')
    if launched.get('status') != 'complete' or launched.get('exit_code') != 0:
        raise ValueError('Actual completed durable launcher required')
    files = [Path(__file__),CONFIG,PROPOSAL,COMPANION,INPUTS,Path(c['tests']['path']),
        RUN/'job.json',RUN/'result.json', *[ROOT/name for name in IMPLEMENTATION],
        *[launcher/name for name in ('launcher.json','result.json','stdout.log','stderr.log')]]
    files = list(dict.fromkeys(files))
    entries = [dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha256(p)) for p in files]
    atomic_json(manifest,dict(created_at=now(),files=entries,tensor_or_corpus_included=False,original_native_checkpoints_preserved=True))
    with tarfile.open(temporary,'w:gz') as archive:
        for path in [*files,manifest]:
            archive.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(bundle)
    passed = result['decision']['passed']
    completion = dict(created_at=now(),status='completed_readonly_token_geometry_screen',
        actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        config= dict(path=str(CONFIG),sha256=sha256(CONFIG)),result=dict(path=str(RUN/'result.json'),sha256=sha256(RUN/'result.json')),
        prospective_proposal=dict(path=str(PROPOSAL),sha256=sha256(PROPOSAL)),
        GPU_seconds=result['GPU_seconds'],GPU_cap_seconds=120,CPU_preparation_seconds=c['CPU_preparation_seconds'],
        actual_CUDA_readonly_checks=result['read_only_checks'],models=result['models'],fixed_decision=result['decision'],
        fixed_severe_marker_condition_closed=not passed,diagnostic_units=12,models_measured=3,
        new_scientific_teacher_tokens=0,optimizer_updates=0,new_unique_corpus=0,extra_parameters=0,
        SimCTG_training_implemented=False,SimCTG_training_run=False,contrastive_search_used=False,
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        archive=dict(files=len(entries),bytes=sum(r['bytes'] for r in entries),
            manifest=dict(path=str(manifest),sha256=sha256(manifest)),
            compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle))),
        interpretation='No severe marker in these fixed short TRAIN units. Not proof of globally isotropic states, absence of every geometric effect, causal sufficiency or useful Base quality.' if not passed else 'Severe local marker observed; not a causal or Base-quality proof. Implement and bound one concrete matched learning test before running it.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Negative: close this severe-marker-led branch; no thresholds/subsets/layers/normalization/parents/source/decoder/cap rescue or automatic learning. Select a different evidence-grounded Base comparison before GPU. Qualified Base only gets final independent learnedseed/fullDEV/protectedTEST/adoption; notify and stop at Base. No Chat or quantization.' if not passed else 'Prepare one concretely implemented/frozen matched100M token-separation comparison; same original native greedy/quality/retention gates; actual CUDA resume/memory/speed budget first.')
    atomic_json(output,completion)
    print(json.dumps(dict(status=completion['status'],severe_marker=passed,GPU_seconds=result['GPU_seconds'],UI_pid=ui['pid'],archive_files=len(entries))))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    import argparse
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
