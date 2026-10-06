"""Training-only residual dropout around the unchanged native 10M decoder.

No new parameters or state keys. Native evaluation loads the usual tensors and
never installs these hooks. All stochastic masks use checkpointed torch RNG.
"""
import math

from torch.nn import functional as F

from natural_context_contrast_corpus import NaturalCorpusTrainer

KIND = 'native_full_CE_training_only_embedding_and_residual_dropout_v1'
PROBABILITY = 0.1


def install_training_dropout(model, probability=PROBABILITY):
    if not math.isfinite(probability) or not 0 <= probability < 1:
        raise ValueError('Finite dropout probability in [0,1) required')
    if model.config['dropout'] != 0 or hasattr(model, '_residual_dropout_hooks'):
        raise ValueError('Require unchanged zero-dropout native model; install once')

    def tensor_hook(module, inputs, output):
        return F.dropout(output, p=probability, training=module.training)

    def attention_hook(module, inputs, output):
        # Drop only the residual branch; do not modify or discard the KV tuple.
        attention, cache = output
        return F.dropout(attention, p=probability, training=module.training), cache

    handles = [model.model.embed_tokens.register_forward_hook(tensor_hook)]
    for block in model.model.layers:
        handles.append(block.self_attn.register_forward_hook(attention_hook))
        handles.append(block.mlp.register_forward_hook(tensor_hook))
    model._residual_dropout_hooks = handles
    return handles


class ResidualDropoutTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, contrast=False,
                 device='cuda', seed=42):
        if contrast:
            raise ValueError('Dropout comparison is ordinary full CE, no auxiliary loss')
        super().__init__(parent, sampler, binding, batch, False, device, seed)
        install_training_dropout(self.model)
        self.spec.update(kind=KIND, regularization=dict(
            kind='inverted_training_only_dropout', probability=PROBABILITY,
            sites=['token_embedding', 'attention_output_before_residual',
                   'MLP_output_before_residual'],
            attention_probability_dropout=0.0, new_parameters=0,
            native_inference_unchanged=True, RNG='existing_checkpoint_CPU_CUDA_RNG'))
        self.lineage.update(kind=KIND)

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def step(self):
        if not self.model.training:
            raise ValueError('Training-only dropout requires model.train()')
        return super().step()
