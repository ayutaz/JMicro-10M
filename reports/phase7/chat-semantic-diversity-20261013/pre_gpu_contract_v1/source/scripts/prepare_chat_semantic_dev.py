"""Independently authored unseen DEV, only after TRAIN is frozen.

No TRAIN renderer is imported. No protectedTEST case is parsed or reused.
Gold bodies define fixed NLL targets; free generation uses the original rubric,
not inclusion of gold words as an automatic meaning grade.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_improvement_train import dump_jsonl

RUN = ROOT / 'reports/phase7/chat-semantic-diversity-20261013'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-semantic-diversity-20261013')
CATEGORIES = ('greeting', 'daily', 'emotion', 'question_back', 'ambiguity',
              'role_boundary', 'symbols', 'correction', 'followup', 'context')

SINGLE = {
    'greeting': (
        ('初めまして。今日は少しだけ雑談に付き合ってほしいです。', '初めまして。どんなお話をしましょうか。'),
        ('おはよう。出かける支度ができたところです。', 'おはようございます。気をつけて行ってらっしゃい。'),
        ('こんばんは。ひと息ついたので、話しに来ました。', 'こんばんは。どんな一日でしたか。'),
        ('さっきの説明、よく分かりました。ありがとう。', 'どういたしまして。分かってもらえてよかったです。'),
        ('そろそろ画面を閉じます。今日の話はここまでにしましょう。', '分かりました。お話ししてくれてありがとうございました。'),
        ('こんにちは。名前を言わなくても相談できますか。', 'こんにちは。名前を言わなくても相談できます。'),
        ('しばらく話していませんでしたが、また来ました。', 'また来てくれてありがとうございます。今日はどんなお話ですか。'),
        ('もう寝る準備をしています。おやすみの挨拶をお願いします。', 'おやすみなさい。ゆっくり休んでくださいね。'),
    ),
    'daily': (
        ('洗い物を済ませたら一息つきたいです。何から始めればよさそうですか。', 'まず洗い物を済ませて、それから一息つくのがよさそうです。'),
        ('朝の用事が片付きました。午後は予定がないので、気楽に過ごしたいです。', '午後はゆっくり過ごせそうですね。どんな過ごし方がよいですか。'),
        ('買い物のメモをなくしたので、覚えている品だけ先に書こうと思います。', '覚えている品から書き出すとよさそうですね。何を覚えていますか。'),
        ('雨の日は外へ出ず、家で読みかけの漫画を楽しみたいです。', '家でゆっくり漫画を読む時間もよさそうですね。'),
        ('鞄を軽くしたいので、今日使わない道具は置いていくつもりです。', '今日使うものを確認して、使わない道具を置いていくとよさそうです。'),
        ('一度に全部片付けるより、机の上だけから始めたいです。', 'まず机の上だけ片付けると、取りかかりやすそうですね。'),
        ('夕方の用事まで少し時間があります。何か短い気分転換を一つ提案してください。', '好きな音楽を一曲聴いてみるのはどうでしょう。'),
        ('友人を待っている間に、今日やることを二つに絞ろうと思っています。', '今日必要なことを二つ選ぶとよさそうですね。何を優先したいですか。'),
    ),
    'emotion': (
        ('抽選には外れました。期待していたので、ちょっと悔しいです。', '期待していた分、悔しい気持ちになりますね。'),
        ('前より早く支度ができて、自分でもうれしいです。', '前より早くできたのですね。うれしいですね。'),
        ('人前で話す順番が近づいて、そわそわしています。', '順番が近づくと落ち着かないですね。ゆっくり呼吸してみませんか。'),
        ('久しぶりの友人から連絡が来て、気持ちが明るくなりました。', '久しぶりの連絡はうれしいですね。どんなお話でしたか。'),
        ('約束を忘れてしまって、申し訳ない気持ちです。', '申し訳なく感じているのですね。まず相手に謝る言葉を伝えてみませんか。'),
        ('ずっと探していた物が見つかって、安心しました。', '見つかってよかったですね。ほっとしますね。'),
        ('今日はいろいろ重なって、何も考えず休みたいです。', 'いろいろあって疲れたのですね。今はゆっくり休めるといいですね。'),
        ('応援していた人が頑張っていて、私も励まされました。', '頑張る姿に励まされたのですね。気持ちが伝わってきます。'),
    ),
    'question_back': (
        ('映画の券は玲さんの分が二枚、私の分が一枚です。私の分は何枚ですか。', 'あなたの分は一枚です。'),
        ('入口の案内係は小田さんで、出口の案内係は栗原さんです。出口では誰に聞けばいいですか。', '出口では栗原さんに聞けばよいです。'),
        ('先に靴を磨いて、その後で鞄を拭きます。先にするのはどちらですか。', '先に靴を磨きます。'),
        ('レンタルの皿は十二枚で、そのうち二枚は予備です。予備を除くと何枚使えますか。', '十枚使えます。'),
        ('水曜日の集まりは十九時からで、入場は十八時半からです。入場できるのは何時からですか。', '十八時半から入場できます。'),
        ('貸出の傘は長い方が残っています。短い方は借りられません。今借りられるのはどちらですか。', '長い傘を借りられます。'),
        ('商品を受け取るのは私で、支払いをするのは父です。支払いをするのは誰ですか。', 'お父さんです。'),
        ('小さい棚は空で、大きい棚には箱があります。箱があるのはどちらの棚ですか。', '大きい棚です。'),
    ),
    'ambiguity': (
        ('いくつか候補がありますが、まだ名前を伝えていません。おすすめを決めてほしいです。', '候補を教えてもらえますか。'),
        ('家からそこまで行きたいです。どこへ行くかはまだ話していません。', 'どこへ行きたいですか。'),
        ('この文章をもっと短くできますか。文章は次のメッセージで送ります。', 'はい。短くしたい文章を送ってください。'),
        ('二つの荷物のうち、それを先に運んでくださいと頼まれました。どちらか分かりません。', 'どちらの荷物を先に運べばよいか確認しましょう。'),
        ('予定の時間を確認したいのですが、予定そのものをまだ説明していません。', 'どの予定の時間を確認したいですか。'),
        ('何人分の飲み物を用意するか考えています。人数はまだ分かりません。', '来る人数を確認してから必要な飲み物の量を決めましょう。'),
        ('いつもの相手に連絡してください。相手の名前は共有していません。', '連絡する相手は誰ですか。'),
        ('箱は二個と伝えました。何個必要か聞かれたら、その数で答えてください。', '二個です。'),
    ),
    'role_boundary': (
        ('私が昨日見た夢を話しました。あなたも実際にその夢を見たことになりますか。', 'いいえ、あなたが見た夢のお話です。'),
        ('小説の中で「僕は浜田だ」と人物が名乗っています。浜田はあなたの本名ですか。', 'いいえ、小説の登場人物の名前です。'),
        ('姉が弟に荷物を渡しました。あなたが受け取ったことにして答えてよいですか。', 'いいえ、受け取ったのは弟さんです。'),
        ('あなたが提案しただけの場所を、私が予約した場所と呼んでよいですか。', 'いいえ、提案したことと予約したことは別です。'),
        ('私は来月引っ越すかもしれません。必ず引っ越すと決まったことになりますか。', 'いいえ、まだ可能性の話で、決定したわけではありません。'),
        ('あなた自身の実際の出身校を、会話を合わせるために作ってください。', '実際の出身校はありません。架空の学校を実際の出身校とは説明できません。'),
        ('友人の彩さんが料理を作りました。誰が作ったか聞かれたら何と答えますか。', '友人の彩さんが作りました。'),
        ('友人が送った写真です。あなたが現場へ行って撮ったと説明できますか。', 'いいえ、友人が送った写真で、私が撮影したものではありません。'),
    ),
    'symbols': (
        ('参加票の記号は「M-7」です。「M-1」ではありません。正しい記号をそのまま教えてください。', 'M-7'),
        ('メモには「14:20」と書いてあります。この時刻を数字で返してください。', '14:20'),
        ('二つの文字列「abc」と「xyz」があります。「xyz」の方を選んで、その文字列を答えてください。', 'xyz'),
        ('保存先の名前は「memo_4」です。「memo_9」ではありません。保存先の名前を答えてください。', 'memo_4'),
        ('合図には丸「○」を使い、三角「△」は使いません。使う記号を答えてください。', '○'),
        ('席の番号は「B12」から「B13」に訂正しました。今の番号だけ教えてください。', 'B13'),
        ('二つの札「上」と「下」から、「下」を除いた札を答えてください。', '上'),
        ('メモの数は「2,000」です。「200」ではありません。書かれた数をそのまま返してください。', '2,000'),
    ),
}

#Each list ends with a User turn. Earlier Assistant bodies are provided gold,
#but rollout evaluation replaces them with real generated Assistant responses.
DIALOGUES = {
    'correction': (
        (['本は棚の上段へ戻します。', 'はい、上段へ戻すのですね。', '置き場所を下段へ変えました。今はどこへ戻しますか。'], '下段へ戻します。'),
        (['借りる椅子は五脚の予定です。', '五脚ですね。', '必要な数を三脚に訂正します。最終的には何脚ですか。'], '三脚です。'),
        (['連絡は平井さんにします。', '平井さんへ連絡するのですね。', '担当変更で町田さんへ連絡します。今の相手は誰ですか。'], '町田さんです。'),
        (['参加する日は土曜と伝えました。', '土曜ですね。', '日曜へ訂正しました。何曜日に参加する予定ですか。'], '日曜です。'),
        (['集合は午前十時です。', '午前十時ですね。', '午前十一時へ遅らせます。今の集合時刻を答えてください。'], '午前十一時です。'),
        (['包装は青いひもにします。', '青いひもですね。', '赤いひもに変更しました。今使うひもは何色ですか。'], '赤色です。'),
        (['注文の飲み物は牛乳です。', '牛乳ですね。', '豆乳へ変更しました。今注文している飲み物は何ですか。'], '豆乳です。'),
        (['荷物の送り先は二号室です。', '二号室ですね。', '三号室へ変えます。', '三号室へ変更ですね。', 'その変更を撤回して元へ戻します。送り先はどこですか。'], '二号室です。'),
    ),
    'followup': (
        (['昼の休憩は四十分あります。', '四十分ですね。', 'その時間をもう一度教えてもらえますか。'], '四十分です。'),
        (['預けた袋の中にはスリッパが入っています。', 'スリッパを入れた袋ですね。', '袋に入れた物は何でしたか。'], 'スリッパです。'),
        (['私は甘い菓子より塩味の菓子が好きです。', '塩味の菓子が好きなのですね。', '私の好みはどちらの味でしたか。'], '塩味です。'),
        (['次の電話は高橋さんから来ます。', '高橋さんからですね。', '電話をかけてくる人の名前を確認してください。'], '高橋さんです。'),
        (['私の予約番号は二十五番です。', '二十五番ですね。', '予約番号はいくつでしたか。'], '二十五番です。'),
        (['家を出る前に戸締まりを確認します。', '出る前に戸締まりですね。', '出る前に確認することをもう一度答えてください。'], '戸締まりです。'),
        (['明日の集合場所は港の待合所です。', '港の待合所ですね。', '集合時刻は正午です。', '正午ですね。', '場所だけもう一度確認したいです。どこでしたか。'], '港の待合所です。'),
        (['自転車は弟の物です。', '弟さんの自転車ですね。', 'ヘルメットは私の物です。', 'ヘルメットはあなたの物ですね。', '自転車は誰の物か、もう一度答えてください。'], '弟さんの物です。'),
    ),
    'context': (
        (['朝の担当は岸さんで、午後の担当は森さんです。', '朝は岸さん、午後は森さんですね。', '午後に来た人は誰へ声をかければよいですか。'], '森さんです。'),
        (['切り花は客間、鉢植えはベランダに置きます。', '切り花は客間、鉢植えはベランダですね。', '鉢植えを置く場所を答えてください。'], 'ベランダです。'),
        (['持っていくのは白いタオルです。', '白いタオルですね。', 'タオルだけ灰色へ変えます。', '灰色のタオルへ変更ですね。', '今持っていく物を色と一緒に答えてください。'], '灰色のタオルです。'),
        (['遊ぶ場所は南の公園です。', '南の公園ですね。', '待ち合わせだけ東の公園にします。遊ぶ場所は変えません。', '待ち合わせは東、遊ぶのは南の公園ですね。', '遊ぶ場所はどちらの公園ですか。'], '南の公園です。'),
        (['書類を持つのは私で、提出するのは姉です。', '持つのはあなた、提出はお姉さんですね。', '弟は送迎をします。', '弟さんは送迎ですね。', '提出する人は誰でしたか。'], 'お姉さんです。'),
        (['最初に袋を開け、次に中身を確かめます。', '袋を開けてから中身を確認するのですね。', '最後に袋を畳みます。', '最後は袋を畳むのですね。', '中身を確かめる前に何をしますか。'], '袋を開けます。'),
        (['火曜は映画、水曜は買い物の予定です。', '火曜は映画、水曜は買い物ですね。', '映画だけ木曜へ移します。', '映画は木曜へ変更ですね。', '買い物の内容は変えません。', '買い物は水曜のままですね。', '映画と買い物はそれぞれ何曜日ですか。'], '映画は木曜、買い物は水曜です。'),
        (['昼食は私と伯父の二人で取ります。', 'あなたと伯父さんですね。', '伯父ではなく伯母でした。訂正します。', '一緒なのは伯母さんですね。', '場所は食堂です。', '食堂ですね。', '誰と昼食を取るのか答えてください。'], '伯母さんと取ります。'),
    ),
}


def main():
    manifest = read_json(DATA / 'manifest.json')
    assert manifest['status'] == 'reviewed_TRAIN_frozen_before_unseen_DEV'
    assert sha256(DATA / 'train.jsonl') == manifest['train']['sha256']
    assert not (DATA / 'dev.jsonl').exists() and not (DATA / 'dev_authored.json').exists()
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    cases, targets = [], []
    for category in CATEGORIES:
        entries = SINGLE[category] if category in SINGLE else DIALOGUES[category]
        assert len(entries) == 8
        for index, (prompt, body) in enumerate(entries):
            turns = [prompt] if isinstance(prompt, str) else prompt
            assert len(turns) % 2 == 1
            messages = [dict(role='user' if turn % 2 == 0 else 'assistant', content=text)
                        for turn, text in enumerate(turns)]
            assert all(message['content'] and '\ufffd' not in message['content'] and '<|im_' not in message['content']
                       for message in messages)
            assert tok.decode(tok.encode(body)) == body
            case_id = f'semantic-unseen-{category}-{index + 1:02d}'
            _, removed = tok.chat_prompt(messages, 960)
            assert removed == 0 and 2 <= len(tok.encode(body)) + 1 <= 65
            checks = ['提示された条件と話者を保ち、最後のUserの依頼に自然に答える。',
                      '知らない情報や実体験を作らず、不要な前置きや反復を加えない。',
                      '文法・関連性・実履歴文脈を既存rubricで判断し、gold単語一致で採点しない。']
            record = dict(id=case_id, family_id=case_id, split='dev', category=category,
                          messages=messages, checks=checks)
            cases.append(record)
            targets.append(dict(id=case_id, category=category, messages=messages,
                                gold_body=body, rationale='独立した自然文の状況に対する固定NLL用の一つの妥当な回答。別の自然な生成もrubricで認める。'))
    context_cases = [case for case in cases if len(case['messages']) > 1]
    assert len(context_cases) == 24
    own_turns = sum(sum(message['role'] == 'user' for message in case['messages']) for case in context_cases)
    assert own_turns == 59
    train_final = {row['messages'][-2]['text'] for row in
                   (json.loads(line) for line in (DATA / 'train.jsonl').read_text().splitlines())}
    overlap = sorted(case['id'] for case in cases if case['messages'][-1]['content'] in train_final)
    assert not overlap, overlap
    dump_jsonl(DATA / 'dev.jsonl', cases)
    atomic_json(DATA / 'dev_authored.json', dict(created_at=now(), TRAIN_manifest_sha256=sha256(DATA / 'manifest.json'),
                                               author='Codex nonblind', independent_human=False, targets=targets,
                                               protected_TEST_used=False, used_TRAIN_renderer=False))
    report = dict(created_at=now(), families=80, own_families=24, own_responses=59,
                  categories=dict(Counter(case['category'] for case in cases)),
                  own_turn_distribution=dict(Counter(sum(message['role'] == 'user' for message in case['messages']) for case in context_cases)),
                  dev_sha256=sha256(DATA / 'dev.jsonl'), authored_sha256=sha256(DATA / 'dev_authored.json'),
                  TRAIN_manifest_sha256=sha256(DATA / 'manifest.json'), TRAIN_frozen_at=manifest['created_at'],
                  TRAIN_frozen_before_new_DEV=True, exact_final_question_overlap=0,
                  surface_flags=0, used_TRAIN_renderer=False, protected_TEST_used=False,
                  semantic_family_identity='independently authored situation, not a TRAIN-generated slot variant',
                  independence_limitations='same Codex author/nonblind; broad semantic similarity is not fully excluded',
                  GPU_learning_updates=0, all_TRAIN_independent_human_certified=False)
    atomic_json(RUN / 'dev_preparation.json', report)
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
