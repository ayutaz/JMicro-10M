"""Query-dependent SDPA output gates; frozen native model remains unchanged.

Both study arms start with zero gate logits and doubled output projections.
sigmoid(0)=1/2 preserves the parent's prediction function at conversion. This
reparameterization changes AdamW dynamics, so the matched control uses the same
conversion and a permanently constant half gate; old native CE is not that
control. This is an adaptation experiment, not a reproduction of fresh gated
attention pretraining.
"""
import copy

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, JMicroModel, rope

ARMS = ('static_half', 'query_headwise')
POLICY = dict(kind='head_specific_query_dependent_post_SDPA_sigmoid_v1',
              input='original_pre_attention_RMSNorm_output',
              position='after_SDPA_before_head_concatenation_and_o_proj',
              granularity='one_scalar_per_query_token_and_query_head',
              gate_bias=False, initial_gate_weights=0., initial_gate_value=.5,
              initial_o_proj_multiplier=2., extra_block_invocations=0)
FOREIGN_TAGS = ('ffn_research', 'gated_shared_reuse', 'output_probability_link')
TAG = 'attention_gate_research'


def gated_config(native, arm):
    if (arm not in ARMS or TAG in native or any(k in native for k in FOREIGN_TAGS)
            or native.get('activation') != 'swiglu'
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Explicit ordinary native config/count and gate arm required')
    result = copy.deepcopy(native)
    added = native['num_hidden_layers'] * native['hidden_size'] * native['num_attention_heads']
    result[TAG] = dict(policy=copy.deepcopy(POLICY), arm=arm,
                       native_expected_parameter_count=native['expected_parameter_count'])
    result['expected_parameter_count'] += added
    return result


def native_config(tagged):
    tag = tagged.get(TAG)
    if (not isinstance(tag, dict)
            or set(tag) != {'policy', 'arm', 'native_expected_parameter_count'}
            or tag['policy'] != POLICY or tag['arm'] not in ARMS
            or type(tag['native_expected_parameter_count']) is not int
            or any(k in tagged for k in FOREIGN_TAGS)):
        raise ValueError('Exact tagged query-gate policy/arm/native count required')
    native = copy.deepcopy(tagged)
    del native[TAG]
    native['expected_parameter_count'] = tag['native_expected_parameter_count']
    if gated_config(native, tag['arm']) != tagged:
        raise ValueError('Declared gate count/config differs from actual architecture')
    return native


class HeadwiseGatedAttention(Attention):
    def __init__(self, native, arm):
        if type(native) is not Attention or arm not in ARMS:
            raise ValueError('Original attention instance and explicit study arm required')
        nn.Module.__init__(self)
        self.qheads, self.kvheads = native.qheads, native.kvheads
        self.dim, self.theta, self.scale = native.dim, native.theta, native.scale
        self.q_proj, self.k_proj, self.v_proj = native.q_proj, native.k_proj, native.v_proj
        self.o_proj, self.q_norm, self.k_norm = native.o_proj, native.q_norm, native.k_norm
        self.arm = arm
        # Linear's discarded random initialization must not advance the parent's
        # RNG. The final gate weights are zero in both arms and on every device.
        with torch.random.fork_rng(devices=[]):
            gate = nn.Linear(self.q_proj.in_features, self.qheads, bias=False)
            nn.init.zeros_(gate.weight)
        self.gate_proj = gate.to(device=self.q_proj.weight.device, dtype=self.q_proj.weight.dtype)
        with torch.no_grad():
            self.o_proj.weight.mul_(2.)
        if not self.o_proj.weight.is_meta and not torch.isfinite(self.o_proj.weight).all():
            raise ValueError('Function-preserving output reparameterization must remain finite')
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
        groups = self.qheads // self.kvheads
        attended = F.scaled_dot_product_attention(
            q, k.repeat_interleave(groups, dim=1), v.repeat_interleave(groups, dim=1),
            attn_mask=None if causal else allowed[:, None], dropout_p=0.,
            is_causal=causal, scale=self.scale)
        scores = self.gate_proj(x)
        if self.arm == 'static_half':
            # Keep the same projection, tensor shapes and optimizer parameter
            # partition in both arms. The control's gate gradients are zero.
            scores = scores * 0.
        gate = scores.sigmoid().transpose(1, 2).unsqueeze(-1)
        attended = (attended * gate).transpose(1, 2).reshape(batch, length, -1)
        return self.o_proj(attended), (k, v)


class HeadwiseGateModel(JMicroModel):
    def __init__(self, config):
        native = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(native, config)

    def _take_native(self, native, config):
        expected = config[TAG]['native_expected_parameter_count']
        if sum(p.numel() for p in native.parameters()) != expected:
            raise ValueError('Native unique parameter count does not match config')
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = native.model, native.lm_head
        for block in self.model.layers:
            block.self_attn = HeadwiseGatedAttention(block.self_attn, config[TAG]['arm'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Actual gate parameter count or native vocabulary tie differs')
        self.train(native.training)

    @classmethod
    def from_native(cls, native, arm):
        if type(native) is not JMicroModel or any(p.grad is not None for p in native.parameters()):
            raise ValueError('Unmodified native parent without accumulated gradients required')
        config = gated_config(native.config, arm)
        if any(not torch.isfinite(p).all() for p in native.parameters() if not p.is_meta):
            raise ValueError('Finite original parent parameters required')
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        # Preserve the actual parent, its ties, weights and RNG for both arms.
        result._take_native(copy.deepcopy(native), config)
        return result

    def hf_reference(self):
        raise ValueError('Headwise attention gates require a dedicated model adapter')

    def load_state_dict(self, state_dict, strict=True, assign=False):
        if (strict is not True or set(state_dict) != set(self.state_dict())
                or any(not torch.isfinite(v).all() for v in state_dict.values())
                or not torch.equal(state_dict['lm_head.weight'], state_dict['model.embed_tokens.weight'])
                or (self.config[TAG]['arm'] == 'static_half' and any(
                    torch.count_nonzero(v) != 0 for k, v in state_dict.items() if '.self_attn.gate_proj.weight' in k))):
            raise ValueError('Exact finite tagged state, tied vocabulary and zero static gates required')
        return super().load_state_dict(state_dict, strict=True, assign=assign)

    def save(self, directory):
        raise ValueError('Study checkpoints must retain explicit gate config/state; export not implemented')

    @classmethod
    def load(cls, directory):
        raise ValueError('Use explicitly tagged scientific checkpoints, not stock native exports')


def model_from_config(config):
    if any(k in config for k in FOREIGN_TAGS):
        raise ValueError('Unrelated research architecture is not a headwise-gate checkpoint')
    return HeadwiseGateModel(config) if TAG in config else JMicroModel(config)
