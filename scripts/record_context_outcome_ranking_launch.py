"""Persist actual CUDA gate and live Base-only science identity without editing frozen inputs."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_context_outcome_ranking_comparison as study


def ref(path):
    return dict(path=str(path),sha256=sha256(path))


def main():
    report=ROOT/'reports/phase6/context_outcome_ranking_launch.json'
    if report.exists():raise ValueError('Preserve actual launch record')
    c=read_json(study.CONFIG);probe=study.probe_evidence();job=read_json(study.RUN/'job.json')
    study.scope(c)
    if (job['config_sha256']!=sha256(study.CONFIG) or not alive(job)
            or job['status'] in ('failed','complete') or job.get('stage')!='training'
            or not job.get('teachers',0)>0):raise ValueError('Actual positive-learning live science process required')
    for path,digest in c['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen owned science source differs')
    snapshot=ROOT/'reports/phase6/context_outcome_ranking_launch_job_snapshot.json'
    if snapshot.exists():raise ValueError('Preserve live job snapshot')
    atomic_json(snapshot,job)
    timing,estimate=study.estimate_training(probe)
    if estimate+probe['GPU_seconds']>study.CEILING:raise ValueError('Keep original finite budget gate')
    r=dict(status='actual_CUDA_gate_complete_scientific100M_live_no_quality_result_yet',created_at=now(),
        scientific_config=ref(study.CONFIG),probe_config=ref(study.PROBE_CONFIG),
        probe_result=ref(study.RUN/'probe/result.json'),probe_job=ref(study.RUN/'probe/job.json'),
        live_job_snapshot=ref(snapshot),live_job_path=str(study.RUN/'job.json'),
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        actual_identity_verified_live=True,observed_teachers=job['teachers'],observed_loss=job['loss'],
        restart_command=job['restart_command'],checkpoint_directory=str(study.RUN/study.ARM/'training'),
        original_UI_restore='Durable Windows wrapper finally restores the original10B Base UI; no failed pilot served.',
        actual_CUDA_full_resume_passed=probe['gate']['passed'],actual_CUDA_state_history_checks=probe['gate']['checks'],
        actual_initial_parent_checks=probe['initial_parent_preservation'],
        probe_GPU_seconds=probe['GPU_seconds'],new_total_GPU_ceiling_seconds=study.CEILING,
        previous_related_all_GPU_seconds=c['previous_related_study_GPU_seconds'],
        estimated_training_seconds=timing['estimated_training_seconds'],measured_timing=timing,
        forecast_science_GPU_seconds_with_margin=estimate,
        forecast_total_new_GPU_seconds_with_margin=estimate+probe['GPU_seconds'],
        verification_CE_teacher_tokens=probe['verification_teacher_tokens'],
        verification_reference_input_tokens=probe['verification_reference_input_tokens'],
        verification_reference_soft_positions=probe['verification_reference_soft_positions'],
        verification_reference_non_EOS_teacher_probability_mass=probe['verification_reference_non_EOS_teacher_probability_mass'],
        verification_ranking=probe['verification_ranking'],verification_optimizer_updates=probe['GPU_optimizer_updates'],
        verification_weights_discarded_for_science=True,
        proposed_scientific_ordinary_CE_teachers=100000000,proposed_scientific_main_input_positions=100532224,
        proposed_scientific_reference_input_positions=25133056,
        proposed_scientific_ranking_padded_positions=6283264,
        proposed_scientific_relational_choice_labels=12272,proposed_combined_student_padded_positions=131948544,
        new_original_corpus_tokens=0,full_scientific_counts_pending=True,
        CPU_runner_tests=ref(ROOT/'reports/phase6/context_outcome_ranking_comparison_tests.xml'),
        prefreeze_operational_corrections='Owned generation patch initially assumed an extra blank line; synchronization stopped before copying the test, so the first pytest invocation found no test file and executed0tests. Corrected only the new unfrozen builder/runner synchronization; next actual2CPU tests passed. No GPU failure or changed prototype/loss/quality/budget.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Wait for this exact live owned100M job; inspect PID/boot/start before any resume. Then full256/Japanese/all80 individual notes/bridge-retention/all3068 primary+Web input equality and actual ranking exposure audits, unchanged strong stagedCE/absolute/historical-Web adoption gates. Independent seed/full dev/protected test only after a qualified pilot; notify/stop after actual adopted Base.')
    atomic_json(report,r)
    extensions={'.json','.jsonl','.py','.ps1','.xml','.tsv','.md','.toml','.lock','.log'}
    files={p for p in (study.RUN/'probe').rglob('*') if p.is_file() and p.suffix in extensions}
    files.update(ROOT/path for path in c['source_sha256'] if 'context_outcome' in path)
    files.update(p for p in (ROOT/'reports/phase6').glob('context_outcome_*.json') if 'portable' not in p.name)
    files.update((ROOT/'reports/phase6').glob('context_outcome_*.xml'))
    files.update((ROOT/'configs/phase6').glob('context_outcome_*.json'))
    files.update((ROOT/'scripts/record_context_outcome_ranking_launch.py',ROOT/'.python-version'))
    files=sorted(files)
    manifest={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/context_outcome_ranking_launch_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve evidence archive')
    with tarfile.open(archive,'w:gz',compresslevel=5) as stream:
        for p in files:stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/context_outcome_ranking_launch_portable.json',dict(files=manifest,
        file_count=len(files),raw_bytes=sum(v['bytes'] for v in manifest.values()),archive=ref(archive),
        archive_bytes=archive.stat().st_size,checkpoint_tensors_and_corpus_arrays_excluded=True,
        mutable_scientific_job_not_in_archive=True,live_observation_is_snapshot=True))
    prefix=f'''train文脈比較100Mの実CUDA検証完了・科学学習を永続開始（2026-10-06 JST）。前goal turnは有限CPU診断/全raw/3損失prototypeの実CPU再開をd4587a5へ保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

owned runner/reviewer/accountant/durablePSを実装、既存凍結source/prototype/dataは不変。関連scope/実TRAIN入力台帳改変拒否のCPU2tests/.1桁秒とPS構文成功（実XMLはcontext_outcome_ranking_comparison_tests.xml）。新コード生成のblank-line置換は初回に拒否されtest未copyの最初のpytestは0件で終了、own unfrozen同期を修正後2tests成功、実GPU失敗0・基準/予算変更なし。rank係数/温度1・2family/8x256/eager BF16 math、main32x1024/ref8x1024 compiled flashの同100M＋conditional WebKLを保つ。

probe actual609903/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15795098はcomplete・実ps不在。実CUDA連続4対2+2の全53state/history/有限値/LRと初期親10checks合格、rank sampler/state/counters/digestも一致。40検証更新/CE{probe['verification_teacher_tokens']:,}/reference input{probe['verification_reference_input_tokens']:,}/body{probe['verification_reference_soft_positions']:,}/mass{probe['verification_reference_non_EOS_teacher_probability_mass']}、rank80family presentations/160choice labels/13376valid/81920padded/gold933・foil933位置/gold4022・foil4022bytes、GPU{probe['GPU_seconds']:.6f}秒を科学学習へ加えず重みを破棄。全32 main/ref入力が終了済controlと一致。

combined更新中央値{timing['steady_step_seconds']:.9f}秒、3068更新のtrain推定{timing['estimated_training_seconds']:.6f}秒（約7.3分）。従来150秒非学習枠＋30%＋50秒余裕を保持してscience見積{estimate:.6f}＋probe{probe['GPU_seconds']:.6f}=新全{estimate+probe['GPU_seconds']:.6f}秒<900で科学configを凍結。旧関連全{c['previous_related_study_GPU_seconds']:.6f}秒を別保存し消さない。

durable Windows worker34292、actual WSL{job['pid']}/同boot/start{job['start_ticks']}をlive identity確認、main追加{job['teachers']:,}CE教師/loss{job['loss']}有限で科学100M学習中。configs/phase6/context_outcome_ranking_comparison.jsonとreports/phase6/context_outcome_ranking_launch.json、RUN context-outcome-ranking-comparison-20261006へjob/log/checkpoints/source snapshotsを保存。元10B UIはGPU中停止しwrapper finallyで復帰。actual不在・valid checkpointのときだけ{job['restart_command']}で再開、二重GPUなし。main100M/reference25,133,056inputに加わるrank6,283,264padded/12,272choice labelsは別会計、combined131,948,544input、valid/gold/foil/bytesは全3068実値を監査。新corpus0・同supervision量とは言わない。

次はこのowned job終端→同256全文472055bytes/122343tokens、日本語192-331-1119、全80greedy64と全80個別内容、bridge/retention各128family、全3068主/参照input-digest-mask-sourceとrank入力・全露出台帳の採否。conditionalKLは機序対照、採用は強い元staged CE23+8/CI lower>0/EOS>=76/反復<=2と既存absolute/歴史Web BPB<=.981285952を維持、弱いcontrolへ置換しない。pilot合格後だけ独立学習seed/full dev/protected test。設定sweep/有利CP探索/予算追加/自動延長なし。旧Phase0–3/数値7失敗/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    prefix=prefix.replace('CPU2tests/.1桁秒','CPU2tests/1.01秒')
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(),encoding='utf-8')
    path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(path)
    progress.update(status='Base_only_context_outcome_ranking_actual_CUDA_gate_complete_scientific100M_live',
        last_updated_at=now(),context_outcome_ranking_launch=ref(report),next_action=r['next_action'],
        Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(path,progress)
    print(dict(status=r['status'],actual_identity=r['actual_identity'],forecast=r['forecast_total_new_GPU_seconds_with_margin']),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
