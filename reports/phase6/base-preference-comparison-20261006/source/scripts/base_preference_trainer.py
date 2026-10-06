"""Inherited native Web prefix followed by matched, role-free CE versus CE+DPO."""
import copy
import hashlib
import math
from pathlib import Path
import time
from types import SimpleNamespace
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import sha256
from jmicro.training import Trainer,implementation_hashes,restore_rng,rng_state,autocast,synchronize
from original_web_retention_trainer import OriginalWebStream
from condition_positive_trainer import ConditionPositiveTrainer
from base_preference_loss import collate_continuations,dpo_loss

KIND='role_free_Base_chosen_CE_vs_chosen_CE_plus_fixed_reference_DPO_v1'
LR=.00001


def Web_cursor(parent):
    sampler=parent['sampler']
    if sampler['kind']=='eos-pilot-mixture-v1':return sampler['web']
    if sampler['kind']=='Base_preference_common_Web_exact_v1':return sampler['streams']['web']['sampler']
    raise ValueError('Actual original d18 or explicit common-Web cursor required')


class CommonWebSampler:
    def __init__(self,web,cursor,goal,context):
        if type(goal) is not int or goal<=0:raise ValueError('Exact positive Web quota required')
        self.web=web;self.goals=dict(web=goal);self.context=context;self.position=0
        self.streams=dict(web=OriginalWebStream(web,cursor,context))
        for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):setattr(self,key,dict(web=0))

    def batch(self,size):
        if self.source_teachers==self.goals:raise ValueError('Common Web exhausted')
        xs=[];ys=[];byte_count=0
        for _ in range(size):
            x,y=self.streams['web'].block(self.context);remaining=self.goals['web']-self.source_teachers['web'];labeled=np.flatnonzero(y!=-100);y[labeled[remaining:]]=-100
            count=int(np.count_nonzero(y!=-100));bytes_=int(self.web.byte_lengths[y[y>=8]].sum())
            self.source_teachers['web']+=count;self.source_tokens['web']+=self.context;self.source_eos['web']+=int(np.count_nonzero(y==3))
            self.source_body_bytes['web']+=bytes_;byte_count+=bytes_;xs.append(x);ys.append(y)
        self.position+=1;x=torch.from_numpy(np.stack(xs));y=torch.from_numpy(np.stack(ys))
        return x,y,byte_count,torch.zeros_like(y,dtype=torch.bool)

    def state_dict(self):
        return dict(kind='Base_preference_common_Web_exact_v1',goals=self.goals.copy(),context=self.context,position=self.position,
            streams={k:v.state_dict() for k,v in self.streams.items()},
            **{k:getattr(self,k).copy() for k in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers')})

    def load_state_dict(self,state):
        current=self.state_dict()
        if any(state[k]!=current[k] for k in ('kind','goals','context')):raise ValueError('Common-Web recipe differs')
        self.streams['web'].load_state_dict(state['streams']['web']);self.position=state['position']
        for k in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):setattr(self,k,state[k].copy())


class CommonWebTrainer(ConditionPositiveTrainer):
    def __init__(self,parent,web,goal,binding,device='cuda',context=1024,batch=32):
        if parent['implementation_sha256']!=implementation_hashes() or parent['shard_manifest_sha256']!=sha256(web.directory/'manifest.json'):
            raise ValueError('Actual inherited native source/core differs')
        lrs=[g['lr'] for g in parent['optimizer']['param_groups']]
        if any(v!=LR for v in lrs) or any(not math.isclose(v/base,.1,rel_tol=1e-10) for v,base in zip(lrs,parent['scheduler']['base_lrs'],strict=True)):
            raise ValueError('Actual LR1e-5 floor must be inherited without reheat')
        spec=dict(seed=42,context=context,batch=batch,accumulation=1,lr=LR,weight_decay=parent['spec']['weight_decay'],warmup=0,
            schedule_updates=parent['update']+math.ceil(2*goal/(context*batch))+32,scheduler='wsd',dtype='bf16' if device=='cuda' else 'fp32',
            backend='flash' if device=='cuda' else 'math',compile=device=='cuda',compile_mode='reduce-overhead',training_fast_path=True,deterministic=True,
            research_kind=KIND,phase='common_Web',outcome_weight=1,teacher_goals=dict(web=goal),original_web_manifest_sha256=sha256(web.directory/'manifest.json'),
            base_preference_trainer_sha256=sha256(Path(__file__)))
        stub=SimpleNamespace(tokens=web.tokens[:context+1],split='train',manifest=web.manifest,byte_lengths=web.byte_lengths,directory=web.directory)
        Trainer.__init__(self,parent['model_config'],stub,spec,device);self.shard=web
        self.model.load_state_dict(parent['model'],strict=True);self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:.1);self.scheduler.load_state_dict(copy.deepcopy(parent['scheduler']))
        self.sampler=CommonWebSampler(web,Web_cursor(parent),goal,context);self.factor=1
        for k in ('update','tokens','supervised_tokens','body_bytes','token_digest'):setattr(self,k,parent[k])
        self.focus_token_digest=parent.get('focus_token_digest','00'*32);self.focus_teacher_tokens=self.weighted_teacher_mass=0
        self.binding=copy.deepcopy(binding);self.pilot_binding=dict(parent.get('pilot_binding',{}),**binding)
        self.lineage=dict(kind=KIND,phase='common_Web',parent=binding['parent'],parent_update=parent['update'],parent_tokens=parent['tokens'],
            parent_supervised_tokens=parent['supervised_tokens'],parent_body_bytes=parent['body_bytes'],actual_parent_sampler=copy.deepcopy(parent['sampler']),
            actual_parent_Web_cursor=copy.deepcopy(Web_cursor(parent)),parent_scheduler=copy.deepcopy(parent['scheduler']),optimizer_policy='inherit',no_reheat=True)
        restore_rng(parent['rng'])


class PairQuotaSampler:
    """Shuffle seven fixed8-pair groups; cap CE labels, score full active DPO pairs."""
    def __init__(self,pairs,goal,batch,byte_lengths,reference_digest):
        if type(goal) is not int or goal<=0 or not pairs or len(pairs)%batch:raise ValueError('Positive quota and complete fixed groups required')
        self.pairs=copy.deepcopy(pairs);self.goal=goal;self.batch_size=batch;self.byte_lengths=byte_lengths;self.reference_digest=reference_digest
        self.groups=[pairs[i:i+batch] for i in range(0,len(pairs),batch)]
        self.span=max(len(r['prompt_ids'])+len(r[k])-1 for r in pairs for k in ('chosen_ids','rejected_ids'))
        self.data_digest=hashlib.sha256(__import__('json').dumps(pairs,sort_keys=True).encode()).hexdigest()
        self.epoch=self.group_position=self.position=self.teachers=self.EOS=self.body_bytes=self.physical=self.valid=0
        self.scored_chosen=self.scored_rejected=self.active_pair_exposures=0;self.auxiliary_digest='00'*32

    def ordered_group(self):
        order=np.random.default_rng(np.random.SeedSequence([42,self.epoch,991])).permutation(len(self.groups))
        return int(order[self.group_position])

    def tensors(self,group):
        rows=self.groups[group];x,y,mask=collate_continuations(rows);pad=self.span-x.shape[1]
        return rows,F.pad(x,(0,pad)),F.pad(y,(0,pad),value=-100),F.pad(mask,(0,pad),value=False)

    def batch(self):
        if self.teachers==self.goal:raise ValueError('Positive completion quota exhausted')
        group=self.ordered_group();rows,x,y,mask=self.tensors(group);n=len(rows);ce=y.clone();ce[n:]=-100
        remaining=self.goal-self.teachers
        for i in range(n):
            labeled=torch.nonzero(ce[i].ne(-100)).flatten();ce[i,labeled[remaining:]]=-100;remaining-=int(ce[i].ne(-100).sum())
        active=ce[:n].ne(-100).any(-1);count=int(ce.ne(-100).sum());bytes_=int(self.byte_lengths[ce[ce>=8].numpy()].sum())
        self.teachers+=count;self.EOS+=int(ce.eq(3).sum());self.body_bytes+=bytes_;self.physical+=x.numel();self.valid+=int(mask.sum())
        self.active_pair_exposures+=int(active.sum());self.scored_chosen+=int(y[:n][active].ne(-100).sum());self.scored_rejected+=int(y[n:][active].ne(-100).sum())
        digest=hashlib.sha256(bytes.fromhex(self.auxiliary_digest));digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes());digest.update(active.numpy().astype(np.uint8).tobytes());self.auxiliary_digest=digest.hexdigest()
        self.position+=1;self.group_position+=1
        if self.group_position==len(self.groups):self.group_position=0;self.epoch+=1
        return group,x,y,ce,mask,active,bytes_

    def state_dict(self):
        return dict(kind='fixed_group_role_free_positive_quota_full_active_DPO_v1',goal=self.goal,batch=self.batch_size,span=self.span,
            data_digest=self.data_digest,reference_digest=self.reference_digest,**{k:getattr(self,k) for k in ('epoch','group_position','position','teachers','EOS','body_bytes','physical','valid','scored_chosen','scored_rejected','active_pair_exposures','auxiliary_digest')})

    def load_state_dict(self,state):
        current=self.state_dict()
        if any(state[k]!=current[k] for k in ('kind','goal','batch','span','data_digest','reference_digest')):raise ValueError('Frozen pair/data/reference differs')
        if (any(type(state[k]) is not int or state[k]<0 for k in ('epoch','group_position','position','teachers','EOS','body_bytes','physical','valid','scored_chosen','scored_rejected','active_pair_exposures'))
                or state['group_position']>=len(self.groups) or state['teachers']>self.goal or state['EOS']>state['teachers']
                or state['epoch']*len(self.groups)+state['group_position']!=state['position']
                or state['physical']!=state['position']*2*self.batch_size*self.span or state['valid']>state['physical']):raise ValueError('Pair exposure/cursor invalid')
        for k in ('epoch','group_position','position','teachers','EOS','body_bytes','physical','valid','scored_chosen','scored_rejected','active_pair_exposures','auxiliary_digest'):setattr(self,k,state[k])


def target_logps(logits,y):
    return logits.float().log_softmax(-1).gather(-1,y.clamp_min(0).unsqueeze(-1)).squeeze(-1)*y.ne(-100)


def build_reference(model,sampler,device,dtype):
    before=rng_state();training=model.training;model.eval();groups=[]
    try:
        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH):
            for group in range(len(sampler.groups)):
                _,x,y,mask=sampler.tensors(group)
                with autocast(device,dtype):scores=target_logps(model(x.to(device),attention_mask=mask.to(device)).logits,y.to(device)).sum(-1)
                if not bool(torch.isfinite(scores).all()):raise ValueError('Finite full-reference sequence sums required')
                n=sampler.batch_size;groups.append(dict(group=group,chosen=scores[:n].cpu().tolist(),rejected=scores[n:].cpu().tolist()))
    finally:model.train(training);restore_rng(before)
    return dict(groups=groups,data_digest=sampler.data_digest,span=sampler.span,batch=sampler.batch_size,dtype=dtype,backend='math')


class PairPreferenceTrainer(ConditionPositiveTrainer):
    def __init__(self,parent,web,pairs,goal,coefficient,reference,binding,device='cuda',batch=8):
        if coefficient not in (0.,.1):raise ValueError('Only frozen CE or CE+DPO coefficient allowed')
        digest=hashlib.sha256(__import__('json').dumps(reference,sort_keys=True).encode()).hexdigest()
        sampler=PairQuotaSampler(pairs,goal,batch,web.byte_lengths,digest)
        if (reference['data_digest']!=sampler.data_digest or reference['span']!=sampler.span or reference['batch']!=batch
                or len(reference['groups'])!=len(sampler.groups) or reference['dtype']!=('bf16' if device=='cuda' else 'fp32')):
            raise ValueError('Exact full56 grouped reference required')
        if parent['implementation_sha256']!=implementation_hashes() or parent['shard_manifest_sha256']!=sha256(web.directory/'manifest.json'):raise ValueError('Shared native common-Web source/core differs')
        spec=dict(seed=42,context=sampler.span,batch=batch,accumulation=1,lr=LR,weight_decay=parent['spec']['weight_decay'],warmup=0,
            schedule_updates=parent['update']+goal+32,scheduler='wsd',dtype='bf16' if device=='cuda' else 'fp32',backend='math',compile=False,deterministic=True,
            research_kind=KIND,phase='pair',coefficient=coefficient,beta=.1,original_web_manifest_sha256=sha256(web.directory/'manifest.json'),
            pair_data_digest=sampler.data_digest,reference_digest=digest,base_preference_trainer_sha256=sha256(Path(__file__)),
            mask_policy='Prompt/BOS/PAD masked, one shifted CE completion quota; full original chosen/rejected sums on active pairs, including last partially CE-labeled pair. Auxiliary positions separate, never forced EOS.')
        stub=SimpleNamespace(tokens=web.tokens[:sampler.span+1],split='train',manifest=web.manifest,byte_lengths=web.byte_lengths,directory=web.directory)
        Trainer.__init__(self,parent['model_config'],stub,spec,device);self.shard=web;self.model.load_state_dict(parent['model'],strict=True)
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']));self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:.1);self.scheduler.load_state_dict(copy.deepcopy(parent['scheduler']))
        if any(g['lr']!=LR for g in self.optimizer.param_groups):raise ValueError('Shared inherited LR differs')
        self.sampler=sampler;self.reference=copy.deepcopy(reference);self.coefficient=coefficient;self.factor=1
        for k in ('update','tokens','supervised_tokens','body_bytes','token_digest'):setattr(self,k,parent[k])
        self.focus_token_digest=parent.get('focus_token_digest','00'*32);self.focus_teacher_tokens=self.weighted_teacher_mass=0
        self.binding=copy.deepcopy(binding);self.pilot_binding=dict(parent.get('pilot_binding',{}),**binding)
        self.lineage=dict(kind=KIND,phase='pair',parent=binding['parent'],parent_update=parent['update'],parent_tokens=parent['tokens'],parent_supervised_tokens=parent['supervised_tokens'],
            parent_body_bytes=parent['body_bytes'],actual_parent_sampler=copy.deepcopy(parent['sampler']),parent_scheduler=copy.deepcopy(parent['scheduler']),optimizer_policy='inherit',no_reheat=True)
        restore_rng(parent['rng'])

    def audit_counters(self):
        s=self.sampler
        if (self.update-self.lineage['parent_update']!=s.position or self.tokens-self.lineage['parent_tokens']!=s.physical
                or self.supervised_tokens-self.lineage['parent_supervised_tokens']!=s.teachers or self.body_bytes-self.lineage['parent_body_bytes']!=s.body_bytes
                or self.weighted_teacher_mass!=s.teachers or self.focus_teacher_tokens!=0):raise ValueError('Pair completed update accounting differs')

    def step(self):
        synchronize(self.device);started=time.perf_counter();group,x,y,ce,mask,active,bytes_=self.sampler.batch();n=self.spec['batch'];count=int(ce.ne(-100).sum())
        digest=hashlib.sha256(bytes.fromhex(self.token_digest));digest.update(x.numpy().astype('<i8').tobytes());digest.update(ce.numpy().astype('<i8').tobytes())
        self.optimizer.zero_grad(set_to_none=True);self.model.train()
        x,y,ce,mask,active=(v.to(self.device) for v in (x,y,ce,mask,active))
        with sdpa_kernel(SDPBackend.MATH),autocast(self.device,self.spec['dtype']):
            logits=self.model(x,attention_mask=mask).logits;scores=target_logps(logits,y);sums=scores.sum(-1)
            CE=-(scores*ce.ne(-100)).sum()/count
            ref=self.reference['groups'][group]
            if ref['group']!=group:raise ValueError('Frozen reference group differs')
            chosen=torch.tensor(ref['chosen'],device=self.device,dtype=sums.dtype);rejected=torch.tensor(ref['rejected'],device=self.device,dtype=sums.dtype)
            DPO,margin=dpo_loss(sums[:n][active],sums[n:][active],chosen[active],rejected[active],self.spec['beta']);loss=CE+self.coefficient*DPO
        loss.backward();norm=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        if not bool(torch.isfinite(loss)):raise ValueError('Finite actual pair objective required')
        self.optimizer.step();self.scheduler.step();self.update+=1;self.tokens+=x.numel();self.supervised_tokens+=count;self.body_bytes+=bytes_;self.weighted_teacher_mass+=count;self.token_digest=digest.hexdigest();self.audit_counters()
        if any(g['lr']!=LR for g in self.optimizer.param_groups):raise ValueError('Inherited pair LR reheated')
        synchronize(self.device);seconds=time.perf_counter()-started;s=self.sampler
        return dict(update=self.update,loss=float(loss.detach()),CE_loss=float(CE.detach()),DPO_loss=float(DPO.detach()),DPO_coefficient=self.coefficient,beta=.1,
            mean_reference_ratio_margin=float(margin.detach().mean()),gradient_norm=float(norm),lr=LR,seconds=seconds,tokens_seen=self.tokens,supervised_tokens=self.supervised_tokens,
            body_bytes_seen=self.body_bytes,token_digest=self.token_digest,focus_token_digest=self.focus_token_digest,additional_teacher_tokens=s.teachers,
            physical_input_tokens=s.physical,valid_input_tokens=s.valid,CE_EOS=s.EOS,scored_chosen_positions=s.scored_chosen,scored_rejected_positions=s.scored_rejected,
            active_pair_exposures=s.active_pair_exposures,auxiliary_digest=s.auxiliary_digest,group=group,weighted_teacher_mass=self.weighted_teacher_mass,
            optimizer_pair_exposures=s.active_pair_exposures if self.coefficient else 0)
