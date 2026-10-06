"""Bounded source replacement; new probes declared before learning, no GPU."""
from collections import Counter
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive, identity
from prepare_condition_positive_teachers import outcome_token_mask
from prepare_condition_transfer_curriculum import encode_probes, check_dev_leakage
from condition_relation_language import DATA, CONTROL_DATA, KIND, SEED, generate, validate_replacement, RelationLanguageTrainView

RUN = ROOT/'reports/phase6/condition-relation-language-20261006'
PROPOSAL = ROOT/'reports/phase6/condition_relation_language_proposal.json'
SOURCES = ('scripts/condition_relation_language.py', 'scripts/prepare_condition_relation_language.py',
           'scripts/prepare_condition_relation_language.ps1', 'scripts/review_condition_relation_language.py')


def references():
    p = read_json(PROPOSAL)
    for ref in (p['evidence'], p['fixeddev_pairs'], p['controls']['reuse_original_eval']):
        if sha256(Path(ref['path'])) != ref['sha256']:
            raise ValueError('Original completed100M evidence differs')
    control_run = ROOT/'reports/phase6/condition-transfer-comparison-20261006'
    job = read_json(control_run/'job.json'); result = read_json(control_run/'compare-result.json')
    if (job['status'] != 'complete' or alive(job) or result['checkpoints']['curriculum'] != p['controls']['reuse_completed_curriculum100M']
            or p['preparation']['CPU_limit_seconds'] != 240 or p['preparation']['documents'] != 2048
            or p['GPU_limit_seconds_including_probe'] != 900 or p['Base_adopted'] or p['Chat_started'] or p['quantization_started'] or p['protected_test_used']):
        raise ValueError('Actual terminal100M and unchanged Base-only proposal required')
    original_manifest = read_json(CONTROL_DATA/'manifest.json')
    original_review = read_json(CONTROL_DATA/'content-review.json')
    if (not original_review['training_pool_accepted'] or original_review['manifest_sha256'] != sha256(CONTROL_DATA/'manifest.json')
            or original_manifest['train_source_sha256'] != sha256(CONTROL_DATA/'train-source.json')
            or original_review['notes_sha256'] != sha256(CONTROL_DATA/'content-notes.json')):
        raise ValueError('Accepted immutable selected source required')
    base = read_json(ROOT/'configs/phase6/textbook_quantity_comparison.json')
    if sha256(ROOT/base['tokenizer']) != base['tokenizer_sha256']:
        raise ValueError('Pinned Tokenizer changed')
    return p, base


def main():
    started = time.monotonic(); p, base = references()
    if DATA.exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve existing fixed/partial bridge preparation; no reroll')
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='preparing', **identity(), started_at=now(), CPU_limit_seconds=240,
        proposal_sha256=sha256(PROPOSAL), scientific_teacher_tokens=0, actual_GPU_seconds=0, protected_test_used=False,
        restart_command='Inspect existing fixed/partial preparation; no automatic reroll. uv run --frozen --extra hub --extra data --extra ml --extra export scripts/prepare_condition_relation_language.py')
    atomic_json(RUN/'job.json', job)
    try:
        control = read_json(CONTROL_DATA/'train-source.json')
        groups, rows = generate(control); checks = validate_replacement(control, groups, rows)
        leakage = check_dev_leakage(rows, groups, ROOT/'reports/phase6/condition-source-learning-100m-20261006')
        tok = Tokenizer(ROOT/base['tokenizer'])
        tokens=[]; masks=[]; offsets=[]; lengths=[]; metadata=[]; body_tokens=body_bytes=0
        for row in rows:
            if time.monotonic()-started > 240: raise TimeoutError('CPU240s preparation budget exhausted')
            ids = tok.encode(row['text'])
            if tok.decode_bytes(ids) != row['text'].encode() or len(ids)+1 > 1024:
                raise ValueError('Complete native body bytes/context required')
            mask = outcome_token_mask(row['text'], ids, tok, [row])
            offsets.append(len(tokens)); lengths.append(len(ids)+2); tokens.extend([2, *ids, 3]); masks.extend(mask.tolist())
            body_tokens += len(ids); body_bytes += len(row['text'].encode())
            metadata.append(dict(id=row['id'], family=row['family'], category=row['category'], template_id=row['template_id'],
                text_sha256=row['text_sha256'], body_tokens=len(ids), body_bytes=len(row['text'].encode()), outcome_focus_enabled=True))
        probes = encode_probes(groups, tok)
        pilot = dict(rows=rows[:64], sampling='Same first64 IDs/facts/labels;24 structures; no reroll',
            all24_train_structures_covered=len({r['template_id'] for r in rows[:64]}) == 24,
            generated_source=True, source_families_independent=False, protected_test_used=False)
        if not pilot['all24_train_structures_covered']: raise ValueError('Fixed64 lacks24 structures')
        DATA.mkdir(parents=True)
        for name, value in (('train-source.json', dict(rows=rows, families=groups['train'])), ('transfer-probes.json', probes), ('content-pilot.json', pilot)):
            atomic_json(DATA/name, value); atomic_json(RUN/name, value)
        retention = CONTROL_DATA/'transfer-probes.json'
        # Preserve original128 bytes; they are retention cases, not new structural holdouts.
        (DATA/'retention-probes.json').write_bytes(retention.read_bytes())
        arrays = dict(tokens=np.asarray(tokens, dtype='<u2'), focus=np.asarray(masks, dtype=np.uint8),
            offsets=np.asarray(offsets, dtype='<i8'), lengths=np.asarray(lengths, dtype='<i4'))
        np.savez(DATA/'train.npz', **arrays)
        m = dict(kind=KIND, source='local_programmatic_Japanese', created_at=now(), seed=SEED,
            original_train_selection_seed=read_json(CONTROL_DATA/'manifest.json')['seed'], documents=2048, train_families=1024,
            template_count=24, category_counts=dict(Counter(r['category'] for r in rows)), metadata=metadata,
            generated_body_tokens=body_tokens, generated_body_bytes=body_bytes, serialized_tokens=len(tokens),
            full_CE_targets=body_tokens+2048, EOS_targets=2048, outcome_focus_body_targets=int(arrays['focus'].sum()),
            arrays_sha256=sha256(DATA/'train.npz'), tokenizer_sha256=base['tokenizer_sha256'],
            source_sha256={s:sha256(ROOT/s) for s in SOURCES}, train_source_sha256=sha256(DATA/'train-source.json'),
            probe_sha256=sha256(DATA/'transfer-probes.json'), retention_probe_sha256=sha256(DATA/'retention-probes.json'),
            pilot_sha256=sha256(DATA/'content-pilot.json'), original_manifest_sha256=sha256(CONTROL_DATA/'manifest.json'),
            original_train_source_sha256=sha256(CONTROL_DATA/'train-source.json'),
            replacement_checks=checks, leakage=leakage, newly_prepared_original_corpus_tokens=0,
            new_local_serialized_tokens=len(tokens), scientific_teacher_tokens=0, actual_GPU_seconds=0,
            protected_test_used=False, training_pool_accepted=False,
            loss_policy='All body+EOS ordinary CE weight1; focus annotates outcomes but does not replace supervision.',
            limitations='Only negation/comparison language replaced in the same selected2048; changes token length/lexical/EOS density together.128 new two-category probes share authored semantics; original128 are retention, not newly held-out grammar after replacement. Not independent natural-language quality or external truth certification.')
        atomic_json(DATA/'manifest.json', m); atomic_json(RUN/'manifest.json', m)
        RelationLanguageTrainView(DATA, sha256(DATA/'manifest.json'), require_accepted=False)
        elapsed = time.monotonic()-started
        if elapsed > 240: raise TimeoutError('CPU240s preparation budget exhausted')
        job.update(status='complete_pending_fixed64_content', completed_at=now(), CPU_seconds=elapsed,
            data_path=str(DATA), manifest_sha256=sha256(DATA/'manifest.json'), changed_documents=checks['changed_documents'])
        atomic_json(RUN/'job.json', job)
        atomic_json(ROOT/'reports/phase6/condition_relation_language_preparation.json', dict(status=job['status'], job=job,
            documents=2048, changed_documents=checks['changed_documents'], body_tokens=body_tokens, body_bytes=body_bytes,
            serialized_tokens=len(tokens), new_probe_families=128, retention_probe_families=128,
            actual_GPU_seconds=0, scientific_teacher_tokens=0, Base_adopted=False, Chat_started=False, quantization_started=False,
            protected_test_used=False, next_action='Read every fixed64 source text and preserve unchanged prior notes; require raw-bound acceptance before CUDA/frozen100M comparison.'))
        print(dict(status=job['status'], CPU_seconds=elapsed, changed_documents=checks['changed_documents'], body_tokens=body_tokens), flush=True)
    except BaseException as error:
        job.update(status='failed_preserve_fixed_or_partial', ended_at=now(), error=repr(error), CPU_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json', job); raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
