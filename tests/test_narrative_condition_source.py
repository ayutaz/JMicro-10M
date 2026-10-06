"""Grounding, complete native codec, fixed selection and stream continuation."""
import copy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import numpy as np
import pytest
from jmicro.experiment import ROOT, read_json
from jmicro.tokenizer import Tokenizer
from narrative_condition_source import generate, render, select_pilot, encode_rows, CATEGORIES
from condition_positive_trainer import PositiveStream
from review_narrative_condition_source import validate_notes

TRAIN = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/train-source.json')


@pytest.fixture(scope='module')
def material():
    control = read_json(TRAIN)
    return control, generate(control)


def test_every_accepted_fact_branch_surface_retained_and_no_reroll(material):
    control, rows = material
    assert len(rows) == len({r['text_sha256'] for r in rows}) == 16384
    lookup = {f['id']: f for f in control['families']}
    for r in rows:
        family = lookup[r['family']]
        assert r['facts'] == family['facts']
        assert r['local_state'] == family['branches'][r['label']]['local_state']
        assert r['text'].count('。') == 3 and r['text'].endswith('。')
        assert r['split'] == 'train'
    assert {(r['family'], r['label'], r['surface']) for r in rows} == {
        (f['id'], b, s) for f in control['families'] for b in (0, 1) for s in range(8)}
    # Non-pilot input fixture: no actual64 preparation or content review here.
    pilot = select_pilot(rows)
    assert pilot == select_pilot(rows)
    assert len({(r['category'], r['surface']) for r in pilot['rows'][:48]}) == 48
    bad = copy.deepcopy(control['families'][0]); bad['split'] = 'lexical_holdout'
    with pytest.raises(ValueError, match='TRAIN'): render(bad, 0, 0)
    bad = copy.deepcopy(control['families'][0]); bad['branches'][0]['local_state']['did_action'] = False
    with pytest.raises(ValueError, match='local state'): render(bad, 0, 0)


def test_arithmetic_time_roles_and_devices_keep_opposed_truths(material):
    control, _ = material
    families = {cat: next(f for f in control['families'] if f['category'] == cat) for cat in CATEGORIES}
    for s in range(8):
        q = families['quantity']; x, d, u = q['facts']['x'], q['facts']['delta'], q['facts']['unit']
        assert f'{x+d}{u}' in render(q, 0, s)['text']
        assert f'{x-d}{u}' in render(q, 1, s)['text']
        t = families['time']; h, d = t['facts']['hour'], t['facts']['duration']
        assert f'{h-d}時' in render(t, 0, s)['text'] and '早めた' in render(t, 0, s)['text']
        assert f'{h+d}時' in render(t, 1, s)['text'] and '遅らせた' in render(t, 1, s)['text']
        c = families['comparison']
        assert f'{c["facts"]["A"]}の棒' in render(c, 0, s)['text'][render(c, 0, s)['cut']:]
        assert f'{c["facts"]["B"]}の棒' in render(c, 1, s)['text'][render(c, 1, s)['cut']:]
    for form in range(4):
        e = next(f for f in control['families'] if f['category'] == 'entity_reference' and f['form'] == form)
        c = next(f for f in control['families'] if f['category'] == 'causality' and f['form'] == form)
        for s in range(8):
            for b in (0, 1):
                er = render(e, b, s)
                assert er['local_state']['target'] == e['facts']['A' if b == 0 else 'B']
                assert er['local_state']['target'] in er['text'][er['cut']:]
                cr = render(c, b, s)
                assert ('点灯している' in cr['text'] or '光っている' in cr['text']) if b == 0 else ('消えている' in cr['text'] or '光っていない' in cr['text'])


def test_native_codec_variable_lengths_eos_focus_and_mid_document_resume(material, tmp_path):
    _, all_rows = material
    # Each surface/category and both branches, fixed fixture independent of actual pilot selection.
    rows = [next(r for r in all_rows if r['category'] == cat and r['surface'] == s and r['label'] == b)
            for cat in CATEGORIES for s in range(8) for b in (0, 1)]
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    arrays, metadata = encode_rows(rows, tok)
    for r, m, start, length in zip(rows, metadata, arrays['offsets'], arrays['lengths'], strict=True):
        ids = arrays['tokens'][start:start+length].tolist()
        assert ids[0] == 2 and ids[-1] == 3 and min(ids[1:-1]) >= 8
        assert tok.decode_bytes(ids[1:-1]) == r['text'].encode('utf-8')
        assert m['body_tokens'] == length-2
        assert not arrays['focus'][start] and not arrays['focus'][start+length-1]
    class View:
        directory = tmp_path
        manifest_sha256 = 'narrative-fixture'
    view = View()
    for k, v in arrays.items(): setattr(view, k, v.astype(bool) if k == 'focus' else v)
    stream = PositiveStream(view, 42); stream.block(1024)
    state = stream.state_dict(); expected = [stream.block(1024) for _ in range(3)]
    resumed = PositiveStream(view, 42); resumed.load_state_dict(state)
    for block in expected:
        assert all(np.array_equal(a,b) for a,b in zip(block, resumed.block(1024), strict=True))
    state['manifest_sha256'] = 'other-source'
    with pytest.raises(ValueError, match='identity'): resumed.load_state_dict(state)


def test_content_review_refuses_missing_weak_grammar_and_raw_rebinding(material):
    _, rows = material; pilot = select_pilot(rows)
    notes = [dict(id=r['id'], text_sha256=r['text_sha256'], paired_condition_outcome=2, weak_document=False,
                  unresolved_grammar_issue=False, unresolved_grounding_issue=False,
                  reason='Protocol fixture only; not actual individual content review.') for r in pilot['rows']]
    raw = dict(pilot_sha256='fixture', all64_individually_read=True, notes=notes)
    assert validate_notes(pilot, raw, 'fixture')['weak_documents'] == 0
    bad = copy.deepcopy(raw); bad['notes'][0]['text_sha256'] = 'changed'
    with pytest.raises(ValueError, match='Exact raw'): validate_notes(pilot, bad, 'fixture')
    bad = copy.deepcopy(raw); bad['notes'][0]['paired_condition_outcome'] = 1
    with pytest.raises(ValueError, match='Exact raw'): validate_notes(pilot, bad, 'fixture')
    bad = copy.deepcopy(raw); bad['notes'].pop()
    with pytest.raises(ValueError, match='Every fixed64'): validate_notes(pilot, bad, 'fixture')
    raw['notes'][0].update(paired_condition_outcome=1, weak_document=True, unresolved_grammar_issue=True, unresolved_grounding_issue=True)
    assert validate_notes(pilot, raw, 'fixture') == dict(weak_documents=1, unresolved_grammar_documents=1, unresolved_grounding_documents=1)
