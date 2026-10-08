"""Enrich the already-verified first640 consumed windows with indexed provenance."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src')]
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json


def main():
    started=time.monotonic();phase=ROOT/'reports/phase6'
    destination=phase/'base_residual_consumed_unit_provenance.json'
    if destination.exists(): raise ValueError('Preserve existing consumed-unit diagnosis')
    prepared=read_json(phase/'base_residual_train_dev_history_preparation.json')
    trained=read_json(Path(prepared['training_record']['path']))
    if sha256(Path(prepared['training_record']['path']))!=prepared['training_record']['sha256']:
        raise ValueError('Same actual completed2B training record required')
    paths=list(Path(trained['checkpoint']).parent.glob('metrics-*.jsonl'))
    if len(paths)!=1: raise ValueError('Unambiguous actual committed history required')
    binding=prepared['source_binding'];index=Path(binding['pool'])/'train.index.jsonl'
    stat=index.stat()
    if (stat.st_size,stat.st_mtime_ns)!=(binding['index_size'],binding['index_mtime_ns']):
        raise ValueError('Accepted index identity differs; no scan fallback')
    units={}; windows=[];kind_teachers=Counter();source_teachers=Counter();web_paragraph=web_omitted=web_total=0
    with paths[0].open() as metrics,index.open('rb') as handle:
        for expected in prepared['completed_history_prefix']:
            actual=json.loads(metrics.readline())
            if actual['update']!=expected['update'] or actual['token_digest']!=expected['token_digest']:
                raise ValueError('Already-verified completed history prefix differs')
            for position,digest,first,end,teachers in actual['draw_trace']:
                if time.monotonic()-started>=30: raise TimeoutError('CPU provenance30-second cap exhausted')
                if position not in units:
                    handle.seek(position);raw=handle.readline(16385)
                    if not raw or len(raw)>16384 or hashlib.sha256(raw).hexdigest()!=digest:
                        raise ValueError('Actual emitted source index row differs')
                    row=json.loads(raw)
                    if row['split']!='train': raise ValueError('Actual TRAIN provenance required')
                    units[position]=dict(index_byte_position=position,index_record_sha256=digest,
                        source=row['source'],unit_kind=row['unit_kind'],body_tokens=row['body_tokens'],
                        canonical_sha256=row['canonical_sha256'],source_family=row['source_family'],
                        source_char_start=row.get('source_char_start'),source_char_end=row.get('source_char_end'),
                        paragraph_position=row.get('paragraph_position'),source_start=row.get('source_start'),
                        source_end=row.get('source_end'),source_manifest_sha256=row.get('source_manifest_sha256'))
                row=units[position]
                if row['index_record_sha256']!=digest: raise ValueError('Consumed source row digest changed')
                key=row['source']+':'+row['unit_kind'];kind_teachers[key]+=teachers;source_teachers[row['source']]+=teachers
                if row['source']=='web':
                    web_total+=teachers
                    if row['unit_kind'].startswith('intact-'): web_paragraph+=teachers
                    if row['source_char_start'] is not None and row['source_char_start']>0: web_omitted+=teachers
                windows.append(dict(update=actual['update'],index_byte_position=position,source=row['source'],
                    unit_kind=row['unit_kind'],target_first=first,target_end=end,teacher_tokens=teachers))
    web=[r for r in units.values() if r['source']=='web']
    distinct_kinds=Counter(r['source']+':'+r['unit_kind'] for r in units.values())
    length_groups=Counter('64..128' if r['body_tokens']<=128 else '129..256' if r['body_tokens']<=256
                          else '257..512' if r['body_tokens']<=512 else '513..1024' for r in web)
    if len(windows)!=640 or sum(source_teachers.values())!=sum(r['teachers'] for r in prepared['completed_history_prefix']):
        raise ValueError('Exactly all640 original consumed windows/teacher total required')
    elapsed=time.monotonic()-started
    atomic_json(destination,dict(status='CPU_consumed_index_provenance_complete',created_at=now(),CPU_seconds=elapsed,
        source_sha256=sha256(Path(__file__)),preparation_sha256=sha256(phase/'base_residual_train_dev_history_preparation.json'),
        source_binding=binding,actual_completed_updates=8,actual_windows=640,distinct_original_units=len(units),
        teacher_tokens_by_source=dict(source_teachers),teacher_tokens_by_source_and_unit_kind=dict(kind_teachers),
        distinct_units_by_source_and_kind=dict(distinct_kinds),distinct_Web_body_length_bins=dict(length_groups),
        Web_teachers=web_total,Web_paragraph_unit_teachers=web_paragraph,
        Web_paragraph_unit_teacher_fraction=web_paragraph/web_total,
        Web_noninitial_source_slice_teachers=web_omitted,Web_noninitial_source_slice_teacher_fraction=web_omitted/web_total,
        original_source_span_bounds_available=sum(r['source_start'] is not None and r['source_end'] is not None for r in web),
        units=list(units.values()),windows=windows,scientific_teacher_tokens=0,optimizer_updates=0,GPU_seconds=0,
        Base_complete=False,Chat_started=False,quantization_started=False,
        interpretation='Metadata enrichment of the already-bound initial actual updates, not a global corpus/near-duplicate/content audit. Paragraph-unit prevalence and omitted context do not themselves establish a cause of poor generation. Original source offsets enable a separate bounded same-target context diagnostic without rescanning the corpus.'))
    print(json.dumps(dict(CPU_seconds=elapsed,actual_windows=640,distinct_units=len(units),
        teacher_kind=dict(kind_teachers),distinct_Web_lengths=dict(length_groups),
        Web_paragraph_teacher_fraction=web_paragraph/web_total,Web_noninitial_slice_teacher_fraction=web_omitted/web_total)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
