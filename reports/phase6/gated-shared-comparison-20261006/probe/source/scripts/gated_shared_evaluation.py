"""Use the frozen evaluators with an explicit architecture factory, same suites.

Only the caller's evaluation-module factory is scoped here. Native core files,
Tokenizer, prompts, scoring, precision and decoding remain unchanged.
"""
from contextlib import contextmanager
from gated_shared_model import GatedSharedModel


@contextmanager
def architecture_factory(module):
    previous = module.JMicroModel
    module.JMicroModel = GatedSharedModel
    try:
        yield
    finally:
        module.JMicroModel = previous


def evaluate(module, *args, **kwargs):
    with architecture_factory(module):
        result = module.evaluate(*args, **kwargs)
    return result


def transfer_scores(module, *args, **kwargs):
    with architecture_factory(module):
        result = module.transfer_scores(*args, **kwargs)
    return result
