"""Snapshot an actually live scientific worker; never treat labels as liveness."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_parameter_displacement_anchor_v3 as study


def main():
    c=read_json(study.CONFIG);job=read_json(study.RUN/'job.json')
    if not alive(job) or job['config_sha256']!=sha256(study.CONFIG):raise ValueError('Actual matching scientific process required')
    for p,digest in c['source_sha256'].items():
        if sha256(ROOT/p)!=digest:raise ValueError('Live scientific source differs')
    record=dict(status='scientific_worker_confirmed_live',observed_at=now(),actual_job_snapshot=job,
        config=study.reference(study.CONFIG),run=str(study.RUN),actual_process_confirmed_live=True,
        successful_and_failed_probe_GPU_seconds=c['verification_GPU_seconds'],GPU_total_ceiling_seconds=1800,
        scientific_teacher_goal=200000000,Base_complete=False,Base_adopted=False,
        protected_test_used=False,quality_criteria_unchanged=True,Chat_started=False,quantization_started=False,
        restart_command='scripts/run_parameter_displacement_anchor_v3.ps1 -Mode Train -Worker',
        restart_requires_actual_process_absent=True,
        next_action='Continue this actual worker; finish both100M/evaluation and all160 raw-bound reviews. '
            'Do not restart from an observation timeout or a setup label. Restore original UI at termination; '
            'only qualified pilot allows independent learning seed/full dev/protected test/adoption.')
    destination=ROOT/'reports/phase6/parameter_displacement_anchor_active_job.json';atomic_json(destination,record)
    prefix=f'''固定parameter L2対照の本比較を永続起動（2026-10-06 JST）。実両CUDA gate/32timingと凍結設定はd1b44f0へ保存したprogress。Baseのみ継続・完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}を実確認、configSHA{job['config_sha256']}、run reports/phase6/parameter-displacement-anchor-v3-20261006。stage {job.get('stage')}、追加教師{job.get('teachers')}/当arm100M、loss{job.get('loss')}有限で継続。初期status setupラベルで終了/停止を推定せずPID/heartbeat/teacher更新を用いる。両科学200M＋検証2615904教師は別、probe成功/失敗GPU33.680480秒を保ち全上限1800。元UIは科学実行中停止、durable finallyで元10Bへ復帰。

review_parameter_displacement_anchor.pyを準備、実CPU terminal ledger/anchor/body+EOS CE+L2/連続更新/教師0の誤会計を拒否する1test/1.63秒成功。これは品質判定ではなく、本流/評価/全160内容/採否は未完了。親state/core/anchor/source/係数は凍結後不変、checkpoint/optimizer/RNG/samplerは完了更新で保存。再開はactual不在確認後scripts/run_parameter_displacement_anchor_v3.ps1 -Mode Train -Worker。観測timeoutやラベルだけで再起動しない。

次は同実jobの両100M/共通256bytes・日本語192-331-1119・全80各・bridge/retention各128→160個別raw notes/両対照と旧全基準の採否→UI/可搬証拠/commit。fixed lambda/anchor/source/decoder sweepなし、pilot合格後だけ独立学習seed/full dev/protected test/adoption。Base未完了・未採用、全旧失敗とPhase0–3/数値7失敗を保持。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_parameter_anchor_scientific_worker_actual_live',updated_at=now(),
        parameter_displacement_anchor_active_job=study.reference(destination),next_action=record['next_action'],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=record['status'],pid=job['pid'],stage=job.get('stage'),teachers=job.get('teachers'))))


if __name__=='__main__':main()
