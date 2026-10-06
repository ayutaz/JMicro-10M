import sys
from pathlib import Path
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_base_parent_baselines import metadata,parent_references


def test_actual_optimizer_lr_and_nested_cursor_are_not_nominal_peak():
    cursor=dict(seed=42,epoch=1,position=6,context=1024,blocks=100)
    s=dict(optimizer=dict(param_groups=[dict(lr=.00001)],state={0:dict(step=torch.tensor(320435.))}),
        model={'weight':torch.tensor(1.)},scheduler=dict(update=320435),rng={},
        sampler=dict(kind='mixture',position=15259,web=cursor),spec=dict(lr=.0001),
        update=320435,tokens=10500014080,supervised_tokens=10477786961,body_bytes=10,
        model_config={},shard_manifest_sha256='abc',implementation_sha256={})
    m=metadata(s)
    assert m['actual_optimizer_LRs']==[.00001] and m['saved_spec_peak_lr']==.0001
    assert m['block_sampler_cursors']==[dict(path='sampler/web',**cursor)]
    assert m['optimizer_step_range']==[320435.,320435.]


def test_quality_guard_reference_is_not_registered_training_parent():
    ref=dict(path='guard.pt',sha256='abc')
    c=dict(reference=dict(web=ref),arms=dict(x=dict(parent=ref)),parents=dict(root=ref))
    found=parent_references(c)
    assert len(found)==2
    assert {r['field'] for r in found}=={'config/arms/x/parent','config/parents/root'}
