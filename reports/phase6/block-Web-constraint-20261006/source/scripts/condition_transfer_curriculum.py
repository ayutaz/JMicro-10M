"""Locally authored plain Base text; explicit local states, split provenance."""
import hashlib
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import read_json, sha256

SEED = 2026100660
KIND = 'local_self_contained_condition_curriculum_v2'
CATEGORIES = ('negation', 'quantity', 'time', 'comparison', 'entity_reference', 'causality')
TRAIN_NAMES = ('あかね', 'ひなた', 'つばさ', 'みなと', 'さくら', 'しおり', 'たくみ', 'なお',
               'かおる', 'ゆうき', 'まこと', 'りょう', 'すみれ', 'はるか', 'あおい', 'いずみ')
LEXICAL_NAMES = ('こはる', 'つむぎ', 'あさひ', 'ちひろ', 'ほのか', 'なぎさ', 'せいじ', 'りつ')
TRAIN_ACTIONS = (('パン', '食べた', '食べていない'), ('水', '飲んだ', '飲んでいない'),
                 ('本', '読んだ', '読んでいない'), ('紙', '切った', '切っていない'),
                 ('窓', '開けた', '開けていない'), ('手紙', '書いた', '書いていない'),
                 ('靴', '買った', '買っていない'), ('皿', '洗った', '洗っていない'))
LEXICAL_ACTIONS = (('花', '飾った', '飾っていない'), ('写真', '撮った', '撮っていない'),
                   ('帽子', 'かぶった', 'かぶっていない'), ('荷物', '運んだ', '運んでいない'))
TRAIN_ITEMS = (('りんご', '個'), ('みかん', '個'), ('箱', '個'), ('石', '個'),
               ('本', '冊'), ('ノート', '冊'), ('紙', '枚'), ('カード', '枚'))
LEXICAL_ITEMS = (('消しゴム', '個'), ('電池', '個'), ('雑誌', '冊'), ('写真', '枚'))
TRAIN_ACTIVITIES = ('読書', '練習', '作業', '散歩', '掃除', '勉強')
LEXICAL_ACTIVITIES = ('見学', '買い物', '昼寝', '集会')


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def facts(category, rng, split):
    lexical = split == 'lexical_holdout'
    names = LEXICAL_NAMES if lexical else TRAIN_NAMES
    a, b = rng.sample(names, 2)
    item, unit = rng.choice(LEXICAL_ITEMS if lexical else TRAIN_ITEMS)
    obj, positive, negative = rng.choice(LEXICAL_ACTIONS if lexical else TRAIN_ACTIONS)
    structural = split == 'structural_holdout'
    return dict(category=category, A=a, B=b, item=item, unit=unit, object=obj,
                positive=positive, negative=negative,
                x=rng.randint(30, 48) if structural else rng.randint(8, 20),
                delta=rng.randint(6, 10) if structural else rng.randint(1, 5),
                hour=rng.randint(9, 16), duration=rng.randint(1, 3),
                activity=rng.choice(LEXICAL_ACTIVITIES if lexical else TRAIN_ACTIVITIES),
                length=rng.randint(5, 40), gap=rng.randint(1, 12),
                sequence=rng.choice(('先', '後')))


def render(f, form, branch):
    """Two explicitly opposed local states with SAME two candidate strings."""
    if form not in range(6) or branch not in (0, 1):
        raise ValueError('Fixed structure and opposed branch required')
    a, b, item, unit = (f[k] for k in ('A', 'B', 'item', 'unit'))
    cat = f['category']
    if cat == 'negation':
        obj = f['object']; state = f['positive'] if branch == 0 else f['negative']
        choices = [f'{a}は今朝、{obj}を{v}。' for v in (f['positive'], f['negative'])]
        prefixes = (
            f'{a}の日記には、今朝は{obj}を{state}と書いてある。この記録によると、',
            f'今朝の{a}の行動が確認された。{obj}を{state}ことは確かだ。つまり、',
            f'{a}についての記録を読んだ。今朝、{obj}を{state}との記載がある。その記録によると、',
            f'今朝の出来事をまとめる。{a}は{obj}を{state}。記録に残すと、',
            f'{a}が今朝{obj}を{f["positive"]}という話は、' + ('事実だった。' if branch == 0 else '事実ではなかった。') + '確認できた内容は、',
            f'確かめたところ、今朝は{obj}を{state}ことが分かった。その行動をした人は{a}である。記録には、')
        state_record = dict(did_action=branch == 0, morning=True)
    elif cat == 'quantity':
        x, d = f['x'], f['delta']; value = x + d if branch == 0 else x - d
        choices = [f'{x+d}{unit}である。', f'{x-d}{unit}である。']
        change = f'{d}{unit}を加えた' if branch == 0 else f'{d}{unit}を取り出した'
        location = 'そこへ' if branch == 0 else 'そこから'
        received = f'{d}{unit}を受け取った' if branch == 0 else f'{d}{unit}を渡した'
        prefixes = (
            f'{a}の箱には{item}が{x}{unit}あった。{location}{change}。いま箱にある{item}は、',
            f'{a}は{item}を{x}{unit}持っていた。そのあと{received}。現在の所持数は、',
            f'店に{item}が{x}{unit}残っている。{location}{change}。変更後の店の在庫数は、',
            f'{item}を数えると{x}{unit}あった。続いて{change}。現在の合計は、',
            f'{item}を{x}{unit}と数え、記録した。{location}{change}。変更後の{item}の数は、',
            f'{a}が並べた{item}は{x}{unit}だった。{location}{change}。いま並んでいる数は、')
        state_record = dict(initial=x, delta=d, operation='add' if branch == 0 else 'subtract', final=value)
    elif cat == 'time':
        h, d, activity = f['hour'], f['duration'], f['activity']
        shift = f'{d}時間早めた' if branch == 0 else f'{d}時間遅らせた'
        choices = [f'{h-d}時になった。', f'{h+d}時になった。']
        prefixes = (
            f'{a}は{h}時に{activity}を始める予定だった。開始を{shift}。新しい開始時刻は、',
            f'{activity}の開始予定は{h}時だったが、{shift}。変更後の開始は、',
            f'予定表には{activity}を{h}時から始めると書いてあった。開始を{shift}ので、その時刻は、',
            f'{a}の{activity}は、当初{h}時に始まる予定だった。開始を{shift}ところ、開始時刻は、',
            f'時計の時刻を24時間表記で記録する。{activity}は{h}時に開始する予定を、{shift}。変更後の予定は、',
            f'{activity}の予定を変更した。元の開始時刻は{h}時であり、それを{shift}。時計に示す開始時刻は、')
        state_record = dict(initial_hour=h, delta_hours=d, operation='earlier' if branch == 0 else 'later', final_hour=h-d if branch == 0 else h+d)
    elif cat == 'comparison':
        lo, gap = f['length'], f['gap']; la, lb = (lo+gap, lo) if branch == 0 else (lo, lo+gap)
        choices = [f'{a}である。', f'{b}である。']
        first = f'{a}の棒は{la}センチ、{b}の棒は{lb}センチだ。'
        second = f'{b}の棒は{lb}センチ、{a}の棒は{la}センチだ。'
        record = first if f['sequence'] == '先' else second
        prefixes = (
            record + 'より長い棒を持つ人は、',
            f'二人の棒を測った。{record}長さが大きい方の持ち主は、',
            f'棒の長さを記録する。{record}長い方の棒を選ぶと、その持ち主は、',
            f'二本の棒を並べた。{record}短い方ではなく長い方を持っているのは、',
            f'測定記録を見直す。{record}長さの数値を比べて大きい方を選ぶと、持ち主は、',
            f'{record}二本から一方を選ぶ。短い方を除いた棒を持っているのは、')
        state_record = dict(A_length=la, B_length=lb, longer=a if la > lb else b)
    elif cat == 'entity_reference':
        choices = [f'{a}である。', f'{b}である。']
        target, other = (a, b) if branch == 0 else (b, a)
        prefixes = (
            f'{other}が{item}を{target}に渡した。その{item}を受け取った人は、',
            f'{target}が{item}を{other}へ届けた。その{item}を届けた人は、',
            f'この{item}の持ち主は{target}だ。{other}はそれを借りた。借りる前の持ち主は、',
            f'{other}は「つき」、{target}は「ほし」という別名で呼ばれている。「ほし」と呼ばれる人は、',
            f'{target}から{other}へ{item}が渡り、その後{other}から{target}に戻った。最後にそれを持つ人は、',
            f'{other}は{item}を持っていた。それを{target}へ渡し、返してもらっていない。いまそれを持つ人は、')
        state_record = dict(target=target, relation=('receiver', 'sender', 'original_owner', 'alias', 'returned_owner', 'current_owner')[form])
    elif cat == 'causality':
        # Each device's state rules are declared locally; no empirical/world fact inference.
        choices = ['ライトは点灯している。', 'ライトは消えている。']
        operation = 'オン' if branch == 0 else 'オフ'
        pressed = '押している' if branch == 0 else '押していない'
        left = '左' if branch == 0 else '右'
        lever = '上' if branch == 0 else '下'
        prefixes = (
            f'この装置のライトは、スイッチがオンなら点灯し、オフなら消える設定だ。{a}はスイッチを{operation}にした。設定に従うと、',
            f'このライトは、ボタンを押している間は点灯し、押していない間は消える仕組みだ。今はボタンを{pressed}状態である。そのため、',
            f'この装置は、左の位置でライトが点灯し、右の位置で消える設定だ。{a}はつまみを{left}に合わせた。その結果、',
            f'レバーが上にあるとライトが点灯し、下にあると消える装置だ。いまレバーは{lever}にある。仕組みに従って、',
            '二つのスイッチがどちらもオンの時だけライトが点灯し、それ以外は消える装置だ。一つ目はオンで、二つ目は' + operation + 'である。設定に従うと、',
            '二つのスイッチのうち少なくとも一つがオンならライトが点灯し、両方オフなら消える装置だ。一つ目はオフで、二つ目は' + operation + 'である。設定に従うと、')
        prefixes = tuple(f'{a}が{item}をしまう箱に、小さなライトが付いている。'+prefix for prefix in prefixes)
        state_record = dict(on=branch == 0, mechanism=('switch', 'button', 'position', 'lever', 'AND', 'OR')[form])
    else:
        raise ValueError('Unknown grounded category')
    return dict(prefix=prefixes[form], choices=choices, label=branch, local_state=state_record)


def build_family(index, split, rng, form=None):
    category = CATEGORIES[index % 6]
    if form is None:
        form = (index // 6) % 4 if split != 'structural_holdout' else 4 + (index // 6) % 2
    f = facts(category, rng, split)
    branches = [render(f, form, b) for b in (0, 1)]
    if branches[0]['choices'] != branches[1]['choices'] or len(set(branches[0]['choices'])) != 2:
        raise ValueError('Opposed local states require common distinct candidates')
    return dict(id=f'{split}-{index:04d}', split=split, category=category, template_id=f'{category}-{form}',
                form=form, facts=f, branches=branches)


def generate():
    rng = random.Random(SEED)
    groups = {}; known = set()
    for split, n in (('train', 1024), ('lexical_holdout', 64), ('structural_holdout', 64)):
        group = []; groups[split] = group
        for i in range(n):
            for attempt in range(64):
                family = build_family(i, split, rng)
                bodies = [digest(b['prefix']+b['choices'][b['label']]) for b in family['branches']]
                if not any(h in known for h in bodies):
                    known.update(bodies); family['generation_attempt'] = attempt+1
                    group.append(family); break
            else:
                raise ValueError('Bounded local exact-body uniqueness exhausted')
    rows = []
    for family in groups['train']:
        for branch in family['branches']:
            text = branch['prefix'] + branch['choices'][branch['label']]
            rows.append(dict(id=f'{family["id"]}-{branch["label"]}', split='train',
                family=family['id'], category=family['category'], template_id=family['template_id'],
                text=text, text_sha256=digest(text), prefix=branch['prefix'], outcome=branch['choices'][branch['label']],
                cut=len(branch['prefix']), end=len(text), source='local_programmatic_Japanese',
                facts=family['facts'], local_state=branch['local_state'], choices=branch['choices'], label=branch['label']))
    return groups, rows


def validate_split(groups, rows):
    if (len(rows) != 2048 or len({r['text_sha256'] for r in rows}) != 2048
            or any(r['text_sha256'] != digest(r['text']) or r['text'] != r['prefix']+r['outcome']
                   or r['outcome'] != r['choices'][r['label']] or r['split'] != 'train' for r in rows)):
        raise ValueError('Complete distinct declared train documents required')
    if set(groups) != {'train', 'lexical_holdout', 'structural_holdout'} or [len(groups[s]) for s in groups] != [1024, 64, 64]:
        raise ValueError('Fixed1024 train and128 separate probe families required')
    if len({r['template_id'] for r in rows}) != 24:
        raise ValueError('All24 train structures required')
    train_templates = {r['template_id'] for r in rows}
    train_hashes = {r['text_sha256'] for r in rows}
    probe_hashes = set()
    for split in ('lexical_holdout', 'structural_holdout'):
        for family in groups[split]:
            if family['split'] != split or len(family['branches']) != 2 or {b['label'] for b in family['branches']} != {0, 1}:
                raise ValueError('Complete opposed probe family required')
            if split == 'lexical_holdout' and any(family['facts'][k] in TRAIN_NAMES for k in ('A', 'B')):
                raise ValueError('Lexical entity holdout leaked')
            if split == 'structural_holdout' and family['template_id'] in train_templates:
                raise ValueError('Structural template holdout leaked')
            for branch in family['branches']:
                body_hash = digest(branch['prefix']+branch['choices'][branch['label']])
                if body_hash in train_hashes:
                    raise ValueError('Probe text included in train')
                if body_hash in probe_hashes:
                    raise ValueError('Duplicate probe body inflates evidence')
                probe_hashes.add(body_hash)
    return dict(local_exact_train_body_unique=True, all24_train_structures=True,
                lexical_entities_disjoint=True, structural_template_ids_disjoint=True,
                all128_probe_family_ids_disjoint=True, probe_complete_bodies_absent_from_train=True)


class CurriculumTrainView:
    """Same stream protocol as PositiveTrainView, with honest GENERATED provenance."""
    def __init__(self, path, manifest_sha256, require_accepted=True):
        self.directory = Path(path)
        if sha256(self.directory / 'manifest.json') != manifest_sha256:
            raise ValueError('Generated curriculum manifest differs')
        self.manifest = read_json(self.directory / 'manifest.json')
        m = self.manifest
        if (m['kind'] != KIND or m['source'] != 'local_programmatic_Japanese'
                or m['documents'] != 2048 or m['newly_prepared_original_corpus_tokens'] != 0
                or sha256(self.directory / 'train.npz') != m['arrays_sha256']
                or m['tokenizer_sha256'] != 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'):
            raise ValueError('Generated provenance/codec/arrays differ')
        if require_accepted:
            review_path = self.directory / 'content-review.json'
            review = read_json(review_path)
            if (not review['all64_read'] or not review['training_pool_accepted'] or review['weak_documents'] > 10
                    or review['pilot_sha256'] != m['pilot_sha256'] or review['manifest_sha256'] != manifest_sha256):
                raise ValueError('Accepted individually read fixed64 required')
        with np.load(self.directory / 'train.npz', allow_pickle=False) as arrays:
            self.tokens = arrays['tokens'].copy(); self.focus = arrays['focus'].astype(bool)
            self.offsets = arrays['offsets'].copy(); self.lengths = arrays['lengths'].copy()
        if (len(self.offsets) != 2048 or len(self.tokens) != m['serialized_tokens']
                or self.focus.shape != self.tokens.shape or int(self.focus.sum()) != m['outcome_focus_body_targets']
                or not np.array_equal(self.offsets, np.r_[0, np.cumsum(self.lengths)[:-1]])
                or int(self.lengths.sum()) != len(self.tokens) or np.any(self.focus & (self.tokens < 8))
                or np.count_nonzero(self.tokens == 2) != 2048 or np.count_nonzero(self.tokens == 3) != 2048
                or not np.all(self.tokens[self.offsets] == 2) or not np.all(self.tokens[self.offsets+self.lengths-1] == 3)
                or np.any(self.tokens >= 4096) or np.any(np.isin(self.tokens, [0, 1, 4, 5, 6, 7]))):
            raise ValueError('Generated whole body+EOS IDs/masks differ')
        self.manifest_sha256 = manifest_sha256
