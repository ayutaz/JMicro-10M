"""Read-only decomposition of the native tied embedding's two gradient paths."""
import math

import torch
from torch.nn import functional as F

from natural_context_contrast_trainer import right_padded_hidden


def gradient_statistics(input_gradient, output_gradient):
    a, b = input_gradient.detach().double(), output_gradient.detach().double()
    if a.shape != b.shape or a.ndim != 2 or not torch.isfinite(a).all() or not torch.isfinite(b).all():
        raise ValueError('Two finite vocabulary-by-hidden gradients required')
    na, nb = float(a.norm()), float(b.norm())
    if not na or not nb:
        raise ValueError('Both native gradient paths must be nonzero')
    dot = float((a*b).sum())
    an, bn = a.norm(dim=1), b.norm(dim=1)
    shared = (an > 0) & (bn > 0)
    row_dot = (a*b).sum(dim=1)
    return dict(input_norm=na, output_norm=nb, output_to_input_norm_ratio=nb/na,
        dot=dot, cosine=dot/(na*nb), combined_norm=float((a+b).norm()),
        cancellation_ratio=float((a+b).norm())/(na+nb),
        shared_nonzero_vocabulary_rows=int(shared.sum()),
        conflicting_shared_rows=int(((row_dot < 0) & shared).sum()),
        EOS_input_norm=float(an[3]), EOS_output_norm=float(bn[3]),
        input_objective_descent_dot=float(((a+b)*a).sum()),
        output_objective_descent_dot=float(((a+b)*b).sum()))


def decompose(model, inputs, targets):
    """Keep tied parameters untouched; use an ephemeral tensor for attribution."""
    if model.training or inputs.shape != targets.shape or any(p.grad is not None for p in model.parameters()):
        raise ValueError('Eval-mode native model, matching targets and no accumulated grads required')
    weight = model.model.embed_tokens.weight
    if model.lm_head.weight is not weight or not model.config['tie_word_embeddings']:
        raise ValueError('Actual tied native embedding required')
    selected = targets != -100
    if not selected.any():
        raise ValueError('Original supervised body/EOS positions required')
    # Same native decoder/FP32 output head and teacher mask in both forwards.
    hidden = right_padded_hidden(model, inputs)
    logits = F.linear(hidden[selected], weight).float()
    loss = F.cross_entropy(logits, targets[selected])
    tied, = torch.autograd.grad(loss, weight)
    ordinary_logits = logits.detach()
    del hidden, logits
    output_leaf = weight.detach().clone().requires_grad_(True)
    hidden = right_padded_hidden(model, inputs)
    logits = F.linear(hidden[selected], output_leaf).float()
    split_loss = F.cross_entropy(logits, targets[selected])
    input_grad, output_grad = torch.autograd.grad(split_loss, (weight, output_leaf))
    difference = tied - (input_grad+output_grad)
    absolute_error = float(difference.abs().max())
    relative_error = float(difference.double().norm()/tied.double().norm())
    logit_error = float((ordinary_logits-logits.detach()).abs().max())
    if (not torch.isfinite(loss) or not torch.isfinite(split_loss)
            or logit_error != 0.0 or float(loss.detach()) != float(split_loss.detach())
            or absolute_error > 1e-5 or relative_error > 1e-4
            or any(p.grad is not None for p in model.parameters())):
        raise ValueError('Native logits/loss/full tied gradient must match split attribution')
    stats = gradient_statistics(input_grad, output_grad)
    stats.update(loss=float(loss.detach()), teachers=int(selected.sum()),
        EOS_teachers=int(targets.eq(3).sum()), valid_inputs=int(inputs.ne(0).sum()),
        physical_inputs=inputs.numel(), logit_max_error=logit_error,
        decomposition_max_error=absolute_error, decomposition_relative_error=relative_error)
    return stats, input_grad.detach(), output_grad.detach()


def interference_screen(sources):
    """Predeclared research screen; never a Base quality/adoption gate."""
    if set(sources) != {'web', 'textbook', 'story'}:
        raise ValueError('All three fixed TRAIN source summaries required')
    for row in sources.values():
        if not math.isfinite(row['cosine']) or not math.isfinite(row['cancellation_ratio']):
            raise ValueError('Finite actual aggregate gradients required')
    severe = [name for name, row in sources.items()
              if row['cosine'] <= -.1 and row['cancellation_ratio'] <= .9]
    return dict(severe_sources=severe,passed=len(severe)>=2,
        rule='At least two of three fixed source aggregates have cosine<=-0.1 and cancellation<=0.9',
        causal_proof=False,Base_quality_gate=False)
