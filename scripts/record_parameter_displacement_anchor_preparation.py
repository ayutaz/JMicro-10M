"""Persist actual CUDA probe, its two implementation failures, and measured plan."""
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
import run_parameter_displacement_anchor_v3 as study


def main():
    destination=ROOT/'reports/phase6/parameter_displacement_anchor_preparation.json'
    if destination.exists():raise ValueError('Preserve original actual preparation')
    c=study.inspect(study.CONFIG);probe=study.probe_evidence();job=read_json(study.RUN/'probe/job.json')
    failed=read_json(Path(c['references']['v2_failed_job']['path']))
    if alive(failed) or failed['GPU_elapsed_seconds']!=c['failed_probe_GPU_seconds']:
        raise ValueError('Old failed probe must be absent and its exact cost retained')
    report=dict(status='own_two_arm_CUDA_fullstate_resume_timing_complete_science_frozen_unstarted',created_at=now(),
        scientific_config=study.reference(study.CONFIG),probe_config=study.reference(study.PROBE_CONFIG),
        probe_result=study.reference(study.RUN/'probe/result.json'),actual_probe_job=job,actual_probe_process_absent=True,
        initial_fullstate_preservation=probe['initial_fullstate_preservation'],
        resume_checks={arm:gate['checks'] for arm,gate in probe['gates'].items()},
        verification_optimizer_updates=probe['GPU_optimizer_updates'],verification_teacher_tokens=probe['verification_teacher_tokens'],
        scientific_teacher_tokens=0,scientific_optimizer_updates=0,
        successful_probe_GPU_seconds=probe['GPU_seconds'],failed_probe_GPU_seconds=c['failed_probe_GPU_seconds'],
        total_new_GPU_seconds_so_far=c['verification_GPU_seconds'],probe_cumulative_GPU_ceiling_seconds=120,
        total_comparison_GPU_ceiling_seconds=1800,remaining_science_GPU_seconds=c['GPU_budget_seconds'],
        previous_related_GPU_seconds_preserved=2343.8289305070936,
        related_GPU_including_probe_seconds=2343.8289305070936+c['verification_GPU_seconds'],
        initial_CPU_test_failure=dict(xml=study.reference(ROOT/'reports/phase6/parameter_displacement_anchor_tests_initial_failure.xml'),
            failures=2,reason='CPU fixture changed scheduler base_lrs but retained inconsistent optimizer initial_lr; '
                'corrected fixture and restored exact optimizer state after LambdaLR construction. No GPU or quality evidence.'),
        v1_preflight_failure=dict(config=c['references']['v1_preflight_failure_config'],GPU_seconds=0,
            reason='Raw bytes were compared with newline-normalized implementation_hashes. Preserved v1 source/config; v2 separates contracts.'),
        v2_GPU_failure=dict(config=c['references']['v2_config'],job=failed,
            reason='Anchor comparison used a CUDA tensor and CPU parent tensor. No optimizer updates occurred; '
                'v3 compares CPU views and retains exact failed cost within120/1800 ceilings.'),
        CPU_preparation_seconds={version:read_json(ROOT/path)['CPU_preparation_seconds'] for version,path in
            [('v1','configs/phase6/parameter_displacement_anchor_probe.json'),
             ('v2','configs/phase6/parameter_displacement_anchor_probe_v2.json'),
             ('v3','configs/phase6/parameter_displacement_anchor_probe_v3.json')]},
        own_measured_timings=c['measured_timings'],estimated_total_science_seconds_with_margin=c['estimated_GPU_seconds_with_margin'],
        parameter_coefficient=c['coefficients']['parameter_anchor'],quality_criteria_unchanged=True,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Launch one persistent v3 matched CE100M plus fixed parameter-anchor100M; '
            'evaluate full256/Japanese/80each/bridge128/retention128; read all160 and compare unchanged guards '
            'to both new matched CE and old strong staged. Pilot is not Base adoption.')
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROBE_CONFIG,ROOT/'configs/phase6/parameter_displacement_anchor_probe.json',
        ROOT/'configs/phase6/parameter_displacement_anchor_probe_v2.json',
        ROOT/'reports/phase6/parameter_displacement_anchor_tests.xml',ROOT/'reports/phase6/parameter_displacement_anchor_tests_initial_failure.xml',
        ROOT/'reports/phase6/parameter_displacement_anchor_proposal.json',Path(__file__),*[ROOT/p for p in study.SOURCES],
        ROOT/'scripts/run_parameter_displacement_anchor.py',ROOT/'scripts/run_parameter_displacement_anchor.ps1',
        ROOT/'scripts/run_parameter_displacement_anchor_v2.py',ROOT/'scripts/run_parameter_displacement_anchor_v2.ps1',
        Path(c['references']['v2_failed_job']['path'])]
    files.extend(p for p in sorted((study.RUN/'probe').rglob('*.json')) if 'source' not in p.relative_to(study.RUN).parts)
    files.extend(p for p in sorted((study.RUN/'probe').rglob('*.jsonl')) if 'source' not in p.relative_to(study.RUN).parts)
    files=list(dict.fromkeys(files))
    evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/parameter_displacement_anchor_preparation_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve raw preparation archive')
    with tarfile.open(archive,'w:gz') as output:
        for path in files:output.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/parameter_displacement_anchor_preparation_portable.json',dict(files=evidence,
        file_count=len(files),raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    prefix=f'''parameter変位の固定L2比較を実装・両arm実CUDA gate/速度測定を完了（2026-10-06 JST）。前TRAIN診断はd516c78へ保存したprogress。Baseのみ継続、品質・独立学習seed/full dev/protected test/採用で完成時に通知・停止。Chat/Dialogue/SFT/量子化なし。

same mixed fullstate SHA6d901bd…/update323503から両新arm同追加staged100Mを実装、candidateだけlambda=.04161064039180984のunique parameter L2。両armmodel/Adam/scheduler/RNG/actualWebcursor/親sampler/anchor/actualLR.00001の初期一致を実確認。短source/local quotasのみ同seed42でresetし親cursorはlineageへ保持。tieは一回、L2教師0。CPU初回fixtureのscheduler base_lrsとoptimizer initial_lr不一致2failedを保存し修正、4tests/1.64秒で解析勾配・anchor不変・両CPU4vs2+2全state/phase/counters・費用計算が成功。

v1preflightはnormalized core hashをrawSHAと比較してGPU前に拒否。v2はCUDAanchor対CPU親の検証でGPU{failed['GPU_elapsed_seconds']:.6f}秒・optimizer0で停止、actual{failed['pid']}不在。旧source/config/rawを変えずv3owned修正版に分離。v3probe actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・不在。実両CUDA4vs2+2のmodel/Adam/scheduler/RNG/sampler/lineage/全会計/digest/loss/CE/L2/有限値一致、各32steady timingsを確認。検証80更新/{probe['verification_teacher_tokens']}教師は科学へ加えず、成功GPU{probe['GPU_seconds']:.6f}＋失敗={c['verification_GPU_seconds']:.6f}秒/上限120に保持。

本比較の設定configs/phase6/parameter_displacement_anchor_v3.jsonを実測から凍結。対照step{c['measured_timings']['matched_staged_CE']['steady_step_seconds']:.6f}秒/candidate{c['measured_timings']['parameter_anchor']['steady_step_seconds']:.6f}秒、2armtrain予測に1.3×・save・評価reserve150・余裕50を含み{c['estimated_GPU_seconds_with_margin']:.6f}秒、probe込み1800秒以内。run reports/phase6/parameter-displacement-anchor-v3-20261006、永続起動scripts/run_parameter_displacement_anchor_v3.ps1 -Mode Train、再開はactual不在確認後-Worker。新科学教師/optimizer0、本学習まだ未開始。全raw/gates/timings/failures/source/testsはparameter_displacement_anchor_preparation/portable.json/archiveへ保存、旧失敗/Phase0–3/数値7失敗を保持。

次は実両100M→同256共通byte/日本語192-331-1119/greedy80各/bridge-ret128→全160個別raw notes/採否/UI復帰/commit。newmatched対照とoldstrong staged23+8/CI正/EOS76/反復2・絶対/歴史BPB全guardを維持。coefficient/anchor/source/decoder sweepなし。pilot合格後だけ独立学習seed/full dev/protected test/採用へ進む。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_parameter_anchor_own_CUDA_gates_complete_science_frozen_unstarted',updated_at=now(),
        parameter_displacement_anchor_preparation=study.reference(destination),next_action=report['next_action'],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=progress['status'],GPU_seconds=report['total_new_GPU_seconds_so_far'],
        verification_teacher_tokens=probe['verification_teacher_tokens'],estimated_science_seconds=c['estimated_GPU_seconds_with_margin'],portable_files=len(files))))


if __name__=='__main__':main()
