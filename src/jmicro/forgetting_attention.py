"""Explicit matched-conversion cumulative attention decay research model.

Both arms start at f=.5; neither is the native parent's inference function.
Native tensors, including O, stay unchanged. This retains RoPE and NoQKNorm;
it is not a full FoX/Pro reproduction or a CUDA-performance implementation.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, JMicroModel, KVCache, ModelOutput, rope

TAG = 'forgetting_attention_research'
ARMS = ('learned_forget', 'static_half_forget')
POLICY = dict(kind='headwise_cumulative_log_sigmoid_pre_softmax_v1',
              input='native_pre_attention_RMSNorm', initial_weight=0., initial_bias=0.,
              initial_forget=.5, precision='FP32_log_gate_and_cumulative_bias',
              padding='invalid_slots_log_gate0_and_masked_keys',
              cache='typed_full_physical_log_gate_history', original_RoPE=True,
              original_O_unchanged=True, native_initial_function_preserved=False)


def added_parameters(c):
    return c['num_hidden_layers'] * c['num_attention_heads'] * (c['hidden_size'] + 1)


def tagged_config(native, arm='learned_forget'):
    if (arm not in ARMS or any(k.endswith('_research') or k in
            ('gated_shared_reuse', 'output_probability_link') for k in native)
            or native.get('qk_norm_type') != 'none'
            or native.get('num_attention_heads') != 4 or native.get('num_key_value_heads') != 2
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Explicit ordinary NoQKNorm Q4/KV2 config/count and arm required')
    result = copy.deepcopy(native)
    result[TAG] = dict(policy=copy.deepcopy(POLICY), arm=arm,
                       native_expected_parameter_count=native['expected_parameter_count'])
    result['expected_parameter_count'] += added_parameters(native)
    return result


def native_config(tagged):
    tag = tagged.get(TAG)
    if (not isinstance(tag, dict) or set(tag) != {'policy', 'arm', 'native_expected_parameter_count'}
            or tag['policy'] != POLICY or tag['arm'] not in ARMS
            or type(tag['native_expected_parameter_count']) is not int):
        raise ValueError('Exact declared forgetting policy/count/arm required')
    result = copy.deepcopy(tagged)
    del result[TAG]
    result['expected_parameter_count'] = tag['native_expected_parameter_count']
    if tagged_config(result, tag['arm']) != tagged:
        raise ValueError('Tagged architecture count differs')
    return result


@dataclass
class ForgettingKVCache(KVCache):
    log_gates: list[torch.Tensor]
    arm: str


class ForgettingAttention(Attention):
    def __init__(self, native, arm):
        if type(native) is not Attention or arm not in ARMS:
            raise ValueError('Original attention and explicit forgetting arm required')
        nn.Module.__init__(self)
        self.qheads, self.kvheads = native.qheads, native.kvheads
        self.dim, self.theta, self.scale = native.dim, native.theta, native.scale
        self.q_proj, self.k_proj, self.v_proj = native.q_proj, native.k_proj, native.v_proj
        self.o_proj, self.q_norm, self.k_norm = native.o_proj, native.q_norm, native.k_norm
        self.arm = arm
        with torch.random.fork_rng(devices=[]):
            gate = nn.Linear(self.q_proj.in_features, self.qheads, bias=True)
            nn.init.zeros_(gate.weight)
            nn.init.zeros_(gate.bias)
        self.forget_proj = gate.to(device=self.q_proj.weight.device, dtype=self.q_proj.weight.dtype)
        self.train(native.training)

    def forward(self, x, positions, allowed, past, causal=False, *, log_history=None,
                current_valid=None, return_history=False):
        batch, length, _ = x.shape
        if (past is None) != (log_history is None):
            raise ValueError('KV and log gate history must be paired')
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
        cumulative = logs.cumsum(-1)
        bias = cumulative[:, :, -length:, None] - cumulative[:, :, None, :]
        if causal:
            if past is not None or allowed is not None:
                raise ValueError('Causal fast path requires unmasked full prefix')
            allowed = torch.ones((length, length), device=x.device, dtype=torch.bool).tril()
        bias = bias.masked_fill(~allowed[:, None] if allowed.ndim == 3 else ~allowed, -torch.inf)
        groups = self.qheads // self.kvheads
        attended = F.scaled_dot_product_attention(q, k.repeat_interleave(groups, 1),
            v.repeat_interleave(groups, 1), attn_mask=bias, dropout_p=0.,
            is_causal=False, scale=self.scale)
        out = self.o_proj(attended.transpose(1, 2).reshape(batch, length, -1))
        return (out, (k, v), logs) if return_history else (out, (k, v))


class ForgettingModel(JMicroModel):
    def __init__(self, config):
        original = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(original, config)

    def _take_native(self, original, config):
        if sum(p.numel() for p in original.parameters()) != config[TAG]['native_expected_parameter_count']:
            raise ValueError('Actual native count differs')
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = original.model, original.lm_head
        for block in self.model.layers:
            block.self_attn = ForgettingAttention(block.self_attn, config[TAG]['arm'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Actual tagged count/tied vocabulary differs')
        self.train(original.training)

    @classmethod
    def from_native(cls, original, arm='learned_forget'):
        if (type(original) is not JMicroModel or any(p.grad is not None for p in original.parameters())
                or any(not torch.isfinite(p).all() for p in original.parameters() if not p.is_meta)):
            raise ValueError('Finite native without accumulated gradients required')
        config = tagged_config(original.config, arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(original), config)
        return result

    def _blocks(self, ids, positions, allowed, valid, cache=None, causal=False):
        x, layers, histories = self.model.embed_tokens(ids), [], []
        for i, block in enumerate(self.model.layers):
            attention, kv, logs = block.self_attn(block.input_layernorm(x), positions, allowed,
                None if cache is None else cache.layers[i], causal,
                log_history=None if cache is None else cache.log_gates[i],
                current_valid=valid, return_history=True)
            x = x + attention
            x = x + block.mlp(block.post_attention_layernorm(x))
            layers.append(kv)
            histories.append(logs)
        return self.model.norm(x), layers, histories

    def right_padded_hidden(self, ids):
        if ids.ndim != 2 or not 0 < ids.shape[1] <= self.config['max_position_embeddings']:
            raise ValueError('Nonempty bounded physical IDs required')
        positions = torch.arange(ids.shape[1], device=ids.device)[None].expand(ids.shape[0], -1)
        valid = torch.ones_like(ids, dtype=torch.bool)
        return self._blocks(ids, positions, None, valid, causal=True)[0]

    def _validate_cache(self, cache, ids):
        batch = ids.shape[0]
        if (type(cache) is not ForgettingKVCache or cache.arm != self.config[TAG]['arm']
                or len(cache.layers) != len(self.model.layers) or len(cache.log_gates) != len(self.model.layers)
                or cache.valid.ndim != 2 or cache.valid.shape[0] != batch
                or cache.valid.shape[1] == 0 or cache.valid.dtype != torch.bool
                or cache.valid.device != ids.device or cache.positions.shape != cache.valid.shape
                or cache.positions.dtype != torch.long or cache.positions.device != ids.device
                or not torch.equal(cache.positions, (cache.valid.long().cumsum(-1)-1).clamp_min(0))):
            raise ValueError('Typed forgetting cache metadata mismatch')
        length = cache.valid.shape[1]
        for row, logs in zip(cache.layers, cache.log_gates, strict=True):
            if (not isinstance(row, (tuple, list)) or len(row) != 2
                    or any(t.shape != (batch, self.config['num_key_value_heads'], length, self.config['head_dim'])
                           or t.device != ids.device or not t.is_floating_point()
                           or not torch.isfinite(t).all() for t in row)
                    or row[0].dtype != row[1].dtype
                    or logs.shape != (batch, self.config['num_attention_heads'], length)
                    or logs.device != ids.device or logs.dtype != torch.float32
                    or not torch.isfinite(logs).all() or (logs > 0).any()
                    or torch.count_nonzero(logs.masked_select(~cache.valid[:, None].expand_as(logs)))):
                raise ValueError('Typed finite KV/log gate shape, validity or precision mismatch')

    def forward(self, input_ids, attention_mask=None, cache=None, use_cache=False, labels=None,
                training_fast_path=False):
        if input_ids.ndim != 2 or input_ids.shape[1] == 0:
            raise ValueError('Nonempty batch/token IDs required')
        if training_fast_path:
            if attention_mask is not None or cache is not None or use_cache or labels is not None:
                raise ValueError('Full unmasked training only')
            return ModelOutput(self.lm_head(self.right_padded_hidden(input_ids)).float())
        valid = torch.ones_like(input_ids, dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError('Mask/current IDs mismatch')
        if cache is not None:
            self._validate_cache(cache, input_ids)
        before = (torch.zeros(input_ids.shape[0], device=input_ids.device, dtype=torch.long)
                  if cache is None else cache.valid.sum(-1))
        positions = (before[:, None] + valid.long().cumsum(-1)-1).clamp_min(0)
        if ((before + valid.sum(-1)) > self.config['max_position_embeddings']).any():
            raise ValueError('Context exceeded; reprefill required')
        key_valid = valid if cache is None else torch.cat((cache.valid, valid), 1)
        key_positions = positions if cache is None else torch.cat((cache.positions, positions), 1)
        allowed = valid[:, :, None] & key_valid[:, None, :] & (key_positions[:, None, :] <= positions[:, :, None])
        hidden, layers, histories = self._blocks(input_ids, positions, allowed, valid, cache)
        logits = self.lm_head(hidden).float() * valid[..., None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape or not labels[:, 1:].ne(-100).any():
                raise ValueError('Full current shifted supervised labels required')
            loss = F.cross_entropy(logits[:, :-1].reshape(-1, logits.shape[-1]),
                                   labels[:, 1:].reshape(-1), ignore_index=-100)
        result_cache = ForgettingKVCache(layers, key_valid, key_positions, histories,
                                          self.config[TAG]['arm']) if use_cache else None
        return ModelOutput(logits, result_cache, loss)

    def clip_grad_norm(self, max_norm, *, error_if_nonfinite=True):
        return torch.nn.utils.clip_grad_norm_(self.parameters(), max_norm,
                                             error_if_nonfinite=error_if_nonfinite)

    def load_state_dict(self, state_dict, strict=True, assign=False):
        expected = self.state_dict()
        if (strict is not True or assign is not False or set(state_dict) != set(expected)
                or any(state_dict[k].shape != v.shape or state_dict[k].dtype != v.dtype
                       or not torch.isfinite(state_dict[k]).all() for k, v in expected.items())
                or not torch.equal(state_dict['lm_head.weight'], state_dict['model.embed_tokens.weight'])
                or (self.config[TAG]['arm'] == 'static_half_forget' and any(torch.count_nonzero(v)
                    for k, v in state_dict.items() if '.forget_proj.' in k))):
            raise ValueError('Exact finite tagged state/tie/static coordinates required before mutation')
        return super().load_state_dict(state_dict, strict=True)

    def hf_reference(self):
        raise ValueError('Forgetting attention/cache requires an explicit inference adapter')

    def save(self, directory):
        raise ValueError('Typed research checkpoint required; portable export unimplemented')

    @classmethod
    def load(cls, directory):
        raise ValueError('Native directory load cannot substitute for typed forgetting state')
