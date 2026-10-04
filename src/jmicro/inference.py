"""Greedy inference with the same external body codec for torch, HF and GGUF."""
from pathlib import Path
import argparse
import json
import subprocess
import tempfile

import torch

from jmicro.experiment import ROOT, read_json, write_json, sha256
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer, SUPPRESS_IDS
from jmicro.text_display import decode_display


def native(model: Path, request: dict, work: Path, bridge: Path | None = None) -> dict:
    import gguf
    reader = gguf.GGUFReader(model)
    precision = reader.fields.get('jmicro.inference_precision')
    profile = precision.contents() if precision else None
    del reader
    if profile:
        from jmicro.inference_precision import PROFILE
        from jmicro.native_precision import validate_stable_runtime
        if profile != PROFILE:
            raise ValueError('Unknown GGUF inference precision profile')
        bridge = bridge or ROOT/'artifacts/runtime-stable-f32-v2/llama-bridge'
        validate_stable_runtime(bridge.resolve().parent)
    work.mkdir(parents=True, exist_ok=True)
    write_json(work / "request.json", request)
    bridge = bridge or ROOT / "artifacts/runtime/llama-bridge"
    with (work / "native.log").open("w") as log:
        subprocess.run([str(bridge.resolve()), str(model.resolve()), str((work / "request.json").resolve()),
                        str((work / "response.json").resolve())], check=True, stdout=log, stderr=log)
    return read_json(work / "response.json")


def greedy(input_ids, step, max_new_tokens, stop_ids, forced_first_id=None):
    """Backend-independent controller. The forced ID is an explicit test hook."""
    cache, generated = None, []
    current = torch.tensor([input_ids], dtype=torch.long)
    for index in range(max_new_tokens):
        logits, cache = step(current, cache)
        scores = logits[0, -1].clone()
        scores[list(SUPPRESS_IDS)] = -torch.inf
        next_id = forced_first_id if index == 0 and forced_first_id is not None else int(scores.argmax())
        generated.append(next_id)
        if next_id in stop_ids:
            return generated, "stop_id"
        current = torch.tensor([[next_id]], dtype=torch.long)
    return generated, "max_new_tokens"


def generate(backend, artifact: Path, tok: Tokenizer, input_ids, max_new_tokens=16,
             chat=True, work=None, forced_first_id=None, bridge=None):
    if backend == "gguf":
        import gguf
        reader = gguf.GGUFReader(artifact)
        tokenizer_hash = reader.fields["jmicro.tokenizer_sha256"].contents()
        vocab_size = len(reader.fields["tokenizer.ggml.tokens"].contents())
        if vocab_size != tok.vocab_size:
            raise ValueError("Tokenizer vocabulary differs from GGUF")
        del reader
    else:
        manifest = read_json(artifact / "artifact_manifest.json")
        tokenizer_hash = manifest["tokenizer_sha256"]
        if manifest["weights_sha256"] != sha256(artifact / "model.safetensors"):
            raise ValueError("Model weights checksum differs")
    if tokenizer_hash != sha256(tok.path):
        raise ValueError("Tokenizer artifact checksum differs from model contract")
    if tok.vocab_size != (read_json(artifact / ("jmicro_config.json" if backend == "torch" else "config.json"))["vocab_size"] if backend != "gguf" else tok.vocab_size):
        raise ValueError("Tokenizer vocabulary differs from model")
    if not input_ids or max_new_tokens < 1 or len(input_ids) + max_new_tokens > 1024:
        raise ValueError("Prompt + generation must fit 1024 tokens")
    if any(i < 0 or i >= tok.vocab_size for i in input_ids):
        raise ValueError("Input ID outside vocabulary")
    stop_ids = [7, 3] if chat else [3]
    torch.set_num_threads(2)
    if backend == "gguf":
        request = {"generate": {"input_ids": input_ids, "max_new_tokens": max_new_tokens,
                                "stop_ids": stop_ids, "suppress_ids": list(SUPPRESS_IDS)}}
        if forced_first_id is not None:
            request["generate"]["forced_first_id"] = forced_first_id
        if work is None:
            with tempfile.TemporaryDirectory(prefix="jmicro-native-") as directory:
                response = native(artifact, request, Path(directory), bridge)
        else:
            response = native(artifact, request, work, bridge)
        if response["vocab_size"] != tok.vocab_size:
            raise ValueError("Tokenizer vocabulary differs from GGUF")
        ids, reason = response["generation"]["ids"], response["generation"]["stop_reason"]
    else:
        if backend == "torch":
            model = JMicroModel.load(artifact).eval()
            def step(current, cache):
                out = model(current, cache=cache, use_cache=True)
                return out.logits, out.cache
        elif backend == "hf":
            from transformers import AutoModelForCausalLM
            model = AutoModelForCausalLM.from_pretrained(artifact, local_files_only=True, attn_implementation="eager").eval()
            def step(current, cache):
                out = model(current, past_key_values=cache, use_cache=True)
                return out.logits, out.past_key_values
        else:
            raise ValueError("Unknown backend")
        precision = manifest.get('inference_precision')
        if precision:
            from jmicro.inference_precision import install, PROFILE
            if precision != PROFILE:
                raise ValueError('Unknown inference precision profile')
            install(model)
        with torch.inference_mode():
            ids, reason = greedy(input_ids, step, max_new_tokens, stop_ids, forced_first_id)
    raw = tok.decode_bytes(ids)
    return {"input_ids": input_ids, "generated_ids": ids, **decode_display(raw, reason),
            "generated_body_bytes_hex": raw.hex(), "stop_reason": reason,
            "backend": backend, "stop_ids": stop_ids, "suppressed_ids": list(SUPPRESS_IDS)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=["torch", "hf", "gguf"], required=True)
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--tokenizer", type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt")
    group.add_argument("--messages", type=Path, help="JSON array of role/text or role/content messages")
    parser.add_argument("--max-new-tokens", type=int, default=16)
    parser.add_argument("--bridge", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    tok = Tokenizer(args.tokenizer)
    removed = 0
    if args.messages:
        ids, removed = tok.chat_prompt(read_json(args.messages), 1024 - args.max_new_tokens)
    else:
        ids = [2, *tok.encode(args.prompt)]
    result = generate(args.backend, args.artifact, tok, ids, args.max_new_tokens,
                      chat=bool(args.messages), bridge=args.bridge)
    result["removed_complete_turns"] = removed
    if args.output:
        write_json(args.output, result)
    print(json.dumps(result, ensure_ascii=False))
