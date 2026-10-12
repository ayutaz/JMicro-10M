"""Separate padding diagnostic; preserve complete teacher order and updates."""
from pathlib import Path
import torch
from jmicro.experiment import sha256
from jmicro.teacher_chat_training import TeacherBudgetSampler,TeacherChatTrainer

POLICY='crop_only_trailing_PAD_rows_and_columns_v1'


class DynamicTeacherSampler(TeacherBudgetSampler):
    @classmethod
    def from_native(cls,native):
        # Windows/token arrays are read-only in the native sampler. Cursor and
        # counters are scalar values; shuffling replaces, rather than edits,order.
        result=cls.__new__(cls);result.__dict__=dict(native.__dict__)
        return result

    def next_update(self):
        batches,teachers,body_bytes=super().next_update();cropped=[]
        for x,y in batches:
            active=y.ne(-100).any(dim=1);rows=int(active.sum())
            assert rows>0 and bool(active[:rows].all()) and not bool(active[rows:].any())
            lengths=x.ne(0).sum(dim=1);length=int(lengths.max())
            assert 0<length<=self.context
            assert not bool(x[:,length:].ne(0).any()) and not bool(y[:,length:].ne(-100).any())
            assert not bool(x[rows:].ne(0).any()) and not bool(y[rows:].ne(-100).any())
            for row,n in enumerate(lengths[:rows]):
                assert bool(x[row,:int(n)].ne(0).all()),'No internal PAD may be removed'
            a,b=x[:rows,:length].contiguous(),y[:rows,:length].contiguous()
            self.physical_tokens-=x.numel()-a.numel();cropped.append((a,b))
        assert sum(int(y.ne(-100).sum()) for _,y in cropped)==teachers
        return cropped,teachers,body_bytes

    def state_dict(self):return dict(super().state_dict(),padding_policy=POLICY)

    def load_state_dict(self,state):
        if state.get('padding_policy')!=POLICY:raise ValueError('Dynamic padding policy mismatch')
        super().load_state_dict(state)


class DynamicTeacherTrainer(TeacherChatTrainer):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.sampler=DynamicTeacherSampler.from_native(self.sampler)
        self.spec=dict(self.spec,dynamic_padding=dict(policy=POLICY,source_sha256=sha256(Path(__file__))))
        self.lineage=dict(self.lineage,padding_policy=POLICY,separate_efficiency_condition=True)
