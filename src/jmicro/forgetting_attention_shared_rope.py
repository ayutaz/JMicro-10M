"""Original BF16 operations with RoPE constants shared within one invocation.

No cross-invocation table cache or learned/buffer state is introduced. FP32,
masked and real-cache inference retain the canonical implementation. A new
explicit runtime prevents silently substituting older caches/checkpoints.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro import forgetting_attention_canonical as reference
from jmicro import forgetting_attention_fused as tiled
from jmicro.forgetting_attention_rope_tables import original_rope_tables, apply_original_rope_tables
from jmicro.model import ModelOutput

TAG, ARMS, POLICY = reference.TAG, reference.ARMS, reference.POLICY
RUNTIME_KEY, CANONICAL_POLICY = reference.RUNTIME_KEY, reference.CANONICAL_POLICY
added_parameters = reference.added_parameters
IMPLEMENTATION = 'same_tiled_BF16_shared_original_RoPE_canonical64_FP32_v1'
ROPE_POLICY = dict(kind='original_RoPE_constant_tables_once_per_full_prefix_v1',
    scope='one_model_invocation', source='original_positions_dim_theta_dtype',
    arithmetic='same_inv_phase_cat_cos_sin_cast_then_original_rotation_mul_add',
    new_parameters=0, new_buffers=0, inference='unchanged_canonical_FP32_real_cache')


def tagged_config(native, arm='learned_forget'):
    c = reference.tagged_config(native, arm)
    c[RUNTIME_KEY] = IMPLEMENTATION
    return c


def native_config(config):
    if config.get(RUNTIME_KEY) != IMPLEMENTATION:
        raise ValueError('Explicit shared-original-RoPE runtime required')
    c = copy.deepcopy(config)
    c[RUNTIME_KEY] = reference.IMPLEMENTATION
    original = reference.native_config(c)
    if tagged_config(original, config[TAG]['arm']) != config:
        raise ValueError('Exact declared shared-RoPE runtime roundtrip required')
    return original


@dataclass
class SharedRopeKVCache(reference.CanonicalKVCache):
    implementation: str = IMPLEMENTATION


class SharedRopeAttention(reference.CanonicalAttention):
    def __init__(self, source):
        if type(source) is not reference.CanonicalAttention:
            raise ValueError('Exact canonical source attention required')
        nn.Module.__init__(self)
        for name in ('qheads', 'kvheads', 'dim', 'theta', 'scale', 'arm', 'q_proj',
                     'k_proj', 'v_proj', 'o_proj', 'q_norm', 'k_norm', 'forget_proj', 'canonical_context'):
            setattr(self, name, getattr(source, name))
        self.train(source.training)

    def shared_full_prefix(self, x, positions, tables):
        if (not x.is_cuda or not torch.is_autocast_enabled('cuda')
                or torch.get_autocast_dtype('cuda') != torch.bfloat16):
            raise ValueError('Explicit original full-prefix CUDA BF16 traversal required')
        batch, length, _ = x.shape
        if positions.shape != (batch, length):
            raise ValueError('Original current full-prefix positions required')
        def project(layer, heads):
            return layer(x).view(batch, length, heads, self.dim).transpose(1, 2)
        q = apply_original_rope_tables(self.q_norm(project(self.q_proj, self.qheads)), tables)
        k = apply_original_rope_tables(self.k_norm(project(self.k_proj, self.kvheads)), tables)
        v = project(self.v_proj, self.kvheads)
        gate_logits = self.forget_proj(x).float().transpose(1, 2)
        if self.arm == 'static_half_forget':
            gate_logits = gate_logits*0.
        logs = F.logsigmoid(gate_logits)
        groups = self.qheads//self.kvheads
        value = tiled.tiled_attention(q, k.repeat_interleave(groups, 1),
            v.repeat_interleave(groups, 1), logs, self.scale)
        return self.o_proj(value.transpose(1, 2).reshape(batch, length, -1))


class SharedRopeForgettingModel(reference.CanonicalForgettingModel):
    def __init__(self, config):
        original = native_config(config)
        source = reference.CanonicalForgettingModel(reference.tagged_config(original, config[TAG]['arm']))
        nn.Module.__init__(self)
        self._take_canonical(source, config)

    def _take_canonical(self, source, config):
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = source.model, source.lm_head
        for block in self.model.layers:
            block.self_attn = SharedRopeAttention(block.self_attn)
        dimensions = {(b.self_attn.dim, b.self_attn.theta) for b in self.model.layers}
        if (len(dimensions) != 1 or sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Common original RoPE geometry, unchanged count and tie required')
        self.train(source.training)

    @classmethod
    def from_native(cls, original, arm='learned_forget'):
        source = reference.CanonicalForgettingModel.from_native(original, arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_canonical(source, tagged_config(original.config, arm))
        return result

    def _blocks(self, ids, positions, allowed, valid, cache=None, causal=False):
        dtype = (torch.get_autocast_dtype('cuda') if ids.is_cuda and torch.is_autocast_enabled('cuda')
                 else None)
        if not tiled.fused_path(ids.device.type, dtype, causal, cache is not None, allowed is not None):
            return super()._blocks(ids, positions, allowed, valid, cache, causal)
        first = self.model.layers[0].self_attn
        tables = original_rope_tables(positions, first.dim, first.theta, torch.bfloat16)
        x = self.model.embed_tokens(ids)
        for block in self.model.layers:
            x = x+block.self_attn.shared_full_prefix(block.input_layernorm(x), positions, tables)
            x = x+block.mlp(block.post_attention_layernorm(x))
        return self.model.norm(x), [], []

    def _validate_cache(self, cache, ids):
        if type(cache) is not SharedRopeKVCache or cache.implementation != IMPLEMENTATION:
            raise ValueError('Exact shared-RoPE runtime real cache required')
        previous = reference.CanonicalKVCache(cache.layers, cache.valid, cache.positions,
                                              cache.log_gates, cache.arm, reference.IMPLEMENTATION)
        super()._validate_cache(previous, ids)

    def forward(self, *args, **kwargs):
        output = super().forward(*args, **kwargs)
        if output.cache is not None:
            c = output.cache
            return ModelOutput(output.logits, SharedRopeKVCache(c.layers, c.valid, c.positions,
                                                               c.log_gates, c.arm), output.loss)
        return output
