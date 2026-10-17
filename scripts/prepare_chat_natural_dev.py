"""Author80 new DEV families after TRAIN freeze; export four known DEV suites.

The original mixed Chat file is never opened. Its80 DEV prompts are recovered
verbatim from an already completed, DEV-only historical evaluation, with the
original case/rubric fields and source binding preserved.
"""
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.tokenizer import Tokenizer
from jmicro.data import normalized
from prepare_chat_natural_sources import ROOT, DATA, RUN, now, save, sha

CATEGORIES = ('greeting','daily','emotion','question_back','ambiguity','role_boundary','symbols','correction','followup','context')
SINGLES = {
'greeting': [
('こんにちは。用事を済ませたので少しお話ししたいな。','こんにちは。何のお話をしましょうか。'),
('おはよう。今日はいつもよりゆっくり起きたんだ。','おはようございます。ゆっくりできたのですね。'),
('こんばんは。帰ってきたところだよ。','こんばんは。おかえりなさい。'),
('今夜はここで失礼するね。話を聞いてくれてありがとう。','こちらこそ、ありがとうございました。おやすみなさい。'),
('また会話しに来ました。よろしくね。','また来てくれてうれしいです。よろしくお願いします。'),
('やっほー。少しだけ付き合ってくれる？','もちろんです。何をお話ししましょうか。'),
('ありがとう。助かったよ。','どういたしまして。お役に立ててうれしいです。'),
('今日はもう寝ようかな。ひとこと挨拶してね。','おやすみなさい。ゆっくり休んでくださいね。')],
'daily': [
('靴箱を片付けたいけれど、どこから始めようかな。','まず使っていない靴を分けてみませんか。'),
('読みかけの雑誌がたまってしまったよ。','一冊ずつ、気になる記事から読んでみませんか。'),
('外は雨なので、室内でできる軽い楽しみを一つ教えて。','好きな曲を聴いてみるのはどうでしょう。'),
('来客まで三十分あるので、玄関だけ掃除するつもり。','玄関だけなら取りかかりやすそうですね。'),
('明日の持ち物を今のうちにまとめておこうと思う。','必要な物を一覧にして確認するとよさそうです。'),
('洗濯物を畳んだので、少し休みたいな。','お疲れさまです。ひと息つきましょう。'),
('帰宅後の用事が多いので、まず優先順位を決めたい。','今日中に必要な用事から並べてみませんか。'),
('ちょっと気分を変えたい。手軽な方法を一つだけ。','窓を開けて外の空気を感じてみませんか。')],
'emotion': [
('練習で昨日より上手にできて、うれしい。','上達を感じられるとうれしいですね。'),
('楽しみにしていた展示が中止になって残念。','楽しみにしていた分、残念ですね。'),
('ずっと借りていた本を返せて、ほっとした。','無事に返せて安心しましたね。'),
('新しい集まりに参加する前で緊張しているよ。','初めての場所は緊張しますね。無理せず過ごしてください。'),
('友人にお礼を言ってもらえて、温かい気持ちになった。','お礼を伝えてもらえるとうれしいですね。'),
('小さな失敗を引きずって、気分が沈んでいる。','失敗が気になるのですね。少し休んでみませんか。'),
('ようやく探していた楽譜が見つかった。うれしいな。','見つかってよかったですね。演奏が楽しみですね。'),
('連絡の返事を待っていて、そわそわしている。','待つ間は落ち着かないですね。別のことをしてみませんか。')],
'question_back': [
('封筒は厚い方が四枚、薄い方が一枚です。薄い封筒は何枚ですか。','一枚です。'),
('受付は二階、休憩所は地下です。休憩所はどこですか。','地下です。'),
('担当は午前が野口さん、午後が沢村さんです。午後の担当は誰ですか。','沢村さんです。'),
('展示は十一時開始で、受付は十時半からです。展示の開始時刻はいつですか。','十一時です。'),
('先に窓を閉めてから鍵をかけます。最初に何をしますか。','窓を閉めます。'),
('葉書が七枚あり、二枚使いました。残りの葉書は何枚ですか。','五枚です。'),
('午前は晴れで午後は雨という予報です。雨なのはいつですか。','午後です。'),
('紙袋に布、木箱に糸を入れました。糸があるのはどちらですか。','木箱です。')],
'ambiguity': [
('その道具の使い方を教えて。道具の名前はまだ言っていないよ。','どの道具の使い方を知りたいですか。'),
('この文章を読みやすくしてほしい。文章は後で送るね。','読みやすくしたい文章を送ってください。'),
('駅の近くのお店を探して。どの駅かはまだ伝えていない。','どの駅の近くで探しましょうか。'),
('二つある作品のうち、あちらを選んでと言われたけれど分からない。','どちらの作品か確認しましょう。'),
('会場へ行く時刻を決めたいけれど、開始時刻を忘れた。','まず開始時刻を確認しましょう。'),
('贈り物の候補を考えて。相手の好みはまだ話していないよ。','贈る相手の好みを教えてもらえますか。'),
('どちらの予定を先にすべき？予定の内容はまだ説明していない。','二つの予定の内容を教えてください。'),
('ほしい付箋は三枚と伝えました。付箋の数をもう一度答えて。','三枚です。')],
'role_boundary': [
('友人が山登りをしたと話しました。登ったのはあなたですか。','いいえ、山登りをしたのはご友人です。'),
('物語では主人公が川辺さんと名乗ります。あなたの本名が川辺さんになりますか。','いいえ、物語の登場人物の名前です。'),
('妹が叔母に写真を渡しました。写真を受け取ったのはあなたですか。','いいえ、受け取ったのは叔母さんです。'),
('予約する案を出しただけです。もう予約済みと答えてよいですか。','いいえ、まだ予約済みとは言えません。'),
('来週見学に行くかもしれません。見学は確定していますか。','いいえ、まだ確定していません。'),
('会話に合わせて、あなたが実際に育った町をでっち上げて。','実際に育った町はありません。事実としては作れません。'),
('花瓶を作ったのは隣人の葉子さんです。誰の作品ですか。','隣人の葉子さんの作品です。'),
('祖父が書いた手紙です。あなたが書いた手紙だと説明できますか。','いいえ、お祖父さんが書いた手紙です。')],
'symbols': [
('受付番号は「K-28」で、「K-82」ではありません。番号だけ返して。','K-28'),
('集合時刻は「09:45」です。その数字表記を返して。','09:45'),
('文字列「pqr」と「stu」のうち、「pqr」をそのまま答えて。','pqr'),
('保存する名前は「note_6」です。名前だけ答えて。','note_6'),
('使う印は「□」です。「◇」ではありません。使う印だけ答えて。','□'),
('部屋の表示を「C21」から「C24」に直しました。今の表示は？','C24'),
('札の文字は「東」と「西」です。「東」を除いた方を答えて。','西'),
('記録された数値は「7,500」です。そのまま返してください。','7,500')]
}

DIALOGUES = {
'correction': [
(['植木鉢は玄関に置きます。','玄関ですね。','植木鉢は玄関ではなくベランダへ変更します。今の置き場所は？'],'ベランダです。'),
(['封書は水曜日に送ります。','水曜日ですね。','発送を金曜日に訂正します。','金曜日に発送ですね。','封書を送るのは何曜日でしたか。'],'金曜日です。'),
(['参加者は六人です。','六人ですね。','訂正します。参加者は四人でした。今は何人ですか。'],'四人です。'),
(['糸の色は紫にします。','紫ですね。','色は橙に変えます。','橙ですね。','使う糸の色は何でしたか。'],'橙です。'),
(['会場は北館です。','北館ですね。','北館ではなく南館でした。会場を答えて。'],'南館です。'),
(['案内役は吉岡さんです。','吉岡さんですね。','案内役を森下さんに変更します。','森下さんですね。','今の案内役の名前を教えて。'],'森下さんです。'),
(['必要なのは画用紙です。','画用紙ですね。','画用紙ではなく方眼紙でした。必要な紙は？'],'方眼紙です。'),
(['集合は十三時です。','十三時ですね。','集合を十四時に変更します。','十四時ですね。','変更後の集合時刻は？'],'十四時です。')],
'followup': [
(['休日に刺繍を始めたいです。','刺繍を始めたいのですね。','さっき始めたいと言った趣味は何ですか。'],'刺繍です。'),
(['市場で桃を買いました。','桃を買ったのですね。','市場で買った果物は何でしたか。'],'桃です。'),
(['発表の題は星空です。','星空が題ですね。','発表は来月です。','来月なのですね。','私の発表の題を覚えていますか。'],'星空です。'),
(['今日は玄関の棚を直しました。','玄関の棚を直したのですね。','今日直したのはどこの棚でしたか。'],'玄関の棚です。'),
(['週末は植物園に行く予定です。','植物園ですね。','友人と二人で行きます。','友人と二人ですね。','週末に行く予定の場所は？'],'植物園です。'),
(['借りた本は木工の入門書です。','木工の本ですね。','借りたのは何の入門書でしたか。'],'木工の入門書です。'),
(['贈り物は手編みの手袋です。','手編みの手袋ですね。','祖母へ渡します。','お祖母さんへの贈り物ですね。','贈る品物は何でしたか。'],'手編みの手袋です。'),
(['休憩に麦茶を飲みました。','麦茶を飲んだのですね。','休憩に飲んだ物を教えて。'],'麦茶です。')],
'context': [
(['上の引き出しに切手、下の引き出しに輪ゴムを入れました。','上に切手、下に輪ゴムですね。','輪ゴムが入っている引き出しはどちらですか。'],'下の引き出しです。'),
(['姉は鍵を持ち、兄は地図を持ちます。','鍵はお姉さん、地図はお兄さんですね。','私は水を持ちます。','あなたは水ですね。','地図を持つ人は誰でしたか。'],'お兄さんです。'),
(['昨日は図書室、今日は資料室へ行きました。','昨日が図書室、今日が資料室ですね。','今日行ったのはどちらの部屋ですか。'],'資料室です。'),
(['午前に散髪、午後に買い物をします。','午前に散髪、午後に買い物ですね。','夕方には帰宅します。','夕方に帰宅ですね。','散髪をする時間帯はいつでしたか。'],'午前です。'),
(['包むのは父、運ぶのは母です。','包むのがお父さん、運ぶのがお母さんですね。','包む担当は誰ですか。'],'お父さんです。'),
(['黄色い紐は使い、灰色の紐は使いません。','使うのは黄色い紐ですね。','使わない紐の色は何ですか。'],'灰色です。'),
(['月曜日に見学、木曜日に面談をします。','月曜に見学、木曜に面談ですね。','見学だけ火曜日へ移します。','見学は火曜ですね。','面談は元の曜日のままです。','面談は木曜のままですね。','見学と面談はそれぞれ何曜日でしたか。'],'見学は火曜、面談は木曜です。'),
(['大きい袋には布、小さい袋には毛糸を入れました。','大きい袋に布、小さい袋に毛糸ですね。','布が入っている袋はどちらですか。'],'大きい袋です。')]
}


def dump(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False) + '\n')


def main():
    manifest = json.loads((DATA / 'manifest.json').read_text())
    assert manifest['status'] == 'TRAIN_frozen_before_new_DEV'
    assert not (DATA / 'dev_suites/new.jsonl').exists()
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    train_questions = set()
    for arm in ('C0', 'C1'):
        ref = manifest['arms'][arm]['records']
        assert sha(Path(ref['path'])) == ref['sha256']
        for line in Path(ref['path']).read_text().splitlines():
            r = json.loads(line)
            train_questions.update(normalized(r['messages'][i-1]['text']) for i in r['target_message_indices'])
    cases, authored = [], []
    for category in CATEGORIES:
        entries = SINGLES.get(category, DIALOGUES.get(category))
        assert len(entries) == 8
        for i, (prompt, answer) in enumerate(entries, 1):
            turns = [prompt] if isinstance(prompt, str) else prompt
            messages = [dict(role='user' if j % 2 == 0 else 'assistant', content=text) for j, text in enumerate(turns)]
            assert normalized(messages[-1]['content']) not in train_questions
            assert tok.chat_prompt(messages, 992)[1] == 0
            assert 2 <= len(tok.encode(answer))+1 <= 32
            uid = f'natural-unseen-{category}-{i:02}'
            cases.append(dict(id=uid, family_id=uid, category=category, split='dev', messages=messages,
                checks=['提示条件と話者を守って最後の質問に自然に答える。',
                        '未提供の属性を作らず、短く完結する。反復・復唱で代用しない。',
                        '文法・関連性・自生成履歴の文脈を別々に判定。gold単語一致だけで意味を採点しない。']))
            authored.append(dict(id=uid, category=category, messages=messages, gold_body=answer))
    contexts = [c for c in cases if len(c['messages']) > 1]
    assert len(cases) == 80 and len(contexts) == 24
    assert sum(sum(m['role'] == 'user' for m in c['messages']) for c in contexts) == 59
    dump(DATA / 'dev_suites/new.jsonl', cases)
    save(DATA / 'new_DEV_authored.json', dict(author='Codex nonblind', independent_human=False, targets=authored,
        TRAIN_manifest_sha256=sha(DATA / 'manifest.json'), created_at=now(), protected_TEST_used=False))
    legacy = json.loads((ROOT / 'configs/phase7/chat-lr-20261014.json').read_text())
    refs = {'new': dict(path=str(DATA / 'dev_suites/new.jsonl'), sha256=sha(DATA / 'dev_suites/new.jsonl'))}
    provenance = {}
    for new_name, old_name in (('lr', 'new'), ('semantic', 'semantic'), ('generalization', 'previous'), ('original', 'old')):
        if old_name == 'old':
            source = ROOT / 'reports/phase7/chat-lr-20261014/evaluation/S1/t3/old/greedy/result.json'
            saved = json.loads(source.read_text())
            assert saved['protected_test_used'] is False
            assert saved['binding']['suite_sha256'] == legacy['suites']['old']['sha256']
            old = [r for k, r in saved['outputs'].items() if k.startswith('suppressed-')]
            fields = ('id','family_id','category','split','messages','checks')
            old = [{key: r[key] for key in fields} for r in old]
            provenance[new_name] = dict(path=str(source), sha256=sha(source),
                original_suite_sha256=legacy['suites']['old']['sha256'], original_mixed_file_opened=False,
                export_method='Exact DEV case fields from completed raw evaluation; generated replies not used as gold')
        else:
            source = Path(legacy['suites'][old_name]['path'])
            assert sha(source) == legacy['suites'][old_name]['sha256']
            old = [json.loads(line) for line in source.read_text().splitlines()]
            provenance[new_name] = dict(path=str(source), sha256=sha(source))
        assert len(old) == 80 and all(r['split'] == 'dev' for r in old)
        assert len({r['family_id'] for r in old}) == 80
        target = DATA / f'dev_suites/{new_name}.jsonl'
        dump(target, old)
        refs[new_name] = dict(path=str(target), sha256=sha(target))
    # Fixed paired NLL: same80 new DEV +64 actual TRAIN targets per arm.
    nll = []
    for row in authored:
        nll.append(dict(id='DEV-'+row['id'], dataset='new_DEV', split='dev',
            messages=row['messages']+[dict(role='assistant', content=row['gold_body'])]))
    from inventory_chat_natural import digest
    for arm in ('C0', 'C1'):
        rows = [json.loads(line) for line in Path(manifest['arms'][arm]['records']['path']).read_text().splitlines()]
        targets = sorted([(digest(arm+':NLL42:'+r['doc_id']+':'+str(i)),r,i) for r in rows for i in r['target_message_indices']], key=lambda t:t[0])[:64]
        for j, (_, row, index) in enumerate(targets):
            nll.append(dict(id=f'{arm}-TRAIN-{j:02}', dataset=arm+'_TRAIN', split='train', messages=row['messages'][:index+1]))
    assert len(nll) == 208
    dump(DATA / 'nll_fixed.jsonl', nll)
    save(RUN / 'DEV_preparation.json', dict(status='DEV_frozen', created_at=now(), suites=refs, provenance=provenance,
        TRAIN_manifest_sha256=sha(DATA / 'manifest.json'), TRAIN_frozen_at=manifest['created_at'],
        TRAIN_frozen_before_new_DEV=True, families=80, own_families=24, own_responses=59,
        categories=dict(Counter(c['category'] for c in cases)), exact_final_question_TRAIN_overlap=0,
        source=str(Path(__file__)), source_sha256=sha(Path(__file__)), max_new_tokens=32,
        NLL=dict(path=str(DATA / 'nll_fixed.jsonl'), sha256=sha(DATA / 'nll_fixed.jsonl'), targets=208),
        protected_TEST_used=False, independent_human=False, all2190_content_reviews_pending=True,
        scope_limit='Formal Base retention not inferred from Chat NLL; authored DEV is not blind TEST'))
    print('New80 DEV + four exact historical DEV exports +208 fixed NLL targets frozen', flush=True)


if __name__ == '__main__':
    assert sys.version_info[:3] == (3,12,7)
    main()
