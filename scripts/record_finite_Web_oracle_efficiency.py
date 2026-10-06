"""Record readonly speed/parity evidence and Base-only scope."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import argparse
import json
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import probe_finite_Web_oracle_efficiency as study
import run_finite_Web_constraint as old


def main(phase):
    destination=ROOT/f'reports/phase6/finite_Web_oracle_efficiency_{phase}.json'
    if destination.exists():raise ValueError('Preserve original efficiency milestone')
    c=study.inspect();report=dict(status='readonly_oracle_efficiency_'+phase,created_at=now(),config=old.reference(study.CONFIG),
        original_UI=original_UI(),CPU_preparation_seconds=c['CPU_preparation_seconds'],GPU_seconds=0,optimizer_updates=0,
        new_source_CE_teacher_tokens=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True)
    detail=f"固定TRAIN32 Web窓・同FP32/autocastなし/TF32なし/micro8/全body教師と分母を保ち、Attention backendのみMATH対EFFICIENT_ATTENTIONを比較するreadonly60GPU秒診断。元10.5B親と固定旧masked-staged終端の2点。事前NLL絶対2e-6、各gradient絶対2e-6+相対2e-5/global L2相対2e-5、candidate反復bitwise/weights・RNG・grad不変を要し、4forward+4gradient実timingを両方式/両点で測る。CPU準備{c['CPU_preparation_seconds']:.6f}秒、新GPU/optimizer0。実装最適化は旧40分予算超過を受けた一案で、packet/dtype/制約/品質救済sweepなし。次はこのownGPU診断を実行、失敗なら同backendの無制限再試行なし。"
    if phase=='terminal':
        job=read_json(study.RUN/'job.json')
        if alive(job) or job['status'] not in ('complete','failed'):raise ValueError('Actual terminal process required')
        report.update(actual_job=job,actual_process_absent=True,GPU_seconds=job['GPU_elapsed_seconds'])
        if job['status']=='complete':
            r=read_json(study.RUN/'result.json')
            if r['GPU_seconds']!=job['GPU_elapsed_seconds'] or not r['passed']:raise ValueError('Completed actual result required')
            report.update(result=old.reference(study.RUN/'result.json'),actual_result=r)
            points={key:dict(NLL_absolute_error=p['NLL_absolute_error'],gradient_global_relative_L2=p['gradient_parity']['global_relative_L2']) for key,p in r['checkpoints'].items()}
            detail=f"FP32 efficient Attentionのreadonly実GPU診断を完了、actual{job['pid']}終端/実不在。GPU{r['GPU_seconds']:.6f}秒/60、optimizer/新source学習0。両固定点のNLL/勾配/bitwise反復/weights・RNG・grad不変に合格: {json.dumps(points)}。max forward{r['maximum_fast_forward_seconds']:.6f}/gradient{r['maximum_fast_gradient_seconds']:.6f}秒。source timing再利用の計画上科学予測{r['illustrative_optimized_science_estimate_seconds']:.6f}秒は元mathの厳密受入監査・新全stateCUDA gate費用を含まず、科学起動許可/将来全重みparity/held-out品質ではない。次はこの実速度を使い、元math実損失の受入確認を維持する最適化trainer/owned CUDA gateの有限計画を定義する。"
        else:
            partial=read_json(study.RUN/'progress-result.json') if (study.RUN/'progress-result.json').exists() else {}
            report.update(partial_result=partial,diagnostic_failed=True)
            detail=f"readonly FP32 efficient Attention診断はactual{job['pid']}終端/実不在、GPU{job['GPU_elapsed_seconds']:.6f}秒/60。実失敗{job.get('error')}、完了済みrawを保持。新optimizer/source学習0・本科学なし・Base未完成。別backend/dtype/packetへ自動変更せず、次は実失敗から計算方式/別改善を定義する。"
    report['completion_scope']='Implementation diagnostic, not Base quality/adoption.'
    atomic_json(destination,report)
    files=[destination,study.CONFIG,Path(__file__),*[ROOT/s for s in study.SOURCES]]
    if phase=='terminal':files.extend(p for p in sorted(study.RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml'))
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=old.sha256(p)) for p in files},
        file_count=len(files),archive=old.reference(archive),tensors_native_only=True))
    prefix=f"Base専用oracle高速化: {phase}（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n{detail}\n\n[PyTorch一次資料](https://pytorch.org/blog/accelerating-large-language-models/)がFP32のmemory efficient Attentionを説明するが、当10M/4090の速度や精度はこの実測で判定。旧math科学上限拒否/数値7/全不採用/Phase0–3と旧全品質基準を保持。合格recipeのみ独立学習seed/full dev/protected test/採用。元10B UI復帰、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n"
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['finite_Web_oracle_efficiency_'+phase]=old.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files)),ensure_ascii=False))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('preparation','terminal'));main(p.parse_args().phase)
