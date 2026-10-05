"""Follow up failed frozen BF16 tolerances without changing those tolerances."""
import gc
import json
from pathlib import Path
import time
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from run_root_cause_diagnostic import OUT,TOK,identity,padded,distribution,choose,first_repeated_ngram
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.experiment import read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,seed_all,implementation_hashes


@torch.no_grad()
def measure(model,cases,tok):
    x,mask=padded([[2,*r['body_ids']] for r in cases],'cuda')
    with sdpa_kernel([SDPBackend.MATH]):
        fp=model(x,attention_mask=mask).logits
        with torch.autocast('cuda',dtype=torch.bfloat16):
            bf=model(x,attention_mask=mask).logits
            first=model(x[:,:8],attention_mask=mask[:,:8],use_cache=True)
            tail=model(x[:,8:],attention_mask=mask[:,8:],cache=first.cache).logits
        p,q=fp.softmax(-1),bf.softmax(-1)
        tv=(p-q).abs().sum(-1)*.5
        endings=[]
        for i,row in enumerate(cases):
            last=mask[i].sum()-1
            begin=len(row['prefix_ids'])-1
            targets=torch.tensor(row['gold_ids'],device='cuda')
            steps=torch.arange(begin,begin+len(targets),device='cuda')
            endings.append(dict(id=row['id'],source=row['source'],fp32=distribution(fp[i,last],3),
                bf16=distribution(bf[i,last],3),bf16_cached=distribution(tail[i,last-8],3),
                fp32_teacher_nll=float(-p[i,steps,targets].log().mean()),
                bf16_teacher_nll=float(-q[i,steps,targets].log().mean()),
                mean_total_variation=float(tv[i,mask[i]].mean()),max_total_variation=float(tv[i,mask[i]].max()),
                top1_agreement=float((fp[i,mask[i]].argmax(-1)==bf[i,mask[i]].argmax(-1)).float().mean())))
        rows=[r['prefix_ids'] for r in cases]
        x,mask=padded(rows,'cuda')
        pre=model(x,attention_mask=mask,use_cache=True)
        cache=pre.cache;logits=pre.logits[torch.arange(len(rows),device='cuda'),mask.sum(-1)-1]
        active=torch.ones(len(rows),device='cuda',dtype=torch.bool)
        generated=[dict(id=r['id'],source=r['source'],generated_ids=[],steps=[]) for r in cases]
        for step in range(64):
            ids=torch.zeros((len(rows),1),device='cuda',dtype=torch.long)
            for i,row in enumerate(generated):
                if not active[i]:continue
                chosen=choose(logits[i]);row['generated_ids'].append(chosen)
                row['steps'].append(distribution(logits[i],chosen));ids[i,0]=chosen
                if chosen==3:active[i]=False
            if not active.any() or step==63:break
            got=model(ids,attention_mask=active[:,None],cache=cache,use_cache=True)
            cache,logits=got.cache,got.logits[:,0]
        for row in generated:
            row.update(text=tok.decode(row['generated_ids'],errors='replace'),
                stop_reason='eos' if row['generated_ids'][-1]==3 else 'max_tokens',
                first_repeated_4gram=first_repeated_ngram(row['generated_ids']))
    return dict(endings=endings,fp32_greedy=generated)


def main():
    contract=read_json(OUT/'contract.json');job=read_json(OUT/'job.json')
    assert job['status']=='complete'
    assert implementation_hashes()==contract['implementation']
    assert job['gpu_job_seconds']+120<600
    assert not (OUT/'precision-job.json').exists()
    binding=dict(parent_contract_sha256=sha256(OUT/'contract.json'),source_sha256=sha256(Path(__file__)),
        cause='frozen numeric BF16/padding failures; determine probability/greedy impact, thresholds unchanged',
        parent_job_seconds=job['gpu_job_seconds'],max_seconds=120,total_gpu_cap=600,
        cases_sha256=sha256(OUT/'cases.json'),no_optimizer_updates=True,protected_test_used=False)
    atomic_json(OUT/'precision-contract.json',binding)
    tok=Tokenizer(TOK);cases=read_json(OUT/'cases.json');seed_all(42);torch.set_num_threads(2)
    start=time.monotonic();record=dict(status='running',identity=identity(),started_at=now(),binding=binding)
    atomic_json(OUT/'precision-job.json',record)
    try:
        with gpu_lock('cuda'):
            for name,entry in contract['checkpoints'].items():
                assert sha256(Path(entry['path']))==entry['sha256']
                state=torch.load(entry['path'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
                result=measure(model,cases,tok);result.update(checkpoint=entry,binding=binding)
                atomic_json(OUT/f'{name}-precision.json',result)
                print(f'{name} FP32/BF16 probability and FP32 greedy saved; {time.monotonic()-start:.1f}s',flush=True)
                del model;gc.collect();torch.cuda.empty_cache()
                if time.monotonic()-start>120:raise TimeoutError('Precision budget exhausted')
            record.update(status='complete',completed_at=now(),gpu_job_seconds=time.monotonic()-start,
                result_sha256={f'{n}-precision.json':sha256(OUT/f'{n}-precision.json') for n in contract['checkpoints']})
    except BaseException as error:
        record.update(status='failed',error=repr(error),gpu_job_seconds=time.monotonic()-start);raise
    finally:atomic_json(OUT/'precision-job.json',record)


if __name__=='__main__':main()
