"""Original RoPE operation order with reusable constants; not yet a runtime.

Helpers only. No existing model/attention/trainer/cache dispatch is modified.
Actual CUDA value/update equivalence and speed remain unverified.
"""
import torch


def original_rope_tables(positions, dim, theta, dtype):
    if (positions.ndim != 2 or positions.dtype != torch.long or not positions.numel()
            or type(dim) is not int or dim <= 0 or dim % 2
            or dtype not in (torch.float32, torch.bfloat16)):
        raise ValueError('Original nonempty positions/even dimension and FP32/BF16 required')
    with torch.autocast(device_type=positions.device.type, enabled=False):
        inv = 1.0 / (theta ** (torch.arange(0, dim, 2, device=positions.device).float() / dim))
        phase = positions.float()[..., None] * inv
        phase = torch.cat((phase, phase), dim=-1)[:, None]
        cos, sin = phase.cos().to(dtype), phase.sin().to(dtype)
    return cos, sin


def apply_original_rope_tables(x, tables):
    cos, sin = tables
    if (x.ndim != 4 or cos.shape != (x.shape[0], 1, x.shape[2], x.shape[3])
            or sin.shape != cos.shape or cos.dtype != sin.dtype or cos.dtype != x.dtype
            or cos.device != sin.device or cos.device != x.device
            or cos.requires_grad or sin.requires_grad):
        raise ValueError('Exact original shape/device/dtype and constant RoPE tables required')
    half = x.shape[-1] // 2
    rotated = torch.cat((-x[..., half:], x[..., :half]), dim=-1)
    return x*cos + rotated*sin
