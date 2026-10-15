"""Full supplied DEV and440 integration: synthetic shards/models only."""
import copy
from dataclasses import replace
import json
import math
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from jmicro.continuation_requests import load_requests
from jmicro.experiment import sha256
from jmicro.isolated_continuations import raw_record
from jmicro.isolated_full_dev import (DevCorpusSpec,ReadOnlyDevGuard,
    evaluate_isolated_full_dev,project_corpus,validate_body,validate_corpus)
from jmicro.phase5 import equal_state
from jmicro.shards import Shard
from jmicro.training import rng_state
from test_continuation_requests import fixture
from test_isolated_continuations import Codec


class Model(torch.nn.Module):
    config = dict(max_position_embeddings=1024)

    def __init__(self,first=8,action=None):
        super().__init__()
        self.first,self.action,self.calls = first,action,0
        self.eval()

    def forward(self,current,attention_mask=None,cache=None,use_cache=False):
        self.calls += 1
        if self.action:
            self.action()
        # Uniform body logits give an independent analytic ln(16) oracle.
        logits = torch.zeros((*current.shape,16))
        if attention_mask is None:
            logits[...,self.first if cache is None else 3] = 100.
        return SimpleNamespace(logits=logits,cache=1)


def setup(tmp_path):
    corpus,suite = tmp_path/'corpus',tmp_path/'suite'
    corpus.mkdir()
    suite.mkdir()
    mp,pin,_ = fixture(suite)
    rows,stream = [],[]
    # Cross both context1024 and stride512; unequal byte denominators.
    for i,(count,bytes_) in enumerate(((2,3),(1100,2000))):
        rows.append(dict(doc_id=f'doc-{i}',split='dev',kind='web',offset=len(stream),
            body_tokens=count,bytes=bytes_))
        stream.extend([2]+[8]*count+[3])
    (corpus/'dev.bin').write_bytes(np.asarray(stream,dtype='<u2').tobytes())
    (corpus/'dev.index.json').write_text(json.dumps(rows))
    (corpus/'token_bytes.json').write_text(json.dumps([0]*8+[1]*8))
    details = dict(tokens=len(stream),documents=2,body_bytes=2003,
        stream_sha256=sha256(corpus/'dev.bin'),index_sha256=sha256(corpus/'dev.index.json'))
    manifest = dict(version=1,dtype='<u2',kind='web',tokenizer_sha256='a'*64,
        vocab_size=16,limit_per_split=None,token_bytes_sha256=sha256(corpus/'token_bytes.json'),
        splits=dict(dev=details))
    (corpus/'manifest.json').write_text(json.dumps(manifest))
    for name in ('test.bin','test.index.json','train.bin'):
        (corpus/name).write_text('MALFORMED FAKE TEST/TRAIN SENTINEL')
    (suite/'base.jsonl').write_text('MALFORMED FAKE MIXED SUITE')
    spec = DevCorpusSpec(corpus,sha256(corpus/'manifest.json'),'a'*64,16,2,1102,2003)
    planned,_ = load_requests(mp,pin)
    screen = dict(checkpoint_sha256='c'*64,max_new_tokens=64,outputs=[
        raw_record(r,[8,3],Codec()) for r in planned
        if r.stage == 'standard400' and r.decoding == 'greedy' and r.suppressed])
    binding = dict(checkpoint_sha256='c'*64,config_sha256='d'*64)
    return SimpleNamespace(spec=spec,mp=mp,pin=pin,screen=screen,binding=binding,rows=rows)


def run(f,model=None,check=lambda:None,progress=lambda *args:None):
    return evaluate_isolated_full_dev(model if model is not None else Model(),Codec(),
        f.spec,f.mp,f.pin,f.screen,f.binding,check,progress,device='cpu')


def test_full_actual_component_analytic_body_EOS_all440_exact_reads_and_no_quality_claim(tmp_path):
    f = setup(tmp_path)
    model,before,events = Model(),rng_state(),[]
    result = run(f,model,progress=lambda *args:events.append(args))
    body = result['body']
    assert body['documents'] == 2 and body['body_tokens'] == 1102 and body['body_bytes'] == 2003
    assert [r['scored_body_tokens'] for r in body['rows']] == [2,1100]
    assert math.isclose(body['body_nll'],1102*math.log(16),rel_tol=2e-7)
    assert math.isclose(body['eos_nll'],2*math.log(16),rel_tol=2e-7)
    assert math.isclose(body['bpb'],1102*4/2003,rel_tol=2e-7)
    assert len(result['generation']['outputs']) == 400 and len(result['long_generation']['rows']) == 40
    assert all(r['generated_ids'] == [8,3] for r in result['generation']['outputs'])
    assert result['fixed80_screen_comparison']['passed']
    allowed = {f.spec.directory/n for n in ('manifest.json','dev.bin','dev.index.json','token_bytes.json')}
    allowed.update((f.mp,f.mp.parent/'base.dev.jsonl'))
    assert set(result['evaluation_read_paths']) == {str(p.resolve()) for p in allowed}
    assert events[-1] == ('long40',40,40)
    assert equal_state(before,rng_state()) and not model.training and not model._forward_pre_hooks
    for key in ('TEST_opened','legacy_mixed_suite_opened','project_full_corpus_scored',
                'content_review_completed','qualification_checked','independent_training_checked',
                'Base_qualified','Base_adopted','full_four_item_goal_complete'):
        assert result[key] is False
    assert result['additional_training_tokens'] == 0


@pytest.mark.parametrize('bad',['subset','partial','duplicate','foreign','macroBPB','EOSinBPB','infinity','rowidentity'])
def test_body_audit_rejects_missing_partial_duplicate_foreign_and_wrong_byte_average(tmp_path,bad):
    f = setup(tmp_path)
    body = run(f)['body']
    if bad == 'subset': body['limit_documents'] = 256
    elif bad == 'partial': body['rows'][1]['scored_body_tokens'] -= 1
    elif bad == 'duplicate': body['rows'][1]['doc_id'] = body['rows'][0]['doc_id']
    elif bad == 'foreign': body['split'] = 'test'
    elif bad == 'macroBPB': body['bpb'] = sum(r['body_nll']/math.log(2)/r['body_bytes'] for r in body['rows'])/2
    elif bad == 'EOSinBPB': body['bpb'] = (body['body_nll']+body['eos_nll'])/math.log(2)/body['body_bytes']
    elif bad == 'infinity': body['body_nll'] = body['bpb'] = float('inf')
    else: body['rows'][1]['doc_id'] = 'substituted-document'
    with pytest.raises(ValueError): validate_body(body,f.spec,f.rows)


@pytest.mark.parametrize('bad',['offset','duplicate','split','count','limited','tokenizer'])
def test_original_corpus_index_and_manifest_invariants(tmp_path,bad):
    f = setup(tmp_path)
    shard = Shard(f.spec.directory,'dev')
    if bad == 'offset': shard.index[1]['offset'] += 1
    elif bad == 'duplicate': shard.index[1]['doc_id'] = shard.index[0]['doc_id']
    elif bad == 'split': shard.index[0]['split'] = 'test'
    elif bad == 'count': shard.index[1]['body_tokens'] -= 1
    elif bad == 'limited': shard.manifest['limit_per_split'] = 256
    else: shard.manifest['tokenizer_sha256'] = 'b'*64
    with pytest.raises(ValueError): validate_corpus(shard,f.spec)


@pytest.mark.parametrize('first',[7,9,1])
def test_raw_role_UTF8_UNK_failures_and_six_versus_seven_policy_mismatch_retained(tmp_path,first):
    f = setup(tmp_path)
    result = run(f,Model(first))
    standard = result['generation']['outputs']
    assert not result['fixed80_screen_comparison']['passed']
    assert len(result['fixed80_screen_comparison']['mismatches']) == 80
    if first == 7:
        assert all(r['generated_ids'] == [7,3] and r['role_leak'] for r in standard)
        assert result['raw_failures']['standard400']['role_leak'] == 400
    elif first == 9:
        assert all(r['raw_utf8_hex'] == 'c3' and not r['valid_utf8'] for r in standard)
        assert result['raw_failures']['long40']['unicode'] == 40
    else:
        unsuppressed = [r for r in standard if not r['suppressed']]
        assert all(r['generated_ids'] == [1,3] and r['unknown_id_present'] and not r['valid_utf8'] for r in unsuppressed)
    assert not result['Base_qualified']


@pytest.mark.parametrize('access',['test','write','oswrite'])
def test_read_guard_blocks_test_and_writes_before_contents_or_truncation(tmp_path,access):
    f = setup(tmp_path)
    source = f.spec.directory/'dev.bin'
    original = sha256(source)
    def action():
        if access == 'test': (f.spec.directory/'test.bin').read_bytes()
        elif access == 'write': source.write_bytes(b'overwrite')
        else:
            import os
            os.open(source,os.O_WRONLY|os.O_TRUNC)
    model,before = Model(action=action),rng_state()
    with pytest.raises(ValueError,match='read-only DEV'): run(f,model)
    assert sha256(source) == original and equal_state(before,rng_state())
    assert not model._forward_pre_hooks and not model.training


@pytest.mark.parametrize('bad',['training','checkpoint','manifest','budget','screen'])
def test_invalid_entry_and_expired_budget_rejected_before_model(tmp_path,bad):
    f,model = setup(tmp_path),Model()
    check = lambda:None
    if bad == 'training': model.train()
    elif bad == 'checkpoint': f.binding['checkpoint_sha256'] = 'e'*64
    elif bad == 'manifest': f.mp = f.mp.parent/'base.test.manifest.json'
    elif bad == 'screen': f.screen['outputs'][0]['text'] = 'concealed failure'
    else:
        def check(): raise TimeoutError('expired fixture budget')
    with pytest.raises((ValueError,TimeoutError)): run(f,model,check=check)
    assert model.calls == 0 and not model._forward_pre_hooks


def test_callback_failure_restores_RNG_mode_and_removes_budget_hook(tmp_path):
    f,model = setup(tmp_path),Model()
    before = rng_state()
    def fail(*args):
        torch.rand(1)
        model.train()
        raise TimeoutError('fixture callback interruption')
    with pytest.raises(TimeoutError): run(f,model,progress=fail)
    assert equal_state(before,rng_state()) and not model.training and not model._forward_pre_hooks


def test_fixture_or_narrow_counts_cannot_claim_original_project_fullDEV(tmp_path):
    f = setup(tmp_path)
    original = project_corpus(f.spec.directory)
    assert original.project_identity and original.documents == 89416
    assert original.body_tokens == 42003934 and original.body_bytes == 164344743
    assert not f.spec.project_identity and not replace(original,documents=256).project_identity


def test_direct_guard_only_permitted_read_and_deactivates_after_exception(tmp_path):
    allowed = tmp_path/'allowed'
    allowed.write_text('original')
    guard = ReadOnlyDevGuard((tmp_path,),(allowed,))
    with pytest.raises(ValueError):
        with guard:
            assert allowed.read_text() == 'original'
            (tmp_path/'forbidden').read_bytes()
    assert not guard.active and guard.paths == [str(allowed.resolve())]
