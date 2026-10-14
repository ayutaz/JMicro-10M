"""One prospective intervention: inverse original-document-length weighted CE.

The existing sampled TRAIN stream and gold masks are unchanged. Each body and
its original EOS receive the same weight. Overlapping context is never gold.
This balances contributions of drawn units, not population document sampling.
"""
import copy
import hashlib
import json
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from natural_context_contrast_corpus import NaturalCorpusTrainer
from natural_context_contrast_trainer import right_pad, right_padded_hidden
from jmicro.training import synchronize

KIND = 'native_original_document_inverse_length_CE_v1'
RECIPE = dict(
    loss='sum_CE_over_original_supervised_positions_divided_by_original_document_teachers_then_normalize_weight_sum',
    denominator='original_body_tokens_plus_one_original_EOS',
    normalization='current_update_sum_of_selected_inverse_length_weights',
    clipping=None, annealing=False, auxiliary_loss=False,
    original_gold_and_stream_unchanged=True, new_parameters=0,
    optimizer='fresh_AdamW_lr1e-5_wd0.1_constant', final_clip_norm=1.,
    inference='unchanged_full_native_depth_greedy')


def document_balanced_loss(logits, targets, original_teachers):
    """Selected logits and one original total teacher count per selected token."""
    if (logits.ndim != 2 or targets.shape != (len(logits),) or not len(logits)
            or original_teachers.shape != targets.shape or original_teachers.dtype != torch.long
            or bool((original_teachers < 2).any()) or bool((targets < 0).any())
            or bool((targets >= logits.shape[1]).any())):
        raise ValueError('Nonempty selected gold and original document lengths required')
    terms = F.cross_entropy(logits.float(), targets, reduction='none')
    weights = original_teachers.float().reciprocal()
    weighted = (terms * weights).sum() / weights.sum()
    return terms.mean(), weights.mean(), weighted, weights.max() / weights.min()


def document_losses(model, ids, targets, original_teachers):
    if (ids.shape != targets.shape or original_teachers.shape != (len(ids),)
            or original_teachers.dtype != torch.long or not bool(targets.ne(-100).any())):
        raise ValueError('Aligned original gold and one original count per row required')
    selected = targets.ne(-100)
    if bool((selected.sum(-1) > original_teachers).any()):
        raise ValueError('A window cannot supervise more than its original whole document')
    lengths = original_teachers[:, None].expand_as(targets)[selected]
    logits = model.lm_head(right_padded_hidden(model, ids)[selected])
    return document_balanced_loss(logits, targets[selected], lengths)


def committed_state(state):
    if state.get('kind') != KIND or state['spec'].get('document_balance') != RECIPE:
        return False
    c, s = state['counters'], state['document_balance']
    steps = c['update']
    if (s != dict(updates=steps, positions=c['supervised_tokens'])
            or steps != state['scheduler']['last_epoch']
            or any(int(v['step']) != steps for v in state['optimizer']['state'].values())
            or c['supervised_tokens'] != sum(c['source_teachers'].values())
            or c['source_teachers'] != state['sampler']['consumed']
            or c['auxiliary_input_tokens'] or c['auxiliary_pairs'] or c['auxiliary_digest'] != '0'*64):
        return False
    def finite(value):
        if isinstance(value, torch.Tensor): return bool(torch.isfinite(value).all())
        if isinstance(value, dict): return all(finite(v) for v in value.values())
        if isinstance(value, (list, tuple)): return all(finite(v) for v in value)
        return True
    return finite(state['model']) and finite(state['optimizer'])


class DocumentBalancedTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, contrast=False, device='cuda', seed=42):
        if contrast: raise ValueError('No auxiliary or contrastive objective')
        super().__init__(parent, sampler, binding, batch, False, device, seed)
        self.spec.update(kind=KIND, document_balance=copy.deepcopy(RECIPE))
        self.lineage.update(kind=KIND)
        self.document_balance = dict(updates=0, positions=0)
        self._step_in_progress = False

    def state_dict(self):
        if self._step_in_progress: raise ValueError('Cannot save interrupted update')
        state = super().state_dict()
        state.update(kind=KIND, document_balance=copy.deepcopy(self.document_balance))
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if not committed_state(state): raise ValueError('Committed matching full state required')
        super().load(path)
        self.document_balance = copy.deepcopy(state['document_balance'])

    def step(self):
        if self._step_in_progress: raise ValueError('Resume valid checkpoint after interrupted update')
        synchronize(self.device)
        started = time.monotonic()
        self._step_in_progress = True
        rows = self.sampler.take(self.spec['batch'])
        wait = time.monotonic()-started
        ids, _ = right_pad([r['input_ids'] for r in rows], self.device)
        targets = torch.full_like(ids, -100)
        for i, r in enumerate(rows):
            targets[i, :len(r['target_ids'])] = torch.tensor(r['target_ids'], device=self.device)
        lengths = torch.tensor([r['original_body_tokens']+1 for r in rows], device=self.device)
        gold = sum(r['teacher_tokens'] for r in rows)
        if int(targets.ne(-100).sum()) != gold: raise ValueError('Exact original gold mask required')
        self.optimizer.zero_grad(set_to_none=True)
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16, enabled=self.device.type == 'cuda'):
            ce, inverse_length, combined, ratio = document_losses(self.model, ids, targets, lengths)
        if not all(bool(torch.isfinite(v)) for v in (ce, inverse_length, combined, ratio)):
            raise ValueError('Nonfinite original/weighted CE or weights')
        combined.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        self.counters['update'] += 1
        for k, v in dict(supervised_tokens=gold, CE_input_tokens=sum(len(r['input_ids']) for r in rows),
                physical_input_tokens=ids.numel(), original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[k] += v
        for r in rows:
            self.counters['source_teachers'][r['source']] += r['teacher_tokens']
            self.counters['source_EOS'][r['source']] += r['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed: raise ValueError('Committed cursor differs')
        stream = json.dumps([(r['index_byte_position'], r['index_record_sha256'], r['input_ids'], r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        self.document_balance['updates'] += 1
        self.document_balance['positions'] += gold
        self._step_in_progress = False
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters), document_balance=copy.deepcopy(self.document_balance),
            CE_loss=float(ce.detach()), balance_mean_inverse_length=float(inverse_length.detach()),
            balance_weight_ratio=float(ratio.detach()), combined_loss=float(combined.detach()),
            gradient_norm=float(gradient), lr=self.optimizer.param_groups[0]['lr'],
            CE_targets_this_update=gold, balance_positions_this_update=gold, decoder_forwards_this_update=1,
            physical_inputs_this_update=ids.numel(), seconds=time.monotonic()-started, data_wait_seconds=wait,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows), original_windows_this_update=len(rows),
            original_document_teachers=[r['original_body_tokens']+1 for r in rows],
            draw_trace=[(r['index_byte_position'], r['index_record_sha256'], r['target_first'], r['target_end'], r['teacher_tokens']) for r in rows])
