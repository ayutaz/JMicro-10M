"""Complete exact source speech bodies, preserving all non-header characters."""
import hashlib
import random
import re
TERMINAL=re.compile(r'[。！？][」』）)\]”"]*$')
WRAPPER=re.compile(r'https?://|www\.|<\||\|>|```|^#{1,6}\s|^(?:System|User|Assistant)\s*:',re.I)
SPEAKER_HEADER=re.compile(r'\A○[^。！？\r\n\t　]{1,100}　')


def candidate(source,row_number,group,tokenizer,protected):
    if not all(isinstance(source.get(k),str) and source[k] for k in ('id','issueID','text','speechURL')):
        return None,'missing_source_identity'
    if not source['id'].startswith(source['issueID']+'_') or not source['speechURL'].startswith('https://kokkai.ndl.go.jp/txt/'+source['issueID']+'/'):
        return None,'source_identity_schema'
    original=source['text'];original.encode('utf-8',errors='strict')
    header=SPEAKER_HEADER.match(original);start=header.end() if header else 0
    body=original[start:]
    if not 10<=len(body)<=256: return None,'characters'
    if WRAPPER.search(body): return None,'URL_special_or_wrapper'
    if not TERMINAL.search(body): return None,'terminal_punctuation'
    if any(prefix in body for prefix in protected): return None,'fixed_DEV_prefix_overlap'
    ids=tokenizer.encode(body)
    if not 6<=len(ids)<=64 or any(n<8 for n in ids): return None,'body_tokens'
    if tokenizer.decode_bytes(ids)!=body.encode(): return None,'original_codec_bytes'
    family=hashlib.sha256(b'openja-meeting-family-v1\0'+source['issueID'].encode()).hexdigest()
    bucket=int(family[:16],16)%100
    split='train' if bucket<90 else 'dev' if bucket<95 else 'test'
    return dict(id='openja-'+source['id'],source_id=source['id'],meeting=source['issueID'],
        source='OpenJA_parliamentary_original_speech',source_url=source['speechURL'],
        source_row=row_number,row_group=group,family=family,split=split,text=body,
        original_text_sha256=hashlib.sha256(original.encode()).hexdigest(),
        original_UTF8_byte_span=[len(original[:start].encode()),len(original.encode())],
        speaker_header_removed=bool(header),body_sha256=hashlib.sha256(body.encode()).hexdigest(),
        body_ids=ids,body_tokens=len(ids),body_bytes=len(body.encode())),None


def fixed_sample(rows,seed=2026100755):
    if len(rows)<80 or any(r['split']!='train' for r in rows): raise ValueError('80 eligibleTRAIN rows required')
    if len({r['body_sha256'] for r in rows})!=len(rows): raise ValueError('Exact-body dedup required')
    indices=sorted(random.Random(seed).sample(range(len(rows)),80))
    return [rows[i] for i in indices],indices
