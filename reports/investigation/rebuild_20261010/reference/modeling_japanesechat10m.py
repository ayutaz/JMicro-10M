"""A randomly initialized decoder, written for this project."""
from dataclasses import dataclass, asdict
import math
import torch
from torch import nn
import torch.nn.functional as F

@dataclass
class Config:
    vocab_size:int=8192
    dim:int=288
    layers:int=8
    heads:int=6
    ff_dim:int=720
    max_seq_len:int=512
    rope_base:float=10000.0
    norm_eps:float=1e-5
    dropout:float=0.0
    seed:int=20261001
    expected_parameters:int=9995040
    def __post_init__(self):
        assert self.dim % self.heads == 0
        assert (self.dim // self.heads) % 2 == 0
    def parameter_formula(self):
        return self.vocab_size*self.dim+self.layers*(4*self.dim**2+3*self.dim*self.ff_dim+2*self.dim)+self.dim

class RMSNorm(nn.Module):
    def __init__(self, dim, eps):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(dim))
        self.eps = eps
    def forward(self, x):
        scale = torch.rsqrt(x.float().square().mean(-1, keepdim=True)+self.eps)
        return (x.float()*scale).to(x.dtype)*self.weight

class Attention(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.heads, self.hd, self.dropout = c.heads, c.dim//c.heads, c.dropout
        self.qkv = nn.Linear(c.dim, 3*c.dim, bias=False)
        self.proj = nn.Linear(c.dim, c.dim, bias=False)
        freq = 1.0/(c.rope_base**(torch.arange(0,self.hd,2).float()/self.hd))
        angle = torch.outer(torch.arange(c.max_seq_len).float(),freq)
        self.register_buffer("cos", angle.cos()[None,None,:,:], persistent=False)
        self.register_buffer("sin", angle.sin()[None,None,:,:], persistent=False)
    def rope(self,x):
        t=x.shape[-2]
        a,b=x[...,0::2],x[...,1::2]
        cos,sin=self.cos[:,:,:t].to(x.dtype),self.sin[:,:,:t].to(x.dtype)
        return torch.stack((a*cos-b*sin,a*sin+b*cos),dim=-1).flatten(-2)
    def forward(self,x):
        b,t,d=x.shape
        q,k,v=self.qkv(x).view(b,t,3,self.heads,self.hd).permute(2,0,3,1,4).unbind(0)
        q,k=self.rope(q),self.rope(k)
        y=F.scaled_dot_product_attention(q,k,v,is_causal=True,
            dropout_p=self.dropout if self.training else 0.0)
        return self.proj(y.transpose(1,2).contiguous().view(b,t,d))

class Block(nn.Module):
    def __init__(self,c):
        super().__init__()
        self.attn_norm=RMSNorm(c.dim,c.norm_eps)
        self.ff_norm=RMSNorm(c.dim,c.norm_eps)
        self.attn=Attention(c)
        self.gate_up=nn.Linear(c.dim,2*c.ff_dim,bias=False)
        self.down=nn.Linear(c.ff_dim,c.dim,bias=False)
    def forward(self,x):
        x=x+self.attn(self.attn_norm(x))
        gate,up=self.gate_up(self.ff_norm(x)).chunk(2,dim=-1)
        return x+self.down(F.silu(gate)*up)

class JapaneseLM(nn.Module):
    def __init__(self,c):
        super().__init__()
        self.config=c
        self.embed=nn.Embedding(c.vocab_size,c.dim)
        self.blocks=nn.ModuleList([Block(c) for _ in range(c.layers)])
        self.norm=RMSNorm(c.dim,c.norm_eps)
        self.apply(self._init)
        for name,p in self.named_parameters():
            if name.endswith("attn.proj.weight") or name.endswith("down.weight"):
                nn.init.normal_(p,std=0.02/math.sqrt(2*c.layers))
        count=sum(p.numel() for p in self.parameters())
        assert count==c.parameter_formula(),(count,c.parameter_formula())
        if c.expected_parameters:
            assert count==c.expected_parameters,(count,c.expected_parameters)
    @staticmethod
    def _init(module):
        if isinstance(module,(nn.Linear,nn.Embedding)):
            nn.init.normal_(module.weight,std=0.02)
    def forward(self,tokens,labels=None,reduction="mean"):
        assert tokens.shape[1]<=self.config.max_seq_len
        x=self.embed(tokens)
        for block in self.blocks:
            x=block(x)
        logits=F.linear(self.norm(x),self.embed.weight)
        loss=None
        if labels is not None:
            loss=F.cross_entropy(logits.float().reshape(-1,self.config.vocab_size),
                labels.reshape(-1),ignore_index=-100,reduction=reduction)
        return logits,loss
