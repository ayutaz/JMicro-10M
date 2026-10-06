"""Persist observed actual fourth-cell worker, checkpoint and restart handoff."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_interleaved_outcome_order as study


def main():
    c=read_json(study.CONFIG);job=read_json(study.RUN/'job.json');live=alive(job)
    if job['config_sha256']!=sha256(study.CONFIG) or not live:raise ValueError('Observe the actual live science worker')
    latest=read_json(study.RUN/'progress-result.json') if (study.RUN/'progress-result.json').exists() else {}
    path=ROOT/'reports/phase6/interleaved_outcome_active_job.json'
    report=dict(status='actual_live_fourth_cell',actual_alive=True,observed_at=now(),actual_job=job,
        config=study.reference(study.CONFIG),checkpoint=latest.get('checkpoint'),source_gate=study.reference(study.LEDGER),
        scientific_teacher_budget=91641755,nominal_reference_teacher_quota=100000000,own_probe_GPU_seconds=c['verification_GPU_seconds'],
        GPU_science_ceiling_seconds=c['GPU_budget_seconds'],restart_command=job['restart_command'],
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(path,report)
    prefix=f'''混在順序×固定outcome/EOS教師の実GPU比較を永続起動（2026-10-06 JST）。own source会計/CUDA gate/実測設定は6970309へ保存したprogress。Baseのみ完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}をalive/ps確認、configSHA{sha256(study.CONFIG)}、run reports/phase6/interleaved-outcome-order-20261006。観測stage{job['stage']}、直近教師{job.get('actual_teachers',0)}/新実hard教師91641755（reference100Mと区別）、直近loss{job.get('loss')}有限。status setupの初期ラベルだけで停止を推定せずPID/heartbeat/教師/完了checkpointを根拠とする。既3条件/両CPU source hashesはそのまま、Web実cursor・全model/Adam/scheduler/RNG/実LR.00001継承。GPU新全上限900/own probe17.989334秒、元UIは実job中停止・durable finallyで復帰。実GPU gate48更新/教師は科学へ加えない。

reviewer/four-cell analysisを追加、CPU2tests/1.70秒で実CPU masked stateのreference教師誤計数・source target SHA改変・欠損更新と不均一byteのpaired四条件交互作用を確認。fixtureは実モデル品質/独立seedの証明ではない。関連source/counter digestと全80raw採点を要求し、既strong/絶対/歴史WebBPB基準を変更しない。全評価/80内容/四条件採否は未完了。再開はactual不在確認後scripts/run_interleaved_outcome_order.ps1 -Mode Train -Worker、観測timeoutだけで重複起動しない。

次は同jobの全256commonbytes/日本語192-331-1119/greedy80/bridge-ret128完了→全80個別raw notes/既3条件の旧採点そのまま四条件比較→採否/元UI/可搬証拠/commit。qualified recipe後だけ独立学習seed/full dev/protected test/adoption、Base未完了。ratio/mask/source/CP/LR/decoder sweepで今回を救済しない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_interleaved_outcome_fourth_cell_GPU_active',updated_at=now(),
        interleaved_outcome_active_job=study.reference(path),next_action='Finish the same actual job, all80 individual content and unchanged four-cell quality review.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],pid=job['pid'],stage=job['stage'])))


if __name__=='__main__':main()
