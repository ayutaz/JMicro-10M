"""Archive a source amount failure, keeping it separate from model quality."""
import gzip
import io
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from prepare_openja_base_source import CONFIG,RUN,DATA

if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv interpreter required')
report=ROOT/'reports/phase6';out=report/'openja_base_source_completion.json'
if out.exists(): raise ValueError('Existing source closeout retained')
c,j,r=read_json(CONFIG),read_json(RUN/'job.json'),read_json(RUN/'result.json')
if alive(j) or j['status']!='complete' or r['status']!='fixed_group_amount_failed' or r['amount_screen_passed'] or r['eligible_for_training']:
    raise ValueError('Actual exited source amount failure required')
if r['config_sha256']!=sha256(CONFIG) or j['config_sha256']!=r['config_sha256']:
    raise ValueError('Actual frozen config binding required')
for name,digest in c['source_sha256'].items():
    if sha256(ROOT/name)!=digest: raise ValueError('Frozen source changed: '+name)
for name,ref in c['references'].items():
    if sha256(Path(ref['path']))!=ref['sha256']: raise ValueError('Frozen reference changed: '+name)
if r['source_rows']!=sum(x['documents'] for x in r['splits'].values())+sum(r['rejections'].values()):
    raise ValueError('Actual one-pass source accounting required')
if not r['splits']['train']['body_tokens']<c['readiness']['minimum_distinct_TRAIN_body_tokens']:
    raise ValueError('Preserve prospective amount screen')
sample=read_json(Path(r['fixed80']['path']))
if sha256(Path(r['fixed80']['path']))!=r['fixed80']['sha256'] or len(sample['rows'])!=80:
    raise ValueError('Frozen source80 binding required; no content pass claim')
pin=read_json(Path(r['source_pin']['path']))
if sha256(Path(r['source_pin']['path']))!=r['source_pin']['sha256']: raise ValueError('Bound partial range pin required')
for ref in pin['range_pins']:
    if Path(ref['path']).stat().st_size!=ref['bytes']: raise ValueError('Partial range size changed')
for ref in r['source_files'].values():
    stat=Path(ref['path']).stat()
    if (stat.st_size,stat.st_mtime_ns)!=(ref['bytes'],ref['mtime_ns']): raise ValueError('Prepared split stat changed')
result=dict(created_at=now(),status='one_fixed_OpenJA_group_quantity_failure_closed',actual_identity=r['actual_identity'],
    actual_process_ended=True,config_sha256=sha256(CONFIG),source_result_sha256=sha256(RUN/'result.json'),
    source_group=c['group'],source_rows=r['source_rows'],splits=r['splits'],rejections=r['rejections'],
    amount_screen_passed=False,full80_content_review_performed=False,content_screen_passed=None,
    fixed80_frozen=True,eligible_for_training=False,network_wall_seconds=r['network_wall_seconds'],
    remote_bytes=r['remote_bytes'],CPU_seconds=r['CPU_seconds'],GPU_seconds=0,scientific_teacher_tokens=0,
    optimizer_updates=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
    protected_test_scored=False,quality_criteria_unchanged=True,
    scope='One metadata-selected uniform group of50000 at pinned revision, not full3.24M record corpus quantity/quality. Speaker header removal preserves exact original body byte spans. Meeting-family split and exact-body dedup; no semantic independence/decontamination proof.',
    source_access_identity='Observed exact206 pinned revision/file-size ranges, matching initial header/footer digests; per-range byte hashes preserved. Upstream1.86GB fullblob SHA declared, not independently verified. Local partial bytes remain onWSL and are not published.',
    next_action='Close this fixed group/amount condition; no alternate groups/revision/filter/seed/threshold/epoch/full-download rescue or training. Investigate one unused native same-architecture teacher comparison against existing cached CE without acquiring new data.')
atomic_json(out,result)
paths={Path(__file__).resolve(),CONFIG}
paths.update(report.glob('openja_base*.json'));paths.update(report.glob('openja_base*.xml'))
paths.update((ROOT/'scripts').glob('*openja_base*.py'));paths.update((ROOT/'tests').glob('*openja_base*.py'))
paths.update(RUN.glob('*.json'))
entries=[];target=report/'openja_base_source_evidence.tar.gz'
with target.open('xb') as stream,gzip.GzipFile(fileobj=stream,mode='wb',mtime=0) as compressed,tarfile.open(fileobj=compressed,mode='w|') as tar:
    for path in sorted(paths):
        data=path.read_bytes();name=path.relative_to(ROOT).as_posix();info=tarfile.TarInfo(name);info.size=len(data);info.mtime=0
        tar.addfile(info,io.BytesIO(data));entries.append(dict(path=name,bytes=len(data),sha256=sha256(path)))
manifest=dict(created_at=now(),files=entries,text_files=len(entries),text_bytes=sum(x['bytes'] for x in entries),
    archive=dict(path=str(target),bytes=target.stat().st_size,sha256=sha256(target)),raw_partial_source_kept_on_WSL=True,GPU_seconds=0,Base_complete=False)
atomic_json(report/'openja_base_source_evidence_manifest.json',manifest)
print(json.dumps(dict(status=result['status'],TRAIN_body_tokens=r['splits']['train']['body_tokens'],archive=manifest['archive'],text_files=len(entries))))
