"""Original accepted TRAIN units, exact genre teachers, native contrastive CE.

Reuse prior index verification with identity guards; random-access bounded
records avoid rescanning13GB. Within genre sampling is index-byte weighted,
not uniform documents. Both science arms consume exactly the same CE stream.
"""
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import random
import re
import time

import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.experiment import sha256
from jmicro.training import synchronize
from natural_context_contrast_trainer import (NaturalContextTrainer, right_pad,
    right_padded_hidden, symmetric_InfoNCE, COEFFICIENT)

GENRES = ('web', 'textbook', 'story')
KIND = 'native_original_TRAIN_windowed_CE_observed_context_InfoNCE_v1'


def document_windows(body, context=1024, stride=512):
    """Each original body token and original EOS once, no fragment BOS/EOS."""
    if not body or not 1 <= stride < context:
        raise ValueError('Nonempty original unit and stride<context required')
    serialized = [2]+body+[3]
    for first in range(1, len(serialized), stride):
        end = min(first+stride, len(serialized))
        start = max(0, end-1-context)
        inputs = serialized[start:end-1]
        targets = [-100 if position < first else serialized[position]
                   for position in range(start+1, end)]
        yield dict(input_ids=inputs, target_ids=targets, target_first=first, target_end=end,
                   input_start=start)


def observed_pair(body_ids, tokenizer):
    """Keep every unit for CE, independently decide auxiliary eligibility."""
    raw = tokenizer.decode_bytes(body_ids)
    if len(body_ids) > 2046:
        return raw, [], [], 'whole_unit_too_long_for_two_original_contexts'
    text = raw.decode('utf-8')
    if tokenizer.encode(text) != body_ids:
        raise ValueError('Original accepted body token/byte round trip differs')
    cuts = [m.end() for m in re.finditer(r'[。！？](?:[」』）)]*)|\n', text)]
    cuts.sort(key=lambda n: (abs(n-len(text)/2), n))
    for cut in cuts:
        prefix, suffix = text[:cut], text[cut:]
        left, right = tokenizer.encode(prefix), tokenizer.encode(suffix)
        if (16 <= len(left) <= 1023 and 16 <= len(right) <= 1023
                and left == body_ids[:len(left)]
                and tokenizer.decode_bytes(left) == prefix.encode()
                and tokenizer.decode_bytes(right) == suffix.encode()):
            return raw, left, right, 'original_sentence_or_LF_boundary'
    return raw, [], [], 'no_original_codec_stable_sentence_pair'


class OriginalTrainCorpusSampler:
    def __init__(self, pool, manifest_sha256, tokenizer, goals, seed=42):
        self.pool = Path(pool)
        if set(goals) != set(GENRES) or any(type(n) is not int or n <= 0 for n in goals.values()):
            raise ValueError('Positive exact per-genre teacher goals required')
        if sha256(self.pool/'manifest.json') != manifest_sha256:
            raise ValueError('Accepted original source manifest differs')
        manifest = json.loads((self.pool/'manifest.json').read_text())
        train = manifest['splits']['train']
        self.index = self.pool/'train.index.jsonl'
        self.stream_path = self.pool/'train.bin'
        index_stat, token_stat = self.index.stat(), self.stream_path.stat()
        ready_path = self.pool/('.compact-index-'+manifest_sha256[:16])/'ready.json'
        ready = json.loads(ready_path.read_text())
        saved = ready['binding']
        if (not ready['source_hash_verified_during_single_parse']
                or saved['manifest_sha256'] != manifest_sha256
                or saved['index_sha256'] != train['index_sha256']
                or (saved['index_size'], saved['index_mtime_ns']) != (index_stat.st_size, index_stat.st_mtime_ns)
                or token_stat.st_size != train['tokens']*2):
            raise ValueError('Prior verified TRAIN index/stream identity differs; no rescan fallback')
        self.binding = dict(manifest_sha256=manifest_sha256, index_sha256=train['index_sha256'],
            index_size=index_stat.st_size, index_mtime_ns=index_stat.st_mtime_ns,
            stream_size=token_stat.st_size, stream_mtime_ns=token_stat.st_mtime_ns,
            ready_sha256=sha256(ready_path), pool=str(self.pool))
        self.tokens = np.memmap(self.stream_path, dtype='<u2', mode='r')
        self.handle = self.index.open('rb')
        self.tokenizer = tokenizer
        self.byte_lengths = [0 if i < 8 else len(tokenizer.decode_bytes([i]))
                             for i in range(tokenizer.vocab_size)]
        self.goals = goals.copy()
        self.seed = seed
        self.rng = random.Random(seed)
        self.consumed = dict.fromkeys(GENRES, 0)
        self.pending = {g: [] for g in GENRES}
        self.draws = self.documents_drawn = self.windows_emitted = 0
        self.auxiliary_reasons = Counter()

    @property
    def exhausted(self):
        return self.consumed == self.goals

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
            original, left, right, reason = observed_pair(body, self.tokenizer)
            digest = hashlib.sha256(original).hexdigest()
            if digest != record['canonical_sha256']:
                raise ValueError('Original accepted unit bytes differ')
            metadata = dict(source=genre, source_family=record['source_family'],
                full_original_body_sha256=digest, index_byte_position=location,
                index_record_sha256=hashlib.sha256(raw).hexdigest(), original_body_tokens=count,
                original_body_UTF8_bytes=len(original), auxiliary_eligibility=reason)
            windows = list(document_windows(body))
            for i, window in enumerate(windows):
                window.update(metadata, prefix_ids=left if i == 0 else [],
                    suffix_ids=right if i == 0 else [], original_document_first_window=i == 0)
            self.pending[genre] = windows
            self.documents_drawn += 1
            self.auxiliary_reasons[reason] += 1
            return
        raise RuntimeError('Fixed4096 bounded index draws lack requested genre; do not reroll unchanged failure')

    def take(self, size):
        if size < 2 or self.exhausted:
            raise ValueError('Nonexhausted original source and batch>=2 required')
        rows = []
        for _ in range(size):
            active = [g for g in GENRES if self.consumed[g] < self.goals[g]]
            if not active:
                break
            genre = min(active, key=lambda g: self.consumed[g]/self.goals[g])
            if not self.pending[genre]:
                self._draw_document(genre)
            row = self.pending[genre].pop(0)
            row['target_ids'] = row['target_ids'].copy()
            remaining = self.goals[genre]-self.consumed[genre]
            positions = [i for i, n in enumerate(row['target_ids']) if n != -100]
            for position in positions[remaining:]:
                row['target_ids'][position] = -100
            teachers = min(len(positions), remaining)
            self.consumed[genre] += teachers
            row['teacher_tokens'] = teachers
            row['teacher_body_bytes'] = sum(self.byte_lengths[i] for i in row['target_ids'] if i >= 8)
            row['original_EOS_targets'] = row['target_ids'].count(3)
            rows.append(row)
            self.windows_emitted += 1
        return rows

    def state_dict(self):
        return dict(kind='bounded_original_TRAIN_index_byte_draw_genre_quota_windows_v1',
            binding=self.binding.copy(), seed=self.seed, goals=self.goals.copy(),
            RNG=self.rng.getstate(), consumed=self.consumed.copy(), pending=copy.deepcopy(self.pending),
            draws=self.draws, documents_drawn=self.documents_drawn, windows_emitted=self.windows_emitted,
            auxiliary_reasons=dict(self.auxiliary_reasons))

    def load_state_dict(self, state):
        if any(state[k] != self.state_dict()[k] for k in ('kind', 'binding', 'seed', 'goals')):
            raise ValueError('Original corpus sampler recipe/binding differs')
        if set(state['consumed']) != set(GENRES) or any(
                type(v) is not int or not 0 <= v <= self.goals[g] for g, v in state['consumed'].items()):
            raise ValueError('Original source teacher quota cursor invalid')
        self.rng.setstate(state['RNG'])
        self.consumed = state['consumed'].copy()
        self.pending = copy.deepcopy(state['pending'])
        for key in ('draws', 'documents_drawn', 'windows_emitted'):
            setattr(self, key, state[key])
        self.auxiliary_reasons = Counter(state['auxiliary_reasons'])


class NaturalCorpusTrainer(NaturalContextTrainer):
    def __init__(self, parent, sampler, binding, batch=64, contrast=True, device='cuda', seed=42):
        super().__init__(parent, [], binding, batch, contrast, device, seed)
        self.sampler = sampler
        self.spec.update(kind=KIND, CE_policy='document_local1024_context512_target_stride_original_EOS_once',
            head_policy='only_supervised_valid_hidden_states_no_PAD_or_overlap_logits',
            auxiliary_policy='first_window_observed_pair_once_per_draw_deduplicate_family_and_body_in_batch',
            goals=sampler.goals.copy())
        self.counters.update(source_teachers=dict.fromkeys(GENRES, 0), source_EOS=dict.fromkeys(GENRES, 0),
            auxiliary_digest='0'*64)
        self.lineage.pop('probe_weights_discarded', None)
        self.lineage.update(kind=KIND, weights_role=binding.get('weights_role', 'verification_only'))

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def step(self):
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        data_wait = time.monotonic()-started
        ids, _ = right_pad([r['input_ids'] for r in rows], self.device)
        targets = torch.full_like(ids, -100)
        for i, row in enumerate(rows):
            targets[i, :len(row['target_ids'])] = torch.tensor(row['target_ids'], device=self.device)
        pairs, families, bodies = [], set(), set()
        for row in rows:
            if (row['prefix_ids'] and row['suffix_ids'] and row['source_family'] not in families
                    and row['full_original_body_sha256'] not in bodies):
                pairs.append(row)
                families.add(row['source_family'])
                bodies.add(row['full_original_body_sha256'])
        self.optimizer.zero_grad(set_to_none=True)
        auxiliary_tokens = auxiliary_physical = pairs_used = 0
        stats = dict(positive_cosine=0., distractor_cosine=0., representation_variance=0.)
        aux_norm = contrast_loss = 0.
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                                enabled=self.device.type == 'cuda'):
            if self.spec['contrast'] and len(pairs) >= 2:
                auxiliary = ([[2]+r['prefix_ids'] for r in pairs]+[[2]+r['suffix_ids'] for r in pairs])
                aux_ids, lengths = right_pad(auxiliary, self.device)
                hidden = right_padded_hidden(self.model, aux_ids)
                features = hidden[torch.arange(len(auxiliary), device=self.device), lengths-1]
                loss, measures = symmetric_InfoNCE(features[:len(pairs)], features[len(pairs):])
                if not torch.isfinite(loss):
                    raise ValueError('Nonfinite native corpus contrastive loss')
                (COEFFICIENT*loss).backward()
                aux_norm = float(torch.stack([p.grad.detach().float().norm()
                    for p in self.model.parameters() if p.grad is not None]).norm())
                stats = {k: float(v) for k, v in measures.items()}
                if not (0 < aux_norm < float('inf') and stats['representation_variance'] > 1e-10):
                    raise ValueError('Nonfinite/zero auxiliary gradient or collapsed native features')
                contrast_loss = float(loss.detach())
                auxiliary_tokens, auxiliary_physical, pairs_used = sum(map(len, auxiliary)), aux_ids.numel(), len(pairs)
                del hidden, features, aux_ids, loss
            hidden = right_padded_hidden(self.model, ids)
            # Avoid the large vocabulary projection for padding and overlap.
            selected = targets != -100
            logits = self.model.lm_head(hidden[selected]).float()
            ce = F.cross_entropy(logits, targets[selected])
            if not torch.isfinite(ce):
                raise ValueError('Nonfinite original corpus CE')
            ce.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        supervised = sum(r['teacher_tokens'] for r in rows)
        self.counters['update'] += 1
        for key, value in dict(supervised_tokens=supervised,
            CE_input_tokens=sum(len(r['input_ids']) for r in rows), auxiliary_input_tokens=auxiliary_tokens,
            auxiliary_pairs=pairs_used, physical_input_tokens=ids.numel()+auxiliary_physical,
            original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed:
            raise ValueError('Completed-update source quotas differ')
        stream = json.dumps([(r['index_byte_position'], r['index_record_sha256'],
            r['input_ids'], r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        if pairs_used:
            stream = json.dumps([(r['full_original_body_sha256'], r['prefix_ids'], r['suffix_ids']) for r in pairs]).encode()
            self.counters['auxiliary_digest'] = hashlib.sha256(bytes.fromhex(self.counters['auxiliary_digest'])+stream).hexdigest()
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters), CE_loss=float(ce.detach()), contrast_loss=contrast_loss,
            combined_loss=float(ce.detach())+COEFFICIENT*contrast_loss, auxiliary_gradient_norm=aux_norm,
            gradient_norm=float(gradient), **stats, CE_targets_this_update=supervised,
            auxiliary_inputs_this_update=auxiliary_tokens, physical_inputs_this_update=ids.numel()+auxiliary_physical,
            eligible_pairs_this_update=len(pairs), auxiliary_pairs_this_update=pairs_used,
            original_windows_this_update=len(rows), seconds=time.monotonic()-started,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            data_wait_seconds=data_wait, lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'], r['index_record_sha256'], r['target_first'],
                         r['target_end'], r['teacher_tokens']) for r in rows])
