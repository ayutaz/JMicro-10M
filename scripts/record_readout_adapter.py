"""Portable CPU/actual CUDA milestones, with unchanged Base stop boundary."""
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
import probe_readout_adapter as study


def main(phase):
    c=study.inspect();p=read_json(study.PROPOSAL);destination=ROOT/f'reports/phase6/readout_adapter_{phase}.json'
    if destination.exists():raise ValueError('Preserve original readout milestone')
    previous=c.get('previous_failed_GPU_seconds',0.)
    report=dict(status='readout_adapter_'+phase,created_at=now(),config=study.reference(study.CONFIG),proposal=study.reference(study.PROPOSAL),
        previous_failed_GPU_seconds=previous,repair=c.get('repair'),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],GPU_seconds=0,scientific_teacher_tokens=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        unique_parameters=10099456,trainable_parameters=98304,quality_criteria_unchanged=True,original_UI=original_UI())
    detail=('前の層共有100Mは全gate未達・不採用のまま。元d18 greedy80の固定64token pathをCPU0.059142秒で再利用し、終了判定だけの非EOS順序不変/CE二値勾配一致をCPU2tests/0.90秒で確認。'
        '人手の第一可用prefix62件・文法54/一貫性36、文法56のfeasibility marker未達。nonblind・事後・非全停止位置の診断で、全EOS法やモデル容量の不可能性を主張しない。'
        '次は同mixed親6dに一つのpostnorm256→192→256/biasなしSiLU/zero-up readoutを追加。元119/10,001,152重みは全凍結、新2tensor/98,304のみfresh Adam・LR.0001/WD0、合計10,099,456。'
        'native tied/13KVを保ち、本文の語選択とEOSを変えられるがWeb保持は保証しない。旧rank4全層linear融合とは異なる非線形final readoutを一条件として定義。'
        'CPU3tests/2.06秒で初期native出力/重みobject/独立RNG/新梯度のみ、nonzero ragged/cache/未来非参照/labels/native saveとfresh2Adam4対2+2全state/historyに合格。'
        f'CPU proposal{p["preparation_CPU_seconds"]:.6f}秒・probe準備{c["CPU_preparation_seconds"]:.6f}秒、新GPU/科学0。'
        '次はown native FP32/BF16 identity32/1024・nonzero cache1024・CUDA全state再開/32timingを120秒内で測る。1.3margin+300秒評価+ownprobeが900内の場合だけ専用科学runner/全80採否を実装・凍結し同full100Mへ。')
    if phase!='preparation':
        job=read_json(study.RUN/'probe/job.json')
        if alive(job) or job['status'] not in ('complete','failed_or_interrupted'):raise ValueError('Actually terminal/absent probe required')
        report.update(actual_job=job,GPU_seconds=job['GPU_elapsed_seconds'])
        if job['status']=='complete':
            r=read_json(study.RUN/'probe/result.json');timing,estimate=study.estimate_training(r)
            if (not r['passed'] or not all(r['initial_preservation'].values()) or not all(r['resume_gate']['checks'].values())
                    or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120
                    or r['config_sha256']!=sha256(study.CONFIG) or any(not v['passed'] for v in r['architecture']['checks'].values())):
                raise ValueError('Own actual numeric/frozen/fresh readout/restart evidence required')
            report.update(result=study.reference(study.RUN/'probe/result.json'),actual_result=r,estimated_science_GPU_seconds=estimate,
                estimated_total_GPU_seconds=estimate+r['GPU_seconds']+previous,science_cost_within900=estimate+r['GPU_seconds']+previous<=900)
            detail=(f'actual{job["pid"]}実完了/不在、ownCUDA probe{r["GPU_seconds"]:.6f}秒/120。初期FP32/BF16 native32/1024・nonzero full/cache1024とnative119重み凍結/RNG/13KV、'
                f'fresh readout-only Adam/fixedLR.0001・連続4対2+2全state/history/finiteと32timingに合格。40検証更新/{r["verification_teacher_tokens"]}教師/11readonly forward6272contextは科学へ混ぜない。'
                f'ピークVRAM{r["timing"]["peak_VRAM_bytes"]/1024**3:.3f}GiB、科学予測{estimate:.6f}秒・ownprobe/旧失敗込み{estimate+r["GPU_seconds"]+previous:.6f}/900。'
                '旧probeはCPU準備moduleのimport副作用でCUDAを隠したため失敗。元source/config/失敗を保存しproposal定数path参照だけへ限定修復、GPU可視性import回帰testを追加し科学recipe不変。'
                'これは実装/再開/費用の証明で、日本語品質やBase完成の証明ではない。次は予算内のみ専用科学runner/明示readout評価/全80reviewを実装し、cached native full100M対照を再GPUせず固定条件で比較する。')
        else:detail=f'出力変換probe actual{job["pid"]}実終端/不在、GPU{job["GPU_elapsed_seconds"]:.6f}秒、理由{job.get("error")}。原source/partial/失敗を保持し、基準や幅等を変えて救済せず実原因に対する限定修復または別機構を定義する。'
    atomic_json(destination,report)
    files=[destination,study.CONFIG,study.PROPOSAL,Path(__file__),*[ROOT/s for s in study.SOURCES],
        ROOT/'reports/phase6/readout_adapter_tests.xml',ROOT/'scripts/stop_only_feasibility.py',ROOT/'tests/test_stop_only_feasibility.py',
        ROOT/'reports/phase6/stop_only_feasibility.json',ROOT/'reports/phase6/stop_only_feasibility_tests.xml',ROOT/'reports/phase6/stop_only_feasibility_observations.tsv']
    if phase!='preparation':files += [q for q in sorted((study.RUN/'probe').rglob('*')) if q.is_file() and q.suffix in ('.json','.jsonl','.py','.ps1','.xml')]
    files=list(dict.fromkeys(files));archive=destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive,'w:gz') as output:
        for q in files:output.add(q,arcname=q.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),dict(files={q.relative_to(ROOT).as_posix():dict(bytes=q.stat().st_size,sha256=sha256(q)) for q in files},
        file_count=len(files),archive=study.reference(archive),tensors_native_only=True))
    prefix=('Base専用frozen nonlinear readout: '+phase+'（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n'+detail+
        '\n\n[Houlsby adapter](https://proceedings.mlr.press/v97/houlsby19a.html)と[feature distortion/linear probing](https://arxiv.org/abs/2202.10054)を参考にした独自の転移仮説。'
        'per-layer BERT分類adapter/主にvisionの報告を日本語10Mでの改善保証としない。全旧失敗/数値7/Phase0–3/元相対・絶対・歴史Web1%基準保持。'
        '幅/activation/placement/init/LR/source/mask/parent/decoder/CP救済sweepなし、native HF export未対応を完成としない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n')
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        q=ROOT/relative;q.write_text(prefix+q.read_text(encoding='utf-8-sig'),encoding='utf-8')
    q=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(q)
    progress.update(status=report['status'],updated_at=now(),next_action=detail,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['readout_adapter_'+phase]=study.reference(destination);atomic_json(q,progress)
    print(json.dumps(dict(status=report['status'],GPU_seconds=report['GPU_seconds'],portable_files=len(files))))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('phase',choices=('preparation','probe','probe_failure'));main(p.parse_args().phase)
