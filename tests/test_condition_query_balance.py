import hashlib
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from condition_query_balance import shorter_query


def test_changed_query_selects_shorter_without_changing_relation_facts():
    r = dict(id='train-1-0', split='train', category='comparison', family='train-1', template_id='comparison-0',
             facts=dict(A='さくら', B='あおい'), local_state=dict(A_length=5, B_length=3, longer='さくら'),
             prefix='さくらの棒はあおいの棒より長い。長い方の棒を持っているのは、',
             outcome='さくらである。', choices=['さくらである。', 'あおいである。'], label=0)
    result = shorter_query(r)
    assert result['outcome'] == 'あおいである。' and result['label'] == 1
    assert result['prefix'].startswith('さくらの棒はあおいの棒より長い。')
    assert result['facts'] == r['facts'] and result['local_state'] == r['local_state']
    assert result['text_sha256'] == hashlib.sha256(result['text'].encode()).hexdigest()
    assert r['label'] == 0
    reversed_row = {**r, 'label': 1, 'outcome': 'あおいである。',
                    'local_state': dict(A_length=3, B_length=5, longer='あおい')}
    assert shorter_query(reversed_row)['outcome'] == 'さくらである。'


def test_heldout_and_incorrect_ground_truth_are_not_silently_rewritten():
    r = dict(split='dev', category='comparison', template_id='comparison-4')
    with pytest.raises(ValueError):
        shorter_query(r)
    r = dict(split='train', category='comparison', template_id='comparison-0', facts=dict(A='A', B='B'),
             local_state=dict(A_length=1, B_length=2), outcome='Aである。', choices=['Aである。', 'Bである。'],
             label=0, prefix='長い方の棒を持っているのは、')
    with pytest.raises(ValueError):
        shorter_query(r)
