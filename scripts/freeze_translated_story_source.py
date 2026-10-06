"""Freeze native source/exclusions/selection before actual fixed64 preparation."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from prepare_translated_story_source import RUN,PROPOSAL,FREEZE,SOURCES


def reference(path):return dict(path=str(path),sha256=sha256(path))


def main():
    if FREEZE.exists() or (RUN/'job.json').exists():raise ValueError('Preserve fixed/partial preparation; no refreeze')
    p=read_json(PROPOSAL);source=p['source'];refs={k:v for k,v in source.items() if isinstance(v,dict) and 'path' in v}
    for number,record_ref in enumerate(p['preparation']['inspected_calibration_sources']):refs[f'calibration_{number}']=record_ref
    ancestry_path=ROOT/'reports/phase6/natural_story_ancestry_result.json'
    refs['mixed_pilot_ancestry']=reference(ancestry_path)
    for name in ('root_cause_corpus.json','root_cause_cases.json'):
        refs[name]=reference(ROOT/'reports/phase6'/name)
    for record_ref in refs.values():
        if sha256(Path(record_ref['path']))!=record_ref['sha256']:raise ValueError('Fixed source/calibration input differs')
    tests=ROOT/'reports/phase6/translated_story_source_tests.xml';suite=ET.parse(tests).getroot().find('testsuite')
    if int(suite.attrib['tests'])!=3 or any(int(suite.attrib[k]) for k in ('errors','failures','skipped')):
        raise ValueError('Three passing boundary/exclusion/native stream tests required')
    offsets=set();hashes=set()
    current=read_json(Path(refs['calibration_0']['path']))
    ancestor={r['id']:r for r in read_json(ancestry_path)['rows']}
    for row in current['rows']:
        origin=ancestor[row['id']]
        if origin['text_sha256']!=row['text_sha256']:raise ValueError('Original prior64 ancestry differs')
        offsets.add(origin['upstream_metadata']['offset']);hashes.add(row['text_sha256'])
    for row in read_json(Path(refs['calibration_1']['path']))['rows']:
        offsets.add(row['offset']);hashes.add(row['text_sha256'])
    for row in read_json(Path(refs['calibration_2']['path']))['reviews']:
        if row['source']=='story':
            if row['source_manifest_sha256']!=source['manifest']['sha256']:raise ValueError('Prior mixture story origin differs')
            offsets.add(row['source_start']);hashes.add(row['canonical_sha256'])
    for name in ('root_cause_corpus.json','root_cause_cases.json'):
        for row in read_json(Path(refs[name]['path'])):
            if row['source']=='story200m':
                offsets.add(row['offset']);hashes.add(row['text_sha256'])
    index=Path(source['native_pool'])/'train.index.jsonl';stat=index.stat()
    atomic_json(FREEZE,dict(status='original_translation_source_view_inputs_exclusions_seed_frozen_before_actual64',created_at=now(),
        proposal_sha256=sha256(PROPOSAL),source_sha256={s:sha256(ROOT/s) for s in SOURCES},references=refs,
        tests=dict(path=str(tests),sha256=sha256(tests),count=3,CPU_seconds=float(suite.attrib['time']),GPU_seconds=0),
        native_index_size_and_mtime_ns=[stat.st_size,stat.st_mtime_ns],
        excluded_native_offsets=sorted(offsets),excluded_text_sha256=sorted(hashes),
        supplemental_earlier_root64_and_train32_calibration_excluded=True,
        source_interval=source['native_translation_serialized_interval'],seed=2026100693,CPU_ceiling_seconds=60,
        actual_pilot_not_created_or_read=True,scientific_teacher_tokens=0,GPU_seconds=0,
        Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False))
    print(dict(status='frozen',excluded_original_offsets=len(offsets),excluded_texts=len(hashes),tests=3))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
