"""Frozen native decoder with one identity-initialized nonlinear readout.

The tied vocabulary matrix stays the exact original Parameter. Only a final
post-RMSNorm 256->192->256 bias-free SiLU residual is trainable. This can change
body-token choices and EOS, and therefore does not guarantee Web retention.
"""
import copy
import torch
from torch import nn
from torch.nn import functional as F
from jmicro.model import JMicroModel

POLICY=dict(kind='frozen_native_postnorm_silu_residual_readout_v1',bottleneck_ratio=[3,4],
    native_weights_frozen=True,up_initialization='exact_zero',down_initialization='private_normal_std_0.02',
    initialization_seed=2026100651,bias=False,dropout=0.,placement='after_final_RMSNorm_before_tied_vocabulary_matrix')


class ReadoutHead(nn.Module):
    def __init__(self,weight):
        super().__init__();self.weight=weight
        hidden=weight.shape[1]
        if hidden%4:raise ValueError('Readout hidden width must be divisible by4')
        inner=hidden*3//4
        generator=torch.Generator(device='cpu').manual_seed(POLICY['initialization_seed'])
        down=torch.empty(inner,hidden,dtype=torch.float32).normal_(0.,.02,generator=generator)
        self.down=nn.Parameter(down.to(device=weight.device,dtype=weight.dtype))
        self.up=nn.Parameter(torch.zeros(hidden,inner,device=weight.device,dtype=weight.dtype))

    def forward(self,x):
        residual=F.linear(F.silu(F.linear(x,self.down)),self.up)
        return F.linear(x+residual,self.weight)


class ReadoutAdapterModel(JMicroModel):
    def __init__(self,config):
        if config.get('readout_adapter')!=POLICY:raise ValueError('Explicit readout-adapter config required')
        native={k:v for k,v in config.items() if k!='readout_adapter'}
        super().__init__(native);self.requires_grad_(False)
        self.lm_head=ReadoutHead(self.lm_head.weight);self.config=copy.deepcopy(config)

    @classmethod
    def from_native(cls,native):
        if isinstance(native,cls) or any(k in native.config for k in ('readout_adapter','gated_shared_reuse')):
            raise ValueError('Unmodified native parent required')
        native.requires_grad_(False);result=cls.__new__(cls);nn.Module.__init__(result)
        result.config=dict(copy.deepcopy(native.config),readout_adapter=copy.deepcopy(POLICY))
        result.model=native.model;result.lm_head=ReadoutHead(native.lm_head.weight);result.train(native.training)
        return result

    def hf_reference(self):
        raise ValueError('Nonlinear readout needs dedicated export; stock tied HF/Llama cannot represent it')
