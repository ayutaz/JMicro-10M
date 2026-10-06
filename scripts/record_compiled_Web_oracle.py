"""Portable evidence for the one fixed compiled FP32 implementation probe."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import argparse
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import probe_compiled_Web_oracle as study
import run_finite_Web_constraint as old


def main(phase):
    destination=ROOT/f'reports/phase6/compiled_Web_oracle_{phase}.json'
    if destination.exists():raise ValueError('Preserve original compiled milestone')
    c=study.inspect();report=dict(status='readonly_compiled_Web_oracle_'+phase,created_at=now(),config=old.reference(study.CONFIG),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],GPU_seconds=0,previous_related_GPU_seconds=c['previous_related_GPU_seconds'],
        optimizer_updates=0,new_source_CE_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,original_UI=original_UI())
    initial=study.RUN/'unlaunched-setup-v1'
    if initial.exists():
        report['unlaunched_setup_correction']=dict(reason='Separate first no_grad and autograd compiler specializations before steady timings; both warmups stay in real GPU cost.',
            GPU_seconds=0,source=old.reference(initial/'scripts/probe_compiled_Web_oracle.py'),
            config=old.reference(initial/'configs/phase6/compiled_Web_oracle.json'),old_files_preserved=True)
    detail=f"同FP32/micro8/固定TRAIN32/効率Attentionへtorch.compile(fullgraph=True, mode=default, dynamic=False)を一つだけ適用。元親/固定旧masked-stagedの2点で同math NLL2e-6/gradient element絶対2e-6+相対2e-5・global L2相対2e-5/bitwise反復/weights・RNG・grad不変を確認し、4forward+4gradient実timingを測る。初回compileも含む120GPU秒、CPU準備{c['CPU_preparation_seconds']:.6f}秒、新GPU/optimizer0。旧2診断{c['previous_related_GPU_seconds']:.6f}GPU秒も次の2400秒予算へ計数。dtype/backend/mode/packet/CP救済なし。次は実GPU比較を起動、元math厳密受入監査込みの予測と新全stateCUDA gateなしでは本科学を起動しない。"
    if phase=='terminal':
        job=read_json(study.RUN/'job.json')
        if alive(job) or job['status'] not in ('complete','failed'):raise ValueError('Actual terminal job required')
        report.update(actual_job=job,actual_process_absent=True,GPU_seconds=job['GPU_elapsed_seconds'])
        if job['status']=='complete':
            r=read_json(study.RUN/'result.json')
            if not r['passed'] or r['GPU_seconds']!=job['GPU_elapsed_seconds']:raise ValueError('Actual complete result required')
            within=r['estimated_total_with_prior_and_own_probes']<=2400
            report.update(actual_result=r,result=old.reference(study.RUN/'result.json'),planning_within_budget=within)
            next_action=('次は元mathの実NLL受入確認を必須とするcompile候補のtransactional trainerとownCUDA fullstate gate/実timingを実装する。' if within
                else '厳密受入監査を保つ計画でも40分予算を超えるため、本科学を凍結/起動しない。compile/mode/dtype等の救済sweepなし、次はこの実費用を根拠に別のBase改善機構を定義する。')
            detail=f"readonly compiled FP32診断が実完了、actual{job['pid']}終端/実不在。GPU{r['GPU_seconds']:.6f}秒/120、optimizer/新source学習0。両固定点で元math NLL/勾配・bitwise反復/weights・RNG/grad不変合格。max forward{r['maximum_compiled_forward_seconds']:.6f}/gradient{r['maximum_compiled_gradient_seconds']:.6f}秒。元math受入監査一回/各更新と初回compile余裕を含む科学予測{r['estimated_science_with_original_math_acceptance_seconds']:.6f}秒、旧2診断/ownprobe込み{r['estimated_total_with_prior_and_own_probes']:.6f}秒/2400。これは計画で、owntransactional CUDA gateや将来全重みparity/品質/完成の証明ではない。{next_action}"
        else:
            partial=read_json(study.RUN/'progress-result.json') if (study.RUN/'progress-result.json').exists() else {}
            report.update(partial_result=partial,diagnostic_failed=True)
            detail=f"readonly compiled FP32診断はactual{job['pid']}終端/実不在、GPU{job['GPU_elapsed_seconds']:.6f}秒/120。実失敗{job.get('error')}を原source/完了partialと保持。optimizer/新source学習0、本科学/採用なし。mode/dtype/backend/CP救済sweepをせず、次はこの実失敗から別Base改善機構を定義する。"
    report['completion_scope']='Readonly implementation evidence, not qualified Base/adoption.'
    atomic_json(destination,report)
    files=[destination,study.CONFIG,Path(__file__),*[ROOT/s for s in study.SOURCES]]
    if initial.exists():files.extend(p for p in sorted(initial.rglob('*')) if p.is_file())
    if phase=='terminal':files.extend(p for p in sorted(study.RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml'))
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files},
        file_count=len(files),archive=old.reference(archive),tensors_native_only=True))
    prefix=f"Base専用compiled oracle: {phase}（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n{detail}\n\n[PyTorch公式compile仕様](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)を参照し、当固定FP32計算の数値/時間は実測で判定。元10B UI復帰、全旧失敗/数値7/Phase0–3/相対・絶対・歴史Web品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。以下は過去の履歴。\n\n"
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['compiled_Web_oracle_'+phase]=old.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)),ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('preparation','terminal'));main(p.parse_args().phase)
