"""Reject unmasked teacher claims and altered original-input suffix ledgers."""
import copy
import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from conditional_prefix_mask_trainer import PrefixMaskTrainer
from review_conditional_prefix_mask import accounting
from test_conditional_prefix_mask import shared_fixture


def test_completed_actual_CPU_masked_state_rejects_reference_label_count_and_missing_updates(tmp_path):
    pool,parent,b,positive=shared_fixture(tmp_path)
    t=PrefixMaskTrainer(parent,pool,pool,positive,b,'cpu');rows=[t.step() for _ in range(4)]
    cp=tmp_path/'actual.pt';t.save(cp);state=torch.load(cp,weights_only=False)
    record=dict(binding=b,additional_supervised_tokens=t.supervised_tokens-parent['supervised_tokens'],
        additional_input_tokens=t.tokens-parent['tokens'],sampler=state['sampler'],token_digest=t.token_digest,
        reference_token_digest=t.sampler.reference_token_digest)
    expected=[];teachers=body=0
    for row in rows:
        expected.append(dict(update=row['update'],reference_token_digest=row['reference_token_digest'],
            actual_source_routes=row['actual_source_routes'],actual_teachers=row['additional_teacher_tokens']-teachers,
            actual_body_bytes=row['body_bytes_seen']-parent['body_bytes']-body))
        teachers=row['additional_teacher_tokens'];body=row['body_bytes_seen']-parent['body_bytes']
    ledger=dict(rows=expected,actual_masked_suffix_teacher_tokens=teachers,actual_source_accounting=t.sampler.actual,
        original_reference_token_digest=t.sampler.reference_token_digest,terminal_reference_sampler=t.sampler.reference_state(),
        original_reference_suffix_teacher_tokens=rows[-1]['reference_suffix_teacher_tokens'])
    assert accounting(parent,state,record,rows,ledger)['new_actual_hard_teachers']==teachers
    wrong=copy.deepcopy(record);wrong['additional_supervised_tokens']=ledger['original_reference_suffix_teacher_tokens']
    assert wrong['additional_supervised_tokens']>teachers
    with pytest.raises(ValueError):accounting(parent,state,wrong,rows,ledger)
    wrong=copy.deepcopy(ledger);wrong['rows'][1]['reference_token_digest']='ff'*32
    with pytest.raises(ValueError):accounting(parent,state,record,rows,wrong)
    with pytest.raises(ValueError):accounting(parent,state,record,rows[1:],ledger)
