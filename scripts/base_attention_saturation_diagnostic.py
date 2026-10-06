"""Observe native causal attention concentration without changing its forward."""
from contextlib import contextmanager
import math

import torch
from torch.nn import functional as F
from jmicro.model import rope


def attention_statistics(q,k,targets,scale):
    if (q.ndim!=4 or k.ndim!=4 or q.shape[0]!=k.shape[0] or q.shape[2:]!=k.shape[2:]
            or q.shape[1]%k.shape[1] or targets.shape!=(q.shape[0],q.shape[2])
            or not torch.isfinite(q).all() or not torch.isfinite(k).all()):
        raise ValueError('Finite matching uncached native Q/K and teacher mask required')
    batch,heads,length,dim=q.shape
    k=k.repeat_interleave(heads//k.shape[1],dim=1)
    position=torch.arange(length,device=q.device)
    allowed=position[:,None]>=position[None,:]
    scores=(q@k.transpose(-1,-2))*scale
    probability=F.softmax(scores.masked_fill(~allowed,float('-inf')),dim=-1)
    entropy=-(probability*probability.clamp_min(torch.finfo(probability.dtype).tiny).log()).sum(-1)
    denominator=(position+1).float().log().clamp_min(1e-8)
    normalized=entropy/denominator
    peak,winner=probability.max(-1)
    eligible=targets.ne(-100)&(position[None]>=15)
    recent=(position[:,None]-position[None,:])<8
    distant=(position[:,None]-position[None,:])>=16
    saturated=(peak>=.98)&(normalized<=.05)
    per_head=[]
    for head in range(heads):
        pick=eligible
        count=int(pick.sum())
        p=probability[:,head]
        selected_saturated=saturated[:,head]&pick
        selected_winner=winner[:,head]
        row=dict(head=head,eligible_queries=count,saturated_queries=int(selected_saturated.sum()),
            saturated_to_BOS=int((selected_saturated&selected_winner.eq(0)).sum()),
            saturated_to_recent_non_BOS=int((selected_saturated&selected_winner.ne(0)&
                (position[None]-selected_winner<8)).sum()),
            saturated_to_other=int((selected_saturated&selected_winner.ne(0)&
                (position[None]-selected_winner>=8)).sum()),
            entropy_nats_sum=float(entropy[:,head][pick].double().sum()),
            normalized_entropy_sum=float(normalized[:,head][pick].double().sum()),
            maximum_probability_sum=float(peak[:,head][pick].double().sum()),
            BOS_mass_sum=float(p[:,:,0][pick].double().sum()),
            recent8_mass_sum=float((p*recent).sum(-1)[pick].double().sum()),
            distant16_mass_sum=float((p*distant).sum(-1)[pick].double().sum()),
            query_norm_sum=float(q[:,head].norm(dim=-1)[pick].double().sum()),
            key_norm_sum=float(k[:,head].norm(dim=-1)[pick].double().sum()))
        if row['saturated_queries']!=sum(row[key] for key in ('saturated_to_BOS','saturated_to_recent_non_BOS','saturated_to_other')):
            raise ValueError('Every saturated query destination must be classified')
        per_head.append(row)
    return per_head


@contextmanager
def observe_attention(model,targets):
    if model.training or any(p.grad is not None for p in model.parameters()):
        raise ValueError('Unchanged eval model without accumulated grads required')
    captured=[];handles=[]
    try:
        for layer,block in enumerate(model.model.layers):
            def hook(module,args,kwargs,layer=layer):
                x,positions,allowed,past=args[:4]
                causal=kwargs.get('causal',args[4] if len(args)>4 else False)
                if past is not None or not causal or x.shape[:2]!=targets.shape:
                    raise ValueError('Uncached native right-padded causal diagnostic required')
                batch,length,_=x.shape
                def project(projection,heads):
                    return projection(x).view(batch,length,heads,module.dim).transpose(1,2)
                q=rope(module.q_norm(project(module.q_proj,module.qheads)),positions,module.theta)
                k=rope(module.k_norm(project(module.k_proj,module.kvheads)),positions,module.theta)
                captured.append(dict(layer=layer,heads=attention_statistics(q,k,targets,module.scale)))
                # Observation hook returns None; native attention forward remains intact.
            handles.append(block.self_attn.register_forward_pre_hook(hook,with_kwargs=True))
        yield captured
    finally:
        for handle in handles:handle.remove()


def aggregate(records,layers):
    out=[]
    for layer in range(layers):
        heads=[]
        head_count=len(records[0]['heads'])
        for head in range(head_count):
            selected=[r['heads'][head] for r in records if r['layer']==layer]
            if not selected:raise ValueError('All fixed layers/heads required')
            row={key:sum(r[key] for r in selected) for key in selected[0] if key!='head'}
            n=row['eligible_queries']
            if n<=0:raise ValueError('At least16 causal keys in fixed diagnostic required')
            row.update(head=head,saturated_fraction=row['saturated_queries']/n,
                normalized_entropy_mean=row['normalized_entropy_sum']/n,
                maximum_probability_mean=row['maximum_probability_sum']/n)
            heads.append(row)
        n=sum(h['eligible_queries'] for h in heads)
        saturated=sum(h['saturated_queries'] for h in heads)
        out.append(dict(layer=layer,heads=heads,eligible_head_queries=n,saturated_head_queries=saturated,
            saturated_fraction=saturated/n,marker=saturated/n>=.25))
    return dict(layers=out,marked_layers=sum(r['marker'] for r in out),
        total_layers=layers,eligible_head_queries=sum(r['eligible_head_queries'] for r in out),
        saturated_head_queries=sum(r['saturated_head_queries'] for r in out))


def broad_screen(sources):
    if set(sources)!={'web','textbook','story'}:raise ValueError('All fixed three sources required')
    marked=[name for name,row in sources.items() if row['marked_layers']>=math.ceil(row['total_layers']/2)]
    return dict(passed=len(marked)>=2,marked_sources=marked,
        rule='pmax>=.98 AND entropy/log(causal_keys)<=.05, at least16 causal keys; >=25percent eligible head-queries in >=half all layers, >=two of three fixed sources',
        causal_proof=False,Base_quality_gate=False,
        caution='Sharp specialized heads and attention sinks can be functional. This local concentration screen does not establish training entropy collapse, unused context, necessity or success of normalization.')
