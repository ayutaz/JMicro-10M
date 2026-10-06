"""Fresh native attention-allocation models; original TRAIN CE and token LR.

This separate sampler omits unused sentence-pair extraction. The original
frozen contrast/smoothing implementations remain untouched.
"""
from collections import Counter
import copy
import hashlib
import json
import math
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.model import JMicroModel
from jmicro.training import restore_rng, seed_all, synchronize
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, GENRES, document_windows
from natural_context_contrast_trainer import NaturalContextTrainer, host, right_pad, right_padded_hidden

KIND = 'fresh_native_KV_allocation_original_TRAIN_CE_token_schedule_v1'
SAMPLER_KIND = 'bounded_original_TRAIN_index_byte_draw_CE_only_genre_quota_windows_v1'


class CEOnlyOriginalSampler(OriginalTrainCorpusSampler):
    def _draw_document(self, genre):
        for _ in range(4096):
            position = self.rng.randrange(self.binding['index_size'])
            self.draws += 1
            self.handle.seek(position)
            if position:
                self.handle.readline(16384)
            location = self.handle.tell()
            raw = self.handle.readline(16385)
            if not raw or len(raw) > 16384:
                continue
            record = json.loads(raw)
            if record['split'] != 'train':
                raise ValueError('Only accepted TRAIN records may be decoded')
            if record['source'] != genre:
                continue
            count, offset = record['body_tokens'], record['offset']
            serialized = self.tokens[offset:offset+count+2].tolist()
            if len(serialized) != count+2 or serialized[0] != 2 or serialized[-1] != 3:
                raise ValueError('Original full BOS/body/EOS unit differs')
            body = serialized[1:-1]
            if any(i < 8 for i in body):
                raise ValueError('Plain accepted original body required')
            original = self.tokenizer.decode_bytes(body)
            original.decode('utf-8', errors='strict')
            digest = hashlib.sha256(original).hexdigest()
            if digest != record['canonical_sha256']:
                raise ValueError('Original accepted unit bytes differ')
            reason = 'CE_only_no_auxiliary_pair_extraction'
            metadata = dict(source=genre, source_family=record['source_family'],
                full_original_body_sha256=digest, index_byte_position=location,
                index_record_sha256=hashlib.sha256(raw).hexdigest(), original_body_tokens=count,
                original_body_UTF8_bytes=len(original), auxiliary_eligibility=reason)
            windows = list(document_windows(body))
            for i, window in enumerate(windows):
                window.update(metadata, prefix_ids=[], suffix_ids=[], original_document_first_window=i == 0)
            self.pending[genre] = windows
            self.documents_drawn += 1
            self.auxiliary_reasons[reason] += 1
            return
        raise RuntimeError('Fixed4096 bounded index draws lack requested genre; no reroll')

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = SAMPLER_KIND
        return state


class TargetPositionSchedule:
    """LR for an update uses its end position; commit only after AdamW succeeds."""
    def __init__(self, optimizer, total, warmup=5000000, peak=.002, final=1e-5):
        if (type(total) is not int or type(warmup) is not int or not 0 < warmup < total
                or not 0 < final <= peak or not math.isfinite(peak)):
            raise ValueError('Finite peak/final and positive warmup<total required')
        self.optimizer, self.total, self.warmup = optimizer, total, warmup
        self.peak, self.final, self.tokens = peak, final, 0
        self.last_lr = 0.
        for group in optimizer.param_groups:
            group['lr'] = self.last_lr

    def value(self, tokens):
        if not 0 <= tokens <= self.total:
            raise ValueError('Target schedule cursor outside exact teacher goal')
        if tokens <= self.warmup:
            return self.peak*tokens/self.warmup
        phase = (tokens-self.warmup)/(self.total-self.warmup)
        return self.final+(self.peak-self.final)*(1+math.cos(math.pi*phase))/2

    def prepare(self, teachers):
        if type(teachers) is not int or teachers <= 0:
            raise ValueError('Positive original teacher increment required')
        lr = self.value(self.tokens+teachers)
        for group in self.optimizer.param_groups:
            group['lr'] = lr
        return lr

    def commit(self, teachers):
        self.tokens += teachers
        self.last_lr = self.value(self.tokens)
        if any(group['lr'] != self.last_lr for group in self.optimizer.param_groups):
            raise ValueError('Committed target position differs from applied learning rate')

    def state_dict(self):
        return dict(kind='original_teacher_end_position_warmup_cosine_v1', total=self.total,
            warmup=self.warmup, peak=self.peak, final=self.final, tokens=self.tokens, last_lr=self.last_lr)

    def validate(self, state):
        if (any(state[k] != self.state_dict()[k] for k in ('kind','total','warmup','peak','final'))
                or type(state['tokens']) is not int or state['last_lr'] != self.value(state['tokens'])):
            raise ValueError('Target schedule recipe/cursor differs')

    def load_state_dict(self, state):
        self.validate(state)
        self.tokens, self.last_lr = state['tokens'], state['last_lr']
        if any(group['lr'] != self.last_lr for group in self.optimizer.param_groups):
            raise ValueError('Saved optimizer learning rate differs from target schedule')


class FreshKVAllocationTrainer(NaturalContextTrainer):
    def __init__(self, model_config, sampler, binding, batch=48, device='cuda', seed=42,
                 warmup=5000000, peak=.002, final=1e-5):
        if not isinstance(sampler, CEOnlyOriginalSampler) or type(batch) is not int or batch < 2:
            raise ValueError('Explicit CE-only TRAIN protocol and batch>=2 required')
        self.device = torch.device(device)
        self.binding = copy.deepcopy(binding)
        seed_all(seed)
        self.model = JMicroModel(copy.deepcopy(model_config)).to(self.device).train()
        count = sum(p.numel() for p in self.model.parameters())
        if count != model_config['expected_parameter_count']:
            raise ValueError('Actual unique native parameter count differs')
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=peak, weight_decay=.1)
        self.sampler = sampler
        self.scheduler = TargetPositionSchedule(self.optimizer, sum(sampler.goals.values()), warmup, peak, final)
        self.spec = dict(kind=KIND, batch=batch, seed=seed, optimizer='fresh_AdamW', weight_decay=.1,
            gradient_clip=1., dtype='bf16' if self.device.type == 'cuda' else 'fp32',
            backend='flash' if self.device.type == 'cuda' else 'math', actual_unique_parameters=count,
            goals=sampler.goals.copy(), scheduler={k:v for k,v in self.scheduler.state_dict().items()
                if k not in ('tokens','last_lr')}, head_policy='only_original_supervised_states',
            CE_policy='document_local1024_context512_original_targets_once', contrast=False)
        self.lineage = dict(kind=KIND, initialization='fresh_native_seed', seed=seed,
            parent=None, learned_parent_weights_used=False, probe_weights_used=False,
            weights_role=binding.get('weights_role','verification_only'))
        self.counters = dict(update=0, supervised_tokens=0, CE_input_tokens=0, auxiliary_input_tokens=0,
            auxiliary_pairs=0, physical_input_tokens=0, original_body_bytes=0, token_digest='0'*64,
            source_teachers=dict.fromkeys(GENRES,0), source_EOS=dict.fromkeys(GENRES,0))

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if any(state[k] != self.state_dict()[k] for k in ('kind','spec','binding','lineage','model_config')):
            raise ValueError('Fresh allocation recipe/source/architecture binding differs')
        total = state['counters']['supervised_tokens']
        if (total != state['scheduler']['tokens'] or total != sum(state['counters']['source_teachers'].values())
                or state['counters']['source_teachers'] != state['sampler']['consumed']
                or state['counters']['auxiliary_input_tokens'] or state['counters']['auxiliary_pairs']):
            raise ValueError('Completed-update teacher/schedule/source accounting differs')
        self.scheduler.validate(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))

    def step(self):
        if not self.model.training:
            raise ValueError('model.train required for original teacher learning')
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        data_wait = time.monotonic()-started
        if any(r['prefix_ids'] or r['suffix_ids'] for r in rows):
            raise ValueError('No auxiliary pairs in CE-only allocation training')
        ids, _ = right_pad([r['input_ids'] for r in rows], self.device)
        targets = torch.full(ids.shape, -100, dtype=torch.long)
        for index, row in enumerate(rows):
            targets[index,:len(row['target_ids'])] = torch.tensor(row['target_ids'])
        targets = targets.to(self.device)
        supervised = sum(r['teacher_tokens'] for r in rows)
        if int(targets.ne(-100).sum()) != supervised:
            raise ValueError('Original target mask count differs')
        self.optimizer.zero_grad(set_to_none=True)
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                               enabled=self.device.type == 'cuda'):
            hidden = right_padded_hidden(self.model, ids)
            selected = targets.ne(-100)
            logits = self.model.lm_head(hidden[selected]).float()
            loss = F.cross_entropy(logits, targets[selected])
            if not torch.isfinite(loss):
                raise ValueError('Finite original teacher CE required')
            loss.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        if not 0 < float(gradient) < float('inf'):
            raise ValueError('Finite nonzero native gradient required')
        lr = self.scheduler.prepare(supervised)
        self.optimizer.step()
        self.scheduler.commit(supervised)
        self.counters['update'] += 1
        for key,value in dict(supervised_tokens=supervised, CE_input_tokens=sum(len(r['input_ids']) for r in rows),
                physical_input_tokens=ids.numel(), original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if (self.counters['source_teachers'] != self.sampler.consumed
                or self.counters['supervised_tokens'] != self.scheduler.tokens):
            raise ValueError('Committed teacher/source/schedule accounting differs')
        stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids'])
                             for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters), CE_loss=float(loss.detach()), combined_loss=float(loss.detach()),
            gradient_norm=float(gradient), CE_targets_this_update=supervised, auxiliary_inputs_this_update=0,
            physical_inputs_this_update=ids.numel(), original_windows_this_update=len(rows),
            seconds=time.monotonic()-started, data_wait_seconds=data_wait, lr=lr,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],
                         r['teacher_tokens']) for r in rows])
