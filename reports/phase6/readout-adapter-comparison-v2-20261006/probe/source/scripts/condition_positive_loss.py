"""Normalized positive-CE weighting, retaining ordinary body and EOS teachers."""
import math

import torch
import torch.nn.functional as F


def positive_weighted_ce(logits, labels, outcome_mask, factor):
    if not math.isfinite(factor) or factor < 1:
        raise ValueError('Positive outcome weight must be finite and at least one')
    if logits.shape[:-1] != labels.shape or outcome_mask.shape != labels.shape:
        raise ValueError('Matching target and outcome-mask shapes required')
    if outcome_mask.dtype != torch.bool:
        raise ValueError('Explicit boolean outcome mask required')
    valid = labels.ne(-100)
    focused = outcome_mask & valid
    if bool((focused & labels.lt(8)).any()):
        raise ValueError('Structural token targets must not be boosted')
    teacher_count = int(valid.sum())
    if teacher_count == 0:
        raise ValueError('At least one ordinary teacher required')
    focused_count = int(focused.sum())
    denominator = teacher_count + (factor - 1) * focused_count
    if factor == 1:
        loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), labels.reshape(-1),
                               ignore_index=-100, reduction='sum') / teacher_count
    else:
        losses = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), labels.reshape(-1),
                                 ignore_index=-100, reduction='none').reshape_as(labels)
        weights = valid.to(losses.dtype) + (factor - 1) * focused.to(losses.dtype)
        loss = (losses * weights).sum() / denominator
    return loss, dict(ordinary_teacher_tokens=teacher_count, outcome_focus_teacher_tokens=focused_count,
                      weighted_teacher_mass=denominator, outcome_weight=factor)
