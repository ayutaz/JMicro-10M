"""Separate launch observation for NVML's observed empty process list.

Keep the frozen scientific config/runner/gate unchanged. An empty NVML list
does NOT prove sole GPU ownership. Require the real UI identity, direct dxg
handles, idle checkpoint API, kernel FLOCK, no project jobs and measured memory
headroom. Any actually reported foreign compute peer remains a rejection.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from chat_natural_contract import ROOT,RUN,CONFIG,preflight,require_ref,ref
from jmicro.experiment import read_json,now,sha256
from jmicro.training import atomic_json
from phase6_performance import identity,alive


def verify_resource_observation(peers,ui_pid,dxg_count,free_bytes,required_bytes):
    if any(peer!=ui_pid for peer in peers):
        raise ValueError('A reported foreign compute peer is present')
    if not dxg_count or free_bytes < required_bytes:
        raise ValueError('Direct GPU handle or measured memory headroom insufficient')
    return 'UI_reported_by_NVML' if peers else 'NVML_empty_ownership_not_established'


def main():
    c,_,_=preflight()
    amendment=read_json(RUN/'launch_observation_amendment.json')
    assert amendment['config']['sha256']==sha256(CONFIG)
    for value in amendment['new_sources'].values():require_ref(value)
    assert shutil.disk_usage(ROOT).free>=10*1024**3
    conflicts=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:cmd=path.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,PermissionError,ProcessLookupError):continue
        if path.parent.name==str(os.getpid()):continue
        if any(s in cmd for s in ('scripts/run_chat_natural.py','scripts/run_chat_lr.py','scripts/run_chat_first_sft.py',
            'scripts/run_chat_semantic.py','scripts/run_chat_generalization.py','scripts/run_chat_improvement.py','scripts/run_rdrop_science.py')):
            conflicts.append(dict(pid=int(path.parent.name),command=cmd))
    assert not conflicts,conflicts
    server=read_json(ROOT/'reports/local/webui/server.json')
    assert server['status']=='running' and alive(server)
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:ui=json.load(response)
    assert not ui['busy'] and ui['checkpoint_sha256']==c['parent']['sha256']
    lock=Path.home()/'jmicro-data/gpu.lock'
    assert read_json(lock)['pid']==server['pid']
    inode=lock.stat().st_ino
    assert any('FLOCK' in row and 'WRITE' in row and str(server['pid']) in row and
        any(p.endswith(':'+str(inode)) for p in row) for row in (line.split() for line in Path('/proc/locks').read_text().splitlines()))
    dxg=[]
    for fd in (Path('/proc')/str(server['pid'])/'fd').iterdir():
        try:target=os.readlink(fd)
        except FileNotFoundError:continue
        if target=='/dev/dxg':dxg.append(fd.name)
    command=['/usr/lib/wsl/lib/nvidia-smi']
    peers_raw=subprocess.run(command+['--query-compute-apps=pid,process_name,used_gpu_memory','--format=csv,noheader,nounits'],
        check=True,capture_output=True,text=True).stdout.strip()
    peers=[int(line.split(',')[0]) for line in peers_raw.splitlines() if line.strip()]
    memory_raw=subprocess.run(command+['--query-gpu=memory.total,memory.used','--format=csv,noheader,nounits'],
        check=True,capture_output=True,text=True).stdout.strip()
    total,used=map(int,memory_raw.split(','))
    gate=read_json(RUN/'native_gate.json')
    assert gate['passed'] and gate['config_sha256']==c['config_sha256']
    required=gate['arms']['C0']['maximum_shape']['peak_allocated_bytes']+2*1024**3
    status=verify_resource_observation(peers,server['pid'],len(dxg),(total-used)*1024**2,required)
    atomic_json(RUN/'launch_observations'/('observed-'+now().replace(':','')+'.json'),dict(observed_at=now(),
        observer=identity(),UI_identity={k:server[k] for k in ('pid','boot_id','start_ticks')},HTTP=ui,
        dxg_fds=dxg,actual_kernel_FLOCK_owner=server['pid'],NVML_compute_raw=peers_raw,
        NVML_status=status,sole_global_GPU_peer_proven=False,listed_peers_only_UI=bool(peers),memory_total_MiB=total,memory_used_MiB=used,
        measured_headroom_bytes=(total-used)*1024**2,required_bytes=required,conflicting_project_jobs=conflicts,
        scientific_config_unchanged=ref(CONFIG),amendment=ref(RUN/'launch_observation_amendment.json')))
    print('Original UI/identity/dxg/kernel lock/project processes/memory verified; NVML status: '+status,flush=True)


if __name__=='__main__':main()
