"""Pre-learning forecast repair: account cold startup once per stage.

Keep the failed forecast, same worst-case counts, same 1.5 safety factor and
same hard budgets. Separately measure steady throughput and cold overhead.
This does not change TRAIN, native training sources or the decoding recipe.
"""
import gc
import json
import math
import os
from pathlib import Path
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.model import JMicroModel
from jmicro.training import atomic_json,seed_all
from jmicro.chat_evaluation import generate_reply
from chat_improvement_contract import RUN,preflight,load_parent,GPU_stage,reference,remaining
from evaluate_chat_improvement import load_cases,nll_windows,nll_batch


def main():
    config=ROOT/'configs/phase7/chat-improvement-20261012.json';c,tok,_=preflight(config)
    path=RUN/'evaluation_forecast.json';previous=read_json(path)
    assert previous['config_sha256']==c['config_sha256'] and not previous['passed']
    assert not (RUN/'C0/job.json').exists() and not (RUN/'C1/job.json').exists(),'Freeze revision before main learning'
    protocol_path=RUN/'forecast_method_revision.json'
    protocol=dict(frozen_before_measurement=now(),source=reference(Path(__file__)),config_sha256=c['config_sha256'],
        failed_forecast=reference(path),change='Separate cold startup from steady generation throughput; cold charged per invocation, not per token of every response',
        unchanged=dict(maximum_required_responses=4380,maximum_tokens=64,safety_factor=1.5,total_limit=21600,evaluation_limit=10800),
        frames='largest four provided prompts, worst-length own history; each steady frame measured twice after one cold warmup',
        NLL='one cold plus three steady fixed physical32x1024 batches; all2554 targets at7 checkpoints',
        startup_IO_cleanup_reserve_seconds=600,planned_maximum_model_invocations=21,quality_evidence=False)
    assert not protocol_path.exists(),'Measure only the already defined revision; retain interrupted evidence'
    atomic_json(protocol_path,protocol)
    old_path=RUN/'evaluation_forecast_failed_cold_per_response.json';assert not old_path.exists();path.replace(old_path)
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    raw=[];timings=[];nll_times=[]
    with GPU_stage('evaluation','separate_cold_and_steady_forecast',c['config_sha256']) as (left,heartbeat),sdpa_kernel(SDPBackend.MATH):
        state=load_parent(c);model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
        cases,contexts=load_cases(c['new_DEV']['path'],tok)
        selected=sorted(cases,key=lambda x:len(tok.chat_prompt(x['messages'],960)[0]),reverse=True)[:4]
        worst=max(contexts,key=lambda x:len(x['messages']))['messages']
        frames=[s['messages'] for s in selected]+[[dict(m) if m['role']=='user' else dict(role='assistant',content='あ'*64) for m in worst]]
        for label,ms in [('cold',frames[0])]+[(f'steady-{i}-{repeat}',ms) for i,ms in enumerate(frames) for repeat in (1,2)]:
            if left()<20:raise TimeoutError('Forecast revision budget reserve')
            started=time.monotonic();r=generate_reply(model,tok,ms,'cuda','bf16',64,True);torch.cuda.synchronize()
            timing=dict(label=label,seconds=time.monotonic()-started,tokens=r['generated_tokens'],prompt_tokens=r['prompt_tokens'])
            timing['seconds_per_token']=timing['seconds']/timing['tokens'];timings.append(timing)
            raw.append(dict(messages=ms,response=r,timing_only=True));heartbeat(stage='forecast-steady',completed=len(raw))
        windows=nll_windows(c,tok)
        for start in (0,0,112,224):
            started=time.monotonic();nll_batch(model,windows[start:start+32]);torch.cuda.synchronize();nll_times.append(time.monotonic()-started)
        rate=max(r['seconds_per_token'] for r in timings[1:])
        generation=rate*64*4380*1.5
        nll=max(nll_times[1:])*math.ceil(2554/32)*7*1.5
        cold=21*(max(0.,timings[0]['seconds']-rate*timings[0]['tokens'])+max(0.,nll_times[0]-max(nll_times[1:])))
        total=generation+nll+cold+600.
        report=dict(passed=total<=remaining_before,config_sha256=c['config_sha256'],method_revision=reference(protocol_path),
            previous_failed_forecast=reference(old_path),timings=timings,raw_timing_only=raw,NLL_batch_seconds=nll_times,
            conservative_generation_seconds=generation,conservative_NLL_seconds=nll,cold_overhead_seconds=cold,
            forecast_evaluation_seconds=total,limit_seconds=10800,remaining_at_stage_start=remaining_before,
            maximum_required_responses=4380,maximum_tokens_per_response=64,safety_factor=1.5,
            includes_all_greedy_savepoints_and_conditional_three_seed_sampling=True,quality_evidence=False,completed_at=now())
        del model;gc.collect();torch.cuda.empty_cache()
    atomic_json(path,report);assert report['passed'],'Complete evaluation still cannot fit; do not launch learning'
    print(json.dumps({k:report[k] for k in ('passed','forecast_evaluation_seconds','conservative_generation_seconds','conservative_NLL_seconds','cold_overhead_seconds')}))

if __name__=='__main__':
    remaining_before=remaining('evaluation')
    main()
