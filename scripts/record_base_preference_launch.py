"""Record actual durable Base-only science identity without changing frozen recipe."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_base_preference_comparison as study

job=read_json(study.RUN/'job.json')
if job['status']!='running' or not alive(job) or job['config_sha256']!=sha256(study.CONFIG):
    raise ValueError('Actually live frozen comparison required')
destination=ROOT/'reports/phase6/base_preference_science_launch.json'
if destination.exists():raise ValueError('Preserve original launch identity')
atomic_json(destination,dict(created_at=now(),actual_job=job,config=study.reference(study.CONFIG),Base_complete=False,Chat_started=False,quantization_started=False))
detail=(f'科学actual{job["pid"]}/boot{job["boot_id"]}/start{job["start_ticks"]}実稼働、stage{job["stage"]}、GPU累積{job["GPU_elapsed_seconds"]:.3f}秒。'
    '共通6M一度と両同positive2M、250更新/中断時全state原子的保存。restartは実PID不在を先に確認して scripts/run_base_preference_comparison.ps1 -Worker。'
    '元UIは終端finallyで復帰。次は同日本語/dev256/各80/bridge-retention512→全160個別内容・旧品質条件→採否。Base未完成、完成時通知停止。Chat/Dialogue/SFT/量子化なし、WSL uv/local commitのみ/pushなし。')
for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
    q=ROOT/relative;q.write_text('Base専用CE対CE+DPO: 実比較開始（2026-10-06 JST）。\n\n'+detail+'\n\n以下は過去の履歴。\n\n'+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
progress.update(status='Base_preference_science_running',updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
progress['Base_preference_launch']=study.reference(destination);atomic_json(q,progress)
print(dict(status='Base_preference_running',pid=job['pid'],stage=job['stage']))
