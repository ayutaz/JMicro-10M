"""Close the actual exited readonly precision assay and archive its evidence."""
import json
import math
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, now, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from base_gradient_precision import screen
from diagnose_base_gradient_precision import CONFIG,RUN,PAYLOAD,SOURCES


def main():
    phase=ROOT/'reports/phase6'; target=phase/'base_gradient_precision_completion.json'
    bundle=phase/'base_gradient_precision_evidence.tar.gz'; manifest=phase/'base_gradient_precision_evidence_manifest.json'
    temporary=bundle.with_suffix('.tmp')
    if any(p.exists() for p in (target,bundle,manifest,temporary)):
        raise ValueError('Preserve completed/interrupted closeout; inspect before retrying')
    c,j,r=read_json(CONFIG),read_json(RUN/'job.json'),read_json(RUN/'result.json')
    if (alive(j) or j['status']!='complete' or r['status']!='fixed_all_parameter_training_precision_assay_complete'
        or j['config_sha256']!=r['config_sha256'] or r['config_sha256']!=sha256(CONFIG)
        or r['actual_identity']!={k:j[k] for k in ('pid','boot_id','start_ticks')}
        or not 0<j['GPU_occupancy_seconds']==r['GPU_occupancy_seconds']<=c['GPU_limit_seconds']
        or r['optimizer_updates']!=0 or r['scientific_teacher_tokens']!=0 or not r['fixed_diagnostic_closed']
        or r['peak_VRAM_bytes']>=r['memory_policy']['allocator_allowance_bytes']
        or any(r[k] is not False for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))
        or not r['quality_criteria_unchanged'] or not r['old_numeric7_preserved']):
        raise ValueError('Actual exited, unchanged, bounded readonly native assay required')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen assay source changed')
    for ref in [c['payload'],c['CPU_tests'],*c['references'].values()]:
        if sha256(Path(ref['path']))!=ref['sha256']: raise ValueError('Bound evidence changed')
    rows=read_json(PAYLOAD)['rows']; declared={x['id']:x for x in rows}
    if len(rows)!=25 or len(declared)!=25 or set(r['endpoints'])!={'parent','CE100M'}: raise ValueError('All fixed rows/endpoints required')
    expected_positions=0
    for name,e in r['endpoints'].items():
        if e['checkpoint']!=c['checkpoints'][name] or not all(e['checks'].values()): raise ValueError('Endpoint binding/state checks failed')
        actual=[]
        for b in e['batches']:
            actual.extend(b['row_ids'])
            batch=[declared[i] for i in b['row_ids']]
            teachers=sum(sum(n!=-100 for n in x['target_ids']) for x in batch)
            if any(x['source']!=b['source'] for x in batch): raise ValueError('Source labels changed')
            if set(b['measurements'])!=set(c['paths']): raise ValueError('Every precision path required')
            for m in b['measurements'].values():
                if (m['teachers']!=teachers or not 0<=m['loss']<float('inf')
                    or m['valid_inputs']!=sum(len(x['input_ids']) for x in batch)
                    or m['physical_inputs']!=len(batch)*max(len(x['input_ids']) for x in batch)):
                    raise ValueError('Identical original teacher/input accounting required')
                expected_positions+=teachers
            for v in b['comparisons'].values():
                if v['gradient']['elements']!=c['native_parameters']: raise ValueError('All distinct native parameters required')
        if sorted(actual)!=sorted(declared): raise ValueError('Missing/repeated original TRAIN window')
        for genre,s in e['sources'].items():
            selected=[x for x in rows if x['source']==genre]
            if s['rows']!=len(selected) or s['teachers']!=sum(sum(n!=-100 for n in x['target_ids']) for x in selected):
                raise ValueError('Complete source aggregate required')
    recomputed=screen(r['endpoints'])
    if recomputed!=r['research_screen'] or expected_positions!=r['diagnostic_teacher_positions_all_paths']:
        raise ValueError('Fixed screen or diagnostic accounting changed')
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response: model=json.load(response)
    if not alive(ui) or model['busy'] or model['checkpoint_sha256']!=c['checkpoints']['parent']['sha256']:
        raise ValueError('Original idle UI actual identity and HTTP parent SHA required')
    files=[CONFIG,PAYLOAD,Path(__file__),*[(ROOT/name) for name in SOURCES],
        Path(c['CPU_tests']['path']),*[(Path(ref['path'])) for ref in c['references'].values()],
        phase/'base_gradient_precision_initial_preparation.py',phase/'base_gradient_precision_initial_preparation_payload.json',
        phase/'base_gradient_precision_initial_preparation_failure.json']
    files.extend(p for p in sorted(RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.py','.ps1','.xml','.lock','.log','.txt'))
    launcher=phase/'base-gradient-precision-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    files=list(dict.fromkeys(files))
    entries=[dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha256(p)) for p in files]
    atomic_json(manifest,dict(created_at=now(),files=entries,tensor_or_corpus_included=False,full_checkpoints_preserved_native=True))
    with tarfile.open(temporary,'w:gz') as archive:
        for p in [*files,manifest]: archive.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(bundle)
    positive=any(s['supported'] for s in recomputed.values())
    completion=dict(status='readonly_gradient_precision_assay_closed',created_at=now(),actual_identity=r['actual_identity'],
        actual_process_absent_verified=True,result=dict(path=str(RUN/'result.json'),sha256=sha256(RUN/'result.json')),
        config_sha256=sha256(CONFIG),GPU_occupancy_seconds=r['GPU_occupancy_seconds'],GPU_cap_seconds=c['GPU_limit_seconds'],
        peak_VRAM_bytes=r['peak_VRAM_bytes'],research_screen=recomputed,precision_training_comparison_supported=positive,
        original_TRAIN_rows_per_endpoint=25,new_source_draws=0,diagnostic_teacher_positions_all_paths=expected_positions,
        optimizer_updates=0,scientific_teacher_tokens=0,new_unique_data_tokens=0,
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        archive=dict(files=len(entries),bytes=sum(e['bytes'] for e in entries),
            manifest=dict(path=str(manifest),sha256=sha256(manifest)),
            compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle))),
        fixed_diagnostic_closed=True,old_numeric7_preserved=True,quality_criteria_unchanged=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        next_action='Positive fixed marker: define an independently bounded precision training comparison before learning. Otherwise no precision training/sample/threshold/cap rescue; select a distinct mechanism from existing evidence.',
        limitations=r['limitations'])
    atomic_json(target,completion)
    print(json.dumps(dict(status=completion['status'],GPU_seconds=r['GPU_occupancy_seconds'],
        screen=recomputed,archive_files=len(entries),UI_pid=ui['pid'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
