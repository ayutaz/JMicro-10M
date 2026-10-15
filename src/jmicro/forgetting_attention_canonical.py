"""Same tiled BF16 training with explicitly fixed-shape FP32 arithmetic.

Workspace padding is cropped/masked, never stored as tokens in a KV cache.
Only current decoder states are computed during incremental inference. This
tests shape-related rounding; it does not establish the old update6 cause.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro import forgetting_attention_fused as reference
from jmicro.model import ModelOutput, rope

TAG, ARMS, POLICY = reference.TAG, reference.ARMS, reference.POLICY
added_parameters = reference.added_parameters
RUNTIME_KEY = reference.RUNTIME_KEY
IMPLEMENTATION = 'same_tiled_BF16_canonical64_pointwise_Q64_Kcontext_MATH_FP32_v1'
BLOCK = 64
CANONICAL_POLICY = dict(pointwise_rows_per_sequence=64, attention_query_rows=64,
    key_workspace='max(original_context,real_physical_history)_rounded64',
    precision='FP32', backend='MATH', cache='real_KV_log_valid_positions_only',
    recompute_past_decoder_states=False, original_tiled_BF16_training_unchanged=True)


def tagged_config(native, arm='learned_forget'):
    result = reference.tagged_config(native, arm)
    result[RUNTIME_KEY] = IMPLEMENTATION
    return result


def native_config(config):
    if config.get(RUNTIME_KEY) != IMPLEMENTATION:
        raise ValueError('Explicit canonical arithmetic runtime required')
    old = copy.deepcopy(config)
    old[RUNTIME_KEY] = reference.IMPLEMENTATION
    native = reference.native_config(old)
    if tagged_config(native, config[TAG]['arm']) != config:
        raise ValueError('Exact canonical architecture/runtime roundtrip required')
    return native


def packed_pointwise(x, operation):
    """Same pointwise operation on real rows, with a fixed Bx64 work shape."""
    if x.ndim not in (2, 3) or x.shape[-2] == 0 or not x.is_floating_point():
        raise ValueError('Nonempty floating token/feature rows required')
    squeezed = x.ndim == 2
    source = x[None] if squeezed else x
    outputs = []
    for start in range(0, source.shape[1], BLOCK):
        part = source[:, start:start+BLOCK]
        n = part.shape[1]
        work = F.pad(part, (0, 0, 0, BLOCK-n)).contiguous()
        result = operation(work)
        if result.ndim != 3 or result.shape[:2] != work.shape[:2]:
            raise ValueError('Pointwise operation must preserve batch/workspace rows')
        outputs.append(result[:, :n])
    result = torch.cat(outputs, 1)
    return result[0] if squeezed else result


def canonical_attention(q, k, v, logs, allowed, minimum_keys, scale):
    batch, heads, length, dim = q.shape
    keys = k.shape[2]
    if (q.dtype != torch.float32 or k.dtype != q.dtype or v.dtype != q.dtype
            or k.shape != v.shape or k.shape[:2] != (batch, heads) or k.shape[-1] != dim
            or logs.shape != (batch, heads, keys) or logs.dtype != torch.float32
            or allowed.shape != (batch, length, keys) or allowed.dtype != torch.bool
            or type(minimum_keys) is not int or minimum_keys <= 0
            or length == 0 or keys == 0):
        raise ValueError('Exact FP32 QKV/logs, bool real-key mask and positive workspace required')
    width = ((max(minimum_keys, keys)+BLOCK-1)//BLOCK)*BLOCK
    pk = F.pad(k, (0, 0, 0, width-keys)).contiguous()
    pv = F.pad(v, (0, 0, 0, width-keys)).contiguous()
    cumulative = F.pad(logs, (0, width-keys)).contiguous().cumsum(-1)
    outputs = []
    for start in range(0, length, BLOCK):
        part = q[:, :, start:start+BLOCK]
        n = part.shape[2]
        pq = F.pad(part, (0, 0, 0, BLOCK-n)).contiguous()
        mask = F.pad(allowed[:, start:start+n], (0, width-keys, 0, BLOCK-n), value=False)
        bias = (-cumulative[:, :, None]).expand(batch, heads, BLOCK, width).masked_fill(~mask[:, None], -torch.inf)
        with sdpa_kernel(SDPBackend.MATH), torch.autocast(q.device.type, enabled=False):
            value = F.scaled_dot_product_attention(pq, pk, pv, attn_mask=bias,
                                                    dropout_p=0., is_causal=False, scale=scale)
        outputs.append(value[:, :, :n])
    return torch.cat(outputs, 2)


def fp32_path(x):
    return x.dtype == torch.float32 and not torch.is_autocast_enabled(x.device.type)


class CanonicalHead(nn.Linear):
    def __init__(self, source):
        nn.Module.__init__(self)
        self.in_features, self.out_features = source.in_features, source.out_features
        self.weight = source.weight
        self.register_parameter('bias', source.bias)

    def forward(self, x):
        operation = lambda value: F.linear(value, self.weight, self.bias)
        return packed_pointwise(x, operation) if fp32_path(x) else operation(x)


@dataclass
class CanonicalKVCache(reference.FusedKVCache):
    implementation: str = IMPLEMENTATION


class CanonicalAttention(reference.FusedForgettingAttention):
    def __init__(self, source, context):
        if type(source) is not reference.FusedForgettingAttention:
            raise ValueError('Exact original fused attention required')
        nn.Module.__init__(self)
        for name in ('qheads', 'kvheads', 'dim', 'theta', 'scale', 'arm', 'q_proj',
                     'k_proj', 'v_proj', 'o_proj', 'q_norm', 'k_norm', 'forget_proj'):
            setattr(self, name, getattr(source, name))
        self.canonical_context = context
        self.train(source.training)

    def forward(self, x, *args, **kwargs):
        if fp32_path(x):
            raise ValueError('FP32 decoding/training requires explicit model-owned canonical traversal')
        return super().forward(x, *args, **kwargs)

    def canonical_forward(self, x, positions, allowed, past, causal, log_history, current_valid):
        if not fp32_path(x) or (past is None) != (log_history is None):
            raise ValueError('FP32 canonical inputs and paired KV/log history required')
        batch, length, _ = x.shape
        def project(layer, heads):
            return packed_pointwise(x, layer).view(batch, length, heads, self.dim).transpose(1, 2)
        q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
        k = rope(self.k_norm(project(self.k_proj, self.kvheads)), positions, self.theta)
        v = project(self.v_proj, self.kvheads)
        logits = packed_pointwise(x, self.forget_proj).float().transpose(1, 2)
        if self.arm == 'static_half_forget':
            logits = logits*0.
        logs = torch.where(current_valid[:, None], F.logsigmoid(logits), 0.)
        if past is not None:
            k, v = torch.cat((past[0], k), 2), torch.cat((past[1], v), 2)
            logs = torch.cat((log_history, logs), -1)
        if causal:
            if past is not None or allowed is not None:
                raise ValueError('Canonical causal prefix cannot contain a cache/mask')
            allowed = torch.ones((batch, length, length), device=x.device, dtype=torch.bool).tril()
        groups = self.qheads//self.kvheads
        value = canonical_attention(q, k.repeat_interleave(groups, 1), v.repeat_interleave(groups, 1),
            logs, allowed, self.canonical_context, self.scale)
        out = packed_pointwise(value.transpose(1, 2).reshape(batch, length, -1), self.o_proj)
        return out, (k, v), logs


class CanonicalForgettingModel(reference.FusedForgettingModel):
    def __init__(self, config):
        native = native_config(config)
        source = reference.FusedForgettingModel(reference.tagged_config(native, config[TAG]['arm']))
        nn.Module.__init__(self)
        self._take_fused_source(source, config)

    def _take_fused_source(self, source, config):
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = source.model, CanonicalHead(source.lm_head)
        for block in self.model.layers:
            block.self_attn = CanonicalAttention(block.self_attn, config['max_position_embeddings'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Unchanged actual parameter count and vocabulary tie required')
        self.train(source.training)

    @classmethod
    def from_native(cls, original, arm='learned_forget'):
        source = reference.FusedForgettingModel.from_native(original, arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_fused_source(source, tagged_config(original.config, arm))
        return result

    def _blocks(self, ids, positions, allowed, valid, cache=None, causal=False):
        if (self.model.embed_tokens.weight.dtype != torch.float32
                or torch.is_autocast_enabled(ids.device.type)):
            return super()._blocks(ids, positions, allowed, valid, cache, causal)
        x, layers, histories = self.model.embed_tokens(ids), [], []
        for i, block in enumerate(self.model.layers):
            attention, kv, logs = block.self_attn.canonical_forward(
                packed_pointwise(x, block.input_layernorm), positions, allowed,
                None if cache is None else cache.layers[i], causal,
                None if cache is None else cache.log_gates[i], valid)
            x = x+attention
            x = x+packed_pointwise(packed_pointwise(x, block.post_attention_layernorm), block.mlp)
            layers.append(kv)
            histories.append(logs)
        return packed_pointwise(x, self.model.norm), layers, histories

    def _validate_cache(self, cache, ids):
        if type(cache) is not CanonicalKVCache or cache.implementation != IMPLEMENTATION:
            raise ValueError('Exact canonical-runtime real-token cache required')
        old = reference.FusedKVCache(cache.layers, cache.valid, cache.positions, cache.log_gates,
                                      cache.arm, reference.IMPLEMENTATION)
        super()._validate_cache(old, ids)

    def forward(self, *args, **kwargs):
        output = super().forward(*args, **kwargs)
        if output.cache is not None:
            c = output.cache
            return ModelOutput(output.logits, CanonicalKVCache(c.layers, c.valid, c.positions, c.log_gates, c.arm),
                               output.loss)
        return output
