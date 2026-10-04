from http.client import HTTPConnection
import json
import threading
from types import SimpleNamespace

import pytest

from jmicro.webui import Engine, ThreadingHTTPServer, make_handler, validate_request


@pytest.mark.parametrize("change", [{"max_new_tokens": True}, {"max_new_tokens": 513},
    {"temperature": float("nan")}, {"top_p": 0}, {"seed": -1}, {"mode": "chat"}, {"prompt": " "}])
def test_invalid_generation_settings(change):
    with pytest.raises(ValueError):
        validate_request({"prompt": "書き出し", **change})


def test_context_overflow_is_rejected_without_truncating_input():
    engine = object.__new__(Engine)
    engine.tok = SimpleNamespace(encode=lambda text: [8] * 1000)
    engine.info = {"context": 1024}
    with pytest.raises(ValueError, match="文脈上限"):
        engine.prepare({"prompt": "long", "max_new_tokens": 64})


@pytest.fixture
def http_ui():
    engine = SimpleNamespace(info={"name": "test"}, lock=threading.Lock())
    engine.prepare = lambda body: (validate_request(body), [2, 8])
    def stream(request, ids):
        yield {"type": "start"}
        yield {"type": "done", "text": "日本語"}
    engine.stream = stream
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(engine))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield server, engine
    server.shutdown()
    server.server_close()
    thread.join()


def fetch(server, path="/api/generate", *, origin=None, host=None, payload=None):
    client = HTTPConnection("127.0.0.1", server.server_port, timeout=3)
    headers = {"Content-Type": "application/json"}
    if origin is not None:
        headers["Origin"] = origin
    if host is not None:
        headers["Host"] = host
    client.request("POST", path, json.dumps(payload or {"prompt": "始まり"}), headers)
    response = client.getresponse()
    status, content = response.status, response.read()
    client.close()
    return status, content


def test_only_local_origin_and_host_are_accepted(http_ui):
    server, _ = http_ui
    assert fetch(server, origin="https://example.com")[0] == 403
    assert fetch(server, host=f"example.com:{server.server_port}")[0] == 403
    assert fetch(server, origin=f"http://127.0.0.1:{server.server_port}")[0] == 200


def test_concurrent_request_rejected_and_stream_lock_released(http_ui):
    server, engine = http_ui
    engine.lock.acquire()
    try:
        assert fetch(server)[0] == 409
    finally:
        engine.lock.release()
    status, content = fetch(server)
    assert status == 200
    assert [row["type"] for row in map(json.loads, content.splitlines())] == ["start", "done"]
    assert not engine.lock.locked()


def test_invalid_input_does_not_enter_inference(http_ui):
    server, engine = http_ui
    assert fetch(server, payload={"prompt": "start", "max_new_tokens": 0})[0] == 400
    assert not engine.lock.locked()
    assert fetch(server, path="/api/other")[0] == 404
