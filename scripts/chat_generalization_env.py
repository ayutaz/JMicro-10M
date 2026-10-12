"""Record live, bounded prerequisites for the explicitly resumed plan133."""
import json
from pathlib import Path
import subprocess
import sys
import urllib.request
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, implementation_hashes
from phase6_performance import identity, alive

RUN = ROOT / "reports/phase7/chat-generalization-20261013"
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006')
PARENT = ROOT / 'reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt'
TOKENIZER = ROOT / 'artifacts/phase2/4096/tokenizer.model'

def main():
    assert sys.version_info[:3] == (3,12,7)
    expected = dict(parent='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290',
        tokenizer='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318',
        manifest='1ad9f04c0b7d43c4fc253c7cdc8057e9a09d7ef34b9073e53d972aeef278e0ee',
        train='4b062f827e5d33e178959720f927e42f6606ff6412cbe1ec46b6e8740b255d60',
        dev='6074afd2ca787615c83f83ff5e356bcac7cbe6d752947357639c2d54b10cef92')
    paths = dict(parent=PARENT,tokenizer=TOKENIZER,manifest=DATA/'manifest.json',train=DATA/'train.jsonl',dev=DATA/'dev.jsonl')
    actual = {k:sha256(p) for k,p in paths.items()}
    assert expected == actual
    server = read_json(ROOT/'reports/local/webui/server.json')
    assert server['status'] == 'running' and alive(server)
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:
        ui = json.load(response)
    assert ui['busy'] is False and ui['checkpoint_sha256'] == expected['parent'] and ui['parameters'] == 10001152
    processes = subprocess.run(['ps','-eo','pid,etimes,args'],capture_output=True,text=True,check=True).stdout
    suspicious = [line for line in processes.splitlines() if any(s in line for s in
        ('run_chat_first_sft.py','run_chat_improvement.py','evaluate_chat_improvement.py','run_chat_generalization.py','evaluate_chat_generalization.py','base_teacher_decay_trainer.py'))]
    assert not suspicious, suspicious
    gpu = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi','--query-gpu=name,memory.total,memory.used,utilization.gpu',
        '--format=csv,noheader'],capture_output=True,text=True,check=True).stdout.strip()
    stat = __import__('os').statvfs(DATA)
    result = dict(status='bounded_live_prerequisites_verified',created_at=now(),**identity(),
        files={k:dict(path=str(paths[k]),sha256=v) for k,v in actual.items()},implementation=implementation_hashes(),
        ui_observed=ui,ui_identity={k:server[k] for k in ('pid','boot_id','start_ticks')},
        GPU_observed=gpu,available_bytes=stat.f_bavail*stat.f_frsize,conflicting_processes=suspicious,
        Python_version=sys.version,new_training_tokens=0,protected_test_used=False,
        execution_authorization='User explicitly resumed four improvement items, first comparison plan133 stages1-4',
        experiment_GPU_budget_seconds=21600,Base_adopted=False,Chat_adopted=False)
    atomic_json(RUN/'prerequisites.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == '__main__': main()
