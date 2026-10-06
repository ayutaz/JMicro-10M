"""Full-vocabulary parent KL on train Web body positions; explicit replay ledger."""
import copy
import hashlib
import numpy as np
import torch
from torch.nn import functional as F
from original_web_retention_trainer import OriginalWebStream

POLICY=dict(kind='frozen-parent-Web-body-KL-v1',direction='parent_to_student',temperature=1.,coefficient=1.,
    every_completed_update=1,reference_context=1024,reference_batch=8,
    masked_targets='labels>=8; ignore EOS/BOS/role/padding positions, retain full vocabulary including EOS in probability normalization',
    reference_teacher='immutable actual historical10.5B parent, no optimizer/gradients',
    replay_policy='separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test')


def body_parent_kl(student_logits,parent_logits,labels):
    if student_logits.shape!=parent_logits.shape or student_logits.shape[:-1]!=labels.shape:
        raise ValueError('Same full-vocabulary logits and target positions required')
    valid=labels>=8
    positions=int(valid.sum())
    if positions==0:raise ValueError('At least one train Web body target required')
    student=F.log_softmax(student_logits.float(),dim=-1)
    parent=F.log_softmax(parent_logits.detach().float(),dim=-1)
    loss=F.kl_div(student,parent,log_target=True,reduction='none').sum(-1)[valid].sum()/positions
    if not torch.isfinite(loss):raise ValueError('Finite full-vocabulary KL required')
    return loss,dict(soft_target_body_positions=positions,ignored_special_positions=labels.numel()-positions,
        physical_reference_input_tokens=labels.numel(),new_ordinary_CE_teacher_tokens=0)


class WebBodyReplay:
    def __init__(self,view,cursor,batch=8,context=1024):
        if type(batch) is not int or batch<=0 or cursor['context']!=context:
            raise ValueError('Fixed valid replay shape required')
        self.initial_cursor=copy.deepcopy(cursor)
        self.stream=OriginalWebStream(view,cursor,context)
        self.batch,self.context=batch,context
        self.updates=self.physical_input_tokens=self.body_positions=self.ignored_positions=0
        self.digest='00'*32

    def next(self):
        xs,ys=[],[]
        for _ in range(self.batch):
            x,y=self.stream.block(self.context);xs.append(x);ys.append(y)
        x,y=torch.from_numpy(np.stack(xs)),torch.from_numpy(np.stack(ys))
        positions=int((y>=8).sum())
        if x.eq(0).any() or positions==0:raise ValueError('Unpadded train Web body replay required')
        digest=hashlib.sha256(bytes.fromhex(self.digest))
        digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
        self.updates+=1;self.physical_input_tokens+=x.numel();self.body_positions+=positions
        self.ignored_positions+=x.numel()-positions;self.digest=digest.hexdigest()
        return x,y

    def state_dict(self):
        return dict(kind=POLICY['kind'],batch=self.batch,context=self.context,initial_cursor=self.initial_cursor,
            stream=self.stream.state_dict(),updates=self.updates,physical_input_tokens=self.physical_input_tokens,
            body_positions=self.body_positions,ignored_positions=self.ignored_positions,digest=self.digest)

    def load_state_dict(self,state):
        if (state['kind']!=POLICY['kind'] or state['batch']!=self.batch or state['context']!=self.context
                or state['initial_cursor']!=self.initial_cursor
                or any(type(state[k]) is not int or state[k]<0 for k in
                    ('updates','physical_input_tokens','body_positions','ignored_positions'))
                or state['physical_input_tokens']!=state['updates']*self.batch*self.context
                or state['body_positions']+state['ignored_positions']!=state['physical_input_tokens']
                or len(state['digest'])!=64):
            raise ValueError('Replay source/shape/counter binding differs')
        bytes.fromhex(state['digest'])
        self.stream.load_state_dict(state['stream'])
        for key in ('updates','physical_input_tokens','body_positions','ignored_positions','digest'):
            setattr(self,key,state[key])
