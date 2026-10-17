"""Read actual scientific identity, stage and live lock; never restarts work."""
import json
from pathlib import Path
import subprocess
import time
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
from answer_learning_common import save,ref,read_json,now
from phase6_performance import identity,alive


def snapshot():
    path=RUN/'pipeline.json'
    if not path.exists():
        print('Pipeline identity not yet written; inspect actual Windows launcher/preflight, no restart');return
    job=read_json(path);current=alive(job)
    value=dict(observed_at=now(),job=job,actual_process_alive=current,config=ref(CONFIG))
    if current:
        value['actual_identity']=identity(job['pid'])
        value['actual_cmdline']=(Path('/proc')/str(job['pid'])/'cmdline').read_bytes().replace(b'\0',b' ').decode()
        assert 'scripts/run_answer_curriculum_resource_v2.py run' in value['actual_cmdline']
        value['all_frozen_sources_match']={p:contract.sha256(contract.ROOT/p)==h for p,h in read_json(CONFIG)['source_sha256'].items()}
        assert all(value['all_frozen_sources_match'].values())
        lock=Path.home()/'jmicro-data/gpu.lock'
        inode=str(lock.stat().st_ino)
        value['actual_kernel_FLOCK']=[line for line in Path('/proc/locks').read_text().splitlines() if 'FLOCK' in line and 'WRITE' in line
            and line.split()[4]==str(job['pid']) and any(t.endswith(':'+inode) for t in line.split())]
        value['NVML_compute_raw']=subprocess.run(['/usr/lib/wsl/lib/nvidia-smi','--query-compute-apps=pid,process_name,used_gpu_memory',
            '--format=csv,noheader,nounits'],capture_output=True,text=True,check=True).stdout.strip()
    if (RUN/'GPU_ledger.json').exists():value['ledger']=read_json(RUN/'GPU_ledger.json')
    value['arms']={}
    for arm in ('C0','C1'):
        p=RUN/arm/'job.json'
        if p.exists():value['arms'][arm]=read_json(p)
    if (RUN/'native_gate.json').exists():
        gate=read_json(RUN/'native_gate.json')
        value['gate']=dict(passed=gate['passed'],technical_updates=gate['technical_updates'],
            forecasts={k:v['forecast_training_seconds'] for k,v in gate['arms'].items()},evaluation=gate['evaluation_forecast_seconds'])
    save(RUN/f'observation-{time.time_ns()}.json',value)
    print(json.dumps(value,ensure_ascii=False))


if __name__=='__main__':snapshot()
