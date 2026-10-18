"""Fresh process/lock/VRAM check for this new comparison only."""
from pathlib import Path
import chat_recovery_contract as contract
import inspect_answer_curriculum as previous
from answer_learning_common import save,ref,now


def main():
    conflicts=[]
    for p in Path('/proc').glob('[0-9]*/cmdline'):
        try:command=p.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,ProcessLookupError,PermissionError):continue
        if 'scripts/run_chat_recovery_sft.py run' in command:conflicts.append(dict(pid=int(p.parent.name),command=command))
    assert not conflicts,conflicts
    previous.CONFIG=contract.CONFIG;previous.RUN=contract.RUN;previous.preflight=contract.preflight
    previous.main()
    save(contract.RUN/'owned_launch_guard.json',dict(observed_at=now(),config=ref(contract.CONFIG),source=ref(__file__),
        additional_new_runner_conflicts=conflicts,underlying_observation=ref(contract.RUN/'launch_observation.json'),
        global_NVML_ownership_limit_preserved=True,new_GPU_updates=0))


if __name__=='__main__':main()
