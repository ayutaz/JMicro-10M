"""Select real, complete short targets and a stratified 300-target QA sample.

This is a review draft. No generation, fabricated examples, truncation, DEV
content, or learning is performed. Acceptance follows individual QA notes.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from prepare_chat_natural_sources import DATA, RUN, now, save, sha
from inventory_chat_natural import digest


def topic(text):
    for name, terms in [('food', '料理 食べ 飲み ご飯 食事 お酒'),
                        ('work_study', '仕事 勉強 学校 大学 学生'),
                        ('hobby', '趣味 映画 音楽 ゲーム 読書 スポーツ'),
                        ('travel', '旅行 海外 温泉 観光 出かけ'),
                        ('daily', '休み 休日 家族 ペット 犬 猫')]:
        if any(term in text for term in terms.split()):
            return name
    return 'other'


def main():
    receipt = RUN / 'TRAIN_draft.json'
    if receipt.exists():
        raise FileExistsError('Review the preserved draft instead of silently redrawing it')
    pools = {}
    targets = []
    for source in ('RPC', 'magpie'):
        path = DATA / f'{source}_eligible_inventory.jsonl'
        ref = json.loads((RUN / 'availability.json').read_text())['files'][source]
        assert sha(path) == ref['sha256']
        rows = [json.loads(line) for line in path.read_text().splitlines()]
        pools[source] = {r['doc_id']: r for r in rows}
        for row in rows:
            for target in row['targets']:
                if target['teachers'] <= 32:
                    targets.append(dict(source=source, doc_id=row['doc_id'], **target))
    magpie = [t for t in targets if t['source'] == 'magpie']
    requested_total = 1050000
    rpc_goal = requested_total - sum(t['teachers'] for t in magpie)
    rpc = sorted([t for t in targets if t['source'] == 'RPC'],
                 key=lambda t: digest('natural-C1-42:' + t['doc_id'] + ':' + str(t['index'])))
    chosen, consumed = [], 0
    for target in rpc:
        if consumed >= rpc_goal:
            break
        chosen.append(target)
        consumed += target['teachers']
    selected = dict(C1=chosen + magpie,
                    C0=[t for t in targets if t['source'] == 'RPC' and pools['RPC'][t['doc_id']]['original_RPC_train']])
    summaries = {}
    for arm, selection in selected.items():
        groups = defaultdict(list)
        for target in selection:
            groups[target['doc_id']].append(target)
        records, answers = [], set()
        for uid in sorted(groups):
            source = groups[uid][0]['source']
            indices = sorted(t['index'] for t in groups[uid])
            row = pools[source][uid]
            messages = row['messages'][:indices[-1]+1]
            records.append(dict(doc_id=uid, split='train', source=source, messages=messages,
                target_message_indices=indices, original_RPC_train=row['original_RPC_train']))
            for index in indices:
                answers.add(digest(messages[index]['text']))
        path = DATA / f'{arm}_TRAIN_draft.jsonl'
        with path.open('x') as stream:
            for row in records:
                stream.write(json.dumps(row, ensure_ascii=False) + '\n')
        summaries[arm] = dict(path=str(path), sha256=sha(path), families=len(records), targets=len(selection),
            teachers_per_pass=sum(t['teachers'] for t in selection), distinct_answer_texts=len(answers),
            by_source={s: dict(targets=sum(t['source'] == s for t in selection),
                              teachers=sum(t['teachers'] for t in selection if t['source'] == s)) for s in pools})
    # Over-sample the smaller synthetic source for QA; train weights are not
    # changed by this review distribution. Within source, round-robin strata.
    samples = []
    for source, count in (('RPC', 200), ('magpie', 100)):
        strata = defaultdict(list)
        for t in selected['C1']:
            if t['source'] != source:
                continue
            messages = pools[source][t['doc_id']]['messages'][:t['index']+1]
            key = (1 if t['index'] == 1 else 2, 'short' if t['teachers'] <= 16 else 'long',
                   topic(messages[-2]['text'] + messages[-1]['text']))
            strata[key].append(t)
        for key in strata:
            strata[key].sort(key=lambda t: digest('natural-QA-42:' + t['doc_id'] + ':' + str(t['index'])))
        cursor = 0
        while count:
            added = False
            for key in sorted(strata):
                if cursor >= len(strata[key]) or not count:
                    continue
                t = strata[key][cursor]
                messages = pools[source][t['doc_id']]['messages'][:t['index']+1]
                samples.append(dict(id=f'QA{len(samples)+1:03}', source=source, doc_id=t['doc_id'],
                    target_message_index=t['index'], teachers=t['teachers'], stratum=key,
                    raw_binding=digest(json.dumps(messages, ensure_ascii=False, sort_keys=True)), messages=messages))
                count -= 1
                added = True
            assert added
            cursor += 1
    assert len(samples) == 300
    save(DATA / 'TRAIN_QA_sample.json', samples)
    with (RUN / 'TRAIN_QA_display.jsonl').open('x') as stream:
        for row in samples:
            stream.write(json.dumps(dict(id=row['id'], source=row['source'], teachers=row['teachers'],
                original_target_index=row['target_message_index'], previous=row['messages'][-4:-2],
                user=row['messages'][-2]['text'], answer=row['messages'][-1]['text']), ensure_ascii=False) + '\n')
    save(receipt, dict(status='draft_awaiting_individual_content_review', created_at=now(), arms=summaries,
        teacher_cap_including_EOT=32, target_truncation=False, original70_30_proposal_superseded=True,
        reason='Only15,934 unique short Magpie teachers available; do not upsample this629-target pool to30percent',
        candidate_pool_total=requested_total, teacher_budget_each_arm=1000000,
        actual_consumed_source_ratio='Pending deterministic complete-target dry run after QA',
        QA_sample=dict(path=str(DATA / 'TRAIN_QA_sample.json'), sha256=sha(DATA / 'TRAIN_QA_sample.json'),
                       count=300, source_counts={'RPC':200, 'magpie':100}),
        semantic_quality_not_yet_accepted=True, protected_TEST_used=False, training_updates=0))
    print(json.dumps(summaries, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7)
    main()
