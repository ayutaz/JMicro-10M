"""Own launch guard reusing the original actual process/HTTP/FLOCK/dxg checks."""
from pathlib import Path
import inspect_answer_curriculum as previous
from two_attribute_contract import CONFIG,RUN,preflight
from answer_learning_common import save,ref,now

def main():
    conflicts=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:command=path.read_bytes().replace(b'\0',b' ').decode(errors='replace')
        except (FileNotFoundError,ProcessLookupError,PermissionError):continue
        if any(needle in command for needle in ('scripts/run_two_attribute_diagnosis.py run','scripts/run_chat_recovery_sft.py run')):
            conflicts.append(dict(pid=int(path.parent.name),command=command))
    assert not conflicts,conflicts
    previous.CONFIG=CONFIG;previous.RUN=RUN;previous.preflight=lambda **_:preflight();previous.main()
    save(RUN/'owned_launch_guard.json',dict(observed_at=now(),config=ref(CONFIG),source=ref(__file__),additional_conflicts=conflicts))

if __name__=='__main__':main()
