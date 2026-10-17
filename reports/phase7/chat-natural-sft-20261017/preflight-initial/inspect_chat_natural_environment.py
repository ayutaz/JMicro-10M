"""Verify current processes, original idle Base UI and its actual GPU lock."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.request
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from chat_natural_contract import ROOT, RUN
from jmicro.training import gpu_lock, atomic_json
from jmicro.experiment import read_json, now
from phase6_performance import identity, alive


def main():
    assert shutil.disk_usage(ROOT).free >= 10 * 1024**3
    conflicts=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:
            cmd=path.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,PermissionError,ProcessLookupError):
            continue
        if path.parent.name==str(os.getpid()):
            continue
        if any(s in cmd for s in ('scripts/run_chat_natural.py','scripts/run_chat_lr.py',
            'scripts/run_chat_first_sft.py','scripts/run_chat_semantic.py','scripts/run_chat_generalization.py',
            'scripts/run_chat_improvement.py','scripts/run_rdrop_science.py')):
            conflicts.append(dict(pid=int(path.parent.name),command=cmd))
    assert not conflicts,conflicts
    server=read_json(ROOT/'reports/local/webui/server.json')
    assert server['status']=='running' and alive(server)
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:
        ui=json.load(response)
    assert not ui['busy'] and ui['checkpoint_sha256']=='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    lock=Path.home()/'jmicro-data/gpu.lock'
    holder=read_json(lock)
    assert holder['pid']==server['pid']
    inode=lock.stat().st_ino
    assert any('FLOCK' in row and 'WRITE' in row and str(server['pid']) in row
        and any(p.endswith(':'+str(inode)) for p in row)
        for row in (line.split() for line in Path('/proc/locks').read_text().splitlines()))
    observed=subprocess.run(['/usr/lib/wsl/lib/nvidia-smi','--query-compute-apps=pid,process_name,used_gpu_memory',
        '--format=csv,noheader,nounits'],check=True,capture_output=True,text=True).stdout.strip()
    peers=[int(line.split(',')[0]) for line in observed.splitlines() if line.strip()]
    assert peers==[server['pid']],observed
    atomic_json(RUN/'launch_observations'/('launch-'+now().replace(':','')+'.json'),dict(observed_at=now(),
        observer=identity(),original_UI_identity={k:server[k] for k in ('pid','boot_id','start_ticks')},
        HTTP=ui,actual_kernel_FLOCK_owner=server['pid'],sole_GPU_peer=observed,
        free_bytes=shutil.disk_usage(ROOT).free,conflicts=conflicts,new_GPU_learning_updates=0))
    print('Current original UI/HTTP/kernel lock/sole GPU peer/process/capacity checks passed')


if __name__=='__main__':
    main()
