"""Portable bounded sharing evidence; CPU/probe are not Base completion."""
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
import probe_gated_shared_comparison as study


def main(phase):
    c=study.inspect();p=read_json(study.PROPOSAL)
    destination=ROOT/f'reports/phase6/gated_shared_{phase}.json'
    if destination.exists():raise ValueError('Preserve original sharing milestone')
    report=dict(status='gated_shared_'+phase,created_at=now(),config=study.reference(study.CONFIG),proposal=study.reference(study.PROPOSAL),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],GPU_seconds=0,scientific_teacher_tokens=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        unique_parameters=10001165,unique_blocks=13,logical_invocations=26,quality_criteria_unchanged=True,original_UI=original_UI())
    detail=('KL/full・nonEOS/金body復習/positive anchor/Fisherの不採用を確認し、未実装の層共有を別機構として定義。'
        '同13 unique blockに追加の共有呼出を挟み、追加attention/MLP residualの同一scalarを0初期化して元関数を保つ。'
        '重み10,001,152→10,001,165（新13gate/1tensor）、logical26、tied/独立26KV/cache/causality/native save/load。'
        'CPU4tests/2.07秒でゼロ時の元logits・重みobject/梯度/RNG一致、非ゼロsigned gateのragged/chunk/未来非参照、'
        'native Adam継承/新gate group/全state4対2+2を確認。random tiny fixtureで品質の証明ではない。'
        f'実CPU proposal{p["preparation_CPU_seconds"]:.6f}秒、probe準備{c["CPU_preparation_seconds"]:.6f}秒、新GPU/科学0。'
        '比較はsame mixed親/継承native Adam・LR.00001/source/full100M CEとcached matched_staged_CE、'
        '追加gateのみfresh Adam・LR.0001/WD0固定。計算/KVが増え、stock HF adapterは未対応で完成としない。'
        '次はown native FP32/BF16 zero-gate32/1024、signed full/cache1024とCUDA4対2+2/32timing/batch32を120秒内で測る。'
        '1.3margin+300秒評価+ownprobeが1800内の場合のみ科学runnerを実装・凍結して100M一候補へ。')
    if phase!='preparation':
        job=read_json(study.RUN/'probe/job.json')
        if alive(job) or job['status'] not in ('complete','failed_or_interrupted'):raise ValueError('Actual terminal absent probe required')
        report.update(actual_job=job,GPU_seconds=job['GPU_elapsed_seconds'])
        if job['status']=='complete':
            r=read_json(study.RUN/'probe/result.json');timing,estimate=study.estimate_training(r)
            if (not r['passed'] or not all(r['initial_fullstate_preservation'].values()) or not all(r['resume_gate']['checks'].values())
                    or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120
                    or r['config_sha256']!=sha256(study.CONFIG) or any(not v['passed'] for v in r['architecture']['checks'].values())):
                raise ValueError('Actual fixed numerical/initial/resume/timing evidence required')
            report.update(result=study.reference(study.RUN/'probe/result.json'),actual_result=r,
                estimated_science_GPU_seconds=estimate,estimated_total_GPU_seconds=estimate+r['GPU_seconds'],
                science_cost_within1800=estimate+r['GPU_seconds']<=1800)
            detail=(f'actual{job["pid"]}は実完了/不在、probeGPU{r["GPU_seconds"]:.6f}秒/120。'
                f'zero-gate native FP32/BF16の32/1024とsigned gate full/cache1024、native重み/RNG不変・logical26KVに合格。'
                f'初期native W/Adam・scheduler/RNG/Webcursor継承/新gateのみfresh、own CUDA4連続対2+2全state/history・finite/固定nativeLR.00001/newgate.0001、'
                f'32timing完了。40検証更新/{r["verification_teacher_tokens"]}教師/11readonly forward6272contextは科学から除外。'
                f'ピークVRAM{r["timing"]["peak_VRAM_bytes"]/1024**3:.3f}GiB、科学予測{estimate:.6f}秒、ownprobe込み{estimate+r["GPU_seconds"]:.6f}/1800。'
                'これは初期構造と再開/実費用の証明で、日本語品質/容量原因/完成の証明ではない。'
                '次は予算内のみ専用科学runnerと全80reviewを実装、同full100M native対照を再GPUせず比較する。')
        else:
            detail=(f'共有probe actual{job["pid"]}は実終端/不在、GPU{job["GPU_elapsed_seconds"]:.6f}秒/120、理由{job.get("error")}。'
                '原source/partial/失敗を保持、本科学0、数値/予算を緩和せず、同じgate設定等の救済sweepなし。次は実原因に対する限定修復または別機構の定義。')
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,Path(__file__),ROOT/'reports/phase6/gated_shared_tests.xml',*[ROOT/s for s in study.SOURCES]]
    if phase!='preparation':files += [q for q in sorted((study.RUN/'probe').rglob('*')) if q.is_file() and q.suffix in ('.json','.jsonl','.py','.ps1','.xml')]
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix=('Base専用gated層共有: '+phase+'（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n'+detail+
        '\n\n[MobileLLM](https://arxiv.org/abs/2402.14905)の即時block sharingと[ReZero](https://arxiv.org/abs/2003.04887)の0初期gateを参考にした独自の転移仮説。'
        '公開論文の正確な再現や日本語10Mでの改善を主張しない。全旧失敗/数値7/Phase0–3/旧品質基準保持、'
        'gateLR/初期値/count/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n')
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text(prefix+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['gated_shared_'+phase]=study.reference(destination);atomic_json(q,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files))))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('phase',choices=('preparation','probe','probe_failure'));main(parser.parse_args().phase)
