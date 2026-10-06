"""Native causal attention with a single optional BOS-document restriction."""
import math
import statistics
import torch
from torch.nn import functional as F
from source_gradient_attribution import GROUPS,target_groups


def document_attention(input_ids,isolate=True):
    if input_ids.ndim!=2 or not input_ids.shape[1] or input_ids.eq(0).any():raise ValueError('Nonempty unpadded sequences required')
    length=input_ids.shape[1];positions=torch.arange(length,device=input_ids.device)[None].expand(input_ids.shape[0],-1)
    allowed=positions[:,:,None]>=positions[:,None,:]
    if isolate:
        documents=input_ids.eq(2).long().cumsum(-1)
        allowed=allowed&documents[:,:,None].eq(documents[:,None,:])
    return positions,allowed


def context_logits(model,input_ids,isolate=True):
    if model.training or input_ids.shape[1]>model.config['max_position_embeddings']:raise ValueError('Bounded eval-only native context required')
    positions,allowed=document_attention(input_ids,isolate)
    hidden=model.model.embed_tokens(input_ids)
    for layer in model.model.layers:hidden,_=layer(hidden,positions,allowed,None,causal=False)
    return model.lm_head(model.model.norm(hidden)).float()


def group_losses(logits,labels,routes):
    if logits.shape[:-1]!=labels.shape or not torch.isfinite(logits).all():raise ValueError('Matching finite group logits required')
    masks=target_groups(labels,routes)
    losses=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),labels.reshape(-1),ignore_index=-100,reduction='none').reshape_as(labels)
    if not torch.isfinite(losses).all():raise ValueError('Finite actual target NLL required')
    return {g:dict(teachers=int(m.sum()),nll_sum=float(losses[m].sum())) for g,m in masks.items()}


def all_groups(groups):
    if set(groups)!=set(GROUPS) or any(type(r['teachers'])!=int or r['teachers']<0 or not math.isfinite(r['nll_sum']) or r['nll_sum']<0 for r in groups.values()):
        raise ValueError('Complete finite five target groups required')
    result={g:dict(r) for g,r in groups.items()}
    for name,selected in [('conditional_total',GROUPS[-2:]),('all',GROUPS)]:
        result[name]=dict(teachers=sum(groups[g]['teachers'] for g in selected),nll_sum=sum(groups[g]['nll_sum'] for g in selected))
    for r in result.values():
        if not r['teachers'] and r['nll_sum']!=0:raise ValueError('Unsupported group must have zero loss mass')
        r['CE_mean']=r['nll_sum']/r['teachers'] if r['teachers'] else None
    return result


def summarize(records):
    if len(records)!=16 or [r['index'] for r in records]!=list(range(16)):raise ValueError('All16 fixed consecutive logical batches required')
    groups={}
    for name in (*GROUPS,'conditional_total','all'):
        total=sum(r['isolated_groups'][name]['teachers'] for r in records);new=old=0.;deltas=[]
        for r in records:
            a,b=r['isolated_groups'][name],r['cached_full_causal_groups'][name]
            if (a['teachers']!=b['teachers'] or any(not math.isfinite(v['nll_sum']) or v['nll_sum']<0 for v in (a,b))
                    or (a['teachers'] and (not math.isfinite(a['CE_mean']) or not math.isfinite(b['CE_mean'])))):
                raise ValueError('Paired actual group/count/finite reference required')
            new+=a['nll_sum'];old+=b['nll_sum']
            if a['teachers']:deltas.append(a['CE_mean']-b['CE_mean'])
        groups[name]=dict(teachers=total,isolated_teacher_weighted_CE=new/total if total else None,
            cached_full_teacher_weighted_CE=old/total if total else None,teacher_weighted_CE_change=(new-old)/total if total else None,
            supported_batches=len(deltas),positive_batches=sum(v>0 for v in deltas),batches_increase_at_least_point1=sum(v>=.1 for v in deltas),
            minimum_CE_change=min(deltas) if deltas else None,median_CE_change=statistics.median(deltas) if deltas else None,maximum_CE_change=max(deltas) if deltas else None)
    conditional=groups['conditional_total']
    marker=conditional['supported_batches']==16 and conditional['teacher_weighted_CE_change']>=.1 and conditional['batches_increase_at_least_point1']>=12
    return dict(groups=groups,descriptive_conditional_history_dependence_marker=marker,
        marker_definition='Conditional teacher-weighted CE increase>=.1nats and logical batches with increase>=.1nats>=12/16; local TRAIN description, not quality.')
