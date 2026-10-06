"""Grounding, leakage and actual stream protocol; no GPU-quality claim."""
import copy
import json
from pathlib import Path
import sys
import numpy as np
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from condition_transfer_curriculum import CATEGORIES, KIND, TRAIN_NAMES, SEED, generate, validate_split, render, digest, CurriculumTrainView
from prepare_condition_transfer_curriculum import encode_probes, check_dev_leakage, validate_single_repair
from prepare_condition_positive_teachers import outcome_token_mask
from condition_positive_trainer import PositiveStream
from jmicro.experiment import ROOT,sha256
from jmicro.tokenizer import Tokenizer


def fixed(category):
    return dict(category=category,A='あかね',B='ひなた',item='りんご',unit='個',object='パン',
        positive='食べた',negative='食べていない',x=10,delta=3,hour=12,duration=2,
        activity='読書',length=10,gap=4,sequence='先')


def test_all_six_opposed_local_states_have_expected_literal_outcomes_and_constraints():
    expected=dict(negation=['あかねは今朝、パンを食べた。','あかねは今朝、パンを食べていない。'],
        quantity=['13個である。','7個である。'],time=['10時になった。','14時になった。'],
        comparison=['あかねである。','ひなたである。'],entity_reference=['あかねである。','ひなたである。'],
        causality=['ライトは点灯している。','ライトは消えている。'])
    for cat in CATEGORIES:
        for form in range(6):
            pair=[render(fixed(cat),form,b) for b in (0,1)]
            assert all(v['choices']==expected[cat] for v in pair)
            assert pair[0]['label']==0 and pair[1]['label']==1
            assert pair[0]['prefix']!=pair[1]['prefix']
            if cat=='quantity':
                assert ('3個を加えた' if form != 1 else '3個を受け取った') in pair[0]['prefix']
                assert '3個を取り出した' in pair[1]['prefix'] or '3個を渡した' in pair[1]['prefix']
                assert 'そこへ3個を取り出した' not in pair[1]['prefix']
            if cat=='comparison':
                assert 'あかねの棒は14センチ' in pair[0]['prefix']
                assert 'ひなたの棒は14センチ' in pair[1]['prefix']
    # Reversing presentation order must leave the logical winner unchanged.
    f=fixed('comparison');f['sequence']='後'
    assert render(f,0,0)['choices'][0]=='あかねである。'
    assert render(f,0,0)['prefix'].startswith('ひなたの棒は10センチ')


def test_fixed2048_source128_is_reproducible_diverse_and_rejects_split_leaks():
    groups,rows=generate();second,second_rows=generate()
    assert groups==second and rows==second_rows
    assert all(validate_split(groups,rows).values())
    assert len({r['template_id'] for r in rows[:64]})==24
    assert {r['label'] for r in rows}=={0,1}
    assert all(r['outcome'] in r['choices'] and r['text'].endswith('。') for r in rows)
    bad=copy.deepcopy(groups);bad['lexical_holdout'][0]['facts']['A']=TRAIN_NAMES[0]
    with pytest.raises(ValueError,match='Lexical entity'):validate_split(bad,rows)
    bad=copy.deepcopy(groups);bad['structural_holdout'][0]['template_id']=rows[0]['template_id']
    with pytest.raises(ValueError,match='Structural template'):validate_split(bad,rows)


def test_observed_single_grammar_repair_keeps_real_v1_facts_labels_and_all_holdouts():
    groups,rows=generate();proof=validate_single_repair(groups,rows)
    assert proof['changed_train_documents']==86 and proof['fixed_first64_ids_unchanged']
    assert all('その内容は、' not in r['text'] for r in rows)
    changed=copy.deepcopy(rows);changed[0]['choices'][0]='無関係な答え。'
    with pytest.raises(ValueError,match='states/labels/IDs'):validate_single_repair(groups,changed)


def test_actual_native_codec_common_probe_targets_and_focus_byte_spans():
    tokenizer=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');groups,rows=generate()
    probes=encode_probes(groups,tokenizer)
    assert len(probes['cases'])==512 and len(probes['families'])==128
    for i in range(0,512,4):
        left,right=probes['cases'][i:i+2],probes['cases'][i+2:i+4]
        assert [v['target_ids'] for v in left]==[v['target_ids'] for v in right]
        assert left[0]['label']==0 and right[0]['label']==1
    for row in rows[:64]:
        ids=tokenizer.encode(row['text']);mask=outcome_token_mask(row['text'],ids,tokenizer,[row])
        assert tokenizer.decode_bytes(ids)==row['text'].encode()
        assert mask.any() and not mask[0] and not mask[-1]
    # Include non-ASCII names and byte pieces; no reference to whole-corpus index.
    assert check_dev_leakage(rows,groups,ROOT/'reports/phase6/condition-source-learning-100m-20261006')['previous_dev80_and192_literal_contexts_absent']


def test_generated_provenance_view_requires_acceptance_and_actual_stream_cursor_resumes(tmp_path):
    # Real native codec2048 small bodies exercises validation and byte/EOS boundary handling.
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');body=tok.encode('あかねはパンを食べた。')
    ids=np.asarray(([2,*body,3])*2048,dtype='<u2');length=len(body)+2
    np.savez(tmp_path/'train.npz',tokens=ids,focus=np.zeros(len(ids),dtype=np.uint8),
        offsets=np.arange(2048,dtype='<i8')*length,lengths=np.full(2048,length,dtype='<i4'))
    manifest=dict(kind=KIND,source='local_programmatic_Japanese',documents=2048,newly_prepared_original_corpus_tokens=0,
        arrays_sha256=sha256(tmp_path/'train.npz'),tokenizer_sha256=sha256(tok.path),serialized_tokens=len(ids),outcome_focus_body_targets=0,
        pilot_sha256='not_yet_reviewed')
    (tmp_path/'manifest.json').write_text(json.dumps(manifest));msha=sha256(tmp_path/'manifest.json')
    with pytest.raises(FileNotFoundError):CurriculumTrainView(tmp_path,msha)
    view=CurriculumTrainView(tmp_path,msha,require_accepted=False)
    original=PositiveStream(view,42);original.block(31);cursor=original.state_dict()
    expected=original.block(87);resumed=PositiveStream(view,42);resumed.load_state_dict(cursor)
    actual=resumed.block(87)
    assert all(np.array_equal(a,b) for a,b in zip(expected,actual,strict=True))
    assert 3 in actual[1] and -100 in actual[1]
    cursor['manifest_sha256']='changed'
    with pytest.raises(ValueError,match='identity/cursor'):resumed.load_state_dict(cursor)
    manifest['kind']='original_train_positive_condition_outcome_spans'
    (tmp_path/'manifest.json').write_text(json.dumps(manifest))
    with pytest.raises(ValueError,match='Generated provenance'):CurriculumTrainView(tmp_path,sha256(tmp_path/'manifest.json'),require_accepted=False)
