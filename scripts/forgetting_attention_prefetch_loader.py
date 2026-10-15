"""One speculative TRAIN batch; checkpoint state describes consumed rows only.

The producer owns the source sampler while running, uses no CUDA/global RNG,
and never changes original source/row/target order or physical padding. Pending
producer rows are discarded on load and deterministically reproduced from the
saved logical sampler state. This is loading work, not completed learning.
"""
import copy
from concurrent.futures import ThreadPoolExecutor

import torch


LOADER_POLICY = dict(kind='one_CPU_batch_prefetch_exact_logical_sampler_v1',
    depth=1, producer_device='cpu', ids_dtype='int64', targets_dtype='int64',
    PAD=0, ignore_index=-100, device_transfers_per_update=2,
    checkpoint_sampler='consumed_current_batch_only',
    queued_rows='discard_and_reproduce_from_logical_state_on_load',
    original_physical_geometry_unchanged=True)


def stage_original_rows(rows):
    if (not rows or any(not r['input_ids'] or len(r['target_ids']) != len(r['input_ids'])
                        for r in rows)):
        raise ValueError('Nonempty original aligned input/target rows required')
    width = max(len(r['input_ids']) for r in rows)
    ids = torch.zeros((len(rows), width), dtype=torch.long, device='cpu')
    targets = torch.full_like(ids, -100)
    for i, row in enumerate(rows):
        n = len(row['input_ids'])
        ids[i, :n] = torch.tensor(row['input_ids'], dtype=torch.long, device='cpu')
        targets[i, :n] = torch.tensor(row['target_ids'], dtype=torch.long, device='cpu')
    return ids, targets


class PrefetchedOriginalSampler:
    def __init__(self, source, batch):
        if type(batch) is not int or batch < 2:
            raise ValueError('Fixed original batch>=2 required')
        self.source, self.batch = source, batch
        self.binding, self.goals = copy.deepcopy(source.binding), copy.deepcopy(source.goals)
        self.seed, self.tokenizer = source.seed, source.tokenizer
        self.logical = copy.deepcopy(source.state_dict())
        self.executor = self.future = None
        self.closed = self.failed = False
        self.handle = self  # Existing cleanup paths must drain BEFORE closing source.
        self.last_producer_error = None

    @property
    def consumed(self):
        return self.logical['consumed'].copy()

    @property
    def exhausted(self):
        return self.logical['consumed'] == self.goals

    def state_dict(self):
        return copy.deepcopy(self.logical)

    def _produce(self):
        rows = self.source.take(self.batch)
        state = copy.deepcopy(self.source.state_dict())
        ids, targets = stage_original_rows(rows)
        return rows, state, ids, targets

    def _submit(self):
        if self.executor is None:
            self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix='jmicro_TRAIN_CPU')
        if self.future is not None:
            raise ValueError('Only one queued original batch allowed')
        self.future = self.executor.submit(self._produce)

    def take_staged(self, size):
        if type(size) is not int or size != self.batch or self.closed or self.failed or self.exhausted:
            raise ValueError('Open nonexhausted fixed-batch logical sampler required')
        if self.future is None:
            self._submit()
        pending, self.future = self.future, None
        try:
            rows, state, ids, targets = pending.result()
        except BaseException:
            self.failed = True
            raise
        self.logical = state
        if not self.exhausted:
            self._submit()
        return rows, ids, targets

    def take(self, size):
        return self.take_staged(size)[0]

    def _quiesce(self):
        if self.future is not None:
            try:
                self.future.result()
            except Exception as error:
                self.last_producer_error = repr(error)
            self.future = None
        if self.executor is not None:
            self.executor.shutdown(wait=True, cancel_futures=True)
            self.executor = None

    def load_state_dict(self, state):
        if self.closed:
            raise ValueError('Closed producer cannot be restored')
        for key in ('kind', 'binding', 'seed', 'goals'):
            if state[key] != self.logical[key]:
                raise ValueError('Original logical sampler identity differs before mutation')
        self._quiesce()
        self.source.load_state_dict(copy.deepcopy(state))
        self.logical = copy.deepcopy(self.source.state_dict())
        self.failed = False
        self.last_producer_error = None

    def close(self):
        if not self.closed:
            self._quiesce()
            self.source.handle.close()
            self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()
