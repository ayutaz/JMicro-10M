"""Bounded schema discovery of the already pinned public archive; no network."""
import gzip
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json

if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv interpreter required')
output=ROOT/'reports/phase6/tanaka_edited_pd2008_format.json'
if output.exists(): raise ValueError('Preserve existing one-shot discovery')
pin=read_json(ROOT/'reports/phase6/tanaka_edited_pd2008_source_pin.json')
p=Path(pin['path']);st=p.stat()
if (st.st_size,st.st_mtime_ns)!=(pin['file_size'],pin['file_mtime_ns']): raise ValueError('Pinned archive stat changed')
began=time.monotonic()
with gzip.open(p,'rb') as f:
    rows=[f.readline(16385) for _ in range(5)]
if any(len(r)>16384 for r in rows): raise ValueError('Bounded discovery line exceeded')
details=[]
for raw in rows:
    decoders={}
    for encoding in ('utf-8','euc_jp'):
        try:
            text=raw.decode(encoding,errors='strict')
            decoders[encoding]=dict(roundtrip=text.encode(encoding)==raw,prefix=text[:2],tabs=text.count('\t'),
                ends_LF=text.endswith('\n'),ends_CRLF=text.endswith('\r\n'),has_sentence_ID='{#' in text,
                header=text.strip() if text.startswith('#') else None)
        except UnicodeError: decoders[encoding]=dict(strict_decode=False)
    details.append(dict(bytes=len(raw),sha256=__import__('hashlib').sha256(raw).hexdigest(),decoders=decoders))
result=dict(created_at=now(),source_sha256=sha256(Path(__file__)),source_pin_sha256=sha256(ROOT/'reports/phase6/tanaka_edited_pd2008_source_pin.json'),
    status='bounded_schema_discovery_completed_no_source_quality_selection',rows=details,
    CPU_seconds=time.monotonic()-began,network_seconds=0,GPU_seconds=0,
    content_review_performed=False,sample_selection_changed=False,Base_complete=False)
atomic_json(output,result)
print(json.dumps(result,ensure_ascii=False))
