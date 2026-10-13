"""One new TRAIN recipe from accepted S0 plus authored semantic operations.

This preparation reads TRAIN only. New/known DEV and TEST are not opened.
Versions during preparation are retained; no learned candidate is replaced.
"""
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import random
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.chat_semantic_curriculum import WEIGHTS, render, semantic_check
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_improvement_train import BOUNDS, content_binding, dump_jsonl

RUN = ROOT / 'reports/phase7/chat-semantic-diversity-20261013'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-semantic-diversity-20261013')
CONTROL = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-generalization-20261013')
TARGET = 660000
NEW_FRACTIONS = {key: .02 if key == 'daily' else .70 for key in WEIGHTS}


def main():
    assert sys.version_info[:3] == (3, 12, 7)
    assert not (DATA / 'manifest.json').exists(), 'Frozen TRAIN must not be overwritten'
    assert not (DATA / 'dev.jsonl').exists(), 'TRAIN must precede new DEV'
    assert not (RUN / 'S1/latest.json').exists(), 'Learned candidate cannot be redesigned'
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    sources = {path: sha256(ROOT / path) for path in
               ('src/jmicro/chat_semantic_curriculum.py', 'scripts/prepare_chat_semantic_train.py')}
    control = read_json(CONTROL / 'manifest.json')
    assert sha256(CONTROL / 'train.jsonl') == control['train']['sha256']
    design_path = RUN / 'train_design_preparation.json'
    version = 1
    if design_path.exists():
        previous = read_json(design_path)
        assert previous['sources'] != sources, 'Same preparation already exists; inspect it'
        version = previous['version'] + 1
        atomic_json(RUN / 'preparation_history' / f'design-v{previous["version"]}.json', previous)
    snapshot = RUN / 'preparation_sources' / f'v{version}'
    for path in sources:
        destination = snapshot / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, destination)
    design = dict(created_at=now(), version=version, sources=sources, recipe='whole_data_recipe',
                  source_categories=WEIGHTS, authored_teacher_fraction_by_category=NEW_FRACTIONS,
                  target_teachers_per_pass=TARGET, max_category_family_teacher_fraction=.047,
                  source_family_definition='authored setting/operation grouping, all slot and surface variants together',
                  authored_family_slots_per_category=32,
                  slot_variants_not_independent_information=True,
                  unchanged_control_TRAIN_sha256=control['train']['sha256'],
                  new_DEV_read=False, known_DEV_read=False, protected_TEST_read=False,
                  comparison_control='latestD1 historical state from original10B, never fine-tune from D1',
                  training_changes=['data_recipe_only'], seed=42, teacher_budget=1899555,
                  fixed_padding=True, native_parameter_count=10001152,
                  max_target_exposure=3, complete_target_max_teachers=65,
                  planned_QA_samples=280, independent_human_review=False,
                  new_GPU_learning_updates=0)
    atomic_json(design_path, design)
    pools = defaultdict(lambda: defaultdict(list))
    seen = set()
    rejected = Counter()

    def add(record, origin):
        body = record['messages'][-1]['text']
        ids = tok.encode(body)
        teachers = len(ids) + 1
        if not 2 <= teachers <= 65:
            rejected['complete_target_length'] += 1
            return
        assert tok.decode(ids) == body, 'Do not repair non-roundtripping targets'
        digest = content_binding(record)
        if digest in seen:
            rejected['exact_message_duplicate'] += 1
            return
        seen.add(digest)
        record.update(content_sha256=digest, teacher_tokens=teachers,
                      length_bin=next(i for i, (low, high) in enumerate(BOUNDS) if low <= teachers <= high),
                      recipe_origin=origin)
        pools[record['category']][origin].append(record)

    for line in (CONTROL / 'train.jsonl').read_text().splitlines():
        original = json.loads(line)
        assert original['split'] == 'train'
        record = dict(original, doc_id='s1-reuse-' + original['doc_id'],
                      family='control-' + original['family'], source='accepted-S0-unchanged',
                      control_provenance=dict(doc_id=original['doc_id'],
                                              content_sha256=original['content_sha256'],
                                              train_sha256=control['train']['sha256']))
        assert content_binding(record) == original['content_sha256']
        add(record, 'accepted_S0_unchanged')
    for category in WEIGHTS:
        for family in range(32):
            for variant in range(768):
                record = render(category, family, variant)
                assert semantic_check(record)
                add(record, 'new_authored_semantic')
        print(json.dumps(dict(stage='TRAIN_only_pool', category=category,
                              accepted={key: len(value) for key, value in pools[category].items()})), flush=True)
    selected = []
    totals = Counter()
    families = defaultdict(Counter)
    rng = random.Random(13542)
    source_teachers = defaultdict(Counter)
    for category, weight in WEIGHTS.items():
        quota = round(TARGET * weight)
        family_cap = int(quota * .047)
        authored_quota = round(quota * NEW_FRACTIONS[category])
        for origin, target in (('new_authored_semantic', authored_quota),
                               ('accepted_S0_unchanged', quota - authored_quota)):
            records = list(pools[category][origin])
            rng.shuffle(records)
            # Favor naturally complete responses rather than padding labels or
            # inventing explanations merely to match length distributions.
            preference = (.20, 1.1, 3., 3.)
            records.sort(key=lambda r: rng.expovariate(preference[r['length_bin']]))
            for record in records:
                if source_teachers[category][origin] >= target:
                    break
                if families[category][record['family']] + record['teacher_tokens'] > family_cap:
                    continue
                selected.append(record)
                totals[category] += record['teacher_tokens']
                source_teachers[category][origin] += record['teacher_tokens']
                families[category][record['family']] += record['teacher_tokens']
            assert source_teachers[category][origin] >= target, (category, origin, target,
                                                               source_teachers[category][origin])
    rng.shuffle(selected)
    for record in selected:
        assert record['split'] == 'train'
        assert record['target_message_indices'] == [len(record['messages']) - 1]
        assert [m['role'] for m in record['messages']] == ['user' if i % 2 == 0 else 'assistant'
                                                        for i in range(len(record['messages']))]
        assert all(m['text'] and '\ufffd' not in m['text'] and '<|im_' not in m['text']
                   for m in record['messages'])
        windows = list(tok.sft_windows(record['messages'], context=1025))
        assert windows[-1]['removed_turns'] == 0, 'New TRAIN target must retain its history'
    dump_jsonl(DATA / 'candidate.train.jsonl', selected)
    packet = []
    for category in WEIGHTS:
        rows = [record for record in selected if record['category'] == category]
        new = [record for record in rows if record['recipe_origin'] == 'new_authored_semantic']
        old = [record for record in rows if record['recipe_origin'] == 'accepted_S0_unchanged']
        review_rng = random.Random('semantic-review-' + category)
        by_family = defaultdict(list)
        for record in new:
            by_family[record['family']].append(record)
        review = [review_rng.choice(by_family[family]) for family in sorted(by_family)]
        #32 authored settings plus8 unchanged sources per category; preserve
        #the actual narrower coverage if a setting is absent from selection.
        review += review_rng.sample(old, 40 - len(review))
        assert len(review) == 40
        packet.extend(review)
    dump_jsonl(DATA / 'train_review_packet.jsonl', packet)
    histogram = Counter(record['length_bin'] for record in selected)
    total_teachers = sum(totals.values())
    report = dict(created_at=now(), status='candidate_pending_actual_QA_and_consumption', version=version,
                  design=dict(path=str(design_path), sha256=sha256(design_path)), sources=sources,
                  candidate=dict(path=str(DATA / 'candidate.train.jsonl'), sha256=sha256(DATA / 'candidate.train.jsonl')),
                  targets=len(selected), teachers_per_pass=total_teachers, teacher_categories=dict(totals),
                  category_fractions={key: value / total_teachers for key, value in totals.items()},
                  source_teachers={key: dict(value) for key, value in source_teachers.items()},
                  family_statistics={key: dict(count=len(value), max_teacher_fraction=max(value.values()) / totals[key])
                                     for key, value in families.items()},
                  semantic_operations=dict(Counter(record.get('semantic_operation', 'unchanged_control') for record in selected)),
                  authored_operations=sorted({record['semantic_operation'] for record in selected
                                              if record['recipe_origin'] == 'new_authored_semantic'}),
                  length_bins=[histogram[i] for i in range(4)],
                  length_bin_fractions=[histogram[i] / len(selected) for i in range(4)],
                  single_User_fraction=sum(len(record['messages']) == 2 for record in selected) / len(selected),
                  exact_body_types=len({record['messages'][-1]['text'] for record in selected}),
                  review_samples=len(packet), review_packet_sha256=sha256(DATA / 'train_review_packet.jsonl'),
                  rejections=dict(rejected), new_DEV_created=False, protected_TEST_used=False,
                  new_GPU_learning_updates=0, all_TRAIN_independent_human_certified=False)
    atomic_json(RUN / f'train_candidate_v{version}.json', report)
    atomic_json(RUN / 'train_candidate.json', report)
    print(json.dumps({key: report[key] for key in ('status', 'targets', 'teachers_per_pass',
                                                 'length_bin_fractions', 'source_teachers')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
