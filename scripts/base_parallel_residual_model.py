"""Equal-parameter independent Attention/FFN residuals; native code is frozen."""
import copy

import torch
from torch import nn
from jmicro.model import Block, JMicroModel

ARMS = ('sequential', 'parallel')
TAG = 'parallel_residual_research'
POLICY = dict(kind='same_input_attention_FFN_separate_native_RMSNorm_v1',
              formula='x+Attention(RMS1(x))+SwiGLU(RMS2(x))',
              norm_weights_tied=False, residual_gain=1., additional_parameters=0,
              physical_block_invocations=1, initialization='identical_fresh_native_matrices')
FOREIGN_TAGS = ('ffn_research', 'output_mixture_research', 'attention_gate_research',
                'gated_shared_reuse', 'output_probability_link')


def parallel_config(native):
    if (TAG in native or any(key in native for key in FOREIGN_TAGS)
            or native.get('activation') != 'swiglu'
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Ordinary counted native SwiGLU configuration required')
    result = copy.deepcopy(native)
    result[TAG] = dict(policy=copy.deepcopy(POLICY))
    return result


def native_config(config):
    native = copy.deepcopy(config)
    tag = native.pop(TAG, None)
    if tag != dict(policy=POLICY) or parallel_config(native) != config:
        raise ValueError('Exact tagged parallel residual policy required')
    return native


class ParallelResidualBlock(nn.Module):
    def __init__(self, original):
        super().__init__()
        if type(original) is not Block:
            raise ValueError('Ordinary native block required')
        # Keep original registration order, matrices and optimizer ordering.
        self.self_attn = original.self_attn
        self.mlp = original.mlp
        self.input_layernorm = original.input_layernorm
        self.post_attention_layernorm = original.post_attention_layernorm

    def forward(self, x, positions, allowed, past, causal=False):
        attention, cache = self.self_attn(self.input_layernorm(x), positions, allowed, past, causal)
        feed_forward = self.mlp(self.post_attention_layernorm(x))
        return (x + attention) + feed_forward, cache


class ParallelResidualModel(JMicroModel):
    def __init__(self, config):
        scaffold = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_scaffold(scaffold, config)

    def _take_scaffold(self, scaffold, config):
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = scaffold.model, scaffold.lm_head
        self.model.layers = nn.ModuleList(ParallelResidualBlock(block) for block in self.model.layers)
        self.train(scaffold.training)

    @classmethod
    def from_native_fresh(cls, scaffold):
        # The fresh trainer must construct this scaffold before any update.
        # Matrix values alone cannot authenticate training provenance.
        if type(scaffold) is not JMicroModel or any(p.grad is not None for p in scaffold.parameters()):
            raise ValueError('Untouched fresh native scaffold required')
        config = parallel_config(scaffold.config)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_scaffold(scaffold, config)
        return result

    def hf_reference(self):
        raise ValueError('Parallel residual research model needs a dedicated reference adapter')

    def save(self, directory):
        raise ValueError('Store tagged research checkpoints; deployment adapter is deferred')


def model_from_config(config):
    if any(key in config for key in FOREIGN_TAGS):
        raise ValueError('Unrelated research architecture refused')
    return ParallelResidualModel(config) if TAG in config else JMicroModel(config)
