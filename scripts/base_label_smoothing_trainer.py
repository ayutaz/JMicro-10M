"""Same original CE stream and native parameters; fixed smoothed targets."""
import copy
import hashlib
import json
import time

import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.training import synchronize
from natural_context_contrast_corpus import NaturalCorpusTrainer
from natural_context_contrast_trainer import right_pad,right_padded_hidden
from base_label_smoothing import EPSILON,KIND,smoothed_teacher_loss


class LabelSmoothingTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,batch=48,contrast=False,device='cuda',seed=42):
        if contrast:raise ValueError('No auxiliary context loss in fixed label smoothing condition')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        self.spec.update(kind=KIND,label_smoothing=EPSILON,uniform_vocabulary=self.model.config['vocab_size'],
            original_gold_weight=1-EPSILON,uniform_weight=EPSILON,
            uniform_support='all_original_native_vocabulary_including_reserved_and_EOS')
        self.lineage['kind']=KIND
        self.counters.update(weighted_original_target_mass=0.,uniform_soft_target_positions=0,uniform_target_mass=0.)

    def state_dict(self):
        state=super().state_dict();state['kind']=KIND
        return state

    def step(self):
        if not self.model.training:raise ValueError('model.train required for original teacher learning')
        synchronize(self.device);started=time.monotonic()
        rows=self.sampler.take(self.spec['batch']);data_wait=time.monotonic()-started
        ids,_=right_pad([r['input_ids'] for r in rows],self.device)
        targets=torch.full_like(ids,-100)
        for index,row in enumerate(rows):targets[index,:len(row['target_ids'])]=torch.tensor(row['target_ids'],device=self.device)
        self.optimizer.zero_grad(set_to_none=True)
        backend=SDPBackend.FLASH_ATTENTION if self.device.type=='cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type=='cuda'):
            hidden=right_padded_hidden(self.model,ids);selected=targets.ne(-100)
            logits=self.model.lm_head(hidden[selected]).float()
            loss,stats=smoothed_teacher_loss(logits,targets[selected])
            loss.backward()
        supervised=sum(r['teacher_tokens'] for r in rows)
        if (stats['original_CE_positions']!=supervised or stats['original_EOS_positions']!=sum(r['original_EOS_targets'] for r in rows)
                or stats['epsilon']!=EPSILON):raise ValueError('Unchanged original body/EOS teacher masks required')
        gradient=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        if not 0<float(gradient)<float('inf'):raise ValueError('Finite nonzero actual native gradient required')
        self.optimizer.step();self.scheduler.step();self.counters['update']+=1
        for key,value in dict(supervised_tokens=supervised,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            physical_input_tokens=ids.numel(),original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[key]+=value
        for row in rows:
            self.counters['source_teachers'][row['source']]+=row['teacher_tokens']
            self.counters['source_EOS'][row['source']]+=row['original_EOS_targets']
        if self.counters['source_teachers']!=self.sampler.consumed:raise ValueError('Completed-update source quota accounting differs')
        # Derive masses from the integer committed position total to avoid repeated fractional-rounding drift.
        total=self.counters['supervised_tokens']
        self.counters.update(weighted_original_target_mass=(1-EPSILON)*total,
            uniform_soft_target_positions=total,uniform_target_mass=EPSILON*total)
        stream=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest']=hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),CE_loss=float(stats['CE_loss'].detach()),
            uniform_smoothing_loss=float(stats['uniform_target_loss'].detach()),combined_loss=float(loss.detach()),
            label_smoothing_epsilon=EPSILON,gradient_norm=float(gradient),contrast_loss=0.,auxiliary_gradient_norm=0.,
            positive_cosine=0.,distractor_cosine=0.,representation_variance=0.,
            CE_targets_this_update=supervised,uniform_positions_this_update=supervised,
            weighted_original_mass_this_update=(1-EPSILON)*supervised,uniform_mass_this_update=EPSILON*supervised,
            auxiliary_inputs_this_update=0,physical_inputs_this_update=ids.numel(),eligible_pairs_this_update=0,
            auxiliary_pairs_this_update=0,original_windows_this_update=len(rows),seconds=time.monotonic()-started,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),data_wait_seconds=data_wait,
            lr=self.optimizer.param_groups[0]['lr'],draw_trace=[(r['index_byte_position'],r['index_record_sha256'],
                r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
