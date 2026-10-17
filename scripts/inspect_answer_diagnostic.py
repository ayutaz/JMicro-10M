"""Read real identities, kernel FLOCK and current VRAM before owned diagnosis."""
import json
import os
from pathlib import Path
import subprocess
from urllib.request import urlopen
from answer_diagnostic import inspect,CONFIG
from answer_learning_common import ROOT,RUN,ref,read_json,save,now
from phase6_performance import alive,identity


def main():
    c=inspect();server=read_json(ROOT/'reports/local/webui/server.json')
    assert server['status']=='running' and alive(server)
    with urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:api=json.load(response)
    assert api['checkpoint_sha256']==c['parent']['sha256'] and not api['busy']
    lock=Path.home()/'jmicro-data/gpu.lock';assert read_json(lock)['pid']==server['pid']
    inode=str(lock.stat().st_ino)
    locks=[line for line in Path('/proc/locks').read_text().splitlines() if 'FLOCK' in line and 'WRITE' in line
        and line.split()[4]==str(server['pid']) and any(t.endswith(':'+inode) for t in line.split())]
    assert len(locks)==1
    dxg=[]
    for fd in (Path('/proc')/str(server['pid'])/'fd').iterdir():
        try:
            if os.readlink(fd)=='/dev/dxg':dxg.append(fd.name)
        except FileNotFoundError:pass
    assert dxg
    conflicts=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:cmd=path.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,PermissionError,ProcessLookupError):continue
        if any(word in cmd for word in ('scripts/answer_diagnostic.py run','scripts/run_chat_natural.py',
            'scripts/run_chat_lr.py','scripts/run_chat_first_sft.py','scripts/run_chat_semantic.py',
            'scripts/run_chat_generalization.py','scripts/run_chat_improvement.py','scripts/run_rdrop_science.py')):
            conflicts.append(dict(pid=int(path.parent.name),command=cmd))
    assert not conflicts
    smi='/usr/lib/wsl/lib/nvidia-smi'
    peers=subprocess.run([smi,'--query-compute-apps=pid,process_name,used_gpu_memory','--format=csv,noheader,nounits'],
        capture_output=True,text=True,check=True).stdout.strip()
    assert all(int(line.split(',')[0])==server['pid'] for line in peers.splitlines() if line.strip())
    memory=subprocess.run([smi,'--query-gpu=memory.total,memory.used','--format=csv,noheader,nounits'],
        capture_output=True,text=True,check=True).stdout.strip()
    total,used=map(int,memory.split(','))
    assert (total-used)*1024**2>=16069554176+2*1024**3
    record=dict(observed_at=now(),config=ref(CONFIG),UI_identity=identity(server['pid']),HTTP=api,
        actual_kernel_FLOCK=locks,dxg_fds=dxg,NVML_compute_raw=peers,sole_global_GPU_peer_proven=False,
        NVML_status='UI_listed' if peers else 'empty_ownership_unknown',memory_total_MiB=total,memory_used_MiB=used,
        project_conflicts=conflicts,CPU_only_inspection=True)
    path=RUN/'diagnostic_launch_observation.json';assert not path.exists();save(path,record)
    print('Frozen diagnostic/Base identity/FLOCK/dxg/VRAM checked; NVML ownership status '+record['NVML_status'])


if __name__=='__main__':main()
