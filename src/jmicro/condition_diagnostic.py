"""Authored, counterfactual condition-learning material, separate from fixed evals."""
import hashlib
import random

CATEGORIES = ('reference', 'quantity', 'negation', 'time', 'cause')
TRAIN_NAMES = ('あおい', 'ひなた', 'みどり', 'なお', 'ゆう', 'まこと', 'はる', 'りょう',
               'あきら', 'けん', 'さくら', 'たくみ', 'なつ', 'ふみ', 'まい', 'りん',
               'えり', 'かず', 'ほのか', 'れん')
DEV_NAMES = ('しおり', 'さとる', 'かえで', 'つばさ', 'すみれ', 'いおり')
OBJECTS = ('本', '封筒', '写真', '手紙', 'ノート', '鍵', '袋', '帽子')
FOODS = ('パン', 'おにぎり', 'うどん', 'そば', 'りんご', 'みかん', 'せんべい', 'クッキー')
ACTIONS = ('窓を開ける', '机を拭く', '靴を磨く', '手を洗う', '花に水をやる', '本を読む')


def render(category, a, b, x, y, n, k, variant, template):
    """Two conditions share the exact answer options; the correct one reverses.

    Templates 0..3 are eligible for train; 4 is reserved for structural dev.
    Every correct continuation is supervised with ordinary Base body/EOS loss.
    """
    if category == 'reference':
        giver, receiver = (a, b) if variant == 0 else (b, a)
        choices = [f'{a}が持っている。', f'{b}が持っている。']
        setups = [f'{giver}は{x}を{receiver}に渡した。{receiver}は受け取った。',
                  f'{x}は最初{giver}の手にあった。{giver}が{receiver}に手渡し、{receiver}が受け取った。',
                  f'{giver}が{x}を持ってきた。それを{receiver}に渡した後、{giver}は手を離した。',
                  f'{receiver}は{giver}から{x}を受け取った。{giver}の手にはもう{x}がない。',
                  f'{giver}から{receiver}へ{x}が手渡された。受け渡しは済み、その後は移動していない。']
        question = f'今、{x}は誰が持っているか。'
        label = 1 - variant
        rationale = f'受け取り後の保持者は{receiver}。以後の移動なし。'
    elif category == 'quantity':
        if not 0 < k < n or n + k > 19:
            raise ValueError('Quantity range invalid')
        choices = [f'{n-k}個ある。', f'{n+k}個ある。']
        setups = [f'{a}は{x}を{n}個持っていた。その後、{k}個を友達に渡した。' if variant == 0 else
                  f'{a}は{x}を{n}個持っていた。その後、友達から{k}個もらった。',
                  f'初め、{a}の{x}は{n}個だった。{a}は友達と会い、{k}個を'+('渡した。' if variant == 0 else '受け取った。'),
                  f'{a}が持っていた{x}は{n}個である。そこから{k}個が'+('友達の手に移った。' if variant == 0 else '友達から加わった。'),
                  f'{x}を{n}個用意した{a}は、友達に'+(f'{k}個を分けてあげた。' if variant == 0 else f'{k}個を分けてもらった。'),
                  f'{a}の手元にあった{x}{n}個は、友達との受け渡しで'+(f'{k}個減った。' if variant == 0 else f'{k}個増えた。')]
        question = f'それ以外の増減はない。今、{a}の{x}はいくつあるか。'
        label = variant
        rationale = f'{n}'+('-' if variant == 0 else '+')+f'{k}={n-k if variant == 0 else n+k}。'
    elif category == 'negation':
        banned, selected = (x, y) if variant == 0 else (y, x)
        choices = [f'{x}を食べる。', f'{y}を食べる。']
        setups = [f'{a}は今日は{banned}を食べないと決めた。食べ物は{x}と{y}だけで、どちらか一つを食べる。',
                  f'今日の食事は{x}か{y}のどちらかである。{a}は{banned}を食べないと決めている。',
                  f'{a}は{x}と{y}から一つを選ぶ。ただし{banned}は今日は食べない。',
                  f'{x}と{y}が並んでいる。{a}は一つを食べるが、{banned}は選ばないと約束した。',
                  f'{a}が食べられる候補は{x}と{y}の二つだけだ。そのうち{banned}を食べないという約束を守る。']
        question = f'{a}は決めたことを守る。何を食べるか。'
        label = 1 - variant
        rationale = f'二択で{banned}を除外したので{selected}。'
    elif category == 'time':
        first, second = (x, y) if variant == 0 else (y, x)
        choices = [f'「{x}」が先である。', f'「{y}」が先である。']
        setups = [f'{a}は「{first}」を終えてから「{second}」をした。',
                  f'{a}が「{second}」をしたのは、「{first}」を終えた後だった。',
                  f'{a}はまず「{first}」をした。次に「{second}」をした。',
                  f'「{second}」より前に、{a}は「{first}」を済ませていた。',
                  f'{a}の行動は「{first}」、続いて「{second}」という順番だった。']
        question = 'この二つの行動のうち、先にしたのはどちらか。'
        label = variant
        rationale = f'明示された順序は{first}→{second}。'
    elif category == 'cause':
        action = '押した' if variant == 0 else '押さなかった'
        choices = ['明かりはついている。', '明かりは消えている。']
        setups = [f'明かりは初め消えていた。このスイッチを押すと明かりがつく。{a}はスイッチを{action}。',
                  f'部屋の明かりは消えている。スイッチを押すことだけで明かりをつけられる。{a}はそれを{action}。',
                  f'{a}の前に、消えている明かりのスイッチがある。押せば明かりがつく。{a}はスイッチを{action}。',
                  f'初めは明かりがついていない。{a}は、押すと明かりがつくスイッチを{action}。',
                  f'スイッチの操作前、明かりは消えていた。押すと点灯する仕組みで、{a}はスイッチを{action}。']
        question = '他の操作や変化はない。今の明かりはどうなっているか。'
        label = variant
        rationale = '初期消灯、押すことだけで点灯、他の変化なし。'+('押したので点灯。' if variant == 0 else '押さず消灯のまま。')
    else:
        raise ValueError(category)
    scene = f'{a}は{x}が置かれた部屋にいる。' if category == 'cause' else ''
    prefix = scene + setups[template] + question + '\n'
    return dict(category=category, prefix=prefix, choices=choices, label=label,
                text=prefix+choices[label], rationale=rationale, template=template)


def make_pairs(split, count_per_category, templates, seed):
    rng = random.Random(seed)
    names = DEV_NAMES if split == 'dev' else TRAIN_NAMES
    records, seen = [], set()
    for category in CATEGORIES:
        made = attempts = 0
        while made < count_per_category:
            attempts += 1
            if attempts > count_per_category * 1000:
                raise ValueError('Requested unique supply exceeds renderer capacity')
            a, b = rng.sample(names, 2)
            x, y = rng.sample(ACTIONS if category == 'time' else FOODS if category == 'negation' else OBJECTS, 2)
            n = rng.randrange(3, 13); k = rng.randrange(1, min(n, 20-n))
            template = templates[made % len(templates)]
            pair = [render(category, a, b, x, y, n, k, v, template) for v in (0, 1)]
            key = tuple(row['text'] for row in pair)
            if any(text in seen for text in key):
                continue
            seen.update(key)
            for variant, row in enumerate(pair):
                row.update(id=f'{split}-{category}-{made:04d}-{variant}',
                           family=f'{split}-{category}-{made:04d}', split=split,
                           variant=variant, structural_holdout=template==4)
                row['canonical_sha256'] = hashlib.sha256(row['text'].encode()).hexdigest()
                records.append(row)
            made += 1
    return records


def summarize_choice(rows):
    families = {}
    for row in rows:
        families.setdefault(row['family'], []).append(row['correct'])
    if any(len(v) != 2 for v in families.values()):
        raise ValueError('Counterfactual pairs incomplete')
    return dict(total=len(rows), correct=sum(r['correct'] for r in rows),
                accuracy=sum(r['correct'] for r in rows)/len(rows),
                pairs=len(families), both_correct=sum(all(v) for v in families.values()),
                both_accuracy=sum(all(v) for v in families.values())/len(families))
