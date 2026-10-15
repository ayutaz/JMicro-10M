"""No data/GPU: exact scope, independent event totals, no double counting."""
import copy
from pathlib import Path
import sys
from types import SimpleNamespace as Row

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from profile_forgetting_attention_ops import assert_scope, summarize, IMPLEMENTATION


def contract():
    return dict(kind='owned_single_saved6_operator_profile_no_optimizer_v1',
        checkpoint_update=6, input_shape=[48,1024], labels_per_row=512, profiled_steps=1,
        warmup_steps=0, optimizer_updates=0, scientific_teacher_positions=0,
        dtype='BF16', attention_implementation=IMPLEMENTATION, new_GPU_ceiling_seconds=30,
        prior_technical_GPU_seconds=70.04953129705973, original_technical_cap_seconds=180,
        original_total_GPU_cap_seconds=4800, new_TRAIN_stream_opened=False,
        DEV_opened=False, TEST_opened=False, model_weights_saved=False, science_forecast=False)


def test_original_single_profile_scope_cannot_be_learning_retiming_or_budget_reset():
    assert_scope(contract())
    for key, value in (('optimizer_updates',1), ('profiled_steps',2), ('warmup_steps',1),
        ('checkpoint_update',38), ('input_shape',[48,512]), ('labels_per_row',128),
        ('new_TRAIN_stream_opened',True), ('DEV_opened',True), ('TEST_opened',True),
        ('model_weights_saved',True), ('science_forecast',True), ('dtype','FP32'),
        ('prior_technical_GPU_seconds',0.), ('original_technical_cap_seconds',181),
        ('original_total_GPU_cap_seconds',4801), ('new_GPU_ceiling_seconds',31)):
        c = contract()
        c[key] = value
        with pytest.raises(ValueError): assert_scope(c)


def kernel(name, duration, device='DeviceType.CUDA'):
    return Row(name=name, device_type=device, time_range=Row(elapsed_us=lambda: duration))


def operator(name, cpu, inclusive_device):
    return Row(key=name,count=2,self_cpu_time_total=cpu,cpu_time_total=cpu+10,
        self_device_time_total=inclusive_device/2,device_time_total=inclusive_device,input_shapes=[[2,3]])


def test_separate_kernel_and_operator_totals_overlap_is_not_double_counted():
    result = summarize([kernel('matmul',3.), kernel('matmul',4.),kernel('rotate',2.),
        kernel('CPU event',900.,'DeviceType.CPU')], [operator('parent',10.,9.),operator('child',2.,7.)])
    assert result['CUDA_event_count'] == 3 and result['CUDA_event_duration_sum_us'] == 9.
    assert result['CPU_operator_self_sum_us'] == 12.
    assert result['CUDA_events'] == [dict(name='matmul',count=2,total_us=7.),dict(name='rotate',count=1,total_us=2.)]


@pytest.mark.parametrize('events', [[], [kernel('CPU only',1.,'DeviceType.CPU')]])
def test_missing_actual_CUDA_activity_cannot_imply_device_timing(events):
    with pytest.raises(ValueError): summarize(events,[operator('op',1.,10.)])


def test_nonfinite_or_impossible_kernel_duration_refused():
    for value in (-1.,float('nan'),float('inf')):
        with pytest.raises(ValueError): summarize([kernel('bad',value)],[operator('op',1.,1.)])


def test_raw_negative_CPU_self_measurement_preserved_not_silently_clamped():
    r=summarize([kernel('k',1.)],[operator('profiler raw negative',-.1,1.)])
    assert r['CPU_negative_self_time_rows'] == 1 and r['CPU_operator_self_sum_us'] == -.1
