"""Same four source streams and quotas; long Web precedes complete short text."""
from pathlib import Path
import numpy as np
import torch
from jmicro.experiment import sha256
from original_web_retention_trainer import OriginalWebQuotaSampler
from historical_parent_condition_trainer import HistoricalParentTrainer, historical_web_cursor

SOURCE_ORDER=('web','story','ordinary_textbook','conditional_textbook')
KIND='historical_parent_source_order_100M'


class SourceOrderQuotaSampler(OriginalWebQuotaSampler):
    def batch(self,size):
        if type(size) is not int or size<=0:raise ValueError('Positive batch size required')
        if self.source_teachers==self.goals:raise ValueError('Teacher quotas exhausted')
        xs,ys,masks=[],[],[];body_bytes=0
        for _ in range(size):
            active=[g for g in SOURCE_ORDER if self.source_teachers[g]<self.goals[g]]
            genre=active[0] if active else 'web'
            if genre=='conditional_textbook':
                x,y,focused=self.streams[genre].block(self.context)
            else:
                x,y=self.streams[genre].block(self.context)
                focused=np.zeros(self.context,dtype=bool)
            remaining=self.goals[genre]-self.source_teachers[genre]
            labeled=np.flatnonzero(y!=-100)
            y[labeled[remaining:]]=-100
            focused &= y>=8
            byte_count=int(self.view.byte_lengths[y[y>=8]].sum())
            self.source_teachers[genre]+=int(np.count_nonzero(y!=-100))
            self.source_eos[genre]+=int(np.count_nonzero(y==3))
            self.source_tokens[genre]+=self.context
            self.source_body_bytes[genre]+=byte_count
            self.source_focus_teachers[genre]+=int(focused.sum())
            body_bytes+=byte_count;xs.append(x);ys.append(y);masks.append(focused)
        self.position+=1
        return torch.from_numpy(np.stack(xs)),torch.from_numpy(np.stack(ys)),body_bytes,torch.from_numpy(np.stack(masks))

    def state_dict(self):
        state=super().state_dict()
        state.update(kind='same-streams-staged-source-order-v1',source_order=list(SOURCE_ORDER))
        return state

    def load_state_dict(self,state):
        if state.get('source_order')!=list(SOURCE_ORDER):raise ValueError('Fixed source order differs')
        super().load_state_dict(state)


class SourceOrderHistoricalTrainer(HistoricalParentTrainer):
    def __init__(self,parent,pool,original_web,positive,goals,binding,device='cuda',context=1024,batch=32):
        super().__init__(parent,pool,original_web,positive,goals,binding,device,context,batch)
        self.sampler=SourceOrderQuotaSampler(pool,original_web,positive,historical_web_cursor(parent),goals,context,42)
        self.spec.update(research_kind=KIND,source_order=list(SOURCE_ORDER),source_order_trainer_sha256=sha256(Path(__file__)))
        self.lineage.update(kind='historical-Web-fullstate-source-order-fork',
            source_sampler_policy='Same source content/relative order/quota/seed and fullstate/LR as historical mixed control; exhaust Web then story then ordinary then conditional. Terminal padding still uses masked Web, preserving its actual physical cursor.')
