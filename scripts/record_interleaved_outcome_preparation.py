"""Persist actual fourth-cell CUDA gates, source equality and measured budget."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
import run_interleaved_outcome_order as study


def main():
    c=study.inspect(study.CONFIG);r=study.probe_evidence();job=read_json(study.RUN/'probe/job.json')
    destination=ROOT/'reports/phase6/interleaved_outcome_preparation.json'
    if destination.exists():raise ValueError('Preserve original actual preparation')
    previous=read_json(ROOT/'reports/phase6/shared_prefix_web_loss_completion.json')['related_GPU_seconds']
    report=dict(status='fourth_order_target_cell_own_CUDA_complete_science_frozen_unstarted',created_at=now(),
        config=study.reference(study.CONFIG),probe_config=study.reference(study.PROBE_CONFIG),probe_result=study.reference(study.RUN/'probe/result.json'),
        actual_probe_job=job,actual_probe_process_absent=True,initial_fullstate_preservation=r['initial_fullstate_preservation'],resume_checks=r['gate']['checks'],
        verification_optimizer_updates=48,verification_teacher_tokens=r['verification_teacher_tokens'],verification_input_tokens=48*1024*32,
        scientific_teacher_tokens=0,scientific_optimizer_updates=0,GPU_seconds=r['GPU_seconds'],previous_related_GPU_seconds_preserved=previous,
        related_GPU_seconds=previous+r['GPU_seconds'],CPU_preparation_seconds=c['CPU_preparation_seconds'],remaining_updates=3068,
        actual_hard_teachers_predicted=c['actual_scientific_teacher_tokens_predicted'],reference_quota_teachers=100000000,
        physical_input_tokens_predicted=3068*1024*32,source_input_target_accounting=c['references']['reference_input_ledger'],
        own_measured_timing=c['measured_timing'],estimated_science_GPU_seconds_with_margin=c['estimated_GPU_seconds_with_margin'],
        total_new_GPU_ceiling_seconds=900,original_three_cells_reused_not_new_learning=True,
        same_per_source_input_masked_targets_EOS_and_cursors=True,global_source_order_differs=True,
        synthetic_CPU_historical_counts_are_not_actual10_5B_CPU_learning=True,
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Launch the sole mixed/outcome+EOS fourth cell: actual91641755 teachers/3068 updates; '
            'full256/Japanese192-331-1119/greedy80 individually read/bridge-ret128 and four-cell review. '
            'Only qualified recipe permits independent learned seed/full dev/protected test/adoption.')
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROBE_CONFIG,study.PROPOSAL,study.LEDGER,Path(__file__),*[ROOT/p for p in study.SOURCES],ROOT/'reports/phase6/interleaved_outcome_tests.xml']
    files.extend(p for p in sorted((study.RUN/'probe').rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl') and 'source' not in p.relative_to(study.RUN).parts)
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/interleaved_outcome_preparation_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve original actual preparation archive')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/interleaved_outcome_preparation_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    prefix=f'''混在順序×固定outcome/EOS教師のownCUDA準備完了・science設定凍結（2026-10-06 JST）。前shared-prefix診断は3024a2a。Baseのみ完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・不在。元10.5B fullparent d18e3e…のmodel/Adam/scheduler/RNG/actual Web cursor/親sampler lineage/実LR.00001を初期一致確認。mixed8対4+4で全4source/実conditional maskを含む全state/history/finite/source digest/会計の一致に成功。own32steady step{c['measured_timing']['steady_step_seconds']:.6f}秒、検証48更新/{r['verification_teacher_tokens']}教師/1572864inputを科学と別に記録。probeGPU{r['GPU_seconds']:.6f}秒/上限120。

CPU3tests/1.59秒・実CPU準備{c['CPU_preparation_seconds']:.6f}秒/上限60、元mixed3068全reference global digestと両順序source別input/元教師/同mask教師/focus/EOS/全cursors/hashが一致。217MB compact cache再利用、full source index scan/dedupなし。新whole recipeは実hard教師91641755/reference100M/physical100532224/3068更新、源内の系列は同じでglobal順序を変える一条件。旧3条件の学習/評価を再利用し新教師に加えない。CPU歴史global countersはsynthetic protocol fixtureで10.5B実CPU学習と称さない。

configs/phase6/interleaved_outcome_order.json SHA{sha256(study.CONFIG)}を実測から凍結。train見積{c['measured_timing']['estimated_training_seconds']:.6f}秒に1.3×/save/評価reserve150/余裕50を含みscience{c['estimated_GPU_seconds_with_margin']:.6f}秒、probe込み900秒以内。新科学教師/optimizer0、未開始。raw gates/timings/source会計/元teacher予算差/tests/codeはinterleaved_outcome_preparation/portable.json/archiveへ保存。旧Phase0–3/数値7失敗/全不採用/品質条件を保持。

次はscripts/run_interleaved_outcome_order.ps1 -Mode Trainで永続起動→実91641755教師→共通256bytes/Japanese192-331-1119/80個別/bridge-ret128→既3条件と四条件review/元strong23+8/CI正/EOS76/反復2・absolute/歴史WebBPB全guard→元UI/可搬証拠/commit。既mask-staged35/EOS79/反復1の差も明記して旧採点を変更しない。失敗は一条件で終了しratio/mask/weight/source/CP/LR/decoder sweepで救済しない。qualified recipe後だけ独立学習seed/full dev/protected test/adoption、Base未完了。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_interleaved_outcome_own_CUDA_complete_science_frozen_unstarted',updated_at=now(),
        interleaved_outcome_preparation=study.reference(destination),next_action=report['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=r['GPU_seconds'],science_estimate_seconds=c['estimated_GPU_seconds_with_margin'],portable_files=len(files))))


if __name__=='__main__':main()
