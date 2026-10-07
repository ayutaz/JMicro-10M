"""Persist explicit Codex judgments after actual reading; never an automated judge."""
import argparse
import json
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from complete_base_sigsoftmax import checked, load_policy, CONFIG, RAW, NOTES
from review_textbook_quantity_comparison import validate_notes

# Only genuinely changed outputs receive fresh numeric judgments here.
# Populated after all80 original prefix/text/stop rows have been read in two40 chunks.
MANUAL = {
    'base-002': [1,1,0,0,'帰宅と母の導入は部分的に合うが母父の呼称を引用内で連続し、発話も出来事も完成させない。'],
    'base-011': [2,2,0,0,'疲れて早寝した導入には沿うが、翌朝の体のだるさを同じ表現で循環して述べ、展開せず上限で途切れる。'],
    'base-012': [2,2,0,0,'傘を持っていたと持っていなかったを同じ人物について切替え、理由も持っていないからという循環になる。'],
    'base-014': [2,2,0,0,'遅延と待ち合わせの語は拾うが、電車が遅れたら遅れるという同じ発言を二度示し、状況を進めずEOS停止。'],
    'base-019': [1,1,0,0,'息が切れる接続は成立するが、その後は母の引用が同じ呼称の連続に崩れ、運動場面の展開や完結がない。'],
    'base-027': [2,1,0,0,'既に霧が出た状況で霧を待つことへ戻り、姉との登山から友達の遊びの誘いへ移って同じ引用を反復する。'],
    'base-031': [1,1,0,0,'朝の挨拶におめでとうを接続した後、言葉を話し合うことから楽しく学ぶという未完の句を連続する。'],
    'base-034': [2,1,0,0,'礼の返答へ進まず、助けてくれてありがとうをその同じ言葉で説明する自己参照となり最後の文も未完。'],
    'base-039': [1,1,0,0,'明日の集合時刻を答えず今日は何時だよへ変わり、お話を聞くという句を連続して応答を完成させない。'],
    'base-041': [2,1,0,0,'マグカップを腹の中に入れることを容易とも困難とも述べ、手に収まる大きさの説明として意味が崩れる。'],
    'base-042': [2,2,0,0,'秋の空の色という話題は保つが、青い夜空の同一描写を何度も並べ、場面の変化や終結へ進まない。'],
    'base-049': [1,1,0,0,'車の窓にいる虫の導入後、虫は虫が怖がって怖がるという不自然な主語の文を連続し、冬の状況を展開しない。'],
    'base-050': [1,1,0,0,'柔らかい毛布に触ると痛いと突然述べ、その後は柔らかくの接続句を繰返すだけで意味も文も完結しない。'],
    'base-051': [1,1,0,0,'残りは食べたという接続が不自然で数量を答えず、おいしいと食べたの同一場面を繰返して終わる。'],
    'base-056': [1,2,0,0,'二十度は十五度より低いと大小関係を逆にし、温度が低いとという未完の条件句へ崩れて反復する。'],
    'base-057': [2,1,0,0,'最初の合計三つは正しいが、その後は箱の中に箱についての文字があるという自己参照を反復し数量の説明から逸れる。'],
    'base-059': [2,2,0,0,'午後三時から一時間後を午後二時と答え、休憩時間を同じ休憩時間で説明する循環を経てEOSで止まる。'],
    'base-062': [1,1,0,0,'持ってきた菓子を作ることへ戻り、お菓子はお菓子の中に食べてという接続も崩れ同じ句を連続する。'],
    'base-065': [2,2,1,0,'名前を書き留める話題は部分的に保つが、ノートの文章が青空文庫の本棚に並ぶ移行を説明せず、同じ説明で終わる。'],
    'base-067': [1,2,0,0,'伝言を引用する初文は沿うが、先に行きますを先に行くとその先に行くとという未完の条件句で反復する。'],
    'base-072': [1,1,0,0,'鍵の紛失に鍵を開ける行為を繰返して接続し、置き場所を探す場面や文の完結に進まない。'],
    'base-074': [2,1,0,0,'買い物メモを牛乳が牛乳やパンの間に入る説明へ変え、最後は牛乳の中に牛乳が入るという循環でEOS停止。'],
    'base-075': [2,1,0,0,'春を感じた場面から春の日と日本の歴史の一般論へ逸れ、日本の歴史が歴史を象徴するという説明を反復して終わる。'],
    'base-076': [1,1,0,0,'真偽の再確認を本を読むことへ変え、その後はおもしろいことにという引用内の句を連続し未完で止まる。'],
    'base-080': [2,1,0,0,'別れの挨拶から笑い合う場面には部分的につながるが、おいしいという発話と笑いを反復して別れを進めない。'],
    'base-081': [2,1,0,0,'母の誕生日に何をするかへ進まず、自分の園芸好みから花が開花を待つ同一文を連続する。擬人化だけを失敗とはしない。'],
    'base-082': [2,1,0,0,'自転車の鍵が見つからないのに鍵を開ける行為へ戻り、開けても見つからないという同一循環でEOS停止。'],
    'base-084': [2,1,0,0,'犬を花火の音から守る行為へ進まず、怖がるという言葉を同じ言葉で引用して説明する循環で終わる。'],
    'base-091': [2,1,0,0,'暖かい部屋の氷が部屋へ戻るという移動や楽になる説明に逸れ、冷やす氷の記述も加わり融解の因果を保たない。'],
    'base-095': [1,2,0,0,'喉の渇きと水を飲む話題は保つが、入れて飲むと喉が渇いたのでを循環させ、述語を完成せず上限に達する。'],
    'base-096': [2,1,0,0,'赤信号で止まる行為を述べず、車が走ると走らないを切替え、車が車の中に入る場面へ崩れて反復する。'],
}


def sources(policy, config):
    refs = policy['references']
    proposal = checked(config['proposal'])
    snapshot = checked(proposal['references']['base_completed_objective_studies_v2_20261007.json'])
    completed = {row['arm']: row['completion'] for row in snapshot['conditions']}
    phase = ROOT/'reports/phase6'
    references = [('cached_CE', refs['cached_control_raw'], refs['cached_control_notes'])]
    for arm, folder in [('middle_supervision','base-middle-supervision-comparison-20261007'),
                        ('sam','base-sam-comparison-20261007'),
                        ('on_policy_teacher','base-on-policy-teacher-comparison-20261007'),
                        ('confidence_penalty','base-confidence-penalty-comparison-20261007'),
                        ('native_teacher_KD','base-native-teacher-KD-science-comparison-20261007'),
                        ('native_hint','base-native-hint-comparison-20261007')]:
        old = checked(completed[arm])
        raw = phase/folder/'evaluation'/arm/'evaluation/generation.json'
        references.append((arm, dict(path=str(raw),sha256=old['generation_sha256']), old['notes']))
    return [(name, {row['id']: row for row in checked(raw)['outputs']},
             {row[0]: row for row in checked(note)['notes']}) for name,raw,note in references]


def main(inspect=False):
    config, policy = load_policy()
    rows, notes = read_json(RAW)['outputs'], read_json(NOTES)
    if len(rows) != 80 or len({r['id'] for r in rows}) != 80:
        raise ValueError('Exact complete80 required')
    prior = sources(policy, config)
    matches, new = {}, []
    for row in rows:
        for name, generated, rated in prior:
            old = generated.get(row['id'])
            if old and all(row[k] == old[k] for k in ('id','prefix','text','stop_reason')):
                matches[row['id']] = (name, rated[row['id']])
                break
        else:
            new.append(row['id'])
    if inspect:
        print(json.dumps(dict(exact_prior_scores_to_preserve=len(matches),fresh_judgment_ids=new),ensure_ascii=False))
        return
    if set(MANUAL) != set(new) or any(any(value is not None for value in row[1:5]) for row in notes['notes']):
        raise ValueError('Preserve prior scores; provide every new explicit judgment once')
    all_notes, reused = [], []
    for row in rows:
        identifier = row['id']
        if identifier in matches:
            name, old = matches[identifier]
            all_notes.append(list(old))
            reused.append(dict(id=identifier,reference=name,scores=old[1:5]))
        else:
            all_notes.append([identifier,*MANUAL[identifier]])
    notes.update(reviewer='Codex nonblind; all current80 individually read in two40 chunks; exact historical numeric scores and reasons preserved',
        notes=all_notes, all80_individually_read=True, fresh_individual_judgments=len(new),
        exact_historical_ratings_preserved=reused, historical_ratings_changed=False,
        reading_evidence='Both ordered40 chunks inspected in this goal turn before assigning new judgments; no automatic or independent human judge',
        created_at=now(), source=dict(path=str(Path(__file__)),sha256=sha256(Path(__file__))))
    validate_notes(rows,notes,sha256(RAW))
    atomic_json(NOTES,notes)
    print(json.dumps(dict(status='all80_content_notes_recorded',fresh=len(new),preserved=len(matches))))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser()
    parser.add_argument('--inspect',action='store_true')
    main(parser.parse_args().inspect)
