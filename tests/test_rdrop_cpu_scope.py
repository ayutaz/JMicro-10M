"""CLI path/type and one-shot boundaries fail before model/data access."""
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import prepare_rdrop as assay
from jmicro.rdrop import POLICY


def contract():
    return dict(kind='native_original10M_normalized_RDrop_CPU_assay_v1',CPU_wall_ceiling_seconds=30,
        native_parameters=10001152,training_parameters=10001152,input_shape=[2,64],cache_split=[32,32],
        borrowed_selected_spans=[[512,576],[576,640]],GPU_seconds=0,optimizer_updates=0,
        cache_atol=3e-5,cache_rtol=2e-5,policy=POLICY,seed=42)


def test_CLI_string_path_gets_scope_error_instead_of_hash_attribute_failure(tmp_path,monkeypatch):
    monkeypatch.setenv('CUDA_VISIBLE_DEVICES','')
    path = tmp_path/'bad.json'
    path.write_text('{}')
    with pytest.raises(ValueError,match='scope required'):
        assay.run(str(path),assay.sha256(path))


def test_nonCPU_environment_rejected_without_reading_even_missing_config(tmp_path,monkeypatch):
    monkeypatch.setenv('CUDA_VISIBLE_DEVICES','0')
    with pytest.raises(ValueError,match='CPU-only'):
        assay.run(str(tmp_path/'missing.json'),'0'*64)


def test_external_pin_mismatch_rejected_before_model_config_read(tmp_path,monkeypatch):
    monkeypatch.setenv('CUDA_VISIBLE_DEVICES','')
    path = tmp_path/'bad.json'
    path.write_text('{}')
    with pytest.raises(ValueError,match='CPU-only'):
        assay.run(str(path),'0'*64)


@pytest.mark.parametrize('case',['existing','outside','changed_geometry'])
def test_one_shot_output_and_geometry_refused_before_source_or_parent_reads(tmp_path,monkeypatch,case):
    monkeypatch.setenv('CUDA_VISIBLE_DEVICES','')
    monkeypatch.setattr(assay,'ROOT',tmp_path)
    c = contract()
    output = tmp_path/'reports/phase6/assay.json'
    c['output'] = 'reports/phase6/assay.json'
    if case == 'existing':
        output.parent.mkdir(parents=True)
        output.write_text('preserved')
    elif case == 'outside': c['output'] = str(tmp_path.parent/'outside.json')
    else: c['input_shape'] = [2,32]
    path = tmp_path/'config.json'
    path.write_text(json.dumps(c))
    with pytest.raises(ValueError): assay.run(str(path),assay.sha256(path))
    if case == 'existing': assert output.read_text() == 'preserved'
