"""Explicit tiled BF16 training runtime; qualified math FP32 cache fallback.

Full-prefix CUDA training uses a pinned author kernel with FP32 log gates.
Masked/cached/FP32/CPU paths retain key-bias math. No bitwise MATH-versus-fused
update equivalence or local CUDA qualification follows from this adapter.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro import forgetting_attention_key_bias as reference
from jmicro.model import ModelOutput, rope

TAG, ARMS, POLICY = reference.TAG, reference.ARMS, reference.POLICY
added_parameters = reference.added_parameters
RUNTIME_KEY = reference.RUNTIME_KEY
IMPLEMENTATION = 'author_f920086a_tiled_BF16_FP32_log_gates_math_FP32_cache_v1'


def tagged_config(native, arm='learned_forget'):
    result = reference.tagged_config(native, arm)
    result[RUNTIME_KEY] = IMPLEMENTATION
    return result


def native_config(config):
    if config.get(RUNTIME_KEY) != IMPLEMENTATION:
        raise ValueError('Explicit pinned fused runtime required')
    previous = copy.deepcopy(config)
    previous[RUNTIME_KEY] = reference.IMPLEMENTATION
    native = reference.native_config(previous)
    if tagged_config(native, config[TAG]['arm']) != config:
        raise ValueError('Exact fused architecture/runtime roundtrip required')
    return native


def fused_path(device_type, dtype, causal, has_cache, has_mask):
    return (device_type == 'cuda' and dtype == torch.bfloat16 and causal
            and not has_cache and not has_mask)


def tiled_attention(q, k, v, log_gates, scale):
    if (any(not t.is_cuda or t.ndim != 4 or t.dtype != torch.bfloat16 for t in (q, k, v))
            or q.shape != k.shape or q.shape != v.shape or q.shape[-1] != 64
            or q.shape[2] == 0 or log_gates.shape != q.shape[:3]
            or log_gates.dtype != torch.float32 or log_gates.device != q.device
            or any(t.device != q.device for t in (k, v))):
        raise ValueError('Explicit same-head full-prefix CUDA BF16 QKV64 and FP32 gates required')
    from jmicro._vendor.forgetting_attention_core import forgetting_attention
    return forgetting_attention(q, k, v, log_gates, head_first=True, seq_start=None,
                                sm_scale=scale, adaptive_threshold=None)


@dataclass
class FusedKVCache(reference.KeyBiasKVCache):
    implementation: str = IMPLEMENTATION


class FusedForgettingAttention(reference.KeyBiasAttention):
    def __init__(self, source):
        if type(source) is not reference.KeyBiasAttention:
            raise ValueError('Explicit key-bias architecture source required')
        nn.Module.__init__(self)
        for name in ('qheads', 'kvheads', 'dim', 'theta', 'scale', 'arm', 'q_proj',
                     'k_proj', 'v_proj', 'o_proj', 'q_norm', 'k_norm', 'forget_proj'):
            setattr(self, name, getattr(source, name))
        self.train(source.training)

    def forward(self, x, positions, allowed, past, causal=False, **kwargs):
        dtype = (torch.get_autocast_dtype('cuda') if x.is_cuda and torch.is_autocast_enabled('cuda')
                 else x.dtype)
        if fused_path(x.device.type, dtype, causal, past is not None, allowed is not None):
            raise ValueError('CUDA BF16 training requires explicit model-owned fused traversal')
        return super().forward(x, positions, allowed, past, causal, **kwargs)

    def fused_full_prefix(self, x, positions):
        if (not x.is_cuda or not torch.is_autocast_enabled('cuda')
                or torch.get_autocast_dtype('cuda') != torch.bfloat16):
            raise ValueError('Explicit full-prefix CUDA BF16 autocast required')
        batch, length, _ = x.shape
        def project(layer, heads):
            return layer(x).view(batch, length, heads, self.dim).transpose(1, 2)
        q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
        k = rope(self.k_norm(project(self.k_proj, self.kvheads)), positions, self.theta)
        v = project(self.v_proj, self.kvheads)
        gate_logits = self.forget_proj(x).float().transpose(1, 2)
        if self.arm == 'static_half_forget':
            gate_logits = gate_logits * 0.
        logs = F.logsigmoid(gate_logits)
        groups = self.qheads // self.kvheads
        out = tiled_attention(q, k.repeat_interleave(groups, 1), v.repeat_interleave(groups, 1), logs, self.scale)
        return self.o_proj(out.transpose(1, 2).reshape(batch, length, -1))


class FusedForgettingModel(reference.KeyBiasModel):
    def __init__(self, config):
        native = native_config(config)
        source = reference.KeyBiasModel(reference.tagged_config(native, config[TAG]['arm']))
        nn.Module.__init__(self)
        self._take_key_source(source, config)

    def _take_key_source(self, source, config):
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = source.model, source.lm_head
        for block in self.model.layers:
            block.self_attn = FusedForgettingAttention(block.self_attn)
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Same actual architecture count/tie required')
        self.train(source.training)

    @classmethod
    def from_native(cls, original, arm='learned_forget'):
        source = reference.KeyBiasModel.from_native(original, arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_key_source(source, tagged_config(original.config, arm))
        return result

    def _blocks(self, ids, positions, allowed, valid, cache=None, causal=False):
        dtype = (torch.get_autocast_dtype('cuda') if ids.is_cuda and torch.is_autocast_enabled('cuda')
                 else None)
        if not fused_path(ids.device.type, dtype, causal, cache is not None, allowed is not None):
            return super()._blocks(ids, positions, allowed, valid, cache, causal)
        # Called only by the inherited full-unmasked right_padded_hidden path.
        # Causality protects valid states from the original right-padding slots.
        x = self.model.embed_tokens(ids)
        for block in self.model.layers:
            x = x + block.self_attn.fused_full_prefix(block.input_layernorm(x), positions)
            x = x + block.mlp(block.post_attention_layernorm(x))
        return self.model.norm(x), [], []

    def _validate_cache(self, cache, ids):
        if type(cache) is not FusedKVCache or cache.implementation != IMPLEMENTATION:
            raise ValueError('Exact fused-runtime inference cache required')
        previous = reference.KeyBiasKVCache(cache.layers, cache.valid, cache.positions,
                                             cache.log_gates, cache.arm, reference.IMPLEMENTATION)
        super()._validate_cache(previous, ids)

    def forward(self, *args, **kwargs):
        output = super().forward(*args, **kwargs)
        if output.cache is not None:
            c = output.cache
            return ModelOutput(output.logits, FusedKVCache(c.layers, c.valid, c.positions, c.log_gates, c.arm),
                               output.loss)
        return output
