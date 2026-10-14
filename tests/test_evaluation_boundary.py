import copy
import json
from pathlib import Path
from unittest.mock import patch

import pytest
import jmicro.evaluation_boundary as boundary


def prepared(tmp_path):
    cases=[dict(id=f'base-{i:03d}',category='fixture',prefix=f'例{i}の続きを',split='dev') for i in range(1,81)]
    payload=''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in cases).encode()
    (tmp_path/boundary.CASES_NAME).write_bytes(payload)
    manifest=dict(kind=boundary.KIND,version=1,split='dev',cases_file=boundary.CASES_NAME,
        cases_sha256=boundary.digest(payload),case_count=80,case_identity_sha256=boundary.identity_digest(cases),
        source_generation_sha256='1'*64,source_legacy_suite_sha256='2'*64,TEST_read_for_export=False)
    blob=json.dumps(manifest).encode()
    path=tmp_path/boundary.MANIFEST_NAME
    path.write_bytes(blob)
    return path,boundary.digest(blob),cases,manifest


def guard_reads(allowed):
    original=Path.open
    observed=[]
    def guarded(path,*args,**kwargs):
        if path not in allowed: raise AssertionError('Unauthorized evaluation read: '+str(path))
        observed.append(str(path))
        return original(path,*args,**kwargs)
    return guarded,observed


def test_dev_and_content_review_never_open_broken_or_sentinel_TEST(tmp_path):
    path,pin,cases,_=prepared(tmp_path)
    (tmp_path/'base.sealed.test.jsonl').write_text('INVALID JSON SECRET_TEST_SENTINEL')
    (tmp_path/'base.jsonl').write_text('MIXED_SUITE_MUST_NOT_BE_OPENED')
    guarded,observed=guard_reads({path,tmp_path/boundary.CASES_NAME})
    with patch.object(Path,'open',guarded):
        suite=boundary.load_dev_suite(path,pin)
        assert boundary.validate_dev_outputs(cases,suite)
    assert observed==[str(path),str(tmp_path/boundary.CASES_NAME)]
    assert len(suite.cases)==80


@pytest.mark.parametrize('name',['base.jsonl','base.test.manifest.json','base.sealed.test.jsonl'])
def test_wrong_entry_path_is_rejected_before_any_open(tmp_path,name):
    path=tmp_path/name
    path.write_text('POISON_TEST_BODY')
    with patch.object(Path,'open',side_effect=AssertionError('No file may be opened')):
        with pytest.raises(ValueError):boundary.load_dev_suite(path,'1'*64)


def test_wrong_manifest_pin_rejects_before_JSON_parsing(tmp_path):
    path,_,_,_=prepared(tmp_path)
    with patch.object(boundary.json,'loads',side_effect=AssertionError('No JSON parsing')):
        with pytest.raises(ValueError):boundary.load_dev_suite(path,'0'*64)


def test_modified_dev_payload_containing_TEST_rejects_before_case_parser(tmp_path):
    path,pin,_,_=prepared(tmp_path)
    (tmp_path/boundary.CASES_NAME).write_text('{"split":"test","prefix":"POISON"}\n')
    original=boundary.json.loads
    parsed=[]
    def guarded(value,*args,**kwargs):
        parsed.append(value)
        assert b'POISON' not in value if isinstance(value,bytes) else 'POISON' not in value
        return original(value,*args,**kwargs)
    with patch.object(boundary.json,'loads',guarded):
        with pytest.raises(ValueError):boundary.load_dev_suite(path,pin)
    assert len(parsed)==1  # Metadata only; altered case contents never parsed.


@pytest.mark.parametrize('mutation',['split','path','extra_path','count','TEST_export'])
def test_bad_manifest_schema_rejects_before_case_file_open(tmp_path,mutation):
    path,_,_,manifest=prepared(tmp_path)
    if mutation=='split':manifest['split']='test'
    if mutation=='path':manifest['cases_file']='../base.sealed.test.jsonl'
    if mutation=='extra_path':manifest['TEST_path']='base.sealed.test.jsonl'
    if mutation=='count':manifest['case_count']=79
    if mutation=='TEST_export':manifest['TEST_read_for_export']=True
    blob=json.dumps(manifest).encode();path.write_bytes(blob)
    guarded,observed=guard_reads({path})
    with patch.object(Path,'open',guarded):
        with pytest.raises(ValueError):boundary.load_dev_suite(path,boundary.digest(blob))
    assert observed==[str(path)]


def test_symlink_entry_and_payload_reject_without_opening_target(tmp_path):
    path,pin,_,_=prepared(tmp_path)
    link=tmp_path/'links';link.mkdir()
    symlink=link/boundary.MANIFEST_NAME;symlink.symlink_to(path)
    with patch.object(Path,'open',side_effect=AssertionError('No target open')):
        with pytest.raises(ValueError):boundary.load_dev_suite(symlink,pin)
    payload=tmp_path/boundary.CASES_NAME;payload.unlink()
    payload.symlink_to(tmp_path/'base.sealed.test.jsonl')
    guarded,_=guard_reads({path})
    with patch.object(Path,'open',guarded):
        with pytest.raises(ValueError):boundary.load_dev_suite(path,pin)


@pytest.mark.parametrize('mutation',['missing','duplicate','prefix','category','split'])
def test_content_review_refuses_mismatched_actual_outputs(tmp_path,mutation):
    path,pin,cases,_=prepared(tmp_path);suite=boundary.load_dev_suite(path,pin)
    rows=copy.deepcopy(cases)
    if mutation=='missing':rows.pop()
    if mutation=='duplicate':rows[-1]=rows[0].copy()
    if mutation=='prefix':rows[0]['prefix']='別のprefix'
    if mutation=='category':rows[0]['category']='別のcategory'
    if mutation=='split':rows[0]['split']='test'
    with pytest.raises(ValueError):boundary.validate_dev_outputs(rows,suite)
