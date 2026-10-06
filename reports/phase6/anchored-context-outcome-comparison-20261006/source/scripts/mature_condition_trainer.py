"""Inherited-Adam Base forks, including an exact Web-only control.

The historical four-positive-quota trainer stays frozen. This protocol admits
zero quotas and never initializes or advances their source streams.
"""
import copy
import math
from pathlib import Path
from types import SimpleNamespace

from jmicro.experiment import sha256
from jmicro.training import Trainer, implementation_hashes, restore_rng
from condition_positive_trainer import (
    SOURCES, ConditionPositiveTrainer, ConditionQuotaSampler, PositiveStream,
)
from story_weight_trainer import GenreStream


class MatureQuotaSampler(ConditionQuotaSampler):
    def __init__(self, view, positive, goals, context=1024, seed=42):
        if (set(goals) != set(SOURCES)
                or any(type(n) is not int or n < 0 for n in goals.values())
                or not sum(goals.values()) or type(context) is not int or context <= 0):
            raise ValueError('Nonnegative exact teacher quotas with a positive total required')
        self.view, self.goals, self.context, self.seed = view, dict(goals), context, seed
        self.streams = {}
        for source in SOURCES:
            if goals[source]:
                self.streams[source] = (PositiveStream(positive, seed) if source == 'conditional_textbook'
                    else GenreStream(view, 'textbook' if source == 'ordinary_textbook' else source, seed))
        self.position = 0
        for key in ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes', 'source_focus_teachers'):
            setattr(self, key, dict.fromkeys(SOURCES, 0))

    def batch(self, size):
        # The inherited packing algorithm pads a terminal batch using Web. All
        # declared arms have positive Web quotas; a generalized recipe is refused.
        if not self.goals['web']:
            raise ValueError('This protocol requires a positive Web quota')
        if type(size) is not int or size <= 0:
            raise ValueError('Positive batch size required')
        return super().batch(size)

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = 'mature-parent-zero-capable-source-quotas-v1'
        return state

    def load_state_dict(self, state):
        current = self.state_dict()
        if (any(state[k] != current[k] for k in ('kind', 'goals', 'context', 'seed'))
                or type(state['position']) is not int or state['position'] < 0
                or set(state['streams']) != set(self.streams)):
            raise ValueError('Mature source recipe/cursor differs')
        counters = ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes', 'source_focus_teachers')
        for key in counters:
            if (set(state[key]) != set(SOURCES)
                    or any(type(n) is not int or n < 0 for n in state[key].values())
                    or any(state[key][g] for g in SOURCES if not self.goals[g])):
                raise ValueError('Invalid mature or inactive-source accounting')
        if (any(state['source_teachers'][g] > self.goals[g]
                or state['source_eos'][g] + state['source_focus_teachers'][g] > state['source_teachers'][g]
                for g in SOURCES)
                or any(state['source_focus_teachers'][g] for g in SOURCES if g != 'conditional_textbook')):
            raise ValueError('Invalid mature teacher/focus quotas')
        for g, stream in self.streams.items():
            stream.load_state_dict(state['streams'][g])
        for key in counters:
            setattr(self, key, state[key].copy())
        self.position = state['position']


class MatureConditionTrainer(ConditionPositiveTrainer):
    def __init__(self, parent, view, positive, goals, binding, device='cuda', context=1024, batch=32):
        # Construct the real sampler first, with no phantom positive bootstrap.
        sampler = MatureQuotaSampler(view, positive, goals, context, 42)
        if not goals['web']:
            raise ValueError('This protocol requires a positive Web quota')
        if parent['implementation_sha256'] != implementation_hashes():
            raise ValueError('Parent core implementation differs')
        lrs = [g['lr'] for g in parent['optimizer']['param_groups']]
        if not lrs or any(not math.isclose(lr, .0002, rel_tol=1e-10) for lr in lrs):
            raise ValueError('Inherited terminal LR must be0.0002')
        spec = dict(seed=42, context=context, batch=batch, accumulation=1, lr=.0002,
            weight_decay=parent['spec']['weight_decay'], warmup=0,
            schedule_updates=parent['update'] + math.ceil(2 * sum(goals.values()) / (context * batch)) + 32,
            scheduler='wsd', dtype='bf16' if device == 'cuda' else 'fp32',
            backend='flash' if device == 'cuda' else 'math', compile=device == 'cuda',
            compile_mode='reduce-overhead', training_fast_path=True, deterministic=True,
            teacher_goals=dict(goals), research_kind='mature_Base_matched_condition_100M',
            outcome_weight=1, positive_manifest_sha256=positive.manifest_sha256 if goals['conditional_textbook'] else None,
            mature_trainer_sha256=sha256(Path(__file__)))
        stub = SimpleNamespace(tokens=view.tokens[:context + 1], split='train', manifest=view.manifest,
                               byte_lengths=view.byte_lengths, directory=view.directory)
        Trainer.__init__(self, parent['model_config'], stub, spec, device)
        self.shard = view
        self.model.load_state_dict(parent['model'], strict=True)
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        self.scheduler.base_lrs = [.0002] * len(lrs)
        self.scheduler.last_epoch = parent['scheduler']['last_epoch']
        self.scheduler._step_count = parent['scheduler']['_step_count']
        self.scheduler._last_lr = lrs.copy()
        self.sampler, self.factor = sampler, 1
        for key in ('update', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest'):
            setattr(self, key, parent[key])
        self.focus_teacher_tokens = self.weighted_teacher_mass = 0
        self.focus_token_digest = '00' * 32
        self.binding = copy.deepcopy(binding)
        self.pilot_binding = dict(parent.get('pilot_binding', {}), **binding)
        self.lineage = dict(kind='mature-Base-exact-source-constant-LR-fork', parent=binding['parent'],
            parent_update=parent['update'], parent_tokens=parent['tokens'],
            parent_supervised_tokens=parent['supervised_tokens'], parent_body_bytes=parent['body_bytes'],
            parent_token_digest=parent['token_digest'], actual_parent_sampler=copy.deepcopy(parent['sampler']),
            parent_scheduler=copy.deepcopy(parent['scheduler']), optimizer_policy='inherit', no_reheat=True,
            source_sampler_policy='fresh seed42 per-source fork; inactive sources absent; original parent cursor recorded')
        restore_rng(parent['rng'])
