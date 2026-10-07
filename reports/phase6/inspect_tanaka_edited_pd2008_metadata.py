"""One finite metadata-only official archive check; no corpus/model acquisition."""
import hashlib
import json
from pathlib import Path
import re
import signal
import sys
import time
import urllib.request
sys.path.insert(0,str(Path.cwd()/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json

proposal=ROOT/'reports/phase6/tanaka_edited_pd2008_source_proposal.json'
target=ROOT/'reports/phase6/tanaka_edited_pd2008_source_metadata.json'
if target.exists(): raise ValueError('Preserve one-shot metadata result; no identical retry')
p=read_json(proposal);started=time.monotonic();records=[];status='checking'
def stop(*args): raise TimeoutError('Fixed metadata network60-second limit exhausted')
signal.signal(signal.SIGALRM,stop);signal.alarm(p['budgets']['network_wall_seconds'])
try:
    for name,url in (('publisher',p['primary_sources_checked'][0]['url']),
                     ('catalog',p['primary_sources_checked'][1]['url'])):
        with urllib.request.urlopen(url,timeout=15) as response:
            raw=response.read(1048577)
            if len(raw)>1048576: raise ValueError('Bounded official metadata page too large')
            text=raw.decode('utf-8')
            entries=re.findall(r'href=[\x22\x27]([^\x22\x27]*examples_pd[^\x22\x27]*)',text,re.I)
            records.append(dict(name=name,url=url,final_url=response.url,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
                candidate_archive_links=entries,mentions_last_Public_Domain=('last Public Domain' in text),
                mentions_Oct2008=bool(re.search(r'Oct(?:ober)?\s*2008',text)),
                mentions_errors=('errors' in text.lower())))
    if not all(r['mentions_last_Public_Domain'] and r['mentions_Oct2008'] for r in records):
        raise ValueError('Actual publisher/catalog do not identify the fixed2008 Public Domain edition')
    url=p['candidate_official_archive_url_to_verify']
    with urllib.request.urlopen(urllib.request.Request(url,method='HEAD'),timeout=15) as response:
        records.append(dict(name='archive_HEAD',url=url,final_url=response.url,status=response.status,
            metadata={k:response.headers.get(k) for k in ('Content-Length','Last-Modified','ETag','Content-Type')},
            downloaded_corpus_bytes=0))
    status='official_edited_PD2008_metadata_reachable_no_corpus_acquired'
except Exception as error:
    status='official_edited_PD2008_metadata_gate_failed';failure=repr(error)
finally:
    signal.alarm(0)
    elapsed=time.monotonic()-started
    atomic_json(target,dict(status=status,created_at=now(),proposal_sha256=sha256(proposal),source_sha256=sha256(Path(__file__)),
        actual_records=records,network_wall_seconds=elapsed,network_cap_seconds=p['budgets']['network_wall_seconds'],
        error=locals().get('failure'),GPU_seconds=0,scientific_teacher_tokens=0,downloaded_corpus_bytes=0,
        source_encoding_verified=False,source_schema_verified=False,source_quantity_verified=False,
        Base_complete=False,Chat_started=False,quantization_started=False,
        next_action='Only verified metadata permits implementing fixed archival-source preparation; source amount/content/quality remain unproven. Failed metadata: close this archive condition, no mirror/current/original source substitution.'))
    print(json.dumps(dict(status=status,seconds=elapsed,records=records,error=locals().get('failure'))))
