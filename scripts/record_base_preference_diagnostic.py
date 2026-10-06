"""Bind individually read TRAIN pairs, preserve diagnostic and define one study."""
import hashlib
import json
import math
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import diagnose_base_preference as study


def main():
    c=study.inspect();job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'result.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>180
            or r['config_sha256']!=sha256(study.CONFIG) or not all(r['readonly_checks'].values())
            or r['optimizer_updates'] or r['scientific_teacher_tokens'] or r['case_count']!=64):
        raise ValueError('Actual complete absent readonly64 diagnostic required')
    study.check_reference(r['pairs']);rows=read_json(Path(r['pairs']['path']));tok=Tokenizer(Path(c['tokenizer']['path']))
    source=read_json(Path(c['references']['source_review']['path']));old=source['notes']
    observations=ROOT/'reports/phase6/base_preference_observations.tsv';notes={}
    for line in observations.read_text().splitlines():
        key,label,reason=line.split('\t')
        if key in notes or label not in ('chosen','undetermined') or not reason:raise ValueError('One individual pair judgement required')
        notes[key]=dict(label=label,rationale=reason)
    if len(rows)!=64 or set(notes)!={row['id'] for row in rows}:raise ValueError('All64 individual paired original observations required')
    for row in rows:
        raw=tok.decode_bytes([v for v in row['rejected_ids'] if v!=3])
        if (raw.hex()!=row['rejected_bytes_hex'] or raw.decode('utf-8',errors='replace')!=row['rejected_text']
                or row['split']!='train' or row['prompt_ids'][1:]+row['chosen_ids'][:-1]!=row['original_body_ids']
                or row['chosen_ids'][-1]!=3 or row['source_text_sha256']!=old[row['id']]['canonical_sha256']
                or hashlib.sha256(tok.decode_bytes(row['original_body_ids'])).hexdigest()!=row['source_text_sha256']
                or (notes[row['id']]['label']=='undetermined')!=old[row['id']]['weak']
                or notes[row['id']]['label']=='chosen' and row['repeated4gram_positions']<8):
            raise ValueError('Raw token/provenance/original weak exclusion differs: '+row['id'])
    valid=[row for row in rows if notes[row['id']]['label']=='chosen'];unique_positive=sum(len(row['chosen_ids']) for row in valid)
    if len(valid)!=56:raise ValueError('Exactly pre-existing8 weak originals remain unlabelled; no source or outcome reroll')
    report=dict(status='all64_original_and_generated_Base_pairs_individually_reviewed',created_at=now(),
        config=study.reference(study.CONFIG),result=study.reference(study.RUN/'result.json'),pairs=r['pairs'],
        observations=study.reference(observations),notes=notes,all64_individually_read=True,reviewer='Codex nonblind',independent_human_blind=False,
        usable_preference_pairs=len(valid),unlabelled_original_weak_pairs=8,positive_completion_teacher_positions_in_fixed56=unique_positive,
        preferred_pair_ids=[row['id'] for row in valid],raw_pair_sha256={row['id']:hashlib.sha256(json.dumps(row,sort_keys=True,ensure_ascii=False).encode()).hexdigest() for row in rows},
        actual_job=job,GPU_seconds=r['GPU_seconds'],geometry=r['geometry'],readonly_checks=r['readonly_checks'],original_UI=original_UI(),
        no_test_or_dev_training=True,optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        limitations='Preference is local coherence/grammar against overt repeated output, not independent human or factual truth.8 original weaknesses known before rollout are not positive labels; no reroll.64-gradient geometry includes all8 weak rows; fixed56 needs its own reference/probe. TRAIN successes are not generalization.')
    destination=ROOT/'reports/phase6/base_preference_diagnostic_review.json'
    if destination.exists():raise ValueError('Preserve original pair review')
    atomic_json(destination,report)
    proposal=dict(kind='role_free_Base_chosen_CE_vs_chosen_CE_plus_fixed_reference_DPO_v1',created_at=now(),
        diagnostic=study.reference(destination),parent=c['parent'],news_pairs=r['pairs'],preferred_pair_ids=report['preferred_pair_ids'],
        source_weak_pair_policy='Exclude precisely8 pre-rollout original-source weak rows. All56 other rows individually support original over generated loop; no new source/selector/reroll.',
        fixed_pair_count=56,fixed_positive_completion_teacher_positions=unique_positive,
        shared_Web_positive_teacher_tokens=6000000,positive_completion_teacher_tokens_per_arm=2000000,
        positive_teacher_tokens_per_arm=8000000,new_unique_scientific_positive_teacher_tokens=10000000,
        positive_completion_exposure_passes=2000000/unique_positive,
        arms=dict(chosen_CE=dict(DPO_coefficient=0.),chosen_CE_DPO=dict(DPO_coefficient=.1)),beta=.1,
        policy='Same native tied10M/Tokenizer, actual d18 Adam/scheduler/LR1e-5/RNG/Web cursor; no reheat. Shared6M Web trained once and retained at predeclared endpoint, then same original completion order/mask2M in both arms. DPO adds negative sequence reference-ratio loss only.',
        reference_policy='Freeze actual shared6M Web endpoint for both arms. Recompute56 exact full-mask reference logps once with fixed grouping/shape. Negative sequences are original d18 fixed64-token rollouts, no online reroll.',
        accounting='Positive CE body+EOS teachers separate from DPO chosen/rejected scored positions and pair exposures, prompt/padding/physical inputs;6M shared common learning counted once physically and in both arm budgets. Repetition of about4k fixed teachers is not new dataset supply.',
        next_action='Implement exact inherited common-Web/pair trainer, cache56 frozen reference scores, CPU loss/ledger/fullstate restart tests. Own actual CUDA4vs2+2 and32timing for both objectives before scientific freeze; estimates with30% margin+600eval+probe within1800 or stop.',
        own_GPU_probe_ceiling_seconds=180,total_new_study_GPU_ceiling_seconds=1800,diagnostic_GPU_seconds_separate=r['GPU_seconds'],
        selection='Unchanged strong staged coherence>=31 and positive paired CI, EOS>=76/repetition<=2; absolute grammar56/coherence27/appropriate27/EOS37/repetition<=18/errors0; historical Web BPB<=.9812859519097707. Eligible only then independent learned seed/full dev/protected test/adoption.',
        evaluation='Same dev256 common bytes/Japanese192-331-1119/greedy80 plain Base plus bridge/retention512each. Both full80 individually read; compare loss factor against own matched chosen-CE and fixed strong staged.',
        completion='Single finite2M completion comparison per arm and full quality judgement; reject failed recipe. No beta/coefficient/source/epoch/LR/decoder/parent/checkpoint rescue sweep.',
        scientific_config_frozen=False,science_started=False,Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        evidence_limits='Measured64-gradient DPO/CE norm8.693 and cosine.5584 are preliminary not a56-scale guarantee. Alpha.1 is one predeclared perturbation of the new objective, not optimized or a safety bound. DPO is not guaranteed to preserve Web BPB or fix free generation. Limited curated source/style and repeated dev remain.')
    proposal_path=ROOT/'reports/phase6/base_preference_comparison_proposal.json';atomic_json(proposal_path,proposal)
    files=[destination,proposal_path,study.CONFIG,study.RUN/'result.json',study.RUN/'job.json',observations,Path(__file__),
        *[ROOT/s for s in study.SOURCES],ROOT/'reports/phase6/base_preference_loss_tests.xml']
    files += [q for q in (study.RUN/'source').rglob('*') if q.is_file()]
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},
        file_count=len(files),archive=study.reference(archive),source_texts_pairs_and_tensors_native_only=True))
    detail=(f'元d18/native10Mの固定TRAIN64を実GPU{r["GPU_seconds"]:.6f}秒/180で生成・score・gradient診断、actual{job["pid"]}完了/不在、元UI復帰。'
        f'全64EOS0/重度4gram位置8以上64/UTF8良64、正解残文CE{r["chosen_CE_nats"]:.6f}、初期DPOloss ln2。全64勾配DPO/CE norm{r["geometry"]["DPO_to_CE_norm"]:.6f}/cosine{r["geometry"]["cosine"]:.6f}、'
        '重み/parentSHA/RNG不変・終了gradなしの5checksに合格、optimizer更新/科学教師0。全64原文と生成を個別nonblind比較し56に原文の文法/一貫性優位を確認、元source受入時から弱だった8は勝者とせず保持。'
        f'固定56のpositive completion+EOSは{unique_positive}positionsのみ。次案は同d18継承状態・LR1e-5から共通Web6M一度→chosenCE対chosenCE+DPO(beta.1/係数0対.1)各positive2M、'
        '共通を含め各8M/新実学習10M、negative/prompt/physical/反復を別会計。新loss一要因、原分岐のsource/epoch/LR/decoder/CP救済なし。'
        'まだ科学未実装/未凍結/未開始。次は56新reference cache/専用trainer/CPU会計とresume→ownCUDA各4対2+2/32timing→実測30%margin+600評価+probe全1800内のみ科学凍結。'
        '全日本語/両80/bridge-retentionと元全品質条件で採否、合格のみ独立学習seed/full dev/protected testへ。小TRAIN集合/元原文8弱/非blind/旧数値7失敗/長さ・作風差を保持しDPOや学習増量の成功を保証しない。')
    prefix='Base専用・文章全体の比較損失の実診断完了（2026-10-06 JST）。\n\n'+detail+'\n\nBase未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。WSL uv/local commitのみ/pushなし。以下は過去の履歴。\n\n'
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text(prefix+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['Base_preference_diagnostic_review']=study.reference(destination);progress['Base_preference_comparison_proposal']=study.reference(proposal_path);atomic_json(q,progress)
    print(dict(status=report['status'],usable_pairs=56,positive_positions=unique_positive,GPU_seconds=r['GPU_seconds'],portable_files=len(files)))


if __name__=='__main__':main()
