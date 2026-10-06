import copy
import sys
from pathlib import Path
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from interleaved_outcome_trainer import InterleavedOutcomeTrainer
from review_interleaved_outcome_order import accounting
from interleaved_order_analysis import four_cell_contrasts
from test_interleaved_outcome import historical_fixture
from test_shared_prefix_web_loss import body


def test_actual_CPU_completed_masked_recipe_rejects_nominal_teacher_and_source_hash_changes(tmp_path):
    pool,parent,b,positive=historical_fixture(tmp_path);goals=dict(web=199,story=51,ordinary_textbook=71,conditional_textbook=197)
    t=InterleavedOutcomeTrainer(parent,pool,pool,positive,goals,b,'cpu',8,3);rows=[t.step() for _ in range(4)];cp=tmp_path/'a.pt';t.save(cp)
    state=torch.load(cp,weights_only=False);record=dict(binding=b,additional_supervised_tokens=t.supervised_tokens-parent['supervised_tokens'],
        additional_input_tokens=t.tokens-parent['tokens'],sampler=state['sampler'],token_digest=t.token_digest,source_digests=t.sampler.source_digests,
        reference_token_digest=t.sampler.reference_token_digest)
    teachers=bytes_seen=0;expected=[]
    for row in rows:
        expected.append(dict(update=row['update'],reference_token_digest=row['reference_token_digest'],actual_source_routes=row['actual_source_routes'],
            actual_teachers=row['additional_teacher_tokens']-teachers,actual_body_bytes=row['body_bytes_seen']-parent['body_bytes']-bytes_seen))
        teachers=row['additional_teacher_tokens'];bytes_seen=row['body_bytes_seen']-parent['body_bytes']
    ledger=dict(rows=expected,actual_masked_suffix_teacher_tokens=teachers,actual_source_accounting=t.sampler.actual,
        original_reference_token_digest=t.sampler.reference_token_digest,source_digests=t.sampler.source_digests,staged_source_digests=t.sampler.source_digests,
        terminal_reference_sampler=t.sampler.reference_state(),original_reference_suffix_teacher_tokens=rows[-1]['reference_suffix_teacher_tokens'])
    assert accounting(parent,state,record,rows,ledger)['actual_new_hard_teachers']==teachers
    wrong=copy.deepcopy(record);wrong['additional_supervised_tokens']=ledger['original_reference_suffix_teacher_tokens']
    with pytest.raises(ValueError):accounting(parent,state,wrong,rows,ledger)
    wrong=copy.deepcopy(ledger);wrong['staged_source_digests']['story']['masked_target']='ff'*32
    with pytest.raises(ValueError):accounting(parent,state,record,rows,wrong)
    with pytest.raises(ValueError):accounting(parent,state,record,rows[1:],ledger)


def test_four_cell_interaction_with_unequal_bytes_and_paired_coherence():
    ev={k:dict(body=body(values)) for k,values in dict(full_mixed=[1,1],full_staged=[3,3],masked_staged=[2,2],masked_mixed=[1.5,1.5]).items()}
    scores={k:{'a':dict(coherence=2 if k=='masked_mixed' else 1),'b':dict(coherence=1)} for k in ev}
    r=four_cell_contrasts(ev,scores);x=r['contrasts']['interaction_mask_effect_mixed_minus_staged']
    assert x['body_BPB_change']==pytest.approx((1+2)/__import__('math').log(2)/10)
    assert x['coherence_count_change']==1
    wrong=copy.deepcopy(ev);wrong['masked_mixed']['body']['rows'].reverse()
    with pytest.raises(ValueError):four_cell_contrasts(wrong,scores)
