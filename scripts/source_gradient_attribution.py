"""Partition the unchanged token-mean CE; gradients never update a model."""
import itertools
import math
import torch
from torch.nn import functional as F

GROUPS=('web','story','ordinary_textbook','conditional_outcome_body','conditional_EOS')


def target_groups(labels,routes):
    if labels.ndim!=2 or len(routes)!=labels.shape[0]:raise ValueError('One actual source route per sequence required')
    masks={g:torch.zeros_like(labels,dtype=torch.bool) for g in GROUPS}
    for i,source in enumerate(routes):
        if source=='conditional_textbook':
            if (labels[i].ne(-100)&labels[i].lt(8)&labels[i].ne(3)).any():raise ValueError('Only outcome body and original EOS allowed')
            masks['conditional_outcome_body'][i]=labels[i].ge(8)
            masks['conditional_EOS'][i]=labels[i].eq(3)
        elif source in GROUPS[:3]:masks[source][i]=labels[i].ne(-100)
        else:raise ValueError('Actual source route unknown')
    validate_partition(labels,masks)
    return masks


def validate_partition(labels,masks):
    if set(masks)!=set(GROUPS) or any(m.shape!=labels.shape or m.dtype!=torch.bool for m in masks.values()):
        raise ValueError('All five exact boolean target groups required')
    coverage=sum(m.to(torch.int8) for m in masks.values())
    if not torch.equal(coverage,labels.ne(-100).to(torch.int8)):raise ValueError('Disjoint exhaustive actual teacher groups required')


def unique_parameters(parameters):
    seen=set();result=[]
    for p in parameters:
        if not p.requires_grad:continue
        if id(p) not in seen:result.append(p);seen.add(id(p))
    if not result or any(p.grad is not None for p in result):raise ValueError('Unique learned parameters without accumulated gradients required')
    return result


def gradients(logits,labels,masks,parameters,teacher_denominator):
    """A microbatch uses the complete logical batch's teacher denominator."""
    validate_partition(labels,masks);parameters=unique_parameters(parameters)
    count=int(labels.ne(-100).sum())
    if type(teacher_denominator)!=int or teacher_denominator<count or count<=0:raise ValueError('Positive complete logical teacher count required')
    if logits.shape[:-1]!=labels.shape or not torch.isfinite(logits).all():raise ValueError('Matching finite logits required')
    losses=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),labels.reshape(-1),ignore_index=-100,reduction='none').reshape_as(labels)
    size=sum(p.numel() for p in parameters);output={};counts={};nll={}
    for name in GROUPS:
        mask=masks[name];counts[name]=int(mask.sum());nll[name]=float(losses[mask].sum().detach())
        if not counts[name]:output[name]=torch.zeros(size,device=logits.device,dtype=parameters[0].dtype)
        else:
            terms=torch.autograd.grad(losses[mask].sum()/teacher_denominator,parameters,retain_graph=True,allow_unused=False)
            output[name]=torch.cat([v.reshape(-1) for v in terms])
    # Independent reduction, not a sum of the previously partitioned losses.
    full=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),labels.reshape(-1),ignore_index=-100,reduction='sum')/teacher_denominator
    terms=torch.autograd.grad(full,parameters,retain_graph=False,allow_unused=False)
    output['independent_total']=torch.cat([v.reshape(-1) for v in terms])
    if any(not torch.isfinite(v).all() for v in output.values()) or any(p.grad is not None for p in parameters):
        raise ValueError('Finite read-only autograd gradients required')
    return output,counts,nll


def readonly_checks(model,before):
    current=model.state_dict()
    return dict(weights_unchanged=set(current)==set(before) and all(torch.equal(v.detach().cpu(),before[k]) for k,v in current.items()),
        no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training,
        finite_weights=all(torch.isfinite(v).all().item() for v in current.values()))


def describe(vectors,counts,nll,tolerance):
    if (set(vectors)!=set(GROUPS)|{'independent_total'} or set(counts)!=set(GROUPS) or set(nll)!=set(GROUPS)
            or not math.isfinite(tolerance) or not 0<tolerance<=.02
            or any(type(n)!=int or n<0 for n in counts.values()) or not sum(counts.values())
            or any(not math.isfinite(n) or n<0 for n in nll.values())):raise ValueError('Complete finite attribution required')
    if len({v.shape for v in vectors.values()})!=1 or any(v.ndim!=1 or not torch.isfinite(v).all() for v in vectors.values()):
        raise ValueError('Common finite unique-parameter vectors required')
    total=vectors['independent_total'];norm=torch.linalg.vector_norm(total)
    summed=sum(vectors[g] for g in GROUPS);error=torch.linalg.vector_norm(summed-total)
    relative=float(error/norm) if norm.item()!=0 else (0. if error.item()==0 else math.inf)
    if relative>tolerance:raise ValueError(f'Gradient decomposition relative L2 error {relative} exceeds {tolerance}')
    expanded=dict(vectors,conditional_total=vectors['conditional_outcome_body']+vectors['conditional_EOS'])
    counts=dict(counts,conditional_total=counts['conditional_outcome_body']+counts['conditional_EOS'],independent_total=sum(counts.values()))
    nll=dict(nll,conditional_total=nll['conditional_outcome_body']+nll['conditional_EOS'],independent_total=sum(nll.values()))
    total_count=counts['independent_total'];groups={};pairs={}
    for name,v in expanded.items():
        vnorm=float(torch.linalg.vector_norm(v));fraction=counts[name]/total_count
        groups[name]=dict(teachers=counts[name],teacher_fraction=fraction,CE_mean=nll[name]/counts[name] if counts[name] else None,
            contribution_gradient_norm=vnorm,group_mean_gradient_norm=vnorm/fraction if fraction else None,
            contribution_to_total_squared_norm=float(torch.dot(v,total)/norm.square()) if norm.item()!=0 else None)
        if not counts[name] and (vnorm!=0 or nll[name]!=0):raise ValueError('Unsupported source must have exact zero contribution')
    for a,b in itertools.combinations(expanded,2):
        va,vb=expanded[a],expanded[b];na=torch.linalg.vector_norm(va);nb=torch.linalg.vector_norm(vb);dot=float(torch.dot(va,vb))
        pairs[a+'__'+b]=dict(dot=dot,cosine=dot/float(na*nb) if na.item()!=0 and nb.item()!=0 else None)
    return dict(groups=groups,pairs=pairs,decomposition_relative_L2_error=relative,decomposition_tolerance=tolerance,
        unique_parameter_elements=total.numel(),total_teacher_count=total_count,
        sum_source_total_squared_norm_contributions=sum(groups[g]['contribution_to_total_squared_norm'] for g in GROUPS) if norm.item()!=0 else None)
