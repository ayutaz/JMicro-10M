"""Fixed full-vocabulary smoothing of original native CE teacher positions."""
import torch
from torch.nn import functional as F

EPSILON=.1
KIND='native_original_full_CE_uniform_label_smoothing_0p1_v1'


def smoothed_teacher_loss(logits,targets,epsilon=EPSILON):
    if not 0<=epsilon<1 or logits.shape[:-1]!=targets.shape or logits.shape[-1]<2:
        raise ValueError('Matching logits/targets and epsilon in [0,1) required')
    selected=targets.ne(-100)
    if not selected.any():raise ValueError('Original nonempty teacher positions required')
    values=logits[selected].float();labels=targets[selected]
    if labels.min()<0 or labels.max()>=values.shape[-1]:raise ValueError('Original vocabulary teacher IDs required')
    logp=F.log_softmax(values,dim=-1)
    ce=F.nll_loss(logp,labels)
    uniform=-logp.mean()
    combined=ce if epsilon==0 else (1-epsilon)*ce+epsilon*uniform
    if not torch.isfinite(combined):raise ValueError('Finite original CE and uniform target loss required')
    positions=labels.numel()
    return combined,dict(CE_loss=ce,uniform_target_loss=uniform,
        original_CE_positions=positions,original_EOS_positions=int(labels.eq(3).sum()),
        weighted_original_target_mass=(1-epsilon)*positions,
        uniform_soft_target_positions=positions if epsilon else 0,
        uniform_target_mass=epsilon*positions,vocabulary_size=values.shape[-1],
        epsilon=epsilon)
