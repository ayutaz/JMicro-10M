"""Observe actual environment/process/UI/lock state without starting GPU jobs."""
import json
import os
from pathlib import Path
import shutil
import sys
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, gpu_lock
from phase6_performance import alive, identity

RUN = ROOT / 'reports/phase7/chat-semantic-diversity-20261013'
PATTERNS = ('scripts/run_chat_', 'scripts/evaluate_chat_', 'scripts/run_eos_short_pilot.py',
            'scripts/chat_generalization_padding.py')


def inspect():
    assert sys.version_info[:3] == (3, 12, 7), sys.version
    conflicts = []
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:
            raw = path.read_bytes().split(b'\0')
        except (OSError, PermissionError):
            continue
        if int(path.parent.name) == os.getpid():
            continue
        # Match real argv entries, never a shell's quoted observer source.
        args = [part.decode(errors='replace') for part in raw if part]
        if any(any(arg.startswith(pattern) or ('/' + pattern) in arg for pattern in PATTERNS)
               for arg in args):
            conflicts.append(dict(pid=int(path.parent.name), argv=args))
    assert not conflicts, conflicts
    available = shutil.disk_usage(ROOT).free
    assert available >= 20 * 1024**3, 'Checkpoint reserve below20GiB'
    saved = read_json(ROOT / 'reports/local/webui/server.json')
    assert saved['status'] == 'running' and alive(saved), 'Reconcile actual UI before launch'
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=5) as response:
        model = json.load(response)
    assert model['checkpoint_sha256'] == '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    assert model['parameters'] == 10001152 and not model['busy']
    lock = read_json(Path.home() / 'jmicro-data/gpu.lock')
    kernel = [line.split() for line in Path('/proc/locks').read_text().splitlines()]
    inode = (Path.home() / 'jmicro-data/gpu.lock').stat().st_ino
    assert lock['pid'] == saved['pid']
    assert any('FLOCK' in row and 'WRITE' in row and str(saved['pid']) in row
               and any(part.endswith(':' + str(inode)) for part in row) for row in kernel)
    try:
        with gpu_lock('cuda'):
            raise AssertionError('Verified UI kernel lock unexpectedly available')
    except RuntimeError:
        pass
    result = dict(observed_at=now(), observer=identity(), free_bytes=available,
                  conflicts=conflicts, UI_identity={key: saved[key] for key in ('pid', 'boot_id', 'start_ticks')},
                  HTTP=model, kernel_GPU_lock_owner_verified=True,
                  frozen_model_source_sha256=sha256(ROOT / 'src/jmicro/model.py'),
                  dependencies_changed=False, GPU_training_launched=False)
    path = RUN / 'environment_observations' / ('observation-' + now().replace(':', '') + '.json')
    atomic_json(path, result)
    print(json.dumps(result, ensure_ascii=False))
    return result


if __name__ == '__main__':
    inspect()
