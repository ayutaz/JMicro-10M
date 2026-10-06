import sys
from pathlib import Path
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts'),str(Path(__file__).resolve().parents[1]/'src')]
import run_historical_parent_condition_comparison_v2 as study


def test_nominal_peak_and_later_stage_or_longer_budget_are_refused():
    c=dict(failed_probe_GPU_seconds=study.read_json(study.PROPOSAL)['failed_probe_GPU_seconds'],research_kind=study.KIND,arms={study.ARM:study.GOALS},outcome_weights={study.ARM:1},
        teachers_per_new_arm=100000000,total_comparison_teachers=200000000,total_new_GPU_ceiling_seconds=900,
        peak_lr=.00001,optimizer_policy='inherit',shapes=dict(context=1024,batch=32,accumulation=1,
        backend='flash',compile_mode='reduce-overhead',dtype='bf16'),loss='ordinary original body+EOS CE, outcome weight1',
        Base_adopted=False,Chat_adopted=False,quantization_started=False,protected_test_used=False,
        requested_five_steps_complete=False,quality_criteria_unchanged=True)
    study.scope(c)
    for key,value in (('peak_lr',.0001),('peak_lr',.0002),('teachers_per_new_arm',500000000),
                      ('protected_test_used',True),('quality_criteria_unchanged',False)):
        with pytest.raises(ValueError):study.scope({**c,key:value})


def test_cpu_alignment_preserves_values_dtypes_shapes_and_nested_metadata():
    import torch
    original={'model':torch.tensor([[1.,2.]],dtype=torch.bfloat16),'state':[torch.tensor(7),('clock',3)]}
    result=study.cpu_state(original)
    assert study.equal_state(original,result)
    assert result['model'].dtype==torch.bfloat16 and result['model'].shape==(1,2)
    assert result['state'][0].dtype==torch.int64 and result['state'][1]==('clock',3)
