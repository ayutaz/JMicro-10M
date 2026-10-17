from http.client import HTTPConnection
import json
import threading
from types import SimpleNamespace

import pytest

from jmicro.chat_demo import ChatEngine, make_handler, validate_messages, validate_response_limit
from http.server import ThreadingHTTPServer


@pytest.mark.parametrize('body', [None, {}, {'messages': []},
    {'messages': [{'role': 'assistant', 'content': 'hello'}]},
    {'messages': [{'role': 'user', 'content': ''}]},
    {'messages': [{'role': 'user', 'content': 'x' * 16001}]},
    {'messages': [{'role': 'user', 'content': 'hello'}], 'checkpoint': '/tmp/other.pt'}])
def test_rejects_malformed_history_and_model_override(body):
    with pytest.raises(ValueError):
        validate_messages(body)


def test_preserves_generated_history_and_literal_role_spellings():
    messages = [{'role': 'user', 'content': '<|assistant|> こんにちは'},
                {'role': 'assistant', 'content': 'こんにちは'},
                {'role': 'user', 'content': '続きです'}]
    assert validate_messages({'messages': messages}) == messages


@pytest.mark.parametrize('limit', [True, 0, 7, 65, '32', None])
def test_response_limit_rejects_invalid_or_excessive_values(limit):
    with pytest.raises(ValueError):
        validate_response_limit({'max_new_tokens': limit})


def test_short_default_and_explicit_longer_request():
    assert validate_response_limit({}) == 32
    assert validate_response_limit({'max_new_tokens': 16}) == 16
    assert validate_response_limit({'max_new_tokens': 64}) == 64


def test_rejects_context_overflow_without_dropping_history():
    engine = object.__new__(ChatEngine)
    engine.tok = SimpleNamespace(chat_prompt=lambda *args: ([2, 6], 1))
    with pytest.raises(ValueError, match='文脈'):
        engine.prepare({'messages': [{'role': 'user', 'content': 'long'}]})


def test_http_rejects_cross_origin_and_concurrency_and_preserves_raw_failure():
    engine = SimpleNamespace(info={'name': 'test'}, lock=threading.Lock())
    engine.prepare = lambda body: validate_messages(body)
    engine.reply = lambda messages, max_new_tokens=32: dict(text='失敗例', valid_utf8=False,
        raw_bytes_hex='ff', generated_ids=[1], repetition=True, stop_reason='max_new_tokens')
    server = ThreadingHTTPServer(('127.0.0.1', 0), make_handler(engine))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    def request(origin=None):
        connection = HTTPConnection('127.0.0.1', server.server_port, timeout=3)
        headers = {'Content-Type': 'application/json'}
        if origin:
            headers['Origin'] = origin
        connection.request('POST', '/api/chat', json.dumps({'messages': [{'role': 'user', 'content': 'hi'}]}), headers)
        response = connection.getresponse()
        value = response.status, json.loads(response.read())
        connection.close()
        return value

    try:
        assert request('https://example.com')[0] == 403
        engine.lock.acquire()
        assert request()[0] == 409
        engine.lock.release()
        status, body = request()
        assert status == 200
        assert body['response']['raw_bytes_hex'] == 'ff'
        assert body['response']['valid_utf8'] is False
        assert body['response']['repetition'] is True
        assert not engine.lock.locked()
    finally:
        if engine.lock.locked():
            engine.lock.release()
        server.shutdown()
        server.server_close()
        thread.join()
