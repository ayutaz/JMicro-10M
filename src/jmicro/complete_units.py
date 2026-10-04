"""Conservative complete Japanese sentence units, independent of GPU training."""
import hashlib
import re

from jmicro.evaluation import canonicalize_text

PAIRS = {'「': '」', '『': '』', '（': '）', '(': ')', '【': '】', '[': ']', '〈': '〉', '《': '》', '〔': '〕', '“': '”'}
CLOSERS = set(PAIRS.values())
ENDS = set('。！？!?')
BAD = re.compile(r'https?://|www\.|```|"|続きを読む|続きはこちら|もっと見る|Read more|\.{2,}|…|⋯', re.I)
JAPANESE = re.compile(r'[ぁ-んァ-ヶ一-龯]')
PREDICATE_END = re.compile(r'[うくすつぬぶむるたいだかねよなわぞ](?:[。！？!?]+)$')


def balanced(text):
    stack = []
    for char in text:
        if char in PAIRS:
            stack.append(PAIRS[char])
        elif char in CLOSERS:
            if not stack or stack.pop() != char:
                return False
    return not stack


def complete_sentences(text):
    """Yield source character spans; never emit an unterminated trailing fragment."""
    start, stack, malformed = 0, [], False
    for i, char in enumerate(text):
        if char in PAIRS:
            stack.append(PAIRS[char])
        elif char in CLOSERS:
            if not stack or stack.pop() != char:
                malformed = True
        if stack:
            continue
        quote_end = char in CLOSERS and text[start:i].rstrip(''.join(CLOSERS)).endswith(tuple(ENDS))
        quote_boundary = i + 1 == len(text) or text[i + 1] in '\r\n'
        ending = char in ENDS or (quote_end and quote_boundary)
        if not ending:
            continue
        if i + 1 < len(text) and (text[i + 1] in ENDS or text[i + 1] in CLOSERS):
            continue
        piece = text[start:i + 1]
        left = len(piece) - len(piece.lstrip())
        a, b = start + left, i + 1
        start = b
        value = text[a:b]
        ending_text = value.rstrip(''.join(CLOSERS))
        heading = any(not PREDICATE_END.search(line.strip().rstrip(''.join(CLOSERS))) for line in value.splitlines()[:-1] if line.strip())
        if (not malformed and value and JAPANESE.search(value) and not BAD.search(value)
                and PREDICATE_END.search(ending_text) and not heading
                and not re.search(r'(^|\n)\s*(?:[|=<>]|[-*#・●0-9０-９]+[.．)）:\s])', value)):
            yield a, b, value
        malformed = False


def complete_units(text, tok, minimum=32, maximum=64):
    """Join adjacent complete sentences when necessary; never cut an oversized one."""
    pending, begin, last_end = '', 0, -1
    for a, b, sentence in complete_sentences(text):
        if pending and text[last_end:a].strip():
            pending = ''
        candidate = pending + text[last_end:a] + sentence if pending else sentence
        ids = tok.encode(candidate)
        if len(ids) > maximum:
            pending = ''
            candidate, ids = sentence, tok.encode(sentence)
        if len(ids) > maximum:
            continue
        if not pending:
            begin = a
        if len(ids) >= minimum:
            if balanced(candidate) and all(i >= 8 for i in ids):
                yield {'text': candidate, 'ids': ids, 'char_start': begin, 'char_end': b,
                       'text_sha256': hashlib.sha256(canonicalize_text(candidate).encode('utf-8')).hexdigest()}
            pending = ''
        else:
            pending = candidate
        last_end = b


def unit_hash(text):
    return hashlib.sha256(canonicalize_text(text).encode('utf-8')).hexdigest()
