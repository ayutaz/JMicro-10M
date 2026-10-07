"""Fresh equal-budget two-projection ReLU squared; frozen native stays intact."""
import copy

import torch
from torch import nn
from torch.nn import functional as F
from jmicro.model import JMicroModel

POLICY = dict(kind='two_projection_squared_ReLU_equal_FFN_matrix_budget_v1',
              projections=2, activation='relu_squared', bias=False,
              gain_or_normalization_added=False, additional_invocations=0)
FOREIGN_TAGS = ('output_probability_link', 'gated_shared_reuse')


def squared_config(native, seed=42):
    if (native.get('activation') != 'swiglu' or 'ffn_research' in native
            or any(k in native for k in FOREIGN_TAGS)
            or type(seed) is not int or not 0 <= seed < 2**31):
        raise ValueError('Fresh ordinary native SwiGLU config and valid initialization seed required')
    width = native['intermediate_size']
    if type(width) is not int or width <= 0 or width % 2:
        raise ValueError('Positive even native FFN width for exact3-to2 matrix budget required')
    result = copy.deepcopy(native)
    result.update(activation='relu_squared', intermediate_size=width * 3 // 2,
        ffn_research=dict(policy=copy.deepcopy(POLICY), native_intermediate_size=width,
                          initialization_seed=seed))
    return result


def native_config(tagged):
    tag = tagged.get('ffn_research')
    if (not isinstance(tag, dict) or set(tag) != {'policy', 'native_intermediate_size', 'initialization_seed'}
            or tag['policy'] != POLICY or any(k in tagged for k in FOREIGN_TAGS)):
        raise ValueError('Explicit unchanged squared-ReLU FFN policy required')
    native = copy.deepcopy(tagged)
    del native['ffn_research']
    native.update(activation='swiglu', intermediate_size=tag['native_intermediate_size'])
    if squared_config(native, tag['initialization_seed']) != tagged:
        raise ValueError('Squared-ReLU activation/width/tag does not match exact native budget')
    return native


class SquaredReLUMLP(nn.Module):
    def __init__(self, hidden, intermediate):
        super().__init__()
        self.up_proj = nn.Linear(hidden, intermediate, bias=False)
        self.down_proj = nn.Linear(intermediate, hidden, bias=False)

    def forward(self, x):
        return self.down_proj(F.relu(self.up_proj(x)).square())


class SquaredReLUModel(JMicroModel):
    """Same inherited causal/mask/cache paths; each physical block visited once."""
    def __init__(self, config):
        native = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_fresh_scaffold(native, config)

    def _take_fresh_scaffold(self, native, config):
        self.config = copy.deepcopy(config)
        self.model, self.lm_head = native.model, native.lm_head
        # Initialize replacement matrices on CPU, even for a GPU scaffold.
        # The fork preserves the native global RNG and all non-FFN tensors.
        with torch.random.fork_rng(devices=[]):
            for index, block in enumerate(self.model.layers):
                torch.random.default_generator.manual_seed(
                    config['ffn_research']['initialization_seed'] + 1000003 + index)
                mlp = SquaredReLUMLP(config['hidden_size'], config['intermediate_size'])
                mlp.apply(native._initialize)
                reference = native.model.embed_tokens.weight
                block.mlp = mlp.to(device=reference.device, dtype=reference.dtype)
        self.train(native.training)

    @classmethod
    def from_native_fresh(cls, native, seed=42):
        if type(native) is not JMicroModel or any(p.grad is not None for p in native.parameters()):
            raise ValueError('Untouched fresh native scaffold required; no learned-weight conversion')
        config = squared_config(native.config, seed)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_fresh_scaffold(native, config)
        return result

    def hf_reference(self):
        raise ValueError('Squared-ReLU FFN needs a dedicated export adapter; stock SwiGLU reference is invalid')


def model_from_config(config):
    """Explicit official FFN constructor; refuse unrelated tagged architectures."""
    if any(k in config for k in FOREIGN_TAGS):
        raise ValueError('Different research architecture is not an FFN study checkpoint')
    if 'ffn_research' in config:
        return SquaredReLUModel(config)
    if config.get('activation') != 'swiglu':
        raise ValueError('Untagged non-native FFN refused')
    return JMicroModel(config)
