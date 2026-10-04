"""Classify saved finishing Unicode failures without GPU inference."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.text_display import decode_display


def main():
    plan = read_json(ROOT / 'configs/phase6/eos_5b_finish_100m.json')
    source = ROOT / plan['output'] / 'short20-full-evaluation.json'
    tok = Tokenizer(ROOT / plan['tokenizer'])
    failures = []
    for row in read_json(source)['generation']['outputs']:
        if row['valid_utf8']:
            continue
        raw = tok.decode_bytes(row['generated_ids'])
        display = decode_display(raw, row['stop_reason'])
        assert not display['raw_valid_utf8']
        assert display['raw_text'] == row['text']
        try:
            raw.decode('utf-8')
        except UnicodeDecodeError as error:
            failures.append(dict(id=row['id'], decoding=row['decoding'], seed=row['seed'],
                stop_reason=row['stop_reason'], raw_bytes_hex=raw.hex(), generated_ids=row['generated_ids'],
                raw_text=row['text'], display=display,
                error=dict(start=error.start, end=error.end, reason=error.reason),
                classification='cap_incomplete_tail' if display['truncated_utf8_tail'] else 'interior_invalid_UTF8'))
    assert len(failures) == 2
    assert [r['classification'] for r in failures] == ['interior_invalid_UTF8', 'cap_incomplete_tail']
    report = dict(status='saved_two_raw_failures_classified', reviewed_at=now(),
        source_sha256=sha256(source), tokenizer_sha256=sha256(ROOT / plan['tokenizer']),
        helper_sha256=sha256(ROOT / 'src/jmicro/text_display.py'), failures=failures,
        raw_failures_retained=2, GPU_inference_calls=0, adoption_gate_passed=False)
    write_json(ROOT / 'reports/phase6/eos_5b_finish_unicode_review.json', report)
    print([(r['id'], r['seed'], r['classification'], r['error']) for r in failures])


if __name__ == '__main__':
    main()
