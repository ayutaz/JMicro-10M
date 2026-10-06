"""Preserve both actual endpoints/rejection without claiming Base completion."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import run_low_rank_base_comparison as study


def main():
    destination=ROOT/'reports/phase6/low_rank_base_v2_completion.json'
    if destination.exists():raise ValueError('Preserve original terminal comparison')
    c=study.inspect(study.CONFIG);r=read_json(study.RUN/'compare-result.json');review=read_json(study.RUN/'review.json')
    job=read_json(study.RUN/'job.json');ui=original_UI()
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']+c['verification_GPU_seconds']>1800 or r['config_sha256']!=sha256(study.CONFIG)
            or review['result']!=study.reference(study.RUN/'compare-result.json') or not review['all160_individually_read']
            or review['Base_complete'] or review['Base_adopted'] or review['protected_test_used']
            or review['Chat_started'] or review['quantization_started']):
        raise ValueError('Actual complete comparison/all160 and unchanged boundary required')
    if set(review['accounting'])!=set(study.ARMS) or any(review['accounting'][a]['actual_new_hard_teachers']!=91641755 for a in study.ARMS):
        raise ValueError('Actual matched both-arm teacher ledger required')
    eligible=[a for a in study.ARMS if review['gates'][a]['eligible_for_final_Base_validation']]
    if eligible!=review['eligible_recipes']:raise ValueError('Actual unchanged Base gates differ')
    previous=read_json(ROOT/'reports/phase6/document_context_ablation_completion.json')['related_GPU_seconds']
    total=r['GPU_seconds']+c['verification_GPU_seconds']
    report=dict(status=review['status'],created_at=now(),config=study.reference(study.CONFIG),
        result=study.reference(study.RUN/'compare-result.json'),review=study.reference(study.RUN/'review.json'),
        actual_terminal_job=job,actual_process_absent=True,original_UI=ui,
        scientific_teacher_tokens=183283510,teacher_tokens_per_arm=91641755,
        nominal_reference_teacher_tokens_per_arm=100000000,physical_input_tokens=201064448,
        scientific_optimizer_updates=6136,verification_teacher_tokens=c['verification_teacher_tokens'],verification_optimizer_updates=96,
        scientific_GPU_seconds=r['GPU_seconds'],probe_GPU_seconds=c['verification_GPU_seconds'],total_new_GPU_seconds=total,
        GPU_ceiling_seconds=1800,previous_related_GPU_seconds_preserved=previous,related_GPU_seconds=previous+total,
        related_series_is_not_whole_project_cost=True,summaries=review['summaries'],gates=review['gates'],
        matched_rank4_vs_full_fresh=review['matched_rank4_vs_full_fresh'],eligible_recipes=eligible,
        all160_individually_read=True,independent_human_blind=False,
        raw_probe_field_clarification=review['raw_probe_field_clarification'],
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Qualified recipe only: independent learned recipe seed/full dev/protected test/adoption; otherwise end rank4/reset comparison and identify a distinct evidence-backed Base mechanism. No salvage sweep.')
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROBE_CONFIG,study.PROPOSAL,ROOT/'reports/phase6/low_rank_base_tests.xml',Path(__file__),
        ROOT/'scripts/record_low_rank_base_content.py',ROOT/'scripts/review_low_rank_base_comparison.py',
        ROOT/'reports/phase6/low_rank_base_initial_failure.json',*[ROOT/s for s in study.SOURCES]]
    files.extend(p for p in sorted(study.RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.tsv'))
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    brief=json.dumps(review['summaries'],ensure_ascii=False)
    prefix=f'''固定rank4対full fresh-AdamのBase比較を実完了（2026-10-06 JST）。Base未完了、実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・実不在。両3068更新/同91,641,755実教師、全科学183,283,510/physical201,064,448、100M reference各と区別。元10.5B親/同Webcursor/元mixed入力・条件outcome+EOS mask/source窓・教師/末尾cursor/hashを全3068で照合、両fresh Adam/actualLR.00001/scheduler clockとfloorを維持。実CUDA8対4+4と32timingの96更新/{c['verification_teacher_tokens']}検証教師は別会計。科学GPU{r['GPU_seconds']:.6f}+probe{c['verification_GPU_seconds']:.6f}=当比較{total:.6f}秒/1800。GPU予測1144.75秒は実績に置換した。元LoRA W0全不変、rank4学習232,960/一時10,234,112→native merge10,001,152、両実FP32/math native merge control成功。full controlは全10M学習可、raw merge helperの共通frozen flagはfull armに適用せず独立endpoint auditを正本とする。旧数値7失敗/旧全不採用は維持。

同dev256/122,343body tokens/472,055common bytes・日本語192/331/1119各・固定greedy80各/全160を個別に読み、raw全項目一致の旧採点だけを継承。非blind Codex、独立人間ではない。結果: {brief}。採否{review['status']}、qualified recipes{eligible}、strong23+8/coh pairedCI>0/EOS>=76/反復<=2・絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0・歴史WebBPB<=.9812859519097707を緩めていない。rank4/fresh fullのpaired差・全理由・会計/source/PID/可搬証拠を保存し、frozen weights/RNG/cursorとnative CPはWSL保持。元final10B UI{ui['identity']['pid']}/boot{ui['identity']['boot_id']}/start{ui['identity']['start_ticks']}をactual ps/HTTP親410f975d…/busy=falseで確認。

次は{report['next_action']} rank/module/scale/LR/source/mask/CP/decoder sweepなし。独立学習seed/full dev/protected test/採用は未達、Base完了と実験完了を分ける。関連series累積{report['related_GPU_seconds']:.6f}秒は全project費用ではない。Phase0–3/旧失敗/全品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=report['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['low_rank_base_completion']=study.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],new_GPU_seconds=total,portable_files=len(files),eligible_recipes=eligible),ensure_ascii=False))


if __name__=='__main__':main()
