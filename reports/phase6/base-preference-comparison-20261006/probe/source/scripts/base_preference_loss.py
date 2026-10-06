"""Role-free Base continuation log probabilities and fixed-reference DPO loss."""
import math
import torch
from torch.nn import functional as F


def collate_continuations(pairs, device='cpu'):
    """Original prompt/BOS are context only; each completion includes its own EOS."""
    sequences=[]; labels=[]
    for completion in ('chosen_ids','rejected_ids'):
        for row in pairs:
            prompt=row['prompt_ids']; body=row[completion]
            if (not prompt or prompt[0]!=2 or any(type(v) is not int or v<8 for v in prompt[1:])
                    or not body or any(type(v) is not int or v<8 and not(v==3 and i==len(body)-1) for i,v in enumerate(body))):
                raise ValueError('Base BOS/body/final optional EOS only; no role tokens')
            ids=prompt+body
            if len(ids)>1024: raise ValueError('Full original continuation exceeds context')
            sequences.append(ids[:-1]); labels.append([-100]*(len(prompt)-1)+body)
    width=max(map(len,sequences)); n=len(sequences)
    x=torch.zeros((n,width),dtype=torch.long,device=device); y=torch.full_like(x,-100); mask=torch.zeros_like(x,dtype=torch.bool)
    for i,(ids,targets) in enumerate(zip(sequences,labels,strict=True)):
        x[i,:len(ids)]=torch.tensor(ids,device=device); y[i,:len(targets)]=torch.tensor(targets,device=device); mask[i,:len(ids)]=True
    return x,y,mask


def continuation_logps(logits, targets):
    if logits.ndim!=3 or targets.shape!=logits.shape[:2]: raise ValueError('Already shifted logits/target shapes differ')
    mask=targets.ne(-100); counts=mask.sum(-1)
    if not bool((counts>0).all()): raise ValueError('Each row needs real completion teachers')
    scores=logits.float().log_softmax(-1).gather(-1,targets.clamp_min(0).unsqueeze(-1)).squeeze(-1)
    return (scores*mask).sum(-1),counts


def dpo_loss(policy_chosen, policy_rejected, reference_chosen, reference_rejected, beta=.1):
    arrays=(policy_chosen,policy_rejected,reference_chosen,reference_rejected)
    if (not math.isfinite(beta) or beta<=0 or policy_chosen.ndim!=1 or not len(policy_chosen)
            or any(a.shape!=policy_chosen.shape or not bool(torch.isfinite(a).all()) for a in arrays)
            or reference_chosen.requires_grad or reference_rejected.requires_grad):
        raise ValueError('Finite equal paired sequence sums and frozen reference required')
    margin=(policy_chosen-policy_rejected)-(reference_chosen-reference_rejected)
    return -F.logsigmoid(beta*margin).mean(),margin
