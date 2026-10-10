"""Bounded local diagnostic chat; raw failures retained, original UI untouched."""
import argparse
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import signal
import sys
import time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,now,sha256
from jmicro.model import JMicroModel
from jmicro.chat_evaluation import generate_reply
from jmicro.training import atomic_json,gpu_lock,seed_all
from chat_first_contract import RUN,resolve_diagnostic
from phase6_performance import identity,alive


def run(a):
    state,tok,provenance=resolve_diagnostic(a.config,a.stage)
    directory=(ROOT/a.output).resolve();assert directory.is_relative_to(ROOT/'reports/phase7')
    directory.mkdir(parents=True,exist_ok=True);job_path=directory/'job.json'
    if job_path.exists(): raise FileExistsError('Preserve earlier chat; choose a distinct diagnostic output')
    assert 0<a.gpu_budget_seconds<=600 and 1<=a.max_replies<=20
    cases=None
    if a.cases:
        cases=read_json(a.cases)['conversations']
        assert len(cases)==5 and sum(len(c['users']) for c in cases)<=20
        assert all(1<=len(c['users'])<=4 for c in cases)
    job=dict(status='starting',**identity(),started_at=now(),GPU_elapsed_seconds=0.,binding=provenance,
        purpose='local_chat_diagnostic',Chat_adopted=False,source_sha256=sha256(Path(__file__)))
    atomic_json(job_path,job);started=None;stop=[False];rows=[]
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError('Diagnostic chat interrupted')
        if started is not None and time.monotonic()-started>a.gpu_budget_seconds:raise TimeoutError('Diagnostic chat budget exhausted')
    try:
        torch.set_num_threads(2);seed_all(42);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'),sdpa_kernel(SDPBackend.MATH):
            started=time.monotonic();model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model'],strict=True)
            def reply(history,user):
                check();assert len(rows)<a.max_replies
                history.append(dict(role='user',content=user))
                raw=generate_reply(model,tok,history,'cuda','bf16',64,True,check)
                rows.append(dict(messages=list(history),response=raw));atomic_json(directory/'raw.json',dict(binding=provenance,outputs=rows))
                history.append(dict(role='assistant',content=raw['text']))
                print(raw['text'],flush=True)
                print('stop='+raw['stop_reason']+' valid_utf8='+str(raw['valid_utf8'])+' repetition='+str(raw['repetition']),flush=True)
            if cases:
                for case in cases:
                    history=[]
                    for user in case['users']:reply(history,user)
            else:
                print('Unadopted research Chat. /new clears history; /quit exits. At most20 replies.',flush=True);history=[]
                while len(rows)<a.max_replies:
                    check()
                    try:user=input('User> ')
                    except EOFError:break
                    if user=='/quit':break
                    if user=='/new':history=[];continue
                    if user.strip():reply(history,user)
            check();job.update(status='complete',completed_at=now(),responses=len(rows))
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if started is not None:job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(job_path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,default=ROOT/'configs/phase7/chat_first_sft.json')
    p.add_argument('--stage',choices=('epoch1','epoch2','epoch3'),default='epoch3');p.add_argument('--output',type=Path,required=True)
    p.add_argument('--cases',type=Path);p.add_argument('--max-replies',type=int,default=20);p.add_argument('--gpu-budget-seconds',type=float,default=600.)
    run(p.parse_args())
