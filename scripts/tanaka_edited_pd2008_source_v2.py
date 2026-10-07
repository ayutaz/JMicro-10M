"""Exact edited-PD2008 Japanese extraction and body-family source contract."""
import hashlib
import random
import re

TERMINAL=re.compile(r'[。！？][」』）)\]”"]*$')
WRAPPER=re.compile(r'https?://|www\.|<\||\|>|```|^#{1,6}\s|^(?:System|User|Assistant)\s*:',re.I)


def parse_line(raw,expected_kind):
    text=raw.decode('euc_jp',errors='strict')
    if text.encode('euc_jp')!=raw: raise ValueError('Lossless strict EUC-JP required')
    if not text.endswith('\r\n'): raise ValueError('Discovered CRLF record schema required')
    text=text[:-2]
    if text.startswith(('#A:','#B:')): return 'comment',None
    if not text.startswith(expected_kind+': '): raise ValueError('Alternating A/Japanese+English and B/index records required')
    if expected_kind=='B':
        if '\t' in text: raise ValueError('Unexpected index record tab')
        return 'B',None
    fields=text[3:].split('\t')
    if len(fields)!=2 or not all(fields): raise ValueError('One exact Japanese/English pair required')
    return 'A',fields[0]


def family_split(text):
    family=hashlib.sha256(b'tanaka-edited-PD2008-body-v1\0'+text.encode('utf-8')).hexdigest()
    bucket=int(family[:16],16)%100
    return family,('train' if bucket<90 else 'dev' if bucket<95 else 'test')


def candidate(text,line_number,tokenizer,protected,archive_sha256):
    if not 10<=len(text)<=256: return None,'characters'
    if WRAPPER.search(text): return None,'URL_special_or_wrapper'
    if not TERMINAL.search(text): return None,'terminal_punctuation'
    if any(prefix in text for prefix in protected): return None,'fixed_DEV_prefix_overlap'
    ids=tokenizer.encode(text)
    if not 6<=len(ids)<=64 or any(n<8 for n in ids): return None,'body_tokens'
    if tokenizer.decode_bytes(ids)!=text.encode('utf-8'): return None,'original_codec_bytes'
    family,split=family_split(text)
    return dict(id='tanaka-pd2008-line-'+str(line_number),source='tanaka_edited_PD2008',
        source_url='ftp://ftp.edrdg.org/pub/Nihongo/examples_pd.gz',license='Public Domain edition, publisher claim',
        provenance='Human-collected/edited examples; translations and contrived usage possible; not independently verified original Japanese authorship',
        archive_sha256=archive_sha256,source_line=line_number,language='jpn',source_encoding='euc_jp',
        family=family,split=split,text=text,body_sha256=hashlib.sha256(text.encode('utf-8')).hexdigest(),
        body_ids=ids,body_tokens=len(ids),body_bytes=len(text.encode('utf-8'))),None


def fixed_sample(rows,seed=2026100751):
    if len(rows)<80 or any(r['split']!='train' for r in rows): raise ValueError('80 eligible TRAIN rows required')
    if len({r['family'] for r in rows})!=len(rows): raise ValueError('Exact-body dedup required')
    indices=sorted(random.Random(seed).sample(range(len(rows)),80))
    return [rows[i] for i in indices],indices
