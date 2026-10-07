"""Close an actual source encoding failure; never claim model completion."""
import gzip
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive

if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
reports=ROOT/'reports/phase6'
output=reports/'tanaka_edited_pd2008_source_completion.json'
if output.exists(): raise ValueError('Preserve actual closeout')
pin=read_json(reports/'tanaka_edited_pd2008_source_pin.json')
diagnosis=read_json(reports/'tanaka_edited_pd2008_encoding_failure.json')
config_path=ROOT/'configs/phase6/tanaka_edited_pd2008_source_v2.json';config=read_json(config_path)
job=read_json(reports/'tanaka-edited-pd2008-source-v2-20261007/job.json')
if alive(job) or job['status']!='failed' or 'UnicodeDecodeError' not in job['error']:
    raise ValueError('Actual ended encoding failure required')
if job['config_sha256']!=sha256(config_path) or diagnosis['failed_line']!=job['scanned_lines'] or diagnosis['is_publisher_commented_metadata']:
    raise ValueError('Actual active-body encoding failure binding required')
for name,digest in config['source_sha256'].items():
    if sha256(ROOT/name)!=digest: raise ValueError('Frozen source changed: '+name)
for name,ref in config['references'].items():
    if sha256(Path(ref['path']))!=ref['sha256']: raise ValueError('Frozen reference changed: '+name)
archive=Path(pin['path']);st=archive.stat()
if (st.st_size,st.st_mtime_ns)!=(pin['file_size'],pin['file_mtime_ns']): raise ValueError('Already streamed archive identity changed')
if any((archive.parent/(split+'-source.jsonl')).exists() for split in ('train','dev','test')):
    raise ValueError('No partial prepared source may be presented as usable')
if (reports/'tanaka-edited-pd2008-source-v2-20261007/fixed80.json').exists():
    raise ValueError('No sample was frozen before incomplete whole-source validation')
result=dict(created_at=now(),status='fixed_edited_PD2008_source_closed_strict_active_body_encoding_failed',
    proposal_sha256=config['references']['proposal']['sha256'],config_sha256=sha256(config_path),
    source_url=pin['source_url'],compressed_archive_SHA256=pin['compressed_SHA256'],compressed_bytes=pin['file_size'],
    actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},actual_process_ended=True,
    whole_archive_encoding_verified=False,whole_archive_schema_verified=False,
    failure='Standard EUC-JP strict decoding failed inside an active A: Japanese/English pair at line298737, byte33=0xad; not excluded #A:/#B: metadata. Do not guess an alternate legacy encoding, replace characters, ignore errors or drop affected active examples to rescue this fixed source.',
    scanned_active_A_records_before_failure=job['scanned_records'],scanned_lines=job['scanned_lines'],decompressed_bytes_at_failure=job['decompressed_bytes'],
    complete_source_quantity_measured=False,source_readiness_failed=True,amount_screen_passed=None,
    fixed80_frozen=False,content_screen_passed=None,eligible_for_training=False,
    network_wall_seconds=pin['total_network_wall_seconds'],network_cap_seconds=60,
    cumulative_source_CPU_seconds=diagnosis['cumulative_CPU_seconds'],CPU_cap_seconds=90,
    GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0,
    corrections='Published FTP endpoint and retrieval used unchanged source/caps after candidateHTTPS certificate and FTP SIZE metadata failures. Initial5line discovery verified only prefix/schema, not full archive. Actual publisher #A:/#B: commented section omission corrected once, preserving failed source/config/job and cumulative CPU; V2 then exposed a genuine active-body decode failure. No third preparation attempt.',
    limitations='Source feasibility failure, not model training failure, complete-corpus quantity estimate or proof against all human Japanese data. Standard EUC-JP may not cover legacy extensions; alternate encoding provenance remains unverified and is not silently inferred.',
    old_corpus_scanned=False,tokenizer_retrained=False,protected_test_scored=False,
    Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
    next_action='Close this source condition; review already pinned public Japanese corpus provenance and one new finite comparison before any additional GPU training. No source mirror/current-release/filter/seed/threshold/epoch or decoding rescue.')
atomic_json(output,result)
paths=set([Path(__file__).resolve(),ROOT/'configs/phase6/tanaka_edited_pd2008_source.json',config_path])
for pattern in ('*tanaka_edited_pd2008*.py','tanaka_edited_pd2008*.json','tanaka_edited_pd2008*.xml'):
    paths.update(reports.glob(pattern))
for pattern in ('*tanaka_edited_pd2008*.py',):
    paths.update((ROOT/'scripts').glob(pattern));paths.update((ROOT/'tests').glob(pattern))
for directory in ('tanaka-edited-pd2008-source-20261007','tanaka-edited-pd2008-source-v2-20261007'):
    paths.update((reports/directory).glob('*.json'))
entries=[];buffers=[]
for path in sorted(paths):
    data=path.read_bytes();name=str(path.relative_to(ROOT));buffers.append((name,data))
    entries.append(dict(path=name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
target=reports/'tanaka_edited_pd2008_source_evidence.tar.gz'
if target.exists(): raise ValueError('Never overwrite evidence archive')
with target.open('xb') as stream,gzip.GzipFile(fileobj=stream,mode='wb',mtime=0) as compressed,tarfile.open(fileobj=compressed,mode='w|') as tar:
    for name,data in buffers:
        info=tarfile.TarInfo(name);info.size=len(data);info.mtime=0;tar.addfile(info,io.BytesIO(data))
manifest=dict(created_at=now(),files=entries,text_files=len(entries),text_bytes=sum(r['bytes'] for r in entries),
    archive=dict(path=str(target),bytes=target.stat().st_size,sha256=sha256(target)),
    raw_archive_kept_on_WSL=str(archive),GPU_seconds=0,Base_complete=False)
atomic_json(reports/'tanaka_edited_pd2008_source_evidence_manifest.json',manifest)
print(json.dumps(dict(status=result['status'],CPU_seconds=result['cumulative_source_CPU_seconds'],network_seconds=result['network_wall_seconds'],
    evidence=manifest['archive'],text_files=len(entries))))
