"""Current launch observations, not stored PID assumptions; no GPU work."""
from pathlib import Path
import json
import os
import shutil
import sys
import urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json
from jmicro.training import gpu_lock,atomic_json
from phase6_performance import alive,identity
from chat_improvement_contract import RUN,ledger


def main():
    ledger();free=shutil.disk_usage(ROOT).free;assert free>=20*1024**3,'Less than 20GiB checkpoint reserve'
    conflicts=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:cmd=path.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,PermissionError,ProcessLookupError):continue
        if int(path.parent.name)==os.getpid():continue
        if any(s in cmd for s in ('scripts/run_chat_improvement.py','scripts/evaluate_chat_improvement.py','scripts/run_chat_first_sft.py','scripts/run_eos_short_pilot.py')):
            # uv parent and Python child both signal a conflicting active job.
            conflicts.append(dict(pid=int(path.parent.name),command=cmd))
    assert not conflicts,conflicts
    ui_path=ROOT/'reports/local/webui/server.json';ui=None
    if ui_path.exists():
        saved=read_json(ui_path)
        if saved['status']=='running':
            assert alive(saved),'Saved running UI identity is stale; reconcile before launch'
            with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:ui=json.load(response)
            assert not ui['busy'] and ui['checkpoint_sha256']=='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            ui=dict(saved_identity={k:saved[k] for k in ('pid','boot_id','start_ticks')},HTTP=ui)
    lock_available=True;lock_holder=None
    try:
        with gpu_lock('cuda'):pass
    except RuntimeError:
        lock_available=False
        assert ui is not None,'A GPU lock is held without the verified idle original UI'
        lock_path=Path.home()/'jmicro-data/gpu.lock';lock_holder=read_json(lock_path)
        assert lock_holder['pid']==ui['saved_identity']['pid'],'A different process holds the GPU lock'
        inode=lock_path.stat().st_ino
        actual_locks=[line.split() for line in Path('/proc/locks').read_text().splitlines()]
        assert any('FLOCK' in row and 'WRITE' in row and str(lock_holder['pid']) in row
            and any(part.endswith(':'+str(inode)) for part in row) for row in actual_locks),'Kernel lock owner differs from UI'
    path=RUN/'launch_observations'/('launch-'+now().replace(':','').replace('+','_')+'.json')
    atomic_json(path,dict(observed_at=now(),observer=identity(),free_bytes=free,UI=ui,conflicts=conflicts,
        shared_GPU_lock_available=lock_available,verified_idle_UI_lock_holder=lock_holder))
    print('Current process/UI/lock/capacity launch gate passed')

if __name__=='__main__':main()
