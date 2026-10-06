"""GPU entrypoint imports must preserve the caller's CUDA visibility."""
import os
from pathlib import Path
import subprocess
import sys
import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from probe_readout_adapter import memory_inputs,ROOT


def test_gpu_probe_import_does_not_run_CPU_preparation_side_effects():
    root=Path(__file__).resolve().parents[1]
    code="import os,sys; before=os.environ.get('CUDA_VISIBLE_DEVICES'); sys.path.insert(0,'scripts'); import probe_readout_adapter; assert os.environ.get('CUDA_VISIBLE_DEVICES')==before"
    for visibility in (None,'0'):
        env=os.environ.copy()
        if visibility is None:env.pop('CUDA_VISIBLE_DEVICES',None)
        else:env['CUDA_VISIBLE_DEVICES']=visibility
        # sys.executable is the pinned interpreter inherited from uv pytest.
        subprocess.run([sys.executable,'-c',code],cwd=root,env=env,check=True)


def test_actual_preserved_TRAIN_memory_schema_and_rejection():
    memory=torch.load(ROOT/'reports/phase6/finite-Web-constraint-20261006/memory.pt',map_location='cpu',weights_only=False)
    x=memory_inputs(memory)
    assert x.shape==(1,1024) and torch.equal(x,memory['x'][:1])
    for bad in ({'inputs':memory['x'],'targets':memory['y']},dict(x=memory['x'][:1],y=memory['y']),dict(x=memory['x'].float(),y=memory['y'])):
        with pytest.raises(ValueError):memory_inputs(bad)
