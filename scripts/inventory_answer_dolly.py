"""Allowlisted TRAIN-only Dolly extraction; full targets, metadata-only held checks."""
from collections import Counter,defaultdict
import json
from pathlib import Path
import sys
from answer_learning_common import ROOT,RUN,DATA,OLD_RUN,save,ref,bound,read_json,digest,now
from jmicro.data import normalized,japanese_ratio
from jmicro.tokenizer import Tokenizer
import pyarrow.parquet as pq
from datasketch import MinHash,MinHashLSH


def main():
    target=RUN/'dolly_inventory.json';assert not target.exists()
    proposal=read_json(RUN/'dolly_source_proposal.json');acquisition=read_json(RUN/'dolly_acquisition.json')
    raw=bound(acquisition['artifact']);assert raw.name==proposal['artifact']
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    metadata=pq.read_table(ROOT/'data/phase1/processed/dataset_manifest.parquet',
        columns=['doc_id','split','dedup_sha256','minhash']).to_pylist()
    scheme=read_json(OLD_RUN/'availability.json')['signature_scheme']['scheme'];assert scheme=='affine32'
    protected=[m for m in metadata if m['split'] in ('dev','test')]
    held_hashes={m['dedup_sha256'] for m in protected};held={};lsh=MinHashLSH(num_perm=128,params=(32,4))
    for m in protected:
        if m['minhash']:
            sig=MinHash(num_perm=128,seed=42,scheme=scheme,hashvalues=m['minhash'])
            held[m['doc_id']]=sig;lsh.insert(m['doc_id'],sig)
    counts=Counter();reserved=[];rows=[];seen=set();strata=defaultdict(list)
    records=DATA/'dolly_eligible_TRAIN.jsonl';assert not records.exists()
    with raw.open() as stream,records.open('x') as out:
        for i,line in enumerate(stream):
            uid='dolly_ja_llmjp:'+str(i)
            if int(digest('answer-dolly-dev42:'+uid)[:8],16)%10==0:
                reserved.append(uid);counts['reserved_project_DEV_not_JSON_parsed']+=1;continue
            data=json.loads(line);counts['allowed_TRAIN_JSON_parsed']+=1
            assert set(data)=={'instruction','context','response','category'}
            assert all(isinstance(data[k],str) for k in data)
            user=data['instruction']+('\n\n'+data['context'] if data['context'] else '')
            answer=data['response'];category=data['category']
            n=len(tok.encode(answer))+1
            band='2-32' if 2<=n<=32 else '33-64' if 33<=n<=64 else '65+'
            counts['all_targets:'+band]+=1
            if not 2<=n<=64:continue
            if (not user.strip() or not answer.strip() or '\ufffd' in user+answer or '\x00' in user+answer or
                japanese_ratio(user)<.2 or normalized(user)==normalized(answer)):
                counts['empty_corrupt_non_Japanese_user_or_echo']+=1;continue
            if any(token in user+answer for token in ('<|user|>','<|assistant|>','<|system|>','<|eot|>','<|end|>')):
                counts['reserved_control_literal']+=1;continue
            messages=[dict(role='user',text=user),dict(role='assistant',text=answer)]
            if len(tok.encode(user))+len(tok.encode(answer))+5>1025:
                counts['complete_pair_exceeds_context']+=1;continue
            text=normalized(user+'\n'+answer);hashed=digest(text)
            if hashed in held_hashes:counts['old_protected_exact']+=1;continue
            if hashed in seen:counts['TRAIN_exact_duplicate']+=1;continue
            mh=MinHash(num_perm=128,seed=42,scheme=scheme)
            mh.update_batch(sorted({text[j:j+5].encode() for j in range(max(1,len(text)-4))}))
            if any(mh.jaccard(held[k])>=.75 for k in lsh.query(mh)):
                counts['old_protected_near_candidate']+=1;continue
            seen.add(hashed)
            row=dict(doc_id=uid,split='train',source='Dolly_llmjp',messages=messages,target_message_indices=[1],
                target_teachers=n,category=category,source_context_present=bool(data['context']),
                normalized_pair_sha256=hashed,original_row_sha256=digest(line.rstrip('\n')))
            out.write(json.dumps(row,ensure_ascii=False)+'\n');rows.append(row)
            counts['eligible:'+band+':targets']+=1;counts['eligible:'+band+':teachers']+=n
            counts['category:'+category+':targets']+=1
            counts['source_context_present']+=bool(data['context'])
            strata[(category,band,bool(data['context']))].append(row)
            if counts['allowed_TRAIN_JSON_parsed']%2000==0:print('Parsed permitted TRAIN '+str(counts['allowed_TRAIN_JSON_parsed']),flush=True)
    sample=[]
    for key,pool in strata.items():pool.sort(key=lambda r:digest('answer-dolly-QA42:'+r['doc_id']))
    cursor=0
    while len(sample)<120:
        added=False
        for key in sorted(strata):
            if cursor<len(strata[key]) and len(sample)<120:
                row=strata[key][cursor];sample.append(dict(id=f'D{len(sample)+1:03}',stratum=key,**row));added=True
        assert added;cursor+=1
    save(DATA/'dolly_reserved_DEV_identities.json',dict(ids=reserved,body_JSON_parsed=False,new_TEST_created=False))
    save(DATA/'dolly_QA_sample.json',sample)
    save(target,dict(status='measured_pending_individual_QA',created_at=now(),proposal=ref(RUN/'dolly_source_proposal.json'),
        acquisition=ref(RUN/'dolly_acquisition.json'),records=ref(records),counts=dict(counts),
        sample=ref(DATA/'dolly_QA_sample.json'),sample_size=120,
        selection='Round-robin category x teacher_length_band x source_context_presence, hash-sorted within strata',
        reserved_identities=ref(DATA/'dolly_reserved_DEV_identities.json'),
        metadata_columns_read=['doc_id','split','dedup_sha256','minhash'],signature_scheme=scheme,
        held_signature_similarity_threshold=.75,LSH_recall_not_exhaustive=True,
        neutral_semantic_quality_not_yet_accepted=True,
        text_format='Original instruction plus blank line plus original context if present; original response unchanged',
        generation_cap=32,complete_teacher_cap=64,non_Japanese_answer_allowed_for_literal_or_translation_tasks=True,
        upstream_corpus_web_overlap_not_excluded=True,protected_TEST_body_parsed=False,new_TEST_created=False,new_training_updates=0))
    print(json.dumps(dict(counts=dict(counts),sample=120),ensure_ascii=False),flush=True)


if __name__=='__main__':main()
