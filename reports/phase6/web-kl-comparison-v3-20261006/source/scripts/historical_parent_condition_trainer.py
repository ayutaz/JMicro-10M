"""Fork the documented historical Web fullstate without reheating its actual LR."""
import copy
import math
import torch
from pathlib import Path
from types import SimpleNamespace
from jmicro.experiment import sha256
from jmicro.training import Trainer, implementation_hashes, restore_rng
from condition_positive_trainer import ConditionPositiveTrainer
from original_web_retention_trainer import OriginalWebQuotaSampler

LR = .00001
KIND = 'historical_Web_parent_inherited_condition_100M'


def historical_web_cursor(parent):
    sampler = parent['sampler']
    if (sampler.get('kind') != 'eos-pilot-mixture-v1' or sampler['position'] != len(sampler['routes'])
            or any(sampler['routes']) or sampler['source_tokens']['short'] != 0
            or sampler['source_eos']['short'] != 0 or sampler['short']['position'] != 0
            or set(sampler['web']) != {'seed','epoch','position','context','blocks'}):
        raise ValueError('Completed actual pure-Web guard sampler required')
    if any(not math.isclose(g['lr'],LR,rel_tol=1e-10) for g in parent['optimizer']['param_groups']):
        raise ValueError('Preserve actual historical terminal LR0.00001 without reheat')
    return copy.deepcopy(sampler['web'])


class HistoricalParentTrainer(ConditionPositiveTrainer):
    def __init__(self,parent,pool,original_web,positive,goals,binding,device='cuda',context=1024,batch=32):
        cursor = historical_web_cursor(parent)
        if parent['implementation_sha256'] != implementation_hashes():
            raise ValueError('Historical parent core implementation differs')
        if parent['shard_manifest_sha256'] != sha256(original_web.directory/'manifest.json'):
            raise ValueError('Historical actual original Web source differs')
        if parent['update'] != 320435 or parent['tokens'] != 10500014080 or parent['supervised_tokens'] != 10477786961:
            raise ValueError('Only the preselected documented10.5B parent may be used')
        sampler = OriginalWebQuotaSampler(pool,original_web,positive,cursor,goals,context,42)
        lrs = [g['lr'] for g in parent['optimizer']['param_groups']]
        spec = dict(seed=42,context=context,batch=batch,accumulation=1,lr=LR,
            weight_decay=parent['spec']['weight_decay'],warmup=0,
            schedule_updates=parent['update']+math.ceil(2*sum(goals.values())/(context*batch))+32,
            scheduler='wsd',dtype='bf16' if device=='cuda' else 'fp32',backend='flash' if device=='cuda' else 'math',
            compile=device=='cuda',compile_mode='reduce-overhead',training_fast_path=True,deterministic=True,
            teacher_goals=dict(goals),research_kind=KIND,outcome_weight=1,positive_manifest_sha256=positive.manifest_sha256,
            original_web_manifest_sha256=parent['shard_manifest_sha256'],historical_trainer_sha256=sha256(Path(__file__)))
        stub = SimpleNamespace(tokens=pool.tokens[:context+1],split='train',manifest=pool.manifest,
                               byte_lengths=pool.byte_lengths,directory=pool.directory)
        Trainer.__init__(self,parent['model_config'],stub,spec,device)
        self.shard = pool
        self.model.load_state_dict(parent['model'],strict=True)
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        # The historical schedule is already at its permanent0.1 decay floor.
        # Keep its actual base_lrs/clock/state and the same future floor value;
        # loading those base_lrs into a unit multiplier would reheat to0.0001.
        if any(not math.isclose(lr/base,.1,rel_tol=1e-10)
               for lr,base in zip(lrs,parent['scheduler']['base_lrs'],strict=True)):
            raise ValueError('Historical actual permanent decay floor differs')
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _: .1)
        self.scheduler.load_state_dict(copy.deepcopy(parent['scheduler']))
        self.sampler,self.factor = sampler,1
        for key in ('update','tokens','supervised_tokens','body_bytes','token_digest'):
            setattr(self,key,parent[key])
        self.focus_teacher_tokens = self.weighted_teacher_mass = 0
        self.focus_token_digest = '00'*32
        self.binding = copy.deepcopy(binding)
        self.pilot_binding = dict(parent.get('pilot_binding',{}),**binding)
        self.lineage = dict(kind='historical-Web-fullstate-actual-LR-short-source-fork',parent=binding['parent'],
            parent_update=parent['update'],parent_tokens=parent['tokens'],parent_supervised_tokens=parent['supervised_tokens'],
            parent_body_bytes=parent['body_bytes'],parent_token_digest=parent['token_digest'],
            actual_parent_sampler=copy.deepcopy(parent['sampler']),actual_parent_Web_cursor=cursor,
            parent_scheduler=copy.deepcopy(parent['scheduler']),optimizer_policy='inherit',no_reheat=True,
            source_sampler_policy='Continue the actual nested historical Web cursor; same fresh seed42 story/ordinary/relation streams and quotas. Parent Web exposure/Adam/RNG/scheduler and actual LR differ from original10B route.')
        restore_rng(parent['rng'])
