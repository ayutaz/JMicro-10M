import copy
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_readout_source_stages import paired_stages,SOURCES


def test_exclusive_and_mixed_batches_use_actual_teacher_denominators():
    rows=[]
    for update,totals,loss in ((1,(2,0,0,0),3.),(2,(6,0,0,0),1.),(3,(7,3,0,0),9.)):
        row=dict(update=update,source_teachers=dict(zip(SOURCES,totals)),CE_loss=loss)
        row.update({k:{} for k in ('source_eos','source_input_tokens','source_body_bytes')},token_digest=str(update),focus_token_digest=str(update))
        rows.append(row)
    result=paired_stages(rows,copy.deepcopy(rows))
    stage=result['exclusive_source_stages']['web']
    assert stage['teachers']==6 and stage['whole']['candidate_CE']==pytest.approx(5/3)
    assert result['mixed_transition_batches']['teachers']==4 and result['total_teachers']==10
    bad=copy.deepcopy(rows);bad[2]['token_digest']='different'
    with pytest.raises(ValueError):paired_stages(rows,bad)
