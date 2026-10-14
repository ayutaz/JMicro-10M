"""Residual causal projected-channel lags; frozen native decoder stays intact.

Inspired by Primer MDHA, not its reproduction: current tap is fixed1, two
preceding VALID-token taps start at zero, and SwiGLU is retained. No first-V
cross-layer path, output gate, extra attention map or input-token replacement.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, JMicroModel, KVCache, ModelOutput, rope

TAG = 'causal_QKV_lag_research'
ARMS = ('lag_learned', 'static_identity')
POLICY = dict(kind='residual_depthwise_QKV_previous2_v1', current_coefficient=1.,
    previous_lags=[1,2], coefficient='direct_signed_per_projected_channel',
    initial_previous_coefficients=0., norm_RoPE_order='project_lag_norm_RoPE',
    padding='preceding_valid_tokens_only', cache='last2_raw_QKV_and_validity',
    new_biases=0, original_FFN_unchanged=True)


def added_parameters(c):
    return 2*(c['num_attention_heads']+2*c['num_key_value_heads'])*c['head_dim']*c['num_hidden_layers']


def tagged_config(native, arm='lag_learned'):
    if (arm not in ARMS or any(k.endswith('_research') or k in
            ('gated_shared_reuse','output_probability_link') for k in native)
            or native.get('qk_norm_type') != 'none'
            or native.get('num_attention_heads') != 4 or native.get('num_key_value_heads') != 2
            or type(native.get('num_hidden_layers')) is not int or native['num_hidden_layers'] < 1
            or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Original native NoQKNorm Q4/KV2 config/count and arm required')
    result = copy.deepcopy(native)
    result[TAG] = dict(policy=copy.deepcopy(POLICY), arm=arm,
                       native_expected_parameter_count=native['expected_parameter_count'])
    result['expected_parameter_count'] += added_parameters(native)
    return result


def native_config(config):
    tag = config.get(TAG)
    if (not isinstance(tag,dict) or set(tag) != {'policy','arm','native_expected_parameter_count'}
            or tag['policy'] != POLICY or tag['arm'] not in ARMS
            or type(tag['native_expected_parameter_count']) is not int):
        raise ValueError('Exact declared causal-QKV policy/arm/native count required')
    original = copy.deepcopy(config)
    del original[TAG]
    original['expected_parameter_count'] = tag['native_expected_parameter_count']
    if tagged_config(original,tag['arm']) != config:
        raise ValueError('Declared lag coordinates or original config differ')
    return original


def mix_lags(current, weights, valid, history=None, history_valid=None, arm='lag_learned'):
    """[B,H,T,D], [H,D,2]; never count masked physical slots as past tokens."""
    if (current.ndim != 4 or valid.shape != (current.shape[0],current.shape[2])
            or valid.dtype != torch.bool or valid.device != current.device
            or weights.shape != (current.shape[1],current.shape[3],2)
            or weights.device != current.device or arm not in ARMS):
        raise ValueError('Aligned projected values, lag weights and valid mask required')
    b,h,t,d = current.shape
    if t == 0:
        raise ValueError('Nonempty projected current sequence required')
    if history is None:
        if history_valid is not None:
            raise ValueError('History validity without raw history')
        history = current.new_zeros(b,h,2,d)
        history_valid = torch.zeros(b,2,dtype=torch.bool,device=current.device)
    if (history.shape != (b,h,2,d) or history.dtype != current.dtype or history.device != current.device
            or history_valid is None or history_valid.shape != (b,2)
            or history_valid.dtype != torch.bool or history_valid.device != current.device
            or (history_valid[:,0] & ~history_valid[:,1]).any()):
        raise ValueError('Two chronological right-aligned raw history slots required')
    joined = torch.cat((history,current),dim=2)
    joined_valid = torch.cat((history_valid,valid),dim=1)
    indices = torch.arange(t+2,device=current.device)[None].expand(b,-1)
    seen = torch.where(joined_valid,indices,-torch.ones_like(indices)).cummax(1).values
    before = torch.cat((-torch.ones_like(seen[:,:1]),seen[:,:-1]),dim=1)
    previous = before[:,2:]
    older = before.gather(1,previous.clamp_min(0))
    newest = seen[:,-1:]
    tail_indices = torch.cat((before.gather(1,newest.clamp_min(0)),newest),dim=1)
    def gather(index):
        values = joined.gather(2,index.clamp_min(0)[:,None,:,None].expand(-1,h,-1,d))
        return values*index.ge(0)[:,None,:,None]
    coefficient = weights if arm == 'lag_learned' else weights*0.
    mixed = current + coefficient[...,0].to(current.dtype)[None,:,None,:]*gather(previous)
    mixed = mixed + coefficient[...,1].to(current.dtype)[None,:,None,:]*gather(older)
    return mixed, gather(tail_indices), tail_indices.ge(0)


@dataclass
class TemporalKVCache(KVCache):
    raw_projections: list[tuple[torch.Tensor,torch.Tensor,torch.Tensor]]
    raw_valid: torch.Tensor


class CausalQKVAttention(Attention):
    def __init__(self,native,arm):
        if type(native) is not Attention or arm not in ARMS:
            raise ValueError('Original native attention and explicit arm required')
        nn.Module.__init__(self)
        self.qheads,self.kvheads = native.qheads,native.kvheads
        self.dim,self.theta,self.scale = native.dim,native.theta,native.scale
        self.q_proj,self.k_proj,self.v_proj = native.q_proj,native.k_proj,native.v_proj
        self.o_proj,self.q_norm,self.k_norm = native.o_proj,native.q_norm,native.k_norm
        for name,heads in (('q_lag',self.qheads),('k_lag',self.kvheads),('v_lag',self.kvheads)):
            setattr(self,name,nn.Parameter(torch.zeros(heads,self.dim,2,
                device=self.q_proj.weight.device,dtype=self.q_proj.weight.dtype)))
        self.arm = arm
        self.train(native.training)

    def forward(self,x,positions,allowed,past,causal=False,*,raw_history=None,
                history_valid=None,return_history=False):
        b,t,_ = x.shape
        if past is not None and raw_history is None:
            raise ValueError('Tagged raw projected history required for cached attention')
        valid = torch.ones(b,t,dtype=torch.bool,device=x.device) if causal else allowed.any(-1)
        raw = [layer(x).view(b,t,heads,self.dim).transpose(1,2) for layer,heads in
               ((self.q_proj,self.qheads),(self.k_proj,self.kvheads),(self.v_proj,self.kvheads))]
        mixed,tails = [],[]
        for index,weight in enumerate((self.q_lag,self.k_lag,self.v_lag)):
            value,tail,tail_valid = mix_lags(raw[index],weight,valid,
                None if raw_history is None else raw_history[index],history_valid,self.arm)
            mixed.append(value)
            tails.append(tail)
        q = rope(self.q_norm(mixed[0]),positions,self.theta)
        k = rope(self.k_norm(mixed[1]),positions,self.theta)
        v = mixed[2]
        if past is not None:
            k,v = torch.cat((past[0],k),dim=2),torch.cat((past[1],v),dim=2)
        groups = self.qheads//self.kvheads
        attended = F.scaled_dot_product_attention(q,k.repeat_interleave(groups,dim=1),
            v.repeat_interleave(groups,dim=1),attn_mask=None if causal else allowed[:,None],
            dropout_p=0.,is_causal=causal,scale=self.scale)
        output = self.o_proj(attended.transpose(1,2).reshape(b,t,-1))
        return (output,(k,v),tuple(tails),tail_valid) if return_history else (output,(k,v))


class CausalQKVModel(JMicroModel):
    def __init__(self,config):
        original = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(original,config)

    def _take_native(self,original,config):
        if sum(p.numel() for p in original.parameters()) != config[TAG]['native_expected_parameter_count']:
            raise ValueError('Actual original parameter count differs')
        self.config = copy.deepcopy(config)
        self.model,self.lm_head = original.model,original.lm_head
        for block in self.model.layers:
            block.self_attn = CausalQKVAttention(block.self_attn,config[TAG]['arm'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Actual tagged count/tied vocabulary differs')
        self.train(original.training)

    @classmethod
    def from_native(cls,original,arm='lag_learned'):
        if (type(original) is not JMicroModel or any(p.grad is not None for p in original.parameters())
                or any(not torch.isfinite(p).all() for p in original.parameters() if not p.is_meta)):
            raise ValueError('Finite native without accumulated gradients required')
        config = tagged_config(original.config,arm)
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(original),config)
        return result

    def _blocks(self,ids,positions,allowed,cache=None,causal=False):
        x,layers,raw = self.model.embed_tokens(ids),[],[]
        for index,block in enumerate(self.model.layers):
            attention,kv,tail,tail_valid = block.self_attn(block.input_layernorm(x),positions,allowed,
                None if cache is None else cache.layers[index],causal,
                raw_history=None if cache is None else cache.raw_projections[index],
                history_valid=None if cache is None else cache.raw_valid,return_history=True)
            x = x + attention
            x = x + block.mlp(block.post_attention_layernorm(x))
            layers.append(kv)
            raw.append(tail)
        return self.model.norm(x),layers,raw,tail_valid

    def right_padded_hidden(self,ids):
        if ids.ndim != 2 or not 0 < ids.shape[1] <= self.config['max_position_embeddings']:
            raise ValueError('Nonempty context-bounded IDs required')
        positions = torch.arange(ids.shape[1],device=ids.device)[None].expand(ids.shape[0],-1)
        return self._blocks(ids,positions,None,causal=True)[0]

    def clip_grad_norm(self,max_norm,*,error_if_nonfinite=True):
        parameters = [p for n,p in self.named_parameters() if self.config[TAG]['arm'] != 'static_identity'
                      or not n.endswith(('.q_lag','.k_lag','.v_lag'))]
        return torch.nn.utils.clip_grad_norm_(parameters,max_norm,error_if_nonfinite=error_if_nonfinite)

    def forward(self,input_ids,attention_mask=None,cache=None,use_cache=False,labels=None,training_fast_path=False):
        if input_ids.ndim != 2 or input_ids.shape[1] == 0:
            raise ValueError('Expected nonempty [batch,tokens] IDs')
        if training_fast_path:
            if attention_mask is not None or cache is not None or use_cache or labels is not None:
                raise ValueError('Fast training requires unpadded blocks without cache/labels')
            return ModelOutput(self.lm_head(self.right_padded_hidden(input_ids)).float())
        valid = torch.ones_like(input_ids,dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError('Mask must match current IDs')
        if cache is not None:
            if (type(cache) is not TemporalKVCache or len(cache.layers) != len(self.model.layers)
                    or len(cache.raw_projections) != len(self.model.layers)
                    or any(not isinstance(row,(tuple,list)) or len(row) != 3 for row in cache.raw_projections)
                    or cache.valid.shape[0] != input_ids.shape[0] or cache.valid.device != input_ids.device
                    or cache.raw_valid.shape != (input_ids.shape[0],2)
                    or cache.raw_valid.dtype != torch.bool or cache.raw_valid.device != input_ids.device
                    or not torch.equal(cache.raw_valid.sum(-1),cache.valid.sum(-1).clamp_max(2))):
                raise ValueError('Tagged KV/raw-lag cache layer/batch/history mismatch')
            before = cache.valid.sum(-1)
        else:
            before = torch.zeros(input_ids.shape[0],device=input_ids.device,dtype=torch.long)
        positions = (before[:,None]+valid.long().cumsum(-1)-1).clamp_min(0)
        if ((before+valid.sum(-1)) > self.config['max_position_embeddings']).any():
            raise ValueError('Context exceeded; reprefill required')
        key_valid = valid if cache is None else torch.cat((cache.valid,valid),dim=1)
        key_positions = positions if cache is None else torch.cat((cache.positions,positions),dim=1)
        allowed = valid[:,:,None] & key_valid[:,None,:] & (key_positions[:,None,:] <= positions[:,:,None])
        hidden,layers,raw,raw_valid = self._blocks(input_ids,positions,allowed,cache)
        logits = self.lm_head(hidden).float()*valid[...,None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape or not labels[:,1:].ne(-100).any():
                raise ValueError('Labels require supervised targets in full current sequence')
            loss = F.cross_entropy(logits[:,:-1].reshape(-1,logits.shape[-1]),labels[:,1:].reshape(-1),ignore_index=-100)
        return ModelOutput(logits,TemporalKVCache(layers,key_valid,key_positions,raw,raw_valid) if use_cache else None,loss)

    def load_state_dict(self,state_dict,strict=True,assign=False):
        expected = self.state_dict()
        if (strict is not True or assign is not False or set(state_dict) != set(expected)
                or any(state_dict[k].shape != v.shape or state_dict[k].dtype != v.dtype
                       or not torch.isfinite(state_dict[k]).all() for k,v in expected.items())
                or not torch.equal(state_dict['lm_head.weight'],state_dict['model.embed_tokens.weight'])
                or (self.config[TAG]['arm'] == 'static_identity' and any(torch.count_nonzero(v)
                    for k,v in state_dict.items() if k.endswith(('.q_lag','.k_lag','.v_lag'))))):
            raise ValueError('Exact finite tagged state/tie/static coefficients required before mutation')
        return super().load_state_dict(state_dict,strict=True)

    def hf_reference(self):
        raise ValueError('Explicit causal-QKV/raw-cache inference adapter required')

    def save(self,directory):
        raise ValueError('Use typed full research checkpoints; portable export not implemented')

    @classmethod
    def load(cls,directory):
        raise ValueError('Native directory loading cannot substitute for tagged checkpoints')
