"""Bounded original TRAIN prefix/suffix probe data; no corpus scan or new EOS."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import re
import sys
import time
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src')]
import numpy as np
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer

POOL = Path('/home/aihub_ubuntu/jmicro-data/phase6/textbook-mixture-20261006/large')
OUT = ROOT/'reports/phase6/natural_context_contrast_preparation.json'
RUN = Path('/home/aihub_ubuntu/jmicro-data/phase6/natural-context-contrast-20261007')
SEED = 2026100743


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    if OUT.exists():
        raise ValueError('Preserve one fixed TRAIN draw; no outcome-based reroll')
    start = time.monotonic()
    review_path = ROOT/'reports/phase6/textbook_mixture_content_review.json'
    review = json.loads(review_path.read_text())
    detail = review['pools']['large']
    if not review['passed'] or review['documents'] != 64 or review['weak_documents'] > 10:
        raise ValueError('Already accepted broad TRAIN source required')
    manifest_path = POOL/'manifest.json'
    if str(POOL) != detail['pool'] or sha256(manifest_path) != detail['manifest_sha256']:
        raise ValueError('Accepted large2B manifest differs')
    manifest = json.loads(manifest_path.read_text())
    index = POOL/'train.index.jsonl'
    stat = index.stat()
    ready_path = POOL/('.compact-index-'+detail['manifest_sha256'][:16])/'ready.json'
    ready = json.loads(ready_path.read_text())
    binding = ready['binding']
    train = manifest['splits']['train']
    if (binding['manifest_sha256'] != detail['manifest_sha256']
            or binding['index_sha256'] != train['index_sha256']
            or binding['index_size'] != stat.st_size or binding['index_mtime_ns'] != stat.st_mtime_ns
            or not ready['source_hash_verified_during_single_parse']):
        raise ValueError('Reuse the prior exact index verification; no13GB rescan')
    tokens_path = POOL/'train.bin'
    token_stat = tokens_path.stat()
    if token_stat.st_size != train['tokens']*2:
        raise ValueError('Accepted TRAIN stream size differs')
    tokens = np.memmap(tokens_path,dtype='<u2',mode='r')
    tokenizer_path = ROOT/'artifacts/phase2/4096/tokenizer.model'
    tokenizer = Tokenizer(tokenizer_path)
    rng = random.Random(SEED)
    draws = [rng.randrange(0,stat.st_size) for _ in range(512)]
    selected = []
    seen_families = set()
    seen_bodies = set()
    reasons = Counter()
    with index.open('rb') as stream:
        for draw in draws:
            if time.monotonic()-start > 30:
                raise TimeoutError('Bounded TRAIN data probe CPU30s exhausted')
            stream.seek(draw)
            if draw:
                stream.readline(16384)
            location = stream.tell()
            raw = stream.readline(16385)
            if not raw or len(raw)>16384:
                reasons['no_complete_bounded_index_record']+=1
                continue
            row = json.loads(raw)
            if row['split']!='train':
                raise ValueError('TRAIN-only file required')
            if row['source_family'] in seen_families:
                reasons['same_source_family']+=1
                continue
            count = row['body_tokens']
            if not 64<=count<=512:
                reasons['probe_whole_unit_length']+=1
                continue
            offset = row['offset']
            serialized = tokens[offset:offset+count+2].tolist()
            if len(serialized)!=count+2 or serialized[0]!=2 or serialized[-1]!=3:
                raise ValueError('Original serialized unit bounds differ')
            body_ids = serialized[1:-1]
            body = tokenizer.decode_bytes(body_ids)
            try:
                text = body.decode('utf-8')
            except UnicodeDecodeError:
                reasons['invalid_UTF8_original_unit']+=1
                continue
            if tokenizer.encode(text)!=body_ids or digest(body)!=row['canonical_sha256']:
                raise ValueError('Original unit canonical bytes/IDs differ')
            if digest(body) in seen_bodies:
                reasons['same_original_body']+=1
                continue
            cuts = [m.end() for m in re.finditer(r'[。！？](?:[」』）)]*)|\n',text)]
            cuts.sort(key=lambda n:(abs(n-len(text)/2),n))
            pair = None
            for cut in cuts:
                prefix,suffix = text[:cut],text[cut:]
                prefix_ids,suffix_ids = tokenizer.encode(prefix),tokenizer.encode(suffix)
                if (16<=len(prefix_ids)<=384 and 16<=len(suffix_ids)<=384
                        and body_ids[:len(prefix_ids)]==prefix_ids
                        and tokenizer.decode_bytes(prefix_ids)==prefix.encode()
                        and tokenizer.decode_bytes(suffix_ids)==suffix.encode()):
                    pair=dict(prefix=prefix,suffix=suffix,prefix_ids=prefix_ids,suffix_ids=suffix_ids,
                        char_cut=cut,byte_cut=len(prefix.encode()))
                    break
            if pair is None:
                reasons['no_original_sentence_boundary_pair']+=1
                continue
            selected.append(dict(index=len(selected),source_family=row['source_family'],source=row['source'],
                index_byte_position=location,index_record_sha256=digest(raw),source_index_record=row,
                full_original_text=text,full_original_body_sha256=digest(body),full_body_ids=body_ids,
                original_BOS=2,original_EOS=3,body_tokens=count,body_UTF8_bytes=len(body),
                prefix_suffix_embeddings_have_no_appended_EOS=True,**pair))
            seen_families.add(row['source_family'])
            seen_bodies.add(digest(body))
            if len(selected)==64:
                break
    if len(selected)!=64 or len({r['source'] for r in selected})!=3:
        raise ValueError('Fixed512 draws lacked64 distinct TRAIN families/all3 accepted genres; no reroll')
    if (index.stat().st_size,index.stat().st_mtime_ns)!=(stat.st_size,stat.st_mtime_ns):
        raise ValueError('Accepted index changed')
    RUN.mkdir(parents=True,exist_ok=True)
    sample = RUN/'sample64.json'
    atomic_json(sample,dict(seed=SEED,rows=selected))
    report = dict(status='fixed64_original_TRAIN_context_suffix_probe_inputs_prepared',created_at=now(),
        accepted_source_review_sha256=sha256(review_path),pool=str(POOL),manifest_sha256=sha256(manifest_path),
        old_exact_index_verification_reused=dict(path=str(ready_path),sha256=sha256(ready_path),binding=binding),
        train_stream_bytes=token_stat.st_size,train_stream_mtime_ns=token_stat.st_mtime_ns,
        tokenizer_sha256=sha256(tokenizer_path),script_sha256=sha256(Path(__file__)),
        sample=dict(path=str(sample),sha256=sha256(sample)),seed=SEED,fixed_maximum_draws=512,
        selected_pairs=64,distinct_source_families=64,genre_counts=dict(Counter(r['source'] for r in selected)),
        exclusions=dict(reasons),total_original_body_tokens=sum(r['body_tokens'] for r in selected),
        all_selected_original_unit_bytes_and_IDs_verified=True,no_source_text_rewriting=True,
        no_artificial_EOS_at_prefix_suffix_split=True,no_old_corpus_or_13GB_index_scan=True,
        original_source_acceptance_unchanged=True,protected_dev_test_records_used=False,
        new_full_training_pool_tokens=0,scientific_teacher_tokens=0,optimizer_updates=0,GPU_seconds=0,
        CPU_wall_seconds=time.monotonic()-start,Base_complete=False,Chat_started=False,quantization_started=False,
        next_action='Implement and freeze the native10M observed-context/suffix InfoNCE feature objective alongside unchanged full-unit body+EOS CE. Probe finite noncollapsed gradients, stable batch/throughput, actual full-state save/resume under GPU180s before a measured matched-CE scientific comparison.',
        limitations='These are64 old accepted TRAIN units for an implementation/gradient probe, not new64 content acceptance, new source supply or model quality. Byte-uniform index-line selection is length-weighted, not a population quality estimate. An observed matching is a corpus relation; other continuations are distractors, not certified logically false facts. No teacher model, synthetic prose, dev/test training or new parameters.')
    atomic_json(OUT,report)
    print({k:report[k] for k in ('selected_pairs','genre_counts','total_original_body_tokens','CPU_wall_seconds','sample')})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
