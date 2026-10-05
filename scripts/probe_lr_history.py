"""Same train/dev32 gold and free generation on saved100M/300M models."""
import gc
import math
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.model import JMicroModel
from run_generation_transfer import make_case
from run_root_cause_diagnostic import teacher,generate


def probe(run,base,old,shard,tok,recipe,check,heartbeat):
    path=run/'history-probe.json'
    if path.exists():return read_json(path)
    rng=random.Random(2026100600);records=[]
    for group,count in [('short',8),('narrative',8),('general',16)]:
        eligible=[r for r in shard.index if r['bucket']==group]
        for r in rng.sample(eligible,count):
            ids=shard.tokens[r['offset']+1:r['offset']+1+r['body_tokens']].tolist()
            records.append(dict(r,text=tok.decode_bytes(ids).decode('utf-8')))
    train=[make_case(r,tok,'train') for r in records]
    dev=[make_case(r,tok,'dev') for r in read_json(Path('/home/aihub_ubuntu/jmicro-data/phase6/curriculum-strategy-20261005-v3/dev32.json'))]
    write_json(run/'history-cases.json',dict(train=train,dev=dev))
    old_result=read_json(old/'compare-result.json');base_result=read_json(base/'compare-result.json')
    baselines=read_json(base/'baselines.json');entries={'original10B':recipe['parent']}
    for suffix,result in [('100M',base_result),('reheat300M',old_result)]:
        for arm,d in result['checkpoints'].items():entries[arm+'_'+suffix]=dict(path=d['checkpoint'],sha256=d['checkpoint_sha256'])
    results={}
    for name,entry in entries.items():
        check();assert sha256(Path(entry['path']))==entry['sha256']
        state=torch.load(entry['path'],map_location='cpu',weights_only=False)
        model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
        parts={}
        for split,cases in [('train',train),('dev',dev)]:
            cache_name=('before_continuation' if name=='original10B' else 'after_'+name.removesuffix('_100M'))
            cache=(baselines['results'][cache_name] if split=='dev' and (name=='original10B' or name.endswith('_100M')) else None)
            if cache:gold=cache['teacher'];rows=cache['generation']
            else:
                full=[dict(r,prefix_ids=[2],gold_ids=[*r['body_ids'],3]) for r in cases];gold=[];rows=[]
                for offset in range(0,32,16):
                    check();heartbeat('history-'+name+'-'+split)
                    gold.extend(teacher(model,full[offset:offset+16]))
                    if split=='train':rows.extend(generate(model,cases[offset:offset+16],tok,None,64))
                if split=='dev':rows=old_result['auxiliary'][name.removesuffix('_reheat300M')]['generation']
            assert [r['id'] for r in gold]==[r['id'] for r in cases]==[r['id'] for r in rows]
            size=sum(len(r['text'].encode()) for r in cases)
            nll=sum(sum(s['target_nll'] for s in r['teacher_steps'][:-1]) for r in gold)
            parts[split]=dict(body_bytes=size,body_NLL=nll,BPB=nll/math.log(2)/size,
                EOS=sum(r['stop_reason']=='eos' for r in rows),
                repeated4gram=sum(r['first_repeated_4gram'] is not None for r in rows),teacher=gold,generation=rows)
        results[name]=dict(checkpoint=entry,**parts)
        write_json(run/'history-progress.json',results)
        del model;gc.collect();torch.cuda.empty_cache()
    report=dict(status='complete_read_only_diagnostic',scientific_teacher_tokens=0,results=results,
        cases_sha256=sha256(run/'history-cases.json'),source_history='Auxiliary Web dev may be known to original10B; official held-out evaluation remains separate',
        interpretation='Train and dev sizes/bytes fixed across models. Repeated4gram presence is a raw proxy, not a full semantic-loop review.',created_at=now())
    write_json(path,report);return report
