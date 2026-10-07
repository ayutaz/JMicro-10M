"""Exact published FTP archive, streamed byte cap instead of unsupported SIZE metadata."""
import ftplib
import hashlib
import json
from pathlib import Path
import signal
import sys
import time
from urllib.parse import urlparse
sys.path.insert(0,str(Path.cwd()/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json

phase=ROOT/'reports/phase6';proposal=phase/'tanaka_edited_pd2008_source_proposal.json'
metadata=phase/'tanaka_edited_pd2008_source_metadata_v2.json'
target=phase/'tanaka_edited_pd2008_source_pin.json'
data=Path('/home/aihub_ubuntu/jmicro-data/phase6/tanaka-edited-pd2008-20261007')
if target.exists() or data.exists(): raise ValueError('Preserve source pin/partial bytes; no blind redownload')
m,p=read_json(metadata),read_json(proposal)
if (m['downloaded_corpus_bytes'] or m['error']!="ValueError(\"invalid literal for int() with base 10: ''\")"
    or not m['actual_records'][0]['rendered_last_edited_PD2008_verified']):
    raise ValueError('Only pre-acquisition, verified-source SIZE-metadata correction allowed')
url=m['actual_records'][0]['actual_archive_URL']
if url!='ftp://ftp.edrdg.org/pub/Nihongo/examples_pd.gz': raise ValueError('No archive/mirror/license substitution')
cap=56
if m['total_network_wall_seconds']+cap>p['budgets']['network_wall_seconds']: raise ValueError('Keep original cumulative60-second acquisition cap')
data.mkdir(parents=True,exist_ok=False);temporary=data/'examples_pd.gz.partial';final=data/'examples_pd.gz'
started=time.monotonic();digest=hashlib.sha256();size=0;prefix=b'';stage='connect';status='running'
def stop(*args): raise TimeoutError('Original cumulative60-second acquisition budget exhausted')
def receive(chunk):
    global size,prefix
    size+=len(chunk)
    if size>p['budgets']['maximum_compressed_bytes']: raise ValueError('Original64MiB compressed cap exceeded')
    if time.monotonic()-started>cap: stop()
    prefix=(prefix+chunk)[:2];stream.write(chunk);digest.update(chunk)
signal.signal(signal.SIGALRM,stop);signal.alarm(cap)
try:
    with ftplib.FTP(timeout=10) as ftp:
        ftp.connect(urlparse(url).hostname);stage='anonymous_login';ftp.login();stage='official_directory';ftp.cwd('/pub/Nihongo')
        stage='retrieve_exact_published_archive'
        with temporary.open('wb') as stream: ftp.retrbinary('RETR examples_pd.gz',receive,blocksize=65536)
    if not size or prefix!=b'\x1f\x8b': raise ValueError('Complete nonempty actual gzip archive required')
    temporary.replace(final);status='exact_official_edited_PD2008_archive_pinned_CPU_preparation_pending'
except Exception as error:
    status='exact_official_edited_PD2008_archive_recovery_failed';failure=repr(error)
finally:
    signal.alarm(0);elapsed=time.monotonic()-started
    atomic_json(target,dict(status=status,created_at=now(),proposal_sha256=sha256(proposal),metadata_sha256=sha256(metadata),
        source_sha256=sha256(Path(__file__)),source_url=url,stage=stage,error=locals().get('failure'),
        compressed_bytes_received=size,compressed_SHA256=digest.hexdigest(),path=str(final if final.exists() else temporary),
        file_size=(final if final.exists() else temporary).stat().st_size if final.exists() or temporary.exists() else None,
        file_mtime_ns=(final if final.exists() else temporary).stat().st_mtime_ns if final.exists() or temporary.exists() else None,
        network_wall_seconds=elapsed,total_network_wall_seconds=m['total_network_wall_seconds']+elapsed,network_cap_seconds=60,
        correction='Local pinned Python3.12.7 FTP.size converts a213 reply payload with int(); previous nonnumeric SIZE metadata is a transport-metadata issue, not proof that the corpus is missing. Use the same verified published FTP archive, require actual streamed gzip bytes, enforce unchanged compressed/decompressed/network/CPU/amount/content budgets. No TLS bypass, source/license/mirror/filter/seed/threshold substitution or model training.',
        source_encoding_verified=False,source_schema_verified=False,source_quantity_verified=False,
        GPU_seconds=0,scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False,
        next_action='Pinned exact source: implement fixed unchanged-body CPU preparation/content review. Actual recovery failure: retain partial bytes and close this access condition; no further network retries or substitutions.'))
    print(json.dumps(dict(status=status,seconds=elapsed,total_seconds=m['total_network_wall_seconds']+elapsed,
        bytes=size,stage=stage,error=locals().get('failure'))))
