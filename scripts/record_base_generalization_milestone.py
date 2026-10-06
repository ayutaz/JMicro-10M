"""Actual source-local readonly milestones and immutable portable evidence."""
import argparse
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import diagnose_base_generalization as study


def main(phase):
    c=read_json(study.CONFIG) if phase=='launch' else study.inspect()
    destination=ROOT/f'reports/phase6/base_generalization_{phase}.json'
    if destination.exists():raise ValueError('Preserve original actual source-local milestone')
    report=dict(status='source_local_Base_generalization_'+phase,created_at=now(),config=study.reference(study.CONFIG),
        optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
    detail=(f'既存archiveからDEV374のみ本文をdecode、TRAIN6617/TEST376はheaderだけ。元同paragraph/token長/localDEV同文重複除去でeligible278→固定seed20261007の64、選別結果でrerollなし。'
        f'CPU{c["CPU_preparation_seconds"]:.6f}秒/30、TRAIN56対DEV64/先頭16各4モデルの同CE-mask/本文byte BPB/greedy64。'
        f'local article-family overlap0、DEV同文overlap curated56={c["DEV_exact_text_overlap_with_selected56"]}/旧news5050={c["DEV_exact_text_overlap_with_news5050"]}、oldWebglobal overlap未保証。'
        'CPU3tests/1.39秒でDEV固定draw・TRAIN/TEST不正byte未decode、quarter prefix UTF8境界だけ進行、単一shift/promptPAD除外・EOS CEとbody BPB分母を確認。'
        '四つの固定原親/共通6M/CE/DPO終端・設定/source/checkpointを凍結、GPU上限120秒/追加学習0。次は永続readonly→全64個別内容→小教材記憶と同source転移の事前定義flag、診断だけでBase完成としない。')
    if phase=='prepared':report['original_UI']=original_UI()
    else:
        job=read_json(study.RUN/'job.json');live=alive(job)
        if phase=='launch':
            if not live or job['status']!='running' or job['config_sha256']!=sha256(study.CONFIG):raise ValueError('Actual live frozen readonly diagnostic required')
            report.update(actual_job=job,actual_live_process=True)
            detail=(f'実diagnostic actual{job["pid"]}/boot{job["boot_id"]}/start{job["start_ticks"]}稼働、stage{job["stage"]}/GPU{job["GPU_elapsed_seconds"]:.3f}秒。'
                '各尤度batchと生成caseを永続保存、上限120秒、更新0。元UIはfinally復帰。重複起動なし・終端oneshotは同一再試行せず保存。次は全64個別内容・readonly/原SHA/flagを確認して診断終了。')
        else:
            r=read_json(study.RUN/'result.json');review=read_json(study.RUN/'review.json')
            if live or job['status']!='complete' or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or not review['all64_individually_read'] or review['result']!=study.reference(study.RUN/'result.json'):
                raise ValueError('Actually terminal absent/read-only/all64-content evidence required')
            report.update(actual_job=job,GPU_seconds=r['GPU_seconds'],result=study.reference(study.RUN/'result.json'),
                review=study.reference(study.RUN/'review.json'),actual_review=review,original_UI=original_UI())
            summaries=review['summaries'];b=summaries['actual_shared_Web6M'];a=summaries['chosen_CE_terminal'];d=summaries['chosen_CE_DPO_terminal']
            detail=(f'実4CP・TRAIN56/DEV64の同mask共通bytes/全64個別DEV生成をGPU{r["GPU_seconds"]:.6f}秒/120で完了、actual{job["pid"]}不在・元UI復帰。'
                f'共通→CE→DPO: TRAIN completion CE{b["train"]["completion_CE_nats"]:.6f}→{a["train"]["completion_CE_nats"]:.6f}→{d["train"]["completion_CE_nats"]:.6f}、'
                f'DEV body BPB{b["dev"]["body_BPB"]:.6f}→{a["dev"]["body_BPB"]:.6f}→{d["dev"]["body_BPB"]:.6f}、'
                f'DEV一貫性{b["coherent"]}→{a["coherent"]}→{d["coherent"]}/16、事前flag={review["diagnostic_flags"]}。'
                '全4weights/parentSHA/RNG不変・eval・gradなし、学習更新/科学教師0、TEST0。小sample/非blind/oldWeboverlap未保証/旧数値7を保持、単独原因や10M容量不足の証明にしない。'
                'このreadonly診断を終了。旧固定CE/DPOrecipe不採用と全基準を維持し、実TRAIN/DEV転移証拠から新しい機構の比較を定義する。source/coefficient/epoch/LR/CP救済なし。')
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PLAN,Path(__file__),*[ROOT/s for s in study.SOURCES],ROOT/'reports/phase6/base_generalization_tests.xml']
    if phase=='complete':files += [q for q in sorted(study.RUN.rglob('*')) if q.is_file() and q.suffix in ('.json','.jsonl','.py','.ps1','.xml')]
    if phase=='complete':files += [ROOT/f'reports/phase6/base_generalization_{arm}_observations.tsv' for arm in study.ARMS]+[ROOT/'reports/phase6/base_generalization_diagnostic_review.json']
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},file_count=len(files),archive=study.reference(archive),original_archive_full_gold_cases_and_tensors_native_only=True))
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text('Base同source一般化diagnostic: '+phase+'（2026-10-07 JST）。\n\n'+detail+'\n\nBase未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。元全品質基準/失敗/Phase0–3保持、WSL uv/local commitのみ/pushなし。以下は過去の履歴。\n\n'+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['Base_generalization_'+phase]=study.reference(destination);atomic_json(q,progress)
    print(dict(status=report['status'],portable_files=len(files),GPU_seconds=report.get('GPU_seconds',0)))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('prepared','launch','complete'));main(p.parse_args().phase)
