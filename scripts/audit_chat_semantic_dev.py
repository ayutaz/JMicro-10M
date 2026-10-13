"""Measure independent authored DEV bindings/overlap/surface/mask contracts."""
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_semantic_train import RUN, DATA, CONTROL


def shingles(text):
    text = ''.join(text.split())
    return {text[index:index + 8] for index in range(max(1, len(text) - 7))}


def main():
    manifest = read_json(DATA / 'manifest.json')
    prep = read_json(RUN / 'dev_preparation.json')
    authored = read_json(DATA / 'dev_authored.json')
    assert sha256(DATA / 'train.jsonl') == manifest['train']['sha256']
    assert sha256(DATA / 'manifest.json') == prep['TRAIN_manifest_sha256'] == authored['TRAIN_manifest_sha256']
    assert manifest['created_at'] < authored['created_at'] <= prep['created_at']
    assert sha256(DATA / 'dev.jsonl') == prep['dev_sha256']
    assert sha256(DATA / 'dev_authored.json') == prep['authored_sha256']
    cases = [json.loads(line) for line in (DATA / 'dev.jsonl').read_text().splitlines()]
    gold = {row['id']: row for row in authored['targets']}
    assert len(cases) == len(gold) == len({case['family_id'] for case in cases}) == 80
    assert len(set(case['id'] for case in cases)) == 80
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    sources = {'S0': CONTROL / 'train.jsonl', 'S1': DATA / 'train.jsonl'}
    questions, index = {}, defaultdict(set)
    for arm, path in sources.items():
        for line in path.read_text().splitlines():
            row = json.loads(line)
            assert row['split'] == 'train'
            text = row['messages'][-2]['text']
            key = (arm, row['doc_id'])
            questions[key] = text
            for shingle in shingles(text):
                index[shingle].add(key)
    exact, near, flags = [], [], []
    prompts, own_counts, windows = [], [], []
    question_set = set(questions.values())
    for case in cases:
        assert case['split'] == 'dev' and case['messages'] == gold[case['id']]['messages']
        messages = case['messages']
        assert [message['role'] for message in messages] == ['user' if n % 2 == 0 else 'assistant' for n in range(len(messages))]
        prompt, removed = tok.chat_prompt(messages, 960)
        assert removed == 0
        prompts.append(len(prompt))
        own_counts.append(sum(message['role'] == 'user' for message in messages))
        for message in messages:
            text = message['content']
            if not text or '\ufffd' in text or '<|im_' in text or tok.decode(tok.encode(text)) != text:
                flags.append(dict(id=case['id'], message=text))
        body = gold[case['id']]['gold_body']
        complete = messages + [dict(role='assistant', content=body)]
        window = list(tok.sft_windows(complete, context=1025))[-1]
        assert window['removed_turns'] == 0 and window['labels'][-1] == 7
        selected = [label for label in window['labels'] if label != -100]
        assert selected == tok.encode(body) + [7]
        windows.append(dict(id=case['id'], teacher_tokens=len(selected), body_bytes=len(body.encode('utf-8'))))
        question = messages[-1]['content']
        if question in question_set:
            exact.append(case['id'])
        query = shingles(question)
        matches = Counter(key for part in query for key in index.get(part, ()))
        for key, intersection in matches.items():
            other = shingles(questions[key])
            ratio = intersection / len(query | other)
            if ratio >= .8:
                near.append(dict(id=case['id'], arm=key[0], train_doc_id=key[1], Jaccard8=ratio))
    contexts = [count for count in own_counts if count > 1]
    assert len(contexts) == 24 and sum(contexts) == 59 and set(contexts) == {2, 3, 4}
    result = dict(observed_at=now(), families=80, own_families=24, own_responses=59,
                  exact_final_question_overlap=len(exact), exact_overlaps=exact,
                  surface_flags=len(flags), surface_findings=flags,
                  near_Jaccard8_at_least80percent=near, near_overlap_count=len(near),
                  maximum_provided_prompt_tokens=max(prompts), fixed_gold_windows=windows,
                  dev_sha256=sha256(DATA / 'dev.jsonl'), authored_sha256=sha256(DATA / 'dev_authored.json'),
                  TRAIN_frozen_before_new_DEV=True, TRAIN_manifest_sha256=sha256(DATA / 'manifest.json'),
                  source_TRAIN_sha256={arm: sha256(path) for arm, path in sources.items()},
                  protected_TEST_used=False, independent_human=False, blind=False,
                  semantic_overlap_fully_certified=False, no_TRAIN_renderer_used=authored['used_TRAIN_renderer'] is False,
                  quality_evidence=False, status='passed' if not (exact or near or flags) else 'failed')
    atomic_json(RUN / 'dev_audit.json', result)
    assert result['status'] == 'passed', 'Preserve failed DEV audit; do not silently claim independence'
    print(json.dumps({key: result[key] for key in ('status', 'families', 'own_families', 'own_responses',
                                                  'exact_final_question_overlap', 'near_overlap_count', 'surface_flags')}))


if __name__ == '__main__':
    main()
