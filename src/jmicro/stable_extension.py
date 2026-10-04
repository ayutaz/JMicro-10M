"""Explicit WSD budget extension; the checkpoint-bound core stays unchanged."""
from pathlib import Path

import torch

from jmicro.experiment import sha256
from jmicro.training import Trainer


class StableExtensionTrainer(Trainer):
    def load_extension(self, path, expected_sha256=None):
        path = Path(path)
        digest = sha256(path)
        if expected_sha256 is not None and digest != expected_sha256:
            raise ValueError('Extension parent checksum differs')
        parent = torch.load(path, map_location='cpu', weights_only=False)
        old, new = parent['spec'], self.spec
        if (old.get('scheduler') != 'wsd' or new.get('scheduler') != 'wsd'
                or parent['update'] < old['warmup']
                or parent['update'] > old['schedule_updates']
                or new['schedule_updates'] <= old['schedule_updates']
                or {k: v for k, v in old.items() if k != 'schedule_updates'}
                != {k: v for k, v in new.items() if k != 'schedule_updates'}):
            raise ValueError('Extension requires stable WSD and only a larger update budget')
        # Core load checks model, source, data and all parent settings. WSD's
        # lambda captures the new budget but is identical at every stable step.
        self.spec = old
        try:
            super().load(path)
        finally:
            self.spec = new
        self.lineage = {
            'kind': 'wsd_stable_budget_extension',
            'parent_checkpoint': str(path.resolve()), 'parent_sha256': digest,
            'parent_update': parent['update'], 'parent_tokens': parent['tokens'],
            'parent_spec': old, 'parent_token_digest': parent['token_digest'],
            'parent_lineage': parent.get('lineage'),
            'old_schedule_updates': old['schedule_updates'],
            'new_schedule_updates': new['schedule_updates'],
            'extension_implementation_sha256': sha256(Path(__file__)),
        }

    def load(self, path, *, decay_branch=False):
        state = torch.load(path, map_location='cpu', weights_only=False)
        lineage = state.get('lineage') or {}
        if (lineage.get('kind') == 'wsd_stable_budget_extension'
                and lineage.get('extension_implementation_sha256') != sha256(Path(__file__))):
            raise ValueError('Extension implementation differs')
        super().load(path, decay_branch=decay_branch)
