"""Reuse only previously read, byte-identical complete TRAIN sample messages."""
import json
import argparse
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import now, read_json, sha256
from jmicro.training import atomic_json
from prepare_chat_improvement_train import content_binding
from prepare_chat_semantic_train import RUN, DATA


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--count', type=int, default=40)
    args = parser.parse_args()
    current = DATA / 'train_review_packet.jsonl'
    candidate = DATA / 'candidate.train.jsonl'
    previous = RUN / 'preparation_history/v2/train_content_review_final.json'
    old_packet = DATA / 'preparation_history/v2/train_review_packet.jsonl'
    old_candidate = DATA / 'preparation_history/v2/candidate.train.jsonl'
    old_review = read_json(previous)
    assert sha256(old_packet) == old_review['packet_sha256']
    assert sha256(old_candidate) == old_review['candidate_sha256']
    rows = [json.loads(line) for line in current.read_text().splitlines()]
    older = [json.loads(line) for line in old_packet.read_text().splitlines()]
    assert len(rows) == len(older) == old_review['samples'] == 280
    old_notes = {note['index']: note for note in old_review['judgments']}
    by_content = {}
    for index, row in enumerate(older):
        note = old_notes[index]
        assert note['content_sha256'] == content_binding(row) == row['content_sha256']
        if note['passed']:
            by_content[(row['category'], row['content_sha256'])] = (row, note)
    reused, pending = [], []
    lines = []
    for index, row in enumerate(rows):
        assert content_binding(row) == row['content_sha256']
        source = by_content.get((row['category'], row['content_sha256']))
        if source is None:
            pending.append(index)
            if args.start <= index < args.start + args.count:
                print(json.dumps([index, row['category'], [m['text'] for m in row['messages']]], ensure_ascii=False))
            continue
        old, note = source
        assert old['messages'] == row['messages'] and old['target_message_indices'] == row['target_message_indices']
        reused.append(dict(index=index, doc_id=row['doc_id'], content_sha256=row['content_sha256'],
                           original_judgment=note, original_index=note['index']))
        lines.append(str(index) + '\t1\t' + note['rationale'])
    result = dict(created_at=now(), current_packet=dict(path=str(current), sha256=sha256(current)),
                  current_candidate_sha256=sha256(candidate),
                  original_review=dict(path=str(previous), sha256=sha256(previous)),
                  original_packet=dict(path=str(old_packet), sha256=sha256(old_packet)),
                  original_candidate=dict(path=str(old_candidate), sha256=sha256(old_candidate)),
                  reused_count=len(reused), changed_count=len(pending), reused=reused, pending_indices=pending,
                  method='same complete messages/target/category, only earlier explicit passed notes',
                  reviewer='Codex nonblind', independent_human=False, automatic_semantic_grader=False)
    atomic_json(RUN / 'train_review_reuse.json', result)
    (RUN / 'train_QA_reused.tsv').write_text('\n'.join(lines) + '\n')
    print(json.dumps(dict(reused=len(reused), requires_actual_new_review=len(pending))))


if __name__ == '__main__':
    main()
