"""Use the correct fresh FFN architecture in every frozen native evaluation."""
from contextlib import contextmanager
from pathlib import Path

from jmicro.experiment import read_json
from jmicro.training import atomic_json
from base_relu_squared_model import POLICY, model_from_config
from base_relu_squared_trainer import ARMS
import run_complete_text_comparison as native


def validate_record(arm, trained):
    config = trained.get('model_config', {})
    if (arm not in ARMS or trained.get('ffn_variant') != arm or trained.get('ffn_policy') != POLICY
            or ('ffn_research' in config) != (arm == 'ReLU_squared')):
        raise ValueError('Explicit matching FFN arm/policy/model_config required')
    # Validate architecture without allocating actual model weights.
    import torch
    with torch.device('meta'):
        model = model_from_config(config)
    if trained.get('FFN_model_class') != type(model).__name__:
        raise ValueError('Explicit actual FFN model class required')


@contextmanager
def typed_native_evaluation(run_root):
    previous_factory, previous_run = native.JMicroModel, native.RUN
    native.JMicroModel, native.RUN = model_from_config, Path(run_root)
    try:
        yield
    finally:
        native.JMicroModel, native.RUN = previous_factory, previous_run


def evaluate(arm, trained, dev, tok, plan, binding, heartbeat, check, deadline, run_root):
    validate_record(arm, trained)
    terminal = Path(run_root) / arm / 'evaluation/result.json'
    if terminal.exists():
        old = read_json(terminal)
        if any(old.get(k) != trained[k] for k in ('ffn_variant', 'ffn_policy', 'FFN_model_class')):
            raise ValueError('Refuse legacy or wrong FFN terminal evaluation')
    with typed_native_evaluation(run_root):
        result = native.evaluate(arm, trained, dev, tok, plan, binding, heartbeat, check, deadline)
    result = dict(result, ffn_variant=arm, ffn_policy=POLICY,
                  FFN_model_class=trained['FFN_model_class'],
                  native_likelihood_cache_and_greedy_use_same_FFN=True)
    atomic_json(terminal, result)
    return result
