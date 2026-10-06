"""Train-only opposite-context outcome pairs and non-EOS ranking objective."""
import copy
import hashlib
import math
from pathlib import Path
import random
import numpy as np
import torch
from torch.nn import functional as F
from jmicro.experiment import read_json,sha256

POLICY = dict(kind='train_opposite_context_non_EOS_outcome_ranking_v1',coefficient=1.,temperature=1.,
    families_per_update=2,candidate_rows_per_family=4,context=256,
    row_order='For each family: branch0-candidate0,branch0-candidate1,branch1-candidate0,branch1-candidate1; gold candidate equals branch.',
    scores='Mean token log probability of complete candidate body, excluding EOS3 from vocabulary normalization; prefix and padding labels ignored.',
    objective='Mean softplus(foil_score-gold_score) over both context poles of all selected families.',
    supervision='Relational choice labels and positive/foil scored positions are separate from ordinary CE teachers and parent-KL soft target positions.',
    input_source='Only already accepted1024 TRAIN families/2048 positive records; other opposite-state outcome is the foil. No dev/probe/test labels.',
    sampler='Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption.')


def outcome_ranking_loss(logits,labels):
    if (logits.shape[:-1]!=labels.shape or labels.ndim!=2 or labels.shape[0]%4
            or logits.shape[-1]<=8 or labels.dtype!=torch.long
            or ((labels!=-100)&(labels<8)).any() or (labels>=logits.shape[-1]).any()):
        raise ValueError('Complete4-row families with body labels or ignore required')
    body=labels>=8;counts=body.sum(-1)
    if (counts==0).any():raise ValueError('Every complete candidate must have scored body tokens')
    keep=torch.arange(logits.shape[-1],device=logits.device)!=3
    targets=torch.where(body,labels-1,-100)
    nll=F.cross_entropy(logits.float()[...,keep].reshape(-1,logits.shape[-1]-1),
        targets.reshape(-1),ignore_index=-100,reduction='none').reshape(labels.shape)
    scores=-(nll.sum(-1)/counts).reshape(-1,2,2)
    gold=torch.stack((scores[:,0,0],scores[:,1,1]),-1)
    foil=torch.stack((scores[:,0,1],scores[:,1,0]),-1)
    loss=F.softplus(foil-gold).mean()
    if not torch.isfinite(loss):raise ValueError('Finite context-sensitive ranking loss required')
    count_grid=counts.reshape(-1,2,2)
    return loss,dict(relational_choice_labels=labels.shape[0]//2,candidate_rows=labels.shape[0],
        gold_body_scored_positions=int(count_grid[:,0,0].sum()+count_grid[:,1,1].sum()),
        foil_body_scored_positions=int(count_grid[:,0,1].sum()+count_grid[:,1,0].sum()),
        ignored_prefix_padding_positions=labels.numel()-int(body.sum()),
        ordinary_CE_teacher_tokens=0,soft_target_body_positions=0)


class RankingTrainView:
    def __init__(self,directory,manifest_sha256):
        self.directory=Path(directory)
        if sha256(self.directory/'manifest.json')!=manifest_sha256:
            raise ValueError('Fixed ranking-input manifest required')
        m=read_json(self.directory/'manifest.json')
        if (m['kind']!='existing_train_relation_outcome_ranking_inputs_v1'
                or m['families']!=1024 or m['candidate_rows']!=4096 or m['context']!=256
                or m['new_original_corpus_tokens'] or m['source_split']!='train'
                or m['tokenizer_sha256']!='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'
                or sha256(self.directory/'arrays.npz')!=m['arrays_sha256']):
            raise ValueError('Existing train-only family inputs required')
        with np.load(self.directory/'arrays.npz',allow_pickle=False) as a:
            self.inputs=a['inputs'].astype(np.int64);self.labels=a['labels'].astype(np.int64)
            self.valid=a['valid'].astype(bool);self.target_bytes=a['target_bytes'].copy()
        self.family_ids=m['family_ids'];self.context=m['context']
        if (self.inputs.shape!=(4096,256) or self.labels.shape!=self.inputs.shape or self.valid.shape!=self.inputs.shape
                or len(set(self.family_ids))!=1024 or self.target_bytes.shape!=(4096,)
                or np.any(self.inputs[self.valid]==0) or np.any(self.inputs[~self.valid]!=0)
                or np.any((self.labels!=-100)&(self.labels<8))
                or np.any((self.labels>=8)&~self.valid) or np.any((self.labels>=8).sum(-1)==0)):
            raise ValueError('Unmodified complete body outcomes and padding mask required')
        self.binding=dict(manifest_sha256=manifest_sha256,train_manifest=m['train_manifest'],
            train_source=m['train_source'],arrays_sha256=m['arrays_sha256'],tokenizer_sha256=m['tokenizer_sha256'],
            family_ids_sha256=hashlib.sha256('\n'.join(self.family_ids).encode()).hexdigest())


class OutcomePairSampler:
    def __init__(self,view,families_per_update=2,seed=42):
        if type(families_per_update) is not int or families_per_update<=0 or not view.family_ids:
            raise ValueError('Positive fixed train-family batch required')
        self.view,self.families_per_update,self.seed=view,families_per_update,seed
        self.epoch=self.position=self.updates=self.families_seen=self.relational_choice_labels=0
        self.valid_input_tokens=self.physical_input_positions=0
        self.gold_body_scored_positions=self.foil_body_scored_positions=0
        self.gold_body_scored_bytes=self.foil_body_scored_bytes=0
        self.digest='00'*32;self.order=self._order(0)

    def _order(self,epoch):
        values=list(range(len(self.view.family_ids)))
        random.Random(self.seed+epoch).shuffle(values)
        return values

    def next(self):
        selected=[]
        for _ in range(self.families_per_update):
            if self.position==len(self.order):
                self.epoch+=1;self.position=0;self.order=self._order(self.epoch)
            selected.append(self.order[self.position]);self.position+=1
        indices=[4*f+i for f in selected for i in range(4)]
        x=torch.from_numpy(self.view.inputs[indices].copy())
        y=torch.from_numpy(self.view.labels[indices].copy())
        valid=torch.from_numpy(self.view.valid[indices].copy())
        counts=(y>=8).sum(-1).reshape(-1,2,2)
        sizes=self.view.target_bytes[indices].reshape(-1,2,2)
        self.updates+=1;self.families_seen+=len(selected);self.relational_choice_labels+=2*len(selected)
        self.valid_input_tokens+=int(valid.sum());self.physical_input_positions+=x.numel()
        self.gold_body_scored_positions+=int(counts[:,0,0].sum()+counts[:,1,1].sum())
        self.foil_body_scored_positions+=int(counts[:,0,1].sum()+counts[:,1,0].sum())
        self.gold_body_scored_bytes+=int(sizes[:,0,0].sum()+sizes[:,1,1].sum())
        self.foil_body_scored_bytes+=int(sizes[:,0,1].sum()+sizes[:,1,0].sum())
        digest=hashlib.sha256(bytes.fromhex(self.digest))
        for array in (x.numpy().astype('<i8'),y.numpy().astype('<i8'),valid.numpy().astype(np.uint8),np.asarray(selected,dtype='<i8')):
            digest.update(array.tobytes())
        self.digest=digest.hexdigest()
        return x,y,valid,selected

    def state_dict(self):
        return dict(kind='train_family_outcome_ranking_sampler_v1',binding=copy.deepcopy(self.view.binding),
            seed=self.seed,families_per_update=self.families_per_update,context=self.view.context,order=self.order.copy(),
            **{k:getattr(self,k) for k in ('epoch','position','updates','families_seen','relational_choice_labels',
                'valid_input_tokens','physical_input_positions','gold_body_scored_positions','foil_body_scored_positions',
                'gold_body_scored_bytes','foil_body_scored_bytes','digest')})

    def load_state_dict(self,state):
        counters=('epoch','position','updates','families_seen','relational_choice_labels','valid_input_tokens',
            'physical_input_positions','gold_body_scored_positions','foil_body_scored_positions','gold_body_scored_bytes','foil_body_scored_bytes')
        if (state['kind']!='train_family_outcome_ranking_sampler_v1' or state['binding']!=self.view.binding
                or state['seed']!=self.seed or state['families_per_update']!=self.families_per_update
                or state['context']!=self.view.context or any(type(state[k]) is not int or state[k]<0 for k in counters)
                or state['order']!=self._order(state['epoch']) or not 0<=state['position']<=len(self.order)
                or state['epoch']*len(self.order)+state['position']!=state['families_seen']
                or state['families_seen']!=state['updates']*self.families_per_update
                or state['relational_choice_labels']!=2*state['families_seen']
                or state['physical_input_positions']!=state['updates']*4*self.families_per_update*self.view.context
                or not state['gold_body_scored_positions']+state['foil_body_scored_positions']<=state['valid_input_tokens']<=state['physical_input_positions']
                or len(bytes.fromhex(state['digest']))!=32):
            raise ValueError('Ranking train binding/sampler/counters differ')
        for k in (*counters,'digest','order'):setattr(self,k,copy.deepcopy(state[k]))
