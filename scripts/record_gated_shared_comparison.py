"""Persist actual shared-gate Base milestones and portable text evidence."""
import argparse
import json
import os
from pathlib import Path
import sys
import tarfile

os.environ['CUDA_VISIBLE_DEVICES']=''
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import run_gated_shared_comparison as study


def main(phase):
    running=phase=='launch';c=read_json(study.CONFIG) if running else study.inspect()
    destination=ROOT/f'reports/phase6/gated_shared_comparison_{phase}.json'
    if destination.exists():raise ValueError('Preserve original shared-gate milestone')
    report=dict(status='gated_shared_comparison_'+phase,created_at=now(),config=study.reference(study.CONFIG),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],verification_GPU_seconds=c['verification_GPU_seconds'],
        verification_teacher_tokens=c['verification_teacher_tokens'],read_only_probe_context_positions=6272,
        scientific_GPU_seconds=0,new_source_CE_teacher_tokens=0,reused_control_teacher_tokens=100000000,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        quality_criteria_unchanged=True)
    detail=(f'own実CUDA/全state再開/32timingのGPU{c["verification_GPU_seconds"]:.6f}秒を再利用し、専用科学runner・同native評価factory・全80採点/採否経路を実装して凍結。'
        '同mixed親6d/継承native Adam・LR.00001/新13gateのみfresh Adam・LR.0001/WD0、同full CE100Mのcached native対照は再GPUしない。'
        '新CPU1test/0.88秒・PS構文成功。初回CPUはdict対strの不一致でAttributeErrorとなったため、その失敗XMLを保存して新照合関数の型/欠損guardを修正、旧core/source不変。'
        f'科学GPU予測{c["estimated_GPU_seconds_with_margin"]:.6f}秒、ownprobe込み{c["estimated_GPU_seconds_with_margin"]+c["verification_GPU_seconds"]:.6f}/1800、科学未開始。'
        '次は一候補100M実学習→同日本語・dev256・native80/内容→旧相対・絶対・歴史Web基準の採否。')
    if phase!='preparation':
        job=read_json(study.RUN/'job.json')
        if alive(job)!=running:raise ValueError('Actual process/milestone mismatch')
        report.update(actual_job=job,actual_live_process=running,scientific_GPU_seconds=job['GPU_elapsed_seconds'])
        if running:
            report['new_source_CE_teacher_tokens']=job.get('teachers',0)
            detail=(f'科学actual{job["pid"]}/boot{job["boot_id"]}/start{job["start_ticks"]}の実稼働、'
                f'stage{job.get("stage")}/観測教師{job.get("teachers",0)}/100Mを確認。科学GPU上限{c["GPU_budget_seconds"]:.6f}秒。'
                '250更新ごと全state原子的CP、中断時は実PID不在を確認して scripts/run_gated_shared_comparison.ps1 -Worker で再開。'
                '元UIは終端finallyで復帰。学習終端/全日本語/80内容/採否は未完了。')
        elif job['status']=='complete':
            r=read_json(study.RUN/'compare-result.json')
            if r['scientific_teacher_tokens']!=100000000 or not r['all_scientific_input_streams_match'] or r['evaluation_model_class']!='GatedSharedModel':
                raise ValueError('Actual complete matched100M and custom-model evaluation required')
            report.update(result=study.reference(study.RUN/'compare-result.json'),actual_result=r,new_source_CE_teacher_tokens=100000000,
                total_new_GPU_seconds=r['GPU_seconds']+c['verification_GPU_seconds'])
            detail=(f'層共有100M/100532224inputと同日本語192/331/1119・dev256・native greedy80/bridge-retention512eachを実完了、actual{job["pid"]}実不在。'
                f'科学GPU{r["GPU_seconds"]:.6f}秒、ownprobe込み{report["total_new_GPU_seconds"]:.6f}/1800。'
                'cached native100Mと全sampler/教師/input/bytes/digests一致。検証教師1307952とreadonly6272contextは科学と別。'
                '次は全80を個別採点し固定の相対・絶対・歴史Web基準で判定。GPU終端だけでBase完成としない。')
            if phase=='completion':
                review=read_json(study.RUN/'review.json')
                if (review['result_sha256']!=sha256(study.RUN/'compare-result.json') or review['config_sha256']!=sha256(study.CONFIG)
                        or not review['all80_individually_read'] or review['Base_complete'] or review['Base_adopted']):
                    raise ValueError('Actual full raw-bound content review required')
                report.update(review=study.reference(study.RUN/'review.json'),actual_review=review,
                    eligible_for_final_Base_validation=review['eligible_for_final_Base_validation'],
                    notes=study.reference(study.RUN/'content-notes.json'),
                    observations=study.reference(ROOT/'reports/phase6/gated_shared_comparison_observations.tsv'))
                a=review['summaries'][study.ARM];b=review['summaries']['native_CE'];rates=a['rates']
                detail=(f'同親/同full100Mの層共有対cached native比較と全80個別raw-bound採点を完了。BPB{b["BPB"]:.9f}→{a["BPB"]:.9f}、'
                    f'文法{b["grammar2"]}→{a["grammar2"]}/関連{b["relevance2"]}→{a["relevance2"]}/一貫性{b["coherent"]}→{a["coherent"]}/'
                    f'適切{b["appropriate"]}→{a["appropriate"]}/EOS{b["rates"]["eos"]}→{rates["eos"]}/反復{b["rates"]["repetition"]}→{rates["repetition"]}（各80）。'
                    f'事前strong-staged相対gate={review["quality_comparisons"]["strong_staged"]["passed"]}、絶対全gate={all(review["absolute_dev_screen"].values())}、'
                    f'歴史Web全gate={all(review["original_Web"].values())}、最終Base検証eligible={review["eligible_for_final_Base_validation"]}。'
                    f'科学100M/3068updates/100532224input、総新GPU{report["total_new_GPU_seconds"]:.6f}/1800、actual{job["pid"]}実不在/元UI復帰。'
                    'nonblind Codex/一学習seed/反復devを独立人手や確実な一般化の証明としない。合格recipeのみ独立学習seed/full dev/protected test/採用へ。'
                    '未合格の場合は固定gate分岐を終了し、同gate/source/decoder等の救済sweepは行わない。stock HF adapter未対応を完成としない。')
        else:
            if phase=='completion' or job['status']!='failed_or_interrupted':raise ValueError('Actual terminal failure required')
            report['partial']=read_json(study.RUN/'progress-result.json') if (study.RUN/'progress-result.json').exists() else {}
            detail=f'層共有科学actual{job["pid"]}実終端/不在、GPU{job["GPU_elapsed_seconds"]:.6f}秒、理由{job.get("error")}。partial/CP/sourceを保持し、未達を成功へ置換しない。'
    if not running:report['original_UI']=original_UI()
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,Path(__file__),*[ROOT/s for s in study.SOURCES],
        ROOT/'reports/phase6/gated_shared_science_tests.xml',ROOT/'reports/phase6/gated_shared_science_tests_initial_failure.xml']
    if phase=='completion':files += [ROOT/'reports/phase6/gated_shared_comparison_observations.tsv',ROOT/'reports/phase6/gated_shared_comparison_review.json']
    if phase not in ('preparation','launch'):
        files += [p for p in sorted(study.RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml')
                  and 'probe' not in p.relative_to(study.RUN).parts]
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix=('Base専用gated層共有: '+phase+'（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n'+detail+
        '\n\n全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。gateLR/初期値/count/source/CP/decoder救済sweepなし。'
        'WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n')
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['gated_shared_comparison_'+phase]=study.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['scientific_GPU_seconds'],portable_files=len(files))))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('preparation','launch','terminal','completion'));main(p.parse_args().phase)
