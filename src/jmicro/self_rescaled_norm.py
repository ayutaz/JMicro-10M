"""Experimental input-conditioned RMS feature rescaling component only.

A tagged model/trainer/cache still has to own this component. Native generic
traversal is deliberately refused. No frozen model or normalization is changed.
"""
import math

import torch
from torch import nn

from jmicro.model import RMSNorm

ARMS = ('self_rescaled', 'disabled_zero')
IMPLEMENTATION = 'original_RMS_plus_FP32_raw_input_dot_tanh_channel_rescale_v1'
POLICY = dict(kind='single_vector_input_conditioned_RMS_feature_rescale_v1',
    alpha_initial=1., beta_initial=0., activation='tanh',
    sites='all_original_pre_attention_pre_FFN_final_RMS_only',
    original_gamma_rescaled=False, QK_norm_added=False,
    aggregation='one_raw_input_dot_per_token',
    arithmetic='original_FP32_RMS_base_plus_input_dtype_unit_times_dynamic_scale',
    dynamic_dot='FP32_except_float64_mathematical_reference')


def extra_parameter(name):
    return name.endswith('.rescale_alpha') or name.endswith('.rescale_beta')


def added_parameters(config):
    return 2*config['hidden_size']*(2*config['num_hidden_layers']+1)


def rescale(unit, raw, gamma, alpha, beta, arm='self_rescaled'):
    """Keep the original u*gamma operation, add u*alpha*tanh(raw dot beta).

    Float64 permits independent analytic mathematical tests. Actual native
    FP32/BF16 execution computes the new dot/tanh explicitly in FP32. The
    original unit vector's dtype and multiplication by gamma are untouched.
    """
    if (arm not in ARMS or unit.shape != raw.shape or raw.ndim < 1 or not raw.shape[-1]
            or any(not t.is_floating_point() or t.device != raw.device for t in (unit,raw,gamma,alpha,beta))
            or unit.dtype != raw.dtype or any(t.shape != (raw.shape[-1],) for t in (gamma,alpha,beta))
            or any(t.dtype != gamma.dtype for t in (alpha,beta))):
        raise ValueError('Aligned original unit/raw and channel vectors/explicit arm required')
    with torch.autocast(device_type=raw.device.type,enabled=False):
        dtype = torch.float64 if raw.dtype == torch.float64 else torch.float32
        activation = (raw.to(dtype)*beta.to(dtype)).sum(-1,keepdim=True).tanh()
        dynamic = activation*alpha.to(dtype)
        if arm == 'disabled_zero':
            dynamic = dynamic*0.
        return unit*gamma + unit*dynamic.to(unit.dtype)


class SelfRescaledRMSNorm(RMSNorm):
    def __init__(self, original, arm='self_rescaled'):
        if (type(original) is not RMSNorm or arm not in ARMS
                or original.weight.ndim != 1 or original.weight.numel() == 0
                or not math.isfinite(original.eps) or original.eps <= 0):
            raise ValueError('Exact original RMSNorm and explicit rescaling arm required')
        nn.Module.__init__(self)
        self.weight, self.eps, self.arm = original.weight, original.eps, arm
        self.rescale_alpha = nn.Parameter(torch.ones_like(self.weight))
        self.rescale_beta = nn.Parameter(torch.zeros_like(self.weight))
        self.train(original.training)

    def forward(self, *args, **kwargs):
        raise ValueError('Self-rescaled RMS requires explicit model-owned traversal')

    def owned_forward(self, x):
        # Match the frozen native FP32 reduction, cast and gamma operation.
        unit = (x.float()*torch.rsqrt(x.float().square().mean(-1,keepdim=True)+self.eps)).to(x.dtype)
        return rescale(unit,x,self.weight,self.rescale_alpha,self.rescale_beta,self.arm)
