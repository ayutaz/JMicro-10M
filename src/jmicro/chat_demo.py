"""Local CPU access to the existing, explicitly unadopted first SFT model.

This inference adapter never calls training preflight or opens corpus/TEST files.
The original scientific recipes, checkpoints and Base UI remain unchanged.
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import hashlib
import json
import os
from pathlib import Path
import threading
import time
from urllib.parse import urlsplit

import torch
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.chat_evaluation import generate_reply
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer

CHECKPOINT_SHA = '1c79692f71efacecf5444a6be250518a4603248ee2b2811b531e566f2cfc2f24'
TOKENIZER_SHA = 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'
PARENT_SHA = '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
MODEL_SHA = '298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83'
MODEL_LF_SHA = '2861baaf1860174fc8f7ae5da23386ae39146b8a907077bce4958a4b6b315b3a'
TRAIN_RESULT = ROOT / 'reports/phase7/chat-first-sft-20261010/result.json'
ASSETS = ROOT / 'webui/chat'


def validate_response_limit(data):
    limit = data.get('max_new_tokens', 32)
    if type(limit) is not int or not 8 <= limit <= 64:
        raise ValueError('返答の上限は8〜64トークンで指定してください。')
    return limit


def validate_messages(data):
    if not isinstance(data, dict) or 'messages' not in data or set(data) - {'messages', 'max_new_tokens'}:
        raise ValueError('messagesを指定してください。')
    validate_response_limit(data)
    messages = data['messages']
    if not isinstance(messages, list) or not 1 <= len(messages) <= 65 or len(messages) % 2 != 1:
        raise ValueError('会話履歴はUserから交互に並べ、最後をUserにしてください。')
    result = []
    total_bytes = 0
    for index, message in enumerate(messages):
        if not isinstance(message, dict) or set(message) != {'role', 'content'}:
            raise ValueError('会話履歴の形式が不正です。')
        expected = 'user' if index % 2 == 0 else 'assistant'
        if message['role'] != expected or not isinstance(message['content'], str):
            raise ValueError('会話履歴の役割が不正です。')
        if expected == 'user' and not message['content'].strip():
            raise ValueError('メッセージを入力してください。')
        total_bytes += len(message['content'].encode('utf-8'))
        result.append(dict(message))
    if total_bytes > 16000:
        raise ValueError('会話が長くなりました。「新しい会話」で始め直してください。')
    return result


class ChatEngine:
    def __init__(self):
        if torch.cuda.is_available():
            raise RuntimeError('Launch this CPU demo with CUDA_VISIBLE_DEVICES empty.')
        torch.set_num_threads(2)
        result = read_json(TRAIN_RESULT)
        ref = result['checkpoints']['epoch3']
        checkpoint = Path(ref['path'])
        config = read_json(ROOT / 'configs/phase7/chat_first_sft.json')
        tokenizer = Path(config['tokenizer']['path'])
        if (ref['sha256'] != CHECKPOINT_SHA or sha256(checkpoint) != CHECKPOINT_SHA or
                sha256(tokenizer) != TOKENIZER_SHA or
                result['config_sha256'] != sha256(ROOT / 'configs/phase7/chat_first_sft.json')):
            raise ValueError('Saved SFT checkpoint/config/tokenizer identity differs.')
        model_source = ROOT / 'src/jmicro/model.py'
        normalized = hashlib.sha256(model_source.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
        if sha256(model_source) != MODEL_SHA or normalized != MODEL_LF_SHA:
            raise ValueError('Native model source differs from the fixed inference implementation.')
        state = torch.load(checkpoint, map_location='cpu', weights_only=False)
        if (state['implementation_sha256']['src/jmicro/model.py'] != MODEL_LF_SHA or
                state['lineage']['base_checkpoint']['sha256'] != PARENT_SHA or
                state['lineage']['kind'] != 'assistant-sft-fresh-optimizer' or
                state['update'] != 3785 or state['supervised_tokens'] != 1899555 or
                state['sampler']['examples'] != 121098):
            raise ValueError('Checkpoint is not the completed first SFT model.')
        self.tok = Tokenizer(tokenizer)
        self.model = JMicroModel(state['model_config'])
        self.model.load_state_dict(state['model'], strict=True)
        self.model.eval().requires_grad_(False)
        if sum(p.numel() for p in self.model.parameters()) != 10001152:
            raise ValueError('Unexpected parameter count.')
        if not all(bool(torch.isfinite(p).all()) for p in self.model.parameters()):
            raise ValueError('Nonfinite model weights.')
        self.lock = threading.Lock()
        self.stopping = threading.Event()
        self.info = dict(name='JMicro-10M Chat', kind='Chat / RealPersonaChat SFT 3周',
                         checkpoint=str(checkpoint), checkpoint_sha256=CHECKPOINT_SHA,
                         tokenizer_sha256=TOKENIZER_SHA, parent_sha256=PARENT_SHA,
                         parameters=10001152, SFT_teacher_tokens=1899555, SFT_epochs=3,
                         device='CPU', precision='FP32 / math attention', decoding='greedy',
                         context=1024, max_new_tokens=32, max_new_tokens_range=[8, 64], Base_adopted=False, Chat_adopted=False,
                         original_model_source_sha256=MODEL_SHA,
                         checkpoint_model_source_LF_sha256=MODEL_LF_SHA,
                         model_source_difference='CRLF versus LF only; original files unchanged')
        del state

    def prepare(self, data):
        messages = validate_messages(data)
        _, removed = self.tok.chat_prompt(messages, 1024 - validate_response_limit(data))
        if removed:
            raise ValueError('文脈の上限に達しました。「新しい会話」で始め直してください。')
        return messages

    def reply(self, messages, max_new_tokens=32):
        validate_response_limit(dict(max_new_tokens=max_new_tokens))
        started = time.monotonic()

        def check():
            if self.stopping.is_set():
                raise InterruptedError('Server stopping')
            if time.monotonic() - started > 60:
                raise TimeoutError('生成が60秒を超えました。')

        with sdpa_kernel(SDPBackend.MATH):
            row = generate_reply(self.model, self.tok, messages, 'cpu', 'fp32', max_new_tokens, True, check)
        if row['removed_turns']:
            raise RuntimeError('Unexpected history truncation')
        return dict(**row, seconds=time.monotonic() - started)


def make_handler(engine):
    class Handler(BaseHTTPRequestHandler):
        def local(self):
            authority = self.headers.get('Host', '')
            try:
                parsed = urlsplit('http://' + authority)
                return (parsed.hostname in ('127.0.0.1', 'localhost', '::1') and
                        (parsed.port or 80) == self.server.server_port and
                        self.headers.get('Origin', 'http://' + authority) == 'http://' + authority)
            except ValueError:
                return False

        def respond(self, status, body, mime='application/json; charset=utf-8'):
            if not isinstance(body, bytes):
                body = json.dumps(body, ensure_ascii=False, allow_nan=False).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', mime)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; frame-ancestors 'none'; base-uri 'none'")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if not self.local():
                return self.respond(403, dict(error='ローカルからアクセスしてください。'))
            if self.path == '/api/model':
                return self.respond(200, dict(**engine.info, busy=engine.lock.locked()))
            files = {'/': ('index.html', 'text/html; charset=utf-8'),
                     '/app.js': ('app.js', 'text/javascript; charset=utf-8'),
                     '/style.css': ('style.css', 'text/css; charset=utf-8')}
            if self.path not in files:
                return self.respond(404, dict(error='Not found'))
            name, mime = files[self.path]
            self.respond(200, (ASSETS / name).read_bytes(), mime)

        def do_POST(self):
            if not self.local():
                return self.respond(403, dict(error='ローカルからアクセスしてください。'))
            if self.path != '/api/chat':
                return self.respond(404, dict(error='Not found'))
            try:
                if self.headers.get_content_type() != 'application/json':
                    raise ValueError('JSON形式で送信してください。')
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 70000:
                    raise ValueError('入力サイズが不正です。')
                self.connection.settimeout(10)
                data = json.loads(self.rfile.read(length))
                messages = engine.prepare(data)
                max_new_tokens = validate_response_limit(data)
            except (ValueError, UnicodeError, TimeoutError) as error:
                return self.respond(400, dict(error=str(error)))
            if not engine.lock.acquire(blocking=False):
                return self.respond(409, dict(error='応答を生成中です。少し待ってください。'))
            try:
                response = engine.reply(messages, max_new_tokens=max_new_tokens)
                self.respond(200, dict(response=response, model=engine.info['name']))
            except (TimeoutError, ValueError) as error:
                self.respond(400, dict(error=str(error)))
            except Exception:
                self.respond(500, dict(error='生成に失敗しました。サーバーログを確認してください。'))
                raise
            finally:
                engine.lock.release()

        def log_message(self, format, *args):
            # HTTP metadata only; user messages are not saved by this server.
            super().log_message(format, *args)

    return Handler


def process_identity():
    raw = Path('/proc/self/stat').read_text()
    return dict(pid=os.getpid(), boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
                start_ticks=raw[raw.rfind(')') + 2:].split()[19])


def serve(port=7861):
    from jmicro.training import atomic_json
    import signal

    record = ROOT / 'reports/local/chat-webui/server.json'
    engine = ChatEngine()
    server = ThreadingHTTPServer(('127.0.0.1', port), make_handler(engine))
    server.daemon_threads = True
    identity = process_identity()
    info = dict(status='running', started_at=now(), **identity, **engine.info,
                url=f'http://127.0.0.1:{port}', training_launched=False, GPU_initialized=False)

    def stop(*_):
        engine.stopping.set()
        threading.Thread(target=server.shutdown, daemon=True).start()

    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    atomic_json(record, info)
    print(json.dumps(info, ensure_ascii=False), flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()
        atomic_json(record, dict(**{k: v for k, v in info.items() if k != 'status'}, status='stopped', stopped_at=now()))
