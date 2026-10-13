"""Verify corrected paired API against real original stored comparisons, CPU only."""
import copy
import json
from pathlib import Path
from chat_lr_contract import RUN, OLD, reference
from jmicro.experiment import read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review, paired_chat_comparison
from review_chat_semantic_observer import get_items


if __name__ == '__main__':
    saved = read_json(OLD / 'selection.json')
    sources = []
    for suite in ('new', 'previous', 'old'):
        data = {}
        for arm in ('S0', 'S1'):
            path = OLD / 'evaluation' / arm / 't3' / suite / 'greedy/result.json'
            evaluation, items = get_items(path)
            notes = read_json(path.with_name('notes.json'))
            review = content_review(evaluation, sha256(path), notes, items)
            canonical = copy.deepcopy(review)
            canonical['reviewer']['identity'] = 'Codex nonblind matched protocol'
            data[arm] = (evaluation, items, canonical)
            sources.append(reference(path))
        observed = paired_chat_comparison(data['S0'][0], data['S1'][0], data['S0'][1], data['S1'][1],
                                         data['S0'][2], data['S1'][2])
        assert json.loads(json.dumps(observed['paired'])) == saved['paired'][suite]['paired']
    atomic_json(RUN / 'paired_API_check.json', dict(passed=True, source=reference(Path(__file__)),
        original_comparison=reference(OLD / 'selection.json'), sources=sources,
        all3_original_paired_metrics_and_CI_recomputed_equal=True,
        new_candidate_quality_evidence=False, GPU_updates=0, completed_at=now()))
    print('Correct paired API reproduced all3 real original metrics/CI exactly; not new model-quality evidence')
