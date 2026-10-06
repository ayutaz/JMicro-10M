"""Same-material source quotas and explicit inherited-Adam constant-LR fork."""
import copy
import hashlib
import math
import os
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np
import torch
from jmicro.experiment import sha256
from jmicro.training import Trainer, atomic_json, implementation_hashes, rng_state, restore_rng

GENRES = ('web', 'story', 'textbook')


class GenreStream:
    """Whole documents shuffled within one genre, without copying train bytes."""
    def __init__(self, view, genre, seed):
        self.view, self.genre, self.seed = view, genre, seed
        if not hasattr(view, 'genre_documents'):
            view.genre_documents = {g: np.flatnonzero(view.index.sources == tag)
                                    for tag, g in enumerate(GENRES)}
            view.genre_orders = {}
        self.documents = view.genre_documents[genre]
        if not len(self.documents):
            raise ValueError('Empty train genre')
        self.epoch = self.document_position = self.token_offset = 0
        self._order()

    def _order(self):
        key = (self.genre, self.seed, self.epoch)
        if key not in self.view.genre_orders:
            order = np.random.default_rng(np.random.SeedSequence(
                [self.seed, self.epoch, GENRES.index(self.genre), 100])).permutation(len(self.documents))
            order.flags.writeable = False
            self.view.genre_orders[key] = order
        self.order = self.view.genre_orders[key]

    def normalize(self):
        if self.document_position == len(self.documents):
            self.epoch += 1; self.document_position = 0; self._order()
        doc = int(self.documents[self.order[self.document_position]])
        if self.token_offset == int(self.view.index.lengths[doc]) + 2:
            self.document_position += 1; self.token_offset = 0
            return self.normalize()
        return doc

    def read(self, count):
        out = np.empty(count, dtype=np.int64); copied = 0
        while copied < count:
            doc = self.normalize()
            length = int(self.view.index.lengths[doc]) + 2
            size = min(count - copied, length - self.token_offset)
            offset = int(self.view.index.offsets[doc]) + self.token_offset
            out[copied:copied + size] = self.view.tokens[offset:offset + size]
            copied += size; self.token_offset += size
        return out

    def block(self, context):
        x = self.read(context)
        doc = self.normalize()
        offset = int(self.view.index.offsets[doc]) + self.token_offset
        # Peek the next target without consuming it as an input a second time.
        y = np.concatenate((x[1:], np.array([int(self.view.tokens[offset])], dtype=np.int64)))
        y[y == 2] = -100
        return x, y

    def state_dict(self):
        return dict(seed=self.seed, genre=self.genre, documents=len(self.documents),
            epoch=self.epoch, document_position=self.document_position, token_offset=self.token_offset)

    def load_state_dict(self, state):
        if any(state[k] != self.state_dict()[k] for k in ('seed', 'genre', 'documents')):
            raise ValueError('Genre stream identity differs')
        if (type(state['epoch']) is not int or state['epoch'] < 0
                or not 0 <= state['document_position'] < len(self.documents)
                or type(state['token_offset']) is not int or state['token_offset'] < 0):
            raise ValueError('Invalid genre stream cursor')
        self.epoch, self.document_position, self.token_offset = (state[k] for k in ('epoch', 'document_position', 'token_offset'))
        self._order()
        doc = int(self.documents[self.order[self.document_position]])
        if self.token_offset >= int(self.view.index.lengths[doc]) + 2:
            raise ValueError('Noncanonical genre stream cursor')


class GenreQuotaSampler:
    def __init__(self, view, goals, context=1024, seed=42):
        if set(goals) != set(GENRES) or any(type(n) is not int or n <= 0 for n in goals.values()):
            raise ValueError('Three positive exact teacher quotas required')
        self.view, self.goals, self.context, self.seed = view, dict(goals), context, seed
        self.streams = {g: GenreStream(view, g, seed) for g in GENRES}
        self.source_teachers = dict.fromkeys(GENRES, 0)
        self.source_eos = dict.fromkeys(GENRES, 0)
        self.source_tokens = dict.fromkeys(GENRES, 0)
        self.source_body_bytes = dict.fromkeys(GENRES, 0)
        self.position = 0

    def batch(self, size):
        if self.source_teachers == self.goals:
            raise ValueError('Teacher quotas exhausted')
        xs, ys = [], []
        for _ in range(size):
            active = [g for g in GENRES if self.source_teachers[g] < self.goals[g]]
            genre = min(active, key=lambda g: self.source_teachers[g] / self.goals[g]) if active else 'web'
            x, y = self.streams[genre].block(self.context)
            remaining = self.goals[genre] - self.source_teachers[genre]
            labeled = np.flatnonzero(y != -100)
            y[labeled[remaining:]] = -100
            teachers = int(np.count_nonzero(y != -100))
            body_bytes = int(self.view.byte_lengths[y[y >= 8]].sum())
            self.source_teachers[genre] += teachers
            self.source_eos[genre] += int(np.count_nonzero(y == 3))
            self.source_tokens[genre] += self.context
            self.source_body_bytes[genre] += body_bytes
            xs.append(x); ys.append(y)
        self.position += 1
        return (torch.from_numpy(np.stack(xs)), torch.from_numpy(np.stack(ys)),
                sum(int(self.view.byte_lengths[y[y >= 8]].sum()) for y in ys))

    def state_dict(self):
        return dict(kind='same-material-genre-teacher-quota-v1', goals=self.goals.copy(), context=self.context,
            seed=self.seed, position=self.position, streams={g: s.state_dict() for g, s in self.streams.items()},
            source_teachers=self.source_teachers.copy(), source_eos=self.source_eos.copy(),
            source_tokens=self.source_tokens.copy(), source_body_bytes=self.source_body_bytes.copy(),
            body_bytes_accounting='supervised body bytes only; EOS/BOS/masked labels excluded',
            input_accounting='all unpadded physical inputs including terminal masked rows')

    def load_state_dict(self, state):
        current = self.state_dict()
        if any(state[k] != current[k] for k in ('kind', 'goals', 'context', 'seed', 'body_bytes_accounting', 'input_accounting')):
            raise ValueError('Source quota recipe differs')
        if type(state['position']) is not int or state['position'] < 0:
            raise ValueError('Invalid update cursor')
        for key in ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes'):
            if set(state[key]) != set(GENRES) or any(type(n) is not int or n < 0 for n in state[key].values()):
                raise ValueError('Invalid source accounting')
            setattr(self, key, state[key].copy())
        if any(self.source_teachers[g] > self.goals[g] or self.source_eos[g] > self.source_teachers[g] for g in GENRES):
            raise ValueError('Source quotas exceeded')
        for g, stream in self.streams.items():
            stream.load_state_dict(state['streams'][g])
        self.position = state['position']


class StoryWeightTrainer(Trainer):
    def __init__(self, parent, view, goals, binding, device='cuda', context=1024, batch=32):
        if parent['implementation_sha256'] != implementation_hashes():
            raise ValueError('Parent core implementation differs')
        lrs = [g['lr'] for g in parent['optimizer']['param_groups']]
        if any(not math.isclose(lr, .0002, rel_tol=1e-10) for lr in lrs):
            raise ValueError('Inherited terminal LR must be0.0002')
        spec = dict(seed=42, context=context, batch=batch, accumulation=1, lr=.0002,
            weight_decay=parent['spec']['weight_decay'], warmup=0,
            schedule_updates=parent['update'] + math.ceil(2 * sum(goals.values()) / (context * batch)) + 32,
            scheduler='wsd', dtype='bf16' if device == 'cuda' else 'fp32',
            backend='flash' if device == 'cuda' else 'math', compile=device == 'cuda',
            compile_mode='reduce-overhead', training_fast_path=True, deterministic=True,
            teacher_goals=dict(goals), research_kind='same_material_story_teacher_weight')
        stub = SimpleNamespace(tokens=view.tokens[:context + 1], split='train', manifest=view.manifest,
                               byte_lengths=view.byte_lengths, directory=view.directory)
        super().__init__(parent['model_config'], stub, spec, device)
        self.shard = view
        self.model.load_state_dict(parent['model'], strict=True)
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        # Adam/groups are inherited; only the declared future schedule changes.
        self.scheduler.base_lrs = [.0002] * len(lrs)
        self.scheduler.last_epoch = parent['scheduler']['last_epoch']
        self.scheduler._step_count = parent['scheduler']['_step_count']
        self.scheduler._last_lr = lrs.copy()
        self.sampler = GenreQuotaSampler(view, goals, context, 42)
        for key in ('update', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest'):
            setattr(self, key, parent[key])
        self.binding = copy.deepcopy(binding)
        self.pilot_binding = dict(parent.get('pilot_binding', {}), **binding)
        self.lineage = dict(kind='explicit-story-weight-constant-LR-fork', parent=binding['parent'],
            parent_update=parent['update'], parent_tokens=parent['tokens'],
            parent_supervised_tokens=parent['supervised_tokens'], parent_body_bytes=parent['body_bytes'],
            parent_token_digest=parent['token_digest'], actual_parent_sampler=copy.deepcopy(parent['sampler']),
            parent_scheduler=copy.deepcopy(parent['scheduler']), optimizer_policy='inherit', no_reheat=True,
            source_sampler_policy='new per-genre shuffle; old mixed cursor retained as parent lineage')
        restore_rng(parent['rng'])

    def step(self):
        row = super().step()
        row.update(source_teachers=self.sampler.source_teachers.copy(), source_eos=self.sampler.source_eos.copy(),
            source_input_tokens=self.sampler.source_tokens.copy(), source_body_bytes=self.sampler.source_body_bytes.copy(),
            valid_input_tokens=self.tokens - self.lineage['parent_tokens'],
            physical_input_tokens=self.tokens - self.lineage['parent_tokens'],
            additional_teacher_tokens=self.supervised_tokens - self.lineage['parent_supervised_tokens'])
        if (row['additional_teacher_tokens'] != sum(self.sampler.source_teachers.values())
                or self.update - self.lineage['parent_update'] != self.sampler.position
                or row['valid_input_tokens'] != sum(self.sampler.source_tokens.values())
                or self.body_bytes - self.lineage['parent_body_bytes'] != sum(self.sampler.source_body_bytes.values())):
            raise ValueError('Fork input/teacher/body-byte/update accounting differs')
        return row

    def save(self, path):
        started = time.perf_counter(); path.parent.mkdir(parents=True, exist_ok=True)
        state = dict(version=2, spec=self.spec, model_config=self.model.config, model=self.model.state_dict(),
            optimizer=self.optimizer.state_dict(), scheduler=self.scheduler.state_dict(), rng=rng_state(),
            sampler=self.sampler.state_dict(), update=self.update, tokens=self.tokens,
            supervised_tokens=self.supervised_tokens, body_bytes=self.body_bytes, token_digest=self.token_digest,
            shard_manifest_sha256=sha256(self.shard.directory / 'manifest.json'),
            implementation_sha256=implementation_hashes(), study_implementation_sha256=sha256(Path(__file__)),
            study_binding=self.binding, pilot_binding=self.pilot_binding, lineage=self.lineage,
            branch_updates=self.update - self.lineage['parent_update'], branch_tokens=self.tokens - self.lineage['parent_tokens'])
        temporary = path.with_suffix('.tmp')
        with temporary.open('wb') as stream:
            torch.save(state, stream); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
        atomic_json(path.parent / 'latest.json', dict(path=str(path.resolve()), sha256=sha256(path), update=self.update, tokens_seen=self.tokens))
        return time.perf_counter() - started

    def load(self, path):
        state = torch.load(path, map_location='cpu', weights_only=False)
        if (state.get('study_binding') != self.binding or state['spec'] != self.spec
                or state['implementation_sha256'] != implementation_hashes()
                or state['study_implementation_sha256'] != sha256(Path(__file__))
                or state['model_config'] != self.model.config
                or state['shard_manifest_sha256'] != sha256(self.shard.directory / 'manifest.json')):
            raise ValueError('Frozen fork resume identity/source/recipe differs')
        self.model.load_state_dict(state['model']); self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler']); self.sampler.load_state_dict(state['sampler'])
        self.lineage = state['lineage']; self.pilot_binding = state['pilot_binding']
        for key in ('update', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest'):
            setattr(self, key, state[key])
        if (self.update - self.lineage['parent_update'] != self.sampler.position
                or self.supervised_tokens - self.lineage['parent_supervised_tokens'] != sum(self.sampler.source_teachers.values())
                or self.tokens - self.lineage['parent_tokens'] != sum(self.sampler.source_tokens.values())
                or self.body_bytes - self.lineage['parent_body_bytes'] != sum(self.sampler.source_body_bytes.values())):
            raise ValueError('Resumed fork accounting differs')
        restore_rng(state['rng'])
