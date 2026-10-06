"""Portable actual fixed Base preference experiment; no false completion claim."""
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import run_base_preference_comparison as study


def main():
    c=study.inspect(); job=read_json(study.RUN/'job.json'); r=read_json(study.RUN/'compare-result.json'); review=read_json(study.RUN/'review.json')
    if (alive(job) or job['status']!='complete' or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['config_sha256']!=sha256(study.CONFIG) or review['result_sha256']!=sha256(study.RUN/'compare-result.json')
            or not review['all160_individually_read'] or review['Base_complete'] or review['Base_adopted']):
        raise ValueError('Terminal actual native/all160 content evidence required')
    destination=ROOT/'reports/phase6/base_preference_comparison_completion.json'
    if destination.exists():raise ValueError('Preserve original actual fixed preference completion')
    report=dict(status='Base_preference_fixed_comparison_completed',created_at=now(),actual_job=job,original_UI=original_UI(),
        config=study.reference(study.CONFIG),result=study.reference(study.RUN/'compare-result.json'),review=study.reference(study.RUN/'review.json'),
        actual_review=review,scientific_GPU_seconds=r['GPU_seconds'],total_new_GPU_seconds=review['new_total_GPU_seconds'],
        scientific_positive_teacher_tokens=study.TOTAL,common_positive_teacher_tokens=study.COMMON,positive_teacher_tokens_per_arm=study.COMMON+study.PAIR,
        eligible_for_final_Base_validation=review['eligible_for_final_Base_validation'],Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,Path(__file__),*[ROOT/s for s in study.SOURCES],ROOT/'reports/phase6/base_preference_science_tests.xml',
        ROOT/'reports/phase6/base_preference_comparison_review.json']
    files += [ROOT/f'reports/phase6/base_preference_{arm}_observations.tsv' for arm in study.ARMS]
    files += [q for q in sorted(study.RUN.rglob('*')) if q.is_file() and q.suffix in ('.json','.jsonl','.py','.ps1','.xml') and 'probe' not in q.relative_to(study.RUN).parts]
    files=list(dict.fromkeys(files)); archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},file_count=len(files),archive=study.reference(archive),raw_source_pairs_and_tensors_native_only=True))
    a,b=(review['summaries'][arm] for arm in study.ARMS)
    detail=(f'共通Web6M一度＋同positive2M/armのCE対CE+DPO(beta.1/係数0対.1)と全160個別raw-bound内容を完了。'
        f'CE→DPOでBPB{a["BPB"]:.9f}→{b["BPB"]:.9f}、文法{a["grammar2"]}→{b["grammar2"]}/関連{a["relevance2"]}→{b["relevance2"]}/'
        f'一貫性{a["coherent"]}→{b["coherent"]}/適切{a["appropriate"]}→{b["appropriate"]}/EOS{a["rates"]["eos"]}→{b["rates"]["eos"]}/反復{a["rates"]["repetition"]}→{b["rates"]["repetition"]}（各80）。'
        f'同CEinput/auxiliary全history一致、native10M・Adam/scheduler継承/cursor/quota/固定参照を確認。実新positive10M/各arm8M、総新GPU{review["new_total_GPU_seconds"]:.6f}/1800、'
        f'actual{job["pid"]}完了/不在/元UI復帰。最終Base検証eligible={review["eligible_for_final_Base_validation"]}。'
        '固定56/4565positions約438反復は教材増量ではない。小TRAIN/長さ・作風/固定旧negative/非blind繰り返しdev/旧数値7の限界を保持。'
        '合格recipeのみ独立学習seed/full dev/protected test/adoptionへ。未合格はこの固定両recipe終了、source/beta/coefficient/epoch/LR/decoder/CP救済sweepなし。')
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text('Base専用CE対CE+DPO: 実比較・全160評価完了（2026-10-07 JST）。\n\n'+detail+'\n\nBase未完成・完成時通知して停止。Chat/Dialogue/SFT/量子化なし。元全品質基準/全失敗/Phase0–3維持、WSL uv/local commitのみ/pushなし。以下は過去の履歴。\n\n'+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['Base_preference_completion']=study.reference(destination);atomic_json(q,progress)
    print(dict(status=report['status'],portable_files=len(files),summaries=review['summaries'],eligible=review['eligible_for_final_Base_validation']))


if __name__=='__main__': main()
