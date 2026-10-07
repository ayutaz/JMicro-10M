"""Matched reparameterized mixture arms, original gold CE and committed full state."""
import copy
import math
from pathlib import Path

import torch
from jmicro.training import restore_rng
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from base_output_mixture_model import ARMS, POLICY, TAG, OutputMixtureModel

KIND = 'original_CE_matched_context_or_probability_output_mixture_v1'
OPT_KIND = 'fresh_all_parameter_AdamW_same_output_matrices_v1'
OPT_POLICY = dict(lr=1e-5,weight_decay=.1,betas=(.9,.999),eps=1e-8)


def finite_tree(value):
    if isinstance(value,torch.Tensor):return bool(torch.isfinite(value).all())
    if isinstance(value,float):return math.isfinite(value)
    if isinstance(value,dict):return all(finite_tree(v) for v in value.values())
    if isinstance(value,(tuple,list)):return all(finite_tree(v) for v in value)
    return True


class OutputMixtureTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,arm,batch=48,device='cuda',seed=42):
        if arm not in ARMS or type(sampler) is not OriginalTrainCorpusSampler:
            raise ValueError('Explicit matched mixture arm and unchanged full original TRAIN sampler required')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        self.model = OutputMixtureModel.from_native(self.model,arm)
        self.optimizer = torch.optim.AdamW(self.model.parameters(),**OPT_POLICY)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:1.)
        self.spec.update(kind=KIND,mixture_arm=arm,mixture_policy=copy.deepcopy(POLICY),
            model_class=type(self.model).__name__,optimizer_policy=OPT_KIND,
            optimizer_recipe=copy.deepcopy(OPT_POLICY),
            actual_unique_parameters=sum(p.numel() for p in self.model.parameters()))
        self.lineage.update(kind=KIND,mixture_arm=arm,optimizer_policy=OPT_KIND,
            native_parent_model_config=copy.deepcopy(parent['model_config']),
            mixture_initialization=copy.deepcopy(POLICY),original_parent_optimizer_reused=False)
        self._step_in_progress = False

    def state_recipe(self,key):
        return KIND if key=='kind' else self.model.config if key=='model_config' else getattr(self,key)

    def validate_committed(self,state):
        try:
            if any(state[k]!=self.state_recipe(k) for k in ('kind','spec','binding','lineage','model_config')):
                raise ValueError('Mixture recipe/arm/parent/source/config differs')
            c,sampler,schedule,opt = (state[k] for k in ('counters','sampler','scheduler','optimizer'))
            steps,tokens = c['update'],c['supervised_tokens']
            if (type(steps) is not int or steps<0 or type(tokens) is not int or tokens<0
                    or (steps==0)!=(tokens==0)
                    or tokens!=sum(c['source_teachers'].values())
                    or c['source_teachers']!=sampler['consumed']
                    or c['auxiliary_input_tokens'] or c['auxiliary_pairs']
                    or c['auxiliary_digest']!='0'*64
                    or not c['physical_input_tokens']>=c['CE_input_tokens']>=tokens
                    or any(type(n) is not int or not 0<=n<=self.sampler.goals[k]
                           for k,n in c['source_teachers'].items())
                    or set(c['source_teachers'])!=set(self.sampler.goals)
                    or any(type(n) is not int or not 0<=n<=c['source_teachers'][k]
                           for k,n in c['source_EOS'].items())
                    or set(c['source_EOS'])!=set(self.sampler.goals)
                    or schedule['last_epoch']!=steps or schedule['_step_count']!=steps+1
                    or schedule['base_lrs']!=[1e-5] or schedule['_last_lr']!=[1e-5]):
                raise ValueError('Completed mixture update/source/constant-scheduler counters differ')
            recipe = self.sampler.state_dict()
            if any(sampler[k]!=recipe[k] for k in ('kind','binding','seed','goals')):
                raise ValueError('Full original sampler recipe differs')
            actual = self.model.state_dict()
            if (set(actual)!=set(state['model']) or any(
                    not isinstance(v,torch.Tensor) or actual[k].shape!=v.shape or actual[k].dtype!=v.dtype
                    for k,v in state['model'].items())
                    or not torch.equal(state['model']['lm_head.weight'],state['model']['model.embed_tokens.weight'])):
                raise ValueError('Exact finite mixture shapes/vocabulary tie required')
            if len(opt['param_groups'])!=1:
                raise ValueError('Single all-parameter AdamW group required')
            group = opt['param_groups'][0]
            parameters = list(self.model.parameters());identifiers = group['params']
            if (len(identifiers)!=len(parameters) or len(set(identifiers))!=len(identifiers)
                    or any(type(k) is not int for k in identifiers)
                    or any(group[k]!=v for k,v in OPT_POLICY.items())
                    or group['initial_lr']!=1e-5
                    or set(opt['state'])!=(set(identifiers) if steps else set())):
                raise ValueError('Exact once-counted all-parameter fresh AdamW policy required')
            if steps:
                for identifier,parameter in zip(identifiers,parameters,strict=True):
                    moments = opt['state'][identifier]
                    if (set(moments)!={'step','exp_avg','exp_avg_sq'}
                            or not isinstance(moments['step'],torch.Tensor) or moments['step'].ndim!=0
                            or float(moments['step'])!=steps
                            or any(not isinstance(moments[k],torch.Tensor)
                                or moments[k].shape!=parameter.shape or moments[k].dtype!=parameter.dtype
                                for k in ('exp_avg','exp_avg_sq'))
                            or (moments['exp_avg_sq']<0).any()):
                        raise ValueError('Each mixture/native Adam tensor must match completed update')
            if not finite_tree(state):
                raise ValueError('Finite full mixture checkpoint required')
        except (KeyError,TypeError,AttributeError,RuntimeError,OverflowError) as exc:
            raise ValueError('Malformed committed mixture state') from exc

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save a partial mixture update; restore last valid checkpoint')
        state = super().state_dict();state['kind'] = KIND
        self.validate_committed(state)
        return state

    def load(self,path):
        state = torch.load(Path(path),map_location=self.device,weights_only=False)
        self.validate_committed(state)
        self._step_in_progress = True
        self.model.load_state_dict(state['model'],strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress or not self.model.training:
            raise ValueError('Valid committed mixture train state required')
        self._step_in_progress = True
        row = super().step()
        if self.scheduler.last_epoch!=self.counters['update']:
            raise ValueError('Completed mixture update/scheduler mismatch')
        self._step_in_progress = False
        row.update(mixture_arm=self.spec['mixture_arm'],mixture_policy=POLICY['kind'],committed_update=True)
        return row
