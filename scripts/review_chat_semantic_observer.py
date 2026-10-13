"""CPU protocol adapter: six-stage metadata accepted by the legacy reviewer.

The frozen generator names the uncompleted request requested_six_steps_complete;
the shared reviewer requires requested_five_steps_complete=False. Add only that
false alias in memory. Raw JSON, histories, scores and frozen sources are unchanged.
All original raw-ID/byte/prompt/checkpoint/rubric validation remains mandatory.
"""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.chat_review import review_items
from evaluate_chat_semantic import load_cases
import review_chat_semantic as frozen_reviewer


def protocol_view(raw):
    evaluation = dict(raw)
    if 'requested_five_steps_complete' not in evaluation:
        assert evaluation['requested_six_steps_complete'] is False
        evaluation['requested_five_steps_complete'] = False
    else:
        assert evaluation['requested_five_steps_complete'] is False
    assert evaluation.get('requested_six_steps_complete', False) is False
    return evaluation


def get_items(path):
    raw = read_json(path)
    evaluation = protocol_view(raw)
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    binding = evaluation['binding']
    assert sha256(tok.path) == binding['tokenizer_sha256']
    config = read_json(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    suite = next(ref['path'] for ref in config['suites'].values()
                 if ref['sha256'] == binding['suite_sha256'])
    cases, _ = load_cases(suite, tok)
    items = review_items(evaluation, cases, tok, 1024)
    assert raw == read_json(path), 'Raw evidence changed while observing'
    return evaluation, items


if __name__ == '__main__':
    frozen_reviewer.get_items = get_items
    frozen_reviewer.main()
