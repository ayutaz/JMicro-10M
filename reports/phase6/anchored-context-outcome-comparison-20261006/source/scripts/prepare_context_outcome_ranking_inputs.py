"""Encode existing TRAIN opposite-state outcomes only; no new corpus/label draws."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import collections
import time
import numpy as np
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from condition_relation_language import RelationLanguageTrainView
from context_outcome_ranking import RankingTrainView

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006')
OUT=Path('/home/aihub_ubuntu/jmicro-data/phase6/context-outcome-ranking-20261006')


def ref(p):return dict(path=str(p),sha256=sha256(p))


def main():
    started=time.monotonic()
    if OUT.exists():raise ValueError('Preserve prepared/partial fixed ranking inputs')
    cfg=read_json(ROOT/'configs/phase6/eos_decoupled_web_kl_comparison.json')
    view=RelationLanguageTrainView(DATA,cfg['positive_data']['manifest_sha256'])
    source=read_json(DATA/'train-source.json')
    if sha256(DATA/'train-source.json')!=view.manifest['train_source_sha256']:
        raise ValueError('Accepted train-family source differs')
    families,records=source['families'],source['rows']
    if len(families)!=1024 or len(records)!=2048 or any(f['split']!='train' for f in families) or any(r['split']!='train' for r in records):
        raise ValueError('Only all1024 existing train families required')
    tokenizer=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    by_id={r['id']:r for r in records}
    inputs=np.zeros((4096,256),dtype='<u2');labels=np.full((4096,256),-100,dtype='<i2')
    valid=np.zeros((4096,256),dtype=bool);sizes=np.zeros(4096,dtype='<i4')
    whole_equal=0;maximum=0;rows=[]
    for family_index,f in enumerate(families):
        if time.monotonic()-started>60:raise TimeoutError('Fixed60s CPU input encoding budget exhausted')
        if [b['label'] for b in f['branches']]!=[0,1] or f['branches'][0]['choices']!=f['branches'][1]['choices']:
            raise ValueError('Existing opposite labels and shared outcomes required')
        for b in f['branches']:
            original=by_id[f'{f["id"]}-{b["label"]}']
            if original['prefix']!=b['prefix'] or original['choices']!=b['choices'] or original['outcome']!=b['choices'][b['label']]:
                raise ValueError('No new states, candidates, labels or wording allowed')
            prefix=tokenizer.encode(b['prefix'])
            for candidate,text in enumerate(b['choices']):
                target=tokenizer.encode(text);ids=[2,*prefix,*target]
                width=len(ids)-1;cut=len(prefix)
                if not target or width>256 or any(t<8 for t in target) or tokenizer.decode_bytes(ids[1:])!=(b['prefix']+text).encode():
                    raise ValueError('Complete original candidate bytes/body IDs within256 required')
                i=4*family_index+2*b['label']+candidate
                inputs[i,:width]=ids[:-1];labels[i,cut:width]=target;valid[i,:width]=True;sizes[i]=len(text.encode())
                same=tokenizer.encode(b['prefix']+text)==ids[1:]
                whole_equal+=same;maximum=max(maximum,width)
                rows.append(dict(index=i,family=f['id'],category=f['category'],branch=b['label'],candidate=candidate,
                    gold=candidate==b['label'],prefix=b['prefix'],outcome=text,target_ids=target,context_tokens=cut+1,
                    target_bytes=int(sizes[i]),whole_joint_tokenization_equal=same))
    OUT.mkdir(parents=True)
    np.savez_compressed(OUT/'arrays.npz',inputs=inputs,labels=labels,valid=valid,target_bytes=sizes)
    atomic_json(OUT/'rows.json',dict(rows=rows))
    m=dict(kind='existing_train_relation_outcome_ranking_inputs_v1',created_at=now(),families=1024,candidate_rows=4096,
        context=256,source_split='train',new_original_corpus_tokens=0,
        train_manifest=ref(DATA/'manifest.json'),train_source=ref(DATA/'train-source.json'),
        accepted_review=ref(DATA/'content-review.json'),tokenizer_sha256=sha256(ROOT/'artifacts/phase2/4096/tokenizer.model'),
        arrays_sha256=sha256(OUT/'arrays.npz'),rows_sha256=sha256(OUT/'rows.json'),
        family_ids=[f['id'] for f in families],categories=dict(collections.Counter(f['category'] for f in families)),
        whole_joint_tokenization_equal_rows=whole_equal,separately_encoded_rows=4096-whole_equal,
        maximum_input_length=maximum,valid_input_positions=int(valid.sum()),physical_input_positions=inputs.size,
        body_outcome_positions=int((labels>=8).sum()),body_outcome_bytes=int(sizes.sum()),
        source_sha256={f:sha256(ROOT/f) for f in ('scripts/context_outcome_ranking.py','scripts/prepare_context_outcome_ranking_inputs.py')},
        learning_limits='Only accepted train families and existing declared states/outcomes used. Foil is correct outcome of opposite state. Shared local generator/retention forms are not independent external facts. No dev/test/probe material read for training inputs.',
        segmentation_limit='Same separately encoded candidate IDs across both contexts, as fixed diagnostic probes; joint-tokenization differences reported rather than silently changed. Main ordinary CE input bytes/tokens remain unchanged.')
    atomic_json(OUT/'manifest.json',m);RankingTrainView(OUT,sha256(OUT/'manifest.json'))
    elapsed=time.monotonic()-started
    if elapsed>60:raise TimeoutError('Fixed60s input encoding budget exhausted')
    atomic_json(ROOT/'reports/phase6/context_outcome_ranking_input_preparation.json',dict(status='actual_all1024_train_families_prepared_no_learning',
        created_at=now(),manifest=ref(OUT/'manifest.json'),rows=ref(OUT/'rows.json'),families=1024,candidate_rows=4096,
        CPU_elapsed_seconds=elapsed,CPU_ceiling_seconds=60,GPU_seconds=0,optimizer_updates=0,scientific_teacher_tokens=0,
        newly_prepared_original_corpus_tokens=0,categories=m['categories'],maximum_input_length=maximum,
        whole_joint_tokenization_equal_rows=whole_equal,separately_encoded_rows=4096-whole_equal,
        valid_input_positions=m['valid_input_positions'],body_outcome_positions=m['body_outcome_positions'],
        source_sha256=m['source_sha256'],Base_complete=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Own CE+conditionalKL+train-outcome-ranking trainer; full CPU resume and separate relational/gold/foil/valid/physical ledgers before actualCUDA bounded comparison.'))
    print(dict(families=1024,rows=4096,CPU_seconds=elapsed,max_input=maximum,separately_encoded=4096-whole_equal))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
