"""Actual durable one-candidate milestones; never automatic Base adoption."""
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
import run_fisher_parameter_anchor as study


def main(phase):
    running=phase=='launch';scientific=phase in ('launch','terminal','completion')
    config=study.CONFIG if scientific else study.PROBE_CONFIG
    c=read_json(config) if running else study.inspect(config)
    folder=study.RUN if scientific else study.RUN/'probe'
    destination=ROOT/f'reports/phase6/fisher_parameter_anchor_{phase}.json'
    if destination.exists():raise ValueError('Preserve original Fisher milestone')
    report=dict(status='Fisher_parameter_anchor_'+phase,created_at=now(),config=study.reference(config),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],field_GPU_seconds=c['field_GPU_seconds'],
        own_job_GPU_seconds=0,new_source_CE_teacher_tokens=0,reused_control_teacher_tokens=100000000,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        quality_criteria_unchanged=True)
    detail=('同mixed親6d/継承Adam・RNG/scheduler・LR.00001/同full CE100M/Web75M-story5M-ordinary10M-conditional10M/'
        'lambda.04161064039180984、差分は固定mean1 Fisher fieldのみ。既存一律L2対照100M/全80/日本語/devを再利用、再GPUなし。'
        f'field実{c["field_GPU_seconds"]:.6f}秒/64MC score gradient・65276sampled labelはsource CEと別。'
        f'新CPU予算1test/1.47秒・PS構文合格、CPU準備{c["CPU_preparation_seconds"]:.6f}秒、本学習0。'
        '次はownCUDA4対2+2全state/history/固定field・anchor/継承状態と32timingを120秒内で測定。'
        'field+probe+本科学+評価を実測margin付き1800秒内の場合のみ科学凍結、同eval/旧全gateを保持。')
    if phase!='preparation':
        job=read_json(folder/'job.json')
        if alive(job)!=running:raise ValueError('Actual process/milestone mismatch')
        report.update(actual_job=job,actual_live_process=running,own_job_GPU_seconds=job['GPU_elapsed_seconds'])
        if phase=='probe':
            r=study.probe_evidence();timings,estimate=study.estimate_training(r)
            total=estimate+r['GPU_seconds']+c['field_GPU_seconds']
            report.update(actual_probe=r,estimated_science_GPU_seconds=estimate,estimated_total_GPU_seconds=total,
                planning_within_budget=total<=1800,result=study.reference(folder/'result.json'))
            detail=(f'ownCUDA4連続対2+2の全state/history/有限値/LR/親Adam・scheduler・RNG/Webcursor・anchor/fieldに合格、32timing完了。'
                f'実40検証更新/{r["verification_teacher_tokens"]}教師は科学と別、ownprobe{r["GPU_seconds"]:.6f}秒/120。'
                f'1.3margin・200秒非学習余裕付き科学予測{estimate:.6f}秒、field+probe込み{total:.6f}/1800。'
                '次は予算内のみ同full100M一候補/同日本語・dev256・native80/旧全gate採否へ。GPUgateは品質の証明ではない。')
        elif running:
            report['new_source_CE_teacher_tokens']=job.get('teachers',0)
            detail=(f'科学actual{job["pid"]}/boot{job["boot_id"]}/start{job["start_ticks"]}の実稼働を確認、'
                f'stage{job.get("stage")}/観測教師{job.get("teachers",0)}/100M。科学GPU上限{c["GPU_budget_seconds"]:.6f}秒。'
                '250更新ごと全state原子的CP、実PID不在後 scripts/run_fisher_parameter_anchor.ps1 -Mode Train -Worker で再開。'
                '終端・全日本語/80内容採否は未完了、元UIは終端finallyで復帰。')
        elif job['status']=='complete':
            r=read_json(folder/'compare-result.json')
            if r['scientific_teacher_tokens']!=100000000 or not r['all_scientific_input_streams_match']:
                raise ValueError('Actual full matched100M result required')
            report.update(actual_result=r,result=study.reference(folder/'compare-result.json'),new_source_CE_teacher_tokens=100000000,
                total_new_GPU_seconds=r['GPU_seconds']+c['verification_GPU_seconds']+c['field_GPU_seconds'])
            detail=(f'同full100M教師のFisher候補と日本語192/331/1119・dev256・native greedy80/bridge-retention実評価完了、'
                f'actual{job["pid"]}実不在。科学GPU{r["GPU_seconds"]:.6f}秒、field+ownprobe込み{report["total_new_GPU_seconds"]:.6f}/1800。'
                'cached uniform100Mとsource/targets/全sampler/teacher/input/bytes/digestsが一致、総計へfield sampled labelsや検証教師を混ぜない。'
                '次は新全80の個別raw-bound内容と旧uniform/強いstaged相対・絶対・歴史Web1%gate採否。'
                '合格のみ独立学習seed/full dev/protected test/採用へ、GPU終端だけでBase完成としない。')
            if phase=='completion':
                review=read_json(study.RUN/'review.json')
                if (review['result_sha256']!=sha256(folder/'compare-result.json') or review['config_sha256']!=sha256(config)
                        or not review['all80_individually_read'] or review['Base_complete'] or review['Base_adopted']):
                    raise ValueError('Actual all80 bounded review required')
                report.update(review=study.reference(study.RUN/'review.json'),actual_review=review,
                    eligible_for_final_Base_validation=review['eligible_for_final_Base_validation'],
                    notes=study.reference(study.RUN/'content-notes.json'),
                    observations=study.reference(ROOT/'reports/phase6/fisher_parameter_anchor_observations.tsv'))
                a=review['summaries']['fisher_anchor'];b=review['summaries']['uniform_anchor']
                detail=(f'同親/継承Adam・LR/全source full100MのFisher対cached uniform比較と新全80個別採点・36exact旧raw採点継承を完了。'
                    f'candidate BPB{a["BPB"]:.9f}（uniform{b["BPB"]:.9f}）、文法{b["grammar2"]}→{a["grammar2"]}/関連{b["relevance2"]}→{a["relevance2"]}/'
                    f'一貫性{b["coherent"]}→{a["coherent"]}/適切{b["appropriate"]}→{a["appropriate"]}/EOS{b["rates"]["eos"]}→{a["rates"]["eos"]}/'
                    f'反復{b["rates"]["repetition"]}→{a["rates"]["repetition"]}（各80）。'
                    f'絶対screen全合格だが、強いstaged23に対し一貫性28/+5<8、EOS65<76/反復7>2、歴史WebBPB上限.9812859519も超過。'
                    f'最終Base検証eligible={review["eligible_for_final_Base_validation"]}、不採用を保持。'
                    f'科学100M/100532224input、検証{c["verification_teacher_tokens"]}教師・field65276model-sampled label別、'
                    f'総新GPU{report["total_new_GPU_seconds"]:.6f}秒/1800、actual{job["pid"]}実不在/元UI復帰。'
                    '日本語意味・構文・常識の微差とnonblind内容採点は独立改善の証明ではない。'
                    '固定field/lambda等分岐終了、独立seed/full dev/protected test/採用なし。次は既存結果を根拠に残るEOS/反復と保持の別機構を定義、'
                    '同field等の救済sweep/対照再GPU/全量scanはしない。')
        else:
            if job['status']!='failed_or_interrupted':raise ValueError('Actual terminal failure required')
            report['partial']=read_json(folder/'progress-result.json') if (folder/'progress-result.json').exists() else {}
            detail=f'Fisher actual{job["pid"]}は実終端/不在、GPU{job["GPU_elapsed_seconds"]:.6f}秒、理由{job.get("error")}。partial/CP/sourceを保持、未達を合格へ置換せず、無制限再試行なし。'
    if not running:report['original_UI']=original_UI()
    atomic_json(destination,report)
    files=[destination,config,study.PROPOSAL,ROOT/'reports/phase6/fisher_parameter_budget_tests.xml',Path(__file__),*[ROOT/s for s in study.SOURCES]]
    if phase=='completion':files += [ROOT/'scripts/review_fisher_parameter_anchor.py',ROOT/'scripts/record_fisher_parameter_content.py',
        ROOT/'reports/phase6/fisher_parameter_anchor_observations.tsv',ROOT/'reports/phase6/fisher_parameter_anchor_review.json']
    if phase not in ('preparation','launch'):
        files += [p for p in sorted(folder.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml')
                  and (not scientific or 'field' not in p.relative_to(folder).parts and 'probe' not in p.relative_to(folder).parts)]
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix=('Base専用Fisher anchor: '+phase+'（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n'+detail+
        '\n\n全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。field/seed/回数/lambda/source/mask/CP/decoder救済sweepなし。'
        'WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n')
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['fisher_parameter_anchor_'+phase]=study.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['own_job_GPU_seconds'],portable_files=len(files))))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=('preparation','probe','launch','terminal','completion','probe_failure'));main(parser.parse_args().phase)
