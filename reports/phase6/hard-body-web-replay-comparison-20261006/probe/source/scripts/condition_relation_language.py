"""Change only two relation-language categories; preserve accepted train selection."""
import copy
import random
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import read_json, sha256
import condition_transfer_curriculum as original

KIND = 'local_condition_relation_language_bridge_v1'
SEED = 2026100662
CHANGED = ('negation', 'comparison')
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006')
CONTROL_DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-transfer-curriculum-20261006-v2')
PAST_NEGATIVE = {
    '食べた': '食べなかった', '飲んだ': '飲まなかった', '読んだ': '読まなかった',
    '切った': '切らなかった', '開けた': '開けなかった', '書いた': '書かなかった',
    '買った': '買わなかった', '洗った': '洗わなかった', '飾った': '飾らなかった',
    '撮った': '撮らなかった', 'かぶった': 'かぶらなかった', '運んだ': '運ばなかった',
}


def render(f, form, branch):
    if f['category'] not in CHANGED or form not in range(6) or branch not in (0, 1):
        raise ValueError('Two grounded relation categories / six forms / two opposed states required')
    a, b = f['A'], f['B']
    state = original.render(f, form, branch)['local_state']
    if f['category'] == 'negation':
        obj, verb = f['object'], f['positive']
        negative = PAST_NEGATIVE[verb]
        action = verb if branch == 0 else negative
        choices = [f'今朝、{a}は{obj}を{v}。' for v in (verb, negative)]
        truth = '正しい' if branch == 0 else '誤っている'
        fact = '事実だ' if branch == 0 else '事実ではない'
        membership = f'{obj}を{verb}のは{a}だ' if branch == 0 else f'{obj}を{verb}人に{a}は含まれない'
        existence = '実際にあった' if branch == 0 else 'なかった'
        prefixes = (
            f'{a}は今朝、{obj}を{action}。その行動を言い直すと、',
            f'{a}が今朝{obj}を{verb}という記録について調べた。その記録は{truth}。実際の出来事は、',
            f'{a}が今朝{obj}を{verb}という話は、{fact}。確認した出来事を述べると、',
            f'今朝、{membership}。{a}の今朝の行動をまとめると、',
            f'今朝、{a}が{obj}を{verb}かどうかを確かめた。その行動は{existence}。確認した結果は、',
            f'「今朝、{a}は{obj}を{verb}」という一文の内容を調べた。その一文の内容は{truth}。出来事を正しく言い直すと、',
        )
    else:
        longer, shorter = (a, b) if branch == 0 else (b, a)
        choices = [f'{a}である。', f'{b}である。']
        first = f'{longer}の棒は{shorter}の棒より長い。'
        inverse = f'{shorter}の棒は{longer}の棒より短い。'
        relation = first if f['sequence'] == '先' else inverse
        prefixes = (
            relation + '長い方の棒を持っているのは、',
            inverse + '二人のうち、長い棒を持つ人は、',
            f'{a}と{b}の棒の長さは異なる。{shorter}の棒より長いのは{longer}の棒だ。長い方の持ち主は、',
            f'{shorter}の棒は{longer}の棒ほど長くない。長い方の棒を選ぶと、持ち主は、',
            f'{longer}の棒よりも{shorter}の棒の方が短かった。二本のうち長い棒の持ち主は、',
            f'二人の棒の長さは異なる。短い方を持っているのは{shorter}で、もう一人は{longer}だ。長い方を持つ人は、',
        )
        # Keep the original unequal lengths / presentation-order information,
        # but do not assign either number to a person: the relation still matters.
        low, high = f['length'], f['length'] + f['gap']
        values = (low, high) if f['sequence'] == '先' else (high, low)
        header = f'二本の棒の長さは{values[0]}センチと{values[1]}センチである。'
        prefixes = tuple(header + prefix for prefix in prefixes)
    return dict(prefix=prefixes[form], choices=choices, label=branch, local_state=state)


def generate(control):
    families = copy.deepcopy(control['families'])
    before = {r['id']: r for r in control['rows']}
    rows = []
    for family in families:
        if family['category'] in CHANGED:
            family['branches'] = [render(family['facts'], family['form'], b) for b in (0, 1)]
        for branch in family['branches']:
            row = copy.deepcopy(before[f'{family["id"]}-{branch["label"]}'])
            if family['category'] in CHANGED:
                text = branch['prefix'] + branch['choices'][branch['label']]
                row.update(prefix=branch['prefix'], choices=branch['choices'], outcome=branch['choices'][branch['label']],
                           text=text, text_sha256=original.digest(text), cut=len(branch['prefix']), end=len(text))
            rows.append(row)
    rng = random.Random(SEED)
    known = {r['text_sha256'] for r in rows}
    groups = {'train': families}
    for split in ('lexical_holdout', 'structural_holdout'):
        groups[split] = []
        for i in range(64):
            cat = CHANGED[i % 2]
            form = (i // 2) % 4 if split == 'lexical_holdout' else 4 + (i // 2) % 2
            for attempt in range(64):
                f = original.facts(cat, rng, split)
                branches = [render(f, form, b) for b in (0, 1)]
                hashes = [original.digest(b['prefix'] + b['choices'][b['label']]) for b in branches]
                if not any(h in known for h in hashes):
                    known.update(hashes)
                    groups[split].append(dict(id=f'relation-{split}-{i:04d}', split=split, category=cat,
                        template_id=f'relation-{cat}-{form}', form=form, facts=f, branches=branches,
                        generation_attempt=attempt + 1))
                    break
            else:
                raise ValueError('Bounded local probe uniqueness exhausted; preserve fixed draws')
    return groups, rows


def validate_replacement(control, groups, rows):
    if len(rows) != 2048 or len(groups['train']) != 1024:
        raise ValueError('Original2048 documents/1024 families required')
    changed = []
    immutable = ('id', 'split', 'family', 'category', 'template_id', 'facts', 'local_state', 'label', 'source')
    for before, after in zip(control['rows'], rows, strict=True):
        if any(before[k] != after[k] for k in immutable):
            raise ValueError('Bridge changed selected train IDs/facts/labels/provenance')
        if before['category'] in CHANGED:
            expected = render(after['facts'], int(after['template_id'].rsplit('-', 1)[1]), after['label'])
            if any(after[k] != expected[k] for k in ('prefix', 'choices', 'local_state')):
                raise ValueError('Train conclusion disagrees with declared local state')
            if before['text'] == after['text']:
                raise ValueError('Declared changed category was not replaced')
            changed.append(after['id'])
        elif before != after:
            raise ValueError('Bridge changed one of the other four categories')
    for before, after in zip(control['families'], groups['train'], strict=True):
        if {k: v for k, v in before.items() if k != 'branches'} != {k: v for k, v in after.items() if k != 'branches'}:
            raise ValueError('Bridge changed selected family facts/order/seed draw')
        for old, new in zip(before['branches'], after['branches'], strict=True):
            if old['label'] != new['label'] or old['local_state'] != new['local_state']:
                raise ValueError('Bridge changed opposed local states')
            if before['category'] not in CHANGED and old != new:
                raise ValueError('Bridge changed unrelated family')
            if before['category'] in CHANGED and new != render(after['facts'], after['form'], new['label']):
                raise ValueError('Train family disagrees with declared local state')
    if len({r['text_sha256'] for r in rows}) != 2048 or len({r['template_id'] for r in rows}) != 24:
        raise ValueError('Do not inflate duplicate material/structure counts')
    train_hashes = {r['text_sha256'] for r in rows}
    probe_ids = set()
    probe_hashes = set()
    for split in ('lexical_holdout', 'structural_holdout'):
        if len(groups[split]) != 64:
            raise ValueError('All128 new opposed probe families required')
        for family in groups[split]:
            if family['id'] in probe_ids or family['id'] in {f['id'] for f in groups['train']}:
                raise ValueError('Probe family overlaps train or duplicate')
            probe_ids.add(family['id'])
            if split == 'lexical_holdout' and any(family['facts'][k] in original.TRAIN_NAMES for k in ('A', 'B')):
                raise ValueError('Lexical entities overlap train')
            if (split == 'structural_holdout' and family['form'] not in (4, 5)) or (split == 'lexical_holdout' and family['form'] not in range(4)):
                raise ValueError('Held-out grammatical form assignment differs')
            expected = [render(family['facts'], family['form'], b) for b in (0, 1)]
            if family['branches'] != expected:
                raise ValueError('Probe conclusions/local state changed')
            for branch in expected:
                h = original.digest(branch['prefix'] + branch['choices'][branch['label']])
                if h in train_hashes or h in probe_hashes:
                    raise ValueError('Probe body overlaps train or duplicate')
                probe_hashes.add(h)
    for row in rows:
        if row['text'] != row['prefix'] + row['outcome'] or row['text_sha256'] != original.digest(row['text']) or row['outcome'] != row['choices'][row['label']]:
            raise ValueError('Native continuation bytes or opposed outcome differs')
    return dict(changed_documents=len(changed), changed_ids=changed, other_four_categories_byte_exact=True,
        original_selected_families_facts_labels_order_preserved=True, all24_train_structures=True,
        all2048_train_bodies_unique=True, lexical_entities_disjoint=True, new_held_grammatical_forms_disjoint=True,
        all128_new_probe_families_disjoint=True, probe_bodies_absent_from_train=True,
        original128_retention_probes_not_new_heldout_evidence=True)


class RelationLanguageTrainView:
    """Own generated kind; original accepted/frozen loader remains unchanged."""
    def __init__(self, path, manifest_sha256, require_accepted=True):
        self.directory = Path(path)
        if sha256(self.directory/'manifest.json') != manifest_sha256:
            raise ValueError('Relation bridge manifest differs')
        m = self.manifest = read_json(self.directory/'manifest.json')
        if (m['kind'] != KIND or m['source'] != 'local_programmatic_Japanese' or m['documents'] != 2048
                or m['newly_prepared_original_corpus_tokens'] != 0 or sha256(self.directory/'train.npz') != m['arrays_sha256']
                or m['tokenizer_sha256'] != 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'):
            raise ValueError('Relation bridge generated provenance differs')
        if require_accepted:
            review = read_json(self.directory/'content-review.json')
            if (not review['all64_read'] or not review['training_pool_accepted'] or review['weak_documents'] > 10
                    or review['unresolved_grammar_documents'] or review['pilot_sha256'] != m['pilot_sha256']
                    or review['manifest_sha256'] != manifest_sha256
                    or review['notes_sha256'] != sha256(self.directory/'content-notes.json')):
                raise ValueError('Accepted raw-bound fixed64 required')
        with np.load(self.directory/'train.npz', allow_pickle=False) as arrays:
            self.tokens = arrays['tokens'].copy(); self.focus = arrays['focus'].astype(bool)
            self.offsets = arrays['offsets'].copy(); self.lengths = arrays['lengths'].copy()
        if (len(self.offsets) != 2048 or len(self.tokens) != m['serialized_tokens'] or self.focus.shape != self.tokens.shape
                or int(self.focus.sum()) != m['outcome_focus_body_targets'] or not np.array_equal(self.offsets, np.r_[0, np.cumsum(self.lengths)[:-1]])
                or int(self.lengths.sum()) != len(self.tokens) or np.any(self.focus & (self.tokens < 8))
                or np.count_nonzero(self.tokens == 2) != 2048 or np.count_nonzero(self.tokens == 3) != 2048
                or not np.all(self.tokens[self.offsets] == 2) or not np.all(self.tokens[self.offsets+self.lengths-1] == 3)
                or np.any(self.tokens >= 4096) or np.any(np.isin(self.tokens, [0, 1, 4, 5, 6, 7]))):
            raise ValueError('Relation bridge whole body/EOS encoding differs')
        self.manifest_sha256 = manifest_sha256
