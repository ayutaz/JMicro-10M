"""TRAIN-only authored narratives. No evaluation data or new factual draws."""
import copy
import random
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import read_json, sha256
from condition_transfer_curriculum import CATEGORIES, TRAIN_NAMES, TRAIN_ACTIONS, TRAIN_ITEMS, TRAIN_ACTIVITIES, digest, render as original_state

KIND = 'locally_authored_TRAIN_grounded_short_narratives_v1'
SOURCE = 'local_programmatic_Japanese_not_public_corpus_or_public_teacher'
SEED = 2026100691
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/narrative-condition-source-20261006')
TOKENIZER_SHA = 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'

# Authored fictional scenes supplement, rather than replace, the TRAIN kernel.
# Four scene introductions preserve a distinction between original source forms.
MEETINGS = ('一緒に{place}へ行き', '{place}で待ち合わせ', '{place}で会い', '{place}に立ち寄り')
NEGATION = {
    '食べた': ('食堂', '皿にパンが一つ載っていた', 'パンを全部食べた', 'パンを食べなかった',
               '皿は空になった', 'パンは皿に残った', '空の皿を片づけた', '残ったパンを袋にしまった'),
    '飲んだ': ('休憩室', 'コップに水が入っていた', 'コップの水を全部飲んだ', '水を飲まなかった',
               'コップは空になった', '水はコップに残った', '空のコップを流しに運んだ', '水の入ったコップを机の端に置いた'),
    '読んだ': ('読書室', 'まだ読み終えていない本が机にあった', '本を最後のページまで読んだ', '本を読まなかった',
               '読みかけだった本を読み終えた', '本は読みかけのままだった', '読み終えた本を棚に戻した', '続きをあとで読むために本をかばんに入れた'),
    '切った': ('作業室', '一枚の紙が机に置いてあった', '紙を半分に切った', '紙を切らなかった',
               '紙は二枚に分かれた', '紙は一枚のまま残った', '二枚の紙を重ねて置いた', '切っていない紙を引き出しにしまった'),
    '開けた': ('談話室', '窓は閉まっていた', '窓を開けた', '窓を開けなかった',
               '窓は開いた状態になった', '窓は閉まったままだった', '開いた窓のそばに椅子を置いた', '閉じた窓のそばに椅子を置いた'),
    '書いた': ('書斎', '机には白い便箋が置いてあった', 'その便箋に手紙を書いた', '手紙を書かなかった',
               '便箋には文字が並んだ', '便箋は白いままだった', '書いた手紙を封筒に入れた', '白い便箋を引き出しに戻した'),
    '買った': ('靴売り場', '棚には新しい靴が並んでいた', '靴を一足買った', '靴を買わなかった',
               '新しい靴を持ち帰れることになった', '新しい靴を持ち帰ることはなかった', '買った靴を袋に入れて店を出た', '財布をしまって店を出た'),
    '洗った': ('台所', '流しには汚れた皿があった', '皿をきれいに洗った', '皿を洗わなかった',
               '皿の汚れは落ちた', '皿は汚れたままだった', '洗った皿を水切りかごに置いた', '汚れた皿をあとで洗うために流しに残した'),
}


def render(family, branch, surface):
    if family['split'] != 'train' or family['category'] not in CATEGORIES or family['form'] not in range(4):
        raise ValueError('Only accepted TRAIN families/forms may supply narratives')
    if type(branch) is not int or branch not in (0, 1) or type(surface) is not int or surface not in range(8):
        raise ValueError('Two branches and eight surfaces required')
    f = family['facts']; cat = family['category']; form = family['form']
    a, b, item, unit = (f[k] for k in ('A', 'B', 'item', 'unit'))
    if (f['category'] != cat or a == b or a not in TRAIN_NAMES or b not in TRAIN_NAMES
            or (f['object'], f['positive'], f['negative']) not in TRAIN_ACTIONS
            or (item, unit) not in TRAIN_ITEMS or f['activity'] not in TRAIN_ACTIVITIES):
        raise ValueError('TRAIN name/action/item/activity banks required')
    expected = original_state(f, form, branch)['local_state']
    given = next(v for v in family['branches'] if v['label'] == branch)
    if given['local_state'] != expected:
        raise ValueError('Accepted local state disagrees with TRAIN facts')
    if cat == 'negation':
        place, initial, positive, negative, yes, no, yes_next, no_next = NEGATION[f['positive']]
        action, result, follow = (positive, yes, yes_next) if branch == 0 else (negative, no, no_next)
        meet = MEETINGS[form].format(place=place)
        sentences = (
            (f'今朝、{a}は{b}と{meet}、{initial}。', f'{a}は{action}。', f'{result}ので、{a}は{follow}。'),
            (f'朝、{a}が{b}と{meet}、{initial}。', f'そこで{a}は{action}。', f'{result}ため、続いて{a}は{follow}。'),
            (f'今朝のことだが、{a}は{b}と{meet}、{initial}。', f'{a}は{action}ので、{result}。', f'そのあと{a}は{follow}。'),
            (f'今朝、{a}が{b}と{meet}、{initial}。', f'その場で{a}は{action}。', f'{result}のを見て、{a}は{follow}。'),
            (f'朝の用事で{a}は{b}と{meet}、{initial}。', f'{a}は{action}。', f'{result}ため、{a}は帰る前に{follow}。'),
            (f'今朝、{b}と{meet}、{a}が見ると{initial}。', f'{a}は{action}ので、{result}。', f'{a}は次に{follow}。'),
            (f'朝、{a}は{b}と{meet}、{initial}。', f'{a}はその場所で{action}。', f'{result}ので、最後に{a}は{follow}。'),
            (f'今朝、{a}は{b}と{meet}、{initial}。', f'そこで{a}は{action}ため、{result}。', f'それから{a}は{follow}。'),
        )[surface]
    elif cat == 'quantity':
        x, d, value = f['x'], f['delta'], expected['final']
        place = ('棚', '机', '作業台', '台')[form]
        action = f'そこに{d}{unit}を加えた' if branch == 0 else f'そこから{d}{unit}を取り出した'
        turns = (
            (f'{a}は{b}と{place}の{item}を数え、{x}{unit}あることを確かめた。', f'{a}が{action}ので、{place}の{item}は{value}{unit}になった。', f'二人はその数を紙に控えてから片づけを始めた。'),
            (f'{place}には{a}が集めた{item}が{x}{unit}あり、{b}も数を確かめた。', f'次に{a}は{action}。', f'{place}の{item}は{value}{unit}になり、二人は数え直した品をまとめて置いた。'),
            (f'{a}と{b}が{place}を片づけると、{item}が{x}{unit}見つかった。', f'{a}は{action}。', f'{place}にある{value}{unit}を確認して、{b}は片づけの続きを始めた。'),
            (f'{a}は{place}に{item}を{x}{unit}並べ、{b}に声をかけた。', f'そのあと{a}が{action}ところ、並んでいる数は{value}{unit}になった。', f'二人は並べ直した品を見ながら次の作業を相談した。'),
            (f'{b}と一緒に{a}が数えた{place}の{item}は{x}{unit}だった。', f'{a}は{action}。', f'いまある{value}{unit}を二人で確かめ、{b}が紙に数を書き留めた。'),
            (f'{a}と{b}の前の{place}には、{item}が{x}{unit}置かれていた。', f'{a}が{action}ので、そこには{value}{unit}残った。', f'{b}はその数を確認し、空いた場所を拭いた。'),
            (f'{a}は{place}の{item}を{x}{unit}と数え、{b}に伝えた。', f'続いて{a}が{action}結果、数は{value}{unit}になった。', f'{b}は新しい数を手帳に書いて手伝いに戻った。'),
            (f'{b}に手伝ってもらい、{a}は{place}の{item}が{x}{unit}あると確かめた。', f'次に{a}は{action}。', f'{place}の{value}{unit}を二人で数え直してから、作業の道具を出した。'),
        )
        sentences = turns[surface]
    elif cat == 'time':
        h, d, value, activity = f['hour'], f['duration'], expected['final_hour'], f['activity']
        shift = f'{d}時間早めた' if branch == 0 else f'{d}時間遅らせた'
        place = ('集会所', '家', '近くの広場', '待ち合わせ場所')[form]
        sentences = (
            (f'{a}と{b}は{place}で{h}時に{activity}を始める予定だった。', f'二人は相談して開始を{shift}。', f'新しい予定の{value}時になると、二人は{activity}を始めた。'),
            (f'{a}は{b}と{place}で行う{activity}を{h}時からと決めていた。', f'その後、二人は開始時刻を{shift}。', f'{value}時に{a}が声をかけ、二人は予定どおり{activity}を始めた。'),
            (f'{place}での{activity}に備え、{a}と{b}は{h}時に始める約束をした。', f'二人が予定を見直して開始を{shift}ため、開始時刻は{value}時になった。', f'その時刻に二人は{activity}を始め、落ち着いて取り組んだ。'),
            (f'{a}と{b}の予定表には、{place}で{h}時から{activity}と書いてあった。', f'二人は開始を{shift}。', f'{value}時になると{b}が準備を終え、二人で{activity}を始めた。'),
            (f'{h}時から{place}で{activity}をするため、{a}は{b}と予定を合わせた。', f'二人は相談の末、開始時刻を{shift}。', f'変更後の{value}時に、二人は{activity}を始めた。'),
            (f'{a}は{place}での{activity}を{h}時から始めようと、{b}に伝えた。', f'二人で話し合い、開始を{shift}。', f'{value}時に{a}が合図して、二人は{activity}を始めた。'),
            (f'{place}で{h}時に{activity}を始める約束を、{a}と{b}はしていた。', f'予定を調整することになり、開始を{shift}。', f'{value}時には二人の準備が整い、{activity}が始まった。'),
            (f'{a}と{b}は、{h}時から{place}で{activity}をするつもりだった。', f'相談して開始を{shift}ので、二人は予定表を直した。', f'書き直した{value}時に、二人は{activity}を始めた。'),
        )[surface]
    elif cat == 'comparison':
        la, lb, longer = expected['A_length'], expected['B_length'], expected['longer']
        place = ('工作室', '庭', '作業場', '玄関')[form]
        record = f'{a}の棒は{la}センチ、{b}の棒は{lb}センチだった'
        if f['sequence'] == '後':
            record = f'{b}の棒は{lb}センチ、{a}の棒は{la}センチだった'
        sentences = (
            (f'{place}で棒を並べると、{record}。', f'長い棒が必要だったので、二人は{longer}の棒を選んだ。', f'選んだ棒を持って、二人は作業を始めた。'),
            (f'{place}で二人が棒を測ったところ、{record}。', f'二人は長い方を使おうと相談し、{longer}の棒を手に取った。', f'その棒を作業台に運んで、道具を並べた。'),
            (f'{place}には二人の棒があり、測ると{record}。', f'長い方から使うことにした二人は、{longer}の棒を選んだ。', f'もう一本は脇に置き、選んだ棒で作業を進めた。'),
            (f'{place}で測り比べると、{record}。', f'二人は長い棒を探していたため、{longer}の棒を持ち上げた。', f'使う棒が決まり、二人は作業の場所へ運んだ。'),
            (f'{place}で準備をする二人が長さを確かめると、{record}。', f'二本のうち長い方を使うので、{longer}の棒を選んだ。', f'二人は選んだ棒を置き、必要な道具を出した。'),
            (f'{place}で二本を並べて測ったところ、{record}。', f'長い棒を先に使うと決め、二人は{longer}の棒を取り出した。', f'選んだ棒を机に置いて、最初の作業に取りかかった。'),
            (f'{place}で二人が持ってきた棒を測ると、{record}。', f'長い棒が必要な作業のため、二人は{longer}の棒を使うことにした。', f'もう一本を片づけて、選んだ棒を作業台に載せた。'),
            (f'{place}で二人は準備を進め、棒を測ると{record}。', f'二本から長い方を選ぶことになり、{longer}の棒に決めた。', f'二人はその棒を手元に置き、作業の手順を相談した。'),
        )[surface]
    elif cat == 'entity_reference':
        target = expected['target']; other = b if target == a else a
        relation = expected['relation']
        introductions = {
            'receiver': f'{other}は{item}を{target}に渡した',
            'sender': f'{target}は{item}を{other}へ届けた',
            'original_owner': f'{target}が持っていた{item}を{other}に貸した',
            'alias': f'{other}は「つき」、{target}は「ほし」という別名で呼ばれていた',
        }
        actions = {
            'receiver': f'受け取った{target}は{item}を机に置いた',
            'sender': f'届け終えた{target}は相手に手を振った',
            'original_owner': f'借りた{other}は、持ち主の{target}にあとで返すと約束した',
            'alias': f'「ほし」と声をかけられると、{target}が振り向いた',
        }
        follow = {
            'receiver': f'{target}は置いた{item}を大切にしまった',
            'sender': f'{target}は用事を終えて帰り道を歩き始めた',
            'original_owner': f'{target}はうなずき、{other}は借りた{item}を手元に置いた',
            'alias': f'{target}は声をかけた人のところへ歩いていった',
        }
        intro, action, ending = introductions[relation], actions[relation], follow[relation]
        # Alias kernel contains no item, so add a coherent TRAIN-item scene.
        scene = f'{item}を並べる二人の間で、' if relation == 'alias' else ''
        sentences = (
            (f'{scene}{intro}。', f'そのあと、{action}。', f'{ending}。'),
            (f'ある日、{scene}{intro}。', f'続いて、{action}。', f'それから{ending}。'),
            (f'昼のことだったが、{scene}{intro}。', f'すると、{action}。', f'そのあと{ending}。'),
            (f'{scene}{intro}。', f'まもなく、{action}。', f'やがて{ending}。'),
            (f'静かな午後、{scene}{intro}。', f'その場で、{action}。', f'続いて{ending}。'),
            (f'{scene}{intro}。', f'次に、{action}。', f'最後に{ending}。'),
            (f'夕方の出来事だったが、{scene}{intro}。', f'それをきっかけに、{action}。', f'それから{ending}。'),
            (f'{scene}{intro}。', f'ほどなく、{action}。', f'その後、{ending}。'),
        )[surface]
    else:
        on = expected['on']
        rules = (
            'スイッチがオンなら点灯し、オフなら消える',
            'ボタンを押している間は点灯し、押していない間は消える',
            'つまみが左にあると点灯し、右にあると消える',
            'レバーが上にあると点灯し、下にあると消える',
        )
        action = (
            f'スイッチを{"オン" if on else "オフ"}にした',
            'ボタンを押したままにした' if on else 'ボタンには触れずにいた',
            f'つまみを{"左" if on else "右"}に合わせた',
            f'レバーを{"上" if on else "下"}に動かした',
        )[form]
        state = '点灯している' if on else '消えている'
        observation = '光っている' if on else '光っていない'
        rule = rules[form]
        sentences = (
            (f'{a}が{item}をしまう箱のライトは、{rule}仕組みだった。', f'{a}が{action}ので、ライトは{state}。', f'{a}は{observation}ライトを見て、箱を棚に戻した。'),
            (f'{a}の{item}用の箱には、{rule}ライトが付いていた。', f'{a}は{action}。', f'ライトが{observation}のを確かめてから、{a}は箱を机に置いた。'),
            (f'{a}が使う{item}の箱にはライトがあり、{rule}設定だった。', f'{a}が{action}ところ、ライトは{state}。', f'{a}はその状態を確認して、箱のふたを閉めた。'),
            (f'{a}は{item}の箱を取り出し、ライトが{rule}と知った。', f'そこで{a}は{action}。', f'ライトが{observation}のを見て、箱を片づけた。'),
            (f'{a}の{item}を入れた箱には、{rule}ライトがあった。', f'{a}が{action}ため、ライトは{state}。', f'{a}はライトの状態を見届け、箱を元の場所に戻した。'),
            (f'{a}が{item}を入れる箱のライトは、{rule}ように作られていた。', f'{a}は{action}。', f'{observation}ライトを確かめ、箱を手元に置いた。'),
            (f'{a}の{item}の箱には、{rule}仕組みのライトが付いていた。', f'{a}が{action}ので、ライトは{state}。', f'{a}はライトを確かめたあと、箱を棚に運んだ。'),
            (f'{a}が持ってきた{item}の箱のライトは、{rule}設定になっていた。', f'{a}は{action}。', f'ライトは{state}ため、{a}はその状態を見届けて箱を置いた。'),
        )[surface]
    text = ''.join(sentences)
    if len(sentences) != 3 or text.count('。') != 3 or any(not s.endswith('。') for s in sentences):
        raise ValueError('Three complete plain narrative sentences required')
    return dict(text=text, text_sha256=digest(text), cut=len(sentences[0]), end=len(text),
                local_state=copy.deepcopy(expected), fictional_scene_details_locally_authored=True)


def generate(control):
    families = control['families']
    if (len(families) != 1024 or len(control['rows']) != 2048 or len({f['id'] for f in families}) != 1024
            or {f['split'] for f in families} != {'train'}):
        raise ValueError('Unchanged accepted 1024 TRAIN fact families required')
    rows = []; originals = {r['id']: r for r in control['rows']}
    for family in families:
        for branch in (0, 1):
            for surface in range(8):
                result = render(family, branch, surface)
                rows.append(dict(id=f'{family["id"]}-{branch}-n{surface}', split='train', family=family['id'],
                    category=family['category'], template_id=f'narrative-{family["category"]}-{surface}',
                    original_template_id=family['template_id'], original_form=family['form'], surface=surface,
                    label=branch, facts=copy.deepcopy(family['facts']), source=SOURCE,
                    original_row_sha256=originals[f'{family["id"]}-{branch}']['text_sha256'], **result))
    if len(rows) != 16384 or len({r['text_sha256'] for r in rows}) != 16384:
        raise ValueError('All 16384 whole texts must be unique without filtering/reroll')
    return rows


def select_pilot(rows):
    rng = random.Random(SEED)
    by_cell = {(cat, s): [] for cat in CATEGORIES for s in range(8)}
    for row in rows:
        by_cell[(row['category'], row['surface'])].append(row)
    selected = [rng.choice(by_cell[cell]) for cell in by_cell]
    used = {r['id'] for r in selected}
    selected.extend(rng.sample([r for r in rows if r['id'] not in used], 16))
    if len({r['id'] for r in selected}) != 64 or {r['label'] for r in selected} != {0, 1}:
        raise ValueError('Fixed64 must cover all48 cells and both branches overall')
    return dict(rows=selected, seed=SEED, category_surface_cells=48,
        sampling='Fixed seed stratified48 category/surface draws then16 unique TRAIN draws; no reroll/filter',
        both_branches_represented=True, new_independent_semantic_families=0, protected_test_used=False)


def encode_rows(rows, tokenizer):
    tokens, focus, offsets, lengths, metadata = [], [], [], [], []
    # Cache piece byte sizes once: no per-token Python decoder calls in the loop.
    byte_sizes = np.asarray([0 if i < 8 else len(tokenizer.decode_bytes([i])) for i in range(4096)])
    for row in rows:
        body = tokenizer.encode(row['text'])
        raw = row['text'].encode('utf-8')
        if (tokenizer.decode_bytes(body) != raw or not body or len(body) + 1 > 1024
                or any(i < 8 for i in body)):
            raise ValueError('Whole exact native body required; never truncate/insert role IDs')
        ends = np.cumsum(byte_sizes[body]); starts = ends - byte_sizes[body]
        cut = len(row['text'][:row['cut']].encode('utf-8'))
        mask = ((starts < len(raw)) & (ends > cut)).astype(np.uint8)
        offsets.append(len(tokens)); lengths.append(len(body) + 2)
        tokens.extend([2, *body, 3]); focus.extend([0, *mask, 0])
        metadata.append({**{k: row[k] for k in ('id', 'family', 'category', 'template_id', 'original_template_id', 'surface', 'label', 'text_sha256')},
                         'body_tokens': len(body), 'body_bytes': len(raw)})
    return dict(tokens=np.asarray(tokens, dtype='<u2'), focus=np.asarray(focus, dtype=np.uint8),
                offsets=np.asarray(offsets, dtype='<i8'), lengths=np.asarray(lengths, dtype='<i4')), metadata


class NarrativeTrainView:
    """Original PositiveStream protocol, without modifying frozen old loaders."""
    def __init__(self, path, manifest_sha256, require_accepted=True):
        self.directory = Path(path)
        if sha256(self.directory / 'manifest.json') != manifest_sha256:
            raise ValueError('Narrative manifest differs')
        m = self.manifest = read_json(self.directory / 'manifest.json')
        if (m['kind'] != KIND or m['source'] != SOURCE or m['documents'] != 16384 or m['train_families'] != 1024
                or m['newly_prepared_original_corpus_tokens'] != 0 or m['tokenizer_sha256'] != TOKENIZER_SHA
                or sha256(self.directory / 'train.npz') != m['arrays_sha256']
                or sha256(self.directory / 'train-source.json') != m['train_source_sha256']
                or sha256(self.directory / 'content-pilot.json') != m['pilot_sha256']):
            raise ValueError('Narrative TRAIN provenance/arrays differs')
        if require_accepted:
            review = read_json(self.directory / 'content-review.json')
            if (not review['all64_read'] or not review['training_pool_accepted'] or review['weak_documents'] > 10
                    or review['unresolved_grammar_documents'] or review['unresolved_grounding_documents']
                    or review['manifest_sha256'] != manifest_sha256 or review['pilot_sha256'] != m['pilot_sha256']
                    or review['notes_sha256'] != sha256(self.directory / 'content-notes.json')):
                raise ValueError('Accepted raw-bound fixed64 narrative review required')
        with np.load(self.directory / 'train.npz', allow_pickle=False) as arrays:
            self.tokens = arrays['tokens'].copy(); self.focus = arrays['focus'].astype(bool)
            self.offsets = arrays['offsets'].copy(); self.lengths = arrays['lengths'].copy()
        if (len(self.lengths) != 16384 or self.offsets.shape != self.lengths.shape
                or len(self.tokens) != m['serialized_tokens'] or self.focus.shape != self.tokens.shape
                or np.any(self.lengths < 3) or np.any(self.lengths - 1 > 1024)
                or not np.array_equal(self.offsets, np.r_[0, np.cumsum(self.lengths)[:-1]])
                or int(self.lengths.sum()) != len(self.tokens) or int(self.focus.sum()) != m['outcome_focus_body_targets']
                or np.any(self.focus & (self.tokens < 8)) or np.any(self.tokens >= 4096)
                or np.any(np.isin(self.tokens, [0, 1, 4, 5, 6, 7]))
                or np.count_nonzero(self.tokens == 2) != 16384 or np.count_nonzero(self.tokens == 3) != 16384
                or not np.all(self.tokens[self.offsets] == 2) or not np.all(self.tokens[self.offsets + self.lengths - 1] == 3)):
            raise ValueError('Narrative whole BOS/body/EOS codec differs')
        self.manifest_sha256 = manifest_sha256
