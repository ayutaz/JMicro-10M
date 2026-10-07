"""Correct the provisional HTTPS transport and HTML check using the published FTP link."""
import ftplib
import hashlib
import html
import json
from pathlib import Path
import re
import signal
import sys
import time
import urllib.request
from urllib.parse import urlparse
sys.path.insert(0,str(Path.cwd()/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json

phase=ROOT/'reports/phase6';initial=phase/'tanaka_edited_pd2008_source_metadata.json'
target=phase/'tanaka_edited_pd2008_source_metadata_v2.json'
if target.exists(): raise ValueError('Preserve adaptive metadata result; no blind retry')
old=read_json(initial);proposal=phase/'tanaka_edited_pd2008_source_proposal.json'
if old['downloaded_corpus_bytes'] or not old['actual_records']: raise ValueError('Only unchanged pre-acquisition transport correction allowed')
budget=58
if old['network_wall_seconds']+budget>read_json(proposal)['budgets']['network_wall_seconds']:
    raise ValueError('Correction still must fit the original cumulative60-second network cap')
started=time.monotonic();records=[];status='checking'
def stop(*args): raise TimeoutError('Fixed cumulative metadata budget exhausted')
signal.signal(signal.SIGALRM,stop);signal.alarm(budget)
try:
    expected=old['actual_records'][0]
    with urllib.request.urlopen(expected['url'],timeout=10) as response:
        raw=response.read(1048577)
        if len(raw)>1048576 or hashlib.sha256(raw).hexdigest()!=expected['sha256']:
            raise ValueError('Do not silently change the already observed publisher page')
    text=raw.decode();plain=' '.join(html.unescape(re.sub(r'<[^>]*>',' ',text)).split())
    links=re.findall(r'href=[\x22\x27]([^\x22\x27]*examples_pd[^\x22\x27]*)',text,re.I)
    url='ftp://ftp.edrdg.org/pub/Nihongo/examples_pd.gz'
    if url not in links or not re.search(r'last Public Domain version\s*\(Oct\s*2008\)',plain,re.I):
        raise ValueError('Actual publisher does not identify this exact fixed edited2008 archive')
    records.append(dict(name='publisher',url=expected['url'],sha256=expected['sha256'],
                        rendered_last_edited_PD2008_verified=True,actual_archive_URL=url))
    parsed=urlparse(url)
    with ftplib.FTP(timeout=10) as ftp:
        ftp.connect(parsed.hostname);ftp.login();ftp.cwd('/pub/Nihongo');ftp.voidcmd('TYPE I')
        size=ftp.size('examples_pd.gz');modified=ftp.sendcmd('MDTM examples_pd.gz')
        if not size or size>read_json(proposal)['budgets']['maximum_compressed_bytes']:
            raise ValueError('Exact official archive absent or exceeds fixed compressed cap')
        records.append(dict(name='official_FTP_archive_metadata',url=url,bytes=size,MDTM=modified,downloaded_corpus_bytes=0))
    status='official_edited_PD2008_published_FTP_metadata_verified_no_corpus_acquired'
except Exception as error:
    status='official_edited_PD2008_published_FTP_metadata_failed';failure=repr(error)
finally:
    signal.alarm(0);elapsed=time.monotonic()-started
    atomic_json(target,dict(status=status,created_at=now(),proposal_sha256=sha256(proposal),initial_result_sha256=sha256(initial),
        source_sha256=sha256(Path(__file__)),correction='Initial candidate HTTPS endpoint has a hostname-mismatched certificate; no TLS bypass. Use the exact FTP link actually published by the same source. Strip HTML tags for the unchanged last-PD2008 text check. No new archive/license/model/threshold/source selection.',
        actual_records=records,network_wall_seconds=elapsed,total_network_wall_seconds=old['network_wall_seconds']+elapsed,
        network_cap_seconds=60,error=locals().get('failure'),downloaded_corpus_bytes=0,GPU_seconds=0,scientific_teacher_tokens=0,
        source_encoding_verified=False,source_schema_verified=False,source_quantity_verified=False,
        Base_complete=False,Chat_started=False,quantization_started=False,
        next_action='Only positive exact published-source metadata supports implementing archival preparation. Otherwise close this source access condition; no further transport/mirror/current/original substitution.'))
    print(json.dumps(dict(status=status,seconds=elapsed,total_seconds=old['network_wall_seconds']+elapsed,records=records,error=locals().get('failure'))))
