"""Tagged first-layer V shortcut; separate from the frozen native decoder.

An adaptation of value residual learning, not a ResFormer reproduction:
V_l' = V_l + alpha_l V_0 for l>0, alpha initialized to zero. Current-layer
Q/K/mask/RoPE/O and the sequential attention/MLP block order are unchanged.
The first values remain in the gradient graph. Caches contain mixed values,
so only NEW current-token values are mixed on a cached call.
"""
import copy

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, JMicroModel, KVCache, ModelOutput, rope

TAG = 'first_layer_value_residual_research'
ARMS = ('value_learned', 'static_identity')
POLICY = dict(kind='first_layer_value_additive_learned_scalar_v1',
    first_layer_unchanged=True, current_value_coefficient=1.,
    initial_alpha=0., coefficient='direct_signed_per_later_layer',
    first_value_detached=False, first_value='original_unrotated_pre_repeat_V0',
    cache='mixed_current_values_then_append_past', additional_projections=0)


def tagged_config(native, arm='value_learned'):
    if (arm not in ARMS or any(k.endswith('_research') or k in
            ('gated_shared_reuse', 'output_probability_link') for k in native)
            or native.get('qk_norm_type') != 'none'
            or native.get('num_attention_heads') != 4 or native.get('num_key_value_heads') != 2
            or type(native.get('num_hidden_layers')) is not int or native['num_hidden_layers'] < 2
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Original native NoQKNorm Q4/KV2 config/count and explicit arm required')
    result = copy.deepcopy(native)
    result[TAG] = dict(policy=copy.deepcopy(POLICY), arm=arm,
                       native_expected_parameter_count=native['expected_parameter_count'])
    result['expected_parameter_count'] += native['num_hidden_layers'] - 1
    return result


def native_config(config):
    tag = config.get(TAG)
    if (not isinstance(tag, dict)
            or set(tag) != {'policy', 'arm', 'native_expected_parameter_count'}
            or tag['policy'] != POLICY or tag['arm'] not in ARMS
            or type(tag['native_expected_parameter_count']) is not int):
        raise ValueError('Exact declared first-value policy, arm and native count required')
    original = copy.deepcopy(config)
    del original[TAG]
    original['expected_parameter_count'] = tag['native_expected_parameter_count']
    if tagged_config(original, tag['arm']) != config:
        raise ValueError('Declared original config/extra scalar count differs')
    return original


def mix_values(current, first, alpha, arm='value_learned'):
    if (current.ndim != 4 or current.shape != first.shape
            or current.device != first.device or current.dtype != first.dtype
            or alpha.shape != () or alpha.device != current.device or arm not in ARMS):
        raise ValueError('Aligned original current/first GQA values and scalar required')
    coefficient = alpha if arm == 'value_learned' else alpha * 0.
    return current + coefficient.to(current.dtype) * first


class ValueResidualAttention(Attention):
    def __init__(self, native, arm):
        if type(native) is not Attention or arm not in ARMS:
            raise ValueError('Frozen native attention and explicit arm required')
        nn.Module.__init__(self)
        self.qheads, self.kvheads = native.qheads, native.kvheads
        self.dim, self.theta, self.scale = native.dim, native.theta, native.scale
        self.q_proj, self.k_proj, self.v_proj = native.q_proj, native.k_proj, native.v_proj
        self.o_proj, self.q_norm, self.k_norm = native.o_proj, native.q_norm, native.k_norm
        self.value_alpha = nn.Parameter(torch.zeros((), device=self.q_proj.weight.device,
                                                    dtype=self.q_proj.weight.dtype))
        self.arm = arm
        self.train(native.training)

    def forward(self, x, positions, allowed, past, causal=False, *, first_values=None):
        if first_values is None:
            raise ValueError('Value-residual decoder traversal required; native helper would bypass shortcut')
        batch, length, _ = x.shape
        def project(layer, heads):
            return layer(x).view(batch, length, heads, self.dim).transpose(1, 2)
        q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
        k = rope(self.k_norm(project(self.k_proj, self.kvheads)), positions, self.theta)
        v = mix_values(project(self.v_proj, self.kvheads), first_values, self.value_alpha, self.arm)
        if past is not None:
            k, v = torch.cat((past[0], k), dim=2), torch.cat((past[1], v), dim=2)
        groups = self.qheads // self.kvheads
        attended = F.scaled_dot_product_attention(q, k.repeat_interleave(groups, dim=1),
            v.repeat_interleave(groups, dim=1), attn_mask=None if causal else allowed[:, None],
            dropout_p=0., is_causal=causal, scale=self.scale)
        return self.o_proj(attended.transpose(1, 2).reshape(batch, length, -1)), (k, v)


class ValueResidualModel(JMicroModel):
    def __init__(self, config):
        original = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(original, config)

    def _take_native(self, original, config):
        if sum(p.numel() for p in original.parameters()) != config[TAG]['native_expected_parameter_count']:
            raise ValueError('Actual original parameter count differs')
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = original.model, original.lm_head
        for block in self.model.layers[1:]:
            block.self_attn = ValueResidualAttention(block.self_attn, config[TAG]['arm'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Tagged parameter count/tied vocabulary differs')
        self.train(original.training)

    @classmethod
    def from_native(cls, original, arm='value_learned'):
        if (type(original) is not JMicroModel or any(p.grad is not None for p in original.parameters())
                or any(not torch.isfinite(p).all() for p in original.parameters() if not p.is_meta)):
            raise ValueError('Finite native instance without accumulated gradients required')
        config = tagged_config(original.config, arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(original), config)
        return result

    def _blocks(self, ids, positions, allowed, cache=None, causal=False):
        x, layers = self.model.embed_tokens(ids), []
        first = None
        for index, block in enumerate(self.model.layers):
            past = None if cache is None else cache.layers[index]
            if index == 0:
                x, kv = block(x, positions, allowed, past, causal)
                first = kv[1][:, :, -ids.shape[1]:]
            else:
                attention, kv = block.self_attn(block.input_layernorm(x), positions,
                    allowed, past, causal, first_values=first)
                x = x + attention
                x = x + block.mlp(block.post_attention_layernorm(x))
            layers.append(kv)
        return self.model.norm(x), layers

    def right_padded_hidden(self, ids):
        """Explicit training helper; valid right-padded positions match native CE."""
        if ids.ndim != 2 or not 0 < ids.shape[1] <= self.config['max_position_embeddings']:
            raise ValueError('Nonempty context-bounded IDs required')
        positions = torch.arange(ids.shape[1], device=ids.device)[None].expand(ids.shape[0], -1)
        return self._blocks(ids, positions, None, causal=True)[0]

    def clip_grad_norm(self, max_norm):
        # Technical identity control must preserve the original reduction list:
        # appending zero-gradient scalars can change FP32 norm rounding. The
        # scientific learned arm includes ALL original and extra coordinates.
        parameters = (p for n, p in self.named_parameters()
            if self.config[TAG]['arm'] != 'static_identity' or not n.endswith('.value_alpha'))
        return torch.nn.utils.clip_grad_norm_(list(parameters), max_norm)

    def forward(self, input_ids, attention_mask=None, cache=None, use_cache=False,
                labels=None, training_fast_path=False):
        if input_ids.ndim != 2 or input_ids.shape[1] == 0:
            raise ValueError('Expected nonempty [batch,tokens] IDs')
        if training_fast_path:
            if attention_mask is not None or cache is not None or use_cache or labels is not None:
                raise ValueError('Fast training requires unpadded blocks without cache/labels')
            return ModelOutput(self.lm_head(self.right_padded_hidden(input_ids)).float())
        valid = torch.ones_like(input_ids, dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError('Mask must match current IDs')
        if cache is not None:
            if (len(cache.layers) != len(self.model.layers) or cache.valid.shape[0] != input_ids.shape[0]
                    or cache.valid.device != input_ids.device):
                raise ValueError('Cache batch/layer/device mismatch')
            before = cache.valid.sum(-1)
        else:
            before = torch.zeros(input_ids.shape[0], device=input_ids.device, dtype=torch.long)
        positions = (before[:, None] + valid.long().cumsum(-1) - 1).clamp_min(0)
        if ((before + valid.sum(-1)) > self.config['max_position_embeddings']).any():
            raise ValueError('Context exceeded; reprefill required')
        key_valid = valid if cache is None else torch.cat((cache.valid, valid), dim=1)
        key_positions = positions if cache is None else torch.cat((cache.positions, positions), dim=1)
        allowed = valid[:, :, None] & key_valid[:, None, :] & (key_positions[:, None, :] <= positions[:, :, None])
        hidden, layers = self._blocks(input_ids, positions, allowed, cache)
        logits = self.lm_head(hidden).float() * valid[..., None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape or not labels[:, 1:].ne(-100).any():
                raise ValueError('Labels require supervised targets in a full current sequence')
            loss = F.cross_entropy(logits[:, :-1].reshape(-1, logits.shape[-1]),
                labels[:, 1:].reshape(-1), ignore_index=-100)
        return ModelOutput(logits, KVCache(layers, key_valid, key_positions) if use_cache else None, loss)

    def load_state_dict(self, state_dict, strict=True, assign=False):
        expected = self.state_dict()
        if (strict is not True or assign is not False or set(state_dict) != set(expected)
                or any(state_dict[k].shape != v.shape or state_dict[k].dtype != v.dtype
                       or not torch.isfinite(state_dict[k]).all() for k, v in expected.items())
                or not torch.equal(state_dict['lm_head.weight'], state_dict['model.embed_tokens.weight'])
                or (self.config[TAG]['arm'] == 'static_identity' and any(torch.count_nonzero(v)
                    for k, v in state_dict.items() if k.endswith('.value_alpha')))):
            raise ValueError('Exact finite tagged state/tie/static coefficients required before mutation')
        return super().load_state_dict(state_dict, strict=True)

    def hf_reference(self):
        raise ValueError('Explicit first-value residual inference adapter required')

    def save(self, directory):
        raise ValueError('Use typed full research checkpoints; portable export not implemented')

    @classmethod
    def load(cls, directory):
        raise ValueError('Native directory loading cannot substitute for tagged checkpoints')
