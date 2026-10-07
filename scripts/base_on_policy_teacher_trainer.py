"""Original gold CE plus native teacher feedback on current-student prefixes."""
import copy
import hashlib
import json
from pathlib import Path
import time
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.model import JMicroModel
from jmicro.training import rng_state,restore_rng,synchronize
from natural_context_contrast_corpus import NaturalCorpusTrainer,GENRES
from natural_context_contrast_trainer import right_pad,right_padded_hidden
from base_native_teacher_KD_trainer import predictive_KL,finite_KD_state

KIND='original_gold_CE_current_student_sampled_prefix_native_teacher_KL_v1'
RECIPE=dict(every_completed_updates=16,max_prefixes=8,max_prompt_body_tokens=16,max_new_tokens=32,
    temperature=1.,coefficient=1.,divergence='forward_KL_teacher_to_student',
    denominator='generated_prediction_positions_this_scheduled_update',
    sources=['textbook','story'],sample_blocked_ids=[0,1,2,4,5,6,7],EOS=3)


def prefixes_from_rows(rows):
    result=[]
    for row in rows:
        if (row['source'] not in RECIPE['sources'] or not row['original_document_first_window']
                or row['target_first']!=1):continue
        ids=row['input_ids']
        if len(ids)<3 or ids[0]!=2 or any(i<8 for i in ids[1:]):
            raise ValueError('Original whole-document BOS/body prefix required')
        body=min(RECIPE['max_prompt_body_tokens'],max(1,(len(ids)-1)//2))
        result.append(dict(source=row['source'],prompt=ids[:body+1],
            index_byte_position=row['index_byte_position'],index_record_sha256=row['index_record_sha256']))
        if len(result)==RECIPE['max_prefixes']:break
    return result


@torch.no_grad()
def sample_rollout(model,prefixes):
    """Original native masked KV-cache; global torch RNG is checkpointed."""
    if not prefixes:raise ValueError('At least one TRAIN prefix required')
    device=next(model.parameters()).device
    if max(len(p['prompt']) for p in prefixes)+RECIPE['max_new_tokens']>model.config['max_position_embeddings']:
        raise ValueError('Rollout exceeds native context')
    mode=model.training
    try:
        model.eval();ids,_=right_pad([p['prompt'] for p in prefixes],device)
        valid=ids.ne(0);lengths=valid.sum(-1)
        physical=ids.numel();inputs=int(valid.sum())
        output=model(ids,attention_mask=valid,use_cache=True)
        logits=output.logits[torch.arange(len(prefixes),device=device),lengths-1]
        cache=output.cache;active=torch.ones(len(prefixes),dtype=torch.bool,device=device)
        generated=[[] for _ in prefixes]
        for step in range(RECIPE['max_new_tokens']):
            scores=logits[active].float().clone();scores[:,RECIPE['sample_blocked_ids']]=-float('inf')
            if not torch.isfinite(scores.softmax(-1)).all():raise ValueError('Finite sampled distribution required')
            draws=torch.multinomial(scores.softmax(-1),1).squeeze(-1)
            indices=active.nonzero(as_tuple=False).flatten()
            next_ids=torch.zeros((len(prefixes),1),dtype=torch.long,device=device)
            next_ids[indices,0]=draws
            for i,token in zip(indices.tolist(),draws.tolist(),strict=True):generated[i].append(token)
            active=active & next_ids[:,0].ne(RECIPE['EOS'])
            if not bool(active.any()) or step+1==RECIPE['max_new_tokens']:break
            next_ids[~active]=0
            output=model(next_ids,attention_mask=active[:,None],cache=cache,use_cache=True)
            inputs+=int(active.sum());physical+=next_ids.numel();cache=output.cache;logits=output.logits[:,0]
        records=[dict(**p,generated=g,EOS_stopped=g[-1]==3) for p,g in zip(prefixes,generated,strict=True)]
        return records,dict(valid_inputs=inputs,physical_inputs=physical)
    finally:
        model.train(mode)


def scoring_batch(records,device):
    """Each generated token is predicted from its actual preceding prefix."""
    sequences=[];labels=[]
    for record in records:
        prompt,g=record['prompt'],record['generated']
        if not g or len(g)>32 or any(t!=3 and t<8 for t in g) or 3 in g[:-1]:
            raise ValueError('Sampled body/firstEOS only, no postEOS targets')
        sequences.append(prompt+g[:-1]);labels.append([-100]*(len(prompt)-1)+g)
    ids,_=right_pad(sequences,device);targets=torch.full_like(ids,-100)
    for i,y in enumerate(labels):targets[i,:len(y)]=torch.tensor(y,device=device)
    return ids,targets,dict(valid_inputs=sum(map(len,sequences)),physical_inputs=ids.numel())


class OnPolicyTeacherTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,teacher_checkpoint,teacher_reference,batch=48,device='cuda',seed=42):
        if parent['model_config']!=teacher_checkpoint['model_config']:raise ValueError('Same native architecture/codec required')
        super().__init__(parent,sampler,binding,batch=batch,contrast=False,device=device,seed=seed)
        self.spec.update(kind=KIND,on_policy_teacher=copy.deepcopy(RECIPE),teacher=copy.deepcopy(teacher_reference),
            main_counters_scope='unchanged_original_CE_only; rollout/scoring/teacher inputs recorded separately')
        self.lineage.update(kind=KIND,teacher=copy.deepcopy(teacher_reference),teacher_parent_update=teacher_checkpoint['update'],
            teacher_parent_tokens=teacher_checkpoint['tokens'])
        before=rng_state()
        self.teacher=JMicroModel(teacher_checkpoint['model_config']).to(self.device).eval()
        self.teacher.load_state_dict(teacher_checkpoint['model'],strict=True);self.teacher.requires_grad_(False)
        restore_rng(before)
        self.on_policy=dict(updates=0,scheduled_batches=0,rollout_batches=0,skipped_batches=0,sequences=0,
            distribution_positions=0,generated_body_positions=0,generated_EOS=0,
            source_positions=dict.fromkeys(GENRES,0),rollout_valid_inputs=0,rollout_physical_inputs=0,
            student_scoring_valid_inputs=0,student_scoring_physical_inputs=0,teacher_valid_inputs=0,teacher_physical_inputs=0,
            teacher_entropy_sum=0.,teacher_selected_probability_sum=0.,teacher_EOS_probability_sum=0.,KL_sum=0.,digest='0'*64)

    def state_dict(self):
        state=super().state_dict();state.update(kind=KIND,on_policy_teacher=copy.deepcopy(self.on_policy));return state

    def load(self,path):
        state=torch.load(Path(path),map_location='cpu',weights_only=False)
        if not committed_state(state):raise ValueError('Committed gold/on-policy fullstate required')
        super().load(path);self.on_policy=copy.deepcopy(state['on_policy_teacher'])

    def step(self):
        synchronize(self.device);started=time.monotonic();rows=self.sampler.take(self.spec['batch']);wait=time.monotonic()-started
        ids,_=right_pad([r['input_ids'] for r in rows],self.device);targets=torch.full_like(ids,-100)
        for i,row in enumerate(rows):targets[i,:len(row['target_ids'])]=torch.tensor(row['target_ids'],device=self.device)
        selected=targets.ne(-100);gold=sum(r['teacher_tokens'] for r in rows)
        if int(selected.sum())!=gold:raise ValueError('Original gold targets differ')
        self.optimizer.zero_grad(set_to_none=True)
        backend=SDPBackend.FLASH_ATTENTION if self.device.type=='cuda' else SDPBackend.MATH
        enabled=self.device.type=='cuda'
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=enabled):
            logits=self.model.lm_head(right_padded_hidden(self.model,ids)[selected]).float()
            ce=F.cross_entropy(logits,targets[selected]);ce.backward()
        counts=copy.deepcopy(self.on_policy);records=[];aux=0.;local=self.counters['update']+1
        if local%RECIPE['every_completed_updates']==0:
            counts['scheduled_batches']+=1;prefixes=prefixes_from_rows(rows)
            if not prefixes:counts['skipped_batches']+=1
            else:
                with sdpa_kernel(SDPBackend.MATH),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=enabled):
                    records,draw=sample_rollout(self.model,prefixes)
                score_ids,score_targets,score=scoring_batch(records,self.device);mask=score_targets.ne(-100);positions=int(mask.sum())
                with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=enabled):
                    with torch.no_grad():q=self.teacher.lm_head(right_padded_hidden(self.teacher,score_ids)[mask]).float()
                    p=self.model.lm_head(right_padded_hidden(self.model,score_ids)[mask]).float()
                    kl,stats=predictive_KL(p,q,score_targets[mask],positions)
                    if not torch.isfinite(kl):raise ValueError('Finite teacher-feedback loss required')
                    (RECIPE['coefficient']*kl).backward();aux=float(kl.detach())
                counts['rollout_batches']+=1;counts['sequences']+=len(records);counts['distribution_positions']+=positions
                counts['generated_EOS']+=sum(r['generated'].count(3) for r in records)
                counts['generated_body_positions']+=sum(sum(t>=8 for t in r['generated']) for r in records)
                for r in records:counts['source_positions'][r['source']]+=len(r['generated'])
                for key,value in dict(rollout_valid_inputs=draw['valid_inputs'],rollout_physical_inputs=draw['physical_inputs'],
                    student_scoring_valid_inputs=score['valid_inputs'],student_scoring_physical_inputs=score['physical_inputs'],
                    teacher_valid_inputs=score['valid_inputs'],teacher_physical_inputs=score['physical_inputs'],
                    teacher_entropy_sum=stats['teacher_entropy_sum'],teacher_selected_probability_sum=stats['teacher_gold_probability_sum'],
                    teacher_EOS_probability_sum=float(q.softmax(-1)[:,3].sum()),KL_sum=stats['KL_sum']).items():counts[key]+=value
                counts['digest']=hashlib.sha256(bytes.fromhex(counts['digest'])+json.dumps(records,sort_keys=True).encode()).hexdigest()
        gradient=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        if not torch.isfinite(ce):raise ValueError('Finite original CE required')
        self.optimizer.step();self.scheduler.step();self.counters['update']+=1;counts['updates']+=1
        for key,value in dict(supervised_tokens=gold,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            physical_input_tokens=ids.numel(),original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():self.counters[key]+=value
        for r in rows:self.counters['source_teachers'][r['source']]+=r['teacher_tokens'];self.counters['source_EOS'][r['source']]+=r['original_EOS_targets']
        if self.counters['source_teachers']!=self.sampler.consumed:raise ValueError('Completed original gold quotas differ')
        stream=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest']=hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest();self.on_policy=counts
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),on_policy_teacher=copy.deepcopy(counts),CE_loss=float(ce.detach()),
            teacher_feedback_KL=aux,combined_loss=float(ce.detach())+aux,gradient_norm=float(gradient),lr=self.optimizer.param_groups[0]['lr'],
            CE_targets_this_update=gold,distribution_positions_this_update=sum(len(r['generated']) for r in records),
            current_student_update_for_rollout=local-1 if records else None,rollout_records=records,
            seconds=time.monotonic()-started,data_wait_seconds=wait,physical_inputs_this_update=ids.numel(),
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),original_windows_this_update=len(rows),
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])


def committed_state(state):
    if state.get('kind')!=KIND or 'on_policy_teacher' not in state or not finite_KD_state(state):return False
    c,d=state['counters'],state['on_policy_teacher'];steps=c['update']
    if (state['spec'].get('on_policy_teacher')!=RECIPE or steps!=d['updates'] or steps!=state['scheduler']['last_epoch'] or
        any(int(v['step'])!=steps for v in state['optimizer']['state'].values()) or
        d['scheduled_batches']!=steps//16 or d['rollout_batches']+d['skipped_batches']!=d['scheduled_batches'] or
        not 0<=d['generated_EOS']<=d['sequences']<=d['distribution_positions']<=32*d['sequences'] or
        d['generated_body_positions']+d['generated_EOS']!=d['distribution_positions'] or
        sum(d['source_positions'].values())!=d['distribution_positions'] or d['source_positions']['web']!=0 or
        not 0<=d['teacher_selected_probability_sum']<=d['distribution_positions'] or
        not 0<=d['teacher_EOS_probability_sum']<=d['distribution_positions'] or d['teacher_entropy_sum']<0 or
        c['source_teachers']!=state['sampler']['consumed'] or c['supervised_tokens']!=sum(c['source_teachers'].values())):return False
    return all(0<=d[p+'_valid_inputs']<=d[p+'_physical_inputs'] for p in ('rollout','student_scoring','teacher'))
