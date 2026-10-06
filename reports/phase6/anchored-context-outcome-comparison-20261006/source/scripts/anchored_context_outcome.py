"""Conditional non-EOS positive likelihood on the same TRAIN paired outcome logits."""
import torch
from torch.nn import functional as F

POLICY=dict(kind='train_gold_outcome_non_EOS_positive_CE_anchor_v1',coefficient=1.,
    gold_rows='For each existing4-row family: branch0-candidate0 and branch1-candidate1 only.',
    objective='Sum gold-body conditional nonEOS token NLL divided by actual positive body token count.',
    vocabulary='Remove EOS3 only; retain all other vocabulary IDs. Prefix/padding ignored; complete body labels>=8.',
    exposure='Reuse the existing8x256 paired logits/input/labels, no extra forward/data/window; gold positions become separately counted hard teachers.',
    update='Ranking and positive anchor combined in one backward; ordinaryCE,WebKL,combined pair gradients precede one clip/Adam/scheduler update.')


def anchored_outcome_loss(logits,labels):
    if (logits.shape[:-1]!=labels.shape or labels.ndim!=2 or labels.shape[0]%4
            or logits.shape[-1]<=8 or labels.dtype!=torch.long
            or ((labels!=-100)&(labels<8)).any() or (labels>=logits.shape[-1]).any()):
        raise ValueError('Complete4-row TRAIN families and body labels required')
    body=labels>=8;counts=body.sum(-1)
    if (counts==0).any():raise ValueError('Every candidate body must contain scored tokens')
    keep=torch.arange(logits.shape[-1],device=logits.device)!=3
    targets=torch.where(body,labels-1,-100)
    nll=F.cross_entropy(logits.float()[...,keep].reshape(-1,logits.shape[-1]-1),
        targets.reshape(-1),ignore_index=-100,reduction='none').reshape(labels.shape)
    scores=-(nll.sum(-1)/counts).reshape(-1,2,2)
    gold=torch.stack((scores[:,0,0],scores[:,1,1]),-1)
    foil=torch.stack((scores[:,0,1],scores[:,1,0]),-1)
    ranking=F.softplus(foil-gold).mean()
    row=torch.arange(labels.shape[0],device=labels.device)%4
    positive=(row==0)|(row==3)
    positive_count=counts[positive].sum()
    anchor=nll[positive].sum()/positive_count
    combined=ranking+anchor
    if not torch.isfinite(combined):raise ValueError('Finite ranking and absolute positive loss required')
    count_grid=counts.reshape(-1,2,2)
    return combined,ranking,anchor,dict(relational_choice_labels=labels.shape[0]//2,candidate_rows=labels.shape[0],
        gold_body_scored_positions=int(count_grid[:,0,0].sum()+count_grid[:,1,1].sum()),
        foil_body_scored_positions=int(count_grid[:,0,1].sum()+count_grid[:,1,0].sum()),
        ignored_prefix_padding_positions=labels.numel()-int(body.sum()),
        ordinary_CE_teacher_tokens=0,soft_target_body_positions=0,
        positive_anchor_body_teacher_tokens=int(positive_count),
        positive_anchor_ignored_positions=labels.numel()-int(positive_count))
