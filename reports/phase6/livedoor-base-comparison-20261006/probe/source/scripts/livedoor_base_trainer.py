"""Native full-CE continuation: actual cached Web cursor, fresh TRAIN news stream."""
import copy
import math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import torch
from jmicro.experiment import sha256
from jmicro.shards import BlockSampler
from jmicro.training import Trainer,implementation_hashes,restore_rng
from condition_positive_trainer import ConditionPositiveTrainer
from original_web_retention_trainer import OriginalWebStream

KIND='authored_Japanese_news_vs_synthetic_native_Base100M_v1'
LR=.00001
SOURCE_ORDER=('web','authored_news')


class NewsBlockStream:
    def __init__(self,view,context,seed):
        self.sampler=BlockSampler(view,context,seed);self.manifest_sha256=sha256(view.directory/'manifest.json')

    def block(self,context):
        if context!=self.sampler.context:raise ValueError('News context differs')
        x,y,_=self.sampler.batch(1)
        return x[0].numpy().copy(),y[0].numpy().copy()

    def state_dict(self):return dict(kind='fresh_authored_news_contiguous_block_shuffle_v1',manifest_sha256=self.manifest_sha256,sampler=self.sampler.state_dict())

    def load_state_dict(self,state):
        if state['kind']!=self.state_dict()['kind'] or state['manifest_sha256']!=self.manifest_sha256:raise ValueError('News source binding differs')
        self.sampler.load_state_dict(state['sampler'])


class NewsQuotaSampler:
    def __init__(self,web,news,cursor,goals,context=1024,seed=42):
        if set(goals)!=set(SOURCE_ORDER) or any(type(n) is not int or n<=0 for n in goals.values()):raise ValueError('Exact positive Web/news teacher quotas required')
        if not np.array_equal(web.byte_lengths,news.byte_lengths):raise ValueError('Common original Tokenizer bytes required')
        self.view,self.goals,self.context,self.seed=news,goals.copy(),context,seed
        self.streams=dict(web=OriginalWebStream(web,cursor,context),authored_news=NewsBlockStream(news,context,seed))
        self.position=0
        for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):setattr(self,key,dict.fromkeys(SOURCE_ORDER,0))

    def batch(self,size):
        if type(size) is not int or size<=0 or self.source_teachers==self.goals:raise ValueError('Positive nonexhausted batch required')
        xs,ys=[],[];body_bytes=0
        for _ in range(size):
            active=[g for g in SOURCE_ORDER if self.source_teachers[g]<self.goals[g]];genre=active[0] if active else 'web'
            x,y=self.streams[genre].block(self.context);remaining=self.goals[genre]-self.source_teachers[genre]
            labeled=np.flatnonzero(y!=-100);y[labeled[remaining:]]=-100
            count=int(np.count_nonzero(y!=-100));byte_count=int(self.view.byte_lengths[y[y>=8]].sum())
            self.source_teachers[genre]+=count;self.source_eos[genre]+=int(np.count_nonzero(y==3))
            self.source_tokens[genre]+=self.context;self.source_body_bytes[genre]+=byte_count;body_bytes+=byte_count
            xs.append(x);ys.append(y)
        x=torch.from_numpy(np.stack(xs));y=torch.from_numpy(np.stack(ys));self.position+=1
        return x,y,body_bytes,torch.zeros_like(y,dtype=torch.bool)

    def state_dict(self):
        return dict(kind='exact_staged_Web_then_authored_news_quota_v1',goals=self.goals.copy(),source_order=list(SOURCE_ORDER),context=self.context,seed=self.seed,position=self.position,
            **{k:getattr(self,k).copy() for k in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers')},
            streams={g:s.state_dict() for g,s in self.streams.items()})

    def load_state_dict(self,state):
        current=self.state_dict()
        if any(state[k]!=current[k] for k in ('kind','goals','source_order','context','seed')):raise ValueError('Exact news sampler recipe differs')
        if (type(state['position']) is not int or state['position']<0
                or any(type(n) is not int or n<0 or n>self.goals[g] for g,n in state['source_teachers'].items())
                or set(state['source_teachers'])!=set(SOURCE_ORDER)
                or any(state['source_focus_teachers'].values())
                or state['source_teachers']['authored_news'] and state['source_teachers']['web']!=self.goals['web']):raise ValueError('News quota/order cursor invalid')
        for g,s in self.streams.items():s.load_state_dict(state['streams'][g])
        for k in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):setattr(self,k,state[k].copy())
        self.position=state['position']


class NewsBaseTrainer(ConditionPositiveTrainer):
    def __init__(self,parent,web,news,goals,binding,device='cuda',context=1024,batch=32):
        if parent['implementation_sha256']!=implementation_hashes():raise ValueError('Shared native implementation differs')
        if parent['spec']['original_web_manifest_sha256']!=sha256(web.directory/'manifest.json'):raise ValueError('Actual original Web source differs')
        cursor=parent['sampler']['streams']['web']['sampler'];lrs=[g['lr'] for g in parent['optimizer']['param_groups']]
        if any(not math.isclose(v,LR,rel_tol=1e-10) for v in lrs):raise ValueError('Inherit actual LR1e-5 without reheating')
        if any(not math.isclose(lr/base,.1,rel_tol=1e-10) for lr,base in zip(lrs,parent['scheduler']['base_lrs'],strict=True)):raise ValueError('Actual permanent decay floor required')
        spec=dict(seed=42,context=context,batch=batch,accumulation=1,lr=LR,weight_decay=parent['spec']['weight_decay'],warmup=0,
            schedule_updates=parent['update']+math.ceil(2*sum(goals.values())/(context*batch))+32,scheduler='wsd',
            dtype='bf16' if device=='cuda' else 'fp32',backend='flash' if device=='cuda' else 'math',compile=device=='cuda',compile_mode='reduce-overhead',training_fast_path=True,deterministic=True,
            teacher_goals=goals.copy(),research_kind=KIND,outcome_weight=1,original_web_manifest_sha256=sha256(web.directory/'manifest.json'),
            news_manifest_sha256=sha256(news.directory/'manifest.json'),news_trainer_sha256=sha256(Path(__file__)),
            news_stream_policy='fixed shuffled contiguous1024 blocks with internal BOS masked; incomplete source tail under one context is unsampled, not extra documents')
        stub=SimpleNamespace(tokens=news.tokens[:context+1],split='train',manifest=news.manifest,byte_lengths=news.byte_lengths,directory=news.directory)
        Trainer.__init__(self,parent['model_config'],stub,spec,device);self.shard=news
        self.model.load_state_dict(parent['model'],strict=True);self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:.1);self.scheduler.load_state_dict(copy.deepcopy(parent['scheduler']))
        self.sampler=NewsQuotaSampler(web,news,cursor,goals,context,42);self.factor=1
        for key in ('update','tokens','supervised_tokens','body_bytes','token_digest'):setattr(self,key,parent[key])
        self.focus_token_digest=parent['focus_token_digest'];self.focus_teacher_tokens=self.weighted_teacher_mass=0
        self.binding=copy.deepcopy(binding);self.pilot_binding=dict(parent.get('pilot_binding',{}),**binding)
        self.lineage=dict(kind=KIND,parent=binding['parent'],original_parent=binding.get('original_parent'),
            parent_update=parent['update'],parent_tokens=parent['tokens'],parent_supervised_tokens=parent['supervised_tokens'],parent_body_bytes=parent['body_bytes'],parent_token_digest=parent['token_digest'],
            parent_focus_token_digest=parent['focus_token_digest'],parent_weighted_teacher_mass=parent['weighted_teacher_mass'],
            actual_parent_sampler=copy.deepcopy(parent['sampler']),actual_parent_Web_cursor=copy.deepcopy(cursor),parent_scheduler=copy.deepcopy(parent['scheduler']),optimizer_policy='inherit',no_reheat=True,
            accounting='New26.428M counted from cached73.572M prefix; original prefix teacher/input/source counters retained separately, not new scientific training.')
        restore_rng(parent['rng'])

    def step(self):
        row=super().step()
        if any(g['lr']!=LR for g in self.optimizer.param_groups):raise ValueError('Inherited constant LR changed')
        return row
