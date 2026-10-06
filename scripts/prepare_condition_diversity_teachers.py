"""Prepare nested original2048 IDs/masks without changing the original2B corpus."""
import hashlib
from pathlib import Path
import sys
import tarfile
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from condition_positive_trainer import PositiveTrainView
from prepare_condition_positive_teachers import outcome_token_mask
from prepare_condition_diversity_source import OUT,SMALL,nested

OUTPUT=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-diversity-positive-20261006')


def main():
    started=time.monotonic()
    if OUTPUT.exists(): raise ValueError('Preserve fixed nested teacher preparation; no overwrite')
    review=read_json(OUT/'content-review.json'); source=read_json(OUT/'source-pairs.json')['rows']
    original=read_json(SMALL/'source-pairs.json')['rows']; nested(source,original)
    if (not review['all64_read'] or not review['training_pool_accepted'] or review['weak_pairs']>10
            or review['notes_sha256']!=sha256(OUT/'content-notes.tsv')
            or review['source_pairs_sha256']!=sha256(OUT/'source-pairs.json') or len(source)!=2048):
        raise ValueError('Accepted fixed64 new content and2048 nested source required')
    config=read_json(ROOT/'configs/phase6/condition_positive_comparison.json')
    old=PositiveTrainView(config['positive_data']['path'],config['positive_data']['manifest_sha256'])
    pool=TrainView(config['pool']['pool'],config['pool']['manifest_sha256'])
    base=read_json(Path(config['original_config']['path']))
    if sha256(ROOT/base['tokenizer'])!=base['tokenizer_sha256']: raise ValueError('Tokenizer changed')
    tokenizer=Tokenizer(ROOT/base['tokenizer'])
    weak={n['id'] for n in review['notes'] if n['weak_pair']}
    weak|={n['id'] for n in read_json(SMALL/'content-review.json')['notes'] if n['weak_pair']}
    ids_all=[]; masks=[]; offsets=[]; lengths=[]; metadata=[]; body_tokens=body_bytes=0
    for row in source:
        if time.monotonic()-started>30: raise TimeoutError('CPU30s preparation exhausted')
        offset=row['train_offset']; count=row['original_body_tokens']; ids=pool.tokens[offset:offset+count+2].tolist()
        raw=tokenizer.decode_bytes(ids[1:-1])
        if (row['split']!='train' or row['source']!='textbook' or ids[0]!=2 or ids[-1]!=3
                or any(i<8 for i in ids[1:-1]) or raw.decode()!=row['original_text']
                or hashlib.sha256(raw).hexdigest()!=row['decoded_body_sha256']):
            raise ValueError('Whole original train body binding differs')
        for branch in row['branches']:
            if branch['prefix']!=row['original_text'][:branch['cut']] or branch['outcome']!=row['original_text'][branch['cut']:branch['end']]:
                raise ValueError('Original outcome span differs')
        mask=outcome_token_mask(row['original_text'],ids[1:-1],tokenizer,row['branches'])
        if row['id'] in weak: mask[:]=0
        offsets.append(len(ids_all)); lengths.append(len(ids)); ids_all.extend(ids); masks.extend(mask.tolist())
        body_tokens+=count; body_bytes+=len(raw)
        metadata.append(dict(id=row['id'],original_document_index=row['document_index'],
            original_train_offset=offset,decoded_body_sha256=row['decoded_body_sha256'],outcome_focus_enabled=row['id'] not in weak))
    arrays=dict(tokens=np.asarray(ids_all,dtype='<u2'),focus=np.asarray(masks,dtype=np.uint8),
        offsets=np.asarray(offsets,dtype='<i8'),lengths=np.asarray(lengths,dtype='<i4'))
    checks=dict(tokens=np.array_equal(arrays['tokens'][:len(old.tokens)],old.tokens),
        focus=np.array_equal(arrays['focus'][:len(old.focus)],old.focus),
        offsets=np.array_equal(arrays['offsets'][:512],old.offsets),
        lengths=np.array_equal(arrays['lengths'][:512],old.lengths),metadata=metadata[:512]==old.manifest['metadata'])
    if not all(checks.values()): raise ValueError('Actual nested512 IDs/masks/metadata changed')
    OUTPUT.mkdir(parents=True); np.savez(OUTPUT/'train.npz',**arrays)
    manifest=dict(kind='original_train_positive_condition_outcome_spans',created_at=now(),documents=2048,
        unique_normalized_bodies=2048,original_body_tokens=body_tokens,original_body_bytes=body_bytes,
        serialized_tokens=len(ids_all),EOS_targets=2048,full_CE_targets=body_tokens+2048,
        outcome_focus_body_targets=int(arrays['focus'].sum()),known_weak_pilot_documents_with_focus_disabled=len(weak),
        focus_enabled_documents=2048-len(weak),metadata=metadata,arrays_sha256=sha256(OUTPUT/'train.npz'),
        source_pairs_sha256=sha256(OUT/'source-pairs.json'),content_review_sha256=sha256(OUT/'content-review.json'),
        original_pool_manifest_sha256=config['pool']['manifest_sha256'],tokenizer_sha256=base['tokenizer_sha256'],
        nested_small_manifest_sha256=old.manifest_sha256,nested_small_actual_checks=checks,
        newly_prepared_original_tokens=0,copied_existing_serialized_tokens=len(ids_all),
        scientific_teacher_tokens=0,actual_GPU_seconds=0,protected_test_used=False,hard_negative_labels_created=0,
        mask_policy='Unchanged original token byte overlap; BOS/EOS never marked. Known old8/new4 weak pilot focus disabled; full original body+EOS CE retained. Next comparison uses weight1 so mask does not reweight learning.',
        limitations='All source already in original2B; local exact body uniqueness only; only64 new/64 old individually reviewed. No global/family/factual certification, no retokenization or source rewrite.')
    atomic_json(OUTPUT/'manifest.json',manifest)
    PositiveTrainView(OUTPUT,sha256(OUTPUT/'manifest.json'))
    archive=ROOT/'reports/phase6/condition_diversity_teacher_data.tar.gz'; temporary=archive.with_suffix('.tmp')
    if archive.exists(): raise ValueError('Archive immutable')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for name in ('manifest.json','train.npz'): stream.add(OUTPUT/name,arcname=name,recursive=False)
    temporary.replace(archive)
    report=dict(status='actual_nested2048_original_teacher_arrays_prepared_learning_not_started',created_at=now(),
        CPU_seconds=time.monotonic()-started,CPU_limit_seconds=30,data_path=str(OUTPUT),
        manifest_sha256=sha256(OUTPUT/'manifest.json'),arrays_sha256=manifest['arrays_sha256'],
        script_sha256=sha256(Path(__file__)),documents=2048,original_body_tokens=body_tokens,original_body_bytes=body_bytes,
        serialized_tokens=len(ids_all),full_CE_targets=body_tokens+2048,outcome_focus_body_targets=manifest['outcome_focus_body_targets'],
        nested_small_actual_checks=checks,known_weak_focus_disabled=len(weak),scientific_teacher_tokens=0,
        actual_GPU_seconds=0,newly_prepared_original_tokens=0,protected_test_used=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,archive=dict(path=str(archive),sha256=sha256(archive),bytes=archive.stat().st_size),
        next_action='Implement/review matched25M ordinary CE512 vs2048 using frozen parent/quotas/weight1; reuse control after binding checks, CPU/CUDA fullstate resume and measured budget before science.')
    atomic_json(ROOT/'reports/phase6/condition_diversity_teacher_preparation.json',report)
    print(report)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
