"""Verify actual terminal identities and restored Base, without generation/restart."""
import json
import os
from pathlib import Path
from urllib.request import urlopen
from answer_learning_common import ROOT,save,ref,read_json,now
from run_answer_curriculum_resource_v2 import CONFIG,RUN,contract
from phase6_performance import identity,alive


def main():
    target=RUN/'terminal_restoration_observation.json';assert not target.exists()
    c=read_json(CONFIG);job=read_json(RUN/'pipeline.json')
    assert job['status']=='complete_raw_pending_all_content_and_UI' and not alive(job)
    windows=read_json(RUN/'windows_terminal_observation.json')
    assert not windows['process_present'] and windows['launcher_result']['exit_code']==windows['launcher_result']['original_UI_restore_exit_code']==0
    assert all(contract.sha256(ROOT/p)==h for p,h in c['source_sha256'].items())
    servers={}
    for port,name in {7860:'webui',7861:'chat-webui',7862:'chat-natural-C1',7863:'chat-natural-C0',7864:'chat-answer-C1',7865:'chat-answer-C0'}.items():
        path=ROOT/f'reports/local/{name}/server.json';record=read_json(path);assert record['status']=='running' and alive(record)
        with urlopen(f'http://127.0.0.1:{port}/api/model',timeout=5) as response:api=json.load(response)
        assert api['parameters']==10001152 and not api['busy']
        if port==7860:assert api['checkpoint_sha256']==c['parent']['sha256']
        else:assert api['max_new_tokens']==32
        if port in (7864,7865):
            result=read_json(RUN/api['arm']/'result.json');assert api['checkpoint_sha256']==result['checkpoint']['sha256'] and api['config_sha256']==ref(CONFIG)['sha256']
        servers[str(port)]=dict(identity=identity(record['pid']),HTTP=api,record=ref(path))
    pid=servers['7860']['identity']['pid'];lock=Path.home()/'jmicro-data/gpu.lock';assert read_json(lock)['pid']==pid
    inode=str(lock.stat().st_ino)
    locks=[line for line in Path('/proc/locks').read_text().splitlines() if 'FLOCK' in line and 'WRITE' in line
        and line.split()[4]==str(pid) and any(part.endswith(':'+inode) for part in line.split())]
    assert len(locks)==1;dxg=[]
    for fd in (Path('/proc')/str(pid)/'fd').iterdir():
        try:
            if os.readlink(fd)=='/dev/dxg':dxg.append(fd.name)
        except FileNotFoundError:pass
    assert dxg
    ledger=read_json(RUN/'GPU_ledger.json');assert all(r['status']=='complete' for r in ledger['entries'][1:])
    save(target,dict(observed_at=now(),scientific_identity=job,scientific_process_alive=False,
        Windows=ref(RUN/'windows_terminal_observation.json'),servers=servers,actual_kernel_FLOCK=locks,Base_dxg_fds=dxg,
        all_frozen_scientific_sources_match=True,raw_outputs=2628,owned_main_GPU_stage_wall_seconds=ledger['total_seconds'],
        source=ref(__file__),new_generation_or_training=0,all_content_reviews_still_pending=True))
    print(json.dumps(dict(scientific_process_alive=False,Base_PID=pid,all6_UIs_alive=True,GPU_stage_wall=ledger['total_seconds'])))


if __name__=='__main__':main()
