"""Explicit residual architecture for likelihood, cached decode and generation."""
from contextlib import contextmanager
from pathlib import Path
import torch
from jmicro.experiment import read_json
from jmicro.training import atomic_json
from base_parallel_residual_model import ARMS,POLICY,TAG,model_from_config
from base_parallel_residual_trainer import KIND
import run_complete_text_comparison as native


def validate_record(arm,trained):
    config,spec=trained.get('model_config',{}),trained.get('spec',{})
    expected_class='ParallelResidualModel' if arm=='parallel' else 'JMicroModel'
    if (arm not in ARMS or trained.get('arm')!=arm or trained.get('residual_policy')!=POLICY
            or trained.get('residual_model_class')!=expected_class
            or spec.get('kind')!=KIND or spec.get('arm')!=arm
            or spec.get('residual_policy')!=POLICY or spec.get('model_class')!=expected_class
            or (TAG in config)!=(arm=='parallel')):
        raise ValueError('Exact fresh residual arm/policy/class required')
    with torch.device('meta'):
        model=model_from_config(config)
    if sum(p.numel() for p in model.parameters())!=spec.get('actual_unique_parameters'):
        raise ValueError('Actual residual parameter count differs')


@contextmanager
def typed_native_evaluation(run_root):
    previous_factory,previous_run=native.JMicroModel,native.RUN
    native.JMicroModel,native.RUN=model_from_config,Path(run_root)
    try:
        yield
    finally:
        native.JMicroModel,native.RUN=previous_factory,previous_run


def evaluate(arm,trained,dev,tok,plan,binding,heartbeat,check,deadline,run_root):
    validate_record(arm,trained)
    terminal=Path(run_root)/arm/'evaluation/result.json'
    if terminal.exists():
        old=read_json(terminal)
        if any(old.get(k)!=trained[k] for k in ('arm','residual_policy','residual_model_class')):
            raise ValueError('Refuse legacy or differently typed residual evaluation')
    with typed_native_evaluation(run_root):
        result=native.evaluate(arm,trained,dev,tok,plan,binding,heartbeat,check,deadline)
    result=dict(result,arm=arm,residual_policy=POLICY,residual_model_class=trained['residual_model_class'],
                likelihood_cache_and_generation_use_same_residual_model=True)
    atomic_json(terminal,result)
    return result
