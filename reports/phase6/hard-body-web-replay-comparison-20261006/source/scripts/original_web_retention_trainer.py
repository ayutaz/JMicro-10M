"""Change only Web material/cursor; preserve immutable short-source protocols."""
import copy
from pathlib import Path
import numpy as np
from jmicro.experiment import sha256
from jmicro.shards import BlockSampler
from mature_condition_trainer import MatureQuotaSampler, MatureConditionTrainer


class OriginalWebStream:
    def __init__(self, view, parent_sampler, context):
        self.view = view
        self.manifest_sha256 = sha256(view.directory / 'manifest.json')
        self.sampler = BlockSampler(view, context, parent_sampler['seed'])
        self.sampler.load_state_dict(copy.deepcopy(parent_sampler))

    def block(self, context):
        if context != self.sampler.context: raise ValueError('Original Web context differs')
        x, y, _ = self.sampler.batch(1)
        return x[0].numpy().copy(), y[0].numpy().copy()

    def state_dict(self):
        return dict(kind='actual-parent-Web-block-cursor-v1',manifest_sha256=self.manifest_sha256,
                    sampler=self.sampler.state_dict())

    def load_state_dict(self, state):
        if state['kind'] != 'actual-parent-Web-block-cursor-v1' or state['manifest_sha256'] != self.manifest_sha256:
            raise ValueError('Original Web stream source identity differs')
        self.sampler.load_state_dict(state['sampler'])


class OriginalWebQuotaSampler(MatureQuotaSampler):
    def __init__(self, pool, original_web, positive, parent_sampler, goals, context=1024, seed=42):
        if not np.array_equal(pool.byte_lengths,original_web.byte_lengths):
            raise ValueError('Common tokenizer byte table required')
        super().__init__(pool,positive,goals,context,seed)
        self.streams['web'] = OriginalWebStream(original_web,parent_sampler,context)

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = 'original-Web-retention-short-source-quotas-v1'
        return state


class OriginalWebRetentionTrainer(MatureConditionTrainer):
    def __init__(self,parent,pool,original_web,positive,goals,binding,device='cuda',context=1024,batch=32):
        if parent['shard_manifest_sha256'] != sha256(original_web.directory / 'manifest.json'):
            raise ValueError('Actual parent original Web source required')
        super().__init__(parent,pool,positive,goals,binding,device,context,batch)
        self.sampler = OriginalWebQuotaSampler(pool,original_web,positive,parent['sampler'],goals,context,42)
        self.spec.update(research_kind='original_Web_retention_relation_100M',
            original_web_manifest_sha256=sha256(original_web.directory / 'manifest.json'),
            retention_trainer_sha256=sha256(Path(__file__)))
        self.lineage.update(kind='original-Web-cursor-retained-short-source-fork',
            source_sampler_policy='Actual original Web parent cursor continues; same fresh seed42 short-source streams. Web material/order differs from selected-Web control.')
