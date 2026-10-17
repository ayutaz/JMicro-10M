"""Prepare paired same-answer TRAIN; preserve all old files and target streams."""
import argparse
from collections import Counter
import copy
import gc
import hashlib
import json
import re
import time
from pathlib import Path
from answer_learning_common import ROOT,save,ref,bound,read_json,now
from jmicro.tokenizer import Tokenizer
from jmicro.teacher_chat_training import TeacherBudgetSampler,teacher_lr

RUN=ROOT/'reports/phase7/chat-recovery-20261018'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-recovery-20261018')
OLD=ROOT/'reports/phase7/chat-answer-learning-20261017'
CONFIG=ROOT/'configs/phase7/answer-curriculum-resource-v2-20261017.json'
PLAN=ROOT/'docs/160_chat_input_structure_sft_comparison.md'


def oracle(family,messages):
    users=[m['text'] for m in messages if m['role']=='user'];all_users='\n'.join(users);question=users[-1]
    if family=='name':return re.search(r'名前は([^。]+)です',all_users)[1]+'さんです。'
    if family=='preference':return re.search(r'好きな飲み物は([^。]+)です',all_users)[1]+'です。'
    if family=='correction':return re.findall(r'集合時刻は(\d+時)です',all_users)[-1]+'です。'
    if family=='quantity':
        facts={c:int(n) for c,n in re.findall(r'(青|赤)い箱には(\d+)個',all_users)}
        color=re.search(r'(青|赤)い箱',question)[1];return str(facts[color])+'個です。'
    if family=='owner':
        facts={item:name for name,item in re.findall(r'([ァ-ヴー]+)さんが(鍵|地図)を持っています',all_users)}
        item='地図' if '地図' in question else '鍵';return facts[item]+'さんです。'
    if family=='literal':return re.search(r'指定する語は「([^」]+)」です',all_users)[1]
    if family=='arithmetic':
        a,b=map(int,re.search(r'一つ目の数は(\d+)、二つ目の数は(\d+)',all_users).groups());return str(a+b)+'個です。'
    if family=='missing':
        assert not re.search(r'\d+時',all_users)
        return '時刻はまだ聞いていません。何時ですか？'
    raise ValueError(family)


def rewrite(old,index):
    row=copy.deepcopy(old);family=row['family'];messages=row['messages']
    first=messages[0]['text'];last=messages[-2]['text'];v=index%4;depth=(index//4)%4;reverse=bool((index//16)%2)
    n=(1,2,4,5)[depth]
    if family=='correction':n=(2,3,4,5)[depth]
    if family=='name':
        name=re.search(r'名前は(.+?)です',first)[1]
        fact=f'名前は{name}です。今日は家にいます。' if reverse else f'今日は家にいます。名前は{name}です。'
        q=['最初に伝えた名前を答えてください。','私を何さんと呼びますか。','自己紹介で伝えた名前は何でしたか。','ここまでの話にある私の名前を教えて。'][v]
    elif family=='preference':
        name=re.search(r'私は(.+?)です',first)[1];drink=re.search(r'好きな飲み物は(.+?)です',first)[1]
        facts=[f'私は{name}です。',f'好きな飲み物は{drink}です。'];fact=''.join(reversed(facts) if reverse else facts)
        q=['好みとして伝えた飲み物を答えて。','私が好きなのは何という飲み物でしたか。','飲み物について私の好みを一つ答えてください。','会話の最初に言った好きな飲み物は何？'][v]
    elif family=='correction':
        old_time,new_time=re.findall(r'集合時刻は(\d+時)です','\n'.join(m['text'] for m in messages))[:2]
        place=re.search(r'場所は([^。]+)',first)[1];facts=[f'集合時刻は{old_time}です。',f'場所は{place}です。']
        fact=''.join(reversed(facts) if reverse else facts)
        correction=f'先ほどの時刻を訂正します。集合時刻は{new_time}です。場所は変えません。'
        q=['最後の訂正を反映した集合時刻を答えて。','変更後は何時に集まりますか。','古い時刻ではなく今の集合時刻を教えてください。','結局の集合時刻は何時でしたか。'][v]
    elif family=='quantity':
        facts={c:int(num) for c,num in re.findall(r'(青|赤)い箱には(\d+)個',first)}
        colors=['赤','青'] if reverse else ['青','赤'];fact=''.join(f'{c}い箱には{facts[c]}個あります。' for c in colors)
        color=re.search(r'(青|赤)い箱',last)[1]
        q=[f'最初に説明した{color}い箱の個数を教えて。',f'{color}い箱にあるのは何個でしたか。',f'もう一方と混ぜず、{color}い箱の数を答えてください。',f'ここまでの話では、{color}い箱はいくつですか。'][v]
    elif family=='owner':
        pairs=re.findall(r'([ァ-ヴー]+)さんが(鍵|地図)を持っています',first);assert len(pairs)==2
        if reverse:pairs.reverse()
        fact=''.join(f'{name}さんが{item}を持っています。' for name,item in pairs);item='地図' if '地図' in last else '鍵'
        q=[f'最初に伝えた話で、{item}を持つ人を答えて。',f'{item}の担当は何さんでしたか。',f'もう一人と混ぜず、{item}を持つ人の名前を教えて。',f'ここまでの情報から、{item}の持ち主は誰ですか。'][v]
    elif family=='literal':
        word=re.search(r'「([^」]+)」',last)[1];fact=f'次の返事に指定する語は「{word}」です。'
        q=['先ほど指定した語だけを返してください。','説明は付けず、指定した一語だけ答えて。','引用符を付けず、最初に指定した語をそのまま返して。','指定する語だけで返事をしてください。'][v]
    elif family=='arithmetic':
        a,b=map(int,re.search(r'(\d+)個.*?(\d+)個',last).groups());fact=f'足し算に使う一つ目の数は{a}、二つ目の数は{b}です。'
        q=['二つの数を足すと何個ですか。','最初に伝えた二つの数の合計を答えて。','一つ目に二つ目を足した個数はいくつ？','二つを合わせた個数を教えてください。'][v]
    else:
        assert family=='missing';fact=first
        q=['今の話だけで約束の時刻は分かりますか。','まだ伝えていない情報もあります。待ち合わせは何時でしょう。','時刻を確認したいのですが、何時か聞いていますか。','約束の時刻を教えて。分からなければ確認してください。'][v]
    neutrals=['今日は机を拭きました。','午後は本を読みます。','窓を開けて空気を入れ替えました。','いま話した近況は、先ほどの情報の変更ではありません。']
    users=[fact]+neutrals[:n-1]
    if family=='correction':users[1 if reverse else n-1]=correction
    acknowledgments=['教えてくれてありがとうございます。','わかりました。','お話を伺いました。','了解しました。']
    history=[]
    for i,user in enumerate(users):history.extend([dict(role='user',text=user),dict(role='assistant',text=acknowledgments[(i+v)%4])])
    history.extend([dict(role='user',text=q),copy.deepcopy(messages[-1])])
    row.update(messages=history,target_message_indices=[len(history)-1],original_target_message_indices=old['target_message_indices'],
        transformation_pattern=dict(question=v,depth=depth,reverse=reverse,prior_user_turns=n))
    row['normalized_pair_sha256']=hashlib.sha256('\n'.join(m['text'] for m in history).encode()).hexdigest()
    assert oracle(family,history)==old['messages'][-1]['text']
    return row


def prepare():
    assert not DATA.exists() and not (RUN/'TRAIN_proposal_receipt.json').exists()
    inventory=read_json(OLD/'curriculum_synthetic_inventory.json');path=bound(inventory['records'])
    original=[json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()];assert len(original)==2048
    DATA.mkdir(parents=True);tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');rows=[];samples={}
    for old in original:
        index=int(old['doc_id'].rsplit(':',1)[1]);row=rewrite(old,index)
        window=list(tok.sft_windows(row['messages'],1025))[-1];assert window['removed_turns']==0
        teachers=[i for i in window['labels'] if i!=-100];assert teachers==tok.encode(old['messages'][-1]['text'])+[7]
        assert 2<=len(teachers)<=32 and tok.chat_prompt(row['messages'][:-1],992)[1]==0
        assert all(w['removed_turns']==0 for w in tok.sft_windows(row['messages'],1025))
        key=(row['family'],index%4,(index//4)%4,bool((index//16)%2));samples.setdefault(str(key),row)
        rows.append(row)
    target=DATA/'authored_TRAIN.jsonl';target.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
    save(DATA/'QA_patterns.json',list(samples.values()));assert len(samples)==256
    save(RUN/'TRAIN_proposal_receipt.json',dict(created_at=now(),status='all2048_independent_oracles_passed_pending256_pattern_review',
        source=ref(__file__),plan=ref(PLAN),original_inventory=ref(OLD/'curriculum_synthetic_inventory.json'),
        original_records=inventory['records'],records=ref(target),QA_patterns=ref(DATA/'QA_patterns.json'),rows=2048,patterns=256,
        all_target_IDs_unchanged=True,no_history_trim=True,new_model_updates=0,new_GPU=0,new_DEV_not_authored=True,new_TEST=False))
    print('Prepared2048 exact-answer rows; 256 structure patterns await direct review',flush=True)


def packet(start,count):
    p=read_json(RUN/'TRAIN_proposal_receipt.json');assert p['source']==ref(__file__)
    for i,row in enumerate(read_json(bound(p['QA_patterns']))[start:start+count],start):
        print(json.dumps(dict(i=i,id=row['doc_id'],pattern=row['transformation_pattern'],messages=row['messages']),ensure_ascii=False))


def package():
    p=read_json(RUN/'TRAIN_proposal_receipt.json');assert p['source']==ref(__file__)
    review=read_json(RUN/'TRAIN_pattern_review.json');assert review['all256_reviewed'] and review['proposal']==ref(RUN/'TRAIN_proposal_receipt.json')
    c=read_json(CONFIG);source=bound(c['arms']['C1']['records']);rows={r['doc_id']:r for r in [json.loads(l) for l in bound(p['records']).read_text().splitlines()]}
    counts=Counter();paths={a:DATA/f'{a}_TRAIN.jsonl' for a in ('C0','C1')};assert not any(path.exists() for path in paths.values())
    with source.open() as inp,paths['C0'].open('x') as a,paths['C1'].open('x') as b:
        for line in inp:
            old=json.loads(line);candidate=copy.deepcopy(old)
            if old['source']=='Authored_grounded_TRAIN':
                r=rows[old['semantic_original_id']]
                for key in ('messages','target_message_indices','original_target_message_indices','transformation_pattern','normalized_pair_sha256'):candidate[key]=r[key]
                assert candidate['messages'][-1]==old['messages'][-1];counts['changed_alias_rows']+=1
            else:assert candidate==old;counts['unchanged_rows']+=1
            a.write(line);b.write(json.dumps(candidate,ensure_ascii=False)+'\n')
    assert ref(paths['C0'])['sha256']==c['arms']['C1']['records']['sha256']
    assert counts['changed_alias_rows']==2048*69
    save(RUN/'TRAIN_packaging.json',dict(created_at=now(),proposal=ref(RUN/'TRAIN_proposal_receipt.json'),review=ref(RUN/'TRAIN_pattern_review.json'),
        old_config=ref(CONFIG),arms={k:ref(v) for k,v in paths.items()},counts=dict(counts),old_records_unchanged=True,new_DEV_not_authored=True))


def replay():
    assert not (DATA/'manifest.json').exists();pack=read_json(RUN/'TRAIN_packaging.json');summaries={};streams=[]
    for arm in ('C0','C1'):
        started=time.monotonic();records=bound(pack['arms'][arm]);rows=[json.loads(l) for l in records.read_text().splitlines()];lookup={r['doc_id']:r for r in rows}
        sampler=TeacherBudgetSampler(rows,Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model'),1024,42,1000000,512,32)
        tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');teacher_stream=hashlib.sha256();order_stream=hashlib.sha256();history=[];sources=Counter()
        for w in sampler.windows:
            r=lookup[w['doc_id']];selected=w['labels'][w['labels']!=-100].tolist()
            assert selected==tok.encode(r['messages'][w['target_message_index']]['text'])+[7] and w['removed_turns']==0 and 2<=len(selected)<=32
        while sampler.teacher_tokens<1000000:
            before=sampler.teacher_tokens;epoch=sampler.epoch;position=sampler.position;order=sampler.order.copy();examples=sampler.examples
            batches,n,_=sampler.next_update();used=sampler.examples-examples
            indices=list(order[position:position+used]) if epoch==sampler.epoch else list(order[position:])+list(sampler.order[:sampler.position])
            assert len(indices)==used
            for idx in indices:
                w=sampler.windows[int(idx)];r=lookup[w['doc_id']];ys=w['labels'][w['labels']!=-100]
                teacher_stream.update(ys.astype('<i8').tobytes());order_stream.update((w['doc_id']+'\n').encode());sources[r['source']]+=len(ys)
            history.append(dict(update=len(history)+1,teachers=sampler.teacher_tokens,teachers_this_update=n,microbatches=len(batches),lr=teacher_lr(before,n,1000000,1e-4)))
        summary=dict(status='passed',created_at=now(),records=ref(records),sampler_binding=sampler.binding,updates=len(history),actual_teachers=sampler.teacher_tokens,
            windows=len(sampler.windows),physical_microbatches=sum(h['microbatches'] for h in history),history=history,sampler_terminal=sampler.state_dict(),
            consumed_source_teachers=dict(sources),teacher_stream_sha256=teacher_stream.hexdigest(),ordered_doc_IDs_sha256=order_stream.hexdigest(),
            all_teacher_masks_and_complete_roundtrips=True,no_history_trim=True,CPU_seconds=time.monotonic()-started)
        save(RUN/f'TRAIN_{arm}_CPU_replay.json',summary);summaries[arm]=dict(records=ref(records),dry_run=ref(RUN/f'TRAIN_{arm}_CPU_replay.json'),sampler_binding=sampler.binding)
        streams.append({k:summary[k] for k in ('updates','actual_teachers','physical_microbatches','history','windows','consumed_source_teachers','teacher_stream_sha256','ordered_doc_IDs_sha256')})
        print(arm,summary['updates'],summary['actual_teachers'],summary['CPU_seconds'],flush=True)
        del sampler,rows,lookup;gc.collect()
    assert streams[0]==streams[1],'All targets, their order, updates, LR and source quotas must match'
    save(DATA/'manifest.json',dict(status='TRAIN_frozen_before_new_DEV',created_at=now(),plan=ref(PLAN),proposal=ref(RUN/'TRAIN_proposal_receipt.json'),
        packaging=ref(RUN/'TRAIN_packaging.json'),arms=summaries,teacher_budget=1000000,exact_paired_teacher_streams=True,new_DEV_not_authored=True,new_TEST=False))
    save(RUN/'TRAIN_manifest_ref.json',ref(DATA/'manifest.json'))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','packet','package','replay']);p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=16);a=p.parse_args()
    if a.mode=='prepare':prepare()
    elif a.mode=='packet':packet(a.start,a.count)
    elif a.mode=='package':package()
    else:replay()
