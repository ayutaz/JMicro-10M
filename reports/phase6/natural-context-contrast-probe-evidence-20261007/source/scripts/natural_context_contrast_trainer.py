"""Native full-unit CE and observed prefix/suffix representation contrast.

Right padding occurs strictly after every original sequence. Causal attention
therefore protects all valid states without a quadratic padding mask; PAD
queries are never gathered or supervised. Auxiliary forwards skip the LM head.
"""
import copy
import hashlib
import json
from pathlib import Path
import random
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.model import JMicroModel
from jmicro.training import rng_state, restore_rng, seed_all, synchronize

KIND = 'native_observed_context_suffix_InfoNCE_full_CE_v1'
TEMPERATURE = 0.1
COEFFICIENT = 0.1


def host(value):
    if isinstance(value, torch.Tensor):
        return value.detach().cpu().clone()
    if isinstance(value, dict):
        return {k: host(v) for k, v in value.items()}
    if isinstance(value, list):
        return [host(v) for v in value]
    if isinstance(value, tuple):
        return tuple(host(v) for v in value)
    return copy.deepcopy(value)


def right_pad(sequences, device):
    if not sequences or any(not seq for seq in sequences):
        raise ValueError('Nonempty original sequences required')
    lengths = torch.tensor([len(s) for s in sequences], device=device)
    ids = torch.zeros((len(sequences), max(map(len, sequences))), dtype=torch.long)
    for i, seq in enumerate(sequences):
        ids[i, :len(seq)] = torch.tensor(seq)
    return ids.to(device), lengths


def right_padded_hidden(model, ids):
    """Original native decoder, same valid positions, no output head or cache."""
    if ids.shape[1] > model.config['max_position_embeddings']:
        raise ValueError('Original sequence exceeds context')
    positions = torch.arange(ids.shape[1], device=ids.device)[None].expand(ids.shape[0], -1)
    x = model.model.embed_tokens(ids)
    for layer in model.model.layers:
        x, _ = layer(x, positions, None, None, causal=True)
    return model.model.norm(x)


def symmetric_InfoNCE(prefix, suffix):
    if prefix.shape != suffix.shape or prefix.ndim != 2 or prefix.shape[0] < 2:
        raise ValueError('At least two matched distinct-family pairs required')
    with torch.autocast(prefix.device.type, enabled=False):
        left = F.normalize(prefix.float(), dim=-1)
        right = F.normalize(suffix.float(), dim=-1)
        similarity = left @ right.T
        labels = torch.arange(len(left), device=left.device)
        loss = (F.cross_entropy(similarity/TEMPERATURE, labels)
                + F.cross_entropy(similarity.T/TEMPERATURE, labels))/2
    off_diagonal = ~torch.eye(len(left), dtype=torch.bool, device=left.device)
    stats = dict(positive_cosine=similarity.diag().mean().detach(),
        distractor_cosine=similarity[off_diagonal].mean().detach(),
        representation_variance=torch.minimum(left.var(0, unbiased=False).mean(),
                                              right.var(0, unbiased=False).mean()).detach())
    return loss, stats


class FixedPairSampler:
    """Bounded implementation data only; this is not the scientific corpus."""
    def __init__(self, rows, seed=42):
        if len({r['source_family'] for r in rows}) != len(rows):
            raise ValueError('Distinct original families required')
        if len({r['full_original_body_sha256'] for r in rows}) != len(rows):
            raise ValueError('Distinct original bodies required')
        self.rows = rows
        self.signature = hashlib.sha256(json.dumps([
            (r['source_family'], r['full_original_body_sha256']) for r in rows]).encode()).hexdigest()
        self.rng = random.Random(seed)
        self.order = list(range(len(rows)))
        self.rng.shuffle(self.order)
        self.cursor = self.epochs = 0

    def take(self, size):
        if not 2 <= size <= len(self.rows):
            raise ValueError('Probe batch exceeds distinct fixed pairs')
        result, seen = [], set()
        while len(result) < size:
            if self.cursor == len(self.order):
                self.rng.shuffle(self.order)
                self.cursor = 0
                self.epochs += 1
            index = self.order[self.cursor]
            self.cursor += 1
            if index not in seen:
                result.append(self.rows[index])
                seen.add(index)
        return result

    def state_dict(self):
        return dict(kind='fixed_distinct_TRAIN_probe_pairs_v1', signature=self.signature,
            order=self.order.copy(), cursor=self.cursor, epochs=self.epochs, RNG=self.rng.getstate())

    def load_state_dict(self, state):
        if (state['kind'] != self.state_dict()['kind'] or state['signature'] != self.signature
                or sorted(state['order']) != list(range(len(self.rows)))
                or not 0 <= state['cursor'] <= len(self.rows) or state['epochs'] < 0):
            raise ValueError('Original probe sampler binding/cursor differs')
        self.order, self.cursor, self.epochs = state['order'].copy(), state['cursor'], state['epochs']
        self.rng.setstate(state['RNG'])


class NaturalContextTrainer:
    """Fresh equal optimizer policy; full accounting at completed updates."""
    def __init__(self, parent, rows, binding, batch=16, contrast=True, device='cuda', seed=42):
        self.device = torch.device(device)
        self.spec = dict(kind=KIND, batch=batch, contrast=contrast, seed=seed, lr=1e-5,
            weight_decay=0.1, temperature=TEMPERATURE, coefficient=COEFFICIENT,
            dtype='bf16' if self.device.type == 'cuda' else 'fp32',
            backend='flash' if self.device.type == 'cuda' else 'math',
            optimizer_policy='fresh_equal_AdamW_both_arms', scheduler='constant',
            original_whole_body_plus_EOS=True, no_split_EOS=True)
        self.binding = copy.deepcopy(binding)
        seed_all(seed)
        self.model = JMicroModel(parent['model_config']).to(self.device).train()
        self.model.load_state_dict(parent['model'], strict=True)
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=1e-5, weight_decay=0.1)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _: 1.0)
        self.sampler = FixedPairSampler(rows, seed)
        self.counters = dict(update=0, supervised_tokens=0, CE_input_tokens=0, auxiliary_input_tokens=0,
            auxiliary_pairs=0, physical_input_tokens=0, original_body_bytes=0,
            token_digest='0'*64)
        self.lineage = dict(parent=binding['parent'], parent_update=parent['update'],
            parent_tokens=parent['tokens'], parent_supervised_tokens=parent['supervised_tokens'],
            optimizer_policy='fresh_equal_AdamW_both_arms', probe_weights_discarded=True)

    def step(self):
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        for row in rows:
            if (not row['full_body_ids'] or any(i < 8 for i in row['full_body_ids'])
                    or not row['prefix_ids'] or not row['suffix_ids']
                    or any(i < 8 for i in row['prefix_ids'] + row['suffix_ids'])):
                raise ValueError('Original plain body/prefix/suffix IDs required')
        sequences = [[2]+r['full_body_ids'] for r in rows]
        ids, lengths = right_pad(sequences, self.device)
        targets = torch.full_like(ids, -100)
        for i, row in enumerate(rows):
            targets[i, :len(sequences[i])] = torch.tensor(row['full_body_ids']+[3], device=self.device)
        self.optimizer.zero_grad(set_to_none=True)
        auxiliary_tokens = auxiliary_physical = 0
        stats = dict(positive_cosine=0., distractor_cosine=0., representation_variance=0.)
        aux_norm = contrast_loss = 0.
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                                enabled=self.device.type == 'cuda'):
            if self.spec['contrast']:
                auxiliary = ([[2]+r['prefix_ids'] for r in rows]
                             + [[2]+r['suffix_ids'] for r in rows])
                aux_ids, aux_lengths = right_pad(auxiliary, self.device)
                hidden = right_padded_hidden(self.model, aux_ids)
                features = hidden[torch.arange(len(auxiliary), device=self.device), aux_lengths-1]
                loss, measures = symmetric_InfoNCE(features[:len(rows)], features[len(rows):])
                if not torch.isfinite(loss):
                    raise ValueError('Nonfinite native contrastive loss')
                # Separate backward frees auxiliary activations before full CE.
                (COEFFICIENT*loss).backward()
                norms = [p.grad.detach().float().norm() for p in self.model.parameters() if p.grad is not None]
                aux_norm = float(torch.stack(norms).norm())
                contrast_loss = float(loss.detach())
                stats = {k: float(v) for k, v in measures.items()}
                if not (0 < aux_norm < float('inf') and stats['representation_variance'] > 1e-10):
                    raise ValueError('Zero/nonfinite auxiliary gradient or collapsed representations')
                auxiliary_tokens = sum(map(len, auxiliary))
                auxiliary_physical = aux_ids.numel()
                del hidden, features, aux_ids, loss
            logits = self.model.lm_head(right_padded_hidden(self.model, ids)).float()
            supervised = sum(map(len, sequences))
            ce = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), targets.reshape(-1),
                                 ignore_index=-100, reduction='sum')/supervised
            if not torch.isfinite(ce):
                raise ValueError('Nonfinite full original body/EOS CE')
            ce.backward()
        gradient_norm = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0, error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        self.counters['update'] += 1
        for key, value in dict(supervised_tokens=supervised, CE_input_tokens=supervised,
            auxiliary_input_tokens=auxiliary_tokens, auxiliary_pairs=len(rows) if self.spec['contrast'] else 0,
            physical_input_tokens=ids.numel()+auxiliary_physical,
            original_body_bytes=sum(r['body_UTF8_bytes'] for r in rows)).items():
            self.counters[key] += value
        draw = json.dumps([(r['index'], r['full_body_ids'], r['prefix_ids'], r['suffix_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+draw).hexdigest()
        synchronize(self.device)
        return dict(**self.counters, CE_loss=float(ce.detach()), contrast_loss=contrast_loss,
            combined_loss=float(ce.detach())+COEFFICIENT*contrast_loss,
            auxiliary_gradient_norm=aux_norm, gradient_norm=float(gradient_norm), **stats,
            draw_indices=[r['index'] for r in rows], CE_targets_this_update=supervised,
            auxiliary_inputs_this_update=auxiliary_tokens, physical_inputs_this_update=ids.numel()+auxiliary_physical,
            seconds=time.monotonic()-started, lr=self.optimizer.param_groups[0]['lr'])

    def state_dict(self):
        return dict(kind=KIND, spec=self.spec, binding=self.binding, lineage=self.lineage,
            model_config=self.model.config, model=self.model.state_dict(), optimizer=self.optimizer.state_dict(),
            scheduler=self.scheduler.state_dict(), RNG=rng_state(), sampler=self.sampler.state_dict(),
            counters=self.counters.copy())

    def save(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix('.tmp')
        torch.save(host(self.state_dict()), temporary)
        temporary.replace(path)

    def load(self, path):
        state = torch.load(path, map_location=self.device, weights_only=False)
        if any(state[k] != self.state_dict()[k] for k in ('kind', 'spec', 'binding', 'lineage', 'model_config')):
            raise ValueError('Actual recipe/parent/source binding differs')
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = state['counters'].copy()
        # CPU RNG ByteTensors must stay on the CPU even for CUDA checkpoints.
        restore_rng(host(state['RNG']))
