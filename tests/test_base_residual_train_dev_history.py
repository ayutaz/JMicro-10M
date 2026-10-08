"""Deterministic selection/exposure protocol; no scientific quality claim."""
import hashlib
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
import pytest
from run_base_residual_train_dev_history import match_dev,verify_update


def test_length_matching_ties_use_original_index_and_never_reuse_or_leak():
    train=[dict(full_original_body_sha256='t0',original_body_tokens=100),
           dict(full_original_body_sha256='t1',original_body_tokens=101)]
    candidates=[dict(index=3,canonical_sha256='d0',body_tokens=99),
                dict(index=1,canonical_sha256='d1',body_tokens=101),
                dict(index=0,canonical_sha256='t0',body_tokens=100),
                dict(index=4,canonical_sha256='d1',body_tokens=101)]
    matched=match_dev(train,candidates)
    assert [r['index'] for r in matched]==[1,3]


def test_insufficient_distinct_DEV_fails_without_redraw():
    train=[dict(full_original_body_sha256='t0',original_body_tokens=100),
           dict(full_original_body_sha256='t1',original_body_tokens=100)]
    with pytest.raises(ValueError,match='Insufficient'):
        match_dev(train,[dict(index=0,canonical_sha256='same',body_tokens=100),
                         dict(index=1,canonical_sha256='same',body_tokens=100)])


def test_exposure_guard_checks_every_original_id_trace_and_teacher_count():
    rows=[dict(index_byte_position=4,index_record_sha256='abc',input_ids=[2,9],target_ids=[9,3],
               target_first=1,target_end=3,teacher_tokens=2)]
    digest=hashlib.sha256(bytes(32)+json.dumps([(4,'abc',[2,9],[9,3])]).encode()).hexdigest()
    record=dict(token_digest=digest,draw_trace=[[4,'abc',1,3,2]],CE_targets_this_update=2,original_windows_this_update=1)
    assert verify_update(rows,record,'0'*64)==digest
    record['CE_targets_this_update']=3
    with pytest.raises(ValueError,match='history differs'): verify_update(rows,record,'0'*64)
