"""Pinned Aya upstream TRAIN only; acquisition and Japanese inventory, no TEST."""
import argparse
from collections import Counter, defaultdict
import json
import urllib.request
from answer_learning_common import ROOT, RUN, DATA, OLD_RUN, save, ref, bound, read_json, digest, now

PIN = 'f9ea04583f02a8f86404ff6c58bf75fe637df8a2'
FILE = 'data/train-00000-of-00001.parquet'
BASE = f'https://huggingface.co/datasets/CohereLabs/aya_dataset/resolve/{PIN}/'


def acquire():
    proposal = RUN/'aya_source_proposal.json'
    assert not proposal.exists() and not (RUN/'aya_acquisition.json').exists()
    metadata = read_json(RUN/'source_discovery/CohereLabs__aya_dataset.json')
    assert metadata['sha'] == PIN and metadata['gated'] is False
    save(proposal, dict(created_at=now(), source='CohereLabs/aya_dataset', revision=PIN,
        metadata=ref(RUN/'source_discovery/CohereLabs__aya_dataset.json'), upstream_split='train', artifact=FILE,
        acquisition_byte_cap=350_000_000, license='Apache-2.0 according to official card; preserve attribution',
        purpose='Measure Japanese complete direct-response TRAIN and inspect actual semantic quality before one matched SFT',
        scope='Only upstream TRAIN parquet. No upstream TEST, demographics or user_id column reads.',
        reader_disclosure='All TRAIN language codes read; Arrow may decompress non-Japanese TRAIN body rows within selected row groups. No project DEV is assigned within Aya before this read.',
        target_cap_including_EOT=64, complete_pair_context_cap=1025, generation_cap=32,
        QA_selection='Up to120: round-robin annotation_type x teacher_length_band; SHA answer-aya-QA42:doc_id order within strata',
        identities='aya_dataset_train:<zero-based original TRAIN row index>',
        gates=['Complete original Japanese prompt and response, no truncation or rewriting',
            'Old protected metadata-only exact/MinHash checks; report non-exhaustive recall',
            'Individual semantic QA required; mechanical eligibility is not quality certification'],
        new_project_DEV='Authored independently only after final TRAIN freeze', new_TEST_created=False,
        main_recipe_not_yet_frozen=True, new_training_updates=0))
    raw = DATA/'raw/aya_train.parquet'; raw.parent.mkdir(parents=True, exist_ok=True)
    assert not raw.exists()
    request = urllib.request.Request(BASE+FILE, headers={'User-Agent':'JMicro-local-source-audit/1'})
    total = 0
    with urllib.request.urlopen(request, timeout=180) as response, raw.open('xb') as out:
        while chunk := response.read(1024*1024):
            total += len(chunk)
            if total > 350_000_000: raise RuntimeError('Prospective byte cap exceeded; preserve partial file')
            out.write(chunk)
    card = RUN/'source_discovery/aya_README.md'
    with urllib.request.urlopen(BASE+'README.md', timeout=60) as response:
        body = response.read(1_000_001)
    assert len(body)<=1_000_000 and not card.exists(); card.write_bytes(body)
    save(RUN/'aya_acquisition.json', dict(created_at=now(), proposal=ref(proposal), artifact=ref(raw),
        bytes=total, official_card=ref(card), body_not_yet_parsed=True, upstream_TEST_acquired=False))
    print(json.dumps(dict(status='acquired',bytes=total,artifact=ref(raw))), flush=True)


def inventory():
    import pyarrow.parquet as pq
    from datasketch import MinHash, MinHashLSH
    from jmicro.data import normalized, japanese_ratio
    from jmicro.tokenizer import Tokenizer
    target = RUN/'aya_inventory.json'; assert not target.exists()
    acquisition=read_json(RUN/'aya_acquisition.json'); raw=bound(acquisition['artifact'])
    parquet=pq.ParquetFile(raw)
    expected={'inputs','targets','language','language_code','annotation_type','user_id'}
    assert set(parquet.schema_arrow.names)==expected
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    metadata=pq.read_table(ROOT/'data/phase1/processed/dataset_manifest.parquet',
        columns=['doc_id','split','dedup_sha256','minhash']).to_pylist()
    scheme=read_json(OLD_RUN/'availability.json')['signature_scheme']['scheme']; assert scheme=='affine32'
    protected=[m for m in metadata if m['split'] in ('dev','test')]
    hashes={m['dedup_sha256'] for m in protected}; signatures={}; lsh=MinHashLSH(num_perm=128,params=(32,4))
    for m in protected:
        if m['minhash']:
            mh=MinHash(num_perm=128,seed=42,scheme=scheme,hashvalues=m['minhash'])
            signatures[m['doc_id']]=mh; lsh.insert(m['doc_id'],mh)
    counts=Counter(); strata=defaultdict(list); seen=set(); offset=0; decoded=0
    records=DATA/'aya_eligible_TRAIN.jsonl'; assert not records.exists()
    with records.open('x') as out:
        for group in range(parquet.num_row_groups):
            codes=parquet.read_row_group(group,columns=['language_code']).column(0).to_pylist()
            counts['all_upstream_TRAIN_language_codes_read']+=len(codes)
            indices=[j for j,code in enumerate(codes) if code=='jpn']
            if not indices: offset+=len(codes); continue
            table=parquet.read_row_group(group,columns=['inputs','targets','annotation_type'])
            decoded+=len(codes)
            for index in indices:
                data=table.slice(index,1).to_pylist()[0]; counts['Japanese_rows_examined']+=1
                user,answer,kind=data['inputs'],data['targets'],data['annotation_type']
                assert isinstance(user,str) and isinstance(answer,str) and isinstance(kind,str)
                n=len(tok.encode(answer))+1
                band='2-32' if 2<=n<=32 else '33-64' if 33<=n<=64 else 'other'
                counts['Japanese_all_targets:'+band]+=1
                if not 2<=n<=64: continue
                if (not user.strip() or not answer.strip() or '\ufffd' in user+answer or '\x00' in user+answer or
                    japanese_ratio(user)<.2 or normalized(user)==normalized(answer)):
                    counts['empty_corrupt_non_Japanese_user_or_echo']+=1; continue
                if any(t in user+answer for t in ('<|user|>','<|assistant|>','<|system|>','<|eot|>','<|end|>')):
                    counts['reserved_control_literal']+=1; continue
                if len(tok.encode(user))+n+4>1025: counts['complete_pair_exceeds_context']+=1; continue
                text=normalized(user+'\n'+answer); hashed=digest(text)
                if hashed in hashes: counts['old_protected_exact']+=1; continue
                if hashed in seen: counts['TRAIN_exact_duplicate']+=1; continue
                mh=MinHash(num_perm=128,seed=42,scheme=scheme)
                mh.update_batch(sorted({text[j:j+5].encode() for j in range(max(1,len(text)-4))}))
                if any(mh.jaccard(signatures[k])>=.75 for k in lsh.query(mh)):
                    counts['old_protected_near_candidate']+=1; continue
                seen.add(hashed)
                uid='aya_dataset_train:'+str(offset+index)
                row=dict(doc_id=uid,split='train',source='Aya_Japanese_TRAIN',annotation_type=kind,
                    messages=[dict(role='user',text=user),dict(role='assistant',text=answer)],target_message_indices=[1],
                    target_teachers=n,normalized_pair_sha256=hashed,
                    original_selected_fields_sha256=digest(json.dumps(data,ensure_ascii=False,sort_keys=True)))
                out.write(json.dumps(row,ensure_ascii=False)+'\n'); strata[(kind,band)].append(row)
                counts['eligible:'+band+':targets']+=1; counts['eligible:'+band+':teachers']+=n
                counts['annotation_type:'+kind]+=1
            offset+=len(codes)
    sample=[]; wanted=min(120,sum(len(v) for v in strata.values()))
    for pool in strata.values(): pool.sort(key=lambda row:digest('answer-aya-QA42:'+row['doc_id']))
    cursor=0
    while len(sample)<wanted:
        for key in sorted(strata):
            if cursor<len(strata[key]) and len(sample)<wanted:
                sample.append(dict(id=f'Y{len(sample)+1:03}',stratum=key,**strata[key][cursor]))
        cursor+=1
    save(DATA/'aya_QA_sample.json',sample)
    save(target,dict(status='measured_pending_individual_QA',created_at=now(),acquisition=ref(RUN/'aya_acquisition.json'),
        proposal=ref(RUN/'aya_source_proposal.json'),records=ref(records),counts=dict(counts),
        schema=str(parquet.schema_arrow),num_row_groups=parquet.num_row_groups,
        TRAIN_rows_in_body_decoded_row_groups=decoded,
        reader_disclosure='Arrow body column decoding includes other TRAIN languages in Japanese-containing row groups; only jpn rows converted to Python values',
        sample=ref(DATA/'aya_QA_sample.json'),sample_size=len(sample),old_metadata_columns=['doc_id','split','dedup_sha256','minhash'],
        old_signature_scheme=scheme,old_signature_threshold=.75,LSH_recall_not_exhaustive=True,
        upstream_ancestry_overlap_not_excluded=True,new_project_DEV_not_yet_authored=True,
        upstream_TEST_body_read=False,user_id_column_read=False,demographics_read=False,new_training_updates=0))
    print(json.dumps(dict(counts=dict(counts),sample=len(sample),body_decoded_rows=decoded),ensure_ascii=False),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['acquire','inventory']);a=p.parse_args()
    {'acquire':acquire,'inventory':inventory}[a.mode]()
