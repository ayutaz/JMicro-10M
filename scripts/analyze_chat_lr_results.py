"""Describe all original ratings and real histories; never grade with word checks."""
from collections import Counter
import json
from pathlib import Path
from chat_lr_contract import RUN, SUITES, preflight, reference
from review_chat_lr import get_items
from jmicro.experiment import read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review


def main():
    c, _, _ = preflight()
    rows = {}
    for arm, points in (('parent', ('t0',)), ('S0', ('t1', 't2', 't3')), ('S1', ('t1', 't2', 't3'))):
        for point in points:
            nll_path = RUN / 'NLL' / arm / (point + '.json')
            nll = read_json(nll_path)
            assert nll['status'] == 'complete' and nll['binding']['config_sha256'] == c['config_sha256']
            for suite in SUITES:
                path = RUN / 'evaluation' / arm / point / suite / 'greedy/result.json'
                evaluation, items = get_items(path)
                notes_path = path.with_name('notes.json')
                notes = read_json(notes_path)
                review = content_review(evaluation, sha256(path), notes, items)
                ratings = {r['key']: r for r in notes['judgments']}
                primary = [item for item in items.values() if item['condition'] == 'suppressed']
                final = [item for item in items.values() if item['condition'] == 'own-history' and item['final_turn']]
                assert len(primary) == 80 and len(final) == 24
                categories = {}
                for category in sorted({item['category'] for item in primary}):
                    cases = [item for item in primary if item['category'] == category]
                    judgments = [ratings[item['key']] for item in cases]
                    categories[category] = dict(responses=len(cases), grammar2=sum(r['grammar'] == 2 for r in judgments),
                        relevance2=sum(r['relevance'] == 2 for r in judgments),
                        joint2=sum(r['grammar'] == r['relevance'] == 2 for r in judgments))
                provided = {item['id']: item for item in primary}
                matched = []
                for item in final:
                    own = ratings[item['key']]
                    supplied = ratings[provided[item['id']]['key']]
                    prior = [prior_item for prior_item in items.values() if prior_item['condition'] == 'own-history'
                             and prior_item['id'] == item['id'] and not prior_item['final_turn']]
                    matched.append(dict(id=item['id'], provided_context=supplied['context'], own_context=own['context'],
                        weak_prior_turns=[p['turn'] for p in prior if ratings[p['key']]['context'] < 2],
                        actual_own_messages=item['messages'], actual_own_response=item['response']['text'],
                        provided_judgment=supplied, own_judgment=own))
                key = '-'.join((arm, point, suite))
                rows[key] = dict(raw=reference(path), notes=reference(notes_path), summaries=review['summaries'],
                    categories=categories, fixed_NLL=nll['summaries'], NLL_source=reference(nll_path),
                    fluent_but_not_relevant=sum(ratings[item['key']]['grammar'] == 2 and ratings[item['key']]['relevance'] < 2 for item in primary),
                    matched24_provided_context2=sum(r['provided_context'] == 2 for r in matched),
                    matched24_own_context2=sum(r['own_context'] == 2 for r in matched),
                    provided_correct_own_weak=[r['id'] for r in matched if r['provided_context'] == 2 and r['own_context'] < 2],
                    matched24=matched)
                print(json.dumps(dict(key=key, joint=review['summaries']['primary']['joint_grammar_relevance_score2'],
                    own_context=rows[key]['matched24_own_context2'], new_NLL=nll['summaries']['new_DEV']['body_mean_NLL'])))
    assert len(rows) == 28
    atomic_json(RUN / 'final_analysis.json', dict(config_sha256=c['config_sha256'], rows=rows, completed_at=now(),
        source=reference(Path(__file__)), ratings_source='all original literal Codex nonblind judgments; reuse retains provenance',
        original_Chat_TEST_exposure_recorded=True, Base_adopted=False, Chat_adopted=False, quality_complete=False))


if __name__ == '__main__':
    main()
