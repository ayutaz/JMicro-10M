"""Lossless SentencePiece body codec and explicit dialogue structure.

Unicode whitespace other than ASCII space, literal U+2581, and '<' use
reserved UTF-8 byte pieces. This avoids whitespace-marker collisions and
interpreting literal special-token spellings as structure. Decode assembles
bytes before UTF-8 validation, including adjacent byte fallback sequences.
"""

from pathlib import Path
import json
import sentencepiece as spm

from jmicro.evaluation import canonicalize_text

ROLE_IDS = {"system": 4, "user": 5, "assistant": 6}
SUPPRESS_IDS = (0, 1, 2, 4, 5, 6)
CODEC_VERSION = "sp-unigram-protected-byte-v1"


def protected(char: str) -> bool:
    return char in "▁<" or (char.isspace() and char != " ")


def training_spans(text: str):
    start = 0
    for i, char in enumerate(text):
        if protected(char):
            if i > start:
                yield text[start:i]
            start = i + 1
    if start < len(text):
        yield text[start:]


class Tokenizer:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.sp = spm.SentencePieceProcessor(model_file=str(self.path))
        self.byte_ids = [self.sp.piece_to_id(f"<0x{b:02X}>") for b in range(256)]
        if len(set(self.byte_ids)) != 256 or any(not self.sp.is_byte(i) for i in self.byte_ids):
            raise ValueError("Tokenizer must contain all 256 byte pieces")
        self.id_bytes = {i: bytes([b]) for b, i in enumerate(self.byte_ids)}
        self.vocab_size = self.sp.get_piece_size()
        expected = ["<|pad|>", "<|unk|>", "<|bos|>", "<|eos|>",
                    "<|system|>", "<|user|>", "<|assistant|>", "<|eot|>"]
        if [self.sp.id_to_piece(i) for i in range(8)] != expected:
            raise ValueError("Special-token ID contract differs")

    def encode(self, text: str) -> list[int]:
        text = canonicalize_text(text)
        ids, start = [], 0
        for i, char in enumerate(text):
            if protected(char):
                ids.extend(self.sp.encode(text[start:i], out_type=int))
                ids.extend(self.byte_ids[b] for b in char.encode("utf-8"))
                start = i + 1
        ids.extend(self.sp.encode(text[start:], out_type=int))
        if any(i < 8 for i in ids):
            raise ValueError("Body encoding emitted a structural/unknown ID")
        return ids

    def decode_bytes(self, ids: list[int]) -> bytes:
        parts = []
        for i in ids:
            if not 0 <= i < self.vocab_size:
                raise ValueError("Token ID outside vocabulary")
            if i == 1:
                raise ValueError("Unknown token cannot be decoded losslessly")
            if i < 8:
                continue
            parts.append(self.id_bytes[i] if i in self.id_bytes else
                         self.sp.id_to_piece(i).replace("▁", " ").encode("utf-8"))
        return b"".join(parts)

    def decode(self, ids: list[int], errors: str = "strict") -> str:
        return self.decode_bytes(ids).decode("utf-8", errors=errors)

    def dialogue(self, messages: list[dict], generation_prompt: bool = False) -> tuple[list[int], list[int]]:
        ids, labels = [2], [-100]
        for message in messages:
            role = message["role"]
            body = self.encode(message.get("text", message.get("content", "")))
            ids.extend([ROLE_IDS[role], *body, 7])
            labels.extend([-100, *(body if role == "assistant" else [-100] * len(body)),
                           7 if role == "assistant" else -100])
        if generation_prompt:
            ids.append(6)
            labels.append(-100)
        return ids, labels

    def chat_prompt(self, messages: list[dict], max_tokens: int) -> tuple[list[int], int]:
        """Remove oldest complete user/assistant turns, retain system and current user."""
        messages = list(messages)
        if not messages or messages[-1]["role"] != "user":
            raise ValueError("Generation history must end with user")
        offset = int(messages[0]["role"] == "system")
        roles = [m["role"] for m in messages[offset:]]
        if roles != ["user" if i % 2 == 0 else "assistant" for i in range(len(roles))]:
            raise ValueError("History must alternate user/assistant")
        removed = 0
        while True:
            ids, _ = self.dialogue(messages, generation_prompt=True)
            if len(ids) <= max_tokens:
                return ids, removed
            if len(messages) - offset <= 1:
                raise ValueError("System/current user cannot fit without cutting a message")
            del messages[offset:offset + 2]
            removed += 1

    def sft_windows(self, messages: list[dict], context: int = 1024):
        """One complete assistant target per window, retaining fitting prior messages."""
        offset = int(bool(messages) and messages[0]["role"] == "system")
        for end, message in enumerate(messages):
            if message["role"] != "assistant":
                continue
            history = list(messages[:end + 1])
            removed = 0
            while len(self.dialogue(history)[0]) > context:
                if len(history) - offset <= 2:
                    raise ValueError("A complete user/assistant target exceeds context")
                del history[offset:offset + 2]
                removed += 1
            ids, labels = self.dialogue(history)
            # Mask earlier assistant replies; each source target is taught once.
            target_len = len(self.encode(message.get("text", message.get("content", "")))) + 1
            labels[:-target_len] = [-100] * (len(labels) - target_len)
            yield {"input_ids": ids, "labels": labels, "target_tokens": target_len,
                   "target_message_index": end, "removed_turns": removed}

    def save_wrapper(self, directory: Path) -> None:
        (directory / "tokenizer_wrapper.json").write_text(json.dumps({
            "codec": CODEC_VERSION, "model": "tokenizer.model", "external_codec_required": True,
            "canonicalization": "CRLF/CR to LF; remove NUL; otherwise preserve Unicode",
            "protected": "non-ASCII-space whitespace, U+2581, '<' as UTF-8 byte pieces",
            "body_special_ids_forbidden": list(range(8)), "role_ids": ROLE_IDS,
            "base_stop_ids": [3], "chat_stop_ids": [7, 3], "suppress_ids": list(SUPPRESS_IDS),
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
