"""Exact EOS-mass/conditional-vocabulary decomposition of parent-to-student KL."""
import torch


def decompose(parent_logits, student_logits, labels, eos=3):
    if parent_logits.shape != student_logits.shape or labels.shape != parent_logits.shape[:-1]:
        raise ValueError('Same logits and shifted labels required')
    mask = labels >= 8
    if not mask.any():
        raise ValueError('Body target positions required')
    p_log = parent_logits.double().log_softmax(-1)[mask]
    q_log = student_logits.double().log_softmax(-1)[mask]
    p = p_log.exp()
    keep = torch.arange(p.shape[-1], device=p.device) != eos
    p_other = p_log[:, keep].logsumexp(-1)
    q_other = q_log[:, keep].logsumexp(-1)
    eos_mass_KL = p[:, eos] * (p_log[:, eos] - q_log[:, eos]) + p_other.exp() * (p_other - q_other)
    conditional_KL = (p[:, keep] * ((p_log[:, keep] - p_other[:, None]) - (q_log[:, keep] - q_other[:, None]))).sum(-1)
    full_KL = (p * (p_log - q_log)).sum(-1)
    derivative = q_log[:, eos].exp() - p[:, eos]
    result = dict(full_KL=full_KL, EOS_mass_KL=eos_mass_KL, weighted_conditional_non_EOS_KL=conditional_KL,
        parent_EOS_probability=p[:, eos], student_EOS_probability=q_log[:, eos].exp(), EOS_logit_KL_derivative=derivative)
    if any(not torch.isfinite(v).all() for v in result.values()):
        raise ValueError('Finite probability decomposition required')
    if (full_KL - eos_mass_KL - conditional_KL).abs().max().item() > 1e-9:
        raise ValueError('KL chain-rule identity differs')
    return result
