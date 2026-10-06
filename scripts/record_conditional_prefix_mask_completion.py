"""Persist improved generation, failed historical retention and next finite assay."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
import tarfile
import time
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity
import run_conditional_prefix_mask as study


def main():
    started=time.monotonic();c=study.inspect(study.CONFIG);r=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json')
    review=read_json(study.RUN/'review.json');destination=ROOT/'reports/phase6/conditional_prefix_mask_completion.json'
    if destination.exists():raise ValueError('Preserve original fixed mask completion')
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json')
            or review['eligible_for_final_Base_validation'] or not review['all80_individually_read']
            or not review['relative_to_original_strong_staged']['passed']
            or review['absolute_and_historical_guards']['BPB_degradation_at_most1percent']):
        raise ValueError('Actually terminated all80 improved generation but failed historical retention required')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode('utf-8')
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:processes.append(identity(int(path.parent.name)))
    if len(processes)!=1 or not alive(processes[0]) or ui['busy'] or ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Actual original idle UI must be restored')
    proposal=dict(status='defined_not_implemented_not_launched',created_at=now(),trigger=study.reference(study.RUN/'review.json'),
        question='Did historical Web-body loss already deteriorate in the shared75M Web/5M story/ordinary prefix, before any conditional teacher?',
        reason='Prefix masking passes all relative generation guards but still exceeds historical WebBPB. '
            'A sole conditional-prefix explanation is therefore insufficient. The already selected shared CP has not had a Web dev score.',
        sole_new_checkpoint=c['parent'],selection_policy='Reuse CP323185 selected only from original source counters before the first conditional update323190. '
            'No checkpoint/endpoint/quality selection or new training.',
        cached_comparators=dict(original_historical_Web=read_json(Path(c['original_config']['path']))['reference']['web_screen'],
            strong_staged=c['references']['control_result'],masked_suffix=study.reference(study.RUN/'compare-result.json')),
        common_evaluation='Same original256 dev documents/full body122343 tokens/472055 bytes, same nativeBF16/math body likelihood. '
            'Compare cached per-document body NLL and paired byte-weighted BPB. BOS/EOS are excluded from body BPB. '
            'Keep counts/IDs/common denominators and historical guard fixed.',
        interpretation='Shared checkpoint still has159637 ordinary teachers left before conditional. The final-minus-shared difference contains '
            'that ordinary remainder and conditional learning, not a pure conditional effect. One common dev split/one learned seed cannot prove sole causality.',
        implementation_prerequisite='Implement owned read-only runner/binding/tests/process evidence before CUDA. Verify finite unchanged weights/no gradients/eval mode/RNG restoration.',
        CPU_preparation_ceiling_seconds=10,total_new_GPU_ceiling_seconds=30,optimizer_updates=0,new_teacher_tokens=0,new_source=0,
        completion='One finite sharedCP Web score, full common256 paired before/after decomposition, actual terminal process/UI/raw SHA/decision/commit. '
            'Use only for localization, not model/checkpoint adoption or relaxed Base quality.',
        failure='End the one fixed assay on mismatch or exhausted budget; no checkpoint list, coefficient/source/decoder rescue or repeated old GPU scores.',
        next_action='Implement the one fixed shared-prefix Web-body loss assay; define a distinct Base intervention only from its actual evidence.',
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    # Preserve the actual preconditional source counters already bound in the ledger.
    proposal.update(shared_update=323185,remaining_ordinary_reference_teachers=159637,conditional_teachers_at_shared=0,
        actual_prefix_reference_teachers=dict(web=75000000,story=5000000,ordinary_textbook=9840363,conditional_textbook=0),
        original_reference_input_ledger=c['references']['reference_input_ledger'])
    next_path=ROOT/'reports/phase6/shared_prefix_web_loss_proposal.json'
    if next_path.exists():raise ValueError('Preserve original single boundary assay proposal')
    atomic_json(next_path,proposal)
    total=c['verification_GPU_seconds']+r['GPU_seconds'];summary=review['summaries'][study.ARM]
    report=dict(status='all80_complete_relative_generation_improved_historical_Web_retention_failed_unadopted',created_at=now(),
        config=study.reference(study.CONFIG),result=study.reference(study.RUN/'compare-result.json'),review=study.reference(study.RUN/'review.json'),
        actual_terminal_job=job,actual_scientific_process_absent=True,scientific_optimizer_updates=318,
        scientific_actual_hard_teacher_tokens=r['scientific_teacher_tokens'],reference_suffix_teacher_tokens=c['reference_suffix_teacher_tokens'],
        physical_input_tokens=r['checkpoint']['additional_input_tokens'],actual_source_accounting=r['checkpoint']['actual_source_accounting'],
        probe_optimizer_updates=48,probe_teacher_tokens=read_json(study.RUN/'probe/result.json')['verification_teacher_tokens'],
        science_GPU_seconds=r['GPU_seconds'],probe_GPU_seconds=c['verification_GPU_seconds'],total_new_GPU_seconds=total,GPU_ceiling_seconds=600,
        previous_related_GPU_seconds_preserved=2858.8479238640863,related_GPU_seconds=2858.8479238640863+total,
        original_control100M_and_shared_prefix_are_reused_not_new_exposure=True,matched_input_suffix=True,matched_teacher_budget=False,
        all80_individually_read=True,independent_human_blind=False,exact_old_scores_reused=len(read_json(study.RUN/'content-notes.json')['exact_old_score_reuse']),
        summaries=review['summaries'],generation_relative_guards=review['relative_to_original_strong_staged'],
        historical_retention_guards=review['absolute_and_historical_guards'],original_UI=dict(identity=processes[0],HTTP=ui,actual_alive_verified=True),
        next_proposal=study.reference(next_path),next_action=proposal['next_action'],
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    report['CPU_completion_seconds']=time.monotonic()-started
    if report['CPU_completion_seconds']>30:raise TimeoutError('Completion30s exhausted')
    atomic_json(destination,report)
    atomic_json(ROOT/'reports/phase6/conditional_prefix_mask_active_job.json',dict(status='complete_actual_process_absent',actual_alive=False,
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},terminal_job=job,observed_at=now(),science_GPU_seconds=r['GPU_seconds'],Base_complete=False))
    files=[destination,next_path,study.CONFIG,study.PROBE_CONFIG,study.PROPOSAL,study.LEDGER,
        ROOT/'reports/phase6/conditional_prefix_mask_active_job.json',ROOT/'reports/phase6/conditional_prefix_mask_review.json',
        ROOT/'reports/phase6/conditional_prefix_mask_tests.xml',ROOT/'reports/phase6/conditional_prefix_mask_tests_initial_failure.xml',
        ROOT/'reports/phase6/conditional_prefix_mask_review_tests.xml',
        ROOT/'scripts/review_conditional_prefix_mask.py',ROOT/'tests/test_conditional_prefix_mask_review.py',Path(__file__),
        ROOT/'scripts/record_conditional_prefix_mask_content.py',ROOT/'scripts/record_conditional_prefix_mask_preparation.py',*[ROOT/p for p in study.SOURCES],
        ROOT/'reports/phase6/conditional_prefix_mask_preparation.json',ROOT/'reports/phase6/conditional_prefix_mask_preparation_portable.json']
    files.extend(p for p in sorted(study.RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl') and 'source' not in p.relative_to(study.RUN).parts)
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/conditional_prefix_mask_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve original raw evidence archive')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/conditional_prefix_mask_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    prefix=f'''conditional prefix maskの同入力suffix学習/全評価/80個別読解を完了。生成は改善、Web保持で不採用（2026-10-06 JST）。ownCUDA準備は5ac0fb0へ保存したprogress。Baseのみ実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・不在。CP323185→323503の科学318更新/同input10420224、reference教師10159637に対し実masked hard教師1801392、削除prefix8358245。他3source/全source順序/元target digest/全終端samplerが元対照と一致。既先行learning/old100M controlは新教師に加えず同教師比較とはしない。実LR.00001/model/Adam/scheduler/RNGを継承、conditionalのみ既outcome+EOS教師、penalty/KL/rank/newsourceなし。probe48更新/{report['probe_teacher_tokens']}教師別、実scienceGPU{r['GPU_seconds']:.6f}+probe{c['verification_GPU_seconds']:.6f}=新全{total:.6f}秒/上限600。CPUreview1test/1.77秒でreference教師をactualへ混同/欠損更新/改変reference digestを拒否。

同256 full body122343token/common472055byte・日本語192/331/1119・greedy80・bridge-ret各128を完了。BPB{summary['BPB']:.9f}、文法72/関連53/一貫性35/適切54/EOS79/反復1/Unicode-role-empty0（各80）。意味61.458%/JBLiMP75.831%/JCQA29.133%。元strongは一貫性23/適切26/EOS76/反復2/BPB1.133613。paired一貫性+12/CI[.025,.275]、全strong相対gateは通る。歴史WebBPB<=.981285952は未達で採用なし。maskは教師数/EOS率も変えるので量のみや単独原因の証明ではない。全80 rawSHA/具体理由、同raw6例は旧スコア継承。幻想/新人物/暗黙設備/自然な別行動/gold不一致は自動失敗にせず、数値誤りと構文は別。非blind Codex・独立人手なし。

全raw/会計/80notes/review/probe/旧CPU失敗/code/testsをconditional_prefix_mask_completion/portable.json/archiveへ保存、tensorはnative。元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}をactual ps/HTTP親410f975d…/10000007168/busy=falseで確認。旧Phase0–3/数値7失敗・全不採用と関連費用を保持、当series累積{report['related_GPU_seconds']:.6f}秒（全project費用ではない）。今回mask比較は終了、mask位置/weight/source/checkpoint/ratio/decoder sweepで救済しない。Base採用/独立学習seed/full dev/protected testはまだ未達。

次はshared_prefix_web_loss_proposal.jsonの固定CP323185一つだけのread-only Web body診断。元Web75M/story5M/ordinary prefix後・conditional教師0のCPは未Web評価で、既cached historical/strong/maskedの全256同ID/bytesと比較し劣化が既prefix側にあるかを局所化する。普通文教師159637もsuffixに残るためconditionalだけの因果としない。CPU準備10秒/GPU全30秒/教師・optimizer0、owned runner/tests/有限値/weights不変/no gradients/RNG隔離を先に用意。checkpoint選別/adoption/基準緩和や旧GPU再評価なし。未実装/未起動、証拠に基づく別Base介入だけを定義する。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_masked_suffix_generation_improved_historical_Web_retention_failed',updated_at=now(),
        conditional_prefix_mask_completion=study.reference(destination),next_action=report['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=total,coherent=35,EOS=79,repetition=1,portable_files=len(files))))


if __name__=='__main__':main()
