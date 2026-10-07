"""Explicit mixture architecture in native likelihood, cached decode and generation."""
from contextlib import contextmanager
from pathlib import Path

import torch
from jmicro.experiment import read_json
from jmicro.training import atomic_json
from base_output_mixture_model import ARMS, POLICY, TAG, model_from_config
from base_output_mixture_trainer import KIND
import run_complete_text_comparison as native


def validate_record(arm,trained):
    config,spec = trained.get('model_config',{}),trained.get('spec',{})
    if (arm not in ARMS or trained.get('mixture_arm')!=arm or trained.get('mixture_policy')!=POLICY
            or trained.get('mixture_model_class')!='OutputMixtureModel'
            or config.get(TAG,{}).get('arm')!=arm
            or spec.get('kind')!=KIND or spec.get('mixture_arm')!=arm or spec.get('mixture_policy')!=POLICY):
        raise ValueError('Exact tagged mixture arm/policy/model class/record required')
    with torch.device('meta'):
        model = model_from_config(config)
    if sum(p.numel() for p in model.parameters())!=spec.get('actual_unique_parameters'):
        raise ValueError('Actual recorded mixture parameter count differs')


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
        if any(old.get(k)!=trained[k] for k in ('mixture_arm','mixture_policy','mixture_model_class')):
            raise ValueError('Refuse legacy or differently typed mixture evaluation')
    with typed_native_evaluation(run_root):
        result = native.evaluate(arm,trained,dev,tok,plan,binding,heartbeat,check,deadline)
    result = dict(result,mixture_arm=arm,mixture_policy=POLICY,mixture_model_class=trained['mixture_model_class'],
                  likelihood_cache_and_generation_use_same_mixture_model=True)
    atomic_json(terminal,result)
    return result
