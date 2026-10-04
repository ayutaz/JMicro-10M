"""Loopback-only, streaming Base completion UI for the verified 10B checkpoint."""
from contextlib import nullcontext
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import argparse
import json
import logging
import math
import os
from pathlib import Path
import signal
import threading
import time
from urllib.parse import urlsplit

import torch
from torch.nn.attention import SDPBackend, sdpa_kernel

from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.text_display import decode_display
from jmicro.tokenizer import SUPPRESS_IDS, Tokenizer
from jmicro.training import gpu_lock

ASSETS = ROOT / "webui"
PLAN = ROOT / "configs/phase6/base_10b_comparison.json"


def validate_request(data):
    if not isinstance(data, dict):
        raise ValueError("入力はJSON objectで指定してください。")
    prompt = data.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("文章を入力してください。")
    if len(prompt.encode("utf-8")) > 16000:
        raise ValueError("入力が長すぎます。")
    result = {"prompt": prompt}
    for key, default, lower, upper in (("max_new_tokens", 128, 1, 512), ("seed", 42, 0, 2147483647)):
        value = data.get(key, default)
        if type(value) is not int or not lower <= value <= upper:
            raise ValueError(f"{key}は{lower}〜{upper}の整数にしてください。")
        result[key] = value
    for key, default, lower, upper in (("temperature", .8, .05, 2.), ("top_p", .9, .01, 1.)):
        value = data.get(key, default)
        if type(value) not in (int, float) or not math.isfinite(value) or not lower <= value <= upper:
            raise ValueError(f"{key}は{lower}〜{upper}にしてください。")
        result[key] = float(value)
    mode = data.get("mode", "sampling")
    if mode not in ("sampling", "greedy"):
        raise ValueError("生成方法が不正です。")
    result["mode"] = mode
    return result


class Engine:
    def __init__(self, plan_path=PLAN, device="cuda"):
        plan = read_json(plan_path)
        checkpoint = Path(plan["checkpoint"])
        tokenizer = ROOT / plan["tokenizer"]
        if sha256(checkpoint) != plan["checkpoint_sha256"] or sha256(tokenizer) != plan["tokenizer_sha256"]:
            raise ValueError("Checkpoint/tokenizer checksum differs from accepted evaluation")
        if device == "cuda" and (not torch.cuda.is_available() or not torch.cuda.is_bf16_supported()):
            raise RuntimeError("CUDA/BF16 is unavailable; restore the documented WSL environment")
        saved = torch.load(checkpoint, map_location="cpu", weights_only=False)
        if saved["tokens"] != plan["checkpoint_tokens"] or saved["update"] != plan["checkpoint_update"]:
            raise ValueError("Checkpoint training counters differ")
        self.tok = Tokenizer(tokenizer)
        if saved["model_config"]["vocab_size"] != self.tok.vocab_size:
            raise ValueError("Checkpoint/tokenizer vocabulary differs")
        self.model = JMicroModel(saved["model_config"])
        self.model.load_state_dict(saved["model"], strict=True)
        self.model.to(device).eval().requires_grad_(False)
        self.device = device
        self.lock = threading.Lock()
        self.stopping = threading.Event()
        self.info = {"name": "JMicro-10M", "kind": "Base / 文章の続き",
                     "parameters": sum(p.numel() for p in self.model.parameters()),
                     "training_tokens": saved["tokens"], "update": saved["update"],
                     "checkpoint": str(checkpoint), "checkpoint_sha256": plan["checkpoint_sha256"],
                     "tokenizer_sha256": plan["tokenizer_sha256"],
                     "device": torch.cuda.get_device_name() if device == "cuda" else "CPU",
                     "precision": "BF16 / math attention" if device == "cuda" else "FP32 / math attention",
                     "context": self.model.config["max_position_embeddings"]}
        del saved

    def prepare(self, data):
        request = validate_request(data)
        ids = [2, *self.tok.encode(request["prompt"])]
        if len(ids) + request["max_new_tokens"] > self.info["context"]:
            raise ValueError(f"入力{len(ids)}＋生成{request['max_new_tokens']} tokensが文脈上限{self.info['context']}を超えます。入力か生成量を減らしてください。")
        return request, ids

    def stream(self, request, input_ids):
        started = time.monotonic()
        generated, cache, reason = [], None, "max_new_tokens"
        generator = torch.Generator(device=self.device).manual_seed(request["seed"])
        current = torch.tensor([input_ids], device=self.device)
        yield {"type": "start", "input_tokens": len(input_ids)}
        with torch.inference_mode(), sdpa_kernel(SDPBackend.MATH):
            for _ in range(request["max_new_tokens"]):
                if self.stopping.is_set() or time.monotonic() - started > 60:
                    reason = "server_stopping" if self.stopping.is_set() else "time_limit"
                    break
                precision = torch.autocast("cuda", dtype=torch.bfloat16) if self.device == "cuda" else nullcontext()
                with precision:
                    output = self.model(current, cache=cache, use_cache=True)
                cache = output.cache
                scores = output.logits[0, -1].clone()
                if not bool(torch.isfinite(scores).all()):
                    raise RuntimeError("Non-finite inference logits")
                scores[list(SUPPRESS_IDS)] = -torch.inf
                if request["mode"] == "greedy":
                    token = int(scores.argmax())
                else:
                    ordered, indexes = (scores / request["temperature"]).sort(descending=True)
                    probabilities = ordered.softmax(-1)
                    probabilities[probabilities.cumsum(-1) - probabilities >= request["top_p"]] = 0
                    token = int(indexes[torch.multinomial(probabilities, 1, generator=generator)])
                generated.append(token)
                if token == 3:
                    reason = "stop_id"
                    break
                # The existing display helper withholds only an incomplete UTF8 tail.
                display = decode_display(self.tok.decode_bytes(generated), "max_new_tokens")
                yield {"type": "token", "text": display["text"], "generated_tokens": len(generated)}
                current = torch.tensor([[token]], device=self.device)
        raw = self.tok.decode_bytes(generated)
        elapsed = time.monotonic() - started
        yield {"type": "done", **decode_display(raw, reason), "stop_reason": reason,
               "generated_ids": generated, "generated_body_bytes_hex": raw.hex(),
               "input_tokens": len(input_ids), "generated_tokens": len(generated),
               "seconds": elapsed, "tokens_per_second": len(generated) / max(elapsed, 1e-9),
               "settings": {k: v for k, v in request.items() if k != "prompt"}}


def make_handler(engine):
    class Handler(BaseHTTPRequestHandler):
        def local_request(self):
            authority = self.headers.get("Host", "")
            try:
                host = urlsplit("http://" + authority).hostname
                expected_port = self.server.server_port
                port = urlsplit("http://" + authority).port or 80
                if host not in ("127.0.0.1", "localhost", "::1") or port != expected_port:
                    return False
                origin = self.headers.get("Origin")
                return origin is None or origin == "http://" + authority
            except ValueError:
                return False

        def headers_for(self, status, mime, size=None):
            self.send_response(status)
            self.send_header("Content-Type", mime)
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
            if size is not None:
                self.send_header("Content-Length", str(size))
            self.end_headers()

        def send_json(self, status, obj):
            body = json.dumps(obj, ensure_ascii=False, allow_nan=False).encode("utf-8")
            self.headers_for(status, "application/json; charset=utf-8", len(body))
            self.wfile.write(body)

        def do_GET(self):
            if not self.local_request():
                self.send_json(403, {"error": "ローカルからアクセスしてください。"})
                return
            if self.path == "/api/model":
                self.send_json(200, {**engine.info, "busy": engine.lock.locked()})
                return
            files = {"/": ("index.html", "text/html; charset=utf-8"),
                     "/app.js": ("app.js", "text/javascript; charset=utf-8"),
                     "/style.css": ("style.css", "text/css; charset=utf-8")}
            if self.path not in files:
                self.send_json(404, {"error": "Not found"})
                return
            name, mime = files[self.path]
            body = (ASSETS / name).read_bytes()
            self.headers_for(200, mime, len(body))
            self.wfile.write(body)

        def do_POST(self):
            self.connection.settimeout(15)
            if not self.local_request():
                self.send_json(403, {"error": "ローカルからアクセスしてください。"})
                return
            if self.path != "/api/generate":
                self.send_json(404, {"error": "Not found"})
                return
            if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
                self.send_json(415, {"error": "application/jsonが必要です。"})
                return
            try:
                size = int(self.headers.get("Content-Length", "0"))
                if not 0 < size <= 32768:
                    raise ValueError("入力サイズが不正です。")
                request, ids = engine.prepare(json.loads(self.rfile.read(size)))
            except (ValueError, UnicodeError, TimeoutError) as exc:
                self.send_json(400, {"error": str(exc)})
                return
            if not engine.lock.acquire(blocking=False):
                self.send_json(409, {"error": "生成中です。完了または停止後に再実行してください。"})
                return
            stream = engine.stream(request, ids)
            try:
                self.headers_for(200, "application/x-ndjson; charset=utf-8")
                for event in stream:
                    self.wfile.write((json.dumps(event, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8"))
                    self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError, TimeoutError):
                logging.info("Generation disconnected; released inference request")
            except Exception:
                logging.exception("Inference failed")
                try:
                    self.wfile.write(b'{"type":"error","error":"Inference failed; see server log"}\n')
                    self.wfile.flush()
                except OSError:
                    pass
            finally:
                try:
                    stream.close()
                finally:
                    engine.lock.release()

        def log_message(self, fmt, *args):
            # Do not persist prompts or generated text.
            logging.info(fmt, *args)

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument("--device", choices=("cuda", "cpu"), default="cuda")
    parser.add_argument("--run-dir", type=Path, default=ROOT / "reports/local/webui")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    torch.set_num_threads(2)
    torch.backends.cuda.matmul.allow_tf32 = False
    args.run_dir.mkdir(parents=True, exist_ok=True)
    record = {"status": "loading", "pid": os.getpid(), "started_at": now(),
              "url": f"http://127.0.0.1:{args.port}", "additional_training_tokens": 0}
    if Path("/proc/self/stat").exists():
        record.update(boot_id=Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
                      start_ticks=Path("/proc/self/stat").read_text().split()[21])
    record_path = args.run_dir / "server.json"
    owns_record = False
    try:
        with gpu_lock(args.device):
            owns_record = True
            write_json(record_path, record)
            engine = Engine(device=args.device)
            server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(engine))
            def stop(signum, frame):
                engine.stopping.set()
                threading.Thread(target=server.shutdown, daemon=True).start()
            signal.signal(signal.SIGTERM, stop)
            signal.signal(signal.SIGINT, stop)
            record.update(status="running", model=engine.info, ready_at=now())
            write_json(record_path, record)
            logging.info("Ready: %s — %s", record["url"], engine.info["device"])
            try:
                server.serve_forever(poll_interval=.25)
            finally:
                engine.stopping.set()
                server.server_close()
    except Exception as exc:
        if owns_record:
            record.update(status="failed", error=str(exc), ended_at=now())
            write_json(record_path, record)
        raise
    record.update(status="stopped", ended_at=now())
    write_json(record_path, record)
