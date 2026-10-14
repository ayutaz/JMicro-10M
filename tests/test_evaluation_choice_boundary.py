"""Hash/schema/read isolation without actual held-out TEST contents."""
import hashlib
import json
from pathlib import Path
from unittest.mock import patch
import pytest
from jmicro.evaluation_choice_boundary import COUNTS,WIDTHS,MANIFEST_NAME,load_choices


def fixture(tmp_path):
    manifest=dict(kind='isolated_previously_observed_Japanese_diagnostics_v1',
        project_role='dev_fixed_diagnostics',tasks={},TEST_read_for_export=False)
    for task,count in COUNTS.items():
        rows=[dict(id=str(i),family=str(i),category='fixture',context='',choices=['文']*WIDTHS[task],label=0) for i in range(count)]
        raw=''.join(json.dumps(r)+'\n' for r in rows).encode();name=task+'.dev.jsonl'
        (tmp_path/name).write_bytes(raw)
        manifest['tasks'][task]=dict(file=name,count=count,sha256=hashlib.sha256(raw).hexdigest(),source_sha256='a'*64)
    path=tmp_path/MANIFEST_NAME;path.write_text(json.dumps(manifest))
    return path,hashlib.sha256(path.read_bytes()).hexdigest(),manifest


@pytest.mark.parametrize('task',list(COUNTS))
def test_each_task_reads_only_manifest_and_its_own_input_file(tmp_path,task):
    path,pin,_=fixture(tmp_path);(tmp_path/'test.jsonl').write_text('BROKEN_TEST')
    allowed={path,tmp_path/(task+'.dev.jsonl')};original=Path.open;seen=[]
    def guarded(p,*args,**kwargs):
        if p not in allowed:raise AssertionError('Unexpected file read')
        seen.append(p);return original(p,*args,**kwargs)
    with patch.object(Path,'open',guarded):rows,provenance=load_choices(path,pin,task)
    assert len(rows)==COUNTS[task] and seen==[path,tmp_path/(task+'.dev.jsonl')]
    assert provenance['TEST_opened']is False


def test_wrong_entry_and_hash_rejected_before_case_read(tmp_path):
    path,pin,_=fixture(tmp_path)
    with patch.object(Path,'open',side_effect=AssertionError('Must not open TEST')):
        with pytest.raises(ValueError):load_choices(tmp_path/'test.manifest.json',pin,'semantics')
    with pytest.raises(ValueError):load_choices(path,'0'*64,'semantics')


@pytest.mark.parametrize('bad',['path','count','TEST_flag','extra'])
def test_bad_manifest_cannot_open_payload(tmp_path,bad):
    path,_,m=fixture(tmp_path)
    if bad=='path':m['tasks']['semantics']['file']='test.jsonl'
    elif bad=='count':m['tasks']['semantics']['count']=191
    elif bad=='TEST_flag':m['TEST_read_for_export']=True
    else:m['TEST_path']='test.jsonl'
    path.write_text(json.dumps(m));pin=hashlib.sha256(path.read_bytes()).hexdigest()
    original=Path.open
    def guarded(p,*args,**kwargs):
        if p!=path:raise AssertionError('Must reject before payload')
        return original(p,*args,**kwargs)
    with patch.object(Path,'open',guarded):
        with pytest.raises(ValueError):load_choices(path,pin,'semantics')


@pytest.mark.parametrize('bad',['changed_bytes','duplicate_ID','prediction_field','invalid_label'])
def test_corrupt_inputs_and_model_output_fields_rejected(tmp_path,bad):
    path,pin,m=fixture(tmp_path);cases=tmp_path/'semantics.dev.jsonl'
    rows=[json.loads(line) for line in cases.read_bytes().splitlines()]
    if bad=='duplicate_ID':rows[1]['id']=rows[0]['id']
    elif bad=='prediction_field':rows[0]['prediction']=0
    elif bad=='invalid_label':rows[0]['label']=True
    else:rows[0]['context']='改変'
    raw=''.join(json.dumps(r)+'\n' for r in rows).encode();cases.write_bytes(raw)
    if bad!='changed_bytes':
        m['tasks']['semantics']['sha256']=hashlib.sha256(raw).hexdigest()
        path.write_text(json.dumps(m));pin=hashlib.sha256(path.read_bytes()).hexdigest()
    with pytest.raises(ValueError):load_choices(path,pin,'semantics')


def test_symlink_entry_rejected(tmp_path):
    path,pin,_=fixture(tmp_path);other=tmp_path/'linked';other.mkdir()
    link=other/MANIFEST_NAME;link.symlink_to(path)
    with pytest.raises(ValueError):load_choices(link,pin,'semantics')
