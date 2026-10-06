"""One finite TRAIN body-loss constraint, with transactional source updates."""
import copy
import math
import os
from pathlib import Path
import time
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import sha256
from jmicro.training import atomic_json,implementation_hashes,rng_state,restore_rng,synchronize
from interleaved_outcome_trainer import InterleavedOutcomeTrainer,InterleavedOutcomeSampler
from historical_parent_condition_trainer import historical_web_cursor

KIND='finite_original_Web_TRAIN_body_NLL_constraint_projection_v1'
COUNTERS=('update','tokens','supervised_tokens','body_bytes','token_digest','focus_token_digest',
          'focus_teacher_tokens','weighted_teacher_mass')
BACKTRACKS=(.5,.25,.125)


class ConstraintRejected(RuntimeError):
    def __init__(self,decision):
        self.decision=copy.deepcopy(decision)
        super().__init__('Finite TRAIN Web constraint rejected the entire source update')


class BodyOracle:
    """Same fixed body labels in every call; no parameter .grad/RNG mutation."""
    def __init__(self,model,memory,microbatch=8):
        self.model=model;self.parameters=list(model.parameters());self.microbatch=microbatch
        device=next(model.parameters()).device
        self.x=memory['x'].to(device);self.y=memory['y'].clone().to(device)
        self.y[self.y.lt(8)]=-100
        if (self.x.ndim!=2 or self.y.shape!=self.x.shape or self.x.eq(0).any()
                or any(p.dtype!=torch.float32 or not p.requires_grad for p in self.parameters)):
            raise ValueError('Unpadded native FP32 trainable model and exact memory shapes required')
        self.teachers=int(self.y.ne(-100).sum());self.physical=int(self.x.numel())
        if not self.teachers or microbatch<=0:raise ValueError('Positive memory body support required')
        self.stats=dict(forward_only_calls=0,gradient_calls=0,teacher_observations=0,
            gradient_teacher_tokens=0,physical_input_tokens=0)
        self.last_seconds=0.

    def measure(self,gradient=False):
        synchronize(self.x.device);started=time.perf_counter();training=self.model.training
        self.model.eval();total=0.;gradients=[torch.zeros_like(p) for p in self.parameters] if gradient else None
        try:
            with sdpa_kernel(SDPBackend.MATH),torch.autocast(device_type=self.x.device.type,enabled=False),\
                    (torch.enable_grad() if gradient else torch.no_grad()):
                for begin in range(0,len(self.x),self.microbatch):
                    x=self.x[begin:begin+self.microbatch];y=self.y[begin:begin+self.microbatch]
                    logits=self.model(x,training_fast_path=True).logits
                    loss=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),y.reshape(-1),ignore_index=-100,reduction='sum')/self.teachers
                    if not bool(torch.isfinite(loss)):raise ValueError('Nonfinite actual memory body NLL')
                    total+=float(loss.detach())
                    if gradient:
                        values=torch.autograd.grad(loss,self.parameters)
                        for accumulator,value in zip(gradients,values,strict=True):accumulator.add_(value.detach())
                    del logits,loss
            if not math.isfinite(total) or total<0:raise ValueError('Finite memory body NLL required')
            if gradient and any(not bool(torch.isfinite(g).all()) for g in gradients):raise ValueError('Nonfinite memory gradient')
            self.stats['gradient_calls' if gradient else 'forward_only_calls']+=1
            self.stats['teacher_observations']+=self.teachers;self.stats['physical_input_tokens']+=self.physical
            if gradient:self.stats['gradient_teacher_tokens']+=self.teachers
            return total,gradients
        finally:
            self.model.train(training);synchronize(self.x.device);self.last_seconds=time.perf_counter()-started


def constrain(parameters,before,oracle,reference):
    if (not math.isfinite(reference) or reference<=0 or len(parameters)!=len(before)
            or len({id(p) for p in parameters})!=len(parameters)):
        raise ValueError('Fixed positive reference and unique native weights required')
    limit=reference*1.01;value,_=oracle.measure()
    decision=dict(reference_body_NLL=reference,ceiling_body_NLL=limit,proposed_body_NLL=value,
        projected=False,backtracked=False,trials=[dict(kind='Adam',body_NLL=value)],accepted=False)
    if value<=limit:
        decision.update(accepted=True,scale=1.,final_body_NLL=value);return decision
    value,gradient=oracle.measure(gradient=True)
    norm2=sum(float(g.double().square().sum()) for g in gradient)
    if not math.isfinite(norm2) or norm2<=0:
        decision.update(error='Nonfinite or zero memory gradient norm',gradient_norm_squared=norm2)
        raise ConstraintRejected(decision)
    coefficient=(value-limit+reference*1e-5)/norm2
    if not math.isfinite(coefficient) or coefficient<=0:
        decision.update(error='Invalid fixed finite projection coefficient');raise ConstraintRejected(decision)
    with torch.no_grad():
        for p,g in zip(parameters,gradient,strict=True):p.add_(g,alpha=-coefficient)
    del gradient
    decision.update(projected=True,gradient_body_NLL=value,gradient_norm_squared=norm2,projection_coefficient=coefficient)
    value,_=oracle.measure();decision['trials'].append(dict(kind='projected',scale=1.,body_NLL=value))
    if value<=limit:
        decision.update(accepted=True,scale=1.,final_body_NLL=value);return decision
    delta=[p.detach()-w for p,w in zip(parameters,before,strict=True)]
    for scale in BACKTRACKS:
        with torch.no_grad():
            for p,w,d in zip(parameters,before,delta,strict=True):p.copy_(w).add_(d,alpha=scale)
        value,_=oracle.measure();decision['trials'].append(dict(kind='backtracked',scale=scale,body_NLL=value))
        if value<=limit:
            decision.update(accepted=True,backtracked=True,scale=scale,final_body_NLL=value);return decision
    decision.update(error='All four corrected finite proposals violate fixed memory bound')
    raise ConstraintRejected(decision)


class FiniteWebTrainer(InterleavedOutcomeTrainer):
    def __init__(self,parent,pool,original,positive,goals,binding,memory,memory_binding,
                 reference_ce=None,device='cuda',context=1024,batch=32):
        super().__init__(parent,pool,original,positive,goals,binding,device,context,batch)
        self.sampler=InterleavedOutcomeSampler(pool,original,positive,historical_web_cursor(parent),goals,
            context,42,reference_policy='staged')
        self.sampler.reference_token_digest=parent['token_digest']
        self.lineage.update(kind=KIND,actual_initial_reference_sampler=copy.deepcopy(self.sampler.initial_reference),
            source_sampler_policy='Original full staged order, fixed outcome mask; finite TRAIN memory constraint after Adam proposal.',
            memory_binding=copy.deepcopy(memory_binding),additional_memory_supervision_separately_counted=True)
        self.oracle=BodyOracle(self.model,memory,8 if device=='cuda' else min(2,len(memory['x'])))
        self.reference_ce=self.oracle.measure()[0] if reference_ce is None else reference_ce
        if not math.isfinite(self.reference_ce) or self.reference_ce<=0:raise ValueError('Positive finite original reference required')
        self.setup_oracle_counts=copy.deepcopy(self.oracle.stats)
        self.oracle.stats={k:0 for k in self.oracle.stats}
        self.auxiliary=dict(self.oracle.stats,projected_updates=0,backtracked_updates=0,accepted_updates=0)
        self.last_constraint=dict(reference_body_NLL=self.reference_ce,ceiling_body_NLL=self.reference_ce*1.01,
            final_body_NLL=self.reference_ce,accepted=True,initial=True)
        self.last_rejection=None;self._transaction=None
        self.spec.update(research_kind=KIND,finite_Web_trainer_sha256=sha256(Path(__file__)),
            reference_body_NLL=self.reference_ce,memory_binding=copy.deepcopy(memory_binding),
            memory_dtype='fp32',memory_backend='math',memory_microbatch=self.oracle.microbatch,
            ceiling_multiplier=1.01,projection_interior_margin_relative=1e-5,backtracks=list(BACKTRACKS))
        self._hook=self.optimizer.register_step_post_hook(self._after_Adam)
        self.audit_counters()

    def _after_Adam(self,optimizer,args,kwargs):
        if self._transaction is None:raise RuntimeError('Transactional source update required')
        self._decision=constrain(list(self.model.parameters()),self._transaction['weights'],self.oracle,self.reference_ce)

    def step(self):
        synchronize(self.device);started=time.perf_counter()
        if self._transaction is not None:raise RuntimeError('Nested source proposal is forbidden')
        snapshot=dict(weights=[p.detach().clone() for p in self.model.parameters()],
            optimizer=copy.deepcopy(self.optimizer.state_dict()),scheduler=copy.deepcopy(self.scheduler.state_dict()),
            sampler=copy.deepcopy(self.sampler.state_dict()),rng=rng_state(),
            counters={k:getattr(self,k) for k in COUNTERS},oracle=copy.deepcopy(self.oracle.stats),
            optimizer_called=getattr(self.optimizer,'_opt_called',None),training=self.model.training,
            sampler_ephemeral={k:copy.deepcopy(getattr(self.sampler,k)) for k in ('last_genres','last_reference') if hasattr(self.sampler,k)})
        self._transaction=snapshot
        try:
            row=super().step()
            if not self._decision['accepted'] or self._decision['final_body_NLL']>self.reference_ce*1.01:
                raise RuntimeError('Unaccepted update cannot commit')
            self.last_constraint=copy.deepcopy(self._decision)
            self.auxiliary.update(self.oracle.stats)
            self.auxiliary['accepted_updates']+=1
            self.auxiliary['projected_updates']+=int(self.last_constraint['projected'])
            self.auxiliary['backtracked_updates']+=int(self.last_constraint['backtracked'])
            row.update(constraint=copy.deepcopy(self.last_constraint),auxiliary=copy.deepcopy(self.auxiliary))
            synchronize(self.device);row['seconds']=time.perf_counter()-started
            row['tokens_per_second']=self.spec['batch']*self.spec['context']/row['seconds']
            return row
        except BaseException as error:
            proposed_actual=self.sampler.actual['teachers']
            before_actual=snapshot['sampler']['prefix_mask_accounting']['actual']['teachers']
            rejected=dict(error=repr(error),decision=copy.deepcopy(getattr(error,'decision',None)),
                attempted_source_gradient_teacher_tokens=sum(proposed_actual.values())-sum(before_actual.values()),
                auxiliary_completed_calls={k:self.oracle.stats[k]-snapshot['oracle'][k] for k in self.oracle.stats},
                incomplete_oracle_call_not_counted=isinstance(error,ValueError),restored_last_completed_update=snapshot['counters']['update'])
            with torch.no_grad():
                for p,w in zip(self.model.parameters(),snapshot['weights'],strict=True):p.copy_(w)
            self.optimizer.load_state_dict(snapshot['optimizer']);self.scheduler.load_state_dict(snapshot['scheduler'])
            self.sampler.load_state_dict(snapshot['sampler'])
            for k in ('last_genres','last_reference'):
                if k in snapshot['sampler_ephemeral']:setattr(self.sampler,k,snapshot['sampler_ephemeral'][k])
                elif hasattr(self.sampler,k):delattr(self.sampler,k)
            for k,v in snapshot['counters'].items():setattr(self,k,v)
            self.oracle.stats=copy.deepcopy(snapshot['oracle'])
            self.optimizer.zero_grad(set_to_none=True);self.model.train(snapshot['training'])
            if snapshot['optimizer_called'] is None:
                if hasattr(self.optimizer,'_opt_called'):delattr(self.optimizer,'_opt_called')
            else:self.optimizer._opt_called=snapshot['optimizer_called']
            restore_rng(snapshot['rng']);self.audit_counters();self.last_rejection=rejected
            raise
        finally:self._transaction=None

    def save(self,path):
        self.audit_counters();started=time.perf_counter()
        self.audit_auxiliary()
        if (self._transaction is not None or not self.last_constraint['accepted']
                or self.last_constraint['final_body_NLL']>self.reference_ce*1.01):
            raise ValueError('Only accepted completed updates may be saved')
        path.parent.mkdir(parents=True,exist_ok=True)
        state=dict(version=2,spec=self.spec,model_config=self.model.config,model=self.model.state_dict(),
            optimizer=self.optimizer.state_dict(),scheduler=self.scheduler.state_dict(),rng=rng_state(),
            sampler=self.sampler.state_dict(),**{k:getattr(self,k) for k in COUNTERS},
            shard_manifest_sha256=sha256(self.shard.directory/'manifest.json'),implementation_sha256=implementation_hashes(),
            study_implementation_sha256=sha256(Path(__file__)),study_binding=self.binding,pilot_binding=self.pilot_binding,
            lineage=self.lineage,auxiliary=copy.deepcopy(self.auxiliary),last_constraint=copy.deepcopy(self.last_constraint),
            branch_updates=self.update-self.lineage['parent_update'],branch_tokens=self.tokens-self.lineage['parent_tokens'])
        temporary=path.with_suffix('.tmp')
        with temporary.open('wb') as stream:
            torch.save(state,stream);stream.flush();os.fsync(stream.fileno())
        os.replace(temporary,path)
        atomic_json(path.parent/'latest.json',dict(path=str(path.resolve()),sha256=sha256(path),update=self.update,tokens_seen=self.tokens))
        return time.perf_counter()-started

    def load(self,path):
        state=torch.load(path,map_location='cpu',weights_only=False)
        if (state['spec']!=self.spec or state['study_binding']!=self.binding or state['lineage']!=self.lineage
                or state['implementation_sha256']!=implementation_hashes() or state['study_implementation_sha256']!=sha256(Path(__file__))
                or state['shard_manifest_sha256']!=sha256(self.shard.directory/'manifest.json') or state['model_config']!=self.model.config):
            raise ValueError('Finite Web recipe/packet/source identity differs')
        self.model.load_state_dict(state['model'],strict=True);self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler']);self.sampler.load_state_dict(state['sampler'])
        for k in COUNTERS:setattr(self,k,state[k])
        self.auxiliary=copy.deepcopy(state['auxiliary']);self.last_constraint=copy.deepcopy(state['last_constraint'])
        self.oracle.stats={k:self.auxiliary[k] for k in self.oracle.stats}
        self.audit_auxiliary()
        if (not self.last_constraint['accepted'] or self.last_constraint['reference_body_NLL']!=self.reference_ce
                or self.last_constraint['ceiling_body_NLL']!=self.reference_ce*1.01
                or self.last_constraint['final_body_NLL']>self.reference_ce*1.01):raise ValueError('Accepted finite boundary accounting differs')
        self.audit_counters();restore_rng(state['rng'])

    def audit_auxiliary(self):
        a=self.auxiliary;calls=a['forward_only_calls']+a['gradient_calls']
        if (any(type(v) is not int or v<0 for v in a.values())
                or a['accepted_updates']!=self.update-self.lineage['parent_update']
                or a['projected_updates']!=a['gradient_calls'] or a['backtracked_updates']>a['projected_updates']
                or a['projected_updates']>a['accepted_updates']
                or a['teacher_observations']!=calls*self.oracle.teachers
                or a['gradient_teacher_tokens']!=a['gradient_calls']*self.oracle.teachers
                or a['physical_input_tokens']!=calls*self.oracle.physical):
            raise ValueError('Accepted source/auxiliary teacher and physical accounting differs')
