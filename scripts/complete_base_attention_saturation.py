"""Archive terminal attention assay and record its negative fixed screen."""
import json
from pathlib import Path
import shutil
import sys
import tarfile
import urllib.request

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    phase=ROOT/'reports/phase6';run=phase/'base-attention-saturation-diagnostic-20261007'
    target=phase/'base_attention_saturation_completion.json'
    if target.exists():raise ValueError('Preserve terminal one-shot assay')
    result=json.loads((run/'result.json').read_text());job=json.loads((run/'job.json').read_text())
    config=ROOT/'configs/phase6/base_attention_saturation_diagnostic.json'
    if (job['status']!='complete' or alive(job) or sha256(config)!=result['config_sha256']
            or not all(all(e['native_checks'].values()) for e in result['endpoints'].values())
            or result['optimizer_updates'] or result['scientific_teacher_tokens']):
        raise ValueError('Actual terminal native readonly protocol required')
    ui=json.loads((ROOT/'reports/local/webui/server.json').read_text())
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:model=json.load(response)
    if not alive(ui) or model['busy'] or model['checkpoint_sha256']!=result['endpoints']['parent']['checkpoint']['sha256']:
        raise ValueError('Original UI actual process and HTTP identity required')
    summaries={}
    for name,endpoint in result['endpoints'].items():
        summaries[name]={}
        for genre,source in endpoint['sources'].items():
            heads=[h for layer in source['layers'] for h in layer['heads']]
            n=source['eligible_head_queries']
            summaries[name][genre]=dict(marked_layers=source['marked_layers'],total_layers=13,
                saturated_fraction=source['saturated_head_queries']/n,
                eligible_head_queries=n,saturated_head_queries=source['saturated_head_queries'],
                saturated_to_BOS=sum(h['saturated_to_BOS'] for h in heads),
                saturated_to_recent_non_BOS=sum(h['saturated_to_recent_non_BOS'] for h in heads),
                saturated_to_other=sum(h['saturated_to_other'] for h in heads),
                normalized_entropy_mean=sum(h['normalized_entropy_sum'] for h in heads)/n,
                maximum_probability_mean=sum(h['maximum_probability_sum'] for h in heads)/n)
    negative=not result['broad_saturation_at_both_learned_endpoints']
    record=dict(status='readonly_attention_assay_complete_broad_screen_not_passed' if negative else 'readonly_attention_assay_complete_broad_marker_observed',
        created_at=now(),actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        config=dict(path=str(config),sha256=sha256(config)),
        result_reference=dict(path=str(run/'result.json'),sha256=sha256(run/'result.json')),
        source_summaries=summaries,all_native_checks={n:e['native_checks'] for n,e in result['endpoints'].items()},
        broad_saturation_at_both_learned_endpoints=not negative,fixed_diagnostic_closed=True,
        no_QK_restoration_softcap_sigma_learning_from_negative_screen=negative,
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],GPU_limit_seconds=90,
        diagnostic_teacher_positions=result['diagnostic_teacher_positions'],scientific_teacher_tokens=0,
        optimizer_updates=0,new_model_quality_evaluations=0,new_parameters_saved=0,
        interpretation='All fixed learned source aggregates show zero marked layers; about2percent eligible head-queries are sharply concentrated, mostly on original BOS. This does not prove attention always healthy or context used appropriately; no temporal entropy-collapse/causal generalization evidence.',
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_used=False,
        next_action='Prepare one next-two-token auxiliary CE comparison with original100M/source/native inference unchanged, explicit auxiliary positions/parameters/GPU budget. Review primary small-model induction and negative scaling evidence; no automatic launch or adoption.')
    atomic_json(target,record)
    files=[target,config,phase/'base_attention_saturation_result.json',phase/'base_attention_saturation_tests.xml',
        phase/'base_embedding_gradient_payload.json',Path(__file__)]
    files.extend(p for p in sorted(run.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.log','.xml','.lock','.txt'))
    launcher=phase/'base-attention-saturation-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    if any(not p.is_file() for p in files):raise ValueError('Missing text evidence')
    folder=phase/'base-attention-saturation-evidence-20261007';folder.mkdir(exist_ok=False);entries=[]
    for source in files:
        relative=source.relative_to(ROOT);dest=folder/relative;dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,dest);entries.append(dict(path=str(relative),bytes=dest.stat().st_size,sha256=sha256(dest)))
    atomic_json(folder/'manifest.json',dict(created_at=now(),files=entries,tensor_or_corpus_included=False))
    bundle=phase/'base_attention_saturation_evidence.tar.gz'
    with tarfile.open(bundle.with_suffix('.tmp'),'w:gz') as archive:archive.add(folder,arcname=folder.name)
    bundle.with_suffix('.tmp').replace(bundle)
    record['archive']=dict(path=str(folder),files=len(entries),bytes=sum(e['bytes'] for e in entries),
        manifest_sha256=sha256(folder/'manifest.json'),archived_completion_is_pre_bundle_record=True,
        compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle)))
    atomic_json(target,record)
    print(json.dumps(dict(status=record['status'],UI_pid=ui['pid'],GPU_seconds=record['GPU_occupancy_seconds'],archive_files=len(entries))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
