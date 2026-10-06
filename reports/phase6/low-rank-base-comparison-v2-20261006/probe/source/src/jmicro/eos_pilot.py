"""Explicit, resumable EOS-mixture pilot forks; production trainer is unchanged."""
import hashlib
import math
import os
from pathlib import Path
import time

import numpy as np
import torch

from jmicro.experiment import ROOT, read_json, sha256
from jmicro.shards import BlockSampler
from jmicro.training import Trainer, atomic_json, implementation_hashes, restore_rng, rng_state


def spans(chunk, offset, previous_end):
    """Complete documents ending in this chunk, including a boundary crossing."""
    ends = np.flatnonzero(chunk == 3).astype(np.int64) + offset
    if not len(ends):
        return np.empty(0, dtype=np.int64), ends, previous_end
    starts = np.concatenate(([previous_end + 1], ends[:-1] + 1))
    return starts, ends, int(ends[-1])


class TrainView:
    """Train-only mmap of an accepted manifest, without loading the large index.

    Original corpus integrity is supplied by the recorded builder/loader policy;
    this does not claim to repeat its full independent audit.
    """
    def __init__(self, directory, expected_manifest, check_stream=False):
        self.directory, self.split = Path(directory), 'train'
        if sha256(self.directory / 'manifest.json') != expected_manifest:
            raise ValueError('Train manifest binding differs')
        self.manifest = read_json(self.directory / 'manifest.json')
        detail = self.manifest['splits']['train']
        stream = self.directory / 'train.bin'
        if stream.stat().st_size != detail['tokens'] * 2:
            raise ValueError('Train stream size differs')
        if check_stream and sha256(stream) != detail['stream_sha256']:
            raise ValueError('New short stream checksum differs')
        if sha256(self.directory / 'token_bytes.json') != self.manifest['token_bytes_sha256']:
            raise ValueError('Token byte table differs')
        self.tokens = np.memmap(stream, dtype='<u2', mode='r')
        self.byte_lengths = np.asarray(read_json(self.directory / 'token_bytes.json'))


class MixtureSampler:
    def __init__(self, web, short, context, seed, routes, parent_web_state):
        self.web = BlockSampler(web, context, seed)
        self.web.load_state_dict(parent_web_state)
        self.short = BlockSampler(short, context, seed)
        self.routes = tuple(bool(r) for r in routes)
        self.position = 0
        self.source_tokens = {'web': 0, 'short': 0}
        self.source_eos = {'web': 0, 'short': 0}

    def state_dict(self):
        return {'kind': 'eos-pilot-mixture-v1', 'routes': self.routes,
                'position': self.position, 'web': self.web.state_dict(),
                'short': self.short.state_dict(), 'source_tokens': dict(self.source_tokens),
                'source_eos': dict(self.source_eos)}

    def load_state_dict(self, state):
        if state['kind'] != 'eos-pilot-mixture-v1' or tuple(state['routes']) != self.routes:
            raise ValueError('Mixture route configuration differs')
        if not 0 <= state['position'] <= len(self.routes):
            raise ValueError('Invalid mixture cursor')
        self.web.load_state_dict(state['web'])
        self.short.load_state_dict(state['short'])
        self.position = state['position']
        self.source_tokens = dict(state['source_tokens'])
        self.source_eos = dict(state['source_eos'])

    def batch(self, size):
        if self.position >= len(self.routes):
            raise ValueError('Pilot mixture budget exhausted')
        source = 'short' if self.routes[self.position] else 'web'
        x, y, byte_count = getattr(self, source).batch(size)
        self.source_tokens[source] += x.numel()
        self.source_eos[source] += int(y.eq(3).sum())
        self.position += 1
        return x, y, byte_count


def pilot_lr(spec, step):
    schedule = spec['pilot_schedule']
    progress = min(1., max(0., (step - schedule['parent_update'] - schedule['stable_updates']) / schedule['decay_updates']))
    return .1 + .9 * (1 + math.cos(math.pi * progress)) / 2


class PilotTrainer(Trainer):
    def __init__(self, parent, web, short, routes, schedule, binding, device='cuda'):
        if parent['implementation_sha256'] != implementation_hashes():
            raise ValueError('Parent implementation differs')
        if parent['shard_manifest_sha256'] != sha256(web.directory / 'manifest.json'):
            raise ValueError('Parent web data differs')
        spec = dict(parent['spec'])
        spec.update(scheduler='wsd', schedule_updates=parent['update'] + len(routes), pilot_schedule=schedule)
        for key in ('branch_at', 'decay_updates', 'minimum_lr_ratio'):
            spec.pop(key, None)
        super().__init__(parent['model_config'], web, spec, device)
        self.model.load_state_dict(parent['model'], strict=True)
        self.optimizer.load_state_dict(parent['optimizer'])
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda step: pilot_lr(self.spec, step))
        self.scheduler.last_epoch = parent['update']
        self.scheduler._step_count = parent['scheduler']['_step_count']
        self.scheduler.base_lrs = list(parent['scheduler']['base_lrs'])
        values = [base * pilot_lr(self.spec, parent['update']) for base in self.scheduler.base_lrs]
        for group, value in zip(self.optimizer.param_groups, values):
            group['lr'] = value
        self.scheduler._last_lr = values
        self.sampler = MixtureSampler(web, short, spec['context'], spec['seed'], routes, parent['sampler'])
        for key in ('update', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest'):
            setattr(self, key, parent[key])
        self.pilot_binding = binding
        self.lineage = {'kind': 'eos-short-pilot', 'parent_update': parent['update'],
                        'parent_tokens': parent['tokens'], 'parent_spec': parent['spec'],
                        'parent_token_digest': parent['token_digest'], 'parent_checkpoint': binding['parent']}
        restore_rng(parent['rng'])

    def save(self, path):
        started = time.monotonic()
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        state = {'version': 2, 'spec': self.spec, 'model_config': self.model.config,
                 'model': self.model.state_dict(), 'optimizer': self.optimizer.state_dict(),
                 'scheduler': self.scheduler.state_dict(), 'rng': rng_state(),
                 'sampler': self.sampler.state_dict(), 'update': self.update, 'tokens': self.tokens,
                 'supervised_tokens': self.supervised_tokens, 'body_bytes': self.body_bytes,
                 'token_digest': self.token_digest, 'lineage': self.lineage,
                 'pilot_binding': self.pilot_binding,
                 'shard_manifest_sha256': sha256(self.shard.directory / 'manifest.json'),
                 'implementation_sha256': implementation_hashes(),
                 'pilot_implementation_sha256': sha256(ROOT / 'src/jmicro/eos_pilot.py')}
        temporary = path.with_suffix('.tmp')
        with temporary.open('wb') as stream:
            torch.save(state, stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        atomic_json(path.parent / 'latest.json', {'path': str(path), 'sha256': sha256(path),
                    'update': self.update, 'tokens_seen': self.tokens})
        return time.monotonic() - started

    def load(self, path):
        state = torch.load(path, map_location='cpu', weights_only=False)
        if (state['spec'] != self.spec or state['pilot_binding'] != self.pilot_binding or
                state['pilot_implementation_sha256'] != sha256(ROOT / 'src/jmicro/eos_pilot.py') or
                state['implementation_sha256'] != implementation_hashes() or
                state['shard_manifest_sha256'] != sha256(self.shard.directory / 'manifest.json') or
                state['model_config'] != self.model.config):
            raise ValueError('Pilot resume source/config/data binding differs')
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.lineage = state['lineage']
        for key in ('update', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest'):
            setattr(self, key, state[key])
        if self.update - self.lineage['parent_update'] != self.sampler.position:
            raise ValueError('Pilot update/sampler cursor differs')
        if sum(self.sampler.source_tokens.values()) != self.tokens - self.lineage['parent_tokens']:
            raise ValueError('Pilot source-token accounting differs')
        restore_rng(state['rng'])
