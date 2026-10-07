"""Run frozen native suites with an explicit sigsoftmax constructor and metadata."""
from contextlib import contextmanager
from pathlib import Path
from jmicro.experiment import read_json
from jmicro.training import atomic_json
from base_sigsoftmax_model import LINK, SigSoftmaxModel
import run_complete_text_comparison as native


@contextmanager
def typed_native_evaluation(run_root):
    previous_factory, previous_run = native.JMicroModel, native.RUN
    native.JMicroModel, native.RUN = SigSoftmaxModel, Path(run_root)
    try:
        yield
    finally:
        native.JMicroModel, native.RUN = previous_factory, previous_run


def evaluate(arm, trained, dev, tok, plan, binding, heartbeat, check, deadline, run_root):
    if (trained.get('output_probability_link') != LINK
            or trained.get('model_config', {}).get('output_probability_link') != LINK):
        raise ValueError('Explicit tagged sigsoftmax scientific record required')
    terminal = Path(run_root) / arm / 'evaluation/result.json'
    if terminal.exists() and read_json(terminal).get('output_probability_link') != LINK:
        raise ValueError('Refuse untagged ordinary-softmax evaluation reuse')
    with typed_native_evaluation(run_root):
        result = native.evaluate(arm, trained, dev, tok, plan, binding, heartbeat, check, deadline)
    result = dict(result, output_probability_link=LINK,
        likelihood='NLL_under_normalized_exp_raw_z_times_sigmoid_raw_z',
        linked_head_used_for_full_cache_generation_and_likelihood=True)
    atomic_json(terminal, result)
    return result
