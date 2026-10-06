"""Evidence and truthful block-boundary scope; no implicit Base adoption."""
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
import run_block_Web_constraint as study


def main(phase):
    destination=ROOT/f'reports/phase6/block_Web_constraint_{phase}.json'
    if destination.exists():raise ValueError('Preserve original block milestone')
    running=phase=='launch';scientific=phase in ('launch','terminal');config=study.CONFIG if scientific else study.PROBE_CONFIG
    c=read_json(config) if running else study.inspect(config)
    report=dict(status='block_Web_constraint_'+phase,created_at=now(),config=study.reference(config),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],GPU_seconds=0,scientific_source_CE_teacher_tokens=0,
        previous_related_GPU_seconds=c['previous_related_GPU_seconds'],total_related_GPU_ceiling_seconds=2400,
        constraint_scope=c['constraint_scope'],does_not_satisfy_old_per_update_contract=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
    detail=f"固定20更新の提案区切りごとに元FP32/math TRAIN body NLL<=original*1.01を確認し、旧と同じ有限projector/0.5・.25・.125の修正または全区切りrollbackを行う別研究。内部の未確定更新は上限を超える可能性があり、旧毎更新契約の成功へ置換しない。CPU4tests/2.16秒でnative全state連続対再開・全区切り拒否/途中中断rollback・末尾短区切り/改変拒否、CPU準備{c['CPU_preparation_seconds']:.6f}秒。217MB cache/固定32窓を再利用、全量scanなし。新GPU/本学習0。次はownCUDA連続2区切り対1+1/全state、4区切り80更新timingを120秒内で測り、旧3診断{c['previous_related_GPU_seconds']:.6f}秒と新probe/最悪154区切り/全科学予測が2400秒内の場合のみ本学習へ。"
    folder=study.RUN if scientific else study.RUN/'probe'
    if phase!='preparation':
        job=read_json(folder/'job.json')
        if alive(job)!=running:raise ValueError('Actual process does not match milestone')
        report.update(actual_job=job,actual_live_process=running,GPU_seconds=job['GPU_elapsed_seconds'])
        if phase=='probe':
            r=study.probe_evidence();estimate=study.estimate_training(r);total=estimate+r['GPU_seconds']+c['previous_related_GPU_seconds']
            report.update(actual_probe=r,result=study.reference(folder/'result.json'),estimated_science_GPU_seconds=estimate,
                estimated_related_total_GPU_seconds=total,planning_within_budget=total<=2400)
            detail=f"ownCUDA固定20更新×連続2区切り対1+1の全state/history/LR/有限値/境界NLLに合格、4区切り80更新timing完了。検証160更新/{r['verification_source_CE_teacher_tokens']}CE教師は科学から除外、GPU{r['GPU_seconds']:.6f}秒/120。元math有限projector controlは不変source/同memoryの旧実証を再利用と明示し、新診断GPUへ足さない。最悪科学予測{estimate:.6f}秒、旧3診断/ownprobe込み{total:.6f}秒/2400。内部tentative点がboundedとの証明ではない。予算内のみscience凍結し、同元親/Adam/actualLR.00001/同staged91,641,755CE＋追加memory gradient別会計/同日本語・全80/旧全gate採否へ。"
        elif running:
            report.update(scientific_source_CE_teacher_tokens=job.get('actual_teachers',0),teacher_count_scope='Observed accepted block updates at heartbeat, not final total.',
                verification_GPU_seconds=c['verification_GPU_seconds'])
            detail=f"science実起動actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}、実stage{job.get('stage')}・受入{job.get('completed_updates',0)}/3068更新・教師{job.get('actual_teachers',0)}を確認。科学上限{c['GPU_budget_seconds']:.6f}秒＋ownprobe{c['verification_GPU_seconds']:.6f}＋旧診断{c['previous_related_GPU_seconds']:.6f}=2400。各受入境界で重み/Adam/scheduler/RNG/sampler/全会計CP保存、未確定区切りは一切保存/完了量へ加算しない。終端・全日本語/80内容・採否は未完了。restartは実PID不在確認後 scripts/run_block_Web_constraint.ps1 -Mode Train -Worker。"
        else:
            if job['status'] not in ('complete','failed_or_interrupted'):raise ValueError('Terminal status required')
            if job['status']=='complete' and scientific:
                r=read_json(folder/'compare-result.json');report.update(actual_result=r,result=study.reference(folder/'compare-result.json'))
                if 'finite_rejection' in r:
                    rejected=r['finite_rejection'];report['scientific_source_CE_teacher_tokens']=rejected['accepted_source_CE_teacher_tokens']
                    detail=f"固定20区切りの有限受入不能で分岐終了、actual{job['pid']}はcomplete・実不在。受入{rejected['accepted_source_updates']}更新/{rejected['accepted_source_CE_teacher_tokens']}CE教師、拒否した全区切りは重み/Adam/scheduler/RNG/samplerを直前境界へrollbackしnativeCP保持。拒否source梯度/追加memorygradient・forwardは別会計。科学GPU{r['GPU_seconds']:.6f}秒、全3068/91,641,755や品質達成とはしない。元UI復帰、cadence/packet/bound/projector/LR等救済sweepなし。次はこの実失敗を根拠に別のBase改善を定義する。"
                else:
                    report['scientific_source_CE_teacher_tokens']=r['checkpoint']['additional_supervised_tokens']
                    detail=f"全3068更新/同91,641,755CE教師の本科学とdev256/日本語192・331・1119/greedy80 rawを完了、actual{job['pid']}は実不在。科学GPU{r['GPU_seconds']:.6f}秒、追加memorygradient/forward別会計。上限は受入境界だけで内部各更新をboundedと偽らない。元10B UI復帰。次は全80の個別内容と強い旧相対/絶対/歴史Webgateの採否、合格のみ独立学習seed/full dev/protected test/採用へ。GPU終了だけでBase完成ではない。"
            else:
                report['partial_result']=read_json(folder/'progress-result.json') if (folder/'progress-result.json').exists() else {}
                detail=f"固定20境界jobのactual{job['pid']}は実終端/不在、GPU{job['GPU_elapsed_seconds']:.6f}秒、理由{job.get('error')}。原source/partial/受入境界CPと失敗を保持し、未達を合格へ置換しない。元UI復帰、同一失敗の無制限再試行なし。次は実理由に対応する修復または分岐結論。"
    if not running:report['original_UI']=original_UI()
    atomic_json(destination,report)
    files=[destination,config,study.PROPOSAL,ROOT/'reports/phase6/block_Web_constraint_tests.xml',Path(__file__),
        ROOT/'scripts/define_block_Web_constraint.py',*[ROOT/s for s in study.SOURCES]]
    if phase not in ('preparation','launch'):files.extend(p for p in sorted(folder.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml'))
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix=f"Base専用固定20境界constraint: {phase}（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n{detail}\n\n旧毎更新予算超過は不採用のまま、cadence20は別研究として固定。元math保持packet/bound/margin/projector/LR/元staged入力・教師mask/decoderと旧相対・絶対・歴史Webの全品質基準を維持。追加Web gradient/拒否試行を別会計し総教師量matchedと称さない。Phase0–3/数値7/全旧失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n"
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['block_Web_constraint_'+phase]=study.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)),ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('preparation','probe','launch','terminal','probe_failure'));main(p.parse_args().phase)
