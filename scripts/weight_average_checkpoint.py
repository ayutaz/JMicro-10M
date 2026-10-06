"""One equal-weight, same-parent midpoint; model-only, never a resumed optimizer."""
import copy
import torch

KIND = 'jmicro_same_parent_equal_weight_model_only_v1'
TIED = ('model.embed_tokens.weight', 'lm_head.weight')
PARENT_KEYS = ('parent', 'parent_update', 'parent_tokens', 'parent_supervised_tokens',
               'parent_body_bytes', 'parent_token_digest')


def midpoint(left, right, references):
    if left['model_config'] != right['model_config']:
        raise ValueError('Same model configuration required')
    if any(left['lineage'][k] != right['lineage'][k] for k in PARENT_KEYS):
        raise ValueError('Same actual learned parent required')
    if set(left['model']) != set(right['model']):
        raise ValueError('State keys differ')
    for state in (left, right):
        if not state['model_config']['tie_word_embeddings']:
            raise ValueError('Pinned tied embedding policy required')
        if not torch.equal(state['model'][TIED[0]], state['model'][TIED[1]]):
            raise ValueError('Input/output embedding disagreement')
    result = {}
    for name, a in left['model'].items():
        b = right['model'][name]
        if a.shape != b.shape or a.dtype != b.dtype or a.device.type != 'cpu' or b.device.type != 'cpu':
            raise ValueError('Tensor shape/dtype/CPU differs: ' + name)
        if a.is_floating_point():
            if a.dtype != torch.float32 or not torch.isfinite(a).all() or not torch.isfinite(b).all():
                raise ValueError('Finite original FP32 tensors required: ' + name)
            value = a.mul(.5).add(b.mul(.5))
            if not torch.isfinite(value).all():
                raise ValueError('Nonfinite midpoint: ' + name)
            result[name] = value
        else:
            if not torch.equal(a, b):
                raise ValueError('Nonfloating buffer differs: ' + name)
            result[name] = a.clone()
    result[TIED[1]] = result[TIED[0]]
    return dict(kind=KIND, model_config=copy.deepcopy(left['model_config']), model=result,
        model_only=True, resumable_training_state=False,
        lineage=dict(common_parent={k: copy.deepcopy(left['lineage'][k]) for k in PARENT_KEYS},
            inputs=copy.deepcopy(references), coefficients=[.5, .5],
            new_optimizer_updates=0, new_scientific_teacher_tokens=0,
            optimizer_scheduler_RNG_sampler_not_averaged=True,
            inherited_training_exposure='Two named, previously completed100M branches from one shared10.5B learned parent; no new learning and no unique corpus-union claim.'))
