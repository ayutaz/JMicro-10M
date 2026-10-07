"""Same-capacity MoC/MoS output comparison; frozen native decoder is retained.

Two residual low-rank contexts start at the original normalized hidden state.
Both arms learn identical physical matrices. MoC mixes contexts then uses one
softmax; MoS mixes normalized component probabilities in FP32 log space. This
is an adaptation with tied vocabulary, not the original paper's RNN recipe.
"""
import copy
import math

import torch
from torch import nn
from torch.nn import functional as F
from jmicro.model import JMicroModel

ARMS = ('mixture_contexts', 'mixture_softmaxes')
TAG = 'output_mixture_research'
POLICY = dict(kind='paired_two_residual_rank32_contexts_MoC_or_MoS_v1',
              experts=2, rank=32, residual='hidden+up(tanh(down(hidden)))',
              down_initializer_std=.02, up_initializer=0., prior_weights_initializer=0.,
              initial_prior=[.75, .25], initialization_seed=2026100741,
              shared_original_vocabulary=True, distribution_computation='FP32_log_space',
              additional_decoder_passes=0)
FOREIGN_TAGS = ('ffn_research', 'gated_shared_reuse', 'output_probability_link',
                'attention_gate_research')


def mixture_config(native, arm):
    if (arm not in ARMS or TAG in native or any(k in native for k in FOREIGN_TAGS)
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Ordinary counted native config and explicit output arm required')
    h = native['hidden_size']
    added = POLICY['experts'] * (2 * h * POLICY['rank'] + h + 1)
    result = copy.deepcopy(native)
    result[TAG] = dict(arm=arm, policy=copy.deepcopy(POLICY),
                       native_expected_parameter_count=native['expected_parameter_count'])
    result['expected_parameter_count'] += added
    return result


def native_config(config):
    tag = config.get(TAG, {})
    native = copy.deepcopy(config)
    native.pop(TAG, None)
    native['expected_parameter_count'] = tag.get('native_expected_parameter_count')
    if mixture_config(native, tag.get('arm')) != config:
        raise ValueError('Exact counted output-mixture policy required')
    return native


class OutputMixtureHead(nn.Module):
    def __init__(self, weight, arm):
        super().__init__()
        if arm not in ARMS or not isinstance(weight, nn.Parameter) or weight.ndim != 2:
            raise ValueError('Explicit arm and original tied vocabulary required')
        self.arm, self.weight = arm, weight
        h = weight.shape[1]
        # Linear's default initialization must not advance global CPU RNG.
        with torch.random.fork_rng(devices=[]):
            self.down = nn.ModuleList([nn.Linear(h, POLICY['rank'], bias=False) for _ in range(2)])
            self.up = nn.ModuleList([nn.Linear(POLICY['rank'], h, bias=False) for _ in range(2)])
            self.prior = nn.Linear(h, 2, bias=True)
            generator = torch.Generator().manual_seed(POLICY['initialization_seed'])
            for down, up in zip(self.down, self.up, strict=True):
                nn.init.normal_(down.weight, std=.02, generator=generator)
                nn.init.zeros_(up.weight)
            nn.init.zeros_(self.prior.weight)
            with torch.no_grad():
                self.prior.bias.copy_(torch.tensor([math.log(3.), 0.]))
        self.to(device=weight.device, dtype=weight.dtype)

    def contexts(self, hidden):
        return [hidden + up(torch.tanh(down(hidden)))
                for down, up in zip(self.down, self.up, strict=True)]

    def forward(self, hidden):
        contexts = self.contexts(hidden)
        # Explicit float linear avoids reduced precision in the prior/link.
        with torch.autocast(device_type=hidden.device.type, enabled=False):
            log_prior = F.log_softmax(F.linear(hidden.float(), self.prior.weight.float(),
                                              self.prior.bias.float()), dim=-1)
        if self.arm == 'mixture_contexts':
            # Native projection's autocast policy is preserved in both arms.
            # Weighted residuals keep the zero-residual parent exactly intact
            # even when exp(log_prior) sums to 1 only within FP32 roundoff.
            mixed = hidden.float() + sum(log_prior[..., k:k+1].exp() * (c.float() - hidden.float())
                                        for k, c in enumerate(contexts))
            return F.linear(mixed.to(hidden.dtype), self.weight).float()
        terms = []
        for k, context in enumerate(contexts):
            scores = F.linear(context, self.weight).float()
            terms.append(F.log_softmax(scores, dim=-1) + log_prior[..., k:k+1])
        return torch.logaddexp(terms[0], terms[1])


class OutputMixtureModel(JMicroModel):
    def __init__(self, config):
        native = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(native, config)

    def _take_native(self, native, config):
        if sum(p.numel() for p in native.parameters()) != config[TAG]['native_expected_parameter_count']:
            raise ValueError('Native actual parameter count differs')
        self.config = copy.deepcopy(config)
        self.model = native.model
        self.lm_head = OutputMixtureHead(native.lm_head.weight, config[TAG]['arm'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Actual output-mixture count or vocabulary tie differs')
        self.train(native.training)

    @classmethod
    def from_native(cls, native, arm):
        if type(native) is not JMicroModel or any(p.grad is not None for p in native.parameters()):
            raise ValueError('Unmodified native parent without accumulated gradients required')
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(native), mixture_config(native.config, arm))
        return result

    def load_state_dict(self, state_dict, strict=True, assign=False):
        expected = self.state_dict()
        if (strict is not True or set(expected) != set(state_dict)
                or any(v.shape != expected[k].shape or v.dtype != expected[k].dtype
                       or not torch.isfinite(v).all() for k, v in state_dict.items())
                or not torch.equal(state_dict['lm_head.weight'], state_dict['model.embed_tokens.weight'])):
            raise ValueError('Exact finite tagged output state and native tie required')
        return super().load_state_dict(state_dict, strict=True, assign=assign)

    def hf_reference(self):
        raise ValueError('Output mixture needs its dedicated typed evaluator')

    def save(self, directory):
        raise ValueError('Use full tagged research checkpoints; deployment is deferred')


def model_from_config(config):
    if TAG in config:
        return OutputMixtureModel(config)
    if any(k in config for k in FOREIGN_TAGS):
        raise ValueError('Refuse another research architecture in mixture evaluator')
    return JMicroModel(config)
