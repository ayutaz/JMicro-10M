"""Fixed zero-Key/zero-Value attention alternative; original weights unchanged.

The extra alternative is not a vocabulary token and is never stored in cache.
Enabled conversion changes the native function. This is an explicit experiment.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, JMicroModel, ModelOutput, rope

TAG = 'fixed_zero_attention_research'
ARMS = ('fixed_zero', 'disabled_native')
IMPLEMENTATION = 'fixed_zero_KV_phantom_square_causal_real_cache_v1'
POLICY = dict(kind='fixed_zero_KV_attention_denominator_plus1_v1',
    phantom_key=0., phantom_value=0., phantom_logit=0., phantom_count=1,
    phantom_trainable=False, phantom_cached=False, real_positions_unchanged=True,
    original_weights_rescaled=False, native_initial_function_preserved=False)


def tagged_config(native, arm='fixed_zero'):
    if (arm not in ARMS or any(k.endswith('_research') for k in native)
            or any(k in native for k in ('gated_shared_reuse', 'output_probability_link'))
            or native.get('qk_norm_type') != 'none' or native.get('num_attention_heads') != 4
            or native.get('num_key_value_heads') != 2
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Original NoQKNorm Q4/KV2 config/count and explicit arm required')
    c = copy.deepcopy(native)
    c[TAG] = dict(policy=copy.deepcopy(POLICY), arm=arm, implementation=IMPLEMENTATION)
    return c


def native_config(tagged):
    tag = tagged.get(TAG)
    if (not isinstance(tag, dict) or set(tag) != {'policy', 'arm', 'implementation'}
            or tag['policy'] != POLICY or tag['implementation'] != IMPLEMENTATION
            or tag['arm'] not in ARMS):
        raise ValueError('Exact fixed-zero attention runtime/arm required')
    native = copy.deepcopy(tagged)
    del native[TAG]
    if tagged_config(native, tag['arm']) != tagged:
        raise ValueError('Exact tagged/native configuration roundtrip required')
    return native


def quiet_attention(q, k, v, *, mask=None, causal=False, scale=None):
    """Ordinary SDPA on an extra exact-zero alternative, including all gradients.

    Causal training prepends a dummy query too: a square causal triangle then
    exposes null plus real keys through the current token without an offset bug.
    Stable SDPA normalizes the phantom alongside the real scores, never after
    an independently shifted real-only maximum.
    """
    if (any(t.ndim != 4 or not t.is_floating_point() for t in (q, k, v))
            or k.shape != v.shape or q.shape[:2] != k.shape[:2]
            or q.shape[-1] != k.shape[-1] or min(q.shape) <= 0 or min(k.shape) <= 0
            or any(t.device != q.device or t.dtype != q.dtype for t in (k, v))
            or (causal and (mask is not None or q.shape[2] != k.shape[2]))):
        raise ValueError('Aligned nonempty Q/K/V and square unmasked causal inputs required')
    if mask is not None and (mask.dtype != torch.bool or mask.device != q.device
            or mask.ndim != 4 or mask.shape[-2:] != (q.shape[2], k.shape[2])
            or mask.shape[0] not in (1, q.shape[0]) or mask.shape[1] not in (1, q.shape[1])):
        raise ValueError('Broadcastable boolean real-key mask required')
    zeros = lambda t: t.new_zeros((*t.shape[:2], 1, t.shape[-1]))
    extended_k, extended_v = torch.cat((zeros(k), k), 2), torch.cat((zeros(v), v), 2)
    if causal:
        out = F.scaled_dot_product_attention(torch.cat((zeros(q), q), 2), extended_k,
            extended_v, dropout_p=0., is_causal=True, scale=scale)
        return out[:, :, 1:]
    if mask is not None:
        null = torch.ones((*mask.shape[:-1], 1), device=mask.device, dtype=torch.bool)
        mask = torch.cat((null, mask), -1)
    return F.scaled_dot_product_attention(q, extended_k, extended_v,
        attn_mask=mask, dropout_p=0., is_causal=False, scale=scale)


@dataclass
class QuietCache:
    # No native .layers attribute: native inference must not silently remove null.
    real: list[tuple[torch.Tensor, torch.Tensor]]
    valid: torch.Tensor
    positions: torch.Tensor
    arm: str
    implementation: str = IMPLEMENTATION


class QuietAttention(Attention):
    def __init__(self, original, arm):
        if type(original) is not Attention or arm not in ARMS:
            raise ValueError('Original native attention and explicit arm required')
        nn.Module.__init__(self)
        for name in ('qheads', 'kvheads', 'dim', 'theta', 'scale',
                     'q_proj', 'k_proj', 'v_proj', 'o_proj', 'q_norm', 'k_norm'):
            setattr(self, name, getattr(original, name))
        self.arm = arm
        self.train(original.training)

    def forward(self, *args, **kwargs):
        raise ValueError('Fixed-zero attention requires model-owned typed traversal')

    def owned_forward(self, x, positions, allowed, past, causal=False):
        if self.arm == 'disabled_native':
            return Attention.forward(self, x, positions, allowed, past, causal)
        batch, length, _ = x.shape
        def project(layer, heads):
            return layer(x).view(batch, length, heads, self.dim).transpose(1, 2)
        q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
        k = rope(self.k_norm(project(self.k_proj, self.kvheads)), positions, self.theta)
        v = project(self.v_proj, self.kvheads)
        if past is not None:
            if causal:
                raise ValueError('Cached attention requires absolute-position real mask')
            k, v = torch.cat((past[0], k), 2), torch.cat((past[1], v), 2)
        groups = self.qheads // self.kvheads
        attended = quiet_attention(q, k.repeat_interleave(groups, 1), v.repeat_interleave(groups, 1),
            mask=None if causal else allowed[:, None], causal=causal, scale=self.scale)
        return self.o_proj(attended.transpose(1, 2).reshape(batch, length, -1)), (k, v)


class QuietModel(JMicroModel):
    def __init__(self, config):
        original = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(original, config)

    def _take_native(self, original, config):
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = original.model, original.lm_head
        for block in self.model.layers:
            block.self_attn = QuietAttention(block.self_attn, config[TAG]['arm'])
        # A nontrainable typed-state sentinel prevents loading native/other-arm
        # tensors as a quiet checkpoint merely because all weight names match.
        self.register_buffer('quiet_runtime', torch.tensor(
            [1, ARMS.index(config[TAG]['arm']), config['expected_parameter_count']],
            device=self.lm_head.weight.device, dtype=torch.long))
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Unchanged actual native count and tied vocabulary required')
        self.train(original.training)

    @classmethod
    def from_native(cls, original, arm='fixed_zero'):
        if (type(original) is not JMicroModel or any(p.grad is not None for p in original.parameters())
                or any(not torch.isfinite(p).all() for p in original.parameters() if not p.is_meta)):
            raise ValueError('Finite original native model without accumulated gradients required')
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(original), tagged_config(original.config, arm))
        return result

    def _blocks(self, ids, positions, allowed, cache=None, causal=False):
        x, real = self.model.embed_tokens(ids), []
        for i, block in enumerate(self.model.layers):
            out, kv = block.self_attn.owned_forward(block.input_layernorm(x), positions, allowed,
                None if cache is None else cache.real[i], causal)
            x = x + out
            x = x + block.mlp(block.post_attention_layernorm(x))
            real.append(kv)
        return self.model.norm(x), real

    def right_padded_hidden(self, ids):
        if ids.ndim != 2 or not 0 < ids.shape[1] <= self.config['max_position_embeddings']:
            raise ValueError('Nonempty bounded physical training inputs required')
        positions = torch.arange(ids.shape[1], device=ids.device)[None].expand(ids.shape[0], -1)
        return self._blocks(ids, positions, None, causal=True)[0]

    def _validate_cache(self, c, ids):
        if (type(c) is not QuietCache or c.implementation != IMPLEMENTATION
                or c.arm != self.config[TAG]['arm'] or len(c.real) != len(self.model.layers)
                or c.valid.ndim != 2 or c.valid.shape[0] != ids.shape[0] or not c.valid.shape[1]
                or c.valid.dtype != torch.bool or c.valid.device != ids.device
                or c.positions.shape != c.valid.shape or c.positions.device != ids.device
                or c.positions.dtype != torch.long
                or not torch.equal(c.positions, (c.valid.long().cumsum(-1)-1).clamp_min(0))):
            raise ValueError('Exact real-cache metadata/arm/runtime required')
        shape = (ids.shape[0], self.config['num_key_value_heads'], c.valid.shape[1], self.config['head_dim'])
        for pair in c.real:
            if (not isinstance(pair, (list, tuple)) or len(pair) != 2
                    or any(t.shape != shape or t.device != ids.device or not t.is_floating_point()
                           or not torch.isfinite(t).all() for t in pair)
                    or pair[0].dtype != pair[1].dtype):
                raise ValueError('Finite aligned real-only K/V history required')

    def forward(self, input_ids, attention_mask=None, cache=None, use_cache=False,
                labels=None, training_fast_path=False):
        if input_ids.ndim != 2 or not input_ids.shape[1]:
            raise ValueError('Nonempty batch/token IDs required')
        if training_fast_path:
            if attention_mask is not None or cache is not None or use_cache or labels is not None:
                raise ValueError('Full unmasked training only')
            return ModelOutput(self.lm_head(self.right_padded_hidden(input_ids)).float())
        valid = torch.ones_like(input_ids, dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError('Current mask/IDs mismatch')
        if cache is not None:
            self._validate_cache(cache, input_ids)
        before = torch.zeros(input_ids.shape[0], device=input_ids.device, dtype=torch.long) if cache is None else cache.valid.sum(-1)
        positions = (before[:, None]+valid.long().cumsum(-1)-1).clamp_min(0)
        if ((before+valid.sum(-1)) > self.config['max_position_embeddings']).any():
            raise ValueError('Context exceeded; reprefill required')
        key_valid = valid if cache is None else torch.cat((cache.valid, valid), 1)
        key_positions = positions if cache is None else torch.cat((cache.positions, positions), 1)
        allowed = valid[:, :, None] & key_valid[:, None, :] & (key_positions[:, None, :] <= positions[:, :, None])
        hidden, real = self._blocks(input_ids, positions, allowed, cache)
        logits = self.lm_head(hidden).float()*valid[..., None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape or not labels[:, 1:].ne(-100).any():
                raise ValueError('Full current supervised shifted labels required')
            loss = F.cross_entropy(logits[:, :-1].reshape(-1, logits.shape[-1]), labels[:, 1:].reshape(-1), ignore_index=-100)
        result = QuietCache(real, key_valid, key_positions, self.config[TAG]['arm']) if use_cache else None
        return ModelOutput(logits, result, loss)

    def clip_grad_norm(self, max_norm, *, error_if_nonfinite=True):
        return torch.nn.utils.clip_grad_norm_(self.parameters(), max_norm, error_if_nonfinite=error_if_nonfinite)

    def load_state_dict(self, state_dict, strict=True, assign=False):
        expected = self.state_dict()
        if (strict is not True or assign is not False or set(state_dict) != set(expected)
                or any(not isinstance(state_dict[k], torch.Tensor) or state_dict[k].shape != v.shape
                       or state_dict[k].dtype != v.dtype or not torch.isfinite(state_dict[k]).all()
                       for k, v in expected.items())
                or not torch.equal(state_dict['quiet_runtime'].cpu(), self.quiet_runtime.cpu())
                or not torch.equal(state_dict['lm_head.weight'], state_dict['model.embed_tokens.weight'])):
            raise ValueError('Strict finite typed quiet state/arm/tie required before mutation')
        return super().load_state_dict(state_dict, strict=True)

    def save(self, directory):
        raise ValueError('Typed quiet research checkpoint required; native export unsupported')

    @classmethod
    def load(cls, directory):
        raise ValueError('Native directory load cannot replace a quiet checkpoint')

    def hf_reference(self):
        raise ValueError('Fixed-zero attention requires its explicit inference adapter')
