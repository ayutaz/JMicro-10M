"""Native original CE plus same-suffix/equal-length context likelihood contrast.

New typed checkpoint; frozen legacy trainer/model sources stay intact. FIFO
commits only with a completed Adam update. Interrupted objects cannot save or
continue until restored from a valid complete checkpoint.
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

from jmicro.context_likelihood import COEFFICIENT, ContextFIFO, original_anchors, pair_loss
from jmicro.evaluation_boundary import require_digest
from jmicro.model import JMicroModel
from jmicro.training import restore_rng, synchronize
from base_fim_trainer import finite, valid_rng
from natural_context_contrast_corpus import NaturalCorpusTrainer, GENRES
from natural_context_contrast_trainer import host, right_pad, right_padded_hidden

KIND = 'native_original_CE_equal_length_context_suffix_likelihood_v1'
RECIPE = dict(coefficient=COEFFICIENT, suffix_score='sum_native_conditional_body_log_likelihood',
    loss='mean_softplus_wrong_context_minus_original_context',
    contexts='previous_completed_updates_FIFO128_oldest_same_genre_exact_prefix_length_distinct_family_body_prefix_suffix',
    anchors='complete_fully_main_supervised_first_window_body_plus_EOS_at_most512_observed_sentence_or_LF',
    labels='identical_original_joint_suffix_body_no_auxiliary_EOS', extra_parameters=0)


def validate_material(state):
    if (state['kind'] != 'bounded_original_TRAIN_index_byte_draw_genre_quota_windows_v1'
            or set(state['consumed']) != set(GENRES) or set(state['goals']) != set(GENRES)
            or set(state['pending']) != set(GENRES)
            or any(type(state['consumed'][g]) is not int
                   or not 0 <= state['consumed'][g] <= state['goals'][g] for g in GENRES)
            or any(type(state[k]) is not int or state[k] < 0 for k in ('draws', 'documents_drawn', 'windows_emitted'))
            or not state['documents_drawn'] <= state['draws']
            or not state['documents_drawn'] <= state['windows_emitted']):
        raise ValueError('Original source counters/quota recipe differ')
    random.Random().setstate(state['RNG'])
    if (any(type(v) is not int or v < 0 for v in state['auxiliary_reasons'].values())
            or sum(state['auxiliary_reasons'].values()) != state['documents_drawn']):
        raise ValueError('Original document eligibility clock differs')
    for genre, windows in state['pending'].items():
        if not isinstance(windows, list):
            raise ValueError('Original pending windows must be lists')
        for row in windows:
            ids, labels = row['input_ids'], row['target_ids']
            start, first, end = row['input_start'], row['target_first'], row['target_end']
            if (row['source'] != genre or not 0 < len(ids) == len(labels) <= 1024
                    or any(type(i) is not int or not (i == 2 or 8 <= i < 4096) for i in ids)
                    or any(type(i) is not int or not (i in (-100, 3) or 8 <= i < 4096) for i in labels)
                    or any(type(v) is not int for v in (start, first, end))
                    or not 0 <= start < first < end <= row['original_body_tokens'] + 2
                    or len(ids) != end - 1 - start
                    or labels[:max(0, first - 1 - start)] != [-100] * max(0, first - 1 - start)
                    or any(i == -100 for i in labels[max(0, first - 1 - start):])
                    or (labels[-1] == 3) != (end == row['original_body_tokens'] + 2)
                    or 3 in labels[:-1]):
                raise ValueError('Original pending window/mask/EOS differs')
            require_digest(row['full_original_body_sha256'])
            require_digest(row['index_record_sha256'])


def suffix_scores(model, pairs, device):
    """Only selected original suffix positions reach the vocabulary head."""
    sequences = [pair[side] for pair in pairs for side in ('positive', 'negative')]
    ids, _ = right_pad([s['input_ids'] for s in sequences], device)
    targets = torch.full_like(ids, -100)
    for i, sequence in enumerate(sequences):
        targets[i, :len(sequence['target_ids'])] = torch.tensor(sequence['target_ids'], device=device)
    selected = targets.ne(-100)
    logits = model.lm_head(right_padded_hidden(model, ids)[selected]).float()
    losses = F.cross_entropy(logits, targets[selected], reduction='none')
    counts = selected.sum(-1).tolist()
    scores = torch.stack([-row.sum() for row in losses.split(counts)])
    if not bool(torch.isfinite(scores).all()):
        raise ValueError('Finite original suffix likelihoods required')
    return scores[::2], scores[1::2], dict(
        valid_inputs=sum(len(s['input_ids']) for s in sequences),
        physical_inputs=ids.numel(), target_evaluations=int(selected.sum()))


def committed_state(state):
    try:
        spec, c, source, opt = (state[k] for k in ('spec', 'counters', 'sampler', 'optimizer'))
        if (state['kind'] != KIND or spec['kind'] != KIND or spec['likelihood_recipe'] != RECIPE
                or state['lineage']['kind'] != KIND or spec['contrast'] is not False
                or state['lineage']['optimizer_policy'] != 'fresh_equal_AdamW_both_arms'
                or type(spec['likelihood_contrast_enabled']) is not bool
                or spec['seed'] != source['seed'] or spec['goals'] != source['goals']):
            return False
        steps, teachers = c['update'], c['supervised_tokens']
        if (type(steps) is not int or type(teachers) is not int or steps < 0 or teachers < 0
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != source['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or not 0 <= c['auxiliary_pairs'] <= c['eligible_anchors_committed'] <= source['windows_emitted']
                or (not steps <= source['windows_emitted'] <= steps * spec['batch']
                    if steps else source['windows_emitted'] != 0)):
            return False
        validate_material(source)
        # Explicit separate integer clocks for likelihood evaluations/FIFO.
        if (any(type(c[k]) is not int or c[k] < 0 for k in ('auxiliary_pairs', 'auxiliary_input_tokens',
                'auxiliary_target_evaluations', 'eligible_anchors_committed'))
                or state['context_FIFO']['committed_anchors'] != c['eligible_anchors_committed']
                or c['auxiliary_target_evaluations'] % 2 or c['auxiliary_target_evaluations'] < 32 * c['auxiliary_pairs']):
            return False
        memory = ContextFIFO(state['binding'])
        memory.load_state_dict(state['context_FIFO'])
        if not spec['likelihood_contrast_enabled'] and (
                c['auxiliary_pairs'] or c['auxiliary_input_tokens'] or c['auxiliary_target_evaluations']
                or c['eligible_anchors_committed'] or c['auxiliary_digest'] != '0' * 64):
            return False
        with torch.device('meta'):
            model = JMicroModel(state['model_config'])
        expected = model.state_dict()
        if (set(expected) != set(state['model'])
                or any(state['model'][k].shape != v.shape or state['model'][k].dtype != v.dtype for k, v in expected.items())
                or sum(p.numel() for p in model.parameters()) != spec['actual_unique_parameters']
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])):
            return False
        groups = opt['param_groups']
        if len(groups) != 1:
            return False
        group, parameters = groups[0], list(model.parameters())
        identifiers = group['params']
        if (len(identifiers) != len(parameters) or len(set(identifiers)) != len(identifiers)
                or group['lr'] != 1e-5 or group['weight_decay'] != .1
                or tuple(group['betas']) != (.9, .999) or group['eps'] != 1e-8
                or state['scheduler']['_last_lr'] != [1e-5]
                or state['scheduler']['base_lrs'] != [1e-5]
                or state['scheduler']['_step_count'] != steps + 1):
            return False
        if not steps:
            if opt['state']:
                return False
        else:
            if set(opt['state']) != set(identifiers):
                return False
            for identifier, parameter in zip(identifiers, parameters, strict=True):
                adam = opt['state'][identifier]
                if (float(adam['step']) != steps or adam['exp_avg'].shape != parameter.shape
                        or adam['exp_avg_sq'].shape != parameter.shape
                        or adam['exp_avg'].dtype != parameter.dtype or adam['exp_avg_sq'].dtype != parameter.dtype):
                    return False
        return valid_rng(state['RNG']) and finite(state)
    except (KeyError, TypeError, ValueError, RuntimeError, OverflowError, AttributeError):
        return False


class ContextLikelihoodTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, device='cuda', seed=42, enabled=True):
        super().__init__(parent, sampler, binding, batch=batch, contrast=False, device=device, seed=seed)
        count = sum(p.numel() for p in self.model.parameters())
        if binding.get('weights_role') != 'verification_only' and count != 10001152:
            raise ValueError('Unchanged native10,001,152 parameters required for science')
        self.spec.update(kind=KIND, actual_unique_parameters=count, likelihood_recipe=copy.deepcopy(RECIPE),
                         likelihood_contrast_enabled=enabled)
        self.lineage.update(kind=KIND)
        self.counters.update(auxiliary_target_evaluations=0, eligible_anchors_committed=0)
        self.context_FIFO = ContextFIFO(binding)
        self._step_in_progress = False

    def _raw_state(self):
        state = super().state_dict()
        state.update(kind=KIND, context_FIFO=self.context_FIFO.state_dict())
        return state

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save interrupted update; restore completed checkpoint')
        state = self._raw_state()
        if not committed_state(state):
            raise ValueError('Finite complete native/Adam/scheduler/source/FIFO state required')
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if (not committed_state(state) or any(state[k] != self._raw_state()[k]
                for k in ('spec', 'binding', 'lineage', 'model_config'))):
            raise ValueError('Matching complete likelihood checkpoint required before mutation')
        memory = ContextFIFO(self.binding)
        memory.load_state_dict(state['context_FIFO'])
        # Validate the legacy material binding/quota/RNG before any mutation.
        current_source = self.sampler.state_dict()
        if any(state['sampler'][k] != current_source[k] for k in ('kind', 'binding', 'seed', 'goals')):
            raise ValueError('Unchanged original material sampler binding required')
        for genre in GENRES:
            value = state['sampler']['consumed'][genre]
            if type(value) is not int or not 0 <= value <= self.sampler.goals[genre]:
                raise ValueError('Original completed teacher quotas differ')
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        self.context_FIFO = memory
        restore_rng(host(state['RNG']))
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress or not self.model.training:
            raise ValueError('Train mode and valid completed-update resume required')
        self._step_in_progress = True
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        wait = time.monotonic() - started
        anchors = original_anchors(rows, self.sampler.tokenizer) if self.spec['likelihood_contrast_enabled'] else []
        pairs = self.context_FIFO.select(anchors)
        ids, _ = right_pad([r['input_ids'] for r in rows], self.device)
        targets = torch.full_like(ids, -100)
        for i, row in enumerate(rows):
            targets[i, :len(row['target_ids'])] = torch.tensor(row['target_ids'], device=self.device)
        gold = sum(r['teacher_tokens'] for r in rows)
        if int(targets.ne(-100).sum()) != gold:
            raise ValueError('Original selected main CE labels differ')
        self.optimizer.zero_grad(set_to_none=True)
        measures = dict(valid_inputs=0, physical_inputs=0, target_evaluations=0)
        auxiliary_loss = auxiliary_gradient = positive_margin = 0.
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16, enabled=self.device.type == 'cuda'):
            if pairs:
                positive, negative, measures = suffix_scores(self.model, pairs, self.device)
                loss = pair_loss(positive, negative)
                (COEFFICIENT * loss).backward()
                auxiliary_loss = float(loss.detach())
                positive_margin = float((positive - negative).mean().detach())
                norms = [p.grad.detach().float().norm() for p in self.model.parameters() if p.grad is not None]
                auxiliary_gradient = float(torch.stack(norms).norm())
                if not 0 < auxiliary_gradient < float('inf'):
                    raise ValueError('Finite nonzero vocabulary-path auxiliary gradient required')
                del positive, negative, loss
            selected = targets.ne(-100)
            logits = self.model.lm_head(right_padded_hidden(self.model, ids)[selected]).float()
            ce = F.cross_entropy(logits, targets[selected])
            if not bool(torch.isfinite(ce)):
                raise ValueError('Finite original CE required')
            ce.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        self.context_FIFO.commit(anchors)
        self.counters['update'] += 1
        for key, value in dict(supervised_tokens=gold, CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            auxiliary_input_tokens=measures['valid_inputs'], auxiliary_target_evaluations=measures['target_evaluations'],
            auxiliary_pairs=len(pairs), physical_input_tokens=ids.numel() + measures['physical_inputs'],
            original_body_bytes=sum(r['teacher_body_bytes'] for r in rows), eligible_anchors_committed=len(anchors)).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed:
            raise ValueError('Completed original source cursor differs')
        stream = json.dumps([(r['index_byte_position'], r['index_record_sha256'], r['input_ids'], r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest']) + stream).hexdigest()
        if pairs:
            stream = json.dumps([{k: pair[k] for k in ('positive_body_sha256', 'negative_body_sha256',
                'positive_prefix_sha256', 'negative_prefix_sha256', 'suffix_sha256', 'prefix_tokens', 'suffix_tokens')}
                for pair in pairs]).encode()
            self.counters['auxiliary_digest'] = hashlib.sha256(bytes.fromhex(self.counters['auxiliary_digest']) + stream).hexdigest()
        self._step_in_progress = False
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters), CE_loss=float(ce.detach()), auxiliary_loss=auxiliary_loss,
            combined_loss=float(ce.detach()) + COEFFICIENT * auxiliary_loss,
            auxiliary_gradient_norm=auxiliary_gradient, positive_context_margin=positive_margin,
            gradient_norm=float(gradient), CE_targets_this_update=gold, auxiliary_pairs_this_update=len(pairs),
            repeated_auxiliary_likelihood_targets_this_update=measures['target_evaluations'],
            eligible_anchors_this_update=len(anchors), CE_physical_inputs_this_update=ids.numel(),
            auxiliary_physical_inputs_this_update=measures['physical_inputs'],
            seconds=time.monotonic() - started, data_wait_seconds=wait, lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'], r['index_record_sha256'], r['target_first'], r['target_end'], r['teacher_tokens']) for r in rows])
