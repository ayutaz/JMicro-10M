"""Independent rank8 Q/K attention branch, zero-coefficient native conversion.

This adds learned projection coordinates rather than permuting native heads.
Original model/tensors remain intact. Not a Differential Transformer replica.
"""
import copy
from dataclasses import dataclass

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import Attention, JMicroModel, ModelOutput, rope

TAG = 'independent_QK_map_research'
ARMS = ('independent_learned', 'disabled_zero')
IMPLEMENTATION = 'independent_rank8_QK_two_original_SDPA_real_K2_cache_v1'
POLICY = dict(kind='independent_rank8_QK_signed_tanh_map_v1', rank=8,
    secondary='shared_new_down_then_independent_Q2_K2_up_original_RoPE',
    output='original_map_minus_tanh_raw_per_head_times_independent_map_on_original_V',
    initial_raw=0., projection_initialization='original_std_CPU_fork_seed42_plus_layer',
    original_weight_rescaling=False, new_head_norm=False, original_labels_unchanged=True,
    native_initial_function_preserved=True)


def added_parameters(c):
    return c['num_hidden_layers']*(8*(c['hidden_size']+
        (c['num_attention_heads']+c['num_key_value_heads'])*c['head_dim'])+c['num_attention_heads'])


def extra_parameter(name):
    return any(part in name for part in ('.independent_raw', '.independent_down.',
                                        '.independent_q.', '.independent_k.'))


def tagged_config(native, arm='independent_learned'):
    if (arm not in ARMS or any(k.endswith('_research') for k in native)
            or any(k in native for k in ('gated_shared_reuse', 'output_probability_link'))
            or native.get('qk_norm_type') != 'none' or native.get('num_attention_heads') != 4
            or native.get('num_key_value_heads') != 2 or type(native.get('expected_parameter_count')) is not int
            or native['expected_parameter_count'] <= 0):
        raise ValueError('Original NoQKNorm Q4/KV2 native config/count and explicit arm required')
    c = copy.deepcopy(native)
    c[TAG] = dict(policy=copy.deepcopy(POLICY), arm=arm, implementation=IMPLEMENTATION,
                  native_expected_parameter_count=native['expected_parameter_count'])
    c['expected_parameter_count'] += added_parameters(native)
    return c


def native_config(config):
    tag = config.get(TAG)
    if (not isinstance(tag, dict) or set(tag) != {'policy','arm','implementation','native_expected_parameter_count'}
            or tag['policy'] != POLICY or tag['implementation'] != IMPLEMENTATION or tag['arm'] not in ARMS
            or type(tag['native_expected_parameter_count']) is not int):
        raise ValueError('Exact independent rank8 map runtime/arm/count required')
    c = copy.deepcopy(config)
    del c[TAG]
    c['expected_parameter_count'] = tag['native_expected_parameter_count']
    if tagged_config(c, tag['arm']) != config:
        raise ValueError('Exact tagged/native architecture roundtrip required')
    return c


def independent_map_attention(q, k, v, q2, k2, raw, *, mask=None, causal=False,
                              scale=None, arm='independent_learned'):
    if (any(t.ndim != 4 for t in (q,k,v,q2,k2)) or q.shape != q2.shape or k.shape != k2.shape
            or k.shape != v.shape or q.shape[:2] != k.shape[:2] or q.shape[-1] != k.shape[-1]
            or raw.shape != (q.shape[1],) or arm not in ARMS or (causal and mask is not None)
            or any(t.device != q.device or t.dtype != q.dtype for t in (k,v,q2,k2))):
        raise ValueError('Aligned independent Q/K maps and original V required')
    a = F.scaled_dot_product_attention(q, k, v, attn_mask=mask, dropout_p=0., is_causal=causal, scale=scale)
    b = F.scaled_dot_product_attention(q2, k2, v, attn_mask=mask, dropout_p=0., is_causal=causal, scale=scale)
    coefficient = raw.tanh()
    if arm == 'disabled_zero':
        coefficient = coefficient*0.
    return a-coefficient.to(a.dtype)[None, :, None, None]*b


@dataclass
class IndependentMapCache:
    # Deliberately no native .layers: frozen native code cannot silently drop K2.
    primary: list[tuple[torch.Tensor, torch.Tensor]]
    secondary: list[torch.Tensor]
    valid: torch.Tensor
    positions: torch.Tensor
    arm: str
    implementation: str = IMPLEMENTATION


class IndependentMapAttention(Attention):
    def __init__(self, original, arm, index, std):
        if type(original) is not Attention or arm not in ARMS:
            raise ValueError('Original attention and explicit independent map arm required')
        nn.Module.__init__(self)
        for name in ('qheads','kvheads','dim','theta','scale','q_proj','k_proj','v_proj','o_proj','q_norm','k_norm'):
            setattr(self, name, getattr(original, name))
        self.arm = arm
        self.independent_raw = nn.Parameter(torch.zeros(self.qheads, device=self.q_proj.weight.device,
                                                        dtype=self.q_proj.weight.dtype))
        with torch.random.fork_rng(devices=[]):
            generator = torch.Generator(device='cpu').manual_seed(42+index)
            down = nn.Linear(self.q_proj.in_features, 8, bias=False, device='cpu')
            q = nn.Linear(8, self.qheads*self.dim, bias=False, device='cpu')
            k = nn.Linear(8, self.kvheads*self.dim, bias=False, device='cpu')
            for layer in (down, q, k): nn.init.normal_(layer.weight, std=std, generator=generator)
        self.independent_down, self.independent_q, self.independent_k = [
            p.to(device=self.q_proj.weight.device, dtype=self.q_proj.weight.dtype) for p in (down,q,k)]
        self.train(original.training)

    def forward(self, *args, **kwargs):
        raise ValueError('Independent K2 cache/training requires explicit model-owned traversal')

    def owned_forward(self, x, positions, allowed, past, past_secondary, causal=False):
        if (past is None) != (past_secondary is None):
            raise ValueError('Original KV and independent K2 history must be paired')
        batch, length, _ = x.shape
        def project(layer, source, heads):
            return layer(source).view(batch,length,heads,self.dim).transpose(1,2)
        q = rope(self.q_norm(project(self.q_proj,x,self.qheads)),positions,self.theta)
        k = rope(self.k_norm(project(self.k_proj,x,self.kvheads)),positions,self.theta)
        v = project(self.v_proj,x,self.kvheads)
        u = self.independent_down(x)
        q2 = rope(project(self.independent_q,u,self.qheads),positions,self.theta)
        k2 = rope(project(self.independent_k,u,self.kvheads),positions,self.theta)
        if past is not None:
            k,v = torch.cat((past[0],k),2),torch.cat((past[1],v),2)
            k2 = torch.cat((past_secondary,k2),2)
        groups = self.qheads//self.kvheads
        attended = independent_map_attention(q,k.repeat_interleave(groups,1),v.repeat_interleave(groups,1),
            q2,k2.repeat_interleave(groups,1),self.independent_raw,
            mask=None if causal else allowed[:,None],causal=causal,scale=self.scale,arm=self.arm)
        return self.o_proj(attended.transpose(1,2).reshape(batch,length,-1)),(k,v),k2


class IndependentMapModel(JMicroModel):
    def __init__(self, config):
        source = JMicroModel(native_config(config))
        nn.Module.__init__(self)
        self._take_native(source, config)

    def _take_native(self, source, config):
        if sum(p.numel() for p in source.parameters()) != config[TAG]['native_expected_parameter_count']:
            raise ValueError('Actual original native count differs')
        self.config = copy.deepcopy(config)
        self.model,self.lm_head = source.model,source.lm_head
        for i,block in enumerate(self.model.layers):
            block.self_attn = IndependentMapAttention(block.self_attn,config[TAG]['arm'],i,config['initializer_std'])
        if (sum(p.numel() for p in self.parameters()) != config['expected_parameter_count']
                or self.lm_head.weight is not self.model.embed_tokens.weight):
            raise ValueError('Actual count and tied original vocabulary required')
        self.train(source.training)

    @classmethod
    def from_native(cls, original, arm='independent_learned'):
        if (type(original) is not JMicroModel or any(p.grad is not None for p in original.parameters())
                or any(not torch.isfinite(p).all() for p in original.parameters() if not p.is_meta)):
            raise ValueError('Finite original native model without accumulated gradients required')
        result = cls.__new__(cls)
        nn.Module.__init__(result)
        result._take_native(copy.deepcopy(original),tagged_config(original.config,arm))
        return result

    def _blocks(self, ids, positions, allowed, cache=None, causal=False):
        x,primary,secondary = self.model.embed_tokens(ids),[],[]
        for i,block in enumerate(self.model.layers):
            out,kv,k2 = block.self_attn.owned_forward(block.input_layernorm(x),positions,allowed,
                None if cache is None else cache.primary[i],None if cache is None else cache.secondary[i],causal)
            x = x+out
            x = x+block.mlp(block.post_attention_layernorm(x))
            primary.append(kv)
            secondary.append(k2)
        return self.model.norm(x),primary,secondary

    def right_padded_hidden(self, ids):
        if ids.ndim != 2 or not 0 < ids.shape[1] <= self.config['max_position_embeddings']:
            raise ValueError('Original nonempty bounded physical inputs required')
        positions = torch.arange(ids.shape[1],device=ids.device)[None].expand(ids.shape[0],-1)
        return self._blocks(ids,positions,None,causal=True)[0]

    def _validate_cache(self, c, ids):
        if (type(c) is not IndependentMapCache or c.implementation != IMPLEMENTATION
                or c.arm != self.config[TAG]['arm'] or len(c.primary) != len(self.model.layers)
                or len(c.secondary) != len(self.model.layers) or c.valid.ndim != 2
                or c.valid.shape[0] != ids.shape[0] or c.valid.shape[1] == 0
                or c.valid.dtype != torch.bool or c.valid.device != ids.device
                or c.positions.shape != c.valid.shape or c.positions.dtype != torch.long
                or c.positions.device != ids.device
                or not torch.equal(c.positions,(c.valid.long().cumsum(-1)-1).clamp_min(0))):
            raise ValueError('Exact independent real-cache metadata/arm/runtime required')
        shape = (ids.shape[0],self.config['num_key_value_heads'],c.valid.shape[1],self.config['head_dim'])
        for pair,k2 in zip(c.primary,c.secondary,strict=True):
            if (not isinstance(pair,(list,tuple)) or len(pair) != 2 or any(
                    p.shape != shape or p.device != ids.device or not p.is_floating_point()
                    or not torch.isfinite(p).all() for p in (*pair,k2))
                    or any(p.dtype != pair[0].dtype for p in (*pair,k2))):
                raise ValueError('Finite aligned original KV plus real K2 required')

    def forward(self,input_ids,attention_mask=None,cache=None,use_cache=False,labels=None,training_fast_path=False):
        if input_ids.ndim != 2 or input_ids.shape[1] == 0:
            raise ValueError('Nonempty batch/token IDs required')
        if training_fast_path:
            if attention_mask is not None or cache is not None or use_cache or labels is not None:
                raise ValueError('Full unmasked training only')
            return ModelOutput(self.lm_head(self.right_padded_hidden(input_ids)).float())
        valid = torch.ones_like(input_ids,dtype=torch.bool) if attention_mask is None else attention_mask.bool()
        if valid.shape != input_ids.shape:
            raise ValueError('Current mask/IDs mismatch')
        if cache is not None: self._validate_cache(cache,input_ids)
        before = torch.zeros(input_ids.shape[0],device=input_ids.device,dtype=torch.long) if cache is None else cache.valid.sum(-1)
        positions = (before[:,None]+valid.long().cumsum(-1)-1).clamp_min(0)
        if ((before+valid.sum(-1)) > self.config['max_position_embeddings']).any():
            raise ValueError('Context exceeded; reprefill required')
        key_valid = valid if cache is None else torch.cat((cache.valid,valid),1)
        key_positions = positions if cache is None else torch.cat((cache.positions,positions),1)
        allowed = valid[:,:,None]&key_valid[:,None,:]&(key_positions[:,None,:] <= positions[:,:,None])
        hidden,primary,secondary = self._blocks(input_ids,positions,allowed,cache)
        logits = self.lm_head(hidden).float()*valid[...,None]
        loss = None
        if labels is not None:
            if cache is not None or labels.shape != input_ids.shape or not labels[:,1:].ne(-100).any():
                raise ValueError('Full current supervised shifted labels required')
            loss = F.cross_entropy(logits[:,:-1].reshape(-1,logits.shape[-1]),labels[:,1:].reshape(-1),ignore_index=-100)
        result = IndependentMapCache(primary,secondary,key_valid,key_positions,self.config[TAG]['arm']) if use_cache else None
        return ModelOutput(logits,result,loss)

    def clip_grad_norm(self,max_norm,*,error_if_nonfinite=True):
        params = [p for n,p in self.named_parameters() if self.config[TAG]['arm'] != 'disabled_zero' or not extra_parameter(n)]
        return torch.nn.utils.clip_grad_norm_(params,max_norm,error_if_nonfinite=error_if_nonfinite)

    def load_state_dict(self,state_dict,strict=True,assign=False):
        expected = self.state_dict()
        if (strict is not True or assign is not False or set(state_dict) != set(expected)
                or any(state_dict[k].shape != v.shape or state_dict[k].dtype != v.dtype
                       or not torch.isfinite(state_dict[k]).all() for k,v in expected.items())
                or not torch.equal(state_dict['lm_head.weight'],state_dict['model.embed_tokens.weight'])
                or (self.config[TAG]['arm'] == 'disabled_zero' and any(torch.count_nonzero(v)
                    for k,v in state_dict.items() if k.endswith('.independent_raw')))):
            raise ValueError('Strict finite independent state/tie/disabled coefficient required before mutation')
        return super().load_state_dict(state_dict,strict=True)

    def hf_reference(self):
        raise ValueError('Independent QK map and real K2 require their explicit inference adapter')

    def save(self,directory):
        raise ValueError('Typed research checkpoint required; portable export not implemented')

    @classmethod
    def load(cls,directory):
        raise ValueError('Native directory load cannot replace an independent-map checkpoint')
