"""Local truth, controlled replacement and actual native stream/codec evidence."""
import copy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import pytest
import numpy as np
from condition_relation_language import render, generate, validate_replacement, CONTROL_DATA, PAST_NEGATIVE
from prepare_condition_transfer_curriculum import encode_probes
from prepare_condition_positive_teachers import outcome_token_mask
from condition_positive_trainer import PositiveStream
from jmicro.experiment import ROOT, read_json
from jmicro.tokenizer import Tokenizer


def fact(category):
    return dict(category=category,A='あかね',B='ひなた',item='りんご',unit='個',object='パン',
        positive='食べた',negative='食べていない',x=10,delta=3,hour=12,duration=2,
        activity='読書',length=10,gap=4,sequence='先')


def test_literal_negation_and_relational_direction_not_numeric_name_matching():
    for form in range(6):
        pair=[render(fact('negation'),form,b) for b in (0,1)]
        assert pair[0]['choices']==pair[1]['choices']==['今朝、あかねはパンを食べた。','今朝、あかねはパンを食べなかった。']
        assert pair[0]['local_state']['did_action'] and not pair[1]['local_state']['did_action']
        assert pair[0]['prefix'] != pair[1]['prefix']
        comp=[render(fact('comparison'),form,b) for b in (0,1)]
        assert comp[0]['choices']==comp[1]['choices']==['あかねである。','ひなたである。']
        assert comp[0]['local_state']['A_length']==14 and comp[1]['local_state']['B_length']==14
        assert comp[0]['prefix'].startswith('二本の棒の長さは10センチと14センチである。')
        assert 'あかねの棒は14センチ' not in comp[0]['prefix']
        reversed_fact=fact('comparison');reversed_fact['sequence']='後'
        changed=render(reversed_fact,form,0)
        assert changed['local_state']==comp[0]['local_state']
        assert changed['prefix'].startswith('二本の棒の長さは14センチと10センチである。')
    assert len(PAST_NEGATIVE)==12


def test_actual_accepted_selection_exact_other_four_and_grounding_rejects_tampering():
    old=read_json(CONTROL_DATA/'train-source.json');groups,rows=generate(old)
    again,second=generate(old)
    assert groups==again and rows==second
    proof=validate_replacement(old,groups,rows)
    assert proof['changed_documents']==684
    assert {r['id'] for r in rows[:64]}=={r['id'] for r in old['rows'][:64]}
    assert len({r['template_id'] for r in rows[:64]})==24
    bad=copy.deepcopy(rows);bad[2]['text']+='別の文。'
    with pytest.raises(ValueError,match='other four'):validate_replacement(old,groups,bad)
    bad=copy.deepcopy(rows);bad[0]['choices'].reverse();bad[0]['outcome']=bad[0]['choices'][bad[0]['label']]
    with pytest.raises(ValueError,match='declared local state'):validate_replacement(old,groups,bad)
    badgroups=copy.deepcopy(groups);badgroups['structural_holdout'][0]['branches'][0]['label']=1
    with pytest.raises(ValueError,match='Probe conclusions'):validate_replacement(old,badgroups,rows)


def test_actual_codec_128_new_probes_common_target_and_complete_body_focus():
    old=read_json(CONTROL_DATA/'train-source.json');groups,rows=generate(old)
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');probes=encode_probes(groups,tok)
    assert len(probes['families'])==128 and len(probes['cases'])==512
    assert sum(f['category']=='negation' for f in probes['families'])==64
    for start in range(0,512,4):
        before,after=probes['cases'][start:start+2],probes['cases'][start+2:start+4]
        assert [r['target_ids'] for r in before]==[r['target_ids'] for r in after]
        assert [r['label'] for r in before]==[0,0] and [r['label'] for r in after]==[1,1]
    for row in rows[:64]:
        ids=tok.encode(row['text']);mask=outcome_token_mask(row['text'],ids,tok,[row])
        assert tok.decode_bytes(ids)==row['text'].encode() and mask.any() and not mask[0] and not mask[-1]


def test_changed_material_actual_stream_cursor_and_manifest_identity(tmp_path):
    # Native whole-document IDs across varying lengths, not a mocked sampler.
    old=read_json(CONTROL_DATA/'train-source.json');_,rows=generate(old)
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    bodies=[tok.encode(r['text']) for r in rows[:64]]
    lengths=np.array([len(b)+2 for b in bodies]);offsets=np.r_[0,np.cumsum(lengths)[:-1]]
    class View:
        directory=tmp_path
        manifest_sha256='fixed-source-identity'
        tokens=np.array([t for b in bodies for t in [2,*b,3]],dtype='<u2')
        focus=np.zeros(sum(lengths),dtype=bool)
        manifest={}
    view=View();view.lengths=lengths;view.offsets=offsets
    original=PositiveStream(view,42);original.block(1024);state=original.state_dict()
    expected=original.block(1024);resumed=PositiveStream(view,42);resumed.load_state_dict(state)
    assert all(np.array_equal(a,b) for a,b in zip(expected,resumed.block(1024),strict=True))
    state['manifest_sha256']='other-source'
    with pytest.raises(ValueError,match='identity/cursor'):resumed.load_state_dict(state)
