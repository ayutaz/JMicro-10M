"""Owned single-vector RMS rescaling model; native source stays frozen."""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import JMicroModel,ModelOutput,RMSNorm
from jmicro.self_rescaled_norm import (ARMS,IMPLEMENTATION,POLICY,SelfRescaledRMSNorm,
    added_parameters,extra_parameter)

TAG = 'self_rescaled_RMS_research'


def tagged_config(native,arm='self_rescaled'):
    if (arm not in ARMS or any(k.endswith('_research') for k in native)
            or any(k in native for k in ('gated_shared_reuse','output_probability_link'))
            or native.get('qk_norm_type') != 'none' or native.get('num_attention_heads') != 4
            or native.get('num_key_value_heads') != 2
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Original NoQKNorm Q4/KV2 config/count and explicit arm required')
    c = copy.deepcopy(native)
    c[TAG] = dict(policy=copy.deepcopy(POLICY),arm=arm,implementation=IMPLEMENTATION,
        native_expected_parameter_count=native['expected_parameter_count'])
    c['expected_parameter_count'] += added_parameters(native)
    return c


def native_config(tagged):
    t = tagged.get(TAG)
    if (not isinstance(t,dict) or set(t) != {'policy','arm','implementation','native_expected_parameter_count'}
            or t['policy'] != POLICY or t['implementation'] != IMPLEMENTATION or t['arm'] not in ARMS
            or type(t['native_expected_parameter_count']) is not int):
        raise ValueError('Exact self-rescaled RMS policy/runtime/arm/count required')
    c = copy.deepcopy(tagged)
    del c[TAG]
    c['expected_parameter_count'] = t['native_expected_parameter_count']
    if tagged_config(c,t['arm']) != tagged:
        raise ValueError('Exact tagged/native config roundtrip required')
    return c


@dataclass
class SelfRescaledCache:
    real: list[tuple[torch.Tensor,torch.Tensor]]
    valid: torch.Tensor
    positions: torch.Tensor
    arm: str
    implementation: str = IMPLEMENTATION


class SelfRescaledModel(JMicroModel):
    def __init__(self,config):
        original = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(original,config)

    def _take_native(self,original,config):
        if sum(p.numel() for p in original.parameters()) != config[TAG]['native_expected_parameter_count']:
            raise ValueError('Actual original native count differs')
        self.config = copy.deepcopy(config)
        self.model,self.lm_head = original.model,original.lm_head
        norms = [(name,m) for name,m in self.model.named_modules() if type(m) is RMSNorm]
        if len(norms) != 2*config['num_hidden_layers']+1:
            raise ValueError('Only original pre-attention/pre-FFN/final RMS sites required')
        for name,norm in norms:
            parent,_,field = name.rpartition('.')
            setattr(self.model.get_submodule(parent),field,SelfRescaledRMSNorm(norm,config[TAG]['arm']))
        self.register_buffer('rescale_runtime',torch.tensor([1,ARMS.index(config[TAG]['arm']),
            config['expected_parameter_count']],device=self.lm_head.weight.device,dtype=torch.long))
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Actual declared count and tied vocabulary required')
        self.train(original.training)

    @classmethod
    def from_native(cls,original,arm='self_rescaled'):
        if (type(original) is not JMicroModel or any(p.grad is not None for p in original.parameters())
                or any(not torch.isfinite(p).all() for p in original.parameters() if not p.is_meta)):
            raise ValueError('Finite original native model without accumulated gradients required')
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(original),tagged_config(original.config,arm))
        return result

    def _blocks(self,ids,positions,allowed,cache=None,causal=False):
        x,real = self.model.embed_tokens(ids),[]
        for i,block in enumerate(self.model.layers):
            out,kv = block.self_attn(block.input_layernorm.owned_forward(x),positions,allowed,
                None if cache is None else cache.real[i],causal)
            x = x+out
            x = x+block.mlp(block.post_attention_layernorm.owned_forward(x))
            real.append(kv)
        return self.model.norm.owned_forward(x),real

    def right_padded_hidden(self,ids):
        if ids.ndim != 2 or not 0 < ids.shape[1] <= self.config['max_position_embeddings']:
            raise ValueError('Original nonempty bounded physical training inputs required')
        positions = torch.arange(ids.shape[1],device=ids.device)[None].expand(ids.shape[0],-1)
        return self._blocks(ids,positions,None,causal=True)[0]

    def _validate_cache(self,c,ids):
        if (type(c) is not SelfRescaledCache or c.implementation != IMPLEMENTATION
                or c.arm != self.config[TAG]['arm'] or len(c.real) != len(self.model.layers)
                or c.valid.ndim != 2 or c.valid.shape[0] != ids.shape[0] or not c.valid.shape[1]
                or c.valid.dtype != torch.bool or c.valid.device != ids.device
                or c.positions.shape != c.valid.shape or c.positions.device != ids.device
                or c.positions.dtype != torch.long
                or not torch.equal(c.positions,(c.valid.long().cumsum(-1)-1).clamp_min(0))):
            raise ValueError('Exact self-rescaled real-cache metadata/arm/runtime required')
        shape = (ids.shape[0],self.config['num_key_value_heads'],c.valid.shape[1],self.config['head_dim'])
        for pair in c.real:
            if (not isinstance(pair,(list,tuple)) or len(pair) != 2
                    or any(t.shape != shape or t.device != ids.device or not t.is_floating_point()
                        or not torch.isfinite(t).all() for t in pair) or pair[0].dtype != pair[1].dtype):
                raise ValueError('Finite aligned real K/V required')

    def forward(self,input_ids,attention_mask=None,cache=None,use_cache=False,labels=None,training_fast_path=False):
        if input_ids.ndim != 2 or not input_ids.shape[1]:
            raise ValueError('Nonempty batch/token IDs required')
        if training_fast_path:
            if attention_mask is not None or cache is not None or use_cache or labels is not None:
                raise ValueError('Full unmasked training only')
            return ModelOutput(self.lm_head(self.right_padded_hidden(input_ids)).float())
        valid = torch.ones_like(input_ids,dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError('Current mask/IDs mismatch')
        if cache is not None:
            self._validate_cache(cache,input_ids)
        before = torch.zeros(input_ids.shape[0],device=input_ids.device,dtype=torch.long) if cache is None else cache.valid.sum(-1)
        positions = (before[:,None]+valid.long().cumsum(-1)-1).clamp_min(0)
        if ((before+valid.sum(-1)) > self.config['max_position_embeddings']).any():
            raise ValueError('Context exceeded; reprefill required')
        key_valid = valid if cache is None else torch.cat((cache.valid,valid),1)
        key_positions = positions if cache is None else torch.cat((cache.positions,positions),1)
        allowed = valid[:,:,None]&key_valid[:,None,:]&(key_positions[:,None,:] <= positions[:,:,None])
        hidden,real = self._blocks(input_ids,positions,allowed,cache)
        logits = self.lm_head(hidden).float()*valid[...,None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape or not labels[:,1:].ne(-100).any():
                raise ValueError('Full current supervised shifted labels required')
            loss = F.cross_entropy(logits[:,:-1].reshape(-1,logits.shape[-1]),labels[:,1:].reshape(-1),ignore_index=-100)
        result = SelfRescaledCache(real,key_valid,key_positions,self.config[TAG]['arm']) if use_cache else None
        return ModelOutput(logits,result,loss)

    def clip_grad_norm(self,max_norm,*,error_if_nonfinite=True):
        params = [p for n,p in self.named_parameters() if self.config[TAG]['arm'] != 'disabled_zero' or not extra_parameter(n)]
        return torch.nn.utils.clip_grad_norm_(params,max_norm,error_if_nonfinite=error_if_nonfinite)

    def load_state_dict(self,state_dict,strict=True,assign=False):
        expected = self.state_dict()
        if (strict is not True or assign is not False or set(state_dict) != set(expected)
                or any(not isinstance(state_dict[k],torch.Tensor) or state_dict[k].shape != v.shape
                    or state_dict[k].dtype != v.dtype or not torch.isfinite(state_dict[k]).all() for k,v in expected.items())
                or not torch.equal(state_dict['rescale_runtime'].cpu(),self.rescale_runtime.cpu())
                or not torch.equal(state_dict['lm_head.weight'],state_dict['model.embed_tokens.weight'])
                or (self.config[TAG]['arm'] == 'disabled_zero' and any(torch.count_nonzero(v)
                    for n,v in state_dict.items() if n.endswith('.rescale_beta')))):
            raise ValueError('Strict finite self-rescaled state/arm/tie/disabled beta required before mutation')
        return super().load_state_dict(state_dict,strict=True)

    def save(self,directory):
        raise ValueError('Typed self-rescaled research checkpoint required; native export unsupported')

    @classmethod
    def load(cls,directory):
        raise ValueError('Native directory load cannot replace self-rescaled checkpoint')

    def hf_reference(self):
        raise ValueError('Self-rescaled RMS requires its explicit inference adapter')
