"""Author a bounded transparent TRAIN supplement, then measure the paired recipe."""
from collections import Counter
import json
import re
from pathlib import Path
from answer_learning_common import ROOT,RUN,DATA,save,ref,bound,read_json,digest,now

DIRECTORY=DATA/'curriculum'
NAMES='アオイ カエデ コハル シオン ツバサ ナギ ハルカ ヒナタ ミオ ユウ リク レン アキラ イツキ カナタ キョウ サツキ スズネ セナ タクミ チハル ナオ フウカ マコト ミナト ムツキ ヤマト ユキ ヨウ ラン リオ ワカナ'.split()
DRINKS='紅茶 緑茶 ほうじ茶 麦茶 水 牛乳 豆乳 ココア コーヒー オレンジジュース りんごジュース 炭酸水 玄米茶 烏龍茶 ミルクティー レモン水'.split()
WORDS='りんご みかん ぶどう いちご もも なし すいか メロン さくら すみれ ひまわり たんぽぽ あじさい つばき もみじ いちょう えんぴつ けしごむ ノート じょうぎ ふでばこ はさみ かばん ぼうし くつ かさ いす つくえ とけい まど ほん はな'.split()
TIMES=[f'{i}時' for i in range(6,22)]


def oracle(family,messages):
    """Extract facts from the actual rendered User turns, not generation metadata."""
    users=[m['text'] for m in messages if m['role']=='user']; first,last=users[0],users[-1]
    if family=='name': return re.search(r'名前は(.+?)です',first)[1]+'さんです。'
    if family=='preference':return re.search(r'好きな飲み物は(.+?)です',first)[1]+'です。'
    if family=='correction':return re.search(r'集合時刻は(.+?)です',users[-2])[1]+'です。'
    if family=='quantity':
        values=dict((color,int(n)) for color,n in re.findall(r'(青|赤)い箱には(\d+)個',first))
        color=re.search(r'(青|赤)い箱',last)[1];return str(values[color])+'個です。'
    if family=='owner':
        values={item:name for name,item in re.findall(r'([^、。]+?)さんが(鍵|地図)を持っています',first)}
        item='地図' if '地図' in last else '鍵';return values[item]+'さんです。'
    if family=='literal':return re.search(r'「(.+?)」',last)[1]
    if family=='arithmetic':
        a,b=map(int,re.search(r'(\d+)個.*?(\d+)個',last).groups());return str(a+b)+'個です。'
    if family=='missing':
        assert '時刻' not in first and not re.search(r'\d+時',first)
        return '時刻はまだ聞いていません。何時ですか？'
    raise ValueError(family)


def synthetic():
    target=RUN/'curriculum_synthetic_inventory.json';assert not target.exists()
    from jmicro.tokenizer import Tokenizer
    from jmicro.data import normalized
    import pyarrow.parquet as pq
    from datasketch import MinHash,MinHashLSH
    plan=ROOT/'docs/153_answer_curriculum_comparison.md';assert plan.exists()
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    DIRECTORY.mkdir(parents=True,exist_ok=True)
    rows=[];examples=[];seen=set()
    name_questions=['私の名前は何ですか？','さっき伝えた私の名前を教えて。','私は何という名前でしたか？','私を名前で呼ぶなら、何さん？']
    preference_questions=['私の好きな飲み物は何ですか？','好きだと伝えた飲み物を覚えていますか？','私が好きなのはどの飲み物でしたか？','さっき言った私の好みを一言で教えて。']
    correction_questions=['集合時刻は何時ですか？','今の集合時刻を教えて。','訂正した後の集合時刻は？','結局、何時に集まる予定ですか？']
    quantity_questions=['{color}い箱には何個ありますか？','{color}い箱の中の数を教えて。','では、{color}い箱は何個でしたか？','{color}い箱にある物はいくつ？']
    owner_questions=['{item}を持っているのは誰ですか？','誰が{item}を持っていますか？','さっきの話で、{item}の持ち主は？','{item}を持つ人の名前を教えて。']
    literal_questions=['「{word}」だけを返してください。','返事は「{word}」の一語にしてください。','説明せず「{word}」と書いて。','指定した語だけ答えてください。「{word}」']
    arithmetic_questions=['{a}個の玉に{b}個を足すと、全部で何個ですか？','箱に{a}個あります。あと{b}個入れると合計は？','{a}個と{b}個を合わせると何個？','最初は{a}個で、さらに{b}個もらいました。今は合計何個？']
    missing_questions=['約束の時刻は何時でしたか？','待ち合わせの時刻を教えて。','予約の時刻は何時ですか？','会う時刻を確認したいです。何時？']
    def message(role,text):return dict(role=role,text=text)
    for family in ('name','preference','correction','quantity','owner','literal','arithmetic','missing'):
        for i in range(256):
            v=i%4;a=NAMES[i%32];b=NAMES[(i%32+1+i//32)%32]
            if family=='name':
                first=f'名前は{a}です。'+('今日は晴れています。' if (i//32)%2 else 'よろしくお願いします。')
                q=name_questions[i//64];text=[first,'よろしくお願いします。',q]
                answer=a+'さんです。'
            elif family=='preference':
                drink=DRINKS[i//16];first=f'私は{NAMES[i%16]}です。好きな飲み物は{drink}です。'
                text=[first,'覚えておきます。',preference_questions[v]];answer=drink+'です。'
            elif family=='correction':
                old=TIMES[i%16];new=TIMES[(i%16+1+i//16)%16]
                # Diagonal replaces the old==new case with a distinct earlier mention.
                if old==new:new=TIMES[(i%16+2)%16]
                first=f'集合時刻は{old}です。場所は{NAMES[i//16]}公園です。'
                text=[first,'わかりました。',f'訂正します。集合時刻は{new}です。','変更を確認しました。',correction_questions[v]]
                answer=new+'です。'
            elif family=='quantity':
                x,y=i%16+1,i//16+1;color='青' if v<2 else '赤'
                text=[f'青い箱には{x}個、赤い箱には{y}個あります。','わかりました。',quantity_questions[v].format(color=color)]
                answer=str(x if color=='青' else y)+'個です。'
            elif family=='owner':
                item='鍵' if v<2 else '地図'
                text=[f'{a}さんが鍵を持っています。{b}さんが地図を持っています。','二人の持ち物を確認しました。',owner_questions[v].format(item=item)]
                answer=(a if item=='鍵' else b)+'さんです。'
            elif family=='literal':
                word=WORDS[i%32];q=literal_questions[i//64].format(word=word)
                text=[('一語でお願いします。' if (i//32)%2 else '短くお願いします。')+q];answer=word
            elif family=='arithmetic':
                x,y=i%16,i//16;text=[arithmetic_questions[v].format(a=x,b=y)];answer=str(x+y)+'個です。'
            else:
                first=f'{a}公園で会います。'+('持ち物は本です。' if i//32%2 else '服装は自由です。')
                text=[first,'わかりました。',missing_questions[i//64]];answer='時刻はまだ聞いていません。何時ですか？'
            messages=[message('user' if j%2==0 else 'assistant',t) for j,t in enumerate(text)]+[message('assistant',answer)]
            assert oracle(family,messages)==answer
            key=digest(normalized(json.dumps(messages,ensure_ascii=False)))
            assert key not in seen,(family,i);seen.add(key)
            uid=f'answer_authored_train:{family}:{i:03}'
            windows=list(tok.sft_windows(messages,context=1025));selected=windows[-1]
            n=selected['target_tokens'];assert 2<=n<=32 and selected['removed_turns']==0
            assert all(w['removed_turns']==0 for w in windows)
            assert tok.chat_prompt([dict(role=m['role'],content=m['text']) for m in messages[:-1]],992)[1]==0
            row=dict(doc_id=uid,split='train',source='Authored_grounded_TRAIN',family=family,variant=i//64 if family in ('name','literal','missing') else v,
                messages=messages,target_message_indices=[len(messages)-1],target_teachers=n,
                semantic_original_id=uid,normalized_pair_sha256=digest(normalized('\n'.join(text+[answer]))))
            rows.append(row)
        # Every phrasing variant, not merely one row from the family.
        group=rows[-256:]
        for variant in range(4):examples.append(next(r for r in group if r['variant']==variant))
    metadata=pq.read_table(ROOT/'data/phase1/processed/dataset_manifest.parquet',columns=['doc_id','split','dedup_sha256','minhash']).to_pylist()
    scheme=read_json(ROOT/'reports/phase7/chat-natural-sft-20261017/availability.json')['signature_scheme']['scheme']
    held=[r for r in metadata if r['split'] in ('dev','test')];hashes={r['dedup_sha256'] for r in held}
    lsh=MinHashLSH(num_perm=128,params=(32,4));signatures={}
    for r in held:
        if r['minhash']:
            mh=MinHash(num_perm=128,seed=42,scheme=scheme,hashvalues=r['minhash']);signatures[r['doc_id']]=mh;lsh.insert(r['doc_id'],mh)
    for row in rows:
        text=normalized('\n'.join(m['text'] for m in row['messages']))
        assert row['normalized_pair_sha256'] not in hashes
        mh=MinHash(num_perm=128,seed=42,scheme=scheme)
        mh.update_batch(sorted({text[j:j+5].encode() for j in range(max(1,len(text)-4))}))
        assert not any(mh.jaccard(signatures[k])>=.75 for k in lsh.query(mh))
    records=DIRECTORY/'authored_TRAIN.jsonl';assert not records.exists()
    records.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    save(DIRECTORY/'authored_QA_variants.json',examples)
    save(target,dict(status='all_oracles_passed_pending32_variant_content_review',created_at=now(),prospective_plan=ref(plan),
        records=ref(records),variant_sample=ref(DIRECTORY/'authored_QA_variants.json'),families=dict(Counter(r['family'] for r in rows)),
        unique_targets=len(rows),teachers=sum(r['target_teachers'] for r in rows),variants_review_required=32,
        checks=dict(all_rendered_fact_oracles=True,complete_targets=True,all_histories_fit=True,unique_dialogues=True,
            old_protected_metadata_exact_near_checked=True,old_metadata_body_read=False),
        LSH_recall_not_exhaustive=True,synthetic_and_finite_templates=True,source_sha256=ref(Path(__file__)),
        new_DEV_not_yet_authored=True,new_TEST_created=False,new_training_updates=0))
    print(dict(targets=len(rows),teachers=sum(r['target_teachers'] for r in rows)),flush=True)


if __name__=='__main__':synthetic()
