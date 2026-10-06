"""Persist Base-only actual milestones without treating preparation as completion."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import argparse
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import run_finite_Web_constraint as study


def main(phase):
    destination=ROOT/f'reports/phase6/finite_Web_constraint_{phase}.json'
    if destination.exists():raise ValueError('Preserve original milestone')
    running=phase=='launch'
    scientific=phase in ('launch','terminal')
    config=study.CONFIG if scientific else study.PROBE_CONFIG
    c=read_json(config) if running else study.inspect(config)
    report=dict(status='finite_Web_constraint_'+phase,created_at=now(),config=study.reference(config),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],GPU_seconds=0,
        scientific_source_CE_teacher_tokens=0,total_new_GPU_ceiling_seconds=2400,
        memory=c['memory_binding'],quality_criteria_unchanged=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    detail=f"CPU4testsで有限制約・拒否時rollback・全state連続対再開を確認。CPU準備{c['CPU_preparation_seconds']:.6f}秒、固定TRAIN32 Web窓/32638body教師・32768input・130336bytesを既cacheから再利用。新GPU/本学習0。次はownCUDA8対4+4・32timing・有限投影数値controlと最悪ケース速度を120秒内で測り、検証を含む2400秒内の場合だけ本学習へ進む。"
    jobdir=study.RUN if scientific else study.RUN/'probe'
    if phase!='preparation':
        job=read_json(jobdir/'job.json');live=alive(job)
        if live!=running:raise ValueError('Actual process does not match milestone')
        report.update(actual_job=job,actual_live_process=live,GPU_seconds=job['GPU_elapsed_seconds'])
        if phase in ('probe','budget_rejected'):
            r=study.probe_evidence();estimate=study.estimate_training(r)
            report.update(result=study.reference(jobdir/'result.json'),actual_probe=r,
                estimated_science_GPU_seconds_with_margin=estimate,
                estimated_total_GPU_seconds=estimate+r['GPU_seconds'],within_budget=estimate+r['GPU_seconds']<=2400)
            detail=f"実CUDA全state8対4+4/有限値/LR/元Webcursor/実制約に成功、32timingと固定旧CPの有限投影control完了。検証GPU{r['GPU_seconds']:.6f}秒/120、科学教師0。最悪ケース科学予測{estimate:.6f}秒、検証込み{estimate+r['GPU_seconds']:.6f}秒/2400。予測は品質/完成の証明ではない。上限内だけscience凍結、同staged実91,641,755CE教師＋追加Web gradient別会計/同日本語・全80/旧全gate採否へ進む。"
            if phase=='budget_rejected':
                if estimate+r['GPU_seconds']<=2400 or study.CONFIG.exists():raise ValueError('Actual rejected budget/no scientific config required')
                report.update(scientific_launched=False,science_config_created=False,
                    decision='Current exact FP32/math implementation exceeds fixed worst-case budget; no training launch.',
                    fixed_packet_and_quality_criteria_retained=True)
                detail=f"実CUDA probeは成功・actual{job['pid']}終端/実不在、検証GPU{r['GPU_seconds']:.6f}秒。本科学最悪予測{estimate:.6f}秒＋検証={estimate+r['GPU_seconds']:.6f}秒>2400、実--freezeが拒否し科学configなし/本学習0。有限投影controlの実NLL2.881102→2.604513は上限2.607075を満たすが学習品質の証明ではない。追加FP32/math保持oracleの最悪5forward+1gradient費用が支配的。上限/packet/制約/品質を変えて救済せず、元10B UI復帰・Base未完成。次は同固定TRAIN/制約を維持する単一のoracle計算高速化案について、数値誤差と実GPU速度を事前条件付きで検証する計画を定義。本科学/Chat/量子化は起動しない。"
        elif phase=='probe_failure':
            if job['status']!='failed_or_interrupted':raise ValueError('Actual terminal failure required')
            partial=read_json(jobdir/'progress-result.json') if (jobdir/'progress-result.json').exists() else {}
            report.update(partial_probe=partial,scientific_launched=False,original_UI=original_UI())
            detail=f"ownCUDA probeが実終了・実不在。GPU{job['GPU_elapsed_seconds']:.6f}秒/120、terminal reason {job.get('error')}。完了済みprobe部分/原source/raw/会計を保持、本科学未起動・Base未完成。固定packet/CP/bound/投影条件を失敗救済のため変えず、同probeの自動再試行なし。元10B UIへ復帰。次は失敗根拠からこの有限分岐の結論と別のBase改善を定義する。"
        elif running:
            report.update(scientific_source_CE_teacher_tokens=job.get('actual_teachers',0),
                teacher_count_scope='Actual accepted updates at observed heartbeat; not final total.',
                verification_GPU_seconds=c['verification_GPU_seconds'])
            detail=f"science永続起動actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}、実stage{job.get('stage')}を確認。実測probe{c['verification_GPU_seconds']:.6f}秒＋科学上限{c['GPU_budget_seconds']:.6f}秒=2400。元親から同stagedを実損失制約付きで学習し、完了更新/Adam/scheduler/RNG/sampler/全教師・追加gradient観測を保存。本科学終端・全80/品質採否は未完了。restartは実PID不在確認後 scripts/run_finite_Web_constraint.ps1 -Mode Train -Worker。"
        else:
            r=read_json(jobdir/'compare-result.json')
            if job['status']!='complete' or r['GPU_seconds']!=job['GPU_elapsed_seconds']:raise ValueError('Actual completed branch required')
            report.update(result=study.reference(jobdir/'compare-result.json'),actual_result=r,original_UI=original_UI(),
                verification_GPU_seconds=c['verification_GPU_seconds'])
            if 'finite_rejection' in r:
                rejection=r['finite_rejection']
                report['scientific_source_CE_teacher_tokens']=rejection['accepted_source_CE_teacher_tokens']
                detail=f"実有限制約の受入不能で分岐終了、actual{job['pid']}はcomplete・実不在。受入{rejection['accepted_source_updates']}更新/{rejection['accepted_source_CE_teacher_tokens']}CE教師、追加Web gradient/forward・拒否試行別会計。科学GPU{r['GPU_seconds']:.6f}＋検証{c['verification_GPU_seconds']:.6f}秒/2400。拒否更新の重み/Adam/scheduler/RNG/samplerは直前完了境界へrollbackしnativeCP保持。全3068/91,641,755完了や品質合格とはしない。元10B UI復帰、Base未完成。固定packet/bound/margin/LR等救済なし、次はこの実失敗を根拠に別機構を検討。"
            else:
                report['scientific_source_CE_teacher_tokens']=r['checkpoint']['additional_supervised_tokens']
                detail=f"全3068更新/実91,641,755CE教師のGPU分岐終了、actual{job['pid']}は実不在。科学GPU{r['GPU_seconds']:.6f}＋検証{c['verification_GPU_seconds']:.6f}秒/2400。追加Web gradient/forward教師は別会計、nativeCP/同日本語・dev256/greedy80 rawを保持。全80の個別内容と旧全gate採否は次に実施、GPU終了だけでBase完成としない。元10B UI復帰。"
    if phase not in ('launch','probe_failure','terminal'):report['original_UI']=original_UI()
    atomic_json(destination,report)
    files=[destination,config,study.PROPOSAL,ROOT/'reports/phase6/finite_Web_constraint_tests.xml',
        study.RUN/'memory.json',Path(__file__),*[ROOT/s for s in study.SOURCES]]
    if phase not in ('preparation','launch'):
        files.extend(p for p in sorted(jobdir.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml'))
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(
        files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix=f"Base専用有限Web実損失制約: {phase}（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n{detail}\n\n固定TRAIN保持はheld-out/自然品質の証明ではない。元LR.00001/Adam/全source/条件outcome+EOS maskと旧相対・絶対・歴史Webの全品質基準を保持。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n"
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,
        Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['finite_Web_constraint_'+phase]=study.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)),ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=('preparation','probe','budget_rejected','probe_failure','launch','terminal'))
    main(parser.parse_args().phase)
