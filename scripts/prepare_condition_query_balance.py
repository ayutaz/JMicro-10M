"""Bounded preparation; no CUDA, tokenizer retraining or original corpus scan."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time
from datetime import datetime, timezone
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
from jmicro.tokenizer import Tokenizer
from prepare_condition_positive_teachers import outcome_token_mask
from condition_query_balance import DATA, KIND, SEED, QueryBalancedTrainView, build_rows, pilot_rows

RUN = ROOT / 'reports/phase6/condition-query-balance-preparation-20261006'
PROPOSAL = ROOT / 'reports/phase6/condition_query_balance_proposal.json'
SOURCES = ('scripts/condition_query_balance.py', 'scripts/prepare_condition_query_balance.py',
           'scripts/review_condition_query_balance.py', 'tests/test_condition_query_balance.py',
           'scripts/prepare_condition_positive_teachers.py')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    tmp.replace(path)


def main():
    started = time.perf_counter()
    if DATA.exists() or RUN.exists():
        raise ValueError('Preserve fixed preparation; inspect completed or partial evidence before restart')
    p = read(PROPOSAL)
    for ref in p['references'].values():
        if sha(ref['path']) != ref['sha256']:
            raise ValueError('Predefined evidence changed')
    if p['seed'] != SEED or p['changed_documents'] != 172 or p['CPU_limit_seconds'] != 120:
        raise ValueError('Fixed query intervention scope differs')
    source = Path(p['references']['source_manifest']['path']).parent
    manifest = read(source / 'manifest.json')
    if sha(source / 'train-source.json') != manifest['train_source_sha256']:
        raise ValueError('Accepted original selected train source differs')
    acceptance = read(source / 'content-review.json')
    if not acceptance['training_pool_accepted'] or not acceptance['all64_read']:
        raise ValueError('Original relation source not accepted')
    original = read(source / 'train-source.json')
    rows, selected = build_rows(original)
    tok = Tokenizer(ROOT / p['tokenizer']['path'])
    if sha(ROOT / p['tokenizer']['path']) != p['tokenizer']['sha256']:
        raise ValueError('Pinned tokenizer differs')
    DATA.mkdir(parents=True)
    RUN.mkdir(parents=True)
    job = dict(status='CPU_preparing', pid=__import__('os').getpid(),
        boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
        start_ticks=Path('/proc/self/stat').read_text().split()[21],
        started_at=datetime.now(timezone.utc).isoformat(), GPU_seconds=0, scientific_teacher_tokens=0,
        proposal_sha256=sha(PROPOSAL))
    write(RUN / 'job.json', job)
    try:
        tokens, focus, offsets, lengths, metadata = [], [], [], [], []
        body_bytes = body_tokens = 0
        for r in rows:
            if time.perf_counter() - started > 120:
                raise TimeoutError('CPU120s preparation budget exhausted')
            ids = tok.encode(r['text'])
            if tok.decode_bytes(ids) != r['text'].encode() or len(ids) + 1 > 1024:
                raise ValueError('Complete native source body/context required')
            offsets.append(len(tokens)); lengths.append(len(ids) + 2)
            tokens.extend([2, *ids, 3])
            focus.extend(outcome_token_mask(r['text'], ids, tok, [r]).tolist())
            body_tokens += len(ids); body_bytes += len(r['text'].encode())
            metadata.append(dict(id=r['id'], category=r['category'], family=r['family'],
                template_id=r['template_id'], requested_relation=r.get('requested_relation', 'longer') if r['category'] == 'comparison' else None,
                text_sha256=r['text_sha256'], body_tokens=len(ids), body_bytes=len(r['text'].encode())))
        probes = read(source / 'transfer-probes.json')
        train_hashes = {r['text_sha256'] for r in rows}
        if any(hashlib.sha256((c['prefix'] + c['outcome']).encode()).hexdigest() in train_hashes for c in probes['cases']):
            raise ValueError('Heldout probe body overlaps training')
        pilot = dict(rows=pilot_rows(rows), sampling='First sorted train family per28 relation/query surfaces, then first four remaining train families; both contexts; no score selection or reroll',
                     train_relation_forms=24, train_surface_query_combinations=28, source='local_programmatic_Japanese', protected_test_used=False)
        value = dict(rows=rows, original_families=original['families'], shorter_query_families=selected,
                     family_policy='Original facts/context branch IDs retained. Changed answer label is1-original_context_branch, because the requested property is shorter.')
        write(DATA / 'train-source.json', value); write(DATA / 'content-pilot.json', pilot)
        for filename in ('transfer-probes.json', 'retention-probes.json'):
            (DATA / filename).write_bytes((source / filename).read_bytes())
        arrays = dict(tokens=np.asarray(tokens, dtype='<u2'), focus=np.asarray(focus, dtype=np.uint8),
                      offsets=np.asarray(offsets, dtype='<i8'), lengths=np.asarray(lengths, dtype='<i4'))
        np.savez(DATA / 'train.npz', **arrays)
        m = dict(kind=KIND, source='local_programmatic_Japanese', seed=SEED, documents=2048,
            train_families=1024, comparison_documents=342, shorter_query_documents=172, longer_query_documents=170,
            changed_documents=172, changed_ids=[r['id'] for r in rows if r.get('requested_relation') == 'shorter'],
            train_relation_forms=24, train_surface_query_combinations=28, category_counts=dict(Counter(r['category'] for r in rows)),
            metadata=metadata, generated_body_tokens=body_tokens, generated_body_bytes=body_bytes,
            serialized_tokens=len(tokens), full_CE_targets=body_tokens + 2048, EOS_targets=2048,
            outcome_focus_body_targets=int(arrays['focus'].sum()), arrays_sha256=sha(DATA / 'train.npz'),
            tokenizer_sha256=p['tokenizer']['sha256'], original_manifest_sha256=sha(source / 'manifest.json'),
            original_train_source_sha256=manifest['train_source_sha256'], train_source_sha256=sha(DATA / 'train-source.json'),
            pilot_sha256=sha(DATA / 'content-pilot.json'), probe_sha256=sha(DATA / 'transfer-probes.json'),
            retention_probe_sha256=sha(DATA / 'retention-probes.json'), proposal_sha256=sha(PROPOSAL),
            source_sha256={s: sha(ROOT / s) for s in SOURCES}, newly_prepared_original_corpus_tokens=0,
            scientific_teacher_tokens=0, GPU_seconds=0, training_pool_accepted=False, protected_test_used=False,
            loss_policy='All body+EOS ordinary CE, outcome weight1; focus only annotates outcomes.',
            limitations='A selected train-source query intervention, not new public corpus volume or a pure position-only manipulation. Changes query words, target entity and token lengths together. Heldout probes remain byte-identical; do not teach their forms or prompts. Same authored source semantics; broader natural Base quality must pass unchanged gates.')
        write(DATA / 'manifest.json', m)
        QueryBalancedTrainView(DATA, sha(DATA / 'manifest.json'), require_accepted=False)
        for filename in ('train-source.json', 'content-pilot.json', 'manifest.json'):
            (RUN / filename).write_bytes((DATA / filename).read_bytes())
        job.update(status='complete_pending_fixed64_content', completed_at=datetime.now(timezone.utc).isoformat(),
                   CPU_seconds=time.perf_counter() - started, data_path=str(DATA), manifest_sha256=sha(DATA / 'manifest.json'))
        write(RUN / 'job.json', job)
        write(ROOT / 'reports/phase6/condition_query_balance_preparation.json', dict(job=job, Base_adopted=False,
            Base_complete=False, Chat_started=False, quantization_started=False, scientific_teacher_tokens=0,
            next_action='Read all fixed64 and preserve raw-bound content notes; only accepted source may enter measured CUDA resume/timing and frozen same100M comparison.'))
        print(dict(status=job['status'], CPU_seconds=job['CPU_seconds'], body_tokens=body_tokens,
                   changed_documents=172, longer_query_documents=170, shorter_query_documents=172))
    except BaseException as error:
        job.update(status='failed_preserve_fixed_partial', error=repr(error), CPU_seconds=time.perf_counter() - started)
        write(RUN / 'job.json', job)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
