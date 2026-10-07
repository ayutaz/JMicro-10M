"""Inspect one failed source record as structural metadata, without scoring bodies."""
import gzip
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
out=ROOT/'reports/phase6/tanaka_edited_pd2008_schema_failure.json'
if out.exists(): raise ValueError('Existing structural diagnosis retained')
pin=read_json(ROOT/'reports/phase6/tanaka_edited_pd2008_source_pin.json')
job=read_json(ROOT/'reports/phase6/tanaka-edited-pd2008-source-20261007/job.json')
start=time.monotonic();last=None
with gzip.open(pin['path'],'rb') as f:
    for i in range(job['scanned_lines']): last=f.readline(131073)
    remaining=f.read(16385)
text=last.decode('euc_jp',errors='strict')
result=dict(created_at=now(),source_sha256=sha256(Path(__file__)),failed_line=job['scanned_lines'],
    failed_record_bytes=len(last),prefix_hex=last[:8].hex(),tabs=text.count('\t'),
    structural_text=text.strip() if not text.startswith(('A:','B:')) else None,
    bytes_following_failed_line_bounded=len(remaining),following_prefix_hex=remaining[:8].hex(),
    CPU_seconds=time.monotonic()-start,cumulative_CPU_seconds=job['CPU_seconds']+time.monotonic()-start,
    source_bodies_read_for_quality=False,network_seconds=0,GPU_seconds=0,Base_complete=False)
atomic_json(out,result);print(json.dumps(result,ensure_ascii=False))
