"""Typed original CE trainer for the explicit causal-QKV lag architecture proposal.

Separate explicit causal-QKV traversal; original source, targets and CE are retained.
Static-identity is a technical control. Original input/teacher clocks stay separate
from the declared extra projected-lag-element operations, which are not new teachers.
"""
import copy
import hashlib
import json
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.causal_qkv import native_config, TAG, POLICY, ARMS
from jmicro.causal_qkv_contiguous import ContiguousCausalQKVModel as CausalQKVModel, IMPLEMENTATION
from causal_qkv_trainer import committed_state as reference_committed_state
from jmicro.evaluation_boundary import require_digest
from jmicro.training import restore_rng
from base_fim_trainer import finite, valid_rng
from context_likelihood_trainer import validate_material
from natural_context_contrast_corpus import NaturalCorpusTrainer, GENRES
from natural_context_contrast_trainer import host, right_pad, synchronize

KIND = 'native_original_CE_causal_QKV_contiguous_v1'
OPTIMIZER_POLICY = 'fresh_AdamW_original_coordinates_plus_causal_QKV_lags'


def migrate_reference_verification(state):
    """Explicit metadata-only conversion for technical A/B, never science."""
    if (not reference_committed_state(state)
            or state['binding'].get('weights_role') != 'verification_only'
            or state['lineage'].get('weights_role') != 'verification_only'
            or 'runtime_implementation' in state['spec'] or 'runtime_implementation' in state['lineage']):
        raise ValueError('Only an actual complete reference VERIFICATION state may be compared')
    result=copy.deepcopy(state)
    for key in ('spec','lineage'):
        result[key]['kind']=KIND
        result[key]['runtime_implementation']=IMPLEMENTATION
    result['kind']=KIND
    if not committed_state(result):
        raise ValueError('Numerical state/config/clocks cannot change during runtime rebinding')
    return result


def committed_state(state):
    try:
        spec, c, source, opt = (state[k] for k in ('spec', 'counters', 'sampler', 'optimizer'))
        original = native_config(state['model_config'])
        steps, teachers = c['update'], c['supervised_tokens']
        if (state['kind'] != KIND or spec['kind'] != KIND or state['lineage']['kind'] != KIND
                or spec.get('runtime_implementation') != IMPLEMENTATION
                or state['lineage'].get('runtime_implementation') != IMPLEMENTATION
                or spec['lag_policy'] != POLICY or spec['lag_arm'] not in ARMS
                or spec['lag_arm'] != state['model_config'][TAG]['arm']
                or spec['original_model_config'] != original or spec['contrast'] is not False
                or spec['CE_decoder_traversal'] != 'explicit_original_QKV_previous_valid_lags'
                or spec['gradient_clip_policy'] != ('all_original_plus_QKV_lag_coordinates'
                    if spec['lag_arm'] == 'lag_learned' else 'exact_original_coordinate_reduction')
                or state['lineage']['optimizer_policy'] != OPTIMIZER_POLICY
                or spec['seed'] != source['seed'] or spec['goals'] != source['goals']
                or any(type(c[k]) is not int or c[k] < 0 for k in ('update', 'supervised_tokens',
                    'CE_input_tokens', 'physical_input_tokens', 'original_body_bytes',
                    'causal_QKV_lag_elements'))
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != source['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or c['auxiliary_pairs'] != 0 or c['auxiliary_input_tokens'] != 0
                or c['auxiliary_digest'] != '0'*64
                or c['causal_QKV_lag_elements'] != c['physical_input_tokens']*original['num_hidden_layers']*(original['num_attention_heads']+2*original['num_key_value_heads'])*original['head_dim']*2
                or set(c['source_EOS']) != set(GENRES)
                or any(type(c['source_EOS'][g]) is not int
                    or not 0 <= c['source_EOS'][g] <= c['source_teachers'][g] for g in GENRES)
                or (not steps <= source['windows_emitted'] <= steps*spec['batch']
                    if steps else source['windows_emitted'] != 0)):
            return False
        validate_material(source)
        require_digest(c['token_digest'])
        with torch.device('meta'):
            model = CausalQKVModel(state['model_config'])
        expected = model.state_dict()
        if (set(expected) != set(state['model'])
                or any(state['model'][k].shape != v.shape or state['model'][k].dtype != v.dtype for k,v in expected.items())
                or sum(p.numel() for p in model.parameters()) != spec['actual_unique_parameters']
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])
                or (spec['lag_arm'] == 'static_identity' and any(torch.count_nonzero(v)
                    for k,v in state['model'].items() if k.endswith(('.q_lag','.k_lag','.v_lag'))))):
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


class ContiguousCausalQKVTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, device='cuda', seed=42, arm='lag_learned'):
        if arm not in ARMS:
            raise ValueError('Explicit causal-QKV lag arm required')
        super().__init__(parent, sampler, binding, batch=batch, contrast=False, device=device, seed=seed)
        self.model = CausalQKVModel.from_native(self.model, arm)
        count = sum(p.numel() for p in self.model.parameters())
        if (binding.get('weights_role') not in ('verification_only', 'scientific_causal_QKV_contiguous')
                or (binding['weights_role'] != 'verification_only' and (arm != 'lag_learned'
                    or count != 10014464 or self.model.config[TAG]['native_expected_parameter_count'] != 10001152))):
            raise ValueError('Exact declared approximate10M science role/count/arm required')
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=1e-5, weight_decay=.1)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _:1.)
        self.spec.update(kind=KIND, runtime_implementation=IMPLEMENTATION, actual_unique_parameters=count, lag_policy=copy.deepcopy(POLICY),
            lag_arm=arm, original_model_config=copy.deepcopy(parent['model_config']),
            CE_decoder_traversal='explicit_original_QKV_previous_valid_lags',
            gradient_clip_policy=('all_original_plus_QKV_lag_coordinates' if arm == 'lag_learned'
                                  else 'exact_original_coordinate_reduction'))
        self.lineage.update(kind=KIND, runtime_implementation=IMPLEMENTATION, optimizer_policy=OPTIMIZER_POLICY)
        self.counters.update(causal_QKV_lag_elements=0)
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress or not self.model.training:
            raise ValueError('Train mode and completed-update resume required')
        self._step_in_progress = True
        synchronize(self.device)
        started = time.monotonic()
        # Same original sampler, row order, right-padding and target placement.
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
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend), torch.autocast(self.device.type, dtype=torch.bfloat16,
                                                enabled=self.device.type == 'cuda'):
            # All original inputs/targets are unchanged; each projected channel
            # reads preceding valid-token features before original attention.
            hidden = self.model.right_padded_hidden(ids)
            selected = targets != -100
            logits = self.model.lm_head(hidden[selected]).float()
            ce = F.cross_entropy(logits, targets[selected])
            if not torch.isfinite(ce):
                raise ValueError('Nonfinite original corpus CE')
            ce.backward()
        # Learned arm includes every new scalar; technical identity preserves
        # the exact native norm reduction list. Both reject nonfinite gradients.
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
        value_elements = ids.numel()*c['num_hidden_layers']*(c['num_attention_heads']+2*c['num_key_value_heads'])*c['head_dim']*2
        self.counters['causal_QKV_lag_elements'] += value_elements
        coefficients = torch.cat([getattr(layer.self_attn,name).detach().reshape(-1)
            for layer in self.model.model.layers for name in ('q_lag','k_lag','v_lag')])
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
            causal_QKV_lag_elements_this_update=value_elements,
            lag_coefficient_abs_max=float(coefficients.abs().max()),
            lag_coefficient_mean=float(coefficients.mean()))
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
        self._load_state(torch.load(Path(path), map_location=self.device, weights_only=False))

    def load_reference_for_verification(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        self._load_state(migrate_reference_verification(state))

    def _load_state(self, state):
        if (not committed_state(state) or any(state[k] != self._raw_state()[k]
                for k in ('spec', 'binding', 'lineage', 'model_config'))):
            raise ValueError('Matching complete causal-QKV lag state required before mutation')
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
