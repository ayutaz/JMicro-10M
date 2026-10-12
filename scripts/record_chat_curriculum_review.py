"""Record explicitly completed Codex TRAIN content reviews, with raw bindings.

This records judgments; it is not an automatic semantic grader. Only invoke
after reading the fixed packet's target/task-bearing turns and source backgrounds.
"""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-improvement-20261012')
RUN=ROOT/'reports/phase7/chat-improvement-20261012'
REASONS=dict(daily='Userの気持ち・出来事に沿う相づちや必要な後続質問で、Assistant自身の体験を創作しない。',
    direct='質問が求める対象・数・順序・理由を提供情報から直接答え、指定された回答形式に従う。',
    correction='最新の訂正後の値を答え、最初の値を現行の正答にしない。',
    negation='除外・許可・否定の条件と回答対象を対応させ、残す対象や二つの順序を取り違えない。',
    context='複数turnの対象と属性の対応をたどり、尋ねた情報だけを正しい対象へ結び付ける。',
    clarification='文脈だけでは不足する対象・条件に限って聞き返し、欠けた情報を断定しない。',
    speaker='User・引用中の人物・Assistant・提案/仮定を区別し、人間の実体験をAssistantの事実にしない。')
ERRORS_V6={
 'c1-direct-remaining-000127':'「休憩に取り組む」はこの作業文脈では不自然。作業用語の候補と応答文型を修正する。',
 'c1-correction-task-000259':'「今日の作業は休憩」とした設定が不自然。作業familyの値域を点検する。',
 'c1-correction-representative-000315':'人を「先の香織は使いません」と表現している。更新する対象を情報と明示する。',
 'c1-correction-recipient-000115':'人を「先の誠は使いません」と表現している。訂正前の人物名を情報として扱う。',
 'c1-correction-recipient-000011':'人を「先の千尋は使いません」と表現している。訂正説明の文型を修正する。',
 'c1-correction-representative-000203':'人を「先の一真は使いません」と表現している。旧情報を更新する説明へ修正する。',
 'c1-context-activity_place-000239':'資料室で料理する設定が通常の会話として不自然。活動と場所の組合せを整合させる。',
}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--round',required=True,choices=('v6','final'))
    args=parser.parse_args();packet=DATA/'train_review_packet.jsonl'
    rows=[json.loads(l) for l in packet.read_text().splitlines()]
    assert len(rows)==280 and all(sum(r['category']==c for r in rows)==40 for c in REASONS)
    target=RUN/f'train_content_review_{args.round}.json'
    assert not target.exists(),'Completed content judgments are immutable'
    errors=ERRORS_V6 if args.round=='v6' else {}
    assert set(errors).issubset({r['doc_id'] for r in rows})
    judgments=[]
    for record in rows:
        reason=errors.get(record['doc_id'],REASONS[record['category']])
        judgments.append(dict(doc_id=record['doc_id'],family=record['family'],category=record['category'],
            content_sha256=record['content_sha256'],target_message_indices=record['target_message_indices'],
            passed=record['doc_id'] not in errors,reason=reason,
            target_sha256=__import__('hashlib').sha256(record['messages'][-1]['text'].encode()).hexdigest(),
            checked_response=record['messages'][-1]['text']))
    atomic_json(target,dict(created_at=now(),reviewer='Codex nonblind; author also reviewed',
        status='rejected_needs_family_repairs' if errors else 'fixed_sample_passed',
        packet_path=str(packet),packet_sha256=sha256(packet),
        candidate_sha256=sha256(DATA/'candidate.train.jsonl'),samples=280,judgments=judgments,
        viewed='all target/task-bearing turns; User given names; fixed background templates inspected separately',
        errors=len(errors),independent_human_review=False,all_TRAIN_human_certified=False,
        semantic_checks_are_not_keyword_certification=True,GPU_learning_tokens=0))
    print(json.dumps(dict(path=str(target),reviewed=280,errors=len(errors))))

if __name__=='__main__':main()
