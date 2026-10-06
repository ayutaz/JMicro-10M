"""One parallel greedy-history mixing pass; retain original gold targets.

This is a fixed greedy variant of parallel scheduled sampling, not an
autoregressive rollout or a likelihood-consistent objective. Sampling and
mixing have no gradient; only the final original-gold CE updates the model.
"""
import copy
import hashlib
import json
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.training import synchronize
from natural_context_contrast_corpus import NaturalCorpusTrainer, GENRES
from natural_context_contrast_trainer import right_pad, right_padded_hidden

KIND = 'native_original_gold_CE_parallel_greedy_input_mixing_v1'


def mix_inputs(ids, predictions, generator, probability):
    """Prediction at j-1 can replace body input j; boundary/PAD never changes."""
    if (ids.ndim != 2 or predictions.shape != ids.shape or
            type(probability) not in (int, float) or not 0 <= probability <= 1):
        raise ValueError('Matching causal prediction shape and finite probability required')
    eligible = (ids[:, 1:] >= 8) & (ids[:, :-1] != 0)
    selected = torch.zeros_like(ids, dtype=torch.bool)
    if probability:
        draws = torch.rand(ids.shape, generator=generator, device='cpu').to(ids.device)
        selected[:, 1:] = eligible & (draws[:, 1:] < probability)
    result = ids.clone()
    if selected.any():
        replacement = torch.zeros_like(ids)
        replacement[:, 1:] = predictions[:, :-1]
        if (replacement[selected] < 8).any():
            raise ValueError('Only model body tokens may enter the original context')
        result[selected] = replacement[selected]
    return result, selected, int(eligible.sum())


class ContextMixingTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, contrast=False,
                 device='cuda', seed=42, probability=.05):
        if contrast or probability not in (0., .05):
            raise ValueError('Fixed .05 mixing; zero only for protocol verification')
        super().__init__(parent, sampler, binding, batch, False, device, seed)
        self.spec.update(kind=KIND, context_mixing_probability=probability,
            context_mixing_passes=1, context_prediction='previous_position_greedy_body_only',
            context_prediction_gradient=False, CE_labels='unaltered_original_gold',
            mixing_rng='dedicated_CPU_generator', context_mixing_rng_seed=seed)
        self.lineage.update(kind=KIND)
        self.mixing_rng = torch.Generator(device='cpu').manual_seed(seed)
        self.mixing = dict(updates=0, eligible_positions=0, selected_positions=0,
            changed_positions=0, prediction_valid_inputs=0, prediction_physical_inputs=0,
            digest='0'*64)

    def state_dict(self):
        state = super().state_dict()
        state.update(kind=KIND, context_mixing=copy.deepcopy(self.mixing),
                     context_mixing_RNG=self.mixing_rng.get_state())
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location='cpu', weights_only=False)
        mixing, counters = state['context_mixing'], state['counters']
        if (mixing['updates'] != counters['update'] or
                not 0 <= mixing['changed_positions'] <= mixing['selected_positions'] <= mixing['eligible_positions'] or
                counters['source_teachers'] != state['sampler']['consumed'] or
                counters['supervised_tokens'] != sum(counters['source_teachers'].values()) or
                counters['auxiliary_input_tokens'] or counters['auxiliary_pairs']):
            raise ValueError('Committed original-label/mixing accounting differs')
        rng = state['context_mixing_RNG']
        if not isinstance(rng, torch.Tensor) or rng.dtype != torch.uint8 or rng.ndim != 1:
            raise ValueError('Dedicated mixing RNG state required')
        # Validate RNG before changing any trainer state.
        torch.Generator(device='cpu').set_state(rng)
        super().load(path)
        self.mixing, self.mixing_rng = copy.deepcopy(mixing), torch.Generator(device='cpu').set_state(rng)

    def step(self):
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        data_wait = time.monotonic()-started
        original, _ = right_pad([r['input_ids'] for r in rows], self.device)
        targets = torch.full_like(original, -100)
        for i, row in enumerate(rows):
            targets[i, :len(row['target_ids'])] = torch.tensor(row['target_ids'], device=self.device)
        supervised = sum(r['teacher_tokens'] for r in rows)
        if int(targets.ne(-100).sum()) != supervised:
            raise ValueError('Exact original gold target accounting required')
        probability = self.spec['context_mixing_probability']
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        prediction_inputs = prediction_physical = 0
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                                enabled=self.device.type == 'cuda'):
            predictions = torch.full_like(original, 8)
            if probability:
                with torch.no_grad():
                    hidden = right_padded_hidden(self.model, original)
                    eligible_previous = torch.zeros_like(original, dtype=torch.bool)
                    eligible_previous[:, :-1] = (original[:, 1:] >= 8) & (original[:, :-1] != 0)
                    logits = self.model.lm_head(hidden[eligible_previous]).float()
                    if not torch.isfinite(logits).all():
                        raise ValueError('Nonfinite clean-context model predictions')
                    predictions[eligible_previous] = logits[:, 8:].argmax(-1)+8
                    del hidden, logits
                prediction_inputs = sum(len(r['input_ids']) for r in rows)
                prediction_physical = original.numel()
            mixed, selected, eligible = mix_inputs(original, predictions, self.mixing_rng, probability)
            changed = int((mixed != original).sum())
            self.optimizer.zero_grad(set_to_none=True)
            hidden = right_padded_hidden(self.model, mixed)
            logits = self.model.lm_head(hidden[targets != -100]).float()
            ce = F.cross_entropy(logits, targets[targets != -100])
            if not torch.isfinite(ce): raise ValueError('Nonfinite original-gold mixed-context CE')
            ce.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        self.counters['update'] += 1
        for key, value in dict(supervised_tokens=supervised,
            CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            physical_input_tokens=original.numel(), original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed:
            raise ValueError('Completed-update original source quotas differ')
        stream = json.dumps([(r['index_byte_position'], r['index_record_sha256'],
            r['input_ids'], r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        for key, value in dict(updates=1, eligible_positions=eligible, selected_positions=int(selected.sum()),
            changed_positions=changed, prediction_valid_inputs=prediction_inputs,
            prediction_physical_inputs=prediction_physical).items():
            self.mixing[key] += value
        self.mixing['digest'] = hashlib.sha256(bytes.fromhex(self.mixing['digest'])+
            json.dumps(mixed.detach().cpu().tolist()).encode()).hexdigest()
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters), context_mixing=copy.deepcopy(self.mixing),
            CE_loss=float(ce.detach()), combined_loss=float(ce.detach()), gradient_norm=float(gradient),
            lr=self.optimizer.param_groups[0]['lr'], CE_targets_this_update=supervised,
            original_windows_this_update=len(rows), physical_inputs_this_update=original.numel(),
            prediction_valid_inputs_this_update=prediction_inputs,
            prediction_physical_inputs_this_update=prediction_physical,
            total_physical_inputs_this_update=original.numel()+prediction_physical,
            mixing_selected_this_update=int(selected.sum()), mixing_changed_this_update=changed,
            seconds=time.monotonic()-started, data_wait_seconds=data_wait,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            draw_trace=[(r['index_byte_position'], r['index_record_sha256'], r['target_first'],
                         r['target_end'], r['teacher_tokens']) for r in rows])
