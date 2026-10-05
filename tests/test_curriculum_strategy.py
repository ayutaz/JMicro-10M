import pytest
from jmicro.curriculum_strategy import select,family_split


def test_literal_complete_quote_and_condition_are_not_globally_excluded():
    text='雨が降った場合は、窓を閉めます。窓を閉めれば、部屋に雨が入らなくなります。'
    assert select(text,110,'web')['group']=='general'
    quote='母は「窓を閉めて」と言いました。私は窓を閉めて、部屋に雨が入らないようにしました。'
    assert select(quote,70,'story')['group']=='short'
    assert select('写真を見ると分かります。ここには写真の説明があります。',110,'web') is None
    assert select('雨が降った場合は、窓を閉めます。途中で文章が',110,'web') is None


def test_family_split_is_stable_and_has_both_partitions():
    results=[family_split('story:'+str(i)) for i in range(200)]
    assert set(results)=={'train','dev'}
    assert results==[family_split('story:'+str(i)) for i in range(200)]


def test_strategy_warmup_uses_completed_local_updates(monkeypatch):
    from types import SimpleNamespace
    from jmicro.curriculum_strategy import StrategyTrainer
    from jmicro.natural_learning import NaturalTrainer
    monkeypatch.setattr(NaturalTrainer,'_set_token_lr',lambda self:.002)
    trainer=SimpleNamespace(pilot_binding=dict(warmup_updates=200),update=15,lineage=dict(parent_update=15),
        optimizer=SimpleNamespace(param_groups=[dict(lr=.002)]),scheduler=SimpleNamespace(_last_lr=[]))
    # Construct an actual StrategyTrainer instance without invoking CUDA/setup.
    instance=object.__new__(StrategyTrainer);instance.__dict__.update(trainer.__dict__)
    assert instance._set_token_lr()==pytest.approx(.002/200)
    instance.update=214
    assert instance._set_token_lr()==pytest.approx(.002)
    assert instance.scheduler._last_lr==[.002]
