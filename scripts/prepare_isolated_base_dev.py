"""Export DEV inputs from already-stored DEV80, without opening mixed/TEST files."""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from jmicro.evaluation_boundary import (MANIFEST_NAME,CASES_NAME,KIND,digest,
    identity_digest,validate_cases,load_dev_suite,validate_dev_outputs)

SOURCE=ROOT/'reports/phase6/base-document-balance-comparison-20261014/evaluation/document_balance/evaluation/generation.json'
SOURCE_SHA='1221a1bdbe6023f2abc6bd122352052a9065bb16af3c90ccd5d57c93c3137f6a'
OUTPUT=ROOT/'eval/isolated-base-dev-v1'


def prepare():
    if OUTPUT.exists(): raise ValueError('Preserve the first pinned isolated DEV export')
    raw=SOURCE.read_bytes()
    if digest(raw)!=SOURCE_SHA: raise ValueError('Previously audited DEV-only generation differs')
    generation=json.loads(raw)
    rows=generation['outputs']
    if len(rows)!=80 or any(row['split']!='dev' for row in rows):
        raise ValueError('Export only the previously reviewed80 DEV rows')
    cases=[{k:r[k] for k in ('id','category','prefix','split')} for r in rows]
    validate_cases(cases)
    payload=''.join(json.dumps(c,ensure_ascii=False,separators=(',',':'))+'\n' for c in cases).encode()
    manifest=dict(kind=KIND,version=1,split='dev',cases_file=CASES_NAME,cases_sha256=digest(payload),
        case_count=80,case_identity_sha256=identity_digest(cases),source_generation_sha256=SOURCE_SHA,
        source_legacy_suite_sha256=generation['suite_sha256'],TEST_read_for_export=False)
    OUTPUT.mkdir(parents=True)
    (OUTPUT/CASES_NAME).write_bytes(payload)
    blob=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
    (OUTPUT/MANIFEST_NAME).write_bytes(blob)
    suite=load_dev_suite(OUTPUT/MANIFEST_NAME,digest(blob))
    assert validate_dev_outputs(rows,suite)
    receipt=dict(status='fixed80_DEV_exported_from_previously_audited_DEV_outputs',
        manifest_sha256=digest(blob),cases_sha256=digest(payload),case_identity_sha256=identity_digest(cases),
        original_DEV_prefix_and_category_identity_verified=True,source_generation_sha256=SOURCE_SHA,
        source_legacy_suite_sha256=generation['suite_sha256'],case_count=80,
        legacy_mixed_suite_opened=False,TEST_opened=False,TEST_parsed=False,
        generated_answers_exported=False,new_quality_evidence=False,GPU_work=False,
        opened_paths=[str(SOURCE),*suite.opened_paths])
    record=ROOT/'reports/phase6/evaluation-boundary-20261015/dev_export.json'
    record.parent.mkdir(parents=True,exist_ok=True)
    record.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(receipt,ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();parser.parse_args();prepare()
