"""Original rubric, literal authored scores and complete actual-history reuse."""
from pathlib import Path
from chat_lr_contract import RUN, CONFIG, require_ref
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.chat_review import review_items
from review_chat_semantic_observer import protocol_view
from evaluate_chat_semantic import load_cases
import review_chat_semantic as reviewer


def get_items(path):
    raw = read_json(path)
    assert raw.get('requested_three_steps_complete', False) is False
    view = protocol_view(raw)
    c = read_json(CONFIG)
    tok = Tokenizer(require_ref(c['tokenizer']))
    binding = raw['binding']
    assert binding['tokenizer_sha256'] == c['tokenizer']['sha256']
    assert binding['config_sha256'] == sha256(CONFIG)
    suite = next(ref for ref in c['suites'].values() if ref['sha256'] == binding['suite_sha256'])
    cases, _ = load_cases(require_ref(suite), tok)
    items = review_items(view, cases, tok, 1024)
    assert raw == read_json(path)
    return view, items


reviewer.RUN, reviewer.get_items = RUN, get_items

if __name__ == '__main__':
    reviewer.main()
