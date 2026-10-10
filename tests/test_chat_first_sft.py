"""Complete three-pass budgets and diagnostic/adoption separation."""
import sys
from pathlib import Path
import pytest
from jmicro.experiment import ROOT, read_json
from jmicro.tokenizer import Tokenizer
from jmicro.chat_training import AssistantBudgetSampler
sys.path.insert(0,str(ROOT/'scripts'))
from prepare_chat_first_config import prepare
from run_chat_first_sft import preflight
from require_adopted_base import require_adopted_base


def test_three_complete_passes_keep_eot_even_with_partial_last_batch():
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    records=[dict(doc_id='a',split='train',messages=[dict(role='user',content='こんにちは。'),dict(role='assistant',content='こんにちは。'),
        dict(role='user',content='猫は好きですか？'),dict(role='assistant',content='猫は好きです。')]),
        dict(doc_id='b',split='train',messages=[dict(role='user',content='今日は晴れですね。'),dict(role='assistant',content='散歩にちょうどよい天気ですね。')])]
    probe=AssistantBudgetSampler(records,tok,128,42,10**6)
    one_series=sum(len(w['ids']) for w in probe.windows)
    one_teachers=sum(int((w['labels']!=-100).sum()) for w in probe.windows)
    sampler=AssistantBudgetSampler(records,tok,128,42,3*one_series)
    while sampler.series_tokens<sampler.series_budget:
        x,y,_=sampler.batch(4)
        assert x.shape==y.shape==(4,128)
        for row in y:
            targets=row[row!=-100]
            if len(targets): assert int(targets[-1])==7
    assert sampler.examples==sampler.eot_teachers==9
    assert sampler.teacher_tokens==3*one_teachers and sampler.series_tokens==3*one_series
    assert sampler.physical_tokens==12*128
    saved=sampler.state_dict();restored=AssistantBudgetSampler(records,tok,128,42,3*one_series);restored.load_state_dict(saved)
    assert restored.state_dict()==saved
    with pytest.raises(ValueError,match='exhausted'): restored.batch(4)
    with pytest.raises(ValueError,match='Only train'): AssistantBudgetSampler([dict(records[0],split='dev')],tok,128,42,1000)


def test_frozen_real_diagnostic_does_not_certify_adoption():
    path=ROOT/'configs/phase7/chat_first_probe.json'
    if not path.exists(): pytest.skip('real-parent preparation not yet performed')
    c,tok,records=preflight(path,require_batch=False)
    assert len(records)==2688 and c['Base_adopted'] is c['Chat_adopted'] is False
    with pytest.raises((AssertionError,KeyError,ValueError)):
        require_adopted_base(c)
