"""Opt-in CPU FP32 inference with FP64 accumulation and FP32 boundaries.

Weights and saved activations stay FP32. This is a real inference profile,
independent of the CUDA/BF16 training path. It is deliberately CPU-only and
inference-only; installing it does not modify weights or their state keys.
"""
import types

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, MLP, RMSNorm

PROFILE = 'cpu-f32-f64-accumulation-v1'


def _check(module, x):
    if module.training or torch.is_grad_enabled() or x.device.type != 'cpu' or x.dtype != torch.float32 or torch.is_autocast_enabled('cpu'):
        raise ValueError('Stable FP32 profile requires CPU FP32 inference_mode and eval')


def linear(module, x):
    _check(module, x)
    return F.linear(x.double(), module.weight.double(),
                    None if module.bias is None else module.bias.double()).float()


def norm(module, x):
    _check(module, x)
    eps = module.eps if isinstance(module, RMSNorm) else module.variance_epsilon
    variance = x.double().square().mean(-1, keepdim=True).float()
    scale = (1.0 / (variance + eps).double().sqrt().float())
    return (x * scale) * module.weight


def silu(x):
    return (x.double() / (1.0 + (-x.double()).exp())).float()


def probabilities(score):
    maximum = score.max(dim=-1, keepdim=True).values
    # Handle fully masked rows without producing NaNs (padding query rows).
    active = torch.isfinite(maximum)
    shifted = torch.where(active, score-maximum, -torch.inf)
    exponent = shifted.double().exp().float()
    total = exponent.double().sum(-1, keepdim=True)
    inverse = torch.where(total > 0, total.reciprocal(), 0).float()
    return exponent * inverse


def attended(q, k, v, mask, scale):
    score = (q.double() @ k.double().transpose(-2, -1)).float() * scale
    if mask is not None:
        score = score.masked_fill(~mask, -torch.inf) if mask.dtype == torch.bool else score + mask
    return (probabilities(score).double() @ v.double()).float()


def rotary(x, positions, theta):
    dim = x.shape[-1]
    inv = 1.0 / (theta ** (torch.arange(0, dim, 2, device=x.device).float()/dim))
    phase = positions.float()[..., None]*inv
    phase = torch.cat((phase, phase), dim=-1)[:, None]
    cos, sin = phase.double().cos().float(), phase.double().sin().float()
    half = dim//2
    rotated = torch.cat((-x[..., half:], x[..., :half]), dim=-1)
    return x*cos + rotated*sin


def own_attention(module, x, positions, allowed, past, causal=False):
    _check(module, x)
    batch, length, _ = x.shape
    def project(layer, heads):
        return layer(x).view(batch, length, heads, module.dim).transpose(1, 2)
    q = rotary(module.q_norm(project(module.q_proj, module.qheads)), positions, module.theta)
    k = rotary(module.k_norm(project(module.k_proj, module.kvheads)), positions, module.theta)
    v = project(module.v_proj, module.kvheads)
    if past is not None:
        k, v = torch.cat((past[0], k), 2), torch.cat((past[1], v), 2)
    groups = module.qheads//module.kvheads
    if causal:
        allowed = torch.ones(length, length, dtype=torch.bool).tril()[None]
    output = attended(q, k.repeat_interleave(groups, 1), v.repeat_interleave(groups, 1),
                      allowed[:, None], module.scale)
    return module.o_proj(output.transpose(1, 2).reshape(batch, length, -1)), (k, v)


def own_mlp(module, x):
    _check(module, x)
    return module.down_proj(silu(module.gate_proj(x))*module.up_proj(x))


def hf_attention(module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs):
    _check(module, query)
    if dropout != 0:
        raise ValueError('Stable inference has no dropout')
    groups = module.num_key_value_groups
    output = attended(query, key.repeat_interleave(groups, 1), value.repeat_interleave(groups, 1),
                      attention_mask, scaling)
    return output.transpose(1, 2).contiguous(), None


def hf_rotary(module, x, position_ids):
    _check(module, x)
    phase = position_ids.float()[..., None]*module.inv_freq
    phase = torch.cat((phase, phase), dim=-1)
    return phase.double().cos().float(), phase.double().sin().float()


def install(model):
    """Install explicit arithmetic on the real Torch/Llama forward/cache path."""
    from transformers.masking_utils import ALL_MASK_ATTENTION_FUNCTIONS
    from transformers.modeling_utils import ALL_ATTENTION_FUNCTIONS
    from transformers.models.llama.modeling_llama import LlamaRMSNorm, LlamaMLP, LlamaRotaryEmbedding
    if model.training or any(p.device.type != 'cpu' or p.dtype != torch.float32 for p in model.parameters()):
        raise ValueError('Stable profile installation requires an eval CPU FP32 model')
    config = model.config
    if isinstance(config, dict):
        if config['qk_norm_type'] != 'none':
            raise ValueError('Stable profile currently supports NoNorm only')
    elif config.model_type != 'llama':
        raise ValueError('Stable profile currently supports Llama only')
    else:
        if config.rope_parameters != {'rope_type':'default','rope_theta':10000.0}:
            raise ValueError('Stable Llama profile requires the trained default RoPE contract')
        ALL_ATTENTION_FUNCTIONS.register(PROFILE, hf_attention)
        ALL_MASK_ATTENTION_FUNCTIONS.register(PROFILE, ALL_MASK_ATTENTION_FUNCTIONS['eager'])
        config._attn_implementation = PROFILE
    for module in model.modules():
        if isinstance(module, nn.Linear):
            module.forward = types.MethodType(linear, module)
        elif isinstance(module, (RMSNorm, LlamaRMSNorm)):
            module.forward = types.MethodType(norm, module)
        elif isinstance(module, Attention):
            module.forward = types.MethodType(own_attention, module)
        elif isinstance(module, MLP):
            module.forward = types.MethodType(own_mlp, module)
        elif isinstance(module, LlamaMLP):
            module.act_fn.forward = types.MethodType(lambda activation, x: silu(x), module.act_fn)
        elif isinstance(module, LlamaRotaryEmbedding):
            module.forward = types.MethodType(hf_rotary, module)
    model._jmicro_inference_precision = PROFILE
    return model
