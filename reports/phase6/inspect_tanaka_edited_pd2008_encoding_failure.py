"""Identify whether an encoding failure is active Japanese or excluded metadata."""
import gzip
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
out=ROOT/'reports/phase6/tanaka_edited_pd2008_encoding_failure.json'
if out.exists(): raise ValueError('Existing structural diagnosis retained')
pin=read_json(ROOT/'reports/phase6/tanaka_edited_pd2008_source_pin.json')
job=read_json(ROOT/'reports/phase6/tanaka-edited-pd2008-source-v2-20261007/job.json')
start=time.monotonic()
with gzip.open(pin['path'],'rb') as f:
    for i in range(job['scanned_lines']): raw=f.readline(131073)
result=dict(created_at=now(),source_sha256=sha256(Path(__file__)),failed_line=job['scanned_lines'],
    failed_record_bytes=len(raw),prefix_hex=raw[:8].hex(),is_publisher_commented_metadata=raw.startswith((b'#A:',b'#B:')),
    CPU_seconds=time.monotonic()-start,cumulative_CPU_seconds=job['CPU_seconds']+time.monotonic()-start,
    source_bodies_read_for_quality=False,network_seconds=0,GPU_seconds=0,Base_complete=False)
atomic_json(out,result);print(json.dumps(result))
