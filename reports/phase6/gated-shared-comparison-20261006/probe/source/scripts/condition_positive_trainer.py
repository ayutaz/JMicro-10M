"""Matched four-stream training; only source-positive outcome loss weights vary."""
import copy
import hashlib
import math
import os
from pathlib import Path
import time

import numpy as np
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import read_json, sha256
from jmicro.training import atomic_json, autocast, implementation_hashes, restore_rng, rng_state, synchronize
from story_weight_trainer import GenreStream, StoryWeightTrainer
from condition_positive_loss import positive_weighted_ce

SOURCES = ('web', 'story', 'ordinary_textbook', 'conditional_textbook')


class PositiveTrainView:
    def __init__(self, path, manifest_sha256):
        self.directory = Path(path)
        if sha256(self.directory / 'manifest.json') != manifest_sha256:
            raise ValueError('Positive train manifest differs')
        self.manifest = read_json(self.directory / 'manifest.json')
        if (self.manifest['kind'] != 'original_train_positive_condition_outcome_spans'
                or self.manifest['newly_prepared_original_tokens'] != 0
                or sha256(self.directory / 'train.npz') != self.manifest['arrays_sha256']):
            raise ValueError('Positive train arrays differ')
        with np.load(self.directory / 'train.npz', allow_pickle=False) as arrays:
            self.tokens = arrays['tokens'].copy()
            self.focus = arrays['focus'].astype(bool)
            self.offsets = arrays['offsets'].copy()
            self.lengths = arrays['lengths'].copy()
        if (len(self.offsets) != self.manifest['documents']
                or self.focus.shape != self.tokens.shape
                or len(self.tokens) != self.manifest['serialized_tokens']
                or not np.array_equal(self.offsets, np.r_[0, np.cumsum(self.lengths)[:-1]])
                or int(self.lengths.sum()) != len(self.tokens)
                or np.any(self.focus & (self.tokens < 8))
                or np.count_nonzero(self.tokens == 3) != len(self.lengths)
                or np.count_nonzero(self.tokens == 2) != len(self.lengths)
                or not np.all(self.tokens[self.offsets] == 2)
                or not np.all(self.tokens[self.offsets + self.lengths - 1] == 3)
                or int(self.focus.sum()) != self.manifest['outcome_focus_body_targets']):
            raise ValueError('Whole original positive documents or masks differ')
        self.manifest_sha256 = manifest_sha256


class PositiveStream:
    def __init__(self, view, seed=42):
        self.view, self.seed = view, seed
        self.epoch = self.document_position = self.token_offset = 0
        self._order()

    def _order(self):
        self.order = np.random.default_rng(np.random.SeedSequence([self.seed, self.epoch, 3, 100])).permutation(len(self.view.lengths))

    def normalize(self):
        while True:
            if self.document_position == len(self.order):
                self.epoch += 1
                self.document_position = 0
                self._order()
            doc = int(self.order[self.document_position])
            if self.token_offset < int(self.view.lengths[doc]):
                return doc
            self.document_position += 1
            self.token_offset = 0

    def block(self, context):
        x = np.empty(context, dtype=np.int64)
        focus = np.empty(context, dtype=bool)
        copied = 0
        while copied < context:
            doc = self.normalize()
            count = min(context - copied, int(self.view.lengths[doc]) - self.token_offset)
            offset = int(self.view.offsets[doc]) + self.token_offset
            x[copied:copied + count] = self.view.tokens[offset:offset + count]
            focus[copied:copied + count] = self.view.focus[offset:offset + count]
            copied += count
            self.token_offset += count
        doc = self.normalize()
        offset = int(self.view.offsets[doc]) + self.token_offset
        y = np.r_[x[1:], int(self.view.tokens[offset])]
        target_focus = np.r_[focus[1:], bool(self.view.focus[offset])]
        y[y == 2] = -100
        target_focus &= y >= 8
        return x, y, target_focus

    def state_dict(self):
        return dict(seed=self.seed, manifest_sha256=self.view.manifest_sha256,
                    epoch=self.epoch, document_position=self.document_position, token_offset=self.token_offset)

    def load_state_dict(self, state):
        if (state['seed'] != self.seed or state['manifest_sha256'] != self.view.manifest_sha256
                or any(type(state[k]) is not int or state[k] < 0 for k in ('epoch', 'document_position', 'token_offset'))
                or state['document_position'] >= len(self.view.lengths)):
            raise ValueError('Positive stream identity/cursor differs')
        self.epoch, self.document_position, self.token_offset = (state[k] for k in ('epoch', 'document_position', 'token_offset'))
        self._order()
        if self.token_offset >= int(self.view.lengths[self.order[self.document_position]]):
            raise ValueError('Positive stream cursor noncanonical')


class ConditionQuotaSampler:
    def __init__(self, view, positive, goals, context=1024, seed=42):
        if set(goals) != set(SOURCES) or any(type(n) is not int or n <= 0 for n in goals.values()):
            raise ValueError('Four positive exact teacher quotas required')
        self.view, self.goals, self.context, self.seed = view, dict(goals), context, seed
        self.streams = {g: GenreStream(view, 'textbook' if g == 'ordinary_textbook' else g, seed)
                        for g in SOURCES if g != 'conditional_textbook'}
        self.streams['conditional_textbook'] = PositiveStream(positive, seed)
        self.position = 0
        for key in ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes', 'source_focus_teachers'):
            setattr(self, key, dict.fromkeys(SOURCES, 0))

    def batch(self, size):
        if self.source_teachers == self.goals:
            raise ValueError('Teacher quotas exhausted')
        xs, ys, masks = [], [], []
        body_bytes = 0
        for _ in range(size):
            active = [g for g in SOURCES if self.source_teachers[g] < self.goals[g]]
            genre = min(active, key=lambda g: self.source_teachers[g] / self.goals[g]) if active else 'web'
            if genre == 'conditional_textbook':
                x, y, focused = self.streams[genre].block(self.context)
            else:
                x, y = self.streams[genre].block(self.context)
                focused = np.zeros(self.context, dtype=bool)
            remaining = self.goals[genre] - self.source_teachers[genre]
            labeled = np.flatnonzero(y != -100)
            y[labeled[remaining:]] = -100
            focused &= y >= 8
            byte_count = int(self.view.byte_lengths[y[y >= 8]].sum())
            self.source_teachers[genre] += int(np.count_nonzero(y != -100))
            self.source_eos[genre] += int(np.count_nonzero(y == 3))
            self.source_tokens[genre] += self.context
            self.source_body_bytes[genre] += byte_count
            self.source_focus_teachers[genre] += int(focused.sum())
            body_bytes += byte_count
            xs.append(x)
            ys.append(y)
            masks.append(focused)
        self.position += 1
        return torch.from_numpy(np.stack(xs)), torch.from_numpy(np.stack(ys)), body_bytes, torch.from_numpy(np.stack(masks))

    def state_dict(self):
        return dict(kind='same-input-four-stream-positive-CE-v1', goals=self.goals.copy(), context=self.context,
                    seed=self.seed, position=self.position, streams={g: s.state_dict() for g, s in self.streams.items()},
                    **{k: getattr(self, k).copy() for k in ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes', 'source_focus_teachers')})

    def load_state_dict(self, state):
        current = self.state_dict()
        if (any(state[k] != current[k] for k in ('kind', 'goals', 'context', 'seed'))
                or type(state['position']) is not int or state['position'] < 0
                or set(state['streams']) != set(SOURCES)):
            raise ValueError('Four-stream recipe differs')
        for key in ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes', 'source_focus_teachers'):
            if set(state[key]) != set(SOURCES) or any(type(n) is not int or n < 0 for n in state[key].values()):
                raise ValueError('Invalid four-stream accounting')
            setattr(self, key, state[key].copy())
        if (any(self.source_teachers[g] > self.goals[g]
                or self.source_eos[g] + self.source_focus_teachers[g] > self.source_teachers[g] for g in SOURCES)
                or any(self.source_focus_teachers[g] for g in SOURCES if g != 'conditional_textbook')):
            raise ValueError('Invalid teacher/focus quotas')
        for g, stream in self.streams.items():
            stream.load_state_dict(state['streams'][g])
        self.position = state['position']


class ConditionPositiveTrainer(StoryWeightTrainer):
    def __init__(self, parent, view, positive, goals, factor, binding, device='cuda', context=1024, batch=32):
        if factor not in (1, 4):
            raise ValueError('Only frozen ordinary1 and positive4 arms allowed')
        combined = dict(web=goals['web'], story=goals['story'], textbook=goals['ordinary_textbook'] + goals['conditional_textbook'])
        super().__init__(parent, view, combined, binding, device, context, batch)
        self.spec.update(teacher_goals=dict(goals), research_kind='same_input_positive_outcome_CE', outcome_weight=factor,
                         positive_manifest_sha256=positive.manifest_sha256)
        self.factor = factor
        self.sampler = ConditionQuotaSampler(view, positive, goals, context, 42)
        self.focus_teacher_tokens = self.weighted_teacher_mass = 0
        self.focus_token_digest = '00' * 32
        self.lineage.update(kind='explicit-positive-CE-constant-LR-fork',
                            source_sampler_policy='new four-stream shuffle with same seed/order in both arms; old mixed cursor preserved')

    def step(self):
        synchronize(self.device)
        started = time.perf_counter()
        x, y, byte_count, focused = self.sampler.batch(self.spec['batch'])
        if x.eq(0).any():
            raise ValueError('Unpadded input required')
        digest = hashlib.sha256(bytes.fromhex(self.token_digest))
        digest.update(x.numpy().astype('<i8').tobytes())
        digest.update(y.numpy().astype('<i8').tobytes())
        focus_digest = hashlib.sha256(bytes.fromhex(self.focus_token_digest))
        focus_digest.update(focused.numpy().astype(np.uint8).tobytes())
        data_wait = time.perf_counter() - started
        self.optimizer.zero_grad(set_to_none=True)
        self.model.train()
        x, y, focused = x.to(self.device), y.to(self.device), focused.to(self.device)
        with sdpa_kernel(SDPBackend.FLASH_ATTENTION if self.spec['backend'] == 'flash' else SDPBackend.MATH), autocast(self.device, self.spec['dtype']):
            logits = self.forward(x, training_fast_path=True).logits
            loss, counts = positive_weighted_ce(logits, y, focused, self.factor)
        loss.backward()
        norm = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1., error_if_nonfinite=True)
        nll = float(loss.detach())
        if not math.isfinite(nll):
            raise ValueError('Nonfinite positive-CE loss')
        lr = self.optimizer.param_groups[0]['lr']
        self.optimizer.step()
        self.scheduler.step()
        self.update += 1
        self.tokens += x.numel()
        self.supervised_tokens += counts['ordinary_teacher_tokens']
        self.body_bytes += byte_count
        self.focus_teacher_tokens += counts['outcome_focus_teacher_tokens']
        self.weighted_teacher_mass += counts['weighted_teacher_mass']
        self.token_digest, self.focus_token_digest = digest.hexdigest(), focus_digest.hexdigest()
        self.audit_counters()
        synchronize(self.device)
        seconds = time.perf_counter() - started
        return dict(update=self.update, loss=nll, gradient_norm=float(norm), lr=lr, tokens_seen=self.tokens,
                    supervised_tokens=self.supervised_tokens, body_bytes_seen=self.body_bytes,
                    token_digest=self.token_digest, focus_token_digest=self.focus_token_digest,
                    focus_teacher_tokens=self.focus_teacher_tokens, weighted_teacher_mass=self.weighted_teacher_mass,
                    outcome_weight=self.factor, seconds=seconds, data_wait_seconds=data_wait,
                    tokens_per_second=x.numel() / seconds,
                    source_teachers=self.sampler.source_teachers.copy(), source_eos=self.sampler.source_eos.copy(),
                    source_input_tokens=self.sampler.source_tokens.copy(), source_body_bytes=self.sampler.source_body_bytes.copy(),
                    source_focus_teachers=self.sampler.source_focus_teachers.copy(),
                    valid_input_tokens=self.tokens - self.lineage['parent_tokens'],
                    physical_input_tokens=self.tokens - self.lineage['parent_tokens'],
                    additional_teacher_tokens=self.supervised_tokens - self.lineage['parent_supervised_tokens'])

    def audit_counters(self):
        teachers = self.supervised_tokens - self.lineage['parent_supervised_tokens']
        if (teachers != sum(self.sampler.source_teachers.values())
                or self.update - self.lineage['parent_update'] != self.sampler.position
                or self.tokens - self.lineage['parent_tokens'] != sum(self.sampler.source_tokens.values())
                or self.tokens - self.lineage['parent_tokens'] != self.sampler.position * self.spec['batch'] * self.spec['context']
                or self.body_bytes - self.lineage['parent_body_bytes'] != sum(self.sampler.source_body_bytes.values())
                or self.focus_teacher_tokens != sum(self.sampler.source_focus_teachers.values())
                or self.weighted_teacher_mass != teachers + (self.factor - 1) * self.focus_teacher_tokens):
            raise ValueError('Positive fork completed-update accounting differs')

    def save(self, path):
        self.audit_counters()
        started = time.perf_counter()
        path.parent.mkdir(parents=True, exist_ok=True)
        state = dict(version=2, spec=self.spec, model_config=self.model.config, model=self.model.state_dict(),
            optimizer=self.optimizer.state_dict(), scheduler=self.scheduler.state_dict(), rng=rng_state(),
            sampler=self.sampler.state_dict(), update=self.update, tokens=self.tokens,
            supervised_tokens=self.supervised_tokens, body_bytes=self.body_bytes, token_digest=self.token_digest,
            focus_token_digest=self.focus_token_digest, focus_teacher_tokens=self.focus_teacher_tokens,
            weighted_teacher_mass=self.weighted_teacher_mass,
            shard_manifest_sha256=sha256(self.shard.directory / 'manifest.json'),
            implementation_sha256=implementation_hashes(), study_implementation_sha256=sha256(Path(__file__)),
            loss_implementation_sha256=sha256(Path(__file__).with_name('condition_positive_loss.py')),
            study_binding=self.binding, pilot_binding=self.pilot_binding, lineage=self.lineage,
            branch_updates=self.update - self.lineage['parent_update'], branch_tokens=self.tokens - self.lineage['parent_tokens'])
        temporary = path.with_suffix('.tmp')
        with temporary.open('wb') as stream:
            torch.save(state, stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        atomic_json(path.parent / 'latest.json', dict(path=str(path.resolve()), sha256=sha256(path), update=self.update, tokens_seen=self.tokens))
        return time.perf_counter() - started

    def load(self, path):
        state = torch.load(path, map_location='cpu', weights_only=False)
        if (state.get('study_binding') != self.binding or state['spec'] != self.spec
                or state['implementation_sha256'] != implementation_hashes()
                or state['study_implementation_sha256'] != sha256(Path(__file__))
                or state['loss_implementation_sha256'] != sha256(Path(__file__).with_name('condition_positive_loss.py'))
                or state['model_config'] != self.model.config
                or state['shard_manifest_sha256'] != sha256(self.shard.directory / 'manifest.json')):
            raise ValueError('Positive fork identity/source/recipe differs')
        self.model.load_state_dict(state['model'])
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.lineage, self.pilot_binding = state['lineage'], state['pilot_binding']
        for key in ('update', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest',
                    'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass'):
            setattr(self, key, state[key])
        self.audit_counters()
        restore_rng(state['rng'])
