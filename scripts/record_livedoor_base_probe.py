"""Preserve real news CUDA probe milestones and portable text, no scientific claim."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import probe_livedoor_base as study


def main(phase):
    c=study.inspect();job=read_json(study.RUN/'probe/job.json')
    if alive(job) or job['status'] not in ('complete','failed_or_interrupted'):raise ValueError('Actually terminal absent own probe required')
    destination=ROOT/f'reports/phase6/livedoor_base_probe_{phase}.json'
    if destination.exists():raise ValueError('Preserve original actual news probe milestone')
    report=dict(status='livedoor_base_probe_'+phase,created_at=now(),config=study.reference(study.CONFIG),actual_job=job,
        GPU_seconds=job['GPU_elapsed_seconds'],previous_failed_GPU_seconds=c.get('previous_failed_GPU_seconds',0.),scientific_teacher_tokens=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,original_UI=original_UI())
    detail=f'own news probe actual{job["pid"]}実終端/不在、GPU{job["GPU_elapsed_seconds"]:.6f}秒、理由{job.get("error")}。原config/source/job/失敗を保存し元UI復帰。'
    if job['status']=='complete':
        r=read_json(study.RUN/'probe/result.json');timing,estimate=study.estimate_training(r)
        if (not r['passed'] or r['config_sha256']!=sha256(study.CONFIG) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
                or not all(r['initial_preservation'].values()) or any(not all(g['checks'].values()) for g in r['gates'].values())
                or r['verification_updates']!=80 or r['measured_timing']!=timing or r['estimated_science_GPU_seconds']!=estimate):
            raise ValueError('Actual full inherited CUDA/both-source exact resume and timings required')
        total=estimate+r['GPU_seconds']+c.get('previous_failed_GPU_seconds',0.)
        report.update(result=study.reference(study.RUN/'probe/result.json'),actual_result=r,estimated_total_GPU_seconds=total,science_cost_within1800=total<=1800)
        detail=(f'actual{job["pid"]}実完了/不在、GPU{r["GPU_seconds"]:.6f}秒/120。実native W/Adam/scheduler/CUDA含む全RNG/Webcursor/tied10M初期一致、'
            f'本goals Webと明示Web=1 news境界stressの両4連続対2+2全state/history/LR/有限値一致・各32timingに合格。80検証更新/{r["verification_teacher_tokens"]}教師は科学と別、stress重み破棄。'
            f'科学予測{estimate:.6f}秒・ownprobe/旧失敗込み{total:.6f}/1800。次は費用内のみ残26428122教師の専用科学runner/同全日本語・dev256・全80reviewを実装して凍結、共通73571878教師/旧対照を再GPUしない。'
            'これは再開/実装/費用の証明でモデル品質/完成ではない。')
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,Path(__file__),*[ROOT/s for s in study.SOURCES],ROOT/'reports/phase6/livedoor_base_trainer_tests.xml',
        ROOT/'reports/phase6/livedoor_base_trainer_tests_initial_failure.xml',Path(c['references']['CPU_tests']['path'])]
    files += [q for q in sorted((study.RUN/'probe').rglob('*')) if q.is_file() and q.suffix in ('.json','.jsonl','.py','.ps1','.xml')]
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix='Base専用news CUDA probe: '+phase+'（2026-10-06 JST）。\n\n'+detail+'\n\nBase未完成・完成時通知停止、Chat/量子化なし。元品質条件/全旧失敗保持、source/LR/epoch/decoder/CP救済sweepなし。WSL uv/local commitのみ/pushなし。以下は過去の履歴。\n\n'
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text(prefix+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['news_probe_'+phase]=study.reference(destination);atomic_json(q,progress)
    print(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('failure_v1','passed'));main(p.parse_args().phase)
