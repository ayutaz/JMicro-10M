"""Original gold CE plus frozen native predictive KL on original short sources."""
import copy
import hashlib
import json
from pathlib import Path
import time
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.model import JMicroModel
from jmicro.training import synchronize,rng_state,restore_rng
from natural_context_contrast_corpus import NaturalCorpusTrainer,GENRES
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden

KIND='native_original_gold_CE_frozen_staged_short_predictive_KL_v1'


def predictive_KL(student_logits,teacher_logits,targets,total_gold):
    """T1/alpha1; original gold denominator, teacher never receives gradient."""
    if student_logits.ndim!=2 or student_logits.shape!=teacher_logits.shape or targets.shape!=(len(student_logits),):
        raise ValueError('Exact matching supervised prediction positions required')
    if type(total_gold) is not int or total_gold<len(targets) or not len(targets):
        raise ValueError('Positive full original gold denominator required')
    if not torch.isfinite(student_logits).all() or not torch.isfinite(teacher_logits).all():
        raise ValueError('Finite full vocabulary predictions required')
    student_logp=F.log_softmax(student_logits.float(),dim=-1)
    teacher_logp=F.log_softmax(teacher_logits.detach().float(),dim=-1)
    q=teacher_logp.exp()
    kl=F.kl_div(student_logp,teacher_logp,reduction='sum',log_target=True)/total_gold
    with torch.no_grad():
        stats=dict(teacher_entropy_sum=float(-(q*teacher_logp).sum()),
            teacher_gold_probability_sum=float(q.gather(1,targets[:,None]).sum()),
            KL_sum=float(kl.detach())*total_gold)
    return kl,stats


class NativeTeacherKDTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,teacher_checkpoint,teacher_reference,batch=48,
                 contrast=False,device='cuda',seed=42):
        if contrast or parent['model_config']!=teacher_checkpoint['model_config']:
            raise ValueError('Same original native architecture/codec and no contrast objective required')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        self.spec.update(kind=KIND,teacher=copy.deepcopy(teacher_reference),KD_temperature=1.,KD_coefficient=1.,
            KD_sources=['textbook','story'],KD_denominator='all_original_gold_positions_this_update',
            KD_targets='full_native_vocab_predictive_distribution_on_same_original_supervised_positions',
            teacher_frozen_eval=True)
        self.lineage.update(kind=KIND,teacher=copy.deepcopy(teacher_reference),
            teacher_parent_update=teacher_checkpoint['update'],teacher_parent_tokens=teacher_checkpoint['tokens'])
        before=rng_state()
        self.teacher=JMicroModel(teacher_checkpoint['model_config']).to(self.device).eval()
        self.teacher.load_state_dict(teacher_checkpoint['model'],strict=True)
        self.teacher.requires_grad_(False)
        restore_rng(before)
        self.KD=dict(updates=0,teacher_positions=0,teacher_EOS=0,teacher_valid_inputs=0,teacher_physical_inputs=0,
            source_positions=dict.fromkeys(GENRES,0),teacher_entropy_sum=0.,teacher_gold_probability_sum=0.,KL_sum=0.,digest='0'*64)

    def state_dict(self):
        state=super().state_dict();state.update(kind=KIND,native_teacher_KD=copy.deepcopy(self.KD))
        return state

    def load(self,path):
        state=torch.load(Path(path),map_location='cpu',weights_only=False)
        if state.get('kind')!=KIND or 'native_teacher_KD' not in state:
            raise ValueError('Predictive-KD fullstate required; old CE states cannot be relabeled')
        kd,c=state['native_teacher_KD'],state['counters']
        expected={g:(c['source_teachers'][g] if g in ('textbook','story') else 0) for g in GENRES}
        if (kd['updates']!=c['update'] or kd['source_positions']!=expected or kd['teacher_positions']!=sum(expected.values())
            or kd['teacher_EOS']!=sum(c['source_EOS'][g] for g in ('textbook','story'))
            or not 0<=kd['teacher_positions']<=kd['teacher_valid_inputs']<=kd['teacher_physical_inputs']
            or not 0<=kd['teacher_gold_probability_sum']<=kd['teacher_positions']
            or kd['teacher_entropy_sum']<0
            or c['source_teachers']!=state['sampler']['consumed'] or c['supervised_tokens']!=sum(c['source_teachers'].values())
            or c['auxiliary_input_tokens'] or c['auxiliary_pairs'] or not finite_KD_state(state)):
            raise ValueError('Committed original gold/short predictive KD accounting differs')
        super().load(path);self.KD=copy.deepcopy(kd)

    def step(self):
        synchronize(self.device);started=time.monotonic()
        rows=self.sampler.take(self.spec['batch']);data_wait=time.monotonic()-started
        ids,_=right_pad([r['input_ids'] for r in rows],self.device)
        targets=torch.full_like(ids,-100)
        for i,row in enumerate(rows): targets[i,:len(row['target_ids'])]=torch.tensor(row['target_ids'],device=self.device)
        selected=targets.ne(-100);supervised=sum(r['teacher_tokens'] for r in rows)
        if int(selected.sum())!=supervised: raise ValueError('Exact original gold targets required')
        short_indices=[i for i,r in enumerate(rows) if r['source'] in ('textbook','story')]
        row_short=torch.tensor([r['source'] in ('textbook','story') for r in rows],device=self.device)
        short_selected=(selected & row_short[:,None])[selected]
        kd_count=int(short_selected.sum());teacher_valid=teacher_physical=0
        stats=dict(teacher_entropy_sum=0.,teacher_gold_probability_sum=0.,KL_sum=0.)
        self.optimizer.zero_grad(set_to_none=True)
        backend=SDPBackend.FLASH_ATTENTION if self.device.type=='cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type=='cuda'):
            teacher_logits=None
            if short_indices:
                teacher_ids,_=right_pad([rows[i]['input_ids'] for i in short_indices],self.device)
                teacher_targets=torch.full_like(teacher_ids,-100)
                for index,i in enumerate(short_indices):
                    teacher_targets[index,:len(rows[i]['target_ids'])]=torch.tensor(rows[i]['target_ids'],device=self.device)
                if not torch.equal(teacher_targets[teacher_targets.ne(-100)],targets[selected][short_selected]):
                    raise ValueError('Teacher and student original short positions differ')
                with torch.no_grad():
                    teacher_logits=self.teacher.lm_head(right_padded_hidden(self.teacher,teacher_ids)[teacher_targets.ne(-100)]).float()
                teacher_valid=sum(len(rows[i]['input_ids']) for i in short_indices);teacher_physical=teacher_ids.numel()
            logits=self.model.lm_head(right_padded_hidden(self.model,ids)[selected]).float()
            ce=F.cross_entropy(logits,targets[selected])
            kl=ce.new_zeros(())
            if teacher_logits is not None:
                kl,stats=predictive_KL(logits[short_selected],teacher_logits,targets[selected][short_selected],supervised)
            combined=ce+kl
            if not torch.isfinite(combined): raise ValueError('Nonfinite gold CE/native short predictive KL')
            combined.backward()
        gradient=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        self.optimizer.step();self.scheduler.step();self.counters['update']+=1
        for key,value in dict(supervised_tokens=supervised,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            physical_input_tokens=ids.numel(),original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[key]+=value
        for row in rows:
            self.counters['source_teachers'][row['source']]+=row['teacher_tokens']
            self.counters['source_EOS'][row['source']]+=row['original_EOS_targets']
        if self.counters['source_teachers']!=self.sampler.consumed: raise ValueError('Completed original source quotas differ')
        stream=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest']=hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        for key,value in dict(updates=1,teacher_positions=kd_count,
            teacher_EOS=sum(rows[i]['original_EOS_targets'] for i in short_indices),
            teacher_valid_inputs=teacher_valid,teacher_physical_inputs=teacher_physical,**stats).items(): self.KD[key]+=value
        for i in short_indices: self.KD['source_positions'][rows[i]['source']]+=rows[i]['teacher_tokens']
        self.KD['digest']=hashlib.sha256(bytes.fromhex(self.KD['digest'])+
            json.dumps([(rows[i]['index_byte_position'],rows[i]['index_record_sha256'],rows[i]['target_ids']) for i in short_indices]).encode()).hexdigest()
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),native_teacher_KD=copy.deepcopy(self.KD),CE_loss=float(ce.detach()),
            KD_loss=float(kl.detach()),combined_loss=float(combined.detach()),gradient_norm=float(gradient),lr=self.optimizer.param_groups[0]['lr'],
            CE_targets_this_update=supervised,KD_targets_this_update=kd_count,teacher_valid_inputs_this_update=teacher_valid,
            teacher_physical_inputs_this_update=teacher_physical,total_physical_inputs_this_update=ids.numel()+teacher_physical,
            physical_inputs_this_update=ids.numel(),original_windows_this_update=len(rows),seconds=time.monotonic()-started,data_wait_seconds=data_wait,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])


def finite_KD_state(value):
    if isinstance(value,torch.Tensor): return not value.is_floating_point() or bool(torch.isfinite(value).all())
    if isinstance(value,float): return __import__('math').isfinite(value)
    if isinstance(value,dict): return all(finite_KD_state(v) for v in value.values())
    if isinstance(value,(list,tuple)): return all(finite_KD_state(v) for v in value)
    return True
