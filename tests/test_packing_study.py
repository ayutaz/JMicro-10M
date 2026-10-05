import copy
from types import SimpleNamespace
import numpy as np
import torch
from jmicro.shards import BlockSampler
from jmicro.packing_study import IsolatedDocuments,ShuffledDocumentBlocks,TeacherBudgetMixture,teacher_lr


def shard():
    tokens=[];index=[]
    for i in range(12):
        index.append(dict(offset=len(tokens),body_tokens=3,split='train'))
        tokens.extend([2,8+i,28+i,48+i,3])
    return SimpleNamespace(split='train',tokens=np.array(tokens,dtype='<u2'),index=index,byte_lengths=np.array([0]*8+[1]*64))


def test_isolated_never_sees_neighbor_and_supervises_EOS_not_PAD():
    s=IsolatedDocuments(shard(),8,42,batch=3);x,y,_=s.batch(32)
    assert x.shape==(3,8)
    assert torch.all(x[:,0]==2) and torch.all(y[:,3]==3)
    assert torch.all(y[:,4:]==-100) and torch.all(x[:,4:]==0)
    assert torch.all(y[:,:3]==x[:,1:4])


def test_document_shuffle_preserves_whole_docs_and_changes_epoch():
    s=ShuffledDocumentBlocks(shard(),8,42);before=s.shard.tokens.copy()
    chunks=s.shard.tokens.reshape(-1,5)
    assert all(row[0]==2 and row[-1]==3 and row[2]-row[1]==20 for row in chunks)
    s.epoch=1;s._shuffle()
    assert not np.array_equal(before,s.shard.tokens)
    assert set(map(tuple,before.reshape(-1,5)))==set(map(tuple,s.shard.tokens.reshape(-1,5)))


def test_shuffle_resume_rebuilds_identical_epoch_and_cursor():
    a=ShuffledDocumentBlocks(shard(),8,42);a.batch(11);state=a.state_dict()
    b=ShuffledDocumentBlocks(shard(),8,42);b.load_state_dict(state)
    assert all(torch.equal(x,y) if torch.is_tensor(x) else x==y for x,y in zip(a.batch(3),b.batch(3)))


def test_exact_teachers_exclude_PAD_and_resume_preserves_next_batch():
    # Web not used; a larger fake web supplies the inherited1024 block cursor.
    web=shard();web.tokens=np.tile(web.tokens,100)
    parent=BlockSampler(web,1024,42).state_dict()
    a=TeacherBudgetMixture(web,shard(),'isolated',parent,dict(web=0,short=37),isolated_batch=3)
    a.batch(32);state=copy.deepcopy(a.state_dict())
    b=TeacherBudgetMixture(web,shard(),'isolated',parent,dict(web=0,short=37),isolated_batch=3);b.load_state_dict(state)
    x=a.batch(32);y=b.batch(32)
    assert torch.equal(x[0],y[0]) and torch.equal(x[1],y[1])
    while sum(a.source_teachers.values())<37:a.batch(32)
    assert a.source_teachers==dict(web=0,short=37)
    assert a.source_physical_tokens['short']>a.source_tokens['short']
    assert a.source_eos['short']>0


def test_teacher_schedule_has_stable90percent_and_exact_floor():
    assert teacher_lr(0,1000,.0001)==.0001
    assert teacher_lr(900,1000,.0001)==.0001
    assert abs(teacher_lr(950,1000,.0001)-.000055)<1e-12
    assert abs(teacher_lr(1000,1000,.0001)-.00001)<1e-12
