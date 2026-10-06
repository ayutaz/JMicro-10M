"""Read-only gradients and inherited AdamW first-order direction estimates."""
import math
import torch


def cosine(a,b):
    dot=torch.dot(a,b)
    denominator=torch.linalg.vector_norm(a)*torch.linalg.vector_norm(b)
    value=None if denominator.item()==0 else float(dot/denominator)
    if not torch.isfinite(dot) or (value is not None and not math.isfinite(value)):
        raise ValueError('Nonfinite gradient geometry')
    return dict(dot=float(dot),cosine=value,norm_a=float(torch.linalg.vector_norm(a)),norm_b=float(torch.linalg.vector_norm(b)))


def body_from_full(full,eos,teachers,eos_teachers):
    if not 0<eos_teachers<teachers:raise ValueError('Positive body and EOS counts required')
    return (teachers*full-eos_teachers*eos)/(teachers-eos_teachers)


def adamw_direction(parameters,gradient,saved):
    """Positive descent direction. Does not mutate parameters, moments or steps.

    Parameters and vector must use saved optimizer group order. This is a
    hypothetical quota-weighted batch, not a claimed actual training update.
    """
    norm=torch.linalg.vector_norm(gradient)
    if not torch.isfinite(norm):raise ValueError('Finite aggregate gradient required')
    clipped=gradient*min(1.,1./(float(norm)+1e-6))
    output=[];offset=0;index=0
    for group in saved['param_groups']:
        if group.get('amsgrad') or group.get('maximize'):raise ValueError('Ordinary AdamW required')
        beta1,beta2=group['betas']
        for param_id in group['params']:
            param=parameters[index];index+=1;n=param.numel()
            g=clipped[offset:offset+n].view_as(param);offset+=n
            old=saved['state'][param_id]
            if old['exp_avg'].shape!=param.shape or old['exp_avg_sq'].shape!=param.shape:
                raise ValueError('Optimizer group order differs')
            step=float(old['step'])+1
            first=old['exp_avg'].to(g.device)*beta1+g*(1-beta1)
            second=old['exp_avg_sq'].to(g.device)*beta2+g.square()*(1-beta2)
            denominator=second.sqrt()/math.sqrt(1-beta2**step)+group['eps']
            update=group['lr']/(1-beta1**step)*first/denominator
            update=update+group['lr']*group['weight_decay']*param.detach()
            output.append(update.reshape(-1))
    if index!=len(parameters) or offset!=gradient.numel():raise ValueError('Complete optimizer/vector required')
    return torch.cat(output)
