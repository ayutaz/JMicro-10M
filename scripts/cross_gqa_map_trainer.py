"""Typed original CE trainer for the explicit cross-GQA architecture proposal.

Reuse the frozen ordinary CE step unchanged; only the model class differs.
Static-zero is a technical control. Original input/teacher clocks stay separate
from the declared two-map/head compute count, which is not new data/teachers.
"""
import copy
from pathlib import Path
import time

import torch

from jmicro.cross_gqa_map import CrossGQAMapModel, native_config, TAG, POLICY, ARMS
from jmicro.evaluation_boundary import require_digest
from jmicro.training import restore_rng
from base_fim_trainer import finite, valid_rng
from context_likelihood_trainer import validate_material
from natural_context_contrast_corpus import NaturalCorpusTrainer, GENRES
from natural_context_contrast_trainer import host

KIND = 'native_original_CE_cross_GQA_signed_map_v1'
OPTIMIZER_POLICY = 'fresh_AdamW_original_coordinates_plus_cross_scalars'


def committed_state(state):
    try:
        spec, c, source, opt = (state[k] for k in ('spec', 'counters', 'sampler', 'optimizer'))
        original = native_config(state['model_config'])
        steps, teachers = c['update'], c['supervised_tokens']
        if (state['kind'] != KIND or spec['kind'] != KIND or state['lineage']['kind'] != KIND
                or spec['cross_policy'] != POLICY or spec['cross_arm'] not in ARMS
                or spec['cross_arm'] != state['model_config'][TAG]['arm']
                or spec['original_model_config'] != original or spec['contrast'] is not False
                or state['lineage']['optimizer_policy'] != OPTIMIZER_POLICY
                or spec['seed'] != source['seed'] or spec['goals'] != source['goals']
                or any(type(c[k]) is not int or c[k] < 0 for k in ('update', 'supervised_tokens',
                    'CE_input_tokens', 'physical_input_tokens', 'original_body_bytes',
                    'attention_map_query_head_positions'))
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != source['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or c['auxiliary_pairs'] != 0 or c['auxiliary_input_tokens'] != 0
                or c['auxiliary_digest'] != '0'*64
                or c['attention_map_query_head_positions'] != c['physical_input_tokens']*original['num_hidden_layers']*8
                or set(c['source_EOS']) != set(GENRES)
                or any(type(c['source_EOS'][g]) is not int
                    or not 0 <= c['source_EOS'][g] <= c['source_teachers'][g] for g in GENRES)
                or (not steps <= source['windows_emitted'] <= steps*spec['batch']
                    if steps else source['windows_emitted'] != 0)):
            return False
        validate_material(source)
        require_digest(c['token_digest'])
        with torch.device('meta'):
            model = CrossGQAMapModel(state['model_config'])
        expected = model.state_dict()
        if (set(expected) != set(state['model'])
                or any(state['model'][k].shape != v.shape or state['model'][k].dtype != v.dtype for k,v in expected.items())
                or sum(p.numel() for p in model.parameters()) != spec['actual_unique_parameters']
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])
                or (spec['cross_arm'] == 'static_zero' and any(torch.count_nonzero(v)
                    for k,v in state['model'].items() if k.endswith('.cross_raw')))):
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


class CrossGQAMapTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, device='cuda', seed=42, arm='cross_learned'):
        if arm not in ARMS:
            raise ValueError('Explicit cross-GQA arm required')
        super().__init__(parent, sampler, binding, batch=batch, contrast=False, device=device, seed=seed)
        self.model = CrossGQAMapModel.from_native(self.model, arm)
        count = sum(p.numel() for p in self.model.parameters())
        if (binding.get('weights_role') not in ('verification_only', 'scientific_cross_GQA_map')
                or (binding['weights_role'] != 'verification_only' and (arm != 'cross_learned'
                    or count != 10001204 or self.model.config[TAG]['native_expected_parameter_count'] != 10001152))):
            raise ValueError('Exact declared approximate10M science role/count/arm required')
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=1e-5, weight_decay=.1)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _:1.)
        self.spec.update(kind=KIND, actual_unique_parameters=count, cross_policy=copy.deepcopy(POLICY),
            cross_arm=arm, original_model_config=copy.deepcopy(parent['model_config']))
        self.lineage.update(kind=KIND, optimizer_policy=OPTIMIZER_POLICY)
        self.counters.update(attention_map_query_head_positions=0)
        self._step_in_progress = False

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
            raise ValueError('Matching complete cross-GQA state required before mutation')
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
            raise ValueError('Train mode and completed-update resume required')
        self._step_in_progress = True
        started = time.monotonic()
        # Frozen original source/quota/window/CE/backward/clip/update path.
        row = super().step()
        query_positions = row['physical_inputs_this_update']*self.model.config['num_hidden_layers']*8
        self.counters['attention_map_query_head_positions'] += query_positions
        coefficients = torch.cat([layer.self_attn.cross_raw.detach().tanh()
                                  for layer in self.model.model.layers])
        row.update(attention_map_query_head_positions=self.counters['attention_map_query_head_positions'],
            attention_map_query_head_positions_this_update=query_positions,
            cross_coefficient_abs_max=float(coefficients.abs().max()),
            cross_coefficient_mean=float(coefficients.mean()), seconds=time.monotonic()-started)
        self._step_in_progress = False
        return row
