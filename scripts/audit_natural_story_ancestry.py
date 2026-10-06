"""Resolve all fixed64 to upstream story records, not just recomposed manifest."""
from collections import defaultdict
from pathlib import Path
import sys
import time
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from story_provenance_lookup import Reader, lookup


def reference(path): return dict(path=str(path), sha256=sha256(path))


def main():
    started = time.monotonic()
    result_path = ROOT/'reports/phase6/natural_story_ancestry_result.json'
    freeze_path = ROOT/'reports/phase6/natural_story_ancestry_freeze.json'
    if result_path.exists() or freeze_path.exists(): raise ValueError('Preserve bounded ancestry audit')
    provenance_path = ROOT/'reports/phase6/natural_story_provenance_result.json'; old = read_json(provenance_path)
    source_path = Path('/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005/shards')
    manifest_path = source_path/'manifest.json'; manifest = read_json(manifest_path)
    if (old['recovered_records'] != 64 or sha256(manifest_path) != 'a33ad89783d7b9c2f65eadc96ceca06d19c1e397b0dc95852b148d408cec7b12'
            or any(r['original_metadata']['source_manifest_sha256'] != sha256(manifest_path) for r in old['rows'])):
        raise ValueError('All64 share this recorded immutable upstream story source')
    index_path = source_path/'train.index.jsonl'; stat = index_path.stat()
    atomic_json(freeze_path, dict(created_at=now(), input=reference(provenance_path), source_manifest=reference(manifest_path),
        source_index_path=str(index_path), recorded_builder_index_sha256=manifest['splits']['train']['index_sha256'],
        source_index_size=stat.st_size, source_index_mtime_ns=stat.st_mtime_ns,
        source_sha256={s:sha256(ROOT/s) for s in ('scripts/story_provenance_lookup.py','scripts/audit_natural_story_ancestry.py')},
        request_offsets=[r['original_metadata']['source_start'] for r in old['rows']],
        CPU_ceiling_seconds=10, index_read_byte_ceiling=8*1024*1024, purpose='All64 upstream provenance/weakness cohorts only; no source acceptance change or filtering',
        new_source_records=0, scientific_teacher_tokens=0, GPU_seconds=0, protected_test_used=False))
    rows=[]; cohorts=defaultdict(lambda:dict(documents=0,weak=0,unresolved_grammar=0))
    with index_path.open('rb') as stream:
        reader=Reader(stream)
        for row in old['rows']:
            if time.monotonic()-started>10: raise TimeoutError('CPU10s ancestry ceiling exceeded')
            source=lookup(reader,row['original_metadata']['source_start'],stat.st_size)
            if (source['body_tokens'] != row['original_metadata']['body_tokens']
                    or source['text_sha256'] != row['text_sha256'] or source['split'] != 'train'):
                raise ValueError('Upstream original whole TRAIN body differs')
            name=source['source']; cohort=cohorts[name];cohort['documents']+=1
            cohort['weak']+=int(row['weak_document']);cohort['unresolved_grammar']+=int(row['unresolved_grammar_issue'])
            rows.append(dict(id=row['id'],text_sha256=row['text_sha256'],upstream_metadata=source,
                weak_document=row['weak_document'],unresolved_grammar_issue=row['unresolved_grammar_issue']))
    after=index_path.stat()
    if (after.st_size,after.st_mtime_ns)!=(stat.st_size,stat.st_mtime_ns):raise ValueError('Upstream index identity changed')
    elapsed=time.monotonic()-started
    if elapsed>10:raise TimeoutError('CPU10s ancestry ceiling exceeded')
    atomic_json(result_path,dict(status='all64_upstream_whole_TRAIN_story_ancestry_and_cohorts_complete',created_at=now(),
        freeze=reference(freeze_path),CPU_elapsed_seconds=elapsed,CPU_ceiling_seconds=10,
        index_bytes_read=reader.bytes_read,original_index_bytes=stat.st_size,index_read_byte_ceiling=8*1024*1024,
        recovered_records=64,rows=rows,cohorts=dict(cohorts),
        original_source_binding=manifest['binding'],
        exact_whole_body_SHA_tokens_and_train_alignment=True,
        source_acceptance_changed=False,source_or_pilot_modified=False,new_source_records=0,
        scientific_teacher_tokens=0,GPU_seconds=0,protected_test_used=False,
        limitations='Observed64 cohort association, not independent source-quality trial or unique cause of model failure. No content filtering, new corpus or global index/corpus audit.'))
    print(json.dumps(dict(CPU_seconds=elapsed,index_bytes_read=reader.bytes_read,cohorts=dict(cohorts)),ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
