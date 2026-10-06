"""Original native CE; official Muon on hidden matrices, AdamW on tied vocab/norms."""
import copy
from pathlib import Path
import torch
from natural_context_contrast_corpus import NaturalCorpusTrainer

KIND = 'native_original_CE_official_Muon_match_rms_AdamW_v1'


class HybridMuon:
    def __init__(self, model):
        vocabulary = model.model.embed_tokens.weight
        groups = {'muon': [], 'adamw': []}
        self.names = {'muon': [], 'adamw': []}
        seen = set()
        for name, parameter in model.named_parameters():
            if id(parameter) in seen: raise ValueError('Unique parameter partition required')
            seen.add(id(parameter))
            key = 'muon' if parameter.ndim == 2 and parameter is not vocabulary else 'adamw'
            groups[key].append(parameter)
            self.names[key].append(name)
        if not all(groups.values()) or vocabulary not in groups['adamw']:
            raise ValueError('Hidden matrices and tied vocabulary must have separate optimizers')
        self.muon = torch.optim.Muon(groups['muon'], lr=1e-5, weight_decay=.1,
            momentum=.95, nesterov=True, ns_steps=5, adjust_lr_fn='match_rms_adamw')
        self.adamw = torch.optim.AdamW(groups['adamw'], lr=1e-5, weight_decay=.1)
        self.param_groups = self.muon.param_groups + self.adamw.param_groups
        self.completed_steps = 0

    def zero_grad(self, set_to_none=True):
        self.muon.zero_grad(set_to_none=set_to_none)
        self.adamw.zero_grad(set_to_none=set_to_none)

    def step(self):
        self.muon.step()
        self.adamw.step()
        self.completed_steps += 1

    def state_dict(self):
        return dict(kind=KIND, names=copy.deepcopy(self.names), completed_steps=self.completed_steps,
                    muon=self.muon.state_dict(), adamw=self.adamw.state_dict())

    def load_state_dict(self, state):
        if state['kind'] != KIND or state['names'] != self.names or type(state['completed_steps']) is not int or state['completed_steps'] < 0:
            raise ValueError('Hybrid optimizer partition/recipe/committed steps differ')
        self.muon.load_state_dict(state['muon'])
        self.adamw.load_state_dict(state['adamw'])
        self.param_groups = self.muon.param_groups + self.adamw.param_groups
        self.completed_steps = state['completed_steps']


class ConstantSchedule:
    def __init__(self, optimizer): self.optimizer, self.position = optimizer, 0
    def step(self):
        if any(g['lr'] != 1e-5 for g in self.optimizer.param_groups):
            raise ValueError('Fixed same nominal constant LR required')
        self.position += 1
    def state_dict(self): return dict(kind='hybrid_constant_lr1e-5_v1', position=self.position, lr=1e-5)
    def load_state_dict(self, state):
        if state['kind'] != self.state_dict()['kind'] or state['lr'] != 1e-5 or type(state['position']) is not int or state['position'] < 0:
            raise ValueError('Hybrid scheduler recipe/cursor differs')
        if any(g['lr'] != 1e-5 for g in self.optimizer.param_groups): raise ValueError('Saved optimizer LR differs')
        self.position = state['position']


class MuonTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, contrast=False, device='cuda', seed=42):
        if contrast: raise ValueError('No auxiliary loss in optimizer-only comparison')
        super().__init__(parent, sampler, binding, batch, False, device, seed)
        self.optimizer = HybridMuon(self.model)
        self.scheduler = ConstantSchedule(self.optimizer)
        self.spec.update(kind=KIND, optimizer_policy='fresh_hidden_Muon_tied_vocabulary_and_norm_AdamW',
            momentum=.95, nesterov=True, ns_steps=5, adjust_lr_fn='match_rms_adamw',
            optimizer_partition=copy.deepcopy(self.optimizer.names))
        self.lineage.update(kind=KIND, optimizer_policy=self.spec['optimizer_policy'])

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        n = state['counters']['supervised_tokens']
        if (state['counters']['update'] != state['optimizer']['completed_steps'] or
                state['counters']['update'] != state['scheduler']['position'] or
                n != sum(state['counters']['source_teachers'].values()) or
                state['counters']['source_teachers'] != state['sampler']['consumed'] or
                state['counters']['auxiliary_input_tokens'] or state['counters']['auxiliary_pairs']):
            raise ValueError('Completed hybrid update/source/scheduler accounting differs')
        super().load(path)


def finite_muon_state(state):
    def finite(value):
        if isinstance(value, torch.Tensor): return bool(torch.isfinite(value).all())
        if isinstance(value, dict): return all(finite(v) for v in value.values())
        if isinstance(value, (list, tuple)): return all(finite(v) for v in value)
        return True
    return (state['kind'] == KIND and finite(state['model']) and finite(state['optimizer']) and
            state['optimizer']['completed_steps'] == state['counters']['update'] == state['scheduler']['position'])
