"""Cache parity and counter/budget guards; fixtures are not GPU evidence."""
import copy
import json
from types import SimpleNamespace
import sys

import numpy as np
import pytest
from jmicro.experiment import ROOT,sha256,write_json

sys.path.insert(0,str(ROOT/'scripts'))
from cached_three_source_index import CachedThreeSourceIndex
from textbook_quantity_trainer import ThreeSourceIndex
from run_sequence_objective_low_alpha import estimate_training
from review_sequence_objective_low_alpha import matched_scientific_counters


def view(tmp_path):
    rows=[dict(offset=0,body_tokens=3,split='train',source='web'),
          dict(offset=5,body_tokens=2,split='train',source='textbook'),
          dict(offset=9,body_tokens=1,split='train',source='story')]
    path=tmp_path/'train.index.jsonl';path.write_text(''.join(json.dumps(r)+'\n' for r in rows))
    manifest=dict(splits=dict(train=dict(documents=3,tokens=12,index_sha256=sha256(path))))
    write_json(tmp_path/'manifest.json',manifest)
    return SimpleNamespace(directory=tmp_path,manifest=manifest,tokens=np.zeros(12,dtype='<u2'))


def test_cache_arrays_and_order_equal_original_and_reuse_without_reparse(tmp_path,monkeypatch):
    v=view(tmp_path);original=ThreeSourceIndex(v);cached=CachedThreeSourceIndex(v)
    assert not cached.cache_reused
    for name in ('offsets','lengths','sources'):assert np.array_equal(getattr(original,name),getattr(cached,name))
    for i in range(3):assert original[i]==cached[i]
    from pathlib import Path
    original_open=Path.open
    def guarded(path,*args,**kwargs):
        if path.name=='train.index.jsonl':pytest.fail('Cached load reopened large index')
        return original_open(path,*args,**kwargs)
    monkeypatch.setattr(Path,'open',guarded)
    assert CachedThreeSourceIndex(v).cache_reused


def test_cache_corruption_rejected(tmp_path):
    v=view(tmp_path);CachedThreeSourceIndex(v)
    file=next(tmp_path.glob('.compact-index-*/sources.npy'));file.write_bytes(b'broken')
    with pytest.raises(ValueError,match='checksum'):CachedThreeSourceIndex(v)


def test_changed_source_identity_rejected(tmp_path):
    v=view(tmp_path);CachedThreeSourceIndex(v)
    with (tmp_path/'train.index.jsonl').open('a') as stream:stream.write('extra')
    with pytest.raises(ValueError,match='identity'):CachedThreeSourceIndex(v)


def test_first_parse_rejects_wrong_boundaries_without_ready_record(tmp_path):
    v=view(tmp_path);v.manifest['splits']['train']['tokens']=13;v.tokens=np.zeros(13,dtype='<u2')
    with pytest.raises(ValueError,match='checksum/size/count'):CachedThreeSourceIndex(v)
    assert not list(tmp_path.glob('.compact-index-*/ready.json'))


def test_estimate_includes_three_rollout_cycles_and_rejects_partial():
    rows=[dict(seconds=100. if i<4 else (1.2 if i%4==3 else .1)) for i in range(16)]
    timing=dict(histories=rows,verification_teacher_tokens=160000)
    measured,estimate=estimate_training(timing)
    assert measured['updates']==2500 and measured['estimated_training_seconds']==937.5
    assert estimate==937.5*1.3+480
    with pytest.raises(AssertionError):estimate_training(dict(timing,histories=rows[:-1]))


@pytest.mark.parametrize('changed',['source_tokens','short','token_digest'])
def test_reused_control_counter_or_digest_mismatch_rejected(changed):
    control=dict(sampler={k:dict(value=1) for k in ('source_teachers','source_tokens','source_physical_tokens',
        'source_eos','genre_teachers','genre_eos','short')},token_digest='same')
    candidate=copy.deepcopy(control)
    if changed=='token_digest':candidate[changed]='changed'
    else:candidate['sampler'][changed]['value']=2
    with pytest.raises(ValueError,match='differs'):matched_scientific_counters(control,candidate)
