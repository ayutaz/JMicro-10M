"""Original CC0 sentence eligibility, exact-body split and fixed TRAIN sample."""
import hashlib
import random
import re

TERMINAL = re.compile(r'[。！？][」』）)\]”"]*$')
WRAPPER = re.compile(r'https?://|www\.|<\||\|>|```|^#{1,6}\s|^(?:System|User|Assistant)\s*:',re.I)


def parse_line(raw):
    text = raw.decode('utf-8',errors='strict').removesuffix('\n')
    fields = text.split('\t')
    if len(fields)!=4 or not fields[0].isdigit() or int(fields[0])<=0 or fields[1]!='jpn':
        raise ValueError('Official Japanese CC0 four-column TSV schema required')
    return dict(source_id=int(fields[0]),language=fields[1],text=fields[2],modified=fields[3])


def family_split(text):
    # Source IDs provide attribution. Identical original bodies, even under
    # multiple IDs, must share one family and one reserved split.
    family = hashlib.sha256(b'tatoeba-original-CC0-body-v1\0'+text.encode('utf-8')).hexdigest()
    bucket = int(family[:16],16)%100
    return family,('train' if bucket<90 else 'dev' if bucket<95 else 'test')


def candidate(record,tokenizer,protected):
    text = record['text']
    if not 10<=len(text)<=256: return None,'characters'
    if WRAPPER.search(text): return None,'URL_special_or_wrapper'
    if not TERMINAL.search(text): return None,'terminal_punctuation'
    if any(prefix in text for prefix in protected): return None,'fixed_DEV_prefix_overlap'
    ids = tokenizer.encode(text)
    if not 6<=len(ids)<=64 or any(n<8 for n in ids): return None,'body_tokens'
    if tokenizer.decode_bytes(ids)!=text.encode('utf-8'): return None,'original_codec_bytes'
    family,split = family_split(text)
    return dict(id='tatoeba-cc0-'+str(record['source_id']),source_id=record['source_id'],
        source='tatoeba_original_CC0',source_url='https://tatoeba.org/en/sentences/show/'+str(record['source_id']),
        license='CC0-1.0',original_provenance='Official CC0 export and documented original-only contribution policy; not independent author verification',
        language='jpn',modified=record['modified'],family=family,split=split,text=text,
        body_sha256=hashlib.sha256(text.encode('utf-8')).hexdigest(),body_ids=ids,
        body_tokens=len(ids),body_bytes=len(text.encode('utf-8'))),None


def fixed_sample(rows,seed=2026100747):
    if len(rows)<80 or any(r['split']!='train' for r in rows):
        raise ValueError('At least80 eligible TRAIN sentences required')
    if len({r['family'] for r in rows})!=len(rows): raise ValueError('Exact-body dedup before sampling required')
    indices = sorted(random.Random(seed).sample(range(len(rows)),80))
    return [rows[i] for i in indices],indices
