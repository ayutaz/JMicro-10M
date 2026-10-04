"""Check production display handling on saved generations, without inference."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.text_display import decode_display
from jmicro.tokenizer import Tokenizer


def main():
    source = ROOT / 'reports/phase6/base-5b-comparison-20261004/generation.json'
    rows = read_json(source)['generation']['outputs']
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    tails, unchanged = [], 0
    for row in rows:
        raw = tok.decode_bytes(row['generated_ids'])
        shown = decode_display(raw, row['stop_reason'])
        assert shown['raw_text'] == row['text'] and shown['valid_utf8'] == row['valid_utf8']
        if row['valid_utf8']:
            assert shown['text'] == row['text'] and not shown['truncated_utf8_tail']
            unchanged += 1
        else:
            assert shown['truncated_utf8_tail'] and shown['pending_utf8_bytes_hex'] == 'e6a5'
            assert shown['text'].encode() + bytes.fromhex(shown['pending_utf8_bytes_hex']) == raw
            tails.append(dict(id=row['id'], suppressed=row['suppressed'], **shown))
    assert len(rows) == 400 and unchanged == 398 and len(tails) == 2
    report = dict(status='passed_production_display_saved400', verified_at=now(),
        source_sha256=sha256(source), outputs=400, unchanged_valid_text=unchanged,
        raw_unicode_failures_retained=2, tails=tails, new_GPU_inference=0,
        implementation={p: sha256(ROOT / p) for p in ('src/jmicro/text_display.py', 'src/jmicro/inference.py')})
    write_json(ROOT / 'reports/phase6/text_display_verification.json', report)
    print(report['status'])


if __name__ == '__main__':
    main()
