"""Same forgetting formula with the cancelling query-row constant removed.

softmax(scores+c_query-c_key)=softmax(scores-c_key), including derivatives.
FP32 operation order changes; bitwise reference training parity is NOT claimed.
Architecture, original weights, gates/initialization and all thresholds stay.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro import forgetting_attention as reference
from jmicro.model import ModelOutput, rope

TAG, ARMS, POLICY = reference.TAG, reference.ARMS, reference.POLICY
added_parameters = reference.added_parameters
RUNTIME_KEY = 'forgetting_attention_runtime'
IMPLEMENTATION = 'FP32_key_cumulative_bias_row_constant_removed_v1'


def tagged_config(native, arm='learned_forget'):
    if RUNTIME_KEY in native:
        raise ValueError('Already runtime-bound config cannot substitute for native')
    result = reference.tagged_config(native, arm)
    result[RUNTIME_KEY] = IMPLEMENTATION
    return result


def native_config(config):
    if config.get(RUNTIME_KEY) != IMPLEMENTATION:
        raise ValueError('Exact new key-bias runtime binding required')
    stripped = copy.deepcopy(config)
    del stripped[RUNTIME_KEY]
    native = reference.native_config(stripped)
    if tagged_config(native, config[TAG]['arm']) != config:
        raise ValueError('Exact architecture/runtime roundtrip required')
    return native


@dataclass
class KeyBiasKVCache(reference.ForgettingKVCache):
    implementation: str = IMPLEMENTATION


class KeyBiasAttention(reference.ForgettingAttention):
    def __init__(self, source):
        if type(source) is not reference.ForgettingAttention:
            raise ValueError('Explicit original forgetting reference attention required')
        nn.Module.__init__(self)
        for name in ('qheads', 'kvheads', 'dim', 'theta', 'scale', 'arm', 'q_proj',
                     'k_proj', 'v_proj', 'o_proj', 'q_norm', 'k_norm', 'forget_proj'):
            setattr(self, name, getattr(source, name))
        self.train(source.training)

    def forward(self, x, positions, allowed, past, causal=False, *, log_history=None,
                current_valid=None, return_history=False):
        batch, length, _ = x.shape
        if (past is None) != (log_history is None):
            raise ValueError('KV/log history must be paired')
        if current_valid is None:
            current_valid = (torch.ones((batch, length), device=x.device, dtype=torch.bool)
                             if causal else allowed.any(-1))
        if current_valid.shape != (batch, length) or current_valid.dtype != torch.bool:
            raise ValueError('Exact bool current validity required')
        def project(layer, heads):
            return layer(x).view(batch, length, heads, self.dim).transpose(1, 2)
        q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
        k = rope(self.k_norm(project(self.k_proj, self.kvheads)), positions, self.theta)
        v = project(self.v_proj, self.kvheads)
        gate_logits = self.forget_proj(x).float().transpose(1, 2)
        if self.arm == 'static_half_forget':
            gate_logits = gate_logits * 0.
        logs = torch.where(current_valid[:, None], F.logsigmoid(gate_logits), 0.)
        if past is not None:
            k, v = torch.cat((past[0], k), 2), torch.cat((past[1], v), 2)
            logs = torch.cat((log_history, logs), -1)
        # The omitted cumulative query term cancels in each valid softmax row.
        bias = -logs.cumsum(-1)[:, :, None, :]
        if causal:
            if past is not None or allowed is not None:
                raise ValueError('Causal path requires unmasked full prefix')
            allowed = torch.ones((length, length), device=x.device, dtype=torch.bool).tril()
        bias = bias.masked_fill(~allowed[:, None] if allowed.ndim == 3 else ~allowed, -torch.inf)
        groups = self.qheads // self.kvheads
        attended = F.scaled_dot_product_attention(q, k.repeat_interleave(groups, 1),
            v.repeat_interleave(groups, 1), attn_mask=bias, dropout_p=0.,
            is_causal=False, scale=self.scale)
        out = self.o_proj(attended.transpose(1, 2).reshape(batch, length, -1))
        return (out, (k, v), logs) if return_history else (out, (k, v))


class KeyBiasModel(reference.ForgettingModel):
    def __init__(self, config):
        native = native_config(config)
        source = reference.ForgettingModel(reference.tagged_config(native, config[TAG]['arm']))
        nn.Module.__init__(self)
        self._take_reference(source, config)

    def _take_reference(self, source, config):
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = source.model, source.lm_head
        for block in self.model.layers:
            block.self_attn = KeyBiasAttention(block.self_attn)
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Same architecture count/tie required')
        self.train(source.training)

    @classmethod
    def from_native(cls, original, arm='learned_forget'):
        source = reference.ForgettingModel.from_native(original, arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_reference(source, tagged_config(original.config, arm))
        return result

    def _validate_cache(self, cache, ids):
        if type(cache) is not KeyBiasKVCache or cache.implementation != IMPLEMENTATION:
            raise ValueError('Exact new-runtime KV cache required; no reference-cache migration')
        surrogate = reference.ForgettingKVCache(cache.layers, cache.valid, cache.positions,
                                                 cache.log_gates, cache.arm)
        super()._validate_cache(surrogate, ids)

    def forward(self, *args, **kwargs):
        output = super().forward(*args, **kwargs)
        if output.cache is not None:
            cache = output.cache
            return ModelOutput(output.logits, KeyBiasKVCache(cache.layers, cache.valid, cache.positions,
                                                              cache.log_gates, cache.arm), output.loss)
        return output
