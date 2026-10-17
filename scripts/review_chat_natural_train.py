"""Persist Codex nonblind individual TRAIN QA, then filter the preserved draft.

Notes refer to the displayed target, user and previous turn. Full-history raw
bindings are retained; this is sampled editorial QA, not verified human labels
or full-corpus semantic certification. Rejected text is never corrected into
synthetic new teaching examples.
"""
from collections import Counter
import json
from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from prepare_chat_natural_sources import DATA, RUN, now, save, sha
from inventory_chat_natural import digest

NOTES = '''
挨拶だけに突然子猫と息子の逸話で無関連
韓国料理の好みに麺名を添えて応答
最近の趣味にDIYの具体例で応答
夏の予定を未定と帰省候補で答える
国内旅行の好みを返し相手にも質問
仕事の調子を多忙と答える
挨拶を返し休日予定を尋ねる
好きな食べ物に魚と回答
挨拶を返し趣味を尋ねる
短い相互挨拶として成立
家事の残りに共感し内容を尋ねる
夏の予定を仕事中心と回答
キャンプには今年行けないと回答
豆腐食品の話題を維持して回答
ゲーム動画からプロの話を継続
黒い服の効果とアクセサリの色を継続
アーモンドバターの理解を肯定
室内仕事かという質問に応答
休日の寝坊から朝昼兼用へ展開
食事内容にカレーと直接回答
描く絵の種類を具体化
SNS利用を閲覧中心と回答
競馬の当てにくさへ相づち
子供時代の夢に政治関係と回答
夏休み予定を近場と回答
昼食にテイクアウトと回答
趣味として水泳を挙げる
こんにちはにおはようと時刻の挨拶が不整合
外出の有無と行先を答える
旅行好きと一人旅の経験を答える
長期休暇がないと回答
昼食に弁当と回答
趣味探しに在宅時間の話で応じる弱い雑談
相互のよろしくで完結
初回から妻という未設定の家族属性を付加
挨拶を返し仕事の終了を尋ねる
衣替えの予定らしいが直前表示だけでは対象が曖昧
軽食かという確認に食事配分を答える
スマホゲーム利用に数独を例示
JPOPの好みに歌手名を添える
うどんのトッピング案を追加
既存の夫の話に謝意と例外を添えるが人物属性は未検証
子供の外遊びの日焼けに対策を質問
パンと飲物の対比からご飯と茶へ継続
ゲームへの関心と難易度質問
未経験という発言に楽しさを伝える
四国旅行に好意的に反応
小学生問題の難しさに共感
朝の挨拶から休暇予定を質問
暑さと食欲から夕食を尋ねる
喫茶店の有無を答えるが所在地の裏付けなし
日付が与えられていないのに25日と断定
調子の質問に疲れと回答
お盆の予定を具体化
安らぐ時間に一人の時間と回答
地域の食べ物にこんにゃくと回答だが地域は未設定
入力にない相手の名前しをを使用
夜の相互挨拶として成立
旅行していないと理由を返す歴史的雑談
仕事かという質問に肯定
仕事の困難から自身の感染経験へ転じる人間会話で医療知識ではない
冷たい甘味への共感と店舗利用の質問
映画の好みに応じ鑑賞頻度を質問
知ったきっかけに作品と曲名を返す
この後の予定を在宅と答える
好きな仕事の選択肢へ希望を返す
猫の特徴について相づち
究極の質問という主張の理由を確認
趣味にダンスと回答
好きな登場人物を回答
外出予定なしと話題を返す
学校行事の中止という話を継続する歴史的雑談
休日の過ごし方に動画視聴と回答
朝食未摂取と回答
趣味の質問にドライブを挙げる
8月という入力に一年の経過を返す
位置情報なしでそちらの近くと断定
趣味にPCを挙げるが仕事という個人属性を付加
挨拶に休日確認を返す
直前の行動にラムネと回答する人間会話
夜の挨拶からゲームの話題へ
挨拶から困り事の質問へ
夜の挨拶に応じ試験勉強の話を開始
店の話から周辺の犬や雑貨へ継続
背脂系への好みを返すが年齢変化は未検証の人間発言
音楽制作の方法を具体的に説明
餃子アレンジへ共感し好みを追加
服の流行への説明だが日本全般への一般化が強い
そうめんの食べ方を前の話へ接続
動画の犬種を確認する質問
台湾の飲茶に関心を返す
ゲーム経験から現在の集中力へ雑談
ウニの好みを直接否定
行きたい国に米国と回答
一日観光と計画という流れを継続
挨拶だけに猫の出産逸話で無関連
就寝前習慣は特になしと回答
趣味探しに屋内外の好みを確認
寝坊に共感し前日の疲れを確認
京都の美術館等を提案する雑談で施設検証ではない
運動の好き嫌いを回答
今日が休みかに夏休みと回答
昼食作りに料理名を質問
挨拶を返し音楽の好みを質問
表記違いを含む相互挨拶
未設定なのに学生だという個人属性を断定
休日の過ごし方へ前の墓参りの話を継続
ホテル朝食の取り過ぎへ共感
スキー経験の有無を回答
香水のつけ過ぎに推測として応じる
一人散策への感想と自分との対比
UXという相手の回答を受け質問
相手が飼う猫に関心を返す
釣った魚の調理時刻に回答
動画を見ないという先の発言を壊さず人気の話へ
気分転換の話を締めてお礼
国内旅行の移動方法で間接肯定
学びながら執筆する姿勢へ感想
ペットは飼っていないと回答
挨拶を返し夕刻らしい雑談だが実時刻の裏付けなし
最近の出来事に動画視聴の話を返す
近所の居酒屋の有無を返すが所在地の裏付けなし
挨拶から家族旅行の有無を質問
挨拶だけに私も文系と前提のない話を開始
労いを返し休日か確認
料理名を聞かれて今日あったと述べるだけで答えていない
趣味に博物館巡りと回答
夜の挨拶と体調確認
挨拶から休日確認へ
未設定の身体属性として動物アレルギーを断定
食物の話からサルの例へ展開
漫画推薦に謝意とゲーム機の話を継続
芸能グループのテレビ番組を質問
旅行を迷う文脈で行先希望を返す
コーヒーの話に未設定の旦那の逸話を追加
猫の好みを答える人間の過去経験談
好きな飲物に酒と回答
動画の話から関連するゲームの話題へ
マスクで判別しづらい話へ共感
九州の食の話を継続
持ち帰った品の具体名を尋ねる
朝の挨拶を返し休暇確認
好きな食べ物に寿司という選好
休日の活動を列挙する人間会話
安眠の助言が抽象的で実行性が低い
休日活動としてランチと旅行を回答
夏休みの子供の様子へ相づち
物価上昇の話題を継続
映画推薦前にジャンルを確認
夜の短い相互挨拶
挨拶から翌日の休日を質問
猫の話に実際の自宅への招待を提示
履歴に匿名化記号CEが残るためそのまま学習させない
Netflixの話題を続ける
料理の好き嫌いに反応するが給食の因果は曖昧
宿泊形式にホテルと回答
弁当準備の負担へ共感
監督の話を継続し近作を質問
体重変化に驚きで応答し健康助言はしない
弓道の難しさを受け道具を質問
思い出を振り返った感想を確認
旅行の目的を観光と研修と回答
海外グルメから渡航希望へ継続
朝の挨拶と朝食の質問
ゲーム端末を答え好みを質問
挨拶と天候の雑談で所在地の裏付けなし
休日の活動にカフェと旅行を回答
お盆休みはないと回答
労いを返し食事の話題を開始
趣味に音楽と回答
夜の相互挨拶
挨拶から翌日の仕事確認
就寝時刻に子供という未設定属性を付加
昼食未摂取と理由を回答
映画推薦にシリーズ名を返す
サバ缶の話へ調理案を添える
暑さと湿度の話を継続する雑談
猛暑への感想を返すが過去気温の検証ではない
履歴に匿名化記号IHが残るためそのまま学習させない
朝食内容を具体的に回答
視聴媒体にテレビと回答
ペンギンの様子へ短い感想
旅行という確認への相づち
朝のつらさへ共感し仕事を質問
朝食内容を具体的に回答
趣味にDIYを挙げる
朝の挨拶と暑さの雑談
挨拶と猫への関心
挨拶を返し趣味を質問
初対面の相互挨拶
予定に仕事と回答する人間会話
犬猫両方好きで犬寄りと回答
旅行中の食事の話を継続
一台では同時利用不能という一般化が不正確
魚を見たかに肯定とカメラの準備を回答
海外勤務の話を継続する人間会話
在宅で運動不足という話を継続
ペットロボットへ関心を返す
お茶漬けへの好意的相づち
長編作品の一話の密度へ感想
ペルシャ猫の英訳として成立
食べることの英語表現だが名詞句ではeatingの方が明瞭
対象文章がないため提示を依頼
対象文章がないため提示を依頼
質問をまだ述べていないので質問を促す
庭の疑問の具体化を促す
三つの質問が書かれていないので質問を促す
質問見出しだけの壊れた入力なので除外
日本についての具体的質問を促す
猫はという冒頭指定を守る一文
レストランの条件と場所を確認
作品についての具体的質問を促す
名前を保持して英訳する
意味変更依頼に同義の言い換えだけで条件不達
質問自体がないため具体化を促す
確認対象の文がないため提示を依頼
詩がないため提示を依頼
日本料理の具体的質問を促す
指定された三語を含む例文
ロシア語の色という語の訳として成立
もしを使う条件文として成立
日本語学習の具体的質問を促す
原文がないため提示を依頼
集計対象文章がないため提示を依頼
食文化の具体的質問を促す
不明な音楽家の名前を確認
意味を調べる対象文の提示を依頼
台湾旅行の具体的質問を促す
修正対象文章がないため提示を依頼
こんにちはの発音をコンニチハと教えており不適切
レビュー本文がないため提示を依頼
私とあなたを使った例文
ゲームの具体的質問を促す
得意分野の簡潔な答え方の例
日本語の具体的質問を促す
説明すべき話題を確認
犬についての具体的質問を促す
料理名がないため確認
映画の具体的質問を促す
2000の二等分を1000と回答
学校制度の具体的質問を促す
AIについての具体的質問を促す
食文化の具体的質問を促す
音楽理論の具体的質問を促す
話題不明なので確認
研究についての具体的質問を促す
英文がないため提示を依頼
映画の具体的質問を促す
言い換え対象がないため提示を依頼
日本語の具体的質問を促す
2023年11月25日の曜日は土曜で一致
簡潔にしたいという希望に同意し話題を確認
文化についての具体的質問を促す
否定を保持した和訳
話の主という断片だけで会話教材として不十分
日本語の具体的質問を促す
説明対象がないため確認
著作権の具体的質問を促すだけで法的回答ではない
翻訳する語句がないため提示を依頼
数学の問題がないため提示を依頼
翻訳する英文がないため提示を依頼
SEOの具体的質問を促す
挨拶についての具体的質問を促す
タイトルを直訳する
学校の図書館をschool libraryと訳す
質問見出しだけの壊れた入力なので除外
HTML改行記号だけの壊れた入力なので除外
仕事が好きという文の英訳
2023年10月15日の曜日は日曜で一致
言語学習の具体的質問を促す
アニメについての具体的質問を促す
義母をいぼと読む誤答なので除外
一般知識の話題がないため確認
ビジネス用語の具体的質問を促す
翻訳原文がないため提示を依頼
文法についての具体的質問を促す
語彙や文法の具体的質問を促す
英文がないため提示を依頼
修正対象の文がないため提示を依頼
留学についての具体的質問を促す
解析対象の文がないため提示を依頼
説明しますというユーザー発言を説明依頼と取り違える
職場についての具体的質問を促す
説明はあるが問いがないため質問を促す
もちろんは正誤の先取りにも読めるが対象文を要求している
仕事についての具体的質問を促す
心理に関する10文字以上の句として成立
調査のテーマと具体的質問を確認
日本語の具体的質問を促す
説明する話題がないため確認
翻訳対象文がないため提示を依頼
日本語の具体的質問を促す
秋の俳句だが定型の音数が合わない
修正対象文がないため提示を依頼
文法の具体的質問を促す
水の俳句だが定型の音数が合わない
英語で話す方法を聞かれて方法を示さず質問を返す
皮膚についての具体的質問を促すだけで医療回答ではない
地名についての具体的質問を促す
文法確認対象がないため提示を依頼
'''.strip().splitlines()

REJECT = {1, 28, 35, 52, 57, 77, 96, 106, 124, 126, 130, 135,
          152, 153, 173, 179, 194, 208, 214, 230, 255, 266, 267, 272, 282, 293, 296, 297}


def additional_issue(messages, index):
    history = messages[:index+1]
    if any(re.search(r'<[A-Z]{1,4}>', m['text']) for m in history):
        return 'anonymized_identity_marker_in_context'
    user, answer = history[-2]['text'], history[-1]['text']
    if re.search(r'俳句|川柳', user):
        return 'poetry_requires_unavailable_mora_validation'
    if index == 1:
        pure = re.fullmatch(r'[\s。、，,!！?？ー〜～]*((こんにちは|こんにちわ|こんばんは|こんばんわ|おはようございます|はじめまして|初めまして|よろしく|宜しく|お願い|します|いたします|致します|です|どうぞ|ー|ー！|ございます|。|！|、|\s)+)[\s。!！]*', user)
        if pure and not re.search(r'こんにちは|こんにちわ|こんばんは|こんばんわ|おはよう|はじめまして|初めまして|よろしく|宜しく|お願い|どうも|こちらこそ|ですか|ますか|[?？]', answer):
            return 'unrelated_story_after_bare_greeting'
        if re.search(r'そちらの近く|[一二三四五六七八九十0-9０-９]+日じゃ', answer):
            return 'unprovided_location_or_date'
        if re.search(r'さん', answer) and not re.search(r'さん', user):
            return 'unprovided_name_in_initial_reply_conservative'
    if re.search(r'うちの旦那|妻と|子供と一緒|動物アレルギー', answer):
        return 'unsupported_personal_attribute'
    return None


def main():
    assert len(NOTES) == 300, len(NOTES)
    path = RUN / 'TRAIN_QA_review.json'
    if path.exists():
        raise FileExistsError('Do not silently revise the completed review')
    draft = json.loads((RUN / 'TRAIN_draft.json').read_text())
    samples = json.loads((DATA / 'TRAIN_QA_sample.json').read_text())
    assert sha(DATA / 'TRAIN_QA_sample.json') == draft['QA_sample']['sha256']
    notes = []
    rejected_pairs = set()
    for i, (sample, reason) in enumerate(zip(samples, NOTES, strict=True), 1):
        assert sample['id'] == f'QA{i:03}'
        assert digest(json.dumps(sample['messages'], ensure_ascii=False, sort_keys=True)) == sample['raw_binding']
        rejected = i in REJECT
        if rejected:
            rejected_pairs.add((sample['doc_id'], sample['target_message_index']))
        notes.append(dict(id=sample['id'], raw_binding=sample['raw_binding'],
            accepted_as_conversational_target=not rejected, reason=reason))
    arms = {}
    for arm in ('C0', 'C1'):
        ref = draft['arms'][arm]
        source = Path(ref['path'])
        assert sha(source) == ref['sha256']
        kept, excluded = [], Counter()
        for line in source.read_text().splitlines():
            row = json.loads(line)
            indices = []
            for index in row['target_message_indices']:
                reason = ('individual_QA_rejected' if (row['doc_id'], index) in rejected_pairs
                          else additional_issue(row['messages'], index))
                if reason:
                    excluded[reason] += 1
                else:
                    indices.append(index)
            if indices:
                kept.append(dict(row, target_message_indices=indices, messages=row['messages'][:indices[-1]+1]))
        target = DATA / f'{arm}_TRAIN.jsonl'
        with target.open('x') as stream:
            for row in kept:
                stream.write(json.dumps(row, ensure_ascii=False) + '\n')
        arms[arm] = dict(path=str(target), sha256=sha(target), families=len(kept),
            targets=sum(len(row['target_message_indices']) for row in kept), exclusions=dict(excluded))
    save(path, dict(status='sample_review_complete_with_exclusions', created_at=now(), samples=300,
        reviewer='Codex, nonblind, no independent human audit', rejected=len(REJECT), notes=notes, arms=arms,
        displayed_scope='Each target, immediate user, and preceding user/assistant turn; full raw history bound and retained',
        limitations=['Sample QA does not establish all-record semantic correctness',
            'Human RPC experience/preference language is conversational style, not verified Assistant identity or factual instruction',
            'Short Magpie is heavily clarification-biased; it cannot be described as629 direct-answer QA examples',
            'Small fixed post-QA additions are common to both arms; no fabricated corrections or replacement sample drawn'],
        protected_TEST_used=False, new_GPU_updates=0))
    print(json.dumps(dict(arms=arms, reviewed=300, rejected=len(REJECT)), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7)
    main()
