"""Real CPU tiny transactions are protocol evidence, not model quality."""
import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from block_Web_constraint import BlockWebTrainer
from finite_Web_constraint import ConstraintRejected
from test_finite_Web_constraint import memory
from test_interleaved_outcome import historical_fixture
from run_eos_short_pilot import equal_state


def fixture(tmp_path):
    pool,parent,b,positive=historical_fixture(tmp_path);goals=dict(web=13,story=13,ordinary_textbook=13,conditional_textbook=197)
    def build(block_updates=2):return BlockWebTrainer(parent,pool,pool,positive,goals,b,memory(),{'CPU_fixture':True},device='cpu',context=8,batch=3,block_updates=block_updates)
    return parent,build


def test_cpu_fullstate_two_blocks_continuous_vs_resumed_and_boundary_only_labels(tmp_path):
    parent,build=fixture(tmp_path);t=build();a=t.block()+t.block();t.save(tmp_path/'continuous.pt')
    t=build();b=t.block();t.save(tmp_path/'split.pt');t=build();t.load(tmp_path/'split.pt');b+=t.block();t.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'continuous.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    for key in set(a[0])-{'seconds','data_wait_seconds','tokens_per_second'}:assert equal_state([r[key] for r in a],[r[key] for r in b]),key
    assert all(r['constraint_valid_only_at_block_boundary'] for r in a)
    assert a[0]['block_boundary_update']==a[1]['update'] and a[0]['update']!=a[0]['block_boundary_update']
    assert t.auxiliary['accepted_blocks']==2 and t.auxiliary['accepted_updates']==4
    assert a[-1]['removed_prefix_targets']['conditional_textbook']>0
    with pytest.raises(RuntimeError):t.step()


def test_real_whole_block_rejection_restores_all_state_and_attempted_exposures(tmp_path):
    _,build=fixture(tmp_path);t=build();t.block();t.save(tmp_path/'before.pt')
    def impossible(gradient=False):
        t.oracle.stats['gradient_calls' if gradient else 'forward_only_calls']+=1
        t.oracle.stats['teacher_observations']+=t.oracle.teachers;t.oracle.stats['physical_input_tokens']+=t.oracle.physical
        if gradient:t.oracle.stats['gradient_teacher_tokens']+=t.oracle.teachers
        return t.reference_ce*2,[torch.zeros_like(p) for p in t.model.parameters()] if gradient else None
    t.oracle.measure=impossible
    with pytest.raises(ConstraintRejected):t.block()
    t.save(tmp_path/'after.pt')
    assert equal_state(torch.load(tmp_path/'before.pt',weights_only=False),torch.load(tmp_path/'after.pt',weights_only=False))
    assert t.last_rejection['attempted_source_updates']==2 and t.last_rejection['attempted_source_gradient_teacher_tokens']>0
    assert t.last_rejection['auxiliary_completed_calls']['gradient_teacher_tokens']==t.oracle.teachers
    assert all(p.grad is None for p in t.model.parameters())


def test_real_interrupted_tentative_update_rolls_back_entire_block(tmp_path):
    _,build=fixture(tmp_path);t=build();t.block();t.save(tmp_path/'before.pt');calls=[0]
    def interrupt():
        calls[0]+=1
        if calls[0]==2:raise InterruptedError('Test only')
    with pytest.raises(InterruptedError):t.block(interrupt)
    t.save(tmp_path/'after.pt')
    assert equal_state(torch.load(tmp_path/'before.pt',weights_only=False),torch.load(tmp_path/'after.pt',weights_only=False))
    assert t.last_rejection['attempted_source_updates']==1 and t.last_rejection['rollback_scope']=='entire_tentative_block'


def test_final_short_block_no_empty_commit_and_tampered_boundary_rejected(tmp_path):
    _,build=fixture(tmp_path);t=build(7);sizes=[]
    while t.sampler.source_teachers!=t.sampler.goals:sizes.append(len(t.block()))
    assert sizes and all(1<=n<=7 for n in sizes) and sizes[-1]<7
    t.save(tmp_path/'end.pt')
    with pytest.raises(RuntimeError):t.block()
    state=torch.load(tmp_path/'end.pt',weights_only=False);state['last_constraint']['final_body_NLL']=t.reference_ce*1.02
    torch.save(state,tmp_path/'bad.pt')
    with pytest.raises(ValueError):build(7).load(tmp_path/'bad.pt')
