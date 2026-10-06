"""Science source alignment and measured budget; no fictional GPU evidence."""
import copy
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_gated_shared_comparison import matched_sources
from probe_gated_shared_comparison import estimate_training


def test_source_target_budget_and_own32_cost_validation():
    record=dict(additional_supervised_tokens=100000000,additional_input_tokens=100532224,
        source_teachers={'web':75000000,'story':5000000,'ordinary_textbook':10000000,'conditional_textbook':10000000},
        source_eos={},source_input_tokens={},source_body_bytes={},focus_token_digest='focus',token_digest='tokens',sampler={'position':3068})
    assert matched_sources(record,copy.deepcopy(record))
    for key in ('token_digest','focus_token_digest','source_teachers','sampler','additional_supervised_tokens'):
        bad=copy.deepcopy(record);bad[key]='wrong'
        with pytest.raises(ValueError):matched_sources(record,bad)
    r=dict(timing=dict(histories=[dict(seconds=.2 if i<8 else .1) for i in range(32)],
        verification_teacher_tokens=32000*32,terminal_save_seconds=.2))
    evidence,total=estimate_training(r)
    assert evidence['estimated_updates']==3125 and total==pytest.approx((312.5+.8+2.8)*1.3+300)
    r['timing']['histories'].pop()
    with pytest.raises(ValueError):estimate_training(r)
