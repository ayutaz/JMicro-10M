"""One bounded metadata-only check of an already pinned parliamentary corpus."""
import hashlib
import json
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import pyarrow.parquet as pq
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from remote_parquet_ranges import RangeBudget,RangeFile

if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
out=ROOT/'reports/phase6/openja_base_footer.json'
plan=ROOT/'reports/phase6/openja_base_source_feasibility_proposal.json'
if out.exists(): raise ValueError('Preserve original footer inspection')
c=read_json(plan)
registry=ROOT/'reports/phase6/public_prose_registry_metadata.json'
review=ROOT/'reports/phase6/public_prose_registry_review.json'
if sha256(registry)!=c['registry_sha256'] or sha256(review)!=c['prior_registry_review_sha256']:
    raise ValueError('Previously pinned exact source binding changed')
source=next(r for r in read_json(registry)['repositories'] if r['repository']==c['repository'])
file=next(r for r in source['siblings'] if r['rfilename']=='openja.parquet')
if source['revision']!=c['revision'] or file['lfs']['sha256']!=c['upstream_full_blob_SHA256']:
    raise ValueError('Exact repository/revision/blob required; no mirror/latest revision')
size=file['size'];url=f"https://huggingface.co/datasets/{source['repository']}/resolve/{source['revision']}/openja.parquet"
start=time.monotonic();budget=RangeBudget(4*1024*1024,30)
try:
    with RangeFile(url,size,budget) as stream:
        if stream.read(4)!=b'PAR1': raise ValueError('Observed Parquet header required')
        parquet=pq.ParquetFile(stream,pre_buffer=False);m=parquet.metadata
        groups=[]
        for i in range(m.num_row_groups):
            g=m.row_group(i)
            groups.append(dict(index=i,rows=g.num_rows,columns=[dict(path=g.column(k).path_in_schema,
                compressed_bytes=g.column(k).total_compressed_size) for k in range(g.num_columns)]))
        ranges=[dict(offset=offset,bytes=len(content),sha256=hashlib.sha256(content).hexdigest()) for offset,content in stream.cache]
        result=dict(status='pinned_metadata_only_footer_observed',created_at=now(),proposal_sha256=sha256(plan),
            source_sha256=sha256(Path(__file__)),range_reader_sha256=sha256(ROOT/'scripts/remote_parquet_ranges.py'),
            repository=c['repository'],revision=c['revision'],file='openja.parquet',file_bytes=size,
            upstream_full_blob_SHA256=c['upstream_full_blob_SHA256'],full_blob_hash_independently_verified=False,
            rows=m.num_rows,schema=str(parquet.schema_arrow),row_groups=groups,ranges=ranges,
            network_bytes=budget.bytes,HTTP_requests=budget.requests,wall_seconds=time.monotonic()-start,
            data_rows_read=0,new_prepared_TRAIN_tokens=0,GPU_seconds=0,Base_complete=False,
            next_action='Use actual compressed column sizes to freeze one group uniformly from groups fitting96MiB; no text-based group choice or full-file fallback.')
except Exception as error:
    result=dict(status='bounded_footer_failed',created_at=now(),proposal_sha256=sha256(plan),
        source_sha256=sha256(Path(__file__)),error_type=type(error).__name__,network_bytes=budget.bytes,HTTP_requests=budget.requests,
        wall_seconds=time.monotonic()-start,data_rows_read=0,GPU_seconds=0,Base_complete=False,
        next_action='Close this access condition without identical retries/full-file fallback.')
    atomic_json(out,result);raise RuntimeError('Bounded footer failure; sanitized evidence saved') from None
atomic_json(out,result)
print(json.dumps({k:result[k] for k in ('status','rows','network_bytes','HTTP_requests','wall_seconds')}))
