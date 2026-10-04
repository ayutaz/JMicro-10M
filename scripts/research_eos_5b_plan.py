"""Read saved evaluation and probe UTF8 buffering on CPU; no model inference."""
import codecs
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, write_json, now, sha256
from jmicro.tokenizer import Tokenizer


def buffered_text(raw):
    decoder = codecs.getincrementaldecoder('utf-8')(errors='strict')
    visible = ''.join(decoder.decode(bytes([b]), final=False) for b in raw)
    pending, _ = decoder.getstate()
    assert visible.encode('utf-8') + pending == raw
    return visible, pending


def main():
    plan = read_json(ROOT / 'configs/phase6/base_5b_comparison.json')
    run = ROOT / plan['output']
    tok = Tokenizer(ROOT / plan['tokenizer'])
    generation = read_json(run / 'generation.json')['generation']['outputs']
    unchanged, failures = 0, []
    for row in generation:
        raw = tok.decode_bytes(row['generated_ids'])
        visible, pending = buffered_text(raw)
        if pending:
            assert row['stop_reason'] == 'max_new_tokens' and not row['valid_utf8']
            failures.append(dict(id=row['id'], suppressed=row['suppressed'],
                pending_bytes_hex=pending.hex(), pending_bytes=len(pending),
                raw_bytes=len(raw), visible_bytes=len(visible.encode('utf-8')),
                visible_text=visible, stop_reason_unchanged=row['stop_reason']))
        else:
            assert visible == row['text'] and row['valid_utf8']
            unchanged += 1
    probes = []
    for char in ('楓', '😀'):
        encoded = char.encode('utf-8')
        for length in range(1, len(encoded)):
            visible, pending = buffered_text(b'A' + encoded[:length])
            assert visible == 'A' and len(pending) == length
            probes.append(dict(character=char, partial_bytes=length, buffered=True))
        assert buffered_text(encoded) == (char, b'')
    for invalid in (b'A\xffB', b'\xe6\x41', b'\xed\xa0\x80', b'\xf4\x90\x80\x80'):
        try:
            buffered_text(invalid)
        except UnicodeDecodeError:
            probes.append(dict(invalid_bytes_hex=invalid.hex(), rejected=True))
        else:
            raise AssertionError('Interior/invalid UTF8 must not be hidden')
    eos = {}
    paths = {'base5B': run / 'full-dev.json'}
    paths.update({key: Path(plan['references'][key]['path']) for key in
                  ('base2B_body', 'lowLR_web', 'short20_reference_only')})
    for key, path in paths.items():
        body = read_json(path)['body']
        mean = body['eos_nll'] / body['documents']
        eos[key] = dict(documents=body['documents'], mean_eos_nll=mean,
                       geometric_eos_probability=math.exp(-mean),
                       source=str(path), method='Saved true-ending losses only; no EOS rank or free-trajectory probability inferred')
    pool = Path('/home/aihub_ubuntu/jmicro-data/phase6/eos-complete-100m-20261004-r2')
    ready = read_json(pool / 'ready.json')
    result = dict(status='completed_CPU_saved_evidence_research_planning_only',
        researched_at=now(), GPU_inference_seconds=0, training_tokens=0,
        generation_source_sha256=sha256(run / 'generation.json'),
        generation_outputs=400, valid_outputs_unchanged=unchanged,
        tail_buffer_probes=probes, incomplete_tails=failures,
        original_unicode_failures_retained=len(failures), saved_teacher_EOS=eos,
        short_pool={k: ready[k] for k in ('status', 'documents', 'tokens',
            'parent_documents', 'manifest_sha256', 'auxiliary_sha256')},
        interpretation='Buffered display can omit only incomplete tail bytes while preserving raw IDs/bytes/invalid flag/max-token stop. This is not EOS or model quality improvement. No production decoder changed.')
    write_json(ROOT / 'reports/phase6/eos_5b_improvement_research.json', result)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
