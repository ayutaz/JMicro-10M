"""Tentative source updates commit only at a finite MATH loss block boundary."""
import copy
import math
from pathlib import Path
import time
import torch
from jmicro.experiment import sha256
from jmicro.training import rng_state,restore_rng,synchronize
from finite_Web_constraint import FiniteWebTrainer,COUNTERS,constrain
from interleaved_outcome_trainer import InterleavedOutcomeTrainer

KIND='finite_Web_body_NLL_at_20_update_transaction_boundaries_v1'


class BlockWebTrainer(FiniteWebTrainer):
    def __init__(self,*args,block_updates=20,**kwargs):
        if type(block_updates) is not int or block_updates<=0:raise ValueError('Positive fixed block updates required')
        super().__init__(*args,**kwargs);self._hook.remove()
        self.block_updates=block_updates
        self.spec.update(research_kind=KIND,block_Web_trainer_sha256=sha256(Path(__file__)),block_updates=block_updates,
            finite_constraint_scope='Accepted block boundary only; tentative internal updates are not bounded/committed/saved.',
            projected_updates_field_counts_blocks=True)
        self.lineage.update(kind=KIND,source_sampler_policy='Same original staged source order and mask; transaction at fixed20 boundaries.')
        self.auxiliary['accepted_blocks']=0

    def step(self):raise RuntimeError('Use block(): an internal source update is not an accepted boundary')

    def block(self,check=lambda:None):
        if self._transaction is not None or self.sampler.source_teachers==self.sampler.goals:
            raise RuntimeError('No nested/empty block')
        synchronize(self.device);started=time.perf_counter()
        snapshot=dict(weights=[p.detach().clone() for p in self.model.parameters()],
            optimizer=copy.deepcopy(self.optimizer.state_dict()),scheduler=copy.deepcopy(self.scheduler.state_dict()),
            sampler=copy.deepcopy(self.sampler.state_dict()),rng=rng_state(),counters={k:getattr(self,k) for k in COUNTERS},
            oracle=copy.deepcopy(self.oracle.stats),optimizer_called=getattr(self.optimizer,'_opt_called',None),
            training=self.model.training,auxiliary=copy.deepcopy(self.auxiliary),last_constraint=copy.deepcopy(self.last_constraint),
            sampler_ephemeral={k:copy.deepcopy(getattr(self.sampler,k)) for k in ('last_genres','last_reference') if hasattr(self.sampler,k)})
        self._transaction=snapshot;rows=[]
        try:
            for _ in range(self.block_updates):
                if self.sampler.source_teachers==self.sampler.goals:break
                check();rows.append(InterleavedOutcomeTrainer.step(self))
            check();decision=constrain(list(self.model.parameters()),snapshot['weights'],self.oracle,self.reference_ce);check()
            if not decision['accepted'] or decision['final_body_NLL']>self.reference_ce*1.01:raise RuntimeError('Cannot commit unbounded boundary')
            self.last_constraint=dict(decision,scope='accepted_block_boundary_only',block_start_update=snapshot['counters']['update'],
                block_end_update=self.update,block_source_updates=len(rows))
            self.auxiliary.update(self.oracle.stats);self.auxiliary['accepted_blocks']+=1
            self.auxiliary['accepted_updates']+=len(rows)
            self.auxiliary['projected_updates']+=int(decision['projected']);self.auxiliary['backtracked_updates']+=int(decision['backtracked'])
            for row in rows:
                row.update(block_boundary_index=self.auxiliary['accepted_blocks'],block_boundary_update=self.update,
                    constraint_valid_only_at_block_boundary=True,boundary_constraint=copy.deepcopy(self.last_constraint))
            synchronize(self.device);rows[-1]['block_GPU_seconds']=time.perf_counter()-started
            rows[-1]['accepted_auxiliary']=copy.deepcopy(self.auxiliary)
            self.audit_auxiliary();return rows
        except BaseException as error:
            attempted=sum(self.sampler.actual['teachers'].values())-sum(snapshot['sampler']['prefix_mask_accounting']['actual']['teachers'].values())
            rejected=dict(error=repr(error),decision=copy.deepcopy(getattr(error,'decision',None)),
                attempted_source_gradient_teacher_tokens=attempted,attempted_source_updates=len(rows),
                auxiliary_completed_calls={k:self.oracle.stats[k]-snapshot['oracle'][k] for k in self.oracle.stats},
                restored_last_completed_update=snapshot['counters']['update'],rollback_scope='entire_tentative_block')
            with torch.no_grad():
                for p,w in zip(self.model.parameters(),snapshot['weights'],strict=True):p.copy_(w)
            self.optimizer.load_state_dict(snapshot['optimizer']);self.scheduler.load_state_dict(snapshot['scheduler']);self.sampler.load_state_dict(snapshot['sampler'])
            for k in ('last_genres','last_reference'):
                if k in snapshot['sampler_ephemeral']:setattr(self.sampler,k,snapshot['sampler_ephemeral'][k])
                elif hasattr(self.sampler,k):delattr(self.sampler,k)
            for k,v in snapshot['counters'].items():setattr(self,k,v)
            self.oracle.stats=copy.deepcopy(snapshot['oracle']);self.auxiliary=copy.deepcopy(snapshot['auxiliary']);self.last_constraint=copy.deepcopy(snapshot['last_constraint'])
            self.optimizer.zero_grad(set_to_none=True);self.model.train(snapshot['training'])
            if snapshot['optimizer_called'] is None:
                if hasattr(self.optimizer,'_opt_called'):delattr(self.optimizer,'_opt_called')
            else:self.optimizer._opt_called=snapshot['optimizer_called']
            restore_rng(snapshot['rng']);self.audit_counters();self.last_rejection=rejected;raise
        finally:self._transaction=None

    def audit_auxiliary(self):
        super().audit_auxiliary()
        if (self.auxiliary['accepted_blocks']!=math.ceil(self.auxiliary['accepted_updates']/self.block_updates)
                or self.auxiliary['projected_updates']>self.auxiliary['accepted_blocks']):
            raise ValueError('Accepted block ledger differs')
