"""Exact original padded tensors with one CPU batch prefetched during learning.

Both arms change native attention at conversion and use identical native
weights/zero gate coordinates. Both explicitly use mathematical SDPA with a
Pinned tiled BF16 training plus FP32 log gates and math FP32 inference. Mathematical SDPA context controls CPU/inference fallback only; explicit CUDA fused traversal does not use SDPA dispatch. No bitwise reference update parity or CUDA qualification is claimed by CPU tests.
Original teachers/source clocks are unchanged. Projection-element operations
are additional compute, not extra labels, data or model-quality evidence.
"""
import copy
import hashlib
import json
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.forgetting_attention_shared_rope import (SharedRopeForgettingModel as ForgettingModel, native_config, TAG, POLICY, ARMS, IMPLEMENTATION, CANONICAL_POLICY, ROPE_POLICY)
from forgetting_attention_prefetch_loader import PrefetchedOriginalSampler, LOADER_POLICY
from jmicro.evaluation_boundary import require_digest
from jmicro.training import restore_rng
from base_fim_trainer import finite, valid_rng
from context_likelihood_trainer import validate_material
from natural_context_contrast_corpus import NaturalCorpusTrainer, GENRES
from natural_context_contrast_trainer import host, right_pad, synchronize

KIND = 'native_original_CE_forgetting_attention_shared_rope_v1'
OPTIMIZER_POLICY = 'fresh_AdamW_original_coordinates_plus_forget_projection'


def committed_state(state):
    try:
        spec, c, source, opt = (state[k] for k in ('spec', 'counters', 'sampler', 'optimizer'))
        original = native_config(state['model_config'])
        steps, teachers = c['update'], c['supervised_tokens']
        if (state['kind'] != KIND or spec['kind'] != KIND or state['lineage']['kind'] != KIND
                or spec['forgetting_policy'] != POLICY or spec['forgetting_arm'] not in ARMS
                or spec['forgetting_arm'] != state['model_config'][TAG]['arm']
                or spec['original_model_config'] != original or spec['contrast'] is not False
                or spec['attention_backend'] != 'pinned_author_tiled_BF16_shared_RoPE_canonical64_FP32_cache_v1'
                or spec['shared_RoPE_policy'] != ROPE_POLICY
                or state['lineage']['shared_RoPE_policy'] != ROPE_POLICY
                or spec['loader_policy'] != LOADER_POLICY
                or state['lineage']['loader_policy'] != LOADER_POLICY
                or spec['FP32_arithmetic_policy'] != CANONICAL_POLICY
                or state['lineage']['FP32_arithmetic_policy'] != CANONICAL_POLICY
                or spec['attention_implementation'] != IMPLEMENTATION
                or state['lineage']['attention_implementation'] != IMPLEMENTATION
                or spec['CE_decoder_traversal'] != 'explicit_original_attention_cumulative_forget_bias'
                or spec['gradient_clip_policy'] != 'all_original_plus_forget_projection_coordinates'
                or state['lineage']['optimizer_policy'] != OPTIMIZER_POLICY
                or spec['seed'] != source['seed'] or spec['goals'] != source['goals']
                or any(type(c[k]) is not int or c[k] < 0 for k in ('update', 'supervised_tokens',
                    'CE_input_tokens', 'physical_input_tokens', 'original_body_bytes',
                    'forget_gate_projection_elements'))
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != source['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or c['auxiliary_pairs'] != 0 or c['auxiliary_input_tokens'] != 0
                or c['auxiliary_digest'] != '0'*64
                or c['forget_gate_projection_elements'] != c['physical_input_tokens']*original['num_hidden_layers']*original['num_attention_heads']*(original['hidden_size']+1)
                or set(c['source_EOS']) != set(GENRES)
                or any(type(c['source_EOS'][g]) is not int
                    or not 0 <= c['source_EOS'][g] <= c['source_teachers'][g] for g in GENRES)
                or (not steps <= source['windows_emitted'] <= steps*spec['batch']
                    if steps else source['windows_emitted'] != 0)):
            return False
        validate_material(source)
        require_digest(c['token_digest'])
        with torch.device('meta'):
            model = ForgettingModel(state['model_config'])
        expected = model.state_dict()
        if (set(expected) != set(state['model'])
                or any(state['model'][k].shape != v.shape or state['model'][k].dtype != v.dtype for k,v in expected.items())
                or sum(p.numel() for p in model.parameters()) != spec['actual_unique_parameters']
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])
                or (spec['forgetting_arm'] == 'static_half_forget' and any(torch.count_nonzero(v)
                    for k,v in state['model'].items() if '.forget_proj.' in k))):
            return False
        groups, parameters = opt['param_groups'], list(model.parameters())
        if len(groups) != 1:
            return False
        group = groups[0]
        identifiers = group['params']
        if (len(identifiers) != len(parameters) or len(set(identifiers)) != len(identifiers)
                or group['lr'] != 1e-5 or group['weight_decay'] != .1
                or tuple(group['betas']) != (.9, .999) or group['eps'] != 1e-8
                or state['scheduler']['_last_lr'] != [1e-5] or state['scheduler']['base_lrs'] != [1e-5]
                or state['scheduler']['_step_count'] != steps+1):
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


class SharedRopeForgettingTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, device='cuda', seed=42, arm='learned_forget'):
        if arm not in ARMS:
            raise ValueError('Explicit forgetting attention arm required')
        if isinstance(sampler, PrefetchedOriginalSampler):
            raise ValueError('Original synchronous source required; no nested prefetch')
        sampler = PrefetchedOriginalSampler(sampler, batch)
        super().__init__(parent, sampler, binding, batch=batch, contrast=False, device=device, seed=seed)
        self.model = ForgettingModel.from_native(self.model, arm)
        count = sum(p.numel() for p in self.model.parameters())
        if (binding.get('weights_role') not in ('verification_only', 'scientific_forgetting_attention_shared_rope')
                or (binding['weights_role'] != 'verification_only' and (arm not in ARMS
                    or count != 10014516 or self.model.config[TAG]['native_expected_parameter_count'] != 10001152))):
            raise ValueError('Exact declared approximate10M science role/count/arm required')
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=1e-5, weight_decay=.1)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _:1.)
        self.spec.update(kind=KIND, shared_RoPE_policy=copy.deepcopy(ROPE_POLICY), loader_policy=copy.deepcopy(LOADER_POLICY), FP32_arithmetic_policy=copy.deepcopy(CANONICAL_POLICY), attention_implementation=IMPLEMENTATION, attention_backend='pinned_author_tiled_BF16_shared_RoPE_canonical64_FP32_cache_v1', actual_unique_parameters=count, forgetting_policy=copy.deepcopy(POLICY),
            forgetting_arm=arm, original_model_config=copy.deepcopy(parent['model_config']),
            CE_decoder_traversal='explicit_original_attention_cumulative_forget_bias',
            gradient_clip_policy='all_original_plus_forget_projection_coordinates')
        self.lineage.update(kind=KIND, shared_RoPE_policy=copy.deepcopy(ROPE_POLICY), loader_policy=copy.deepcopy(LOADER_POLICY), FP32_arithmetic_policy=copy.deepcopy(CANONICAL_POLICY), optimizer_policy=OPTIMIZER_POLICY, attention_implementation=IMPLEMENTATION)
        self.counters.update(forget_gate_projection_elements=0)
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress or not self.model.training:
            raise ValueError('Train mode and completed-update resume required')
        self._step_in_progress = True
        synchronize(self.device)
        started = time.monotonic()
        # Same original sampler, row order, right-padding and target placement.
        rows, CPU_ids, CPU_targets = self.sampler.take_staged(self.spec['batch'])
        data_wait = time.monotonic()-started
        ids, targets = CPU_ids.to(self.device), CPU_targets.to(self.device)
        pairs, families, bodies = [], set(), set()
        for row in rows:
            if (row['prefix_ids'] and row['suffix_ids'] and row['source_family'] not in families
                    and row['full_original_body_sha256'] not in bodies):
                pairs.append(row)
                families.add(row['source_family'])
                bodies.add(row['full_original_body_sha256'])
        self.optimizer.zero_grad(set_to_none=True)
        backend = SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                                enabled=self.device.type == 'cuda'):
            # Original inputs/targets are unchanged; pairwise log bias changes
            # attention routing before normalization in both matched arms.
            hidden = self.model.right_padded_hidden(ids)
            selected = targets != -100
            logits = self.model.lm_head(hidden[selected]).float()
            ce = F.cross_entropy(logits, targets[selected])
            if not torch.isfinite(ce):
                raise ValueError('Nonfinite original corpus CE')
            ce.backward()
        # Both matched arms include every coordinate in the same clip reduction.
        # Static gate coordinates have zero gradients; nonfinite updates fail.
        gradient = self.model.clip_grad_norm(1., error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        supervised = sum(r['teacher_tokens'] for r in rows)
        self.counters['update'] += 1
        for key, value in dict(supervised_tokens=supervised,
            CE_input_tokens=sum(len(r['input_ids']) for r in rows), auxiliary_input_tokens=0,
            auxiliary_pairs=0, physical_input_tokens=ids.numel(),
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
        c = self.model.config
        value_elements = ids.numel()*c['num_hidden_layers']*c['num_attention_heads']*(c['hidden_size']+1)
        self.counters['forget_gate_projection_elements'] += value_elements
        coefficients = torch.cat([p.detach().reshape(-1) for n,p in self.model.named_parameters()
                                  if '.forget_proj.' in n])
        synchronize(self.device)
        result = dict(**copy.deepcopy(self.counters), CE_loss=float(ce.detach()), contrast_loss=0.,
            combined_loss=float(ce.detach()), auxiliary_gradient_norm=0., gradient_norm=float(gradient),
            positive_cosine=0., distractor_cosine=0., representation_variance=0.,
            CE_targets_this_update=supervised, auxiliary_inputs_this_update=0,
            physical_inputs_this_update=ids.numel(), eligible_pairs_this_update=len(pairs),
            auxiliary_pairs_this_update=0, original_windows_this_update=len(rows),
            seconds=time.monotonic()-started, data_wait_seconds=data_wait,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'], r['index_record_sha256'], r['target_first'],
                         r['target_end'], r['teacher_tokens']) for r in rows],
            forget_gate_projection_elements_this_update=value_elements,
            forget_projection_abs_max=float(coefficients.abs().max()),
            forget_projection_mean=float(coefficients.mean()))
        self._step_in_progress = False
        return result

    def _raw_state(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save interrupted update; restore completed state')
        state = self._raw_state()
        if not committed_state(state):
            raise ValueError('Complete finite tagged model/Adam/clock/source state required')
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if (not committed_state(state) or any(state[k] != self._raw_state()[k]
                for k in ('spec', 'binding', 'lineage', 'model_config'))):
            raise ValueError('Matching complete forgetting attention state required before mutation')
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
