"""Actual all64 nonblind source observations; no source repairs or filtering."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from prepare_natural_story_source import RUN, PROPOSAL

REASONS = (
    'まりやが雪不足に困り、友達の協力で雪だるまを作って帰る。問題・援助・解決が同じ対象でつながる完結した物語。',
    '上京した男の子の不安から友達との練習へ進み、夢を続ける決意に至る。夢の具体的職業はないが、人物と感情の変化は一貫する。',
    '空を泳ぐクジラが夢を運び、少女を空へ連れていく幻想譚。山名のひらがなは奇妙だが、超自然的設定そのものを誤りとして落とさない。',
    '祭りのスイカ割りで太郎が外したあと成功し、みんなで食べる。手で振り回す記述は簡略だが、挑戦から結果への流れは明瞭。',
    '歌好きの女の子が箱のマイクを見つけて喜び、歌を続けて皆に聞かせる。小道具と感情の連続があり、始まりから結末まで保持。',
    '恭子とまりやが風船を飛ばして喜ぶ。友達の大切さという結びは定型的で説明が薄いが、共同体験からの感情としては可能。',
    '太陽の下で小動物が友達と遊ぶ短い描写。出来事の解決は小さいが、単純な絵本風の完結した場面として読める。',
    '空腹のアレックスが台所でクッキーの箱を見つけ、食べて遊びに戻る。おやつの発見を重ねて言うが、同じ対象の問題と解決が一致。',
    '節分で恭子とまりやが一緒に豆をまき、人が集まって楽しむ。共同作業から楽しさへ自然に接続する短い完結文。',
    'れいなが甘い香りをたどって果実の木へ行き、食べて幸せになる。対象と行動の流れが一貫した森の場面。',
    '川辺で彼が明治や学びを思い出し、今日も学ぶと決意する内省。人物の年齢は省略されているが、時代を思い出す記述だけで年齢矛盾とはしない。',
    '小魚が大きくなる目標を持って特訓し、やがて成長する。寓話として読めるので、成長の生物学的説明を欠くことだけでは落とさない。',
    'あかりがアイデアを盗まれても新しい案へ進む。秘密組織という創作背景と気持ちの切り替えが維持される。',
    '男の子が友達と山を登って頂上の景色を見て記憶に残す。目的・険しい道・到達した結果が整合する。',
    '星に時間移動の力をもらった少年が王様に正直さを教えて戻る。幻想設定が明示され、その中で行動と結末が一致する。',
    '子犬が公園で宝箱を見つけ、一人で持ち帰る。周りに人がいないことと単独行動の関係が明瞭な短い話。',
    '花に呼ばれた少女が夢の世界に入り冒険を楽しむ。花の中への移動は幻想として成立し、明白な対象の混同はない。',
    '雪国の犬と子供たちが遊んで笑顔になる。現在と過去の語尾は混ざるが、同じ雪遊びの場面として理解できる。',
    '地下で虫と友達になるが、「でも、友達がいなくなるのはさびしい」と未描写の喪失へ飛び、仲良くなる場面からの結論が弱い。弱い接続として記録。',
    '花畑で蝶の言葉を聞いた子供の悲しみが和らぐ。喪失の具体物は省略されているが、悲しみから慰めへの変化は読める。',
    '木の下で本を読む智也が、話す木から世界の話を聞く。木が話す設定は童話として可能で、問いと応答の対象が維持。',
    '侍が悲しい気持ちから子供たちとの遊びへ進む。時制の混在はあるが、出会いと気持ちの変化は一貫する。',
    '絵好きのスーが冷蔵庫の絵に悩み、母の励ましで笑顔になる。絵の出来栄えと気持ちの問題が同じ場面内で解決。',
    '祭りのあかりがおもちゃ作りをし、母との記憶から友達との新しい思い出へ進む。回想と現在の作業の接続が明確。',
    'ティミーがボールを貸さず友達を悲しませ、謝罪のため会いに行って遊ぶ。家でボールを投げる意図はやや粗いが、貸借の対立と和解が整合。',
    '宇宙猫の宙返りをそうすけとまりやがまねして笑う。幻想的な人物でも行動主体と笑いの結果が一貫する。',
    '雨で全員が帰宅しなければならない状況から一本の傘で全員が長くサッカーをできる展開は、雨よけの範囲や条件変更の説明が不足して弱い。義務の記述を実帰宅の断定に置換しない。',
    '智史が悲しい忍びの話を聞き、友達になって一緒に遊ぶ。隠した名前や悲劇の具体内容は省略されるが、気持ちの改善はつながる。',
    '恭子とまりやが音楽会で歌や踊りを楽しみ、手をつないで温かく感じる。対象・人物・結末が自然に保たれる。',
    '流れない星に願う女の子が、自分で夢へ進もうと決める。寓話的な結論で、願望から行動への変化が明瞭。',
    '亀が川を守ろうと決意し、ゴミ拾いと啓発をして皆が川を保つ。主体の行動と川を守る結果が整合する。',
    '泡に笑わされたという説明から友達が「しゃべるなんて嘘」と反論し、「本当に笑った」と応じるため、発言の対象と立証する内容がずれて接続が弱い。幻想性そのものは誤りとしない。',
    'あかりが宇宙人に地球の花や動物を教え、友達になって別れる。訪問目的、交流、帰還が整合した完結文。',
    'トラックが負傷した鳥を見て、驚かせたことへの謝罪を感じ、親切な人が助ける。驚かせた事実と突然の燃料充填が示されず、複数のつなぎが弱い。擬人化自体は許容。',
    '少年が遊び方を工夫し、友達を笑顔にする簡潔な話。遊びの詳細は省略されるが、目的と結果は保たれる。',
    'お化けの本を読んだそうすけが夢で会話し、起きて笑う。お化けの質問の含意は簡略だが、読書・夢・目覚めの時間順が一致。',
    '望遠鏡で星を見る少女が宇宙人と宇宙へ行き、星を見る。幻想の出会いを通じて初めの目的に戻る流れ。',
    'サムが庭で小うさぎと友達になる話は明瞭だが、母が自分の注意の理由を「きっと、だから…言ったのね」と推定する末尾が不自然で因果の結びが弱い。',
    '王国の女の子と友達が旅行を計画し、城を訪れ楽しむ。計画から到着した場面へのつながりが一貫。',
    'ティムが箱を埋め、後日掘り出して入っていたミニカーで遊ぶ。中身が最初に説明されないだけで中身の矛盾とはしない。',
    'そうすけと太郎の読書場面は読めるが、冒頭「ひとつの風が吹く日」は風の数え方が不自然な未解消表現。人物が二人いること自体を矛盾とはしない。',
    '森の不思議なバスが動物と子供を草原へ運び、遊んだ後に戻る。出発・行先・帰還が一貫した創作場面。',
    'カエルが遊ぶ途中に犬が来て、逃げられず食べられる。悲惨な結末でも出来事はつながり、幸福な話でないことを品質失敗にしない。',
    '魚が貝殻を使って模様を作り、満足して帰る幻想的な話。貝殻と共同作業の対象が最後まで維持される。',
    '湖で友達と古いコインを見つけ、その由来を想像する。主語の名前や「ていねい」の引用は省略的だが、対象と展開に明白な破綻はない。',
    '猫のそばで子供が幸せを感じ、猫が小さな宝を持ってくる。宝を見つける能力は創作上可能で、気持ちと対象が維持される。',
    '滑り台の順番争いを先生が仲裁し、子供全員が楽しく遊ぶ。対立と順番という解決策が一致した完結文。',
    '花作りに自信のない女の子が友達と手入れして自信を得る。「いつも失敗」ときれいな花は完全否定ではなく、自己評価の変化として読める。',
    '服をほめる宇宙人との交流は成立するが、「他の人を思いやることが一番の素敵」は述語を名詞にした不自然な結びが未解消。ほうきの比喩そのものを禁止しない。',
    'カニがカキの真珠を欲しがり、他人の物を取らないと反省する。未遂の欲望について謝る寓話として、実際に盗んだと誤読しない。',
    '家族思いの老亀が家族を遊びに誘い喜ばれる。じょうろの比喩は奇妙だが比喩として許容でき、主体と結果が維持。',
    '積み木と絵の意見対立を、電車を作って色を塗る共同活動で解決。トビーとサリーの希望が結果に結び付く自然な話。',
    '皆がソフトクリームを分ける流れはあるが、「私は一番好き」と「本当はみんな好き」の逆接は異なる尺度を対立させ、接続が弱い。量の計算誤りとはしない。',
    '大きな車を怖がりながら調べた少年が、動き出して逃げ帰り母に話す。母の褒め方は価値判断上議論できるが、物語の出来事は整合。',
    '少年が宝石入りの貝を見つけ、友達と宝を探し帰って祝う。創作の宝物を実世界の事実性で否定せず、対象の連続を確認。',
    '魚が亀の助言で練習し、レースで勝つ。練習の経過と目標達成がつながり、動物の会話は寓話として許容。',
    '宝を見つけられなかった少女が美しい石を見つけて友達に贈る。初めの未達と別の喜びを区別し、物の持ち主も一貫。',
    '男の子がお化けとおやつを食べて楽しむ。幻想的な相手でも、おやつと友人関係の対象が安定して閉じる。',
    '太郎と同行者が温泉に入り、智史が再訪を提案する。新しく名前が出る同行者を役割の誤りとはしない。',
    '冬に寒がる森の動物が集まって温まる。寒さという状態への行動と共同体験が一致する短い話。',
    '冒頭「むすんでいるように見えた太郎」は何を結ぶのか、何が結ばれるのかが未導入で述語の意味が成立しにくい。後半の公園のサッカーはつながるが、冒頭表現が未解消。',
    '宇宙の船で嵐に遭い、一人の子の指示と協力で乗り越える。超自然の背景でも、危機から解決への行動が一貫。',
    '雪の古い玩具から田中の幼少時代の喪失へ進む詩的場面だが、「ぎくりとした音」は驚きの状態を音に置き換えた不自然な導入が未解消。悲しい結末自体は落とさない。',
    '雨で音の調子を失った鐘が乾いて元の音に戻る。雨による鐘の影響は寓話上の設定として扱い、登場対象と時間の順は一致。',
)


def main():
    if (RUN/'content-review.json').exists(): raise ValueError('Preserve actual source review')
    repair = read_json(RUN/'metadata-repair-v2.json'); pilot = read_json(RUN/'content-pilot.json'); m = read_json(RUN/'manifest.json')
    if repair['status'] != 'complete_pending_fixed64_content' or alive(repair) or len(REASONS) != 64 or len(pilot['rows']) != 64:
        raise ValueError('Terminal repaired preparation and all64 observations required')
    if m['pilot_sha256'] != sha256(RUN/'content-pilot.json') or repair['manifest_sha256'] != sha256(RUN/'manifest.json'):
        raise ValueError('Actual frozen input differs')
    weak = {18,26,31,33,37,40,48,52,60,62}; grammar = {40,48,60,62}
    notes = [dict(id=r['id'], text_sha256=r['text_sha256'], content_quality=1 if i in weak else 2,
        weak_document=i in weak, unresolved_grammar_issue=i in grammar, unresolved_grounding_issue=False, reason=REASONS[i])
        for i,r in enumerate(pilot['rows'])]
    raw = dict(created_at=now(), pilot_sha256=m['pilot_sha256'], all64_individually_read=True, notes=notes,
        reviewer='Codex nonblind', independent_human_blind=False,
        grammar_flags='Unresolved natural grammatical expression, not proof that every marked phrase has no poetic reading.',
        no_original_text_or_selection_changes=True)
    atomic_json(RUN/'content-notes.json', raw)
    report = dict(status='all64_existing_natural_story_source_review_complete', created_at=now(), all64_read=True,
        pilot_sha256=m['pilot_sha256'], manifest_sha256=sha256(RUN/'manifest.json'), notes_sha256=sha256(RUN/'content-notes.json'),
        weak_documents=10, maximum_weak_documents=10, weak_count_gate_passed=True, unresolved_grammar_documents=4,
        unresolved_grounding_documents=0, training_pool_accepted=False, notes=notes,
        reviewer='Codex nonblind', independent_human_blind=False, external_fact_certification=False,
        limitations='Uniform64 of existing761448 TRAIN stories. Fantasy, unhappy endings, implicit characters and poetic form are not automatically failures; flagged natural phrasing remains unresolved.',
        scientific_teacher_tokens=0, GPU_seconds=0, protected_test_used=False,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False)
    atomic_json(RUN/'content-review.json', report)
    atomic_json(ROOT/'reports/phase6/natural_story_source_content_review.json', report)
    print(dict(read=64, weak=10, unresolved_grammar=4, unresolved_grounding=0, source_accepted=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
