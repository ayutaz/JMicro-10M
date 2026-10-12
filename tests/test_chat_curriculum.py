import copy

import pytest
from jmicro.chat_curriculum import ACTIVITY_PLACES,BORROWABLE,TASKS,WEIGHTS,render,semantic_check,time_rank


def test_authored_oracle_rejects_wrong_value_and_history_for_every_family():
    for category in WEIGHTS:
        for index in range(24):
            for variant in (0,1,2,3,57):
                record=render(category,index,variant)
                assert semantic_check(record)
                changed=copy.deepcopy(record)
                changed['messages'][-1]['text']='分かりません。'
                assert not semantic_check(changed)
                changed=copy.deepcopy(record)
                changed['grounding']['answer']='wrong'
                assert not semantic_check(changed)
                if category=='correction':
                    assert record['grounding']['previous_value']!=record['grounding']['answer']
                    if record['grounding']['operation'] in ('arrival','deadline'):
                        assert time_rank(record['grounding']['previous_value']) < time_rank(record['grounding']['answer'])
                if record['grounding']['operation']=='speaker_request':
                    assert record['grounding']['state']['item'] in BORROWABLE
                if record['grounding']['operation']=='loan_return':
                    assert record['grounding']['state']['item'] in BORROWABLE
                    assert record['grounding']['state']['item2'] in BORROWABLE
                if category=='negation' and record['grounding']['operation']=='output_rule':
                    assert record['messages'][-1]['text']==record['grounding']['answer']
                operation=record['grounding']['operation'];state=record['grounding']['state']
                if category=='context' and operation=='activity_place':
                    assert state['place'] in ACTIVITY_PLACES[state['act']]
                    assert state['place2'] in ACTIVITY_PLACES[state['act2']]
                    assert state['place']!=state['place2']
                if category=='direct' and operation in ('completed','remaining'):
                    assert state['act'] in TASKS and state['act2'] in TASKS
                if category=='correction' and record['grounding']['mode']==3:
                    assert 'という最初の情報' in record['messages'][-1]['text']
                assert record['target_message_indices']==[len(record['messages'])-1]
                assert [m['role'] for m in record['messages']]==['user' if i%2==0 else 'assistant' for i in range(len(record['messages']))]
    assert sum(WEIGHTS.values())==pytest.approx(1)
