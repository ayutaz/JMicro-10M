"""Same original microbatch stream, one teacher-weighted update per fixed group."""
import copy
import hashlib
import json
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from base_parallel_residual_trainer import FreshResidualTrainer, committed_state, KIND as BASE_KIND
from natural_context_contrast_trainer import host, right_pad, right_padded_hidden
from jmicro.training import restore_rng, synchronize

KIND = 'fresh_sequential_original_stream_teacher_weighted_grouped_updates_v1'


def base_state(state):
    value = dict(state)
    value['kind'] = BASE_KIND
    value.pop('grouping')
    return value


def committed_group(state):
    try:
        group = state['grouping']
        return (state['kind'] == KIND and state['spec']['arm'] == 'sequential'
                and type(group['accumulation']) is int and group['accumulation'] in (1,4)
                and group['microbatches'] == state['counters']['update']*group['accumulation']
                and group['weighting'] == 'original_teacher_count_divided_by_group_total'
                and committed_state(base_state(state)))
    except (KeyError,TypeError,ValueError):
        return False


class GroupedTrainer:
    def __init__(self, native, accumulation=4):
        if (not isinstance(native,FreshResidualTrainer) or native.spec['arm']!='sequential'
                or native.counters['update'] or accumulation not in (1,4)):
            raise ValueError('Fresh native sequential and fixed accumulation1/4 required')
        self.native, self.accumulation = native, accumulation
        self.microbatches = 0
        self.in_progress = False

    def step(self):
        if self.in_progress:
            raise ValueError('Interrupted group requires committed checkpoint restore')
        self.in_progress = True
        t = self.native
        if not t.model.training:
            raise ValueError('Original learning requires train mode')
        synchronize(t.device)
        started = time.monotonic()
        batches = [t.sampler.take(t.spec['batch']) for _ in range(self.accumulation)]
        if any(len(rows)!=t.spec['batch'] for rows in batches):
            raise ValueError('This fixed pilot requires complete original microbatches')
        total = sum(row['teacher_tokens'] for rows in batches for row in rows)
        if total<=0:
            raise ValueError('Positive original teachers required')
        data_wait = time.monotonic()-started
        t.optimizer.zero_grad(set_to_none=True)
        backend = SDPBackend.FLASH_ATTENTION if t.device.type=='cuda' else SDPBackend.MATH
        mean_loss, physical = 0., 0
        digest = t.counters['token_digest']
        traces = []
        for rows in batches:
            if any(row['prefix_ids'] or row['suffix_ids'] for row in rows):
                raise ValueError('No auxiliary supervision permitted')
            ids,_ = right_pad([r['input_ids'] for r in rows],t.device)
            targets = torch.full_like(ids,-100)
            for i,row in enumerate(rows):
                targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'],device=t.device)
            selected = targets.ne(-100)
            n = sum(row['teacher_tokens'] for row in rows)
            if int(selected.sum())!=n:
                raise ValueError('Original teacher mask differs')
            with sdpa_kernel(backend),torch.autocast(t.device.type,dtype=torch.bfloat16,enabled=t.device.type=='cuda'):
                hidden = right_padded_hidden(t.model,ids)
                logits = t.model.lm_head(hidden[selected]).float()
                ce = F.cross_entropy(logits,targets[selected])
                if not bool(torch.isfinite(ce)):
                    raise ValueError('Nonfinite original CE')
                weighted = ce if self.accumulation==1 else ce*(n/total)
                weighted.backward()
            mean_loss += float(ce.detach())*(n/total)
            physical += ids.numel()
            payload = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
            digest = hashlib.sha256(bytes.fromhex(digest)+payload).hexdigest()
            traces.append([(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
            del ids,targets,selected,hidden,logits,ce,weighted
        gradient = torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
        if not 0<float(gradient)<float('inf'):
            raise ValueError('Finite nonzero grouped gradient required')
        lr = t.scheduler.prepare(total)
        t.optimizer.step()
        t.scheduler.commit(total)
        rows = [r for batch in batches for r in batch]
        t.counters['update'] += 1
        for key,value in dict(supervised_tokens=total,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
                physical_input_tokens=physical,original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            t.counters[key] += value
        for row in rows:
            t.counters['source_teachers'][row['source']] += row['teacher_tokens']
            t.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        t.counters['token_digest'] = digest
        self.microbatches += self.accumulation
        if t.counters['source_teachers']!=t.sampler.consumed or t.counters['supervised_tokens']!=t.scheduler.tokens:
            raise ValueError('Committed group sampler/teacher/scheduler differs')
        self.in_progress = False
        synchronize(t.device)
        return dict(**copy.deepcopy(t.counters),microbatches=self.microbatches,CE_loss=mean_loss,
            gradient_norm=float(gradient),lr=lr,seconds=time.monotonic()-started,data_wait_seconds=data_wait,
            CE_targets_this_update=total,microbatch_draw_traces=traces)

    def state_dict(self):
        if self.in_progress:
            raise ValueError('Cannot save interrupted/uncommitted group')
        state = dict(self.native.state_dict(),kind=KIND,grouping=dict(accumulation=self.accumulation,
            microbatches=self.microbatches,weighting='original_teacher_count_divided_by_group_total'))
        if not committed_group(state):
            raise ValueError('Invalid/nonfinite completed grouped state')
        return state

    def save(self,path):
        path = Path(path)
        temporary = path.with_suffix('.tmp')
        torch.save(host(self.state_dict()),temporary)
        temporary.replace(path)

    def load(self,path):
        state = torch.load(path,map_location=self.native.device,weights_only=False)
        t = self.native
        if not committed_group(state) or state['grouping']['accumulation']!=self.accumulation:
            raise ValueError('Matching finite committed grouped checkpoint required')
        expected = t.state_dict()
        if any(state[k]!=expected[k] for k in ('spec','binding','lineage','model_config')):
            raise ValueError('Grouped recipe/source binding differs')
        t.scheduler.validate(state['scheduler'])
        t.sampler.load_state_dict(state['sampler'])
        t.model.load_state_dict(state['model'],strict=True)
        t.optimizer.load_state_dict(state['optimizer'])
        t.scheduler.load_state_dict(state['scheduler'])
        t.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        self.microbatches = state['grouping']['microbatches']
        self.in_progress = False
