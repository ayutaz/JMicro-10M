"""Explicit gate architecture in native likelihood, cached decode and generation."""
from contextlib import contextmanager
from pathlib import Path

import torch
from jmicro.experiment import read_json
from jmicro.training import atomic_json
from base_headwise_gate_model import ARMS, POLICY, TAG, model_from_config
from base_headwise_gate_trainer import KIND
import run_complete_text_comparison as native


def validate_record(arm,trained):
    config,spec = trained.get('model_config',{}),trained.get('spec',{})
    if (arm not in ARMS or trained.get('gate_arm')!=arm or trained.get('gate_policy')!=POLICY
            or trained.get('gate_model_class')!='HeadwiseGateModel'
            or config.get(TAG,{}).get('arm')!=arm
            or spec.get('kind')!=KIND or spec.get('gate_arm')!=arm or spec.get('gate_policy')!=POLICY):
        raise ValueError('Exact tagged gate arm/policy/model class/record required')
    with torch.device('meta'):
        model = model_from_config(config)
    if sum(p.numel() for p in model.parameters())!=spec.get('actual_unique_parameters'):
        raise ValueError('Actual recorded gate parameter count differs')


@contextmanager
def typed_native_evaluation(run_root):
    previous_factory,previous_run = native.JMicroModel,native.RUN
    native.JMicroModel,native.RUN = model_from_config,Path(run_root)
    try:
        yield
    finally:
        native.JMicroModel,native.RUN = previous_factory,previous_run


def evaluate(arm,trained,dev,tok,plan,binding,heartbeat,check,deadline,run_root):
    validate_record(arm,trained)
    terminal = Path(run_root)/arm/'evaluation/result.json'
    if terminal.exists():
        old = read_json(terminal)
        if any(old.get(k)!=trained[k] for k in ('gate_arm','gate_policy','gate_model_class')):
            raise ValueError('Refuse legacy or differently typed gate evaluation')
    with typed_native_evaluation(run_root):
        result = native.evaluate(arm,trained,dev,tok,plan,binding,heartbeat,check,deadline)
    result = dict(result,gate_arm=arm,gate_policy=POLICY,gate_model_class=trained['gate_model_class'],
                  likelihood_cache_and_generation_use_same_gate_model=True)
    atomic_json(terminal,result)
    return result
