"""Separate same-math dispatch; immutable generic reference stays available.

Only a causal full prefix without past/raw history has every physical slot
valid by the reference contract. Its previous-token gathers are direct shifts.
Masked and cached calls always use the original reference implementation.
"""
import torch
from torch import nn
from torch.nn import functional as F

from jmicro.causal_qkv import ARMS,CausalQKVAttention,CausalQKVModel
from jmicro.model import rope

IMPLEMENTATION = 'same_math_causal_full_prefix_contiguous_shift_v1'


def contiguous_lags(current,weights,arm='lag_learned'):
    if (current.ndim != 4 or current.shape[2] == 0 or arm not in ARMS
            or weights.shape != (current.shape[1],current.shape[3],2)
            or weights.device != current.device):
        raise ValueError('Nonempty full prefix, aligned channel lags and arm required')
    t=current.shape[2]
    coefficient=weights if arm=='lag_learned' else weights*0.
    # Both lag branches MUST share the same joined tensor as the reference.
    # Independent pad branches change gradient addition grouping/rounding.
    joined=torch.cat((current.new_zeros(current.shape[0],current.shape[1],2,current.shape[3]),current),dim=2)
    previous=joined[:,:,1:t+1]
    older=joined[:,:,:t]
    mixed=current+coefficient[...,0].to(current.dtype)[None,:,None,:]*previous
    mixed=mixed+coefficient[...,1].to(current.dtype)[None,:,None,:]*older
    tail=joined[:,:,-2:]
    valid=(torch.arange(2,device=current.device)[None]>=max(2-t,0)).expand(current.shape[0],-1)
    return mixed,tail,valid


class ContiguousCausalAttention(CausalQKVAttention):
    def __init__(self,reference):
        if type(reference) is not CausalQKVAttention:
            raise ValueError('Exact immutable reference attention required')
        nn.Module.__init__(self)
        self.qheads,self.kvheads=reference.qheads,reference.kvheads
        self.dim,self.theta,self.scale=reference.dim,reference.theta,reference.scale
        self.q_proj,self.k_proj,self.v_proj=reference.q_proj,reference.k_proj,reference.v_proj
        self.o_proj,self.q_norm,self.k_norm=reference.o_proj,reference.q_norm,reference.k_norm
        self.q_lag,self.k_lag,self.v_lag=reference.q_lag,reference.k_lag,reference.v_lag
        self.arm=reference.arm
        self.train(reference.training)

    def forward(self,x,positions,allowed,past,causal=False,*,raw_history=None,
                history_valid=None,return_history=False):
        if not (causal and allowed is None and past is None and raw_history is None and history_valid is None):
            return super().forward(x,positions,allowed,past,causal,raw_history=raw_history,
                                   history_valid=history_valid,return_history=return_history)
        b,t,_=x.shape
        projected=[linear(x).view(b,t,heads,self.dim).transpose(1,2) for linear,heads in
                   ((self.q_proj,self.qheads),(self.k_proj,self.kvheads),(self.v_proj,self.kvheads))]
        mixed,tails=[],[]
        for current,weight in zip(projected,(self.q_lag,self.k_lag,self.v_lag),strict=True):
            value,tail,valid=contiguous_lags(current,weight,self.arm)
            mixed.append(value)
            tails.append(tail)
        q=rope(self.q_norm(mixed[0]),positions,self.theta)
        k=rope(self.k_norm(mixed[1]),positions,self.theta)
        v=mixed[2]
        groups=self.qheads//self.kvheads
        attended=F.scaled_dot_product_attention(q,k.repeat_interleave(groups,dim=1),
            v.repeat_interleave(groups,dim=1),attn_mask=None,dropout_p=0.,is_causal=True,scale=self.scale)
        out=self.o_proj(attended.transpose(1,2).reshape(b,t,-1))
        return (out,(k,v),tuple(tails),valid) if return_history else (out,(k,v))


class ContiguousCausalQKVModel(CausalQKVModel):
    def _take_native(self,original,config):
        super()._take_native(original,config)
        for layer in self.model.layers:
            layer.self_attn=ContiguousCausalAttention(layer.self_attn)
        if sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']:
            raise ValueError('Same-math dispatch must not change parameter topology')
