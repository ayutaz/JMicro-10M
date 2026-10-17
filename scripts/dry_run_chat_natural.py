"""Freeze accepted TRAIN and replay the actual complete-target schedule on CPU."""
from collections import Counter
import json
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.teacher_chat_training import TeacherBudgetSampler, teacher_lr
from jmicro.tokenizer import Tokenizer
from prepare_chat_natural_sources import ROOT, DATA, RUN, now, save, sha


def main():
    manifest_path = DATA / 'manifest.json'
    assert not manifest_path.exists(), 'Preserve frozen TRAIN'
    review = json.loads((RUN / 'TRAIN_QA_review.json').read_text())
    assert review['samples'] == 300 and len(review['notes']) == 300
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    summaries = {}
    for arm in ('C0', 'C1'):
        started = time.monotonic()
        ref = review['arms'][arm]
        path = Path(ref['path'])
        assert sha(path) == ref['sha256']
        rows = [json.loads(line) for line in path.read_text().splitlines()]
        by_doc = {row['doc_id']: row for row in rows}
        sampler = TeacherBudgetSampler(rows, tok, 1024, 42, 1000000, 512, 32)
        lengths = [int(w['labels'].astype(np.int64).astype(bool).sum()) for w in []]  # populated below by exact label mask
        length_counts, source_supply = Counter(), Counter()
        answer_texts = set()
        for window in sampler.windows:
            labels = window['labels']
            target = labels[labels != -100]
            assert 2 <= len(target) <= 32 and target[-1] == 7 and np.all(target[:-1] >= 8)
            row = by_doc[window['doc_id']]
            answer = row['messages'][window['target_message_index']]['text']
            assert tok.decode(target[:-1].tolist()) == answer
            assert window['removed_turns'] == 0
            # Only the current Assistant body+EOT, with exactly one shift.
            assert np.all(labels[:-len(target)] == -100)
            length_counts[len(target)] += 1
            source_supply[row['source']] += len(target)
            answer_texts.add(answer)
        supply = sum(n * count for n, count in length_counts.items())
        history, seen, consumed_source = [], Counter(), Counter()
        max_batch_frames = 0
        while sampler.teacher_tokens < 1000000:
            before = sampler.teacher_tokens
            position, epoch, order = sampler.position, sampler.epoch, sampler.order.copy()
            examples = sampler.examples
            batches, teachers, _ = sampler.next_update()
            used = sampler.examples - examples
            chosen = (list(order[position:position+used]) if sampler.epoch == epoch else
                      list(order[position:]) + list(sampler.order[:sampler.position]))
            assert len(chosen) == used
            for i in chosen:
                w = sampler.windows[int(i)]
                seen[(w['doc_id'], w['target_message_index'])] += 1
                consumed_source[by_doc[w['doc_id']]['source']] += int((w['labels'] != -100).sum())
            assert all(tuple(x.shape) == tuple(y.shape) == (32, 1024) for x, y in batches)
            assert sum(int((y != -100).sum()) for _, y in batches) == teachers
            assert before < sampler.teacher_tokens <= 1000031
            max_batch_frames = max(max_batch_frames, len(batches))
            history.append(dict(update=len(history)+1, teachers=sampler.teacher_tokens,
                                teachers_this_update=teachers, microbatches=len(batches),
                                lr=teacher_lr(before, teachers, 1000000, 3e-5)))
        assert sum(consumed_source.values()) == sampler.teacher_tokens
        assert max(seen.values()) <= (2 if arm == 'C0' else 1)
        assert arm == 'C0' or supply >= 1000000
        terminal = sampler.state_dict()
        restored = TeacherBudgetSampler(rows, tok, 1024, 42, 1000000, 512, 32)
        restored.load_state_dict(terminal)
        assert restored.state_dict() == terminal and np.array_equal(restored.order, sampler.order)
        summary = dict(status='passed', records=ref, sampler_binding=sampler.binding,
            prepared_targets=len(sampler.windows), distinct_answer_texts=len(answer_texts),
            teachers_per_pass=supply, target_length_counts=dict(length_counts), source_supply=dict(source_supply),
            actual_consumed_source_teachers=dict(consumed_source),
            actual_consumed_source_fractions={s: n / sampler.teacher_tokens for s, n in consumed_source.items()},
            updates=len(history), physical_microbatches=sum(r['microbatches'] for r in history),
            max_microbatches_per_update=max_batch_frames, max_target_exposures=max(seen.values()),
            distinct_targets_consumed=len(seen), actual_Assistant_teachers=sampler.teacher_tokens,
            terminal_overshoot=sampler.teacher_tokens-1000000, history=history, sampler_terminal=terminal,
            all_teacher_masks_and_whole_target_roundtrips=True, resume_sampler_exact=True,
            fixed_padding=True, no_history_trim=True, CPU_seconds=time.monotonic()-started, GPU_updates=0,
            created_at=now())
        save(RUN / f'{arm}_dry_run.json', summary)
        summaries[arm] = {k: v for k, v in summary.items() if k not in ('history', 'sampler_terminal', 'target_length_counts')}
        print(json.dumps(dict(arm=arm, **summaries[arm]), ensure_ascii=False), flush=True)
        del sampler, restored
    save(manifest_path, dict(status='TRAIN_frozen_before_new_DEV', created_at=now(),
        teacher_budget_per_arm=1000000, maximum_teacher_length=32, terminal_overshoot_maximum=31,
        arms=summaries, review=dict(path=str(RUN / 'TRAIN_QA_review.json'), sha256=sha(RUN / 'TRAIN_QA_review.json')),
        public_sources=json.loads((RUN / 'acquisition.json').read_text())['files'],
        source_ratio='Deterministic actual teacher fractions above; initial70/30 proposal replaced due short-answer supply',
        scope='Same original10M Base, broader real conversation sources; no synthetic template expansion',
        protected_TEST_used=False, semantic_quality_certified=False))
    save(RUN / 'TRAIN_manifest_ref.json', dict(path=str(manifest_path), sha256=sha(manifest_path), created_at=now()))


if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7)
    main()
