"""Record the actual rejected midpoint and a distinct finite-displacement assay."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
import math
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity
from run_weight_average_comparison import RUN,CONFIG,contract


def reference(path):return dict(path=str(path),sha256=sha256(path))


def main():
    completion_path=ROOT/'reports/phase6/weight_average_comparison_completion.json'
    diagnostic_path=ROOT/'reports/phase6/finite_parameter_displacement_proposal.json'
    if completion_path.exists() or diagnostic_path.exists():
        raise ValueError('Preserve original completed midpoint and next proposal')
    c,base=contract();job=read_json(RUN/'job.json');result=read_json(RUN/'result.json');review=read_json(RUN/'review.json')
    if (job['status']!='complete' or alive(job) or job['GPU_elapsed_seconds']>300
            or review['eligible_for_final_Base_validation'] or review['result_sha256']!=sha256(RUN/'result.json')
            or not review['all80_individually_read'] or review['notes_sha256']!=sha256(RUN/'content-notes.json')):
        raise ValueError('Actual terminal read-only comparison and all80 rejection required')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        ui=json.load(response)
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode('utf-8')
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:
            processes.append(identity(int(path.parent.name)))
    if (len(processes)!=1 or not alive(processes[0]) or ui['busy']
            or ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Original actual idle UI restoration required')
    endpoint=read_json(Path(c['refs']['completed_result']['path']))
    bodies={k:ev['body'] for k,ev in endpoint['evaluations'].items()}
    bodies['midpoint']=result['evaluation']['body']
    reference_ids=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in bodies['control']['rows']]
    if any([(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in body['rows']]!=reference_ids for body in bodies.values()):
        raise ValueError('Every cached common256 document must align exactly')
    pairs=[]
    for a,m,b in zip(bodies['control']['rows'],bodies['midpoint']['rows'],bodies['source_order']['rows'],strict=True):
        average=(a['body_nll']+b['body_nll'])/2
        pairs.append(dict(doc_id=a['doc_id'],body_tokens=a['body_tokens'],body_bytes=a['body_bytes'],
            mixed_body_nll=a['body_nll'],midpoint_body_nll=m['body_nll'],staged_body_nll=b['body_nll'],
            midpoint_minus_mean_endpoint_nll=m['body_nll']-average))
    total_bytes=bodies['control']['body_bytes']
    curve=dict(rows=pairs,common_body_bytes=total_bytes,common_body_tokens=122343,
        endpoint_mean_BPB=(bodies['control']['bpb']+bodies['source_order']['bpb'])/2,
        midpoint_BPB=bodies['midpoint']['bpb'],
        midpoint_below_mean_documents=sum(r['midpoint_minus_mean_endpoint_nll']<0 for r in pairs),
        midpoint_minus_mean_BPB=sum(r['midpoint_minus_mean_endpoint_nll'] for r in pairs)/math.log(2)/total_bytes,
        new_forward_calls=0,new_GPU_seconds=0,
        limitations='One midpoint below the mean endpoint loss does not establish the entire path is convex, '
            'a shared minimum, a likelihood ensemble, causal forgetting, or an adoption-qualified model.')
    curve_path=ROOT/'reports/phase6/weight_average_cached_loss_curve.json';atomic_json(curve_path,curve)
    samples=ROOT/'reports/phase6/source-gradient-interference-20261006/samples.json'
    prior=ROOT/'reports/phase6/source_gradient_interference_diagnostic.json'
    sample_rows=[r for r in read_json(samples)['rows'] if r['source']=='web']
    if len(sample_rows)!=4 or any(len(r['original_Web_blocks'])!=8 for r in sample_rows):
        raise ValueError('Reuse exactly four already fixed TRAIN Web8x1024 batches')
    proposal=dict(status='defined_not_implemented_finite_parameter_displacement_read_only_assay',created_at=now(),
        trigger=reference(RUN/'review.json'),cached_midpoint_curve=reference(curve_path),
        earlier_first_order_source_assay=reference(prior),fixed_TRAIN_samples=reference(samples),
        question='Does the first-order Web-body gradient at the completed mixed endpoint predict the observed finite '
            'Web loss change toward the completed staged endpoint, or does a substantial nonlinear residual remain?',
        reason='Earlier pairwise source-gradient cosines and virtual single AdamW steps did not reach conflict markers, '
            'but source order changed WebBPB sharply and the fixed midpoint shows a nonlinear loss tradeoff. '
            'The previous assay explicitly left curvature/finite-displacement harm unmeasured. '
            'This assay measures that missing quantity, not another source-gradient cosine, weight-merge coefficient or layer-selection sweep.',
        checkpoints={k:dict(path=v['checkpoint'],sha256=v['checkpoint_sha256']) for k,v in c['checkpoints'].items()},
        midpoint=read_json(RUN/'preparation.json')['checkpoint'],
        direction='d=staged-mixed once, with tied embedding counted once and all original named FP32 parameters aligned',
        inputs='Reuse original Web blocks and x/y SHA from exactly4 saved TRAIN batches8x1024; BOS targets ignored; '
            'body-only CE for gradient and actual loss; goldEOS measured separately. No new sample selection, content repair, index scan or dev learning.',
        method='Uncompiled FP32 math attention; evaluate same32 TRAIN sequences at mixed/midpoint/staged. '
            'At mixed compute autograd Web-body gradient without assigning .grad, optimizer or parameter updates; '
            'save g dot d, actual loss differences, finite-difference curvature2*(L1-2*Lhalf+L0), '
            'and nonlinear residual(L1-L0-g dot d). Four batches separately, per-source token accounting and immutable input hashes.',
        descriptive_markers=dict(Web_harm_nats_per_body_token_at_least=.02,batches_at_least=3,
            nonlinear_residual_fraction_of_positive_actual_change_at_least=.5),
        interpretation='Use the markers descriptively to distinguish predicted first-order harm from unmodeled finite displacement. '
            'Signed finite differences on one line are not a Hessian or global convexity proof. '
            'No gradient surgery or new regularizer is justified automatically; choose a bounded intervention only if this evidence adds a distinct mechanism.',
        GPU_ceiling_seconds=120,CPU_preparation_ceiling_seconds=30,optimizer_updates=0,scientific_teacher_tokens=0,
        completion_condition='All4 same batches/three named existing models/actual FP32 finite gradients and losses, '
            'weights unchanged/no .grad/RNG restoration, actual terminal PID/failed costs, raw result/decision, original UI restored and commit. '
            'Never substitute this local TRAIN assay for original80 or independent Base validation.',
        failure='Preserve failures. No repeated identical retries, coefficient/endpoint/layer sweep or automatic long training.',
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False)
    atomic_json(diagnostic_path,proposal)
    completion=dict(status='single_equal_weight_midpoint_all_evidence_complete_rejected',created_at=now(),
        config=reference(CONFIG),preparation=reference(RUN/'preparation.json'),result=reference(RUN/'result.json'),
        review=reference(RUN/'review.json'),notes=reference(RUN/'content-notes.json'),job=job,
        cached_curve=reference(curve_path),next_proposal=reference(diagnostic_path),
        summary=review['summary'],quality_comparison=review['quality_comparison'],absolute_dev_screen=review['absolute_dev_screen'],
        original_Web=review['original_Web'],transfer={k:v['summary']['aggregate'] for k,v in result['transfer'].items()},
        parameter_count=10001152,model_only=True,resumable_training_state=False,
        source_or_decoder_modified=False,new_scientific_teacher_tokens=0,new_optimizer_updates=0,
        actual_GPU_seconds=job['GPU_elapsed_seconds'],GPU_ceiling_seconds=300,
        previous_related_GPU_seconds_preserved=2289.596018486074,
        related_GPU_including_this_research_seconds=2289.596018486074+job['GPU_elapsed_seconds'],
        original_UI=ui,original_UI_identity=processes[0],all80_individually_read=True,
        exact_previous_score_reuse=read_json(RUN/'content-notes.json')['exact_old_score_reuse']['ids'],
        independent_human_blind=False,protected_test_used=False,quality_criteria_unchanged=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        interpretation='The one midpoint reduces Web loss relative to staged CE while retaining much of its stopping behavior, '
            'but does not improve all mandatory quality dimensions; it fails coherence/completion/historical BPB and stronger relative guards. '
            'It is rejected, with no coefficient/endpoint/layer or decoding sweep. '
            'Research papers motivated the comparison but were not evidence of Japanese10M performance.',
        next_action='Implement the defined TRAIN-only finite parameter-displacement assay, with exact existing32 Web blocks and '
            'read-only FP32 gradients, before selecting another Base intervention; no new source or merge search.')
    atomic_json(completion_path,completion)
    files=[CONFIG,completion_path,diagnostic_path,curve_path,ROOT/'reports/phase6/base_intervention_gap_synthesis.json',
        ROOT/'reports/phase6/weight_average_tests.xml',ROOT/'reports/phase6/weight_average_comparison_review.json',
        *[ROOT/p for p in c['source_sha256']],ROOT/'scripts/record_weight_average_content_notes.py',Path(__file__)]
    files.extend(p for p in sorted(RUN.rglob('*.json')) if 'source' not in p.relative_to(RUN).parts)
    files=list(dict.fromkeys(files))
    evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/weight_average_comparison_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve portable midpoint evidence')
    with tarfile.open(archive,'w:gz') as stream:
        for path in files:stream.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/weight_average_comparison_portable.json',dict(status='rejected_midpoint_all_raw_evidence_portable',
        files=evidence,file_count=len(files),raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=reference(archive),
        model_tensors_preserved_native_only=True))
    summary=review['summary']
    prefix=f'''同一親の重み50%平均を実評価・全80採点し、不採用（2026-10-06 JST）。前turnの翻訳source不採用は1b22447に保存したprogress。Baseのみ継続・完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

既存7モデル/不採用3sourceの92,256bytes summaryをCPU0.00994秒で整理し、同10.5B親/同100M教師のmixed対staged重みを各50%で平均する未実施一条件を凍結。関連CPU3tests/0.75秒、実prepare0.35952秒で10,001,152param/120model keys。FP32平均とtied embeddingを保持、optimizer/scheduler/RNG/sampler/会計を混ぜずmodel-onlyとして保存し、resume可能な学習stateと称さない。新科学教師/optimizer0、係数やendpoint/layer選別の総当たりなし。WiSE-FT/Model soupsは着想の一次資料で、日本語10Mへの効果の証拠に代入しない。

actual625718/boot{job['boot_id']}/start{job['start_ticks']}は全GPU評価終了・不在。実GPU{job['GPU_elapsed_seconds']:.6f}秒/上限300、native run reports/phase6/weight-average-comparison-20261006。全256 body/same472055bytes・日本語192/331/1119・greedy80・bridge/retention各128を完了。BPB{summary['BPB']:.9f}、文法{summary['grammar2']}/関連{summary['relevance2']}/一貫性{summary['coherent']}/適切{summary['appropriate']}/EOS71/反復8/Unicode-role-empty0（各80）。意味52.083%/JBLiMP76.435%/JCQA31.859%、bridge両条件65/128・retention35/128。全80個別読解/rawSHA/理由を保存、同じrawの旧4例はスコアそのまま再利用。幻想・新人物・自然な別行動・暗黙の設備・gold不一致は自動失敗にしない。非blind Codexで独立人手なし。

staged対照23/26/76/2/BPB1.133613からWebBPBは改善するが一貫性20/適切21/EOS71/反復8で強いrelative条件未達。paired一貫性差-3/CI[-.15,.075]、絶対一貫性27/適切27・歴史WebBPB<=.981285952も失敗。不採用を確定し、このmidpointの係数/重み組合せ/layer/decoder変更で救済しない。保存済全256を同ID/bytesで集計すると、midpoint BPBはendpoint平均{curve['endpoint_mean_BPB']:.9f}を{abs(curve['midpoint_minus_mean_BPB']):.9f}下回り、{curve['midpoint_below_mean_documents']}/256文書で平均NLLより低い。これは一点の非線形性の観察で、全path凸性や能力改善の因果保証ではない。新forward/GPU0。

全採否/会計/全80/transfer/rawをSHA付きweight_average_comparison_portable.json/archiveに保存。元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}をactual ps/HTTP親410f975d…/10000007168/busy=falseで確認。旧Phase0–3/数値7失敗/全source不採用/既関連GPU2289.596018秒を保持、新比較込み{completion['related_GPU_including_this_research_seconds']:.6f}秒（全project費用ではなく当該series）。独立学習seed/full dev/protected test/採用は未達。

次はfinite_parameter_displacement_proposal.jsonの一つのread-only診断を実装する。旧source-gradient assayで未測定だったfinite displacementの害と一次勾配予測を、既保存TRAIN Web32 blocks（4×8×1024）の同x/ySHAで測る。mixed/midpoint/staged三既存重み・FP32 math、mixedのbodyCE gradient dot(staged-mixed)、実損失差と非線形残差、EOS別を記録。教師/optimizer0、CPU準備30秒/GPU全上限120秒、基準を先に固定。旧cosine/仮想一Adam更新を反復せず、新Web/source全量scan/評価語句の学習/自動regularizer/merge sweepなし。局所TRAIN32で唯一原因や全品質は証明しない。実source/runner/tests/事前条件の準備とactual CUDA完了をこれから進め、証拠に応じた別のBase比較だけを選ぶ。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_fixed_midpoint_complete_rejected_finite_displacement_assay_defined',updated_at=now(),
        weight_average_comparison_completion=reference(completion_path),finite_parameter_displacement_proposal=reference(diagnostic_path),
        next_action=completion['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['weight_average_active_job']['status']='complete_actual_process_absent'
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=progress['status'],summary=summary,GPU_seconds=job['GPU_elapsed_seconds'],curve_documents=curve['midpoint_below_mean_documents'])))


if __name__=='__main__':main()
