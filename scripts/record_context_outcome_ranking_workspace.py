"""Record terminal study, restored original UI, and one evidence-based positive-anchor proposal."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import urllib.request
import json
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_context_outcome_ranking_comparison as study


def ref(path):return dict(path=str(path),sha256=sha256(path))


def main():
    completion_path=ROOT/'reports/phase6/context_outcome_ranking_comparison_completion.json'
    completion=read_json(completion_path)
    analysis_path=ROOT/'reports/phase6/context_outcome_ranking_absolute_likelihood.json'
    analysis=read_json(analysis_path);r=read_json(study.RUN/'compare-result.json');c=read_json(study.CONFIG)
    if completion['eligible_for_final_Base_validation'] or completion['Base_complete']:
        raise ValueError('This postprocessing route is only for the actually rejected pilot')
    job=read_json(study.RUN/'job.json')
    if alive(job) or job['status']!='complete':raise ValueError('Actual terminal science process required')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        ui=json.load(response)
    original_SHA='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    if ui['checkpoint_sha256']!=original_SHA or ui['training_tokens']!=10000007168 or ui['busy']:
        raise ValueError('Original unchanged10B UI required')
    matches=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode()
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '/.venv/bin/' in args:
            fields=(path.parent/'stat').read_text().rsplit(')',1)[1].split()
            matches.append(dict(pid=int(path.parent.name),start_ticks=fields[19],
                boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),args=args.strip()))
    if len(matches)!=1 or not alive(matches[0]):raise ValueError('One actual original UI process required')
    target=ROOT/'reports/phase6/context_outcome_ranking_workspace_completion.json'
    if target.exists():raise ValueError('Preserve terminal workspace observation')
    atomic_json(target,dict(status='rejected_pilot_raw_evidence_recorded_original_UI_restored',created_at=now(),
        completion=ref(completion_path),absolute_candidate_likelihood_analysis=ref(analysis_path),
        actual_scientific_process_absent=True,original_UI=ui,original_UI_identity=matches[0],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True))
    proposal_path=ROOT/'reports/phase6/anchored_context_outcome_proposal.json'
    if proposal_path.exists():raise ValueError('Preserve next one-factor proposal')
    s=completion['summaries'][study.ARM];mechanism=completion['mechanism_summary'];exposure=completion['ranking_exposure']
    proposal=dict(status='one_positive_likelihood_anchor_comparison_proposed_not_implemented_or_GPU_frozen',created_at=now(),
        trigger=dict(completion=ref(completion_path),absolute_likelihood_analysis=ref(analysis_path),
            fixed_bridge_both_correct=86,conditional_KL_bridge_both_correct=54,
            fixed_retention_both_correct=80,conditional_KL_retention_both_correct=33,
            coherence2_to11_vs2=True,
            bridge_gold_NLL_per_token=.28322682306261077,rank_bridge_gold_NLL_per_token=1.9090504258847054,
            bridge_gold_likelihood_worse_context_poles=180,retention_gold_likelihood_worse_context_poles=210,
            note='All256 poles in each128-family suite; correlated poles are not independent samples. Absolute gold likelihood decreases in many cases while foil decreases further.'),
        hypothesis='Relative outcome ranking has no absolute-gold likelihood floor. Add a positive likelihood term on the same TRAIN correct-outcome rows to test whether discrimination gains can coexist with useful continuation probabilities and broad generation quality.',
        causal_limit='Cached likelihood arithmetic and repeated nonblind dev support this mechanism hypothesis, not a unique causal proof. Shared generator/familiar forms and structural drift remain limits.',
        new_action='One single added gold-body conditional nonEOS CE term; comparison weights all fixed at1, no coefficient/temperature/margin sweep.',
        parent=c['parent'],reused_ranking_control=dict(config=ref(study.CONFIG),result=ref(study.RUN/'compare-result.json'),
            review=ref(study.RUN/'review.json'),completion=ref(completion_path),checkpoint=completion['checkpoint']),
        stronger_staged_CE_quality_control=c['reused_control_checkpoint'],
        fixed_main=dict(ordinary_CE_teachers=100000000,quotas=study.GOALS,source_order=list(study.SOURCE_ORDER),
            shape=c['shapes'],full_parent_model_Adam_scheduler_RNG_inherited=True,actual_LR=.00001,
            no_reset_or_reheat=True),
        fixed_Web_reference=dict(policy=c['KL_policy'],same_parent=True,same_8x1024_windows=True,
            physical_positions=25133056,conditional_nonEOS_KL_coefficient=1),
        fixed_pair_inputs=dict(manifest=c['ranking_inputs'],policy=c['ranking_policy'],same_sampler_seed42=True,
            families_per_update=2,candidate_rows_per_family=4,context=256,all_existing_train1024_families=True,
            new_original_corpus_tokens=0,dev_bridge_retention_protected_test_used_for_learning=False,
            extra_input_exposures_relative_to_ranking_control=0),
        positive_anchor=dict(source='Correct candidate rows already present in each frozen TRAIN family batch; no new outcomes/labels/prefixes.',
            loss='Conditional nonEOS gold-body CE, sum over all correct body positions divided by their actual count; prefix/padding ignored.',
            coefficient=1,ranking_coefficient=1,temperature=1,
            direct_EOS_logit_gradient_zero=True,EOS_id3_excluded_from_normalization_and_aux_labels=True,
            implementation='Reuse existing eager BF16 math paired-batch logits; combine ranking and positive anchor before backward, then one clip/Adam/scheduler update after mainCE and WebKL.',
            expected_separately_counted_auxiliary_gold_body_teacher_positions=73725,
            expected_combined_main_and_auxiliary_hard_teacher_positions=100073725,
            supervision_disclosure='Input order/shape and total physical exposure equal completed ranking control, but adds gold-body hard supervision. Integer teachers, relational labels and frozen-parent probability mass remain separate.'),
        prospective_run=dict(main_updates=3068,main_input_positions=100532224,
            ranking_padded_positions=6283264,combined_student_padded_positions=131948544,
            same32_main_Web_rank_input_and_mask_digests_required_for_probe=True,
            same3068_main_Web_rank_input_and_mask_digests_required_for_science=True,
            ranking_sampler_checkpoint_resume_exact=True),
        measured_budget_pending=True,new_total_GPU_ceiling_seconds=900,
        budget_gate='Owned actual CUDA4vs2+2 including positive-anchor losses/counts and32 combined timings. Preserve failed/refused costs. Forecast3068updates plus same150second nontraining reserve,30%margin and50second slack plus all new probe costs must fit900 before scientific freeze.',
        earlier_related_GPU_seconds_preserved=completion['cumulative_related_GPU_seconds'],
        quality_criteria_unchanged=True,
        mandatory_quality_gate='Stronger original stagedCE: coherence>=31 and gain>=8/80 with pairedCI lower>0, EOS>=76/repetition<=2/common-byte BPB<=1.1336128657420816*1.01; absolute grammar>=56/coherence>=27/appropriate>=27/EOS>=37/repetition<=18/noempty-role-Unicode; historical-Web BPB<=.9812859519097707 plus existing EOS/repetition/punctuation guards. Never adopt from probe accuracy alone or ease control.',
        evaluation='Same256 full common bytes/Japanese192-331-1119/all80 greedy and individually read raw-bound notes/bridge128/retention128; report absolute gold and foil NLL separately, not only margin accuracy.',
        completion_condition='One terminal100M comparison with full accounting/quality review; no automatic extension/favorable checkpoint search/settings sweep. Pilot quality success alone does not complete Base.',
        after_qualified_pilot='Independent learned seed/full dev/protected test/adoption; notify user and stop after actually qualified Base.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        next_action='Implement owned positive-anchor loss/trainer/accountant/runner; CPU masks/directEOS gradient/full-state3samplers resume; then actual CUDA fullresume/timing and measured-budget freeze only if valid. No new GPU learning until its own gate passes.')
    atomic_json(proposal_path,proposal)
    portable=read_json(ROOT/'reports/phase6/context_outcome_ranking_comparison_portable.json')
    a=analysis['summaries']['bridge']['all128'];b=analysis['summaries']['retention']['all128']
    prefix=f'''train文脈比較100Mと全評価を完了・不採用（2026-10-06 JST）。実CUDA53checks/永続起動はdf3e2a3へ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続、実完成時に通知して停止。Base未完了・未採用。Chat/Dialogue/SFT/量子化なし。

actual610335/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15803746はcomplete・実ps不在。main100,000,000CE教師/maininput100,532,224/3068更新、CP323503 SHA{completion['checkpoint']['sha256']}。同reference25,133,056input/25,026,383body positions/parent非EOS mass24,981,892.629882812。rank6136family presentations/12272relational labels/1,022,980valid/6,283,264padded/gold73,725・foil73,725位置/gold315,047・foil315,047bytes、combined131,948,544physical/126,688,260validを別計数。rankはCE教師0/soft targets0、新corpus0。全3068主/参照input-mask-digest-sourceとmassがconditionalKLと一致、全rank入力/順序/digest/会計を再現監査、全4終端source cursors一致。

train{completion['training_seconds']:.6f}秒、science GPU{completion['science_GPU_seconds']:.6f}＋probe{completion['verification_GPU_seconds']:.6f}=新全{completion['current_study_all_GPU_seconds']:.6f}秒<900。旧関連1173.595391秒を消さず累積{completion['cumulative_related_GPU_seconds']:.6f}秒。検証40更新/CE1,307,967/reference327,680/body326,339/mass325,778.16796875/rank80family・160labels・81920paddedは科学学習へ加算しない。

conditionalKL→rank: BPB.983031489→{s['BPB']:.9f}悪化、文法2=58→{s['grammar2']}/関連2=49→{s['relevance2']}/一貫性2=11→{s['coherent']}/適切28→{s['appropriate']}/EOS44→{s['rates']['eos']}/自動反復20→{s['rates']['repetition']}、Unicode-role-empty0（各80）。一貫性差-9/paired95%CI[-.1875,-.0375]、強いstaged CE23に対して-21/CI[-.3625,-.1625]。relative/absolute/歴史Web BPB guard失敗、不採用。意味57.292→59.375%/JBLiMP74.320→75.227%/JCQA33.959%同値でもBase完成とはしない。

bridge両極正答54→86/128、語彙42→63/64・構造12→23/64、同候補70→22、文脈反転方向98→102。retention33→80/128。全256全文472055bytes/122343bodytokens、日本語192-331-1119、全80greedy64と全80個別読解（77新観察/同id-prefix-raw-stop3件だけ旧notes再利用）を保存。nonblind Codexで独立人間なし。選択式の改善と生成品質の大幅悪化を両方保持する。

既存BF16 rawのみを用いる全256familyのgold/foil方向分析を実CPU{analysis['CPU_elapsed_seconds']:.6f}秒/上限10、GPU0/新forward0で完了。bridge256polesの正解NLL悪化180、誤候補悪化208、margin改善190うち両候補とも悪化したのにmargin改善120。gold平均tokenNLL.283227→1.909050、foil.457043→4.096298。retention正解悪化210/foil悪化250、両方悪化＋margin改善153、gold.933116→2.238642/foil1.094956→5.052400。語彙bridge first-gold-tokenは.544424→.306681改善だが全goldbody.305072→.824021悪化、構造goldbody.260030→3.061216。相対選好の成功を正解そのものの生成確率/自然文品質の成功へ置換しない。これはteacher-forced/shared-generatorの算術診断で、zero-context/唯一の因果やtop1成功の証明ではない。CPU FP32との数値混合なし。

可搬{portable['file_count']}text/{portable['raw_bytes']:,}rawbytes、gzip{portable['archive_bytes']:,}/SHA{portable['archive']['sha256']}を保存。モデルtensors/dataarraysはnativeのみ。workspace metadataと次proposalはarchive後の別記録。元10B UI{matches[0]['pid']}/同boot/start{matches[0]['start_ticks']}のlive identity・HTTP親410f975d…/10,000,007,168/busy=falseを確認、failed pilotをUIへ置換しない。

次はanchored_context_outcome_proposal.jsonの単一positive likelihood anchor比較をowned実装。親fullstate/実LR.00001・main100M・WebconditionalKL・同pair8x256/入力/順序/全露出を保ち、同TRAIN正解bodyへconditional非EOS CE係数1だけ追加、ranking係数/温度1を保持する。既存gold73,725位置が新hard教師となりmain込み100,073,725教師（別監査）、新corpus/追加入力0、foilはhard教師にしない。EOS3/prefix/padはauxから除外しsharedparameter/MainCEのEOS変化は許容し実測する。まだ新prototype/CUDA/science0・新config未凍結。CPU masks/gradient/fullstate→actualCUDA4vs2+2と32combined timings→従来150秒/30%/50秒余裕＋全probe込み900秒なら単一100M→同全評価/全80/絶対gold NLLとmargin/全3068会計・元強い基準で採否。設定sweep/自動延長/有利CP探索なし。pilot合格後だけ独立学習seed/full dev/protected test、Base完成時通知して停止。旧Phase0–3/数値7失敗/全品質条件/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(),encoding='utf-8')
    path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(path)
    progress.update(status='Base_only_context_ranking100M_fully_reviewed_rejected_positive_anchor_proposed',last_updated_at=now(),
        context_outcome_ranking_completion=ref(completion_path),context_outcome_ranking_workspace_completion=ref(target),
        context_outcome_ranking_absolute_likelihood=ref(analysis_path),anchored_context_outcome_proposal=ref(proposal_path),
        next_action=proposal['next_action'],Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(path,progress)
    print(dict(status='rejected100M_and_gold_foil_diagnosis_recorded_one_anchor_proposed',UI_identity=matches[0]),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
