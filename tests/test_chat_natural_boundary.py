"""Guard new DEV entry points against the prior mixed-file reader failure."""
import builtins
import json
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from chat_natural_contract import read_dev, ref, read_bound
from review_chat_natural_train import additional_issue


def test_mixed_original_file_is_refused_before_any_open(monkeypatch,tmp_path):
    def forbidden(*args,**kwargs):
        raise AssertionError('Protected path was opened')
    monkeypatch.setattr(Path,'open',forbidden)
    with pytest.raises(ValueError,match='dedicated DEV'):
        read_dev(dict(path=str(tmp_path/'eval/chat.jsonl'),sha256='0'*64),tmp_path/'dev_suites')


def test_dev_export_tamper_and_mixed_split_are_refused(tmp_path):
    target=tmp_path/'new.jsonl'
    target.write_text(json.dumps(dict(split='test',messages=[dict(role='user',content='sentinel')]))+'\n')
    with pytest.raises(ValueError,match='protected split'):
        read_dev(ref(target),tmp_path)
    value=ref(target)
    target.write_text('{}\n')
    with pytest.raises(ValueError,match='Frozen artifact differs'):
        read_dev(value,tmp_path)


def test_anonymized_identity_in_earlier_context_is_excluded():
    messages=[dict(role='user',text='こんにちは'),dict(role='assistant',text='<AB>さん、こんにちは'),
              dict(role='user',text='お元気ですか'),dict(role='assistant',text='元気です。')]
    assert additional_issue(messages,3)=='anonymized_identity_marker_in_context'
    messages[1]['text']='こんにちは。'
    assert additional_issue(messages,3) is None


def test_bound_json_string_path_uses_typed_reader_and_preserves_hash_check(tmp_path):
    target=tmp_path/'receipt.json'
    target.write_text('{"status":"complete"}')
    value=ref(target)
    assert isinstance(value['path'],str)
    assert read_bound(value)=={'status':'complete'}
    target.write_text('{}')
    with pytest.raises(ValueError,match='Frozen artifact differs'):
        read_bound(value)
