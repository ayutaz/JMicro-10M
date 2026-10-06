"""Preserve terminal own probe and fixed-science preparation as portable evidence."""
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from record_source_gradient_attribution import original_UI
import run_base_preference_comparison as study


def main():
    c=study.inspect(); p,r,timing,estimate,used,budget=study.probe_evidence(); job=read_json(study.RUN/'probe/job.json')
    destination=ROOT/'reports/phase6/base_preference_science_prepared.json'
    if destination.exists(): raise ValueError('Preserve original own probe and scientific preparation')
    report=dict(status='Base_preference_science_prepared', created_at=now(), config=study.reference(study.CONFIG),
        own_probe_config=study.reference(study.probe.CONFIG), own_probe_result=study.reference(study.RUN/'probe/result.json'),
        actual_probe_job=job, probe_GPU_seconds=used, verification_updates=r['verification_updates'],
        verification_teacher_tokens=r['verification_teacher_tokens'], selected_pair_batch=c['pair_batch'], measured_timing=timing,
        estimated_total_GPU_seconds=estimate+used, new_scientific_positive_teacher_tokens=0,
        diagnostic_GPU_seconds_separate=c['diagnostic_GPU_seconds_separate'], original_UI=original_UI(),
        Base_complete=False, Base_adopted=False, protected_test_used=False, Chat_started=False, quantization_started=False)
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.probe.CONFIG,study.PROPOSAL,Path(__file__),
        *[ROOT/s for s in study.SOURCES],ROOT/'reports/phase6/base_preference_science_tests.xml']
    files += [q for q in sorted((study.RUN/'probe').rglob('*')) if q.is_file() and q.suffix in ('.json','.jsonl','.py','.ps1','.xml')]
    files=list(dict.fromkeys(files)); archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},file_count=len(files),archive=study.reference(archive),raw_source_pairs_and_tensors_native_only=True))
    detail=(f'ownCUDA actual{job["pid"]}完了/不在、GPU{used:.6f}秒/180、native W/Adam/scheduler/全RNG/Webcursor/tied10M初期保存と共通Web・両損失4対2+2全state/history一致。'
        f'152検証更新/{r["verification_teacher_tokens"]}教師は科学と別、検証重み破棄。8対56の実速度から重複なし56を選択、両条件CEinput/auxiliary順序一致、全reference readonly。'
        f'科学予測{estimate:.6f}秒/probe込み{estimate+used:.6f}/1800。実共通6Mを一度→同chosen2MをCE0対CE+DPO.1(beta.1)の一要因、参照は実共通6M endpointから新計算。'
        '専用runner/同全日本語dev256・各80/bridge-retention512/採否/個別raw-bound notesを実装し凍結、CPU3tests/2.84秒で累積費用、native common cursor/Adam会計改変拒否、両末尾quota/negative会計と同順序を確認。'
        '新科学10M・各arm8M予定、固定56/4565positionsの約438反復は教材増量ではない。新科学0の準備証拠・旧69.957秒diagnostic別記。次は永続実比較→全160内容→元相対/絶対/歴史BPB1%で採否。'
        '合格のみ独立学習seed/full dev/protected test/adoptionへ。未合格はこの固定両recipe終了、source/beta/coefficient/epoch/LR/decoder/CP救済sweepなし。')
    prefix='Base専用CE対CE+DPO: GPU継承・再開合格、本比較準備完了（2026-10-06 JST）。\n\n'+detail+'\n\nBase未完成・完成時通知して停止。Chat/Dialogue/SFT/量子化なし。既存全失敗/旧数値7/Phase0–3/品質基準を維持。WSL uv/local commitのみ/pushなし。以下は過去の履歴。\n\n'
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text(prefix+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json'; progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['Base_preference_preparation']=study.reference(destination);atomic_json(q,progress)
    print(dict(status=report['status'],portable_files=len(files),GPU_seconds=used))


if __name__=='__main__': main()
