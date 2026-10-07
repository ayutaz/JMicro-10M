"""Explicit parameter-free native output link; frozen original model is unchanged."""
import torch
from torch import nn
from torch.nn import functional as F
from jmicro.model import JMicroModel

LINK = 'sigsoftmax_exp_z_times_sigmoid_z_FP32_v1'


def sigsoftmax_logits(raw):
    """Scores whose ordinary log_softmax equals normalized exp(z)*sigmoid(z).

    This is not log-probability yet. Do not subtract max(z) before this
    nonlinearity: sigsoftmax is not invariant to a common raw-logit shift.
    """
    scores = raw.float()
    return scores + F.logsigmoid(scores)


class SigSoftmaxHead(nn.Module):
    def __init__(self, weight):
        super().__init__()
        if not isinstance(weight, nn.Parameter) or weight.ndim != 2:
            raise ValueError('Original tied vocabulary parameter required')
        self.weight = weight

    def forward(self, hidden):
        return sigsoftmax_logits(F.linear(hidden, self.weight))


def install_sigsoftmax(model):
    tag = model.config.get('output_probability_link')
    if (tag not in (None, LINK) or type(model.lm_head) is not nn.Linear
            or model.lm_head.bias is not None
            or model.lm_head.weight is not model.model.embed_tokens.weight):
        raise ValueError('Original native tied head required; refuse wrong/double output link')
    model.lm_head = SigSoftmaxHead(model.lm_head.weight)
    model.config['output_probability_link'] = LINK
    return model


class SigSoftmaxModel(JMicroModel):
    """Official constructor for tagged linked checkpoints, including native cache."""
    def __init__(self, config):
        if config.get('output_probability_link') != LINK:
            raise ValueError('Explicit sigsoftmax model_config required')
        super().__init__(config)
        install_sigsoftmax(self)
