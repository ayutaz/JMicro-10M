"""Read-only scope and original cache-subcheck interpretation, CPU only."""
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest
import torch

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from diagnose_forgetting_fused_cache_cuda import assert_scope, observations


def contract():
    return dict(kind='owned_readonly_saved_fused3_FP32_cache_observation_v1',
        read_only=True, checkpoint_update=3, input_shape=[2,64], cache_split=[32,32],
        dtype='FP32', backend='MATH', absolute_tolerance=3e-5, relative_tolerance=2e-5,
        new_GPU_ceiling_seconds=30, original_technical_cap_seconds=180,
        original_total_GPU_cap_seconds=4800, prior_technical_GPU_seconds=12.881095835007727,
        optimizer_updates=0, scientific_teacher_positions=0, TEST_opened=False,
        recreate_failed_update6=False)


def pair():
    def cache():
        return SimpleNamespace(log_gates=[torch.zeros(1,4,4)], positions=torch.arange(4)[None],
            valid=torch.ones(1,4,dtype=torch.bool), layers=[(torch.zeros(1,2,4,64), torch.zeros(1,2,4,64))])
    return (SimpleNamespace(logits=torch.zeros(1,4,10), cache=cache()),
            SimpleNamespace(logits=torch.zeros(1,2,10), cache=cache()))


def test_exact_scope_and_no_rebinding():
    assert_scope(contract())
    for key, value in (('read_only',False), ('checkpoint_update',6), ('optimizer_updates',1),
        ('scientific_teacher_positions',1), ('TEST_opened',True), ('recreate_failed_update6',True),
        ('prior_technical_GPU_seconds',0), ('new_GPU_ceiling_seconds',31),
        ('original_technical_cap_seconds',181), ('original_total_GPU_cap_seconds',4801),
        ('absolute_tolerance',1e-3), ('relative_tolerance',1e-3), ('dtype','BF16'), ('backend','FLASH')):
        c=contract()
        c[key]=value
        with pytest.raises(ValueError): assert_scope(c)


def test_original_combined_precision_and_exact_outside_values():
    a,b=pair()
    assert observations(a,b,True)['all_original_guards_passed']
    b.logits[0,0,0]=4e-5
    result=observations(a,b,True)
    assert not result['original_guard_subchecks']['logits_within_original_tolerance']
    assert result['outside_original_logit_tolerance']==1
    row=result['first_eight_outside_logits'][0]
    assert row['index']==[0,0,0] and row['absolute_difference']>row['allowed_error_using_cached_reference']
    a.logits[:,-2:]=10
    b.logits[:]=10.0001
    assert observations(a,b,True)['all_original_guards_passed']


def test_RNG_metadata_and_log_history_are_independent_original_guards():
    a,b=pair()
    result=observations(a,b,False)
    assert not result['all_original_guards_passed'] and not result['original_guard_subchecks']['RNG_unchanged']
    b.cache.log_gates[0][0,0,0]=.1
    assert not observations(a,b,True)['original_guard_subchecks']['log_gate_history_within_original_tolerance']
    b.cache.positions[0,0]=99
    assert not observations(a,b,True)['original_guard_subchecks']['positions_exact']


def test_descriptive_KV_is_not_silently_an_additional_gate_and_bad_examples_bounded():
    a,b=pair()
    b.cache.layers[0][0][0,0,0,0]=.1
    assert observations(a,b,True)['all_original_guards_passed']
    b.logits[:]=1
    result=observations(a,b,True)
    assert result['outside_original_logit_tolerance']==20
    assert len(result['first_eight_outside_logits'])==8
