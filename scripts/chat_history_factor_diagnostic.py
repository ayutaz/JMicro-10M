"""Fixed paired history/field-count diagnosis, using existing CPU chat APIs."""
import argparse
import json
import time
from urllib.request import Request, urlopen
from pathlib import Path
from chat_quality_100 import ROOT, sha, save, read, now

RUN = ROOT / 'reports/phase7/chat-recovery-20261018/history'
MODELS = {
    'C0': ('http://127.0.0.1:7865', '55280bf3d14361db1687d0e2471c82f96c6407e4f608c8e6508a2d73effa3a1f'),
    'C1': ('http://127.0.0.1:7864', 'b5cb947c2d580e8ec4a080cfa71571a5e59baa2d24272c4229634799c913bc61'),
}


def info(arm):
    with urlopen(MODELS[arm][0] + '/api/model', timeout=5) as response:
        v = json.load(response)
    assert v['checkpoint_sha256'] == MODELS[arm][1]
    assert (v['device'], v['decoding'], v['max_new_tokens'], v['parameters']) == ('CPU', 'greedy', 32, 10001152)
    return v


def reply(arm, history, deadline):
    assert time.monotonic() < deadline
    payload = dict(messages=history, max_new_tokens=32)
    request = Request(MODELS[arm][0] + '/api/chat', data=json.dumps(payload, ensure_ascii=False).encode(), headers={'Content-Type': 'application/json'})
    with urlopen(request, timeout=min(60, deadline-time.monotonic())) as response:
        answer = json.load(response)
    r = answer['response']
    assert r['max_new_tokens'] == 32 and r['generated_tokens'] <= 32 and r['removed_turns'] == 0
    return dict(request=payload, answer=answer)


def prepare():
    assert not RUN.exists()
    memories = [
        ('弁当の主菜','焼き魚','弁当の果物','桃'),
        ('包みの色','紫','包みの中身','手帳'),
        ('旅行先','奈良','移動方法','電車'),
        ('花瓶の花','ゆり','花瓶の置き場所','窓辺'),
        ('店の名前','こもれび','店の定休日','水曜'),
        ('貸した品物','辞書','貸した相手','叔父'),
        ('散歩の行き先','川沿い','散歩の時刻','四時'),
        ('財布の色','茶色','財布の場所','上着の中'),
        ('手作りの品物','しおり','使った素材','和紙'),
        ('発表の題材','星座','発表する場所','教室'),
    ]
    corrections = [
        ('集合の曜日','火曜','日曜','集合場所','時計台'),
        ('注文する料理','うどん','そば','注文する飲み物','お茶'),
        ('小包の宛先','父','妹','小包の中身','タオル'),
        ('参加する人数','四人','六人','会合の場所','会館'),
        ('手帳の色','赤','紺','手帳の置き場所','机'),
        ('借りる道具','定規','コンパス','返す相手','先生'),
        ('開店時刻','九時','十時','開店する曜日','土曜'),
        ('贈る花','ばら','すみれ','花を贈る相手','祖父'),
        ('バスの行き先','港','病院','バスを待つ場所','西口'),
        ('使う封筒の枚数','三枚','五枚','封筒の色','黄緑'),
    ]
    families = []
    for kind, tuples in [('memory', memories), ('correction', corrections)]:
        for i, row in enumerate(tuples):
            if kind == 'memory':
                field, value, other, other_value = row
                first = f'{field}は「{value}」、{other}は「{other_value}」です。'
                second = 'この二つの情報を覚えておいてください。'
                old = None
            else:
                field, old, value, other, other_value = row
                first = f'{field}は「{old}」、{other}は「{other_value}」です。'
                second = f'{field}だけ「{value}」に訂正します。{other}は変更しません。'
            # Counterbalance mention order without changing facts or answer fields.
            if i % 2:
                first = f'{other}は「{other_value}」、{field}は「{old if old is not None else value}」です。'
            single = field if i % 2 == 0 else other
            answer = value if single == field else other_value
            wrong = old if single == field and old is not None else (other_value if single == field else value)
            users = [first, second, '今日は机を拭きました。', '午後は本を読みます。', 'これは近況です。最初に伝えた情報はもう変更しません。']
            gold = [f'{first[:-1]}ね。', f'{field}は{value}、{other}は{other_value}ですね。',
                    '机の掃除をしたのですね。', '午後は読書の予定ですね。', '近況を伺いました。先ほどの情報はそのままですね。']
            families.append(dict(id=f'{kind}-{i+1:02}',kind=kind,fields=[field,other],values=[value,other_value],old=old,
                mention_order='other_first' if i%2 else 'field_first',users=users,gold=gold,
                questions={'one': f'今の{single}を教えてください。', 'two': f'今の{field}と{other}を両方教えてください。'},
                correct={'one': answer+'です。','two': f'{value}、{other_value}です。'},
                wrong={'one': wrong+'です。','two': f'{other_value}、{old if old is not None else value}です。'},
                expected={'one':f'{single}={answer}へ直接回答する。', 'two':f'{field}={value}、{other}={other_value}の両方。対応を逆転しない。'}))
    assert len(families)==20
    save(RUN/'families.json',dict(created_at=now(),families=families,source_sha256=sha(__file__)))
    save(RUN/'protocol.json',dict(created_at=now(),source_sha256=sha(__file__),families_sha256=sha(RUN/'families.json'),
        models={a:info(a) for a in MODELS},max_new_tokens=32,CPU_wall_limit=7200,request_timeout=60,
        prefix_count=100,final_input_count=160,final_response_count=320,conditional_answer_scores=640,
        factors=['query_user_turn_3_or_6','one_or_two_requested_fields','gold_or_frozen_actual_C1_history'],
        all_prefix_users_and_values_fixed_before_generation=True,
        review='Every actual reply read with literal reasons, Codex nonblind; no keyword semantic grading',
        statistics='paired family bootstrap 2000 draws seed42; fixed exploratory diagnosis, not adoption',
        limitation='history replacement changes answer cues and length too; report tokens, do not identify exposure bias uniquely',
        no_training=True,no_sealed_TEST=True))


def check():
    p=read(RUN/'protocol.json')
    assert p['source_sha256']==sha(__file__) and p['families_sha256']==sha(RUN/'families.json')
    return p


def prefix():
    p=check();target=RUN/'prefix.json';assert not target.exists()
    deadline=time.monotonic()+1800
    report=dict(status='running',created_at=now(),protocol_sha256=sha(RUN/'protocol.json'),rows=[],histories={})
    save(target,report)
    try:
        for f in read(RUN/'families.json')['families']:
            history=[];saved={}
            for i,user in enumerate(f['users']):
                history.append(dict(role='user',content=user))
                r=reply('C1',[dict(m) for m in history],deadline)
                report['rows'].append(dict(id=f['id'],turn=i+1,**r))
                history.append(dict(role='assistant',content=r['answer']['response']['text']))
                if i in (1,4):saved[str(i+1)]=[dict(m) for m in history]
                save(target,report)
            report['histories'][f['id']]=saved;save(target,report)
        assert len(report['rows'])==100
        report.update(status='complete',model_after=info('C1'))
    except BaseException as error:
        report.update(status='failed_partial_preserved',error=repr(error));raise
    finally:save(target,report)


def freeze_inputs():
    check();prefixes=read(RUN/'prefix.json');assert prefixes['status']=='complete'
    assert not (RUN/'inputs.json').exists()
    rows=[]
    for f in read(RUN/'families.json')['families']:
        for past in (2,5):
            for count in ('one','two'):
                for quality in ('gold','actual'):
                    if quality=='actual':history=prefixes['histories'][f['id']][str(past)]
                    else:history=[dict(role=role,content=text) for pair in zip(f['users'][:past],f['gold'][:past]) for role,text in zip(('user','assistant'),pair)]
                    messages=[dict(m) for m in history]+[dict(role='user',content=f['questions'][count])]
                    rows.append(dict(id=f"{f['id']}-{past+1}-{count}-{quality}",family=f['id'],kind=f['kind'],query_turn=past+1,
                        field_count=count,history_quality=quality,messages=messages,expected=f['expected'][count],
                        correct=f['correct'][count],wrong=f['wrong'][count]))
    assert len(rows)==160 and len({r['id'] for r in rows})==160
    save(RUN/'inputs.json',dict(created_at=now(),protocol_sha256=sha(RUN/'protocol.json'),prefix_sha256=sha(RUN/'prefix.json'),rows=rows))


def finals():
    check();target=RUN/'raw.json';assert not target.exists()
    inputs=read(RUN/'inputs.json');deadline=time.monotonic()+5400
    report=dict(status='running',created_at=now(),inputs_sha256=sha(RUN/'inputs.json'),rows=[],models_before={a:info(a) for a in MODELS})
    save(target,report)
    try:
        for arm in MODELS:
            for r in inputs['rows']:
                answer=reply(arm,r['messages'],deadline)
                report['rows'].append(dict(arm=arm,input_id=r['id'],family=r['family'],expected=r['expected'],**answer))
                save(target,report)
        assert len(report['rows'])==320
        report.update(status='complete_pending_all_literal_review',models_after={a:info(a) for a in MODELS})
    except BaseException as error:
        report.update(status='failed_partial_preserved',error=repr(error));raise
    finally:save(target,report)


def packet(part,start,count):
    filename='prefix.json' if part=='prefix' else 'raw.json'
    rows=read(RUN/filename)['rows']
    for i,r in enumerate(rows[start:start+count],start):
        print(json.dumps(dict(i=i,arm=r.get('arm','C1'),id=r.get('input_id',r.get('id')),turn=r.get('turn'),
            expected=r.get('expected'),messages=r['request']['messages'],reply=r['answer']['response']['text']),ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','prefix','freeze','run','packet']);p.add_argument('--part',choices=['prefix','final'],default='final');p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=20)
    a=p.parse_args()
    if a.mode=='prepare':prepare()
    elif a.mode=='prefix':prefix()
    elif a.mode=='freeze':freeze_inputs()
    elif a.mode=='run':finals()
    else:packet(a.part,a.start,a.count)
