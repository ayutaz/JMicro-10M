"""Explicit cross-KV signed-map research variant; frozen native stays intact.

Inspired by map subtraction in Differential Transformer, not a reproduction.
Q/K/V/O shapes, original weights, masks and cache layout are retained. A map
from the other GQA group acts on the CURRENT group's values; subtracting the
other head output would be a different, readout-redundant operation.
"""
import copy

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, JMicroModel, rope

TAG = 'cross_GQA_signed_map_research'
ARMS = ('cross_learned', 'static_zero')
POLICY = dict(kind='cross_GQA_attention_map_signed_tanh_v1',
    head_mapping=[2, 3, 0, 1], input_query_heads=4, input_KV_heads=2,
    output='original_map_minus_tanh_scalar_times_other_group_map_on_current_values',
    coefficient_granularity='query_head_per_layer', initial_raw_coefficient=0.,
    extra_projection_parameters=0, new_head_norm=False, original_weight_rescaling=False,
    original_cache_layout=True)


def tagged_config(native, arm):
    if (arm not in ARMS or any(k.endswith('_research') or k in
            ('gated_shared_reuse', 'output_probability_link') for k in native)
            or native.get('qk_norm_type') != 'none'
            or native.get('num_attention_heads') != 4 or native.get('num_key_value_heads') != 2
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Explicit frozen native NoQKNorm Q4/KV2 config/count and arm required')
    result = copy.deepcopy(native)
    result[TAG] = dict(policy=copy.deepcopy(POLICY), arm=arm,
                       native_expected_parameter_count=native['expected_parameter_count'])
    result['expected_parameter_count'] += native['num_hidden_layers'] * 4
    return result


def native_config(config):
    tag = config.get(TAG)
    if (not isinstance(tag, dict)
            or set(tag) != {'policy', 'arm', 'native_expected_parameter_count'}
            or tag['policy'] != POLICY or tag['arm'] not in ARMS
            or type(tag['native_expected_parameter_count']) is not int):
        raise ValueError('Exact cross-group policy, arm and native count required')
    original = copy.deepcopy(config)
    del original[TAG]
    original['expected_parameter_count'] = tag['native_expected_parameter_count']
    if tagged_config(original, tag['arm']) != config:
        raise ValueError('Declared original config/extra coefficient count differs')
    return original


def cross_map_attention(q, k, v, raw, *, mask=None, causal=False, scale=None, arm='cross_learned'):
    """Already expanded Q4/K4/V4. Other map, ORIGINAL V, same mask/scale."""
    if (q.ndim != 4 or k.ndim != 4 or v.shape != k.shape or q.shape[:2] != k.shape[:2]
            or q.shape[1] != 4 or q.shape[-1] != k.shape[-1] or raw.shape != (4,)
            or q.device != k.device or q.device != v.device or q.device != raw.device
            or arm not in ARMS or (causal and mask is not None)):
        raise ValueError('Aligned explicit four-head cross-group attention required')
    original = F.scaled_dot_product_attention(q, k, v, attn_mask=mask,
        dropout_p=0., is_causal=causal, scale=scale)
    other_map_current_values = F.scaled_dot_product_attention(
        q.roll(2, dims=1), k.roll(2, dims=1), v, attn_mask=mask,
        dropout_p=0., is_causal=causal, scale=scale)
    strength = raw.tanh()
    if arm == 'static_zero':
        strength = strength * 0.
    return original - strength.to(original.dtype)[None, :, None, None] * other_map_current_values


class CrossGQAMapAttention(Attention):
    def __init__(self, native, arm):
        if type(native) is not Attention or arm not in ARMS or (native.qheads, native.kvheads) != (4, 2):
            raise ValueError('Original Q4/KV2 attention and explicit variant required')
        nn.Module.__init__(self)
        self.qheads, self.kvheads = native.qheads, native.kvheads
        self.dim, self.theta, self.scale = native.dim, native.theta, native.scale
        self.q_proj, self.k_proj, self.v_proj = native.q_proj, native.k_proj, native.v_proj
        self.o_proj, self.q_norm, self.k_norm = native.o_proj, native.q_norm, native.k_norm
        self.cross_raw = nn.Parameter(torch.zeros(4, device=self.q_proj.weight.device,
                                                  dtype=self.q_proj.weight.dtype))
        self.arm = arm
        self.train(native.training)

    def forward(self, x, positions, allowed, past, causal=False):
        batch, length, _ = x.shape
        def project(layer, heads):
            return layer(x).view(batch, length, heads, self.dim).transpose(1, 2)
        q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
        k = rope(self.k_norm(project(self.k_proj, self.kvheads)), positions, self.theta)
        v = project(self.v_proj, self.kvheads)
        if past is not None:
            k, v = torch.cat((past[0], k), dim=2), torch.cat((past[1], v), dim=2)
        attended = cross_map_attention(q, k.repeat_interleave(2, dim=1), v.repeat_interleave(2, dim=1),
            self.cross_raw, mask=None if causal else allowed[:, None], causal=causal,
            scale=self.scale, arm=self.arm)
        return self.o_proj(attended.transpose(1, 2).reshape(batch, length, -1)), (k, v)


class CrossGQAMapModel(JMicroModel):
    def __init__(self, config):
        original = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(original, config)

    def _take_native(self, original, config):
        if sum(p.numel() for p in original.parameters()) != config[TAG]['native_expected_parameter_count']:
            raise ValueError('Actual original parameter count differs from tagged declaration')
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = original.model, original.lm_head
        for block in self.model.layers:
            block.self_attn = CrossGQAMapAttention(block.self_attn, config[TAG]['arm'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Actual tagged parameter count/tied vocabulary differs')
        self.train(original.training)

    @classmethod
    def from_native(cls, original, arm='cross_learned'):
        if (type(original) is not JMicroModel or any(p.grad is not None for p in original.parameters())
                or any(not torch.isfinite(p).all() for p in original.parameters() if not p.is_meta)):
            raise ValueError('Finite frozen native instance without accumulated gradients required')
        config = tagged_config(original.config, arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(original), config)
        return result

    def load_state_dict(self, state_dict, strict=True, assign=False):
        expected = self.state_dict()
        if (strict is not True or set(state_dict) != set(expected)
                or any(state_dict[k].shape != v.shape or state_dict[k].dtype != v.dtype
                       or not torch.isfinite(state_dict[k]).all() for k, v in expected.items())
                or not torch.equal(state_dict['lm_head.weight'], state_dict['model.embed_tokens.weight'])
                or (self.config[TAG]['arm'] == 'static_zero'
                    and any(torch.count_nonzero(v) for k, v in state_dict.items() if k.endswith('.cross_raw')))):
            raise ValueError('Exact finite tagged state, vocabulary tie and static-zero coefficients required')
        return super().load_state_dict(state_dict, strict=True, assign=assign)

    def hf_reference(self):
        raise ValueError('Cross-GQA signed maps require their own explicit inference adapter')

    def save(self, directory):
        raise ValueError('Use typed full research checkpoints; portable export not implemented')

    @classmethod
    def load(cls, directory):
        raise ValueError('Native model-directory loading cannot substitute for a tagged checkpoint')
