"""Archive the actual terminal CC0 source result; quantity failure is not model failure."""
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,now,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from prepare_tatoeba_original_short_source import CONFIG,RUN,PROPOSAL,SOURCES


def main():
    phase=ROOT/'reports/phase6';target=phase/'tatoeba_original_short_source_completion.json'
    bundle=phase/'tatoeba_original_short_source_evidence.tar.gz';manifest=phase/'tatoeba_original_short_source_evidence_manifest.json'
    temporary=bundle.with_suffix('.tmp')
    if any(p.exists() for p in (target,bundle,manifest,temporary)):
        raise ValueError('Preserve existing/interrupted closeout; inspect before retrying')
    c,j,r=read_json(CONFIG),read_json(RUN/'job.json'),read_json(RUN/'result.json')
    if (alive(j) or j['status']!='complete' or r['status']!='source_pinned_prepared_amount_screen_failed'
        or c['proposal']['sha256']!=sha256(PROPOSAL) or r['config_sha256']!=j['config_sha256']
        or r['config_sha256']!=sha256(CONFIG) or r['actual_identity']!={k:j[k] for k in ('pid','boot_id','start_ticks')}
        or r['amount_screen_passed'] or r['eligible_for_training'] or r['content_screen_passed'] is not None
        or r['network_wall_seconds']>c['budgets']['network_wall_seconds'] or r['CPU_seconds']>c['budgets']['CPU_preparation_seconds']
        or r['GPU_seconds'] or r['scientific_teacher_tokens'] or r['optimizer_updates']
        or any(r[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_scored'))):
        raise ValueError('Actual exited bounded amount-failure record required; no training or quality adoption')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen source changed')
    for key in ('proposal','CPU_tests','previous_completion','tokenizer','fixed_suite'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']: raise ValueError('Bound preparation evidence changed')
    pin=read_json(Path(r['source_pin']['path']))
    if sha256(Path(r['source_pin']['path']))!=r['source_pin']['sha256'] or pin['files']!=r['source_pin_files']:
        raise ValueError('Actual one-shot source pin changed')
    for ref in pin['files'].values():
        st=Path(ref['path']).stat()
        if (st.st_size,st.st_mtime_ns)!=(ref['bytes'],ref['mtime_ns']): raise ValueError('Pinned raw source identity changed')
    if not pin['verified_Japanese_CC0_URL_in_actual_official_page'] or not pin['verified_original_only_policy']:
        raise ValueError('Official metadata/provenance checks required')
    total_rows=0;families=set()
    for split,ref in r['source_files'].items():
        path=Path(ref['path'])
        if sha256(path)!=ref['sha256']: raise ValueError('Prepared split changed')
        rows=[json.loads(line) for line in path.read_text().splitlines()]
        if (r['splits'][split]!=dict(documents=len(rows),body_tokens=sum(x['body_tokens'] for x in rows),
            serialized_tokens=sum(x['body_tokens']+2 for x in rows),body_bytes=sum(x['body_bytes'] for x in rows))
            or any(x['split']!=split for x in rows)):
            raise ValueError('Exact split accounting required')
        for row in rows:
            if row['family'] in families: raise ValueError('Exact source family leaked/duplicated across splits')
            families.add(row['family'])
        total_rows+=len(rows)
    if (r['splits']['train']['body_tokens']>=c['readiness_screen']['minimum_distinct_eligible_TRAIN_body_tokens']
        or r['new_distinct_TRAIN_body_tokens']!=r['splits']['train']['body_tokens']
        or r['source_rows']!=total_rows+sum(r['rejections'].values())):
        raise ValueError('Actual quantity failure and complete source accounting required')
    sample=read_json(Path(r['fixed80']['path']))
    if sha256(Path(r['fixed80']['path']))!=r['fixed80']['sha256'] or sample['rows'] or sample['indices']:
        raise ValueError('This actual two-row result cannot masquerade as a full80 sample')
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response: model=json.load(response)
    previous=read_json(Path(c['previous_completion']['path']))
    if not alive(ui) or model['busy'] or model['checkpoint_sha256']!=previous['UI_restored']['model']['checkpoint_sha256']:
        raise ValueError('Original idle UI actual identity/HTTP model must remain available')
    files=[CONFIG,PROPOSAL,Path(__file__),*[(ROOT/name) for name in SOURCES],Path(c['CPU_tests']['path']),
        phase/'tatoeba_original_short_source_preparation.json',phase/'tatoeba_original_short_source_observations.json']
    files.extend(p for p in sorted(RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.py','.ps1','.xml','.log','.lock','.txt'))
    launcher=phase/'tatoeba-original-short-source-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    files=list(dict.fromkeys(files))
    entries=[dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha256(p)) for p in files]
    atomic_json(manifest,dict(created_at=now(),files=entries,tensor_or_full_corpus_included=False,pinned_data_preserved_native=True))
    with tarfile.open(temporary,'w:gz') as archive:
        for p in [*files,manifest]: archive.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(bundle)
    closed=dict(status='official_Japanese_CC0_source_quantity_failure_closed',created_at=now(),
        actual_identity=r['actual_identity'],actual_process_absent_verified=True,config_sha256=sha256(CONFIG),
        result=dict(path=str(RUN/'result.json'),sha256=sha256(RUN/'result.json')),source_pin=r['source_pin'],
        compressed_snapshot=dict(sha256=pin['files']['Japanese_CC0']['sha256'],bytes=pin['files']['Japanese_CC0']['bytes'],
            last_modified=pin['files']['Japanese_CC0']['HTTP_metadata']['Last-Modified']),
        source_rows=r['source_rows'],splits=r['splits'],network_wall_seconds=r['network_wall_seconds'],CPU_seconds=r['CPU_seconds'],
        amount_screen_passed=False,content_screen_performed=False,full80_available=False,
        no_full80_quality_claim=True,eligible_for_training=False,fixed_CC0_condition_closed=True,
        GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0,source_recovery_repeated=False,
        old_corpus_scanned=False,tokenizer_retrained=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_scored=False,quality_criteria_unchanged=True,
        UI_available=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        archive=dict(files=len(entries),bytes=sum(x['bytes'] for x in entries),
            manifest=dict(path=str(manifest),sha256=sha256(manifest)),
            compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle))),
        next_action='Close this fixed CC0 source; no CC-BY/current translation-export substitution, reroll/filter/threshold/epoch rescue or training. A different corpus requires a separately justified source proposal and unchanged Base evidence gates.',
        limitations='One actually fetched mutable CC0 snapshot, not a measurement of the full Japanese Tatoeba corpus, every license subset, or model quality. Two license-declaration example sentences cannot establish general Japanese-prose readiness; full80 review is unavailable.')
    atomic_json(target,closed)
    print(json.dumps(dict(status=closed['status'],source_rows=r['source_rows'],TRAIN_body_tokens=r['splits']['train']['body_tokens'],
        archive_files=len(entries),UI_pid=ui['pid'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
