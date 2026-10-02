"""Tokenizer-independent evaluation contracts; no model or training code."""

import math


def canonicalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Expected decoded UTF-8 text")
    text.encode("utf-8", errors="strict")
    return text.replace("\r\n", "\n").replace("\r", "\n").replace("\x00", "")


def bits_per_byte(total_body_nll: float, scored_canonical_bytes: int) -> float:
    if not math.isfinite(total_body_nll) or total_body_nll < 0:
        raise ValueError("Body NLL must be finite and nonnegative")
    if isinstance(scored_canonical_bytes, bool) or not isinstance(scored_canonical_bytes, int) or scored_canonical_bytes <= 0:
        raise ValueError("Scored canonical byte count must be a positive integer")
    return total_body_nll / (math.log(2) * scored_canonical_bytes)
