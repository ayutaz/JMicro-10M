"""Resumable packing comparison with exact, PAD-free body/EOS teacher budgets."""
import copy
import math
import numpy as np
import torch
from jmicro.shards import BlockSampler
from jmicro.low_lr_pilot import LowLRPilotTrainer


def teacher_lr(consumed,total,peak):
    if total<=0 or consumed<0 or peak<=0:raise ValueError('Invalid teacher schedule')
    progress=max(0.,min(1.,(consumed/total-.9)/.1))
    return peak*(.1+.9*(1+math.cos(math.pi*progress))/2)


class ShuffledDocumentBlocks(BlockSampler):
    """Each epoch permutes complete documents, then samples unpadded blocks."""
    def __init__(self, shard, context, seed):
        self.original = shard
        super().__init__(shard, context, seed)

    def _shuffle(self):
        order=np.random.default_rng(np.random.SeedSequence([self.seed,self.epoch,1])).permutation(len(self.original.index))
        chunks=[self.original.tokens[r['offset']:r['offset']+r['body_tokens']+2] for r in (self.original.index[int(i)] for i in order)]
        self.shard=copy.copy(self.original)
        self.shard.tokens=np.concatenate(chunks).astype('<u2',copy=False)
        super()._shuffle()

    def state_dict(self):
        return dict(super().state_dict(),mode='shuffle-whole-documents-v1')

    def load_state_dict(self,state):
        if state.get('mode')!='shuffle-whole-documents-v1':raise ValueError('Sampler differs')
        super().load_state_dict(state)


class IsolatedDocuments(BlockSampler):
    """One whole document per row. BOS input, body/EOS targets, masked PAD."""
    def __init__(self,shard,context,seed,batch=256):
        if shard.split!='train' or any(r['body_tokens']+1>context for r in shard.index):
            raise ValueError('Whole train documents must fit; never silently truncate')
        self.shard,self.context,self.seed,self.batch_size=shard,context,seed,batch
        self.blocks=len(shard.index);self.epoch=self.position=0;self._shuffle()

    def state_dict(self):
        return dict(super().state_dict(),mode='isolated-whole-documents-v1',batch=self.batch_size)

    def load_state_dict(self,state):
        if state.get('mode')!='isolated-whole-documents-v1' or state['batch']!=self.batch_size:raise ValueError('Sampler differs')
        super().load_state_dict(state)

    def batch(self,_size):
        x=np.zeros((self.batch_size,self.context),dtype=np.int64);y=np.full_like(x,-100)
        for i in range(self.batch_size):
            if self.position==self.blocks:
                self.epoch+=1;self.position=0;self._shuffle()
            r=self.shard.index[int(self.order[self.position])];self.position+=1
            ids=np.asarray(self.shard.tokens[r['offset']:r['offset']+r['body_tokens']+2],dtype=np.int64)
            if ids[0]!=2 or ids[-1]!=3:raise ValueError('Whole BOS/body/EOS boundary differs')
            x[i,:len(ids)-1]=ids[:-1];y[i,:len(ids)-1]=ids[1:]
        return torch.from_numpy(x),torch.from_numpy(y),int(self.shard.byte_lengths[np.where(y>=0,y,0)].sum())


class TeacherBudgetMixture:
    def __init__(self,web,short,mode,parent_web,goals,seed=42,isolated_batch=256):
        if mode not in ('fixed','shuffle','isolated'):raise ValueError(mode)
        self.mode=mode;self.goals=dict(goals)
        self.web=BlockSampler(web,1024,seed);self.web.load_state_dict(parent_web)
        self.short=(IsolatedDocuments(short,128,seed,isolated_batch) if mode=='isolated' else
                    ShuffledDocumentBlocks(short,1024,seed) if mode=='shuffle' else BlockSampler(short,1024,seed))
        self.position=0
        self.source_tokens=dict(web=0,short=0)
        self.source_physical_tokens=dict(web=0,short=0)
        self.source_teachers=dict(web=0,short=0)
        self.source_eos=dict(web=0,short=0)
        self.last_padding=0;self.last_source=None

    def next_source(self):
        available=[s for s in ('web','short') if self.source_teachers[s]<self.goals[s]]
        if not available:raise ValueError('Teacher budget exhausted')
        return min(available,key=lambda s:self.source_teachers[s]/self.goals[s])

    def state_dict(self):
        return dict(kind='exact-teacher-packing-study-v1',mode=self.mode,goals=self.goals,position=self.position,
                    web=self.web.state_dict(),short=self.short.state_dict(),source_tokens=self.source_tokens.copy(),
                    source_physical_tokens=self.source_physical_tokens.copy(),source_teachers=self.source_teachers.copy(),source_eos=self.source_eos.copy())

    def load_state_dict(self,state):
        if state['kind']!='exact-teacher-packing-study-v1' or state['mode']!=self.mode or state['goals']!=self.goals:
            raise ValueError('Mixture binding differs')
        self.web.load_state_dict(state['web']);self.short.load_state_dict(state['short'])
        self.position=state['position']
        for k in ('source_tokens','source_physical_tokens','source_teachers','source_eos'):
            setattr(self,k,dict(state[k]))
        if any(not 0<=self.source_teachers[s]<=self.goals[s] for s in self.goals):raise ValueError('Invalid teacher cursor')

    def batch(self,size):
        source=self.next_source();sampler=getattr(self,source);x,y,_=sampler.batch(size)
        remaining=self.goals[source]-self.source_teachers[source]
        valid=y.flatten().ne(-100).nonzero().flatten()
        if len(valid)>remaining:y.flatten()[valid[remaining:]]=-100
        count=int(y.ne(-100).sum());padding=int(x.eq(0).sum())
        self.source_teachers[source]+=count;self.source_tokens[source]+=x.numel()-padding
        self.source_physical_tokens[source]+=x.numel();self.source_eos[source]+=int(y.eq(3).sum())
        self.last_padding=padding;self.last_source=source;self.position+=1
        byte_count=int(sampler.shard.byte_lengths[np.where(y.numpy()>=0,y.numpy(),0)].sum())
        return x,y,byte_count


class PackingTrainer(LowLRPilotTrainer):
    def __init__(self,parent,web,short,mode,goals,binding,device='cuda'):
        schedule=dict(parent_update=parent['update'],stable_updates=1,decay_updates=1)
        super().__init__(parent,web,short,[True],schedule,binding,device)
        self.sampler=TeacherBudgetMixture(web,short,mode,parent['sampler'],goals,isolated_batch=binding.get('isolated_batch',256))
        self.spec['teacher_schedule']=dict(goals=goals,stable_fraction=.9,minimum_lr_ratio=.1)
        self.spec['schedule_updates']=parent['update']+100000
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:1.)
        self.scheduler.last_epoch=parent['update'];self.scheduler._step_count=parent['scheduler']['_step_count']
        self.lineage.update(kind='exact-teacher-packing-study',parent_supervised_tokens=parent['supervised_tokens'],
                            packing_mode=mode,teacher_budget=dict(goals))
        self.fast_forward=self.forward
        self._set_token_lr()

    def _set_token_lr(self):
        consumed=sum(self.sampler.source_teachers.values());total=sum(self.sampler.goals.values())
        lr=teacher_lr(consumed,total,self.pilot_binding['peak_lr'])
        for g in self.optimizer.param_groups:g['lr']=lr
        self.scheduler._last_lr=[lr]*len(self.optimizer.param_groups)
        return lr

    def step(self):
        source=self.sampler.next_source();isolated=source=='short' and self.sampler.mode=='isolated'
        saved=dict(self.spec);self._set_token_lr()
        if isolated:
            self.spec.update(sampler='document',backend='math',training_fast_path=False,context=128)
            self.forward=self.model
        try:row=super().step()
        finally:self.spec.clear();self.spec.update(saved);self.forward=self.fast_forward
        self.tokens-=self.sampler.last_padding
        row.update(tokens_seen=self.tokens,source=source,source_teachers=self.sampler.source_teachers.copy(),
                   valid_input_tokens=sum(self.sampler.source_tokens.values()),physical_input_tokens=sum(self.sampler.source_physical_tokens.values()),
                   additional_supervised_tokens=sum(self.sampler.source_teachers.values()),padding_input_tokens=self.sampler.last_padding)
        self._set_token_lr()
        if self.supervised_tokens-self.lineage['parent_supervised_tokens']!=sum(self.sampler.source_teachers.values()):
            raise ValueError('Actual teacher accounting differs')
        return row

    def load(self,path):
        super().load(path)
        self._set_token_lr()
