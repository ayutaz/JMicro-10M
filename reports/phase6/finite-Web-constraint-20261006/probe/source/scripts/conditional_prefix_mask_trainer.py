"""Continue an original staged suffix; mask conditional setup targets only."""
import copy
import hashlib
import math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import torch
from jmicro.experiment import sha256
from jmicro.training import Trainer,implementation_hashes,restore_rng
from condition_positive_trainer import ConditionPositiveTrainer
from source_order_condition_trainer import SourceOrderQuotaSampler,SOURCE_ORDER

KIND='original_staged_suffix_conditional_prefix_mask_v1'
COUNTERS=('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers')


class PrefixMaskSampler(SourceOrderQuotaSampler):
    def __init__(self,pool,original,positive,parent_state):
        cursor=parent_state['streams']['web']['sampler']
        super().__init__(pool,original,positive,cursor,parent_state['goals'],parent_state['context'],parent_state['seed'])
        super().load_state_dict(copy.deepcopy(parent_state))
        self.initial_reference=copy.deepcopy(parent_state)
        self.actual={k:dict.fromkeys(SOURCE_ORDER,0) for k in ('teachers','eos','body_bytes','focus','removed_prefix')}
        self.reference_token_digest=None
        self.last_genres=[]
        # Record the actual source invocation. A zero-focus conditional row is
        # still conditional; do not infer its genre from the focus mask.
        for genre,stream in self.streams.items():
            original_block=stream.block
            def recorded(context,genre=genre,original_block=original_block):
                self.last_genres.append(genre)
                return original_block(context)
            stream.block=recorded

    def reference_state(self):
        return super().state_dict()

    def batch(self,size):
        self.last_genres=[]
        x,y,reference_bytes,focused=super().batch(size)
        if len(self.last_genres)!=size:raise ValueError('Actual source routes missing')
        if self.reference_token_digest is None:raise ValueError('Reference digest initial state required')
        digest=hashlib.sha256(bytes.fromhex(self.reference_token_digest))
        digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
        self.reference_token_digest=digest.hexdigest()
        original_y=y.clone();actual_bytes=0
        for i,genre in enumerate(self.last_genres):
            if genre=='conditional_textbook':
                remove=y[i].ne(-100)&~(focused[i]|y[i].eq(3))
                if (remove&y[i].lt(8)).any():raise ValueError('Only conditional setup body labels may be removed')
                self.actual['removed_prefix'][genre]+=int(remove.sum())
                y[i,remove]=-100
            bytes_here=int(self.view.byte_lengths[y[i][y[i]>=8].numpy()].sum())
            self.actual['teachers'][genre]+=int(y[i].ne(-100).sum())
            self.actual['eos'][genre]+=int(y[i].eq(3).sum())
            self.actual['body_bytes'][genre]+=bytes_here
            self.actual['focus'][genre]+=int(focused[i].sum())
            actual_bytes+=bytes_here
        self.last_reference=dict(teachers=int(original_y.ne(-100).sum()),body_bytes=reference_bytes)
        self.audit()
        return x,y,actual_bytes,focused

    def audit(self):
        for genre in SOURCE_ORDER:
            delta={k:getattr(self,k)[genre]-self.initial_reference[k][genre] for k in COUNTERS}
            a={k:v[genre] for k,v in self.actual.items()}
            if (any(v<0 for v in delta.values()) or any(type(v) is not int or v<0 for v in a.values())
                    or a['teachers']+a['removed_prefix']!=delta['source_teachers']
                    or a['eos']!=delta['source_eos'] or a['focus']!=delta['source_focus_teachers']
                    or a['eos']+a['focus']>a['teachers'] or a['body_bytes']>delta['source_body_bytes']):
                raise ValueError('Reference versus actual target accounting differs')
            if genre!='conditional_textbook' and (a['removed_prefix'] or a['body_bytes']!=delta['source_body_bytes']):
                raise ValueError('Nonconditional labels changed')
        if self.position<self.initial_reference['position']:raise ValueError('Original input cursor went backwards')

    def state_dict(self):
        state=super().state_dict()
        if not hasattr(self,'actual'):return state
        state['prefix_mask_accounting']=dict(actual=copy.deepcopy(self.actual),
            initial_reference=copy.deepcopy(self.initial_reference),reference_token_digest=self.reference_token_digest)
        return state

    def load_state_dict(self,state):
        account=state.get('prefix_mask_accounting')
        if (not account or account['initial_reference']!=self.initial_reference
                or set(account['actual'])!=set(self.actual)
                or any(set(v)!=set(SOURCE_ORDER) for v in account['actual'].values())):
            raise ValueError('Masked suffix accounting identity differs')
        super().load_state_dict(state)
        self.actual=copy.deepcopy(account['actual']);self.reference_token_digest=account['reference_token_digest']
        if len(bytes.fromhex(self.reference_token_digest))!=32:raise ValueError('Reference target digest differs')
        self.audit()


class PrefixMaskTrainer(ConditionPositiveTrainer):
    def __init__(self,parent,pool,original,positive,binding,device='cuda'):
        if (parent['implementation_sha256']!=implementation_hashes()
                or parent['sampler'].get('kind')!='same-streams-staged-source-order-v1'
                or parent['sampler']['source_order']!=list(SOURCE_ORDER)
                or parent['sampler']['source_teachers']['conditional_textbook']):
            raise ValueError('Original fullstate before first conditional exposure required')
        if any(not math.isclose(g['lr'],.00001,rel_tol=1e-10) for g in parent['optimizer']['param_groups']):
            raise ValueError('Original actual LR floor required')
        spec=copy.deepcopy(parent['spec'])
        spec.update(research_kind=KIND,prefix_mask_trainer_sha256=sha256(Path(__file__)),
            target_rule='conditional existing outcome-focus body plus original EOS; other sources unchanged',
            dtype='bf16' if device=='cuda' else 'fp32',backend='flash' if device=='cuda' else 'math',compile=device=='cuda')
        stub=SimpleNamespace(tokens=pool.tokens[:spec['context']+1],split='train',manifest=pool.manifest,
            byte_lengths=pool.byte_lengths,directory=pool.directory)
        Trainer.__init__(self,parent['model_config'],stub,spec,device)
        self.shard=pool;self.model.load_state_dict(parent['model'],strict=True)
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        if any(not math.isclose(g['lr']/base,.1,rel_tol=1e-10) for g,base in
                zip(parent['optimizer']['param_groups'],parent['scheduler']['base_lrs'],strict=True)):
            raise ValueError('Permanent scheduler floor required')
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:.1)
        self.scheduler.load_state_dict(copy.deepcopy(parent['scheduler']))
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        self.sampler=PrefixMaskSampler(pool,original,positive,parent['sampler'])
        self.sampler.reference_token_digest=parent['token_digest']
        self.factor=1
        for k in ('update','tokens','supervised_tokens','body_bytes','token_digest'):setattr(self,k,parent[k])
        self.focus_teacher_tokens=self.weighted_teacher_mass=0;self.focus_token_digest='00'*32
        self.binding=copy.deepcopy(binding);self.pilot_binding=dict(parent.get('pilot_binding',{}),**binding)
        self.lineage=dict(kind=KIND,parent=binding['parent'],parent_update=parent['update'],parent_tokens=parent['tokens'],
            parent_supervised_tokens=parent['supervised_tokens'],parent_body_bytes=parent['body_bytes'],
            parent_token_digest=parent['token_digest'],actual_parent_sampler=copy.deepcopy(parent['sampler']),
            parent_scheduler=copy.deepcopy(parent['scheduler']),optimizer_policy='inherit',no_reheat=True,
            source_sampler_policy='Continue every original stream/cursor/quota and input; reference quotas are not masked hard teachers.')
        restore_rng(parent['rng']);self.audit_counters()

    def audit_counters(self):
        self.sampler.audit();a=self.sampler.actual;initial=self.lineage['actual_parent_sampler']
        teachers=self.supervised_tokens-self.lineage['parent_supervised_tokens']
        updates=self.update-self.lineage['parent_update']
        if (teachers!=sum(a['teachers'].values()) or self.weighted_teacher_mass!=teachers
                or self.focus_teacher_tokens!=sum(a['focus'].values())
                or self.body_bytes-self.lineage['parent_body_bytes']!=sum(a['body_bytes'].values())
                or updates!=self.sampler.position-initial['position']
                or self.tokens-self.lineage['parent_tokens']!=updates*self.spec['batch']*self.spec['context']
                or self.tokens-self.lineage['parent_tokens']!=sum(self.sampler.source_tokens.values())-sum(initial['source_tokens'].values())):
            raise ValueError('Completed masked suffix counters differ')

    def step(self):
        row=super().step()
        row.update(reference_token_digest=self.sampler.reference_token_digest,
            reference_suffix_teacher_tokens=sum(self.sampler.source_teachers.values())-sum(self.sampler.initial_reference['source_teachers'].values()),
            actual_source_teachers=copy.deepcopy(self.sampler.actual['teachers']),
            actual_source_eos=copy.deepcopy(self.sampler.actual['eos']),actual_source_body_bytes=copy.deepcopy(self.sampler.actual['body_bytes']),
            removed_prefix_targets=copy.deepcopy(self.sampler.actual['removed_prefix']),actual_source_routes=list(self.sampler.last_genres))
        return row
