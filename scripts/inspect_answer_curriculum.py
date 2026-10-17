"""Fresh original Base identity, kernel lock, conflicts and VRAM before launch."""
import json
import os
from pathlib import Path
import subprocess
from urllib.request import urlopen
from answer_curriculum_contract import ROOT,RUN,CONFIG,preflight
from answer_learning_common import save,ref,read_json,now
from phase6_performance import identity,alive


def main():
    c,_,_=preflight(load_records=False)
    server=read_json(ROOT/'reports/local/webui/server.json')
    assert server['status']=='running' and alive(server)
    with urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:api=json.load(response)
    assert api['checkpoint_sha256']==c['parent']['sha256'] and not api['busy']
    lock=Path.home()/'jmicro-data/gpu.lock';assert read_json(lock)['pid']==server['pid'];inode=str(lock.stat().st_ino)
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
    needles=('scripts/run_answer_curriculum.py run','scripts/answer_diagnostic.py run','scripts/answer_diagnostic_manifest_v2.py run',
        'scripts/run_chat_natural.py --mode','scripts/run_chat_lr.py','scripts/run_chat_first_sft.py','scripts/run_chat_semantic.py',
        'scripts/run_chat_generalization.py','scripts/run_chat_improvement.py','scripts/run_rdrop_science.py')
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:command=path.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,ProcessLookupError,PermissionError):continue
        if any(needle in command for needle in needles):conflicts.append(dict(pid=int(path.parent.name),command=command))
    assert not conflicts,conflicts
    smi='/usr/lib/wsl/lib/nvidia-smi'
    peers=subprocess.run([smi,'--query-compute-apps=pid,process_name,used_gpu_memory','--format=csv,noheader,nounits'],capture_output=True,text=True,check=True).stdout.strip()
    assert all(int(line.split(',')[0])==server['pid'] for line in peers.splitlines() if line.strip())
    memory=subprocess.run([smi,'--query-gpu=memory.total,memory.used','--format=csv,noheader,nounits'],capture_output=True,text=True,check=True).stdout.strip()
    total,used=map(int,memory.split(','));assert (total-used)*1024**2>=16069554176+2*1024**3
    target=RUN/'launch_observation.json';assert not target.exists()
    save(target,dict(observed_at=now(),config=ref(CONFIG),UI_identity=identity(server['pid']),HTTP=api,actual_kernel_FLOCK=locks,
        dxg_fds=dxg,NVML_compute_raw=peers,NVML_status='UI_listed' if peers else 'empty_ownership_unknown',
        sole_global_GPU_peer_proven=False,memory_total_MiB=total,memory_used_MiB=used,project_conflicts=conflicts,
        CPU_only_observation=True))
    print('Original Base PID/start/boot, idle HTTP, actual FLOCK/dxg, conflicts and current VRAM verified')


if __name__=='__main__':main()
