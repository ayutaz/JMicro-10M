"""GPU entrypoint imports must preserve the caller's CUDA visibility."""
import os
from pathlib import Path
import subprocess
import sys


def test_gpu_probe_import_does_not_run_CPU_preparation_side_effects():
    root=Path(__file__).resolve().parents[1]
    code="import os,sys; before=os.environ.get('CUDA_VISIBLE_DEVICES'); sys.path.insert(0,'scripts'); import probe_readout_adapter; assert os.environ.get('CUDA_VISIBLE_DEVICES')==before"
    for visibility in (None,'0'):
        env=os.environ.copy()
        if visibility is None:env.pop('CUDA_VISIBLE_DEVICES',None)
        else:env['CUDA_VISIBLE_DEVICES']=visibility
        # sys.executable is the pinned interpreter inherited from uv pytest.
        subprocess.run([sys.executable,'-c',code],cwd=root,env=env,check=True)
