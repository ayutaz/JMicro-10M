"""Observe the same live job and real kernel lock; never start or stop work."""
import json
from pathlib import Path
import subprocess
import time
from chat_recovery_contract import RUN,CONFIG,preflight
from answer_learning_common import read_json,ref,save,now
from phase6_performance import identity,alive


def main():
    c,_,_=preflight(False);job=read_json(RUN/'pipeline.json');live=alive(job)
    observation=dict(observed_at=now(),config=ref(CONFIG),job=job,actual_alive=live,all_frozen_sources_verified=True)
    if live:
        observation['actual_identity']=identity(job['pid'])
        lock=Path.home()/'jmicro-data/gpu.lock';inode=str(lock.stat().st_ino)
        observation['lock_payload']=read_json(lock)
        observation['actual_kernel_FLOCK']=[line for line in Path('/proc/locks').read_text().splitlines() if 'FLOCK' in line and 'WRITE' in line and line.split()[4]==str(job['pid']) and any(t.endswith(':'+inode) for t in line.split())]
        observation['NVML_compute_raw']=subprocess.run(['/usr/lib/wsl/lib/nvidia-smi','--query-compute-apps=pid,process_name,used_gpu_memory','--format=csv,noheader,nounits'],capture_output=True,text=True,check=True).stdout
        observation['sole_global_GPU_peer_proven']=False
    if (RUN/'GPU_ledger.json').exists():observation['ledger']=read_json(RUN/'GPU_ledger.json')
    if (RUN/'native_gate.json').exists():observation['gate']=ref(RUN/'native_gate.json')
    for arm in ('C0','C1'):
        path=RUN/arm/'job.json'
        if path.exists():observation[arm]=read_json(path)
        path=RUN/arm/'result.json'
        if path.exists():observation[arm+'_result']=read_json(path)
    path=RUN.parent/f'observation-{time.time_ns()}.json';save(path,observation)
    small=dict(path=str(path),live=live,identity=observation.get('actual_identity'),FLOCK=observation.get('actual_kernel_FLOCK'),job=job,
        stages=[dict(category=r['category'],status=r['status'],seconds=r['seconds'],update=r.get('update'),arm=r.get('arm')) for r in observation.get('ledger',{}).get('entries',[])],
        arms={a:observation.get(a,{}).get('status') for a in ('C0','C1')})
    print(json.dumps(small,ensure_ascii=False))


if __name__=='__main__':main()
