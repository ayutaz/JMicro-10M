"""Native original CE plus TRAIN whole-sentence probability decay.

New typed checkpoints, unchanged frozen native/legacy implementations. Only
completed Adam updates commit counters; an interrupted object must restore a
valid saved state before another step or save. Synthetic inputs are separate
from main gold teachers, original material RNG, and unique corpus size.
"""
import copy
import hashlib
import json
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.evaluation_boundary import require_digest
from jmicro.model import JMicroModel
from jmicro.pseudo_repetition import (COEFFICIENT, DECAY, MAX_COPIES, MAXIMUM,
                                     MAX_ROWS, repeat_rows, repetition_decay_loss)
from jmicro.training import restore_rng, synchronize
from base_fim_trainer import finite, valid_rng
from context_likelihood_trainer import validate_material
from natural_context_contrast_corpus import NaturalCorpusTrainer, GENRES
from natural_context_contrast_trainer import host, right_pad, right_padded_hidden

KIND = 'native_original_CE_TRAIN_sentence_copy_probability_decay_v1'
RECIPE = dict(coefficient=COEFFICIENT, decay=DECAY, maximum_inputs=MAXIMUM,
    maximum_copies=MAX_COPIES, minimum_copies=4, maximum_rows=MAX_ROWS,
    sentence_tokens=[8, 128], preceding_context_tokens=[8, 256],
    selection='first_eligible_complete_original_rows_distinct_family_body_no_new_draws',
    boundary='original_joint_body_token_UTF8_punctuation_no_fragment_reencoding',
    loss='mean_negative_log_one_minus_abs_current_probability_minus_detached_decayed_previous_copy',
    main_CE='unchanged_original_body_EOS', auxiliary_EOS=False,
    extra_parameters=0, additional_RNG=False)


def auxiliary_scores(model, selected, device):
    """One padded native decoder; head only original copied-sentence states."""
    ids, _ = right_pad([r['input_ids'] for r in selected], device)
    hidden = right_padded_hidden(model, ids)
    comparisons = sum(r['pseudo_target_comparisons'] for r in selected)
    total = None
    for index, row in enumerate(selected):
        first, end = row['prefix_tokens'], len(row['input_ids'])
        logits = model.lm_head(hidden[index, first:end]).float()
        targets = torch.tensor(row['target_ids'][first:end], dtype=torch.long, device=device)
        loss = repetition_decay_loss(logits, targets,
            [i-first for i in row['current_positions']],
            [i-first for i in row['previous_positions']])
        weighted = loss * row['pseudo_target_comparisons']
        total = weighted if total is None else total + weighted
    return total / comparisons, dict(valid_inputs=sum(len(r['input_ids']) for r in selected),
        physical_inputs=ids.numel(), comparisons=comparisons,
        first_copy_reference_positions=sum(r['sentence_tokens'] for r in selected))


def committed_state(state):
    """Validate typed numerical, Adam, scheduler, source and separate clocks."""
    try:
        spec, c, source, opt = (state[k] for k in ('spec', 'counters', 'sampler', 'optimizer'))
        steps, teachers = c['update'], c['supervised_tokens']
        if (state['kind'] != KIND or spec['kind'] != KIND or state['lineage']['kind'] != KIND
                or spec['sentence_decay_recipe'] != RECIPE or spec['contrast'] is not False
                or type(spec['sentence_decay_enabled']) is not bool
                or state['lineage']['optimizer_policy'] != 'fresh_equal_AdamW_both_arms'
                or spec['seed'] != source['seed'] or spec['goals'] != source['goals']
                or any(type(c[k]) is not int or c[k] < 0 for k in ('update', 'supervised_tokens',
                    'CE_input_tokens', 'physical_input_tokens', 'original_body_bytes', 'auxiliary_pairs',
                    'auxiliary_input_tokens', 'pseudo_comparisons', 'first_copy_reference_positions'))
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != source['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or not 0 <= c['auxiliary_pairs'] <= min(source['windows_emitted'], steps * MAX_ROWS)
                or not 24*c['auxiliary_pairs'] <= c['pseudo_comparisons'] <= 512*c['auxiliary_pairs']
                or not 8*c['auxiliary_pairs'] <= c['first_copy_reference_positions'] <= 128*c['auxiliary_pairs']
                or c['auxiliary_input_tokens'] > MAXIMUM*c['auxiliary_pairs']
                or c['auxiliary_input_tokens'] < c['pseudo_comparisons']
                or set(c['source_EOS']) != set(GENRES)
                or any(type(c['source_EOS'][g]) is not int
                    or not 0 <= c['source_EOS'][g] <= c['source_teachers'][g] for g in GENRES)
                or (not steps <= source['windows_emitted'] <= steps*spec['batch']
                    if steps else source['windows_emitted'] != 0)):
            return False
        validate_material(source)
        require_digest(c['token_digest'])
        require_digest(c['auxiliary_digest'])
        if not spec['sentence_decay_enabled'] and (c['auxiliary_pairs'] or c['auxiliary_input_tokens']
                or c['pseudo_comparisons'] or c['first_copy_reference_positions']
                or c['auxiliary_digest'] != '0'*64):
            return False
        with torch.device('meta'):
            model = JMicroModel(state['model_config'])
        expected = model.state_dict()
        if (state['model_config']['vocab_size'] != 4096
                or set(expected) != set(state['model'])
                or any(state['model'][k].shape != v.shape or state['model'][k].dtype != v.dtype for k, v in expected.items())
                or sum(p.numel() for p in model.parameters()) != spec['actual_unique_parameters']
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])):
            return False
        groups, parameters = opt['param_groups'], list(model.parameters())
        if len(groups) != 1:
            return False
        group = groups[0]
        identifiers = group['params']
        if (len(identifiers) != len(parameters) or len(set(identifiers)) != len(identifiers)
                or group['lr'] != 1e-5 or group['weight_decay'] != .1
                or tuple(group['betas']) != (.9, .999) or group['eps'] != 1e-8
                or state['scheduler']['_last_lr'] != [1e-5]
                or state['scheduler']['base_lrs'] != [1e-5]
                or state['scheduler']['_step_count'] != steps + 1):
            return False
        if steps:
            if set(opt['state']) != set(identifiers):
                return False
            for identifier, parameter in zip(identifiers, parameters, strict=True):
                adam = opt['state'][identifier]
                if (float(adam['step']) != steps or adam['exp_avg'].shape != parameter.shape
                        or adam['exp_avg_sq'].shape != parameter.shape
                        or adam['exp_avg'].dtype != parameter.dtype or adam['exp_avg_sq'].dtype != parameter.dtype):
                    return False
        elif opt['state']:
            return False
        return valid_rng(state['RNG']) and finite(state)
    except (KeyError, TypeError, ValueError, RuntimeError, OverflowError, AttributeError):
        return False


class PseudoRepetitionTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, device='cuda', seed=42, enabled=True):
        if type(enabled) is not bool or parent['model_config']['vocab_size'] != 4096:
            raise ValueError('Explicit native4096 repetition objective required')
        super().__init__(parent, sampler, binding, batch=batch, contrast=False, device=device, seed=seed)
        count = sum(p.numel() for p in self.model.parameters())
        if (binding.get('weights_role') not in ('verification_only', 'scientific_pseudo_repetition')
                or (binding['weights_role'] != 'verification_only' and count != 10001152)):
            raise ValueError('Explicit typed role and unchanged native10,001,152 science required')
        self.spec.update(kind=KIND, actual_unique_parameters=count,
            sentence_decay_recipe=copy.deepcopy(RECIPE), sentence_decay_enabled=enabled)
        self.lineage.update(kind=KIND)
        self.counters.update(pseudo_comparisons=0, first_copy_reference_positions=0)
        self._step_in_progress = False

    def _raw_state(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save interrupted update; restore a completed checkpoint')
        state = self._raw_state()
        if not committed_state(state):
            raise ValueError('Finite complete native/Adam/scheduler/material/auxiliary state required')
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if (not committed_state(state) or any(state[k] != self._raw_state()[k]
                for k in ('spec', 'binding', 'lineage', 'model_config'))):
            raise ValueError('Matching complete sentence-decay checkpoint required before mutation')
        current = self.sampler.state_dict()
        if any(state['sampler'][k] != current[k] for k in ('kind', 'binding', 'seed', 'goals')):
            raise ValueError('Original material binding required before mutation')
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
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
        selected = repeat_rows(rows, self.sampler.tokenizer) if self.spec['sentence_decay_enabled'] else []
        ids, _ = right_pad([r['input_ids'] for r in rows], self.device)
        targets = torch.full_like(ids, -100)
        for index, row in enumerate(rows):
            targets[index, :len(row['target_ids'])] = torch.tensor(row['target_ids'], device=self.device)
        gold = sum(r['teacher_tokens'] for r in rows)
        if int(targets.ne(-100).sum()) != gold:
            raise ValueError('Original gold teacher masks differ')
        self.optimizer.zero_grad(set_to_none=True)
        measures = dict(valid_inputs=0, physical_inputs=0, comparisons=0, first_copy_reference_positions=0)
        auxiliary_loss = auxiliary_gradient = 0.
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16, enabled=self.device.type == 'cuda'):
            if selected:
                loss, measures = auxiliary_scores(self.model, selected, self.device)
                (COEFFICIENT*loss).backward()
                auxiliary_loss = float(loss.detach())
                norms = [p.grad.detach().float().norm() for p in self.model.parameters() if p.grad is not None]
                auxiliary_gradient = float(torch.stack(norms).norm())
                if not 0 < auxiliary_gradient < float('inf'):
                    raise ValueError('Finite nonzero native auxiliary gradient required')
                del loss
            valid = targets.ne(-100)
            logits = self.model.lm_head(right_padded_hidden(self.model, ids)[valid]).float()
            ce = F.cross_entropy(logits, targets[valid])
            if not bool(torch.isfinite(ce)):
                raise ValueError('Finite original CE required')
            ce.backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        self.counters['update'] += 1
        for key, value in dict(supervised_tokens=gold,
            CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            auxiliary_input_tokens=measures['valid_inputs'], auxiliary_pairs=len(selected),
            pseudo_comparisons=measures['comparisons'],
            first_copy_reference_positions=measures['first_copy_reference_positions'],
            physical_input_tokens=ids.numel()+measures['physical_inputs'],
            original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed:
            raise ValueError('Committed main source cursor differs')
        stream = json.dumps([(r['index_byte_position'], r['index_record_sha256'],
            r['input_ids'], r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest']) + stream).hexdigest()
        if selected:
            stream = json.dumps([{key: r[key] for key in ('original_body_sha256', 'sentence_sha256',
                'prefix_tokens', 'sentence_tokens', 'copies', 'pseudo_target_comparisons')} for r in selected]).encode()
            self.counters['auxiliary_digest'] = hashlib.sha256(bytes.fromhex(self.counters['auxiliary_digest']) + stream).hexdigest()
        self._step_in_progress = False
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters), CE_loss=float(ce.detach()), auxiliary_loss=auxiliary_loss,
            combined_loss=float(ce.detach())+COEFFICIENT*auxiliary_loss,
            auxiliary_gradient_norm=auxiliary_gradient, gradient_norm=float(gradient),
            CE_targets_this_update=gold, auxiliary_rows_this_update=len(selected),
            pseudo_comparisons_this_update=measures['comparisons'],
            first_copy_reference_positions_this_update=measures['first_copy_reference_positions'],
            CE_physical_inputs_this_update=ids.numel(), auxiliary_physical_inputs_this_update=measures['physical_inputs'],
            seconds=time.monotonic()-started, data_wait_seconds=wait, lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'], r['index_record_sha256'], r['target_first'],
                         r['target_end'], r['teacher_tokens']) for r in rows])
