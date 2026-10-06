"""Original mixed reference order, fixed conditional outcome+EOS labels."""
import copy
import hashlib
from pathlib import Path
import numpy as np
import torch
from jmicro.experiment import sha256
from condition_positive_trainer import ConditionPositiveTrainer
from conditional_prefix_mask_trainer import PrefixMaskSampler,SOURCE_ORDER
from original_web_retention_trainer import OriginalWebQuotaSampler
from source_order_condition_trainer import SourceOrderQuotaSampler
from historical_parent_condition_trainer import HistoricalParentTrainer,historical_web_cursor

KIND='original_mixed_order_fixed_conditional_outcome_EOS_v1'


def chain(previous,array):
    digest=hashlib.sha256(bytes.fromhex(previous));digest.update(array);return digest.hexdigest()


class InterleavedOutcomeSampler(PrefixMaskSampler):
    def __init__(self,pool,original,positive,cursor,goals,context=1024,seed=42,reference_policy='interleaved'):
        if reference_policy not in ('interleaved','staged'):raise ValueError('Only the two original order policies allowed')
        self.reference_policy=reference_policy
        OriginalWebQuotaSampler.__init__(self,pool,original,positive,cursor,goals,context,seed)
        self.initial_reference=copy.deepcopy(self.reference_state())
        self.actual={k:dict.fromkeys(SOURCE_ORDER,0) for k in ('teachers','eos','body_bytes','focus','removed_prefix')}
        self.source_digests={g:dict.fromkeys(('input','reference_target','masked_target','focus'),'00'*32) for g in SOURCE_ORDER}
        self.reference_token_digest=None;self.last_genres=[]
        for genre,stream in self.streams.items():
            original_block=stream.block
            def recorded(context,genre=genre,original_block=original_block):
                self.last_genres.append(genre);return original_block(context)
            stream.block=recorded

    def reference_state(self):
        return (OriginalWebQuotaSampler.state_dict(self) if self.reference_policy=='interleaved'
                else SourceOrderQuotaSampler.state_dict(self))

    def batch(self,size):
        self.last_genres=[]
        x,y,reference_bytes,focused=(OriginalWebQuotaSampler.batch(self,size) if self.reference_policy=='interleaved'
            else SourceOrderQuotaSampler.batch(self,size))
        if len(self.last_genres)!=size or self.reference_token_digest is None:raise ValueError('Actual reference route/digest required')
        digest=hashlib.sha256(bytes.fromhex(self.reference_token_digest));digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
        self.reference_token_digest=digest.hexdigest();reference_y=y.clone();actual_bytes=0
        for i,genre in enumerate(self.last_genres):
            if genre=='conditional_textbook':
                remove=y[i].ne(-100)&~(focused[i]|y[i].eq(3))
                if (remove&y[i].lt(8)).any():raise ValueError('Only setup body targets may be removed')
                self.actual['removed_prefix'][genre]+=int(remove.sum());y[i,remove]=-100
            byte_count=int(self.view.byte_lengths[y[i][y[i]>=8].numpy()].sum());actual_bytes+=byte_count
            for field,value in dict(teachers=int(y[i].ne(-100).sum()),eos=int(y[i].eq(3).sum()),
                    body_bytes=byte_count,focus=int(focused[i].sum())).items():self.actual[field][genre]+=value
            for field,array in dict(input=x[i].numpy().astype('<i8'),reference_target=reference_y[i].numpy().astype('<i8'),
                    masked_target=y[i].numpy().astype('<i8'),focus=focused[i].numpy().astype(np.uint8)).items():
                self.source_digests[genre][field]=chain(self.source_digests[genre][field],array.tobytes())
        self.last_reference=dict(teachers=int(reference_y.ne(-100).sum()),body_bytes=reference_bytes)
        self.audit();return x,y,actual_bytes,focused

    def state_dict(self):
        state=self.reference_state()
        if not hasattr(self,'actual'):return state
        state['prefix_mask_accounting']=dict(actual=copy.deepcopy(self.actual),initial_reference=copy.deepcopy(self.initial_reference),
            reference_token_digest=self.reference_token_digest,source_digests=copy.deepcopy(self.source_digests),reference_policy=self.reference_policy)
        return state

    def load_state_dict(self,state):
        a=state.get('prefix_mask_accounting')
        if (not a or a['initial_reference']!=self.initial_reference or a['reference_policy']!=self.reference_policy
                or set(a['actual'])!=set(self.actual) or any(set(v)!=set(SOURCE_ORDER) for v in a['actual'].values())
                or set(a['source_digests'])!=set(SOURCE_ORDER)
                or any(set(v)!=set(self.source_digests[g]) for g,v in a['source_digests'].items())):
            raise ValueError('Original order and masked accounting binding differs')
        if self.reference_policy=='interleaved':OriginalWebQuotaSampler.load_state_dict(self,state)
        else:SourceOrderQuotaSampler.load_state_dict(self,state)
        self.actual=copy.deepcopy(a['actual']);self.source_digests=copy.deepcopy(a['source_digests']);self.reference_token_digest=a['reference_token_digest']
        if any(len(bytes.fromhex(v))!=32 for v in [self.reference_token_digest,*[d for values in self.source_digests.values() for d in values.values()]]):
            raise ValueError('Source/reference digest differs')
        self.audit()


class InterleavedOutcomeTrainer(HistoricalParentTrainer):
    def __init__(self,parent,pool,original,positive,goals,binding,device='cuda',context=1024,batch=32):
        super().__init__(parent,pool,original,positive,goals,binding,device,context,batch)
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        self.sampler=InterleavedOutcomeSampler(pool,original,positive,historical_web_cursor(parent),goals,context,42)
        self.sampler.reference_token_digest=parent['token_digest']
        self.spec.update(research_kind=KIND,interleaved_outcome_trainer_sha256=sha256(Path(__file__)),
            target_rule='conditional existing outcome-focus body plus original EOS; other sources unchanged')
        self.lineage.update(kind=KIND,actual_initial_reference_sampler=copy.deepcopy(self.sampler.initial_reference),
            source_sampler_policy='Original reference-progress-balanced interleaving; original quotas stop input, actual masked teachers separately counted.')
        self.audit_counters()

    def audit_counters(self):
        self.sampler.audit();a=self.sampler.actual;initial=self.sampler.initial_reference
        teachers=self.supervised_tokens-self.lineage['parent_supervised_tokens'];updates=self.update-self.lineage['parent_update']
        if (teachers!=sum(a['teachers'].values()) or self.weighted_teacher_mass!=teachers or self.focus_teacher_tokens!=sum(a['focus'].values())
                or self.body_bytes-self.lineage['parent_body_bytes']!=sum(a['body_bytes'].values())
                or updates!=self.sampler.position-initial['position']
                or self.tokens-self.lineage['parent_tokens']!=updates*self.spec['batch']*self.spec['context']
                or self.tokens-self.lineage['parent_tokens']!=sum(self.sampler.source_tokens.values())-sum(initial['source_tokens'].values())):
            raise ValueError('Completed original-mixed masked counters differ')

    def step(self):
        row=ConditionPositiveTrainer.step(self)
        row.update(reference_token_digest=self.sampler.reference_token_digest,
            reference_suffix_teacher_tokens=sum(self.sampler.source_teachers.values()),
            actual_source_teachers=copy.deepcopy(self.sampler.actual['teachers']),actual_source_eos=copy.deepcopy(self.sampler.actual['eos']),
            actual_source_body_bytes=copy.deepcopy(self.sampler.actual['body_bytes']),removed_prefix_targets=copy.deepcopy(self.sampler.actual['removed_prefix']),
            source_digests=copy.deepcopy(self.sampler.source_digests),actual_source_routes=list(self.sampler.last_genres))
        return row
