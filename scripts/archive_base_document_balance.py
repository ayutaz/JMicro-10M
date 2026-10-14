"""Preserve new evidence in authoritative Windows; keep weights/samplers native."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
WIN=Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
RUN=ROOT/'reports/phase6/base-document-balance-comparison-20261014'
MANIFEST=RUN/'local_archive_manifest.json'


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path): return json.loads(path.read_text())


def without_samplers(value):
    if isinstance(value,dict):
        return {k:(dict(native_only=True,canonical_SHA256=hashlib.sha256(
            json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest())
            if k=='sampler' else without_samplers(v)) for k,v in value.items()}
    if isinstance(value,list): return [without_samplers(v) for v in value]
    return value


def main():
    if MANIFEST.exists(): raise ValueError('Preserve one actual archive')
    completion=read(ROOT/'reports/phase6/base_document_balance_comparison_completion.json')
    assert completion['fixed_condition_closed'] and not completion['Base_adopted']
    files=[]
    for path in sorted(RUN.rglob('*')):
        if not path.is_file() or path.suffix not in ('.json','.py','.ps1'):
            continue
        if path.name in ('result.json','train-result.json') and ('training' in read(path) or 'sampler' in read(path)):
            payload=dict(original_native_path=str(path),original_native_sha256=sha(path),
                portable_view=True,samplers_in_native_WSL_only=True,record=without_samplers(read(path)))
            portable=path.with_name(path.stem+'_portable.json')
            if portable.exists(): raise ValueError('Preserve portable evidence')
            portable.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
            files.append(portable)
        else: files.append(path)
    for pattern in ('base_document_balance*.json','base_document_balance*.xml'):
        files.extend((ROOT/'reports/phase6').glob(pattern))
    entries=[]
    for path in sorted(set(files)):
        relative=path.relative_to(ROOT)
        destination=WIN/relative
        destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(path,destination)
        assert sha(destination)==sha(path)
        entries.append(dict(path=relative.as_posix(),bytes=path.stat().st_size,sha256=sha(path),Windows_WSL_bytes_match=True))
    metrics=list((RUN/'document_balance').glob('metrics-*.jsonl'))
    checkpoint=Path(read(RUN/'result.json')['training']['checkpoint'])
    assert sha(checkpoint)==read(RUN/'numeric_completion_audit.json')['full_checkpoint_sha256']
    manifest=dict(created_at=datetime.now(timezone.utc).isoformat(),status='new_rejected_study_evidence_archived_locally',
        files=entries,files_count=len(entries),stored_bytes=sum(r['bytes'] for r in entries),
        native_full_metrics=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in metrics],
        native_final_checkpoint=dict(path=str(checkpoint),bytes=checkpoint.stat().st_size,sha256=sha(checkpoint)),
        all_native_checkpoints_and_full_sampler_preserved=True,
        original_native_job_result_and_train_result_retained=True,
        datasets_copied=False,weights_copied_to_Git=False,samplers_copied_to_Git=False,
        historical_scientific_results_rewritten=False,push_or_publication=False,
        portable_views_are_not_original_result_bytes=True)
    MANIFEST.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    shutil.copyfile(MANIFEST,WIN/MANIFEST.relative_to(ROOT))
    print(json.dumps(dict(files=len(entries),bytes=manifest['stored_bytes'],native_checkpoint=manifest['native_final_checkpoint'],archive_manifest_sha256=sha(MANIFEST))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
