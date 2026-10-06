"""Review all saved displacement points; preserve evidence and define one hypothesis."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import hashlib
import json
import math
from pathlib import Path
import sys
import tarfile
import time
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity
from diagnose_finite_parameter_displacement import RUN,CONFIG,inspect,reference
from finite_parameter_displacement import summarize_displacement


def main():
    started=time.monotonic()
    destination=ROOT/'reports/phase6/finite_parameter_displacement_completion.json'
    if destination.exists():raise ValueError('Preserve original completed review')
    c=inspect();job=read_json(RUN/'job.json');result=read_json(RUN/'result.json')
    if (job['status']!='complete' or alive(job) or not 0<job['GPU_seconds']<=120
            or result['config_sha256']!=sha256(CONFIG) or result['GPU_seconds']>job['GPU_seconds']
            or not result['RNG_restored'] or result['scientific_teacher_tokens'] or result['optimizer_updates']
            or result['protected_test_used'] or result['Base_complete'] or result['Base_adopted']
            or result['Chat_started'] or result['quantization_started'] or not result['quality_criteria_unchanged']):
        raise ValueError('Actual finite read-only terminal run required')
    if set(result['observations'])!={'mixed','midpoint','staged'} or len(result['rows'])!=4:
        raise ValueError('Every named model and fixed batch required')
    checks=0
    with np.load(c['refs']['fixed_inputs']['path'],allow_pickle=False) as inputs:
        for arm,points in result['observations'].items():
            if len(points)!=4 or not all(result['model_checks'][arm].values()):
                raise ValueError('Every read-only model check and four finite points required')
            for draw,point in enumerate(points):
                raw=read_json(RUN/f'points/{arm}/{draw:02d}.json')
                row=c['rows'][draw]
                if (raw!=point or point['metadata']!=row or point['binding']!=dict(config_sha256=sha256(CONFIG),
                        checkpoint_sha256=c['checkpoints'][arm]['sha256'],draw=draw)
                        or not point['finite_forward'] or point['optimizer_updates']
                        or not all(math.isfinite(point[k]) for k in ('body_CE','EOS_CE'))):
                    raise ValueError('Raw point/hash/batch/finite loss binding differs')
                for name,key in (('x','input_sha256'),('y','target_sha256')):
                    if hashlib.sha256(inputs[name+str(draw)].astype('<i8').tobytes()).hexdigest()!=row[key]:
                        raise ValueError('Original exact TRAIN inputs differ')
                if arm=='mixed' and (not point['finite_gradients'] or point['unique_parameters']!=119
                        or not all(math.isfinite(point[k]) for k in ('directional_body_gradient','gradient_norm','direction_norm'))):
                    raise ValueError('Actual all119 unique finite gradients required')
                checks+=1
    for draw in range(4):
        a,m,b=[result['observations'][arm][draw] for arm in ('mixed','midpoint','staged')]
        calculated=dict(draw=draw,**summarize_displacement(a['body_CE'],m['body_CE'],b['body_CE'],a['directional_body_gradient']))
        if result['rows'][draw]!=calculated:raise ValueError('Saved derived finite displacement differs')
    markers=dict(harm_batches=sum(r['harm_marker'] for r in result['rows']),
        nonlinear_half_or_more_batches=sum(r['nonlinear_half_or_more_marker'] for r in result['rows']),
        first_order_predicts_increase_batches=sum(r['first_order_predicts_increase'] for r in result['rows']))
    if markers!=result['markers']:raise ValueError('Predeclared descriptive markers differ')
    norms=[p['direction_norm'] for p in result['observations']['mixed']]
    if len(set(norms))!=1 or norms[0]<=0:raise ValueError('One fixed nonzero named direction required')
    total=sum(r['body_teachers'] for r in c['rows'])
    def mean(key):return sum(r[key]*m['body_teachers'] for r,m in zip(result['rows'],c['rows'],strict=True))/total
    summary=dict(body_token_weighted_actual_CE_change=mean('actual_body_CE_change'),
        body_token_weighted_first_order_CE_change=mean('first_order_body_CE_change'),
        body_token_weighted_nonlinear_residual=mean('nonlinear_residual'),
        nonlinear_fraction_range=[min(r['nonlinear_fraction_of_positive_change'] for r in result['rows']),
            max(r['nonlinear_fraction_of_positive_change'] for r in result['rows'])],
        direction_L2_norm=norms[0],markers=markers)
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode('utf-8')
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:
            processes.append(identity(int(path.parent.name)))
    if (len(processes)!=1 or not alive(processes[0]) or ui['busy']
            or ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Actual original idle UI must be restored')
    if markers['harm_batches']<3 or markers['nonlinear_half_or_more_batches']<3:
        raise ValueError('Preserve unexpected markers; do not create this conditional intervention')
    # Explicit research decision after seeing the predeclared markers, not an automatic regularizer.
    # Isotropic L2 is a hypothesis: the measured residual is not a Hessian or causal proof.
    coefficient=2*summary['body_token_weighted_nonlinear_residual']/norms[0]**2
    proposal_path=ROOT/'reports/phase6/parameter_displacement_anchor_proposal.json'
    if proposal_path.exists():raise ValueError('Preserve original single next comparison')
    proposal=dict(status='defined_not_implemented_not_launched',created_at=now(),trigger=reference(RUN/'result.json'),
        question='Can one parameter-displacement penalty retain the completed mixed model Web fit while another matched '
            'staged100M teaches completion, compared with exactly the same additional staged CE without the penalty?',
        reason='All four fixed TRAIN batches show actual finite Web loss increases; 94.6–98.9 percent is nonlinear '
            'residual relative to the mixed endpoint derivative. Earlier source cosines/one-step Adam did not capture '
            'this measured quantity. A direct parameter displacement penalty is therefore a distinct testable hypothesis.',
        parent_and_anchor=c['checkpoints']['mixed'],reference_strong_staged=c['checkpoints']['staged'],
        arms=['matched_additional_staged_CE','matched_additional_staged_CE_parameter_anchor'],
        objective='ordinary body+EOS CE + (lambda/2)*sum_unique_parameters((theta-theta_anchor)^2)',
        lambda_fixed=coefficient,lambda_derivation='2*body_token_weighted_finite_residual/observed_direction_L2_norm_squared',
        lambda_units='nats per CE teacher token per squared raw parameter unit; sum, not mean over parameters',
        hypotheses_and_limits='Isotropic calibration along one observed direction need not generalize to other directions. '
            'No claim of Fisher/Hessian estimation, source conflict as the sole cause, or guaranteed quality. '
            'Mixed endpoint is a learned unadopted reference, not an adopted Base or teacher instruction model.',
        distinction_from_previous_KL='Direct unique-parameter penalty anchored at the completed mixed endpoint; '
            'previous KL constrained parent output probabilities on a Web reference. New matched CE control is mandatory '
            'because the starting checkpoint changes. Existing staged quality guards also remain mandatory.',
        training='Both arms restore the identical mixed full model/Adam/scheduler/RNG/sampler/counters. '
            'Same next100M ordinary CE teachers each and frozen75M Web→5M story→10M ordinary→10M conditional '
            'source order, same actual LR0.00001/shape; restart the local source comparison sampler identically, '
            'record its reset separately from inherited full optimizer state. No learned checkpoint averaging.',
        accounting='New main teachers total200M; raw parameter penalty has zero token teachers/reference input. '
            'Previously learned100M mixed reference is reused evidence, not new tokens nor a fresh independent seed. '
            'All verification updates and every physical/valid/source/EOS/byte counter remain separate.',
        prerequisites='Implement loss/state/runner/accounting and meaningful CPU tests before running. '
            'Measure own CUDA BF16 forward/backward and continuous4vsresumed2+2 including penalty/anchor/sampler. '
            'Own stable32 timings, evaluation reserve150s, measured train time*1.3+150+50 and probe costs '
            'must fit1800s before scientific config freeze. Stop budget failure; no LR/lambda/batch beyond measured range sweep.',
        GPU_total_ceiling_seconds=1800,probe_GPU_ceiling_seconds=120,CPU_preparation_ceiling_seconds=30,
        evaluation='Same dev256 common bytes/Japanese192-331-1119/native greedy80/bridge128/retention128. '
            'Read every generated continuation with raw SHA and individual reasons; do not rescore controls favorably. '
            'Compare paired same IDs against both the new matched CE control and original strong staged control.',
        strong_quality_guards='Original staged coherence23+8/paired CI lower>0/EOS>=76/repetition<=2; '
            'same absolute grammar>=56/coherence>=27/appropriate>=27/no role-Unicode-empty; '
            'historical WebBPB<=0.9812859519097707 and all previous EOS/nonpunctuation guards. No relaxation.',
        completion='Both actual terminal jobs/all counters/entire Japanese and80 reviews/adoption decision/UI restoration/commit. '
            'Failure ends this single comparison, no coefficient/anchor/layer/source/decoder salvage. '
            'Only a qualified pilot permits independent learned recipe seed/full dev/protected test/adoption.',
        scientific_teacher_tokens_so_far=0,optimizer_updates_so_far=0,GPU_seconds_so_far=0,
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False)
    elapsed=time.monotonic()-started
    if elapsed>10:raise TimeoutError('Bounded metadata review10s exceeded')
    atomic_json(proposal_path,proposal)
    completion=dict(status='finite_displacement_all12_points_complete_reviewed',created_at=now(),
        config=reference(CONFIG),result=reference(RUN/'result.json'),actual_job=job,actual_process_absent=True,
        all12_raw_points_checked=checks==12,summary=summary,next_proposal=reference(proposal_path),
        CPU_preparation_seconds=c['CPU_preparation_seconds'],CPU_review_seconds=elapsed,CPU_review_ceiling_seconds=10,
        actual_GPU_seconds=job['GPU_seconds'],GPU_ceiling_seconds=120,scientific_teacher_tokens=0,optimizer_updates=0,
        previous_related_GPU_seconds_preserved=2341.710162622068,
        related_GPU_including_this_assay_seconds=2341.710162622068+job['GPU_seconds'],
        original_UI=ui,original_UI_identity=processes[0],RNG_restored=True,weights_unchanged=True,
        interpretation='Observed finite loss harm is much larger than its local first-order prediction on all4 batches. '
            'This is evidence of nonlinear displacement on this fixed TRAIN input/direction, not global curvature or '
            'a proof that data amount/model capacity cannot improve. No new model or quality adoption is produced.',
        next_action='Implement the one matched two-arm parameter-anchor comparison and own measured probe. '
            'Freeze scientific config only after own save/resume/throughput/cost gates. No automatic training from this proposal.',
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False)
    atomic_json(destination,completion)
    files=[CONFIG,destination,proposal_path,ROOT/'reports/phase6/finite_parameter_displacement_result.json',
        ROOT/'reports/phase6/finite_parameter_displacement_tests.xml',*[ROOT/p for p in c['source_sha256']],Path(__file__)]
    files.extend(p for p in sorted(RUN.rglob('*.json')) if 'source' not in p.relative_to(RUN).parts)
    files=list(dict.fromkeys(files))
    evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/finite_parameter_displacement_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve portable assay evidence')
    with tarfile.open(archive,'w:gz') as output:
        for path in files:output.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/finite_parameter_displacement_portable.json',dict(files=evidence,
        file_count=len(files),raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=reference(archive),
        exact_fixed_input_arrays_preserved_native_only=c['refs']['fixed_inputs'],model_tensors_preserved_native_only=True))
    prefix=f'''有限な重み変化のTRAIN診断を実完了（2026-10-06 JST）。前回midpoint不採用はb4e71dcに保存。Base未完了・未採用、完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

既保存TRAIN Web32 blocksの元x/ySHAを再利用し、mixed/midpoint/staged同3重みのFP32 mathを測定。CPU3tests/.82秒、実準備{c['CPU_preparation_seconds']:.6f}秒/上限30、GPU{job['GPU_seconds']:.6f}秒/上限120。actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・不在。全12点/raw metadataと統計を確認、全119unique paramsの有限勾配、全モデル重み不変/.gradなし/RNG復元。input32768/body32626/EOS71各model、科学教師/optimizer0。巨大corpus再scan/再encode/新選別なし。

Web bodyCE増加は4/4で0.438–0.474 nats/token、一次予測0.0050–0.0257、非線形残差比94.6–98.9%。事前harm>=.02/3以上と非線形>=50%/3以上はいずれも4/4。body-token加重実差{mean('actual_body_CE_change'):.9f}/一次{mean('first_order_body_CE_change'):.9f}/残差{mean('nonlinear_residual'):.9f}。局所一次診断が捉えなかった有限変化を観測したが、一方向/4 TRAIN batchesでHessian・全path凸性・唯一原因・モデル容量限界・品質改善は証明しない。全旧quality/source失敗とPhase0–3/数値7失敗を保持。

全点/会計/source/tests/次proposalをfinite_parameter_displacement_completion/portable.jsonとrawSHA付きarchiveへ保存。元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}をactual/HTTP親410f975d…/10000007168/busy=falseで確認。関連GPU累積{completion['related_GPU_including_this_assay_seconds']:.6f}秒（全project費用ではない）。独立学習seed/full dev/protected test/採用は未達。

次はparameter_displacement_anchor_proposal.jsonの一つのmatched2-arm比較を実装・実probeする。完了mixed fullstateを両arm同親とし、同追加staged100M教師×2、candidateだけunique parameter変位のL2 penaltyを加える仮説。lambda={coefficient:.12g}を今回の加重残差/固定direction normから一度定義、sweepなし。これは一方向からの等方性仮説で効果保証ではない。以前のparent-output KLと異なるparameter制約・mixed anchorを試し、親変更に対して新matched CE対照を必須にする。元strong staged23+8/CI正/EOS76/反復2・絶対/歴史BPB全guardを保持。実CUDA4vs2+2/steady32/実測1.3+reserve150+50/全probe込み1800秒gate前に科学設定を凍結・起動しない。提案未実装/未起動、教師/GPU0。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_finite_displacement_complete_parameter_anchor_comparison_defined',updated_at=now(),
        finite_parameter_displacement_completion=reference(destination),parameter_displacement_anchor_proposal=reference(proposal_path),
        next_action=completion['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=progress['status'],summary=summary,lambda_fixed=coefficient,UI_identity=processes[0],
        GPU_seconds=job['GPU_seconds'],CPU_review_seconds=elapsed,portable_files=len(files))))


if __name__=='__main__':main()
