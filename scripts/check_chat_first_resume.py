"""Separate real CUDA resume gate before the Base Chat control or learning."""
import argparse
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import signal
import shutil
import sys
import time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,sha256,read_json,now
from jmicro.training import atomic_json,gpu_lock
from run_chat_first_sft import preflight,resume_gate
from chat_first_contract import parent_state,RUN
from phase6_performance import identity,alive


def run(config):
    c,tok,records=preflight(config);c['config_sha256']=sha256(config)
    path=RUN/'resume-gate/job.json';old=read_json(path) if path.exists() else {}
    if old:
        assert old['config_sha256']==c['config_sha256'] and not alive(old)
        if old['status']=='complete':
            gate=read_json(path.parent/'result.json');assert gate['passed'];print('Completed CUDA resume gate retained');return
    driver_sha = sha256(Path(__file__))
    if old: assert old['driver_sha256'] == driver_sha
    path.parent.mkdir(parents=True,exist_ok=True)
    snapshot=path.parent/'check_chat_first_resume.py'
    if snapshot.exists(): assert sha256(snapshot)==driver_sha
    else: shutil.copyfile(__file__,snapshot)
    job=dict(status='starting',**identity(),config_sha256=c['config_sha256'],driver_sha256=driver_sha,
        started_at=now(),GPU_elapsed_seconds=old.get('GPU_elapsed_seconds',0.))
    atomic_json(path,job);prior=job['GPU_elapsed_seconds'];started=None;stop=[False]
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]: raise InterruptedError('Resume gate interrupted')
        if started is not None and prior+time.monotonic()-started>600: raise TimeoutError('600s cumulative resume gate budget exhausted')
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);parent=parent_state(c)
        with gpu_lock('cuda'):
            started=time.monotonic();job.update(status='running');atomic_json(path,job)
            gate=resume_gate(parent,c,tok,records,RUN,check);check()
            job.update(status='complete',completed_at=now());print('CUDA full-state resume gate:',gate['passed'],flush=True)
    except BaseException as error: job.update(status='failed',error=repr(error));raise
    finally:
        if started is not None:job['GPU_elapsed_seconds']=prior+time.monotonic()-started
        atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True);p.add_argument('--inspect',action='store_true');a=p.parse_args()
    if a.inspect:
        preflight(a.config.resolve());print('CPU preflight passed; CUDA gate not started')
    else: run(a.config.resolve())
