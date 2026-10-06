"""Persist actual news Base milestones, generated output and portable text."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import run_livedoor_base as study


def main(phase):
    running=phase=='launch'; c=read_json(study.CONFIG) if running else study.inspect()
    job=read_json(study.RUN/'job.json')
    if alive(job) != running or job['config_sha256'] != sha256(study.CONFIG): raise ValueError('Actual process/config milestone mismatch')
    destination=ROOT/f'reports/phase6/livedoor_base_comparison_{phase}.json'
    if destination.exists(): raise ValueError('Preserve original news milestone')
    report=dict(status='livedoor_base_comparison_'+phase, created_at=now(), config=study.reference(study.CONFIG), actual_job=job,
        actual_live_process=running, scientific_GPU_seconds=job['GPU_elapsed_seconds'], verification_GPU_seconds=c['verification_GPU_seconds'],
        verification_teacher_tokens=c['verification_teacher_tokens'], observed_new_teacher_tokens=job.get('teachers',0),
        reused_prefix_teacher_tokens=study.REUSED, Base_complete=False, Base_adopted=False, Chat_started=False,
        quantization_started=False, protected_test_used=False, quality_criteria_unchanged=True)
    detail=(f'科学actual{job["pid"]}/boot{job["boot_id"]}/start{job["start_ticks"]}の実稼働、stage{job.get("stage")}/'
        f'観測新教師{job.get("teachers",0)}/{study.TOTAL}を確認。科学GPU上限{c["GPU_budget_seconds"]:.6f}秒。'
        f'共通Web{study.REUSED}教師は再GPUしない。250更新ごと全state原子的CP、中断時は実PID不在を確認して scripts/run_livedoor_base.ps1 -Worker で再開。'
        '元UIは終端finallyで復帰。学習終端/全日本語/80内容/採否は未完了。')
    if not running:
        report['original_UI']=original_UI()
        if job['status']=='complete':
            r=read_json(study.RUN/'compare-result.json')
            if (r['GPU_seconds'] != job['GPU_elapsed_seconds'] or r['scientific_teacher_tokens'] != study.TOTAL
                    or r['reused_prefix_teacher_tokens'] != study.REUSED or r['total_teacher_tokens_from_original_parent'] != 100000000
                    or r['evaluation_model_class'] != 'JMicroModel' or r['exact_same_scientific_sources_as_control']):
                raise ValueError('Actual native news source/teacher accounting required')
            report.update(result=study.reference(study.RUN/'compare-result.json'), actual_result=r,
                observed_new_teacher_tokens=study.TOTAL, total_new_GPU_seconds=r['GPU_seconds']+c['verification_GPU_seconds'])
            detail=(f'共通Web{study.REUSED}を再利用して残{study.TOTAL}新教師・原親から全100Mを実完了。'
                f'同日本語192/331/1119・dev256・native greedy80/bridge-retention512each、科学GPU{r["GPU_seconds"]:.6f}秒、'
                f'ownprobe/旧失敗込み{report["total_new_GPU_seconds"]:.6f}/1800、actual{job["pid"]}実不在/元UI復帰。'
                '次は全80を個別採点して固定品質条件へ。GPU終端だけでBase完成としない。')
            if phase=='completion':
                review=read_json(study.RUN/'review.json')
                if (review['result_sha256'] != sha256(study.RUN/'compare-result.json') or review['config_sha256'] != sha256(study.CONFIG)
                        or not review['all80_individually_read'] or review['Base_complete'] or review['Base_adopted']):
                    raise ValueError('Actual all80 raw-bound original content review required')
                report.update(review=study.reference(study.RUN/'review.json'), actual_review=review,
                    eligible_for_final_Base_validation=review['eligible_for_final_Base_validation'],
                    notes=study.reference(study.RUN/'content-notes.json'), observations=study.reference(ROOT/'reports/phase6/livedoor_base_comparison_observations.tsv'))
                a=review['summaries'][study.ARM]; b=review['summaries']['strong_staged']; rates=a['rates']
                detail=(f'ニュース条件と全80個別raw-bound採点を完了。旧staged対照→newsでBPB{b["BPB"]:.9f}→{a["BPB"]:.9f}、'
                    f'文法{b["grammar2"]}→{a["grammar2"]}/関連{b["relevance2"]}→{a["relevance2"]}/一貫性{b["coherent"]}→{a["coherent"]}/'
                    f'適切{b["appropriate"]}→{a["appropriate"]}/EOS{b["rates"]["eos"]}→{rates["eos"]}/反復{b["rates"]["repetition"]}→{rates["repetition"]}（各80）。'
                    f'相対gate={review["quality_comparison"]["passed"]}/絶対全gate={all(review["absolute_dev_screen"].values())}/歴史Web全gate={all(review["original_Web"].values())}/'
                    f'最終Base検証eligible={review["eligible_for_final_Base_validation"]}。科学新{study.TOTAL}/再利用{study.REUSED}教師、'
                    f'総新GPU{report["total_new_GPU_seconds"]:.6f}/1800。実native10M・継承Adam/scheduler・同Web継続と全会計を確認、元UI復帰。'
                    'source/EOS/多様性・input/update数が変わる比較、523883本文tokensの約47.265反復を新規教材量としない。'
                    '一学習seed/非blind反復dev・独立人手なし。合格recipeのみ独立学習seed/full dev/protected test/採用へ。未合格なら固定news分岐を終了しsource/epoch/LR/decoder/CP救済sweepなし。')
        else:
            if phase=='completion' or job['status']!='failed_or_interrupted': raise ValueError('Actual terminal failure required')
            detail=f'news科学actual{job["pid"]}実終端/不在、GPU{job["GPU_elapsed_seconds"]:.6f}秒、理由{job.get("error")}。全partial/CP/元source保持、未達を成功としない。'
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,Path(__file__),*[ROOT/s for s in study.SOURCES], ROOT/'reports/phase6/livedoor_base_science_tests.xml']
    if phase=='completion': files += [ROOT/'reports/phase6/livedoor_base_comparison_observations.tsv',ROOT/'reports/phase6/livedoor_base_comparison_review.json']
    if not running:
        files += [q for q in sorted(study.RUN.rglob('*')) if q.is_file() and q.suffix in ('.json','.jsonl','.py','.ps1','.xml') and 'probe' not in q.relative_to(study.RUN).parts]
    files=list(dict.fromkeys(files)); archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files: output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'), dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix=('Base専用ニュース比較: '+phase+'（2026-10-06 JST）。\n\n'+detail+
        '\n\nBase未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。元相対・絶対・歴史Web1%品質基準/全旧失敗/数値7/Phase0–3維持。WSL uv/local commitのみ/pushなし。以下は過去の履歴。\n\n')
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative; q.write_text(prefix+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json'; progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['livedoor_base_comparison_'+phase]=study.reference(destination);atomic_json(q,progress)
    print(dict(status=report['status'],GPU_seconds=report['scientific_GPU_seconds'],portable_files=len(files)))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('launch','terminal','completion'));main(p.parse_args().phase)
