"""Train-only projection; the native tied vocabulary path stays unchanged.

Keep the frozen direct-feature trainer intact. Both recipes share the original
TRAIN sampler, labels and digest definition. The new head is checkpointed
separately and is never installed on the native generation model.
"""
import copy
import hashlib
import json
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.training import restore_rng, synchronize
from natural_context_contrast_corpus import NaturalCorpusTrainer
from natural_context_contrast_trainer import (host, right_pad, right_padded_hidden,
    symmetric_InfoNCE, COEFFICIENT)

KIND = 'native_original_TRAIN_CE_train_only_nonlinear_InfoNCE_v1'
HEAD_SEED = 2026100751


def make_projector(width, device):
    # Construct on CPU in a fork: neither native CPU nor CUDA RNG is advanced.
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(HEAD_SEED)
        head = torch.nn.Sequential(torch.nn.Linear(width, width, bias=False),
            torch.nn.ReLU(), torch.nn.Linear(width, width//2, bias=False))
    return head.to(device)


def gradient_norm(module):
    gradients = [p.grad.detach().float().norm() for p in module.parameters() if p.grad is not None]
    return float(torch.stack(gradients).norm()) if gradients else 0.


class ProjectedCorpusTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, contrast=True, device='cuda', seed=42):
        if not contrast:
            raise ValueError('Projection is one fixed contrastive condition; reuse the completed CE control')
        width = parent['model_config']['hidden_size']
        if width != 256 and not (str(device) == 'cpu' and binding.get('weights_role') == 'protocol_fixture'):
            raise ValueError('Scientific native256 projection geometry required')
        super().__init__(parent, sampler, binding, batch, contrast, device, seed)
        self.projector = make_projector(width, self.device).train()
        self.parameters = tuple(self.model.parameters()) + tuple(self.projector.parameters())
        self.optimizer = torch.optim.AdamW(self.parameters, lr=1e-5, weight_decay=.1)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _: 1.)
        self.spec.update(kind=KIND, projection=dict(width=width, output_width=width//2,
            activation='ReLU', bias=False, head_seed=HEAD_SEED,
            train_only=True, separate_state=True),
            native_parameters=sum(p.numel() for p in self.model.parameters()),
            train_only_parameters=sum(p.numel() for p in self.projector.parameters()),
            clipping_policy='joint_native_and_train_only_head_norm1')
        self.lineage.update(kind=KIND, train_only_head_discarded_at_native_evaluation=True)

    def state_dict(self):
        state = super().state_dict()
        state.update(kind=KIND, projector=self.projector.state_dict())
        return state

    def load(self, path):
        state = torch.load(path, map_location=self.device, weights_only=False)
        expected = self.state_dict()
        if any(state[k] != expected[k] for k in ('kind', 'spec', 'binding', 'lineage', 'model_config')):
            raise ValueError('Projected recipe/parent/source binding differs')
        self.model.load_state_dict(state['model'], strict=True)
        self.projector.load_state_dict(state['projector'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))

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
        aux_norm = head_norm = contrast_loss = 0.
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                                enabled=self.device.type == 'cuda'):
            if len(pairs) >= 2:
                auxiliary = ([[2]+r['prefix_ids'] for r in pairs]+[[2]+r['suffix_ids'] for r in pairs])
                aux_ids, lengths = right_pad(auxiliary, self.device)
                hidden = right_padded_hidden(self.model, aux_ids)
                features = hidden[torch.arange(len(auxiliary), device=self.device), lengths-1]
                projected = self.projector(features)
                loss, measures = symmetric_InfoNCE(projected[:len(pairs)], projected[len(pairs):])
                if not torch.isfinite(loss):
                    raise ValueError('Nonfinite projected corpus contrastive loss')
                (COEFFICIENT*loss).backward()
                aux_norm, head_norm = gradient_norm(self.model), gradient_norm(self.projector)
                stats = {k: float(v) for k, v in measures.items()}
                if not (0 < aux_norm < float('inf') and 0 < head_norm < float('inf')
                        and stats['representation_variance'] > 1e-10):
                    raise ValueError('Nonfinite/zero shared or head gradient or collapsed projected features')
                contrast_loss = float(loss.detach())
                auxiliary_tokens, auxiliary_physical, pairs_used = sum(map(len, auxiliary)), aux_ids.numel(), len(pairs)
                del hidden, features, projected, aux_ids, loss
            hidden = right_padded_hidden(self.model, ids)
            selected = targets != -100
            logits = self.model.lm_head(hidden[selected]).float()
            ce = F.cross_entropy(logits, targets[selected])
            if not torch.isfinite(ce):
                raise ValueError('Nonfinite original corpus CE')
            ce.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.parameters, 1., error_if_nonfinite=True)
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
            train_only_head_gradient_norm=head_norm, gradient_norm=float(gradient), **stats,
            CE_targets_this_update=supervised, auxiliary_inputs_this_update=auxiliary_tokens,
            physical_inputs_this_update=ids.numel()+auxiliary_physical,
            eligible_pairs_this_update=len(pairs), auxiliary_pairs_this_update=pairs_used,
            original_windows_this_update=len(rows), seconds=time.monotonic()-started,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            data_wait_seconds=data_wait, lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'], r['index_record_sha256'], r['target_first'],
                         r['target_end'], r['teacher_tokens']) for r in rows])
