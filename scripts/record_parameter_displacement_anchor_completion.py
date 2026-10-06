"""Save the rejected fixed L2 comparison and one distinct label-mask hypothesis."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
import tarfile
import time
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity,finite_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from review_textbook_quantity_comparison import validate_notes
from condition_relation_language import RelationLanguageTrainView
import run_parameter_displacement_anchor_v3 as study


def main():
    torch.set_num_threads(2);started=time.monotonic()
    destination=ROOT/'reports/phase6/parameter_displacement_anchor_completion.json'
    if destination.exists():raise ValueError('Preserve completed original single L2 decision')
    c=study.inspect(study.CONFIG);r=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json');review=read_json(study.RUN/'review.json')
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json')
            or review['eligible_for_final_Base_validation'] or not review['all160_individually_read']
            or job['GPU_elapsed_seconds']+c['verification_GPU_seconds']>1800):raise ValueError('Terminal all160 rejected comparison required')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode('utf-8')
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:processes.append(identity(int(path.parent.name)))
    if (len(processes)!=1 or not alive(processes[0]) or ui['busy']
            or ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Actual original idle UI must be restored')
    old_run=ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006'
    old_result=read_json(old_run/'compare-result.json');strong=old_result['evaluations']['source_order']
    raw=old_run/'evaluation/source_order/evaluation/generation.json'
    strong_scores=validate_notes(strong['generation']['outputs'],read_json(ROOT/'reports/phase6/source_order_condition_notes.json'),sha256(raw))
    new_ev=r['evaluations']['matched_staged_CE'];new_raw=study.RUN/'evaluation/matched_staged_CE/evaluation/generation.json'
    new_scores=validate_notes(new_ev['generation']['outputs'],read_json(study.RUN/'matched_staged_CE-content-notes.json'),sha256(new_raw))
    new_CE_relative=quality_gates(strong,new_ev,strong_scores,new_scores,'content')
    base=read_json(Path(c['original_config']['path']));historical=read_json(Path(base['reference']['web_screen']['path']))
    new_CE_historical=adoption_checks(historical,new_ev)
    # One preselected saved fullstate before conditional exposure. Selection uses
    # only source counters/update cadence; no endpoint scoring/checkpoint sweep.
    history_path=old_run/'source_order/training/metrics.jsonl'
    first=None;parent_update=None
    with history_path.open() as stream:
        for line in stream:
            row=json.loads(line)
            if parent_update is None:parent_update=row['update']-1
            if row['source_teachers']['conditional_textbook']>0:first=row;break
    if first is None:raise ValueError('Original conditional source transition required')
    shared_update=parent_update+((first['update']-parent_update-1)//250)*250
    shared_path=old_run/f'source_order/training/checkpoint-{shared_update:08d}.pt'
    shared=torch.load(shared_path,map_location='cpu',weights_only=False)
    if (not finite_state(shared) or shared['update']!=shared_update or shared['sampler']['source_teachers']['conditional_textbook']
            or shared['sampler']['source_order']!=list(study.prior.SOURCE_ORDER)
            or any(g['lr']!=.00001 for g in shared['optimizer']['param_groups'])):
        raise ValueError('Exact fixed original pre-conditional fullstate required')
    view=RelationLanguageTrainView(c['positive_data']['path'],c['positive_data']['manifest_sha256'])
    source_summary=dict(documents=len(view.lengths),serialized_positions=len(view.tokens),
        body_positions=int((view.tokens>=8).sum()),outcome_body_positions=int(view.focus.sum()),
        EOS_positions=int((view.tokens==3).sum()),prefix_body_positions=int(((view.tokens>=8)&~view.focus).sum()))
    elapsed=time.monotonic()-started
    if elapsed>30:raise TimeoutError('Completion and saved-source metadata30s exhausted')
    proposal_path=ROOT/'reports/phase6/conditional_prefix_mask_proposal.json'
    if proposal_path.exists():raise ValueError('Preserve original single mask hypothesis')
    proposal=dict(status='defined_not_implemented_not_launched',created_at=now(),trigger=study.reference(study.RUN/'review.json'),
        question='Does excluding conditional setup/prefix text from hard CE targets reduce generic template continuation '
            'while preserving conditional outcome and EOS learning on exactly the original input suffix?',
        reason='Fixed L2 improved Web loss but not all generation guards; both new CE and L2 outputs reproduce conditional '
            'light/person/record phrasing on unrelated natural prefixes. Previous positive-weight/ranking/anchor/KL comparisons '
            'still learned hard CE on those setup tokens. This tests target selection, not another parameter coefficient or source variant.',
        selected_shared_checkpoint=study.reference(shared_path),selection_policy='Last original250-update saved checkpoint '
            'strictly before the first conditional teacher, based only on old source counters. No quality/endpoint selection.',
        first_original_conditional_update=first['update'],shared_update=shared_update,
        original_strong_control=c['strong_control'],original_control_result=study.reference(old_run/'compare-result.json'),
        original_control_notes=study.reference(ROOT/'reports/phase6/source_order_condition_notes.json'),
        original_config=c['references']['old_source_config'],accepted_source=c['positive_data'],source_summary=source_summary,
        candidate_target_rule='Continue the original fullstate/sampler/quotas without resetting streams. '
            'Other3 sources retain every original body+EOS label. For conditional source only, '
            'keep existing outcome-focused body positions plus original EOS3 and ignore the other prefix/setup body targets. '
            'Do not change x, BOS, order, document length, source text, shuffle, update count, actual LR0.00001, '
            'optimizer/scheduler/RNG, conditional terminal padding or decoder. Ordinary causal Base continuation; no role labels.',
        sampling_and_accounting='The original unmasked quotas remain a reference input stop condition, not masked teacher counts. '
            'Keep separate original reference teachers/source/EOS/bodybytes/unmasked target digest and actual hard teachers/bodybytes/masked digest. '
            'Reused shared-prefix learning and old100M control are not new exposure. New suffix physical input matches '
            'original remaining suffix exactly; actual candidate hard teachers will be fewer. Do not call it a matched-teacher100M comparison.',
        remaining_reference_teacher_quotas={k:study.GOALS[k]-v for k,v in shared['sampler']['source_teachers'].items()},
        parameter_penalty=0,KL_teacher=0,positive_weight=1,new_source_documents=0,new_family_selection=0,new_tokenizer=0,
        prerequisites='Implement sampler/target mask/completed-state counters/runner/meaningful CPU tests first. '
            'Reuse accepted compact data; no source/full-index scan. Own actual CUDA/BF16 finite save/resume gate must include '
            'masked conditional updates and the source transition; measure own32 steady updates. '
            'Actual measured suffix time*1.3+save+evaluation reserve150+50 and all probe/failed costs must fit600s before science freeze.',
        CPU_preparation_ceiling_seconds=30,probe_GPU_ceiling_seconds=120,total_new_GPU_ceiling_seconds=600,
        evaluation='Old strong original100M control reused unchanged. Same common256 bytes, allJapanese192-331-1119, '
            'greedy80 individually read/raw SHA, bridge128 and retention128. EOS/raw repetitions/Unicode remain visible. '
            'New CE32/80 completion result is supplementary observed evidence, not a lowered primary gate.',
        quality_guards='Keep original strong staged coherence23+8/paired CI lower>0/EOS>=76/repetition<=2; '
            'all original absolute/historical WebBPB<=0.9812859519097707 and nonpunctuation completion guards. '
            'No favorable rescoring of old controls; no gate relaxation.',
        failure='End this single target-mask comparison after failure; no prefix/outcome/EOS weight, source, mask position, '
            'checkpoint, input budget, ratio or decoder sweep to rescue it.',
        limits='Hypothesis chosen after the observed failure. Template repetition and one selected suffix do not prove '
            'the sole cause of quality issues, source-wide quality or a model capacity ceiling. Masking also changes '
            'hard-teacher count and EOS fraction; hold physical input fixed and label the changed budgets.',
        completion='Actual finite suffix/matched original reference input ledger/full evaluation/all80 review/decision/UI/commit. '
            'Only a qualified pilot allows independent learned recipe seed/full dev/protected test/adoption.',
        scientific_teacher_tokens_so_far=0,GPU_seconds_so_far=0,optimizer_updates_so_far=0,
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(proposal_path,proposal)
    completion=dict(status='fixed_parameter_anchor_two100M_all160_complete_rejected',created_at=now(),
        config=study.reference(study.CONFIG),result=study.reference(study.RUN/'compare-result.json'),review=study.reference(study.RUN/'review.json'),
        actual_job=job,actual_process_absent=True,summary=review['summaries'],accounting=review['accounting'],
        quality_comparisons=review['quality_comparisons'],absolute_dev_screen=review['absolute_dev_screen'],original_Web=review['original_Web'],
        supplementary_new_CE_vs_old_staged=new_CE_relative,supplementary_new_CE_historical_Web=new_CE_historical,
        scientific_teacher_tokens=200000000,scientific_optimizer_updates=sum(v['completed_updates'] for v in review['accounting'].values()),
        verification_teacher_tokens=c['verification_teacher_tokens'],verification_optimizer_updates=80,
        science_GPU_seconds=job['GPU_elapsed_seconds'],probe_and_failed_GPU_seconds=c['verification_GPU_seconds'],
        total_new_GPU_seconds=job['GPU_elapsed_seconds']+c['verification_GPU_seconds'],GPU_ceiling_seconds=1800,
        previous_related_GPU_seconds_preserved=2343.8289305070936,
        related_GPU_including_this_comparison_seconds=2343.8289305070936+job['GPU_elapsed_seconds']+c['verification_GPU_seconds'],
        CPU_completion_and_next_metadata_seconds=elapsed,CPU_ceiling_seconds=30,original_UI=ui,original_UI_identity=processes[0],
        transfer={arm:{k:r[k][arm]['summary']['aggregate'] for k in ('transfer','retention')} for arm in study.ARMS},
        all160_individually_read=True,exact_previous_raw_score_reuse={arm:read_json(study.RUN/f'{arm}-content-notes.json')['exact_old_score_reuse'] for arm in study.ARMS},
        independent_human_blind=False,quality_criteria_unchanged=True,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        interpretation='Parameter anchor improves Web fit over new matched CE, but does not meet coherence/stop/old repetition '
            'and historical Web guard simultaneously. The coherence difference CI crosses0, not proof of significant harm. '
            'New CE alone reaches the absolute development screen and32 coherent outputs, but fails old stopping/repetition '
            'and historical Web guards, so neither checkpoint is adopted. Extra100M mixed history also differs from '
            'old staged, so the new CE observation is not an amount-only causal comparison.',
        next_proposal=study.reference(proposal_path),next_action='Implement the single defined conditional-prefix target-mask suffix '
            'comparison using the saved pre-conditional fullstate, own masked-state CUDA probe and actual measured budget before launch.')
    atomic_json(destination,completion)
    files=[study.CONFIG,destination,proposal_path,ROOT/'reports/phase6/parameter_displacement_anchor_review.json',
        ROOT/'reports/phase6/parameter_displacement_anchor_preparation.json',ROOT/'reports/phase6/parameter_displacement_anchor_preparation_portable.json',
        ROOT/'reports/phase6/parameter_displacement_anchor_review_tests.xml',ROOT/'scripts/review_parameter_displacement_anchor.py',
        ROOT/'tests/test_parameter_displacement_anchor_review.py',ROOT/'scripts/record_parameter_displacement_anchor_content.py',Path(__file__)]
    files.extend(p for p in sorted(study.RUN.rglob('*.json')) if 'source' not in p.relative_to(study.RUN).parts and 'probe' not in p.relative_to(study.RUN).parts)
    files.extend(p for p in sorted(study.RUN.rglob('*.jsonl')) if 'source' not in p.relative_to(study.RUN).parts and 'probe' not in p.relative_to(study.RUN).parts)
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/parameter_displacement_anchor_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve all terminal raw evidence')
    with tarfile.open(archive,'w:gz') as output:
        for path in files:output.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/parameter_displacement_anchor_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),model_tensors_preserved_native_only=True))
    summary=review['summaries']
    prefix=f'''固定parameter L2の両100M学習/全評価/160個別読解を完了・不採用（2026-10-06 JST）。CUDA準備d1b44f0・永続起動66bdd3dはprogress。Baseのみ継続・実完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・不在。両科学200000000教師/{completion['scientific_optimizer_updates']}更新、同input/targets/source/全cursor会計が一致、fixed L2教師0。検証80更新/2615904教師別。scienceGPU{job['GPU_elapsed_seconds']:.6f}+probe/失敗33.680480=新全{completion['total_new_GPU_seconds']:.6f}秒/上限1800。係数.04161064039180984/親6d901bd…/実LR.00001を保持。全256common472055bytes/日本語192-331-1119/greedy80各/bridge-ret128各が完了、2arm全160をrawSHA/具体理由で保存。旧raw完全一致は対照7/candidate15の採点をそのまま継承し、幻想/新人物/暗黙設備/自然な別行動/gold不一致を自動失敗にしない。非blind Codex、独立人手なし。

newmatched CE: BPB{summary['matched_staged_CE']['BPB']:.9f}、文法65/関連52/一貫性32/適切37/EOS69/反復6、意味54.167%/JBLiMP76.133%/JCQA29.759%。parameteranchor: BPB{summary['parameter_anchor']['BPB']:.9f}、文法59/関連60/一貫性25/適切29/EOS67/反復6、意味52.604%/JBLiMP75.529%/JCQA32.172%。両Unicode-role-empty0（各80）。candidate一貫性差-7/CI[-.2125,.05]、oldstrong23比+2/CI[-.0875,.15]でいずれも相対条件未達。絶対一貫性27・歴史WebBPB<=.981285952も失敗。差のCIは0を含み有意な悪化の証明ではない。newCEは絶対screenを満たすがoldEOS76/反復2/歴史WebBPBを満たさず採用なし。oldstrongへの比較は追加mixed100Mの履歴も違い、単純学習量だけの因果としない。

全raw/counters/160notes/review/transfer/probe費用/失敗はparameter_displacement_anchor_completion/portable.json/archiveへ保存、モデルtensorはnative。元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}とHTTP親410f975d…/10000007168/busy=falseを確認。旧Phase0–3/数値7失敗・全不採用と関連費用を保持、当series累積{completion['related_GPU_including_this_comparison_seconds']:.6f}秒（全project費用ではない）。Base品質採用/独立学習seed/full dev/protected testは未達。L2係数/anchor/層/source/decoder sweepで救済しない。

次はconditional_prefix_mask_proposal.jsonの一つの別の損失target仮説を実装。Setup語句のhardCEを外し既存outcome focus+EOSだけをconditional教師とする案。source変更0、roleなし、他3source・同残input/順序/実LR/fullstateを保持。oldsourceの最初conditional教師update{first['update']}直前の250保存CP{shared_update}をsource会計だけで選定・実finite/fullstate/conditional教師0確認、quality/endpoint選別なし。全source{source_summary['documents']}docs/body{source_summary['body_positions']}/outcome{source_summary['outcome_body_positions']}/prefix{source_summary['prefix_body_positions']}/EOS{source_summary['EOS_positions']}を既小arrayで確認。hard教師数とEOS率は変わるので同教師100Mとは言わず、原reference quota/digestとmasked actual教師/byte/digestを分ける。CPU準備30/GPUprobe120/新全上限600、own実maskedCUDA保存再開/steady32/実測1.3+reserve150+50を満たしてから科学設定凍結。元strong/absolute/歴史全guardを維持、未実装/未起動、GPU/教師0。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    active=ROOT/'reports/phase6/parameter_displacement_anchor_active_job.json';record=read_json(active)
    record.update(status='complete_actual_process_absent',observed_at=now(),actual_process_confirmed_live=False,actual_job_snapshot=job)
    atomic_json(active,record)
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_parameter_anchor_two100M_complete_rejected_conditional_prefix_mask_defined',updated_at=now(),
        parameter_displacement_anchor_active_job=study.reference(active),parameter_displacement_anchor_completion=study.reference(destination),
        conditional_prefix_mask_proposal=study.reference(proposal_path),next_action=completion['next_action'],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=progress['status'],new_GPU_seconds=completion['total_new_GPU_seconds'],
        source_summary=source_summary,shared_checkpoint=shared_update,first_conditional_update=first['update'],portable_files=len(files))))


if __name__=='__main__':main()
