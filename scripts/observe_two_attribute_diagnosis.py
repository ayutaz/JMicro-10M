"""Actual identity/FLOCK/HTTP observation; never launches or stops a process."""
import argparse
import json
import os
from pathlib import Path
from urllib.request import urlopen
from two_attribute_contract import ROOT,RUN,CONFIG,preflight
from answer_learning_common import save,ref,read_json,now
from phase6_performance import identity,alive

def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['live','terminal']);a=p.parse_args();c,_,_=preflight();job=read_json(RUN/'pipeline.json')
    observation=dict(observed_at=now(),config=ref(CONFIG),pipeline=ref(RUN/'pipeline.json'),saved_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},actual_alive=alive(job),source=ref(__file__))
    lock=Path.home()/'jmicro-data/gpu.lock';inode=str(lock.stat().st_ino)
    pid=job['pid'] if a.mode=='live' else read_json(ROOT/'reports/local/webui/server.json')['pid']
    actual=identity(pid);locks=[line for line in Path('/proc/locks').read_text().splitlines() if 'FLOCK' in line and 'WRITE' in line and line.split()[4]==str(pid) and any(t.endswith(':'+inode) for t in line.split())]
    dxg=[]
    for fd in Path(f'/proc/{pid}/fd').iterdir():
        try:
            if os.readlink(fd)=='/dev/dxg':dxg.append(fd.name)
        except FileNotFoundError:pass
    assert len(locks)==1 and dxg
    observation.update(actual_identity=actual,kernel_FLOCK=locks,dxg_fds=dxg,GPU_ledger=ref(RUN/'GPU_ledger.json'))
    if a.mode=='live':assert observation['actual_alive'] and actual==observation['saved_identity']
    else:
        assert not observation['actual_alive'] and job['status']=='complete_raw_pending_review'
        server=read_json(ROOT/'reports/local/webui/server.json');assert alive(server)
        with urlopen('http://127.0.0.1:7860/api/model',timeout=5) as r:api=json.load(r)
        assert api['checkpoint_sha256']==c['parent']['sha256'] and not api['busy']
        observation.update(restored_UI=api,restored_server=server)
    target=RUN/f'{a.mode}_observation.json';assert not target.exists();save(target,observation);print(json.dumps(observation,ensure_ascii=False))

if __name__=='__main__':main()
