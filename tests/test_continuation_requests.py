"""Original policy/order/context and DEV-only reads with fake TEST fixtures."""
import hashlib
import json
from pathlib import Path
from unittest.mock import patch

import pytest
from jmicro.continuation_requests import (LEGACY_SUPPRESS_IDS, load_requests, preflight_context, validate_outputs)
from jmicro.evaluation_boundary import identity_digest


def fixture(path):
    cases = [dict(id=f'base-{i+1:03d}', category=f'category-{i//8}', prefix=f'文{i}', split='dev') for i in range(80)]
    raw = ''.join(json.dumps(case) + '\n' for case in cases).encode()
    (path / 'base.dev.jsonl').write_bytes(raw)
    manifest = dict(kind='isolated_base_dev_suite_v1', version=1, split='dev', cases_file='base.dev.jsonl',
        cases_sha256=hashlib.sha256(raw).hexdigest(), case_count=80, case_identity_sha256=identity_digest(cases),
        source_generation_sha256='a'*64, source_legacy_suite_sha256='b'*64, TEST_read_for_export=False)
    mp = path / 'base.dev.manifest.json'
    mp.write_text(json.dumps(manifest))
    return mp, hashlib.sha256(mp.read_bytes()).hexdigest(), cases


def test_original_case_major_five_modes_and_maximum_major_long_order(tmp_path):
    mp, pin, cases = fixture(tmp_path)
    planned, provenance = load_requests(mp, pin)
    assert len(planned) == 440 and len({r.key for r in planned}) == 440
    assert [(r.decoding, r.suppressed, r.seed) for r in planned[:5]] == [
        ('greedy', True, 42), ('greedy', False, 42), ('sampling', True, 42),
        ('sampling', True, 43), ('sampling', True, 44)]
    assert [r.case_id for r in planned[400:420]] == [c['id'] for i, c in enumerate(cases) if i % 8 < 2]
    assert [r.max_new_tokens for r in planned[400:]] == [128]*20 + [512]*20
    assert LEGACY_SUPPRESS_IDS == (0, 1, 2, 4, 5, 6) and 7 not in LEGACY_SUPPRESS_IDS
    assert provenance['fixed80_equality_to_qualified_screen_must_be_checked']


def test_planner_opens_only_two_DEV_files_and_never_broken_TEST(tmp_path):
    mp, pin, _ = fixture(tmp_path)
    (tmp_path / 'test.jsonl').write_text('BROKEN_TEST')
    allowed = {mp, tmp_path / 'base.dev.jsonl'}
    seen, original = [], Path.open
    def guarded(p, *args, **kwargs):
        assert p in allowed
        seen.append(p)
        return original(p, *args, **kwargs)
    with patch.object(Path, 'open', guarded):
        planned, provenance = load_requests(mp, pin)
    assert seen == [mp, tmp_path / 'base.dev.jsonl'] and len(planned) == 440
    assert provenance['TEST_opened'] is False


def test_wrong_TEST_entry_rejected_before_any_file_read(tmp_path):
    with patch.object(Path, 'open', side_effect=AssertionError('No TEST opens')):
        with pytest.raises(ValueError): load_requests(tmp_path / 'base.test.manifest.json', 'a'*64)


def test_context_preflight_preserves_whole_prefix_and_rejects_overflow(tmp_path):
    mp, pin, _ = fixture(tmp_path)
    planned, _ = load_requests(mp, pin)
    class Codec:
        def encode(self, text): return [8] * 510
    assert preflight_context(planned, Codec())['maximum_prompt_tokens'] == 511
    class Overflow:
        def encode(self, text): return [8] * 512
    with pytest.raises(ValueError, match='no silent'):
        preflight_context(planned, Overflow())


@pytest.mark.parametrize('bad', ['mode', 'seed', 'order', 'missing'])
def test_output_identity_binding_cannot_accept_changed_or_partial_generation(tmp_path, bad):
    mp, pin, _ = fixture(tmp_path)
    planned, _ = load_requests(mp, pin)
    rows = [dict(id=r.case_id, category=r.category, prefix=r.prefix, split=r.split,
                 decoding=r.decoding, suppressed=r.suppressed, seed=r.seed, max_new_tokens=r.max_new_tokens)
            for r in planned[:400]]
    assert validate_outputs(rows, planned, 'standard400')
    if bad == 'mode': rows[0]['suppressed'] = False
    elif bad == 'seed': rows[2]['seed'] = 44
    elif bad == 'order': rows[0], rows[1] = rows[1], rows[0]
    else: rows.pop()
    with pytest.raises(ValueError): validate_outputs(rows, planned, 'standard400')
