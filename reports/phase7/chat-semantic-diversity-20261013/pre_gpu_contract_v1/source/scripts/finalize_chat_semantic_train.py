"""Freeze reviewed TRAIN after real QA and complete teacher consumption."""
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.chat_semantic_curriculum import semantic_check
from jmicro.experiment import now, read_json, sha256
from jmicro.training import atomic_json
from prepare_chat_improvement_train import content_binding, dump_jsonl
from prepare_chat_semantic_train import RUN, DATA, CONTROL


def main():
    assert not (DATA / 'manifest.json').exists() and not (DATA / 'dev.jsonl').exists()
    candidate, packet = DATA / 'candidate.train.jsonl', DATA / 'train_review_packet.jsonl'
    review = read_json(RUN / 'train_content_review_final.json')
    assert review['status'] == 'fixed_sample_passed' and review['samples'] == 280 and review['errors'] == 0
    assert review['candidate_sha256'] == sha256(candidate) and review['packet_sha256'] == sha256(packet)
    rows = [json.loads(line) for line in candidate.read_text().splitlines()]
    by_id = {row['doc_id']: row for row in rows}
    assert len(by_id) == len(rows)
    selected = [json.loads(line) for line in packet.read_text().splitlines()]
    notes = {row['doc_id']: row for row in review['judgments']}
    assert len(selected) == len(notes) == 280
    for row in selected:
        assert row == by_id[row['doc_id']]
        assert notes[row['doc_id']]['passed'] and notes[row['doc_id']]['content_sha256'] == row['content_sha256']
        assert len(notes[row['doc_id']]['rationale']) >= 12
    old_manifest = read_json(CONTROL / 'manifest.json')
    assert sha256(CONTROL / 'train.jsonl') == old_manifest['train']['sha256']
    old_rows = {row['doc_id']: row for row in (json.loads(line) for line in (CONTROL / 'train.jsonl').read_text().splitlines())}
    for row in rows:
        assert row['split'] == 'train' and content_binding(row) == row['content_sha256']
        if row['recipe_origin'] == 'new_authored_semantic':
            assert semantic_check(row)
        else:
            source = row['control_provenance']
            original = old_rows[source['doc_id']]
            assert source['train_sha256'] == old_manifest['train']['sha256']
            assert row['messages'] == original['messages']
            assert row['target_message_indices'] == original['target_message_indices']
            assert row['content_sha256'] == original['content_sha256'] == source['content_sha256']
    dry = read_json(RUN / 'consumption_dry_run.json')
    assert dry['status'] == 'passed' and all(dry['checks'].values())
    assert dry['S1']['source_sha256'] == sha256(candidate)
    design = read_json(RUN / 'train_design_preparation.json')
    for path, digest in design['sources'].items():
        from jmicro.experiment import ROOT
        assert sha256(ROOT / path) == digest
    dump_jsonl(DATA / 'train.jsonl', rows)
    assert sha256(DATA / 'train.jsonl') == sha256(candidate)
    teachers = sum(row['teacher_tokens'] for row in rows)
    origins = Counter()
    for row in rows:
        origins[row['recipe_origin']] += row['teacher_tokens']
    candidate_report = read_json(RUN / 'train_candidate.json')
    manifest = dict(created_at=now(), status='reviewed_TRAIN_frozen_before_unseen_DEV', vocab_size=4096,
                    train=dict(path=str(DATA / 'train.jsonl'), sha256=sha256(DATA / 'train.jsonl'),
                               targets=len(rows), teachers_per_pass=teachers),
                    design_freeze=dict(path=str(RUN / 'train_design_preparation.json'), sha256=sha256(RUN / 'train_design_preparation.json')),
                    review=dict(path=str(RUN / 'train_content_review_final.json'), sha256=sha256(RUN / 'train_content_review_final.json')),
                    consumption=dict(path=str(RUN / 'consumption_dry_run.json'), sha256=sha256(RUN / 'consumption_dry_run.json')),
                    categories=dict(Counter(row['category'] for row in rows)), source_teacher_amounts=dict(origins),
                    newly_authored_teacher_fraction=origins['new_authored_semantic'] / teachers,
                    authored_operations=candidate_report['authored_operations'],
                    family_statistics=candidate_report['family_statistics'],
                    single_User_fraction=sum(len(row['messages']) == 2 for row in rows) / len(rows),
                    parameter_change=False, independent_human_review=False, all_TRAIN_human_certified=False,
                    protected_TEST_used=False, Base_adopted=False, Chat_adopted=False)
    atomic_json(DATA / 'manifest.json', manifest)
    atomic_json(RUN / 'train_preparation.json', dict(manifest, manifest_path=str(DATA / 'manifest.json'),
                                                  manifest_sha256=sha256(DATA / 'manifest.json')))
    print(json.dumps(dict(manifest['train'], newly_authored_teacher_fraction=manifest['newly_authored_teacher_fraction'],
                          authored_operations=len(manifest['authored_operations'])), ensure_ascii=False))


if __name__ == '__main__':
    main()
