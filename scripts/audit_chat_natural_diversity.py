"""Describe speaker/family concentration and TRAIN-only near duplication.

No frozen data is edited or reselected. This audit reads only already allowed
TRAIN members and bound final TRAIN records. LSH retrieval is probabilistic;
exact Jaccard is calculated for retrieved pairs, not every possible pair.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from datasketch import MinHash,MinHashLSH
from jmicro.tokenizer import Tokenizer
from jmicro.data import normalized
from chat_natural_contract import DATA,RUN,CONFIG,ref,read_bound
from jmicro.experiment import read_json,now
from jmicro.training import atomic_json


def h(text):return hashlib.sha256(text.encode()).hexdigest()


def main():
    target=RUN/'TRAIN_diversity_audit.json'
    assert not target.exists()
    c=read_json(CONFIG)
    rows={arm:[json.loads(line) for line in Path(c['arms'][arm]['records']['path']).read_text().splitlines()]
          for arm in ('C0','C1')}
    allowed=set(read_json(DATA/'RPC_allowed_identities.json')['train'])
    rpc=set(row['doc_id'] for pool in rows.values() for row in pool if row['source']=='RPC')
    speakers={}
    with zipfile.ZipFile(DATA/'raw/real_persona_chat.zip') as archive:
        for uid in sorted(rpc):
            member=uid.split(':',1)[1]
            assert member in allowed
            original=json.loads(archive.read(member))
            first=original['utterances'][0]['interlocutor_id']
            other=[speaker for speaker in original['interlocutors'] if speaker!=first]
            assert len(other)==1
            speakers[uid]=h('RPC-source-speaker:'+str(other[0]))[:16]
    tok=Tokenizer(c['tokenizer']['path'])
    reports={}
    for arm,pool in rows.items():
        flat=[];family_supply=Counter();speaker_supply=Counter();answer_counts=Counter();source_supply=Counter()
        lengths=Counter();prefixes=Counter()
        for row in pool:
            uid=row['doc_id'];speaker=speakers.get(uid,'synthetic_model_not_human_speaker')
            for index in row['target_message_indices']:
                answer=row['messages'][index]['text']
                teachers=len(tok.encode(answer))+1
                assert 2<=teachers<=32
                flat.append((uid,speaker,row['source'],teachers))
                family_supply[uid]+=teachers;speaker_supply[speaker]+=teachers
                source_supply[row['source']]+=teachers;answer_counts[normalized(answer)]+=1;lengths[teachers]+=1
            if len(row['messages'])>=4:
                prefix=normalized('\n'.join(m['text'] for m in row['messages'][:4]))
                if len(prefix)>=80:prefixes[h(prefix)]+=1
        dry=read_bound(c['arms'][arm]['dry_run']);terminal=dry['sampler_terminal']
        assert len(flat)==dry['prepared_targets']
        assert sum(source_supply.values())==dry['teachers_per_pass']
        consumed_speakers=Counter();consumed_source=Counter();consumed_families=Counter()
        for epoch in range(terminal['epoch']+1):
            order=np.random.default_rng(np.random.SeedSequence([42,epoch])).permutation(len(flat))
            stop=len(flat) if epoch<terminal['epoch'] else terminal['position']
            for index in order[:stop]:
                uid,speaker,source,teachers=flat[int(index)]
                consumed_speakers[speaker]+=teachers;consumed_source[source]+=teachers;consumed_families[uid]+=teachers
        assert dict(consumed_source)==dry['actual_consumed_source_teachers']
        total=sum(consumed_source.values());human={k:v for k,v in consumed_speakers.items() if k!='synthetic_model_not_human_speaker'}
        reports[arm]=dict(families=len(pool),prepared_targets=len(flat),prepared_teacher_tokens=sum(source_supply.values()),
            raw_distinct_answer_texts=dry['distinct_answer_texts'],normalized_distinct_answer_texts=len(answer_counts),
            repeated_normalized_answer_targets=sum(n-1 for n in answer_counts.values()),
            EOT_per_target=True,maximum_prepared_teachers_per_family=max(family_supply.values()),
            human_Assistant_speakers=len(human),speaker_teacher_range=[min(human.values()),max(human.values())],
            human_teacher_top5_share=sum(sorted(human.values(),reverse=True)[:5])/sum(human.values()),
            predetermined_consumed_source_teachers=dict(consumed_source),
            predetermined_teacher_tokens=total,consumption_replay_matches_frozen_sampler=True,
            maximum_consumed_family_teacher_share=max(consumed_families.values())/total,
            shared_initial4_messages_clusters=sum(n>1 for n in prefixes.values()),
            shared_initial4_messages_extra_families=sum(n-1 for n in prefixes.values() if n>1))
    lsh=MinHashLSH(num_perm=128,params=(32,4));shingle_sets={};candidate_pairs=0;near=0;samples=[]
    for row in rows['C1']:
        text=normalized('\n'.join(m['text'] for m in row['messages']))
        if len(text)<80:continue
        shingles={text[i:i+5].encode() for i in range(len(text)-4)}
        mh=MinHash(num_perm=128,seed=42,scheme='affine32');mh.update_batch(sorted(shingles))
        for other in lsh.query(mh):
            candidate_pairs+=1;prior=shingle_sets[other]
            similarity=len(shingles&prior)/len(shingles|prior)
            if similarity>=.85:
                near+=1
                if len(samples)<100:samples.append(dict(left=other,right=row['doc_id'],exact_char5_Jaccard=similarity))
        uid=row['doc_id'];lsh.insert(uid,mh);shingle_sets[uid]=shingles
    atomic_json(target,dict(status='descriptive_audit_complete_data_unchanged',created_at=now(),config=ref(CONFIG),
        arms=reports,C1_near_duplicate_audit=dict(minimum_document_characters=80,char_ngram=5,num_perm=128,
            seed=42,scheme='affine32',LSH_bands=32,rows_per_band=4,exact_Jaccard_threshold=.85,
            retrieved_pairs=candidate_pairs,verified_near_pairs=near,sample_pairs=samples),
        protected_TEST_payloads_read=0,source_RPC_members_read=len(rpc),prepared_data_modified=False,
        limitations=['Character-near duplication is not semantic equivalence; LSH can miss pairs',
            'More conversation families do not imply independent human speakers or novel factual knowledge',
            'Consumption is derived from the frozen deterministic sampler; terminal training audits establish actual execution'],
        source=ref(Path(__file__))))
    print(json.dumps(dict(arms=reports,C1_near_pairs=near),ensure_ascii=False),flush=True)


if __name__=='__main__':main()
