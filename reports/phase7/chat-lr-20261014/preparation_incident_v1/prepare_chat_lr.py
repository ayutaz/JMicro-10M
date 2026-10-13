"""Rebind unchanged accepted TRAIN; author new DEV before any candidate learning."""
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from jmicro.teacher_chat_training import teacher_lr
from chat_lr_contract import RUN, OLD, DATA, B, SPEC, CONTROL_SPEC, reference, require_ref
from audit_chat_semantic_dev import shingles

SINGLE = {
 'greeting': [
  ('おはようございます。朝の支度が終わって、今ようやく座れました。', 'おはようございます。少しひと息つけますね。'),
  ('こんにちは。駅で待ち時間ができたので、話し相手になってほしいです。', 'こんにちは。どんなお話をしましょうか。'),
  ('夜の片付けを終えました。寝る前に一言だけ挨拶しに来ました。', 'こんばんは。今日もお疲れさまでした。'),
  ('しばらく使っていませんでした。また短い話から付き合ってください。', 'お久しぶりです。どんなお話をしましょうか。'),
  ('もう休憩が終わるので戻ります。話を聞いてくれて助かりました。', 'どういたしまして。気をつけて戻ってくださいね。'),
  ('今日からこちらでお世話になります。まずはよろしくお願いします。', 'こちらこそ、よろしくお願いします。'),
  ('こんにちは、ほんの少し顔を出しました。今日は落ち着いた一日です。', 'こんにちは。落ち着いて過ごせているのですね。'),
  ('質問に付き合ってくれてありがとう。今日のやり取りはここでおしまいです。', 'どういたしまして。またお話ししましょう。'),
 ],
 'daily': [
  ('古い写真を箱にまとめたら、棚の上が広くなりました。', '棚がすっきりしてよかったですね。'),
  ('朝、洗ったカップをしまってから窓辺の席でお茶を飲みました。', '落ち着いた朝を過ごせたのですね。'),
  ('店が休みだったので、買い物は明日に回して帰ってきました。', '今日はお休みだったのですね。明日行けるといいですね。'),
  ('昼に少し横になったら、夕方の作業を始めやすくなりました。', '休息で少し元気が戻ったのですね。'),
  ('靴箱を片付けていたら、去年使っていた靴べらが見つかりました。', '見つかってよかったですね。'),
  ('雨がやんだ間に、ポストまで手紙を出しに行けました。', '雨の合間に用事を済ませられてよかったですね。'),
  ('今日は料理をせず、冷蔵庫にあった煮物を温めました。', 'ある物で夕食を用意できたのですね。'),
  ('いつもより早いバスに乗れたので、約束の場所で少し待っています。', '余裕を持って着けたのですね。'),
 ],
 'emotion': [
  ('楽しみにしていた展示が休館だったので、少しがっかりしました。', 'それは残念でしたね。また行けるといいですね。'),
  ('初めて作ったスープを家族がおいしいと言ってくれて嬉しいです。', '喜んでもらえてよかったですね。'),
  ('忘れたと思っていた鍵がかばんから出てきて、ほっとしています。', '見つかって安心しましたね。'),
  ('人前で名前を呼ばれるだけでも、今日は少し緊張しそうです。', '緊張するのですね。ゆっくり息を整えてみませんか。'),
  ('楽しみな予定の前なのに、準備に抜けがないか心配になりました。', '楽しみと心配があるのですね。一緒に確認しますか。'),
  ('友達から短い便りが届き、思った以上に元気が出ました。', '便りが嬉しい励みになったのですね。'),
  ('作業を途中まで進めましたが、今日は疲れが出てきました。', 'お疲れさまです。少し休んでもよさそうですね。'),
  ('予定を無事に終えたので、今はのんびりしていたい気分です。', 'お疲れさまでした。ゆっくり過ごせるといいですね。'),
 ],
 'question_back': [
  ('診察券は財布に、領収書は封筒に入れました。領収書を探すなら何を開けますか。', '封筒を開けます。'),
  ('焼くのはパンで、冷やすのはゼリーです。冷やす物を答えてください。', 'ゼリーです。'),
  ('乗るバスは五番で、降りる停留所は橋の前です。バスの番号は何番ですか。', '五番です。'),
  ('返却する道具はドライバーだけで、ペンチはまだ使います。返す道具は何ですか。', 'ドライバーです。'),
  ('先に写真を選び、その後でアルバムに貼ります。最初の作業を教えてください。', '写真を選びます。'),
  ('手紙を送る相手は従姉です。何を送るかではなく、相手を答えてください。', '従姉さんです。'),
  ('今日の受付は二階です。一階には休憩所があります。受付は何階でしょう。', '二階です。'),
  ('鉢植えには朝だけ水をやります。夕方にも水やりをする予定ですか。', 'いいえ、朝だけです。'),
 ],
 'ambiguity': [
  ('それを置く場所は、もう一方でよいでしょうか。', '何をどの場所に置くお話でしょうか。'),
  ('どちらか一つを今日中に選びたいのですが、手伝ってもらえますか。', 'どんな二つの候補か教えてください。'),
  ('あの返事を、もう少し柔らかく直したいです。', '直したい返事の文章を教えてください。'),
  ('ここへ向かう方法なら、どれを使うのがよさそうですか。', '出発地と行き先、使える交通手段を教えてください。'),
  ('さっきの数字は大きすぎたでしょうか。', 'どの数字を何に使ったお話でしょうか。'),
  ('必要な方だけ残しておいてください。', '候補と、何に必要なのかを教えてください。'),
  ('その時間に間に合うか、見てもらいたいです。', '何時までに、何を済ませる予定でしょうか。'),
  ('この順番で続けていいか迷っています。', 'どんな作業をどの順番で進めているか教えてください。'),
 ],
 'role_boundary': [
  ('姉は「私は先に帰る」、私は「もう少し残る」と言いました。残るのは誰ですか。', 'あなたです。'),
  ('父から私へ鍵を渡しました。鍵を受け取ったのはあなたでしょうか。', 'いいえ、受け取ったのはあなたです。'),
  ('同僚の「私は午後に休む」という発言をメモしました。休むのは私ですか。', 'いいえ、同僚の方です。'),
  ('もし店が開いていれば寄ります。店が開いていることは確認済みですか。', 'いいえ、その情報だけでは確認済みとはいえません。'),
  ('あなたが出した案はまだ検討中です。私が採用したと判断してよいですか。', 'いいえ、まだ検討中です。'),
  ('友人は白い靴、私は黒い靴を履きました。白い靴を履いたのは誰でしょう。', '友人です。'),
  ('実体験として、あなたが昨日乗った電車の話をしてもらえますか。', '私は実際に電車に乗った体験はありません。'),
  ('これは作り話です。もし私が鳥なら空を飛びます。私は本当に鳥ですか。', 'いいえ、仮定の作り話です。'),
 ],
 'symbols': [
  ('案内の見出しは「夕方の支度」です。かぎ括弧も含めて見出しだけ返してください。', '「夕方の支度」'),
  ('整理番号はR-8です。間のハイフンも残して、番号だけ書いてください。', 'R-8'),
  ('机の札は「済」で、まだの「未」ではありません。札の一文字だけ返してください。', '済'),
  ('予定を表す文字列は9:05です。コロンを消さずにそのまま書いてください。', '9:05'),
  ('合図は☆です。星の記号を一つだけ返してもらえますか。', '☆'),
  ('フォルダの名前はbox_7です。下線を含めて名前だけ繰り返してください。', 'box_7'),
  ('メモには「風・海」と書きました。中点を含めてその二文字を返してください。', '風・海'),
  ('並びはD→A→Eです。矢印を残して並びだけ出力してください。', 'D→A→E'),
 ],
}

DIALOGUES = {
 'correction': [
  (['荷物は売店で受け取ります。', '売店で受け取るのですね。', '売店ではなく案内所でした。受け取る場所はどこですか。'], '案内所です。'),
  (['お弁当は三つ頼みました。', '三つですね。', '一つ取り消したので二つです。届く数はいくつでしょう。'], '二つです。'),
  (['電話する相手は管理人さんです。', '管理人さんですね。', '今回は受付の方へ電話します。今の相手を答えてください。'], '受付の方です。'),
  (['会場は東棟だと聞きました。', '東棟ですね。', '案内では西棟でした。どちらの棟へ行けばいいですか。'], '西棟です。'),
  (['カーテンは長い方を使います。', '長い方ですね。', '長すぎたので短い方にしました。使う方はどちらですか。'], '短い方です。'),
  (['返す期限は木曜の予定です。', '木曜ですね。', '一日早く水曜になりました。何曜日に返すのでしょう。'], '水曜です。'),
  (['帽子は紺、上着は灰色を用意しました。', '帽子は紺、上着は灰色ですね。', '帽子だけ茶色へ替えます。', '帽子は茶色へ変更ですね。', '上着は替えません。二つの色を教えてください。'], '帽子は茶色、上着は灰色です。'),
  (['椅子を窓側、机を入口側へ置きます。', '椅子は窓側、机は入口側ですね。', '椅子だけ壁側へ移します。', '椅子は壁側ですね。', '机も壁側へ移す案は取り消します。', '机は入口側のままですね。', '最後の椅子と机の場所はどこですか。'], '椅子は壁側、机は入口側です。'),
 ],
 'followup': [
  (['クリップは丸い缶にしまいました。', '丸い缶ですね。', 'クリップを探すなら何の中を見ればよいですか。'], '丸い缶の中です。'),
  (['この包みは祖父へ渡します。', '祖父さんへ渡すのですね。', '包みを受け取る人を教えてください。'], '祖父です。'),
  (['冷蔵庫のジュースはぶどう味です。', 'ぶどう味ですね。', '飲み物の味をもう一度答えてください。'], 'ぶどう味です。'),
  (['折り紙は八枚使います。', '八枚ですね。', '使う枚数を忘れたので教えてください。'], '八枚です。'),
  (['洗うのはタオルで、干す場所は庭です。', 'タオルを庭に干すのですね。', '洗う物は何でしたか。'], 'タオルです。'),
  (['予約の名前は佐々木です。', '佐々木さんですね。', '到着が少し遅れるかもしれません。', '到着が遅れるかもしれないのですね。', '予約名を受付に伝えるので答えてください。'], '佐々木です。'),
  (['読む予定の雑誌は料理の特集です。', '料理の特集ですね。', '読む場所は後で決めます。', '場所は後で決めるのですね。', '雑誌は何の特集でしたか。'], '料理の特集です。'),
  (['最初に靴を磨き、その後でひもを通します。', '磨いてからひもを通すのですね。', 'ひもの色はまだ決めていません。', '色は未定なのですね。', 'ひもを通す前に何をしますか。'], '靴を磨きます。'),
 ],
 'context': [
  (['お皿は戸棚の奥、コップは手前です。', 'お皿は奥、コップは手前ですね。', 'コップだけ取りたいときはどちらを見ますか。'], '手前です。'),
  (['母は布を切り、私は印を付けます。', 'お母さんが切り、あなたが印を付けるのですね。', '布を切る担当は誰ですか。'], 'お母さんです。'),
  (['図書館は明日行き、今日は書類をまとめます。', '今日は書類、明日は図書館ですね。', '本を返しに行く日は今日ですか。'], 'いいえ、明日です。'),
  (['手帳は青い袋、名札は赤い袋に入れます。', '手帳は青、名札は赤ですね。', 'どちらの袋も車に置きます。', '両方とも車ですね。', '名札を入れた袋の色は何色でしょう。'], '赤色です。'),
  (['新しい封筒を買い、古い封筒は処分します。', '新しい物を買い、古い物を処分ですね。', '処分は明日行います。', '処分は明日ですね。', '買うのは古い方でしたか。'], 'いいえ、新しい方です。'),
  (['飲むのは水で、お茶は来客用です。', 'あなたは水、お茶は来客用ですね。', '来客は午後に来ます。', '午後の来客ですね。', '自分が飲む物を答えてください。'], '水です。'),
  (['午前は郵便局、午後は薬局へ寄ります。', '午前は郵便局、午後は薬局ですね。', '薬局ではマスクを買います。', 'マスクを買うのですね。', '午前に寄る場所を教えてください。'], '郵便局です。'),
  (['借りる本は地理、返す本は歴史です。', '地理を借りて歴史を返すのですね。', '借りる本を科学へ替えます。返す本は同じです。', '科学を借りて歴史を返すのですね。', '返す本だけ答えてください。'], '歴史の本です。'),
 ],
}


def dump(path, rows):
    assert not path.exists(), str(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n' for row in rows))


def main():
    assert not (DATA / 'dev.jsonl').exists(), 'Prepared DEV retained, never overwrite'
    old_path = ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json'
    old = read_json(old_path)
    train_path = require_ref(old['arms']['S1']['records'])
    manifest_path = require_ref(old['arms']['S1']['manifest'])
    manifest = read_json(manifest_path)
    assert manifest['status'] == 'reviewed_TRAIN_frozen_before_unseen_DEV'
    qa_path = OLD / 'train_content_review_final.json'
    qa = read_json(qa_path)
    assert qa['samples'] == 280 and qa['errors'] == 0 and qa['status'] == 'fixed_sample_passed'
    train = [json.loads(line) for line in train_path.read_text().splitlines()]
    assert len(train) == 41529 and all(row['split'] == 'train' for row in train)
    tok = Tokenizer(require_ref(old['tokenizer']))
    atomic_json(RUN / 'TRAIN_reuse.json', dict(passed=True, recorded_at=now(), TRAIN=reference(train_path),
        manifest=reference(manifest_path), QA=reference(qa_path), original_frozen_at=manifest['created_at'],
        new_TRAIN_targets=0, new_QA_judgments=0, whole_TRAIN_human_certified=False, protected_TEST_used=False))
    cases, targets = [], []
    for category, entries in {**SINGLE, **DIALOGUES}.items():
        assert len(entries) == 8
        for n, (prompt, body) in enumerate(entries):
            turns = [prompt] if isinstance(prompt, str) else prompt
            messages = [dict(role='user' if i % 2 == 0 else 'assistant', content=text) for i, text in enumerate(turns)]
            assert len(turns) % 2 == 1
            case_id = f'lr-unseen-{category}-{n + 1:02d}'
            checks = ['最後のUserの依頼に、提示された条件・話者・訂正を守って自然に答える。',
                      '未提示の事実や体験を作らず、質問の対象を他の項目へ取り違えない。',
                      '元rubricで文法・関連性・実履歴文脈を判断する。妥当な別回答を認め、gold語一致で採点しない。']
            cases.append(dict(id=case_id, family_id=case_id, split='dev', category=category, messages=messages, checks=checks))
            targets.append(dict(id=case_id, messages=messages, gold_body=body,
                                rationale='提示事実と最後の質問から成立する一つの回答。自由生成は別の妥当な回答も認める。'))
    contexts = [case for case in cases if len(case['messages']) > 1]
    counts = [sum(m['role'] == 'user' for m in case['messages']) for case in contexts]
    assert len(cases) == 80 and len(contexts) == 24 and sum(counts) == 59 and set(counts) == {2, 3, 4}
    question_index = defaultdict(set)
    questions = {}
    for row in train:
        text = row['messages'][-2]['text']
        questions[row['doc_id']] = text
        for part in shingles(text):
            question_index[part].add(row['doc_id'])
    previous_questions = {case['messages'][-1]['content'] for ref in old['suites'].values()
                          for case in (json.loads(line) for line in require_ref(ref).read_text().splitlines())}
    overlaps, near, flags, window_rows = [], [], [], []
    for case, target in zip(cases, targets, strict=True):
        assert all(tok.decode(tok.encode(m['content'])) == m['content'] for m in case['messages'])
        prompt, removed = tok.chat_prompt(case['messages'], 960)
        assert removed == 0
        body = target['gold_body']
        assert tok.decode(tok.encode(body)) == body
        window = list(tok.sft_windows(case['messages'] + [dict(role='assistant', content=body)], context=1025))[-1]
        selected = [v for v in window['labels'] if v != -100]
        assert selected == tok.encode(body) + [7] and 2 <= len(selected) <= 65 and window['removed_turns'] == 0
        window_rows.append(dict(id=case['id'], teachers=len(selected), prompt_tokens=len(prompt)))
        q = case['messages'][-1]['content']
        if q in set(questions.values()) or q in previous_questions:
            overlaps.append(case['id'])
        parts = shingles(q)
        matching = Counter(key for part in parts for key in question_index.get(part, ()))
        for key, intersection in matching.items():
            similarity = intersection / len(parts | shingles(questions[key]))
            if similarity >= .8:
                near.append(dict(id=case['id'], TRAIN_id=key, Jaccard8=similarity))
        for m in case['messages']:
            if not m['content'] or '\ufffd' in m['content'] or '<|im_' in m['content']:
                flags.append(case['id'])
    dump(DATA / 'dev.jsonl', cases)
    atomic_json(DATA / 'dev_authored.json', dict(created_at=now(), author='Codex nonblind',
        independent_human=False, used_TRAIN_renderer=False, TRAIN_manifest_sha256=sha256(manifest_path), targets=targets))
    audit = dict(passed=not (overlaps or near or flags), recorded_at=now(), families=80, own_families=24,
        own_responses=59, own_turn_distribution=dict(Counter(counts)), exact_final_question_overlap=overlaps,
        near_Jaccard8_at_least80percent=near, surface_flags=flags,
        dev_sha256=sha256(DATA / 'dev.jsonl'), authored_sha256=sha256(DATA / 'dev_authored.json'),
        source_TRAIN_sha256=sha256(train_path), original_TRAIN_frozen_at=manifest['created_at'],
        TRAIN_frozen_before_new_DEV=manifest['created_at'] < read_json(DATA / 'dev_authored.json')['created_at'],
        protected_TEST_used=False, independent_human=False, blind=False, semantic_independence_fully_certified=False,
        windows=window_rows, source=reference(Path(__file__)))
    atomic_json(RUN / 'dev_audit.json', audit)
    assert audit['passed'], 'Keep actual failed DEV audit; do not relax separation'
    historical = [json.loads(line) for line in require_ref(old['fixed_NLL']).read_text().splitlines()]
    assert len(historical) == 2554
    fixed = []
    labels = dict(S0_TRAIN='historical_TRAIN', S1_TRAIN='TRAIN', new_DEV='semantic_DEV', RPC_DEV='RPC_DEV')
    for row in historical:
        fixed.append(dict(row, dataset=labels[row['dataset']], previous_dataset=row['dataset']))
    for target in targets:
        messages = target['messages'] + [dict(role='assistant', content=target['gold_body'])]
        window = list(tok.sft_windows(messages, context=1025))[-1]
        teachers = sum(v != -100 for v in window['labels'])
        fixed.append(dict(id='lr-newDEV-' + target['id'], dataset='new_DEV', split='dev', messages=messages,
            teachers=teachers, body_bytes=len(target['gold_body'].encode()),
            window_binding=hashlib.sha256(json.dumps(window, ensure_ascii=False, sort_keys=True).encode()).hexdigest()))
    assert len(fixed) == len({row['id'] for row in fixed}) == 2634
    dump(DATA / 'nll_fixed.jsonl', fixed)
    atomic_json(RUN / 'nll_preparation.json', dict(passed=True, fixed=reference(DATA / 'nll_fixed.jsonl'),
        previous_fixed=old['fixed_NLL'], targets=2634, datasets=dict(Counter(row['dataset'] for row in fixed)),
        fresh_targets=80, previous_targets_preserved=2554, protected_TEST_used=False))
    dry = read_json(OLD / 'S1_dry_run.json')
    actual = read_json(OLD / 'S1/training_audit.json')
    assert actual['passed'] and actual['Assistant_teachers'] == dry['Assistant_teachers'] == 1899557
    # Same unchanged accepted stream/batch/budget: reuse its complete CPU input
    # schedule. Only recompute LR and its cumulative decoupled decay effect.
    scaled = []
    for row in dry['rows']:
        next_row = dict(row)
        next_row['lr'] = row['lr'] * (SPEC['lr'] / CONTROL_SPEC['lr'])
        scaled.append(next_row)
    new_dry = dict(dry, rows=scaled, inherited_consumption=reference(OLD / 'S1_dry_run.json'),
                  inherited_actual_training=reference(OLD / 'S1/training_audit.json'),
                  log_decay=sum(math.log1p(-r['lr'] * .01) for r in scaled),
                  decay_coefficient=math.exp(sum(math.log1p(-r['lr'] * .01) for r in scaled)),
                  numerical_source_unchanged=True, new_GPU_updates=0, quality_evidence=False)
    atomic_json(RUN / 'S1_dry_run.json', new_dry)
    atomic_json(RUN / 'preparation.json', dict(passed=True, created_at=now(), source=reference(Path(__file__)),
        old_config=reference(old_path), TRAIN_reuse=reference(RUN / 'TRAIN_reuse.json'),
        DEV_audit=reference(RUN / 'dev_audit.json'), NLL=reference(RUN / 'nll_preparation.json'),
        dry_run=reference(RUN / 'S1_dry_run.json'), new_GPU_updates=0, model_quality_complete=False))
    print('Unchanged TRAIN/QA reused; new80/24/59 DEV and2634 common NLL frozen; GPU0')


if __name__ == '__main__':
    main()
