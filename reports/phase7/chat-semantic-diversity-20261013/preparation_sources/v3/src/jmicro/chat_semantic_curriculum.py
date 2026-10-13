"""TRAIN-only authored semantic operations, separate from all evaluation text.

Operation graphs, authored settings and surface variants are recorded separately.
Slot/surface variants of a setting are never counted as independent families.
The two prior curricula and native model are not modified.
"""
import random

WEIGHTS = dict(daily=.30, direct=.20, correction=.15, negation=.15,
               context=.10, clarification=.05, speaker=.05)
PEOPLE = ('朋子', '航平', '俊介', '絵里', '遼', '穂乃香', '圭', '久美',
          '悠里', '健太', '奈央', '聖', '史織', '亮太', '紀子', '達也')
VENUES = ('集会所', '正面広場', '展示室', '交流室', '温室', '屋内ホール',
          '作業台', '相談窓口', '休憩所', '中央入口', '小会場', '大広間')
THINGS = ('冊子', 'カード', '伝票', '資料', '袋', 'ポスター', '名札', '箱')
COUNTERS = dict(冊子='冊', カード='枚', 伝票='枚', 資料='枚', 袋='枚',
                ポスター='枚', 名札='個', 箱='個')
ACTIVITIES = ('写真の整理', '植物の世話', '合唱の練習', '工作', '模型作り',
              '手紙の作成', '部屋の模様替え', 'ぬり絵')
COLORS = ('紺色', '水色', '橙色', '銀色', '茶色', '紫色', '黄緑色', '白色')
DAYS = ('平日', '週末', '祝日', '来週', '今週', '月末', '翌月', '明日')

# Settings alter the information roles; shared operations are still identified
# explicitly so that themes are not advertised as independent reasoning skills.
SETTINGS = (
    ('展示会', '飾り付け', '展示室'), ('地域の集まり', '受付', '集会所'),
    ('荷物の整理', '仕分け', '相談窓口'), ('道具の管理', '点検', '作業台'),
    ('合唱の発表', '進行', '屋内ホール'), ('植物の展示', '水やり', '温室'),
    ('読書会', '司会', '交流室'), ('撮影会', '撮影', '小会場'),
)

DAILY = (
    ('{activity}がようやく終わりました。ひと言もらえますか。',
     '{activity}、お疲れさまでした。終わってほっとしますね。', 'completion'),
    ('{activity}を始める前で少し緊張しています。',
     '始める前は緊張しますね。まず小さな一歩からで大丈夫です。', 'before_event'),
    ('{activity}が思いどおりに進まず、がっかりしています。',
     '思いどおりに進まないと残念ですね。少し休んでから考えてもよさそうです。', 'disappointment'),
    ('初めて{activity}がうまくできて、うれしいです。',
     '初めてうまくできたのですね。うれしい気持ちが伝わってきます。', 'success'),
    ('今日は{activity}で忙しかったので、今は休みたいです。',
     '忙しい一日だったのですね。今はゆっくり休めるといいですね。', 'rest'),
    ('{activity}に挑戦した友人へ、短い応援の言葉を考えてください。',
     '「少しずつで大丈夫。応援しているよ」はどうでしょう。', 'support_message'),
    ('{activity}を手伝ってもらいました。短くお礼を伝えたいです。',
     '「手伝ってくれてありがとう。とても助かりました」と伝えられます。', 'thanks_message'),
    ('{activity}を忘れてしまいました。言い訳せず謝る文を作ってください。',
     '「忘れてしまってごめんなさい。次から気をつけます」と伝えられます。', 'apology_message'),
    ('一緒に{activity}をしようと誘われましたが、今日は休みたいです。丁寧に断りたいです。',
     '「誘ってくれてありがとう。今日は休みたいので、また今度お願いします」はどうでしょう。', 'decline_message'),
    ('{activity}を続けている人に、何を聞くと話が広がりますか。',
     '「どんなところが楽しいですか」と聞くと、相手の話を聞けそうです。', 'followup_question'),
    ('{activity}と休憩、今はどちらを選ぶか迷っています。疲れています。',
     '疲れているなら、まず少し休憩してから決めてもよさそうです。', 'preference_from_state'),
    ('{activity}を終えたところです。今の気持ちを聞いてください。',
     '終えてみて、今はどんな気持ちですか。', 'ask_feeling'),
    ('{activity}のやり方が分からないので、詳しい人に聞きたいです。',
     '分からないところを一つ挙げて、詳しい人に聞いてみるとよさそうです。', 'specific_next_step'),
    ('{activity}を少しだけ進めました。全部は終わっていません。',
     '少し進められたのですね。全部終わっていなくても、その一歩は大切ですね。', 'partial_progress'),
    ('私は{activity}が好きです。あなたは実際にやったことがありますか。',
     '私は実際に体験したことはありませんが、どんなところが好きなのか聞きたいです。', 'assistant_role'),
    ('{activity}のための短い合言葉を、自由に一つ考えてください。',
     '「少しずつ、楽しく進もう」はどうでしょう。', 'creative_phrase'),
    ('{activity}を手伝う約束をしました。相手へ確認する文を作ってください。',
     '「いつ、どんなことを手伝えばよいですか」と確認できます。', 'request_details'),
    ('{activity}で友人と意見が分かれました。まず相手の考えを聞きたいです。',
     '「そう考えた理由を教えてもらえますか」と聞いてみるのはどうでしょう。', 'listen_first'),
    ('{activity}を一緒に終えました。相手をねぎらう短い言葉がほしいです。',
     '「一緒に進めてくれてありがとう。お疲れさまでした」と伝えられます。', 'shared_completion'),
    ('{activity}の話をしたいです。まだ詳しいことは話していません。',
     'ぜひ聞かせてください。どんなことがあったのですか。', 'open_invitation'),
    ('こんにちは。今日は{activity}の相談をしたくて来ました。',
     'こんにちは。どんなことを相談したいですか。', 'purpose_greeting'),
    ('おはようございます。今日は{activity}をする予定です。',
     'おはようございます。予定が気持ちよく進むといいですね。', 'morning'),
    ('こんばんは。{activity}の話を少ししてもいいですか。',
     'こんばんは。もちろんです。どんな話でしょうか。', 'evening'),
    ('{activity}の相談を聞いてくれてありがとう。今日はここまでにします。',
     'こちらこそ、話してくれてありがとうございました。また話してくださいね。', 'closing'),
    ('{activity}は明日になりました。今日は急がず過ごせそうです。',
     '明日になったのですね。今日は落ち着いて過ごせそうですね。', 'reschedule_relief'),
    ('{activity}を始めたいけれど、完璧にできるか心配です。',
     '最初から完璧でなくても大丈夫です。できるところから始めてみませんか。', 'perfection_worry'),
    ('{activity}で小さな失敗をして、恥ずかしく感じています。',
     '失敗すると恥ずかしく感じますね。落ち着いたら、次にできることを考えましょう。', 'embarrassment'),
    ('{activity}を一人で進めるか、誰かと進めるか迷っています。',
     '一人で進めやすい部分と、手伝ってほしい部分を分けて考えてみませんか。', 'options_without_invented_fact'),
    ('{activity}について「難しかったけれど楽しかった」を短く言い換えてください。',
     '「大変でしたが、楽しめました」と言い換えられます。', 'paraphrase'),
    ('{activity}に使う文章を、丁寧な言い方にしたいです。何を送ればいいですか。',
     '言い換えたい文章を送ってください。丁寧な表現を一緒に考えます。', 'ask_input'),
    ('{activity}の予定はまだ決めていません。決まったと言わないでください。',
     'まだ予定は決まっていないのですね。これから考える段階だと受け取りました。', 'uncertainty'),
    ('{activity}について短く話したいです。長い説明は要りません。',
     '分かりました。どんなことを話したいですか。', 'brief_conversation'),
)


def variables(seed):
    rng = random.Random(seed)
    a, b, c = rng.sample(PEOPLE, 3)
    x, y, z = rng.sample(THINGS, 3)
    p, q = rng.sample(VENUES, 2)
    red, blue = rng.sample(COLORS, 2)
    n, m = rng.sample(range(2, 18), 2)
    return dict(a=a, b=b, c=c, x=x, y=y, z=z, p=p, q=q, red=red, blue=blue,
                n=n, m=m, hour=rng.choice((8, 10, 14, 16, 18)),
                activity=rng.choice(ACTIVITIES), day=rng.choice(DAYS))


def fact_case(category, op, s, setting):
    topic, task, place = setting
    a, b, c = (s[k] for k in ('a', 'b', 'c'))
    x, y, z = (s[k] for k in ('x', 'y', 'z'))
    p, q, n, m = (s[k] for k in ('p', 'q', 'n', 'm'))
    color, other = s['red'], s['blue']
    cx, cy, cz = COUNTERS[x], COUNTERS[y], COUNTERS[z]
    if category == 'direct':
        cases = (
            (f'{topic}では、{a}さんが{task}、{b}さんが案内を担当します。案内の担当は誰ですか。', b + 'さん', 'role_lookup'),
            (f'{topic}では、先に{task}をして、その後で{place}を片付けます。最後にすることは何ですか。', f'{place}の片付け', 'procedure_last'),
            (f'{topic}で、{x}は{n}{cx}、{y}は{m}{cy}あります。数が多いのはどちらですか。', x if n > m else y, 'numeric_compare'),
            (f'{topic}用の{color}の{z}は{p}、{other}の{z}は{q}にあります。{other}の{z}の場所を教えてください。', q, 'attribute_join'),
            (f'{topic}は{s["hour"]}時からです。準備はその一時間前に始めます。準備は何時からですか。', f'{s["hour"] - 1}時', 'relative_time'),
            (f'{topic}で使う{z}は全部で{n}{cz}です。そのうち一{cz}を予備にします。実際に使う{z}の数はいくつですか。', f'{n - 1}{cz}', 'reserve_subtract'),
            (f'{topic}の集まりには{p}と{q}の二候補があります。{p}は閉まっていて、{q}は利用できます。利用できる場所を一つ教えてください。', q, 'availability_select'),
            (f'{topic}の{task}が終わったら、{a}さんへ連絡します。今、{task}が終わりました。次に誰へ連絡しますか。', a + 'さん', 'conditional_next'),
        )
    elif category == 'correction':
        cases = (
            (f'{topic}の{task}は{a}さんに頼む予定でした。変更して{b}さんに頼みます。今頼む相手は誰ですか。', b + 'さん', 'replace_person'),
            (f'{topic}の場所は{p}でしたが、{q}に変更しました。開始は{s["hour"]}時のままです。今の場所だけ答えてください。', q, 'change_one_keep_other'),
            (f'{topic}の{z}を{n}{cz}と伝えましたが、正しくは{m}{cz}です。訂正後の数を答えてください。', f'{m}{cz}', 'correct_count'),
            (f'{topic}の場所を{p}から{q}へ変えました。その変更を取り消し、元に戻します。最終的な場所はどこですか。', p, 'retract_change'),
            (f'{topic}で使うものは{color}の{z}でした。色だけ{other}に変えます。物の種類は変えません。今使うものを答えてください。', f'{other}の{z}', 'partial_update'),
            (f'{topic}の担当を{a}さんから{b}さん、さらに{c}さんへ変えました。最後に決まった担当は誰ですか。', c + 'さん', 'three_updates'),
            (f'{topic}の時刻は{s["hour"]}時でした。二時間後ろに変更します。今の時刻を答えてください。', f'{s["hour"] + 2}時', 'relative_update'),
            (f'{topic}は{p}に移す案がありましたが、採用されませんでした。もともとの{q}で行います。決まった場所はどこですか。', q, 'proposal_not_decision'),
        )
    elif category == 'negation':
        cases = (
            (f'{topic}では{color}の{z}は使いません。{other}の{z}を使います。使うものはどちらですか。', f'{other}の{z}', 'excluded_attribute'),
            (f'{topic}の{task}は私ではなく{a}さんの担当です。担当者を答えてください。', a + 'さん', 'not_user'),
            (f'{topic}の候補は{p}と{q}です。{q}以外の候補を選んでください。', p, 'except_one'),
            (f'{topic}では{a}さんと{b}さんは案内担当ではありません。{c}さんが案内担当です。案内をするのは誰ですか。', c + 'さん', 'two_exclusions'),
            (f'{topic}用の{z}は{n}{cz}ではありません。必要なのは{m}{cz}です。必要な数だけ答えてください。', f'{m}{cz}', 'denied_quantity'),
            (f'{topic}では{p}を使ってはいけません。{q}なら使えます。許可された場所はどこですか。', q, 'permission'),
            (f'{topic}用に{color}の{z}を探しています。{color}の{z}がない場合だけ{other}にします。{color}は見つかりました。今選ぶ色は何ですか。', color, 'fallback_not_needed'),
            (f'{topic}で、{a}さんは{task}をしないわけではありません。{task}を引き受けています。担当者は誰ですか。', a + 'さん', 'explicit_double_negation'),
        )
    elif category == 'speaker':
        cases = (
            (f'私は{p}へ行きます。{a}さんは「私は{q}へ行く」と言いました。{a}さんが行く場所はどこですか。', q, 'quoted_i'),
            (f'{a}さんの{z}は{color}、私の{z}は{other}です。私の{z}の色を答えてください。', other, 'user_possession'),
            (f'{a}さんが{b}さんへ{z}を渡しました。渡した人は誰ですか。', a + 'さん', 'giver'),
            (f'{a}さんが{b}さんへ{z}を渡しました。受け取った人は誰ですか。', b + 'さん', 'recipient'),
            (f'{a}さんは{task}、{b}さんは案内担当です。{a}さんが「案内は{b}さんです」と説明しました。案内担当は誰ですか。', b + 'さん', 'reporter_not_actor'),
            (f'私の名前は{a}です。{b}さんは私の友人です。私の名前を答えてください。', a, 'user_name'),
            (f'{a}さんは{color}の{z}を希望し、{b}さんは{other}の{z}を希望しました。{b}さんの希望は何ですか。', f'{other}の{z}', 'speaker_preference'),
            (f'{a}さんが{topic}の担当です。私はその話を聞いただけです。担当者は誰ですか。', a + 'さん', 'observer_not_actor'),
        )
    else:
        raise ValueError(category)
    prompt, answer, operation = cases[op]
    expanded = {
        'direct': (f'{b}さんが{topic}の案内を担当します。', f'最後に{place}を片付けます。',
                   f'数が多いのは{answer}です。', f'{other}の{z}は{q}にあります。',
                   f'{topic}の準備は{answer}から始めます。', f'予備を除いて使う{z}は{answer}です。',
                   f'{q}は利用できるので、{topic}には{q}を選べます。', f'{task}が終わったので、{a}さんへ連絡します。'),
        'correction': (f'変更後は{b}さんに{task}を頼みます。', f'変更後の場所は{q}です。',
                       f'訂正後に必要な{z}は{answer}です。', f'変更を取り消したので、場所は元の{p}です。',
                       f'色だけを変えたので、使うのは{other}の{z}です。', f'最後の変更で、{c}さんが担当になりました。',
                       f'二時間後ろに変更したので、今の時刻は{answer}です。', f'{p}への案は採用されず、{q}で行います。'),
        'negation': (f'使うのは{other}の{z}です。{color}の方は使いません。', f'{task}を担当するのは{a}さんです。',
                     f'{q}を除くので、選ぶ候補は{p}です。', f'案内は{c}さんが担当します。',
                     f'必要な{z}の数は{answer}です。', f'許可されている{q}を使えます。',
                     f'{color}が見つかったので、代わりの色には変えません。{color}を選びます。',
                     f'{a}さんは{task}を引き受けているので、担当は{a}さんです。'),
        'speaker': (f'{a}さんは{q}へ行くと言っています。', f'あなたの{z}の色は{other}です。',
                    f'{z}を渡したのは{a}さんです。', f'{z}を受け取ったのは{b}さんです。',
                    f'説明した人ではなく、案内を担当するのは{b}さんです。', f'あなたの名前は{a}さんです。',
                    f'{b}さんが希望しているのは{other}の{z}です。', f'{topic}を担当するのは{a}さんです。'),
    }[category][op]
    variants = (answer + 'です。', expanded, expanded)
    return prompt, variants[s['n'] % 3], operation, dict(requested_value=answer, operation=operation,
                                                       setting=setting, state=s)


def clarification_case(op, s, setting):
    topic, task, place = setting
    counter = COUNTERS[s['z']]
    cases = (
        (f'{s["a"]}さんが{topic}のために{s["p"]}で使う{s["z"]}を買いたいそうです。必要な数はまだ伝えられていません。まず何を確認しますか。', f'{s["z"]}はいくつ必要ですか。', 'missing_quantity'),
        (f'{topic}では{s["a"]}さんと{s["b"]}さんが{s["hour"]}時に集合します。場所はまだ決まっていません。確定した場所を答えられますか。', 'まだ決まっていないので、確定した場所は答えられません。', 'unknown_not_invented'),
        (f'{topic}の{task}は{s["p"]}で{s["hour"]}時に始めます。担当へ連絡したいのですが、誰が担当かはまだ伝えられていません。何を聞きますか。', '担当者は誰ですか。', 'missing_person'),
        (f'{topic}は{s["p"]}で{s["hour"]}時からの予定です。日付をまだ伝えていません。まず確認することは何ですか。', '何日の予定ですか。', 'missing_date'),
        (f'{topic}の準備で、{s["p"]}にある{s["z"]}を「そちらへ移してください」と頼まれました。移動先が分かりません。どう確認しますか。', 'どこへ移せばよいですか。', 'ambiguous_destination'),
        (f'{topic}に来る{s["a"]}さん宛ての文章を短くしてほしいです。文章はまだ送っていません。どう返しますか。', '短くしたい文章を送ってください。', 'missing_text'),
        (f'{topic}の{task}を{s["p"]}で{s["a"]}さんと手伝いたいです。具体的な担当範囲は分かりません。何を確認しますか。', 'どの部分を手伝えばよいですか。', 'missing_action'),
        (f'{topic}の{ s["z"]}を{ s["p"]}へ{ s["n"]}{counter}運びます。数は書いてあります。運ぶ数を答えてください。', f'{s["n"]}{counter}です。', 'information_sufficient'),
    )
    prompt, answer, operation = cases[op]
    return prompt, answer, operation, dict(operation=operation, state=s, setting=setting)


def context_case(op, s, setting):
    topic, task, place = setting
    a, b, p, q, x, y, n, m = (s[k] for k in ('a', 'b', 'p', 'q', 'x', 'y', 'n', 'm'))
    cx, cy = COUNTERS[x], COUNTERS[y]
    cases = (
        ([f'{topic}は{p}で行います。', f'場所を{q}に変えました。今の場所はどこですか。'],
         [f'{p}で行うのですね。', q + 'です。'], 'context_place_update'),
        ([f'{topic}では{a}さんが{task}、{b}さんが案内です。', f'{task}を{b}さんへ変更します。今の{task}担当は誰ですか。'],
         [f'{task}は{a}さん、案内は{b}さんですね。', b + 'さんです。'], 'context_role_update'),
        ([f'{topic}で{x}を{n}{cx}、{y}を{m}{cy}用意します。', f'{x}だけ一{cx}増やします。{y}の数はいくつのままですか。'],
         [f'{x}が{n}{cx}、{y}が{m}{cy}ですね。', f'{m}{cy}のままです。'], 'context_keep_other'),
        ([f'{topic}は{p}の予定です。', f'{q}に変えます。', 'その変更を取り消します。結局どこで行いますか。'],
         [p + 'ですね。', q + 'へ変更ですね。', p + 'です。'], 'context_retraction'),
        ([f'{topic}で{a}さんへ{ x}を渡します。', f'品物だけ{y}へ変えます。誰に何を渡しますか。'],
         [f'{a}さんへ{x}を渡すのですね。', f'{a}さんに{y}を渡します。'], 'context_pair_update'),
        ([f'{topic}の連絡先は{a}さんです。', f'連絡先を{b}さんに変えます。', f'時間だけ{s["hour"]}時にします。連絡する相手は誰ですか。'],
         [a + 'さんですね。', b + 'さんへ変更ですね。', b + 'さんです。'], 'context_latest_subject'),
        ([f'{topic}の用意は{n}個です。', f'{m}個へ訂正します。', '訂正後の数をもう一度教えてください。'],
         [f'{n}個ですね。', f'{m}個へ訂正ですね。', f'{m}個です。'], 'context_recall_corrected'),
        ([f'{topic}は{p}、時刻は{s["hour"]}時です。', '時刻は変えません。場所だけ確認したいです。'],
         [f'{p}で{s["hour"]}時ですね。', p + 'です。'], 'context_select_requested'),
    )
    users, assistants, operation = cases[op]
    return users, assistants, operation, dict(operation=operation, state=s, setting=setting)


def render(category, family_index, variant):
    assert category in WEIGHTS and 0 <= family_index < 32
    seed = f'semantic-train-{category}-{family_index}-{variant}'
    s = variables(seed)
    setting = SETTINGS[family_index // 4]
    op = (family_index % 4) + (4 if variant % 2 else 0)
    # Both operations for a setting are kept in the SAME family, not inflated
    # as independent variant-derived information.
    if category == 'daily':
        user, body, operation = DAILY[family_index]
        user, body = user.format(**s), body.format(**s)
        messages = [dict(role='user', text=user), dict(role='assistant', text=body)]
        evidence = dict(operation=operation, activity=s['activity'])
    elif category == 'clarification':
        user, body, operation, evidence = clarification_case(op, s, setting)
        messages = [dict(role='user', text=user), dict(role='assistant', text=body)]
    elif category == 'context':
        users, bodies, operation, evidence = context_case(op, s, setting)
        messages = [dict(role=role, text=text) for pair in zip(users, bodies, strict=True)
                    for role, text in zip(('user', 'assistant'), pair, strict=True)]
    else:
        user, body, operation, evidence = fact_case(category, op, s, setting)
        # A surface variant asks for the same value and remains in its family.
        if variant % 4 == 1:
            user = '次の話について確認したいです。' + user
        elif variant % 4 == 2:
            user = user.replace('答えてください。', '教えてもらえますか。')
        elif variant % 4 == 3:
            user += '説明は短くお願いします。'
        messages = [dict(role='user', text=user), dict(role='assistant', text=body)]
    family = f'semantic-{category}-setting-{family_index:02d}'
    return dict(doc_id=f'{family}-v{variant:05d}', split='train', category=category,
                family=family, semantic_operation=operation, source='project-authored-semantic-train',
                messages=messages, target_message_indices=[len(messages) - 1],
                target_kind='correct_history_final' if category == 'context' else 'natural_first_turn',
                answer_evidence=evidence, generation=dict(family_index=family_index, variant=variant))


def semantic_check(record):
    g = record['generation']
    expected = render(record['category'], g['family_index'], g['variant'])
    return all(record[key] == expected[key] for key in ('messages', 'family', 'semantic_operation',
                                                       'target_message_indices', 'answer_evidence'))
