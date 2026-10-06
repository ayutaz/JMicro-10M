"""Record the rejected finished pilot, restored UI and one bounded cached-score next action."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import json
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity
import run_anchored_context_outcome_comparison as study


def ref(path):return dict(path=str(path),sha256=sha256(path))


def main():
    complete_path=ROOT/'reports/phase6/anchored_context_outcome_comparison_completion.json'
    complete=read_json(complete_path);analysis_path=ROOT/'reports/phase6/anchored_context_outcome_absolute_likelihood.json'
    analysis=read_json(analysis_path);config=read_json(study.CONFIG);result=read_json(study.RUN/'compare-result.json')
    job=read_json(study.RUN/'job.json')
    if alive(job) or job['status']!='complete' or complete['eligible_for_final_Base_validation']:
        raise ValueError('This route requires the actually terminal rejected pilot')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    if (ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or ui['training_tokens']!=10000007168 or ui['busy']):raise ValueError('Original10B UI required')
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode()
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '/.venv/bin/' in args:processes.append(identity(int(path.parent.name)))
    if len(processes)!=1 or not alive(processes[0]):raise ValueError('One actual live UI identity required')
    proposal_path=ROOT/'reports/phase6/decision_span_diagnostic_proposal.json'
    if proposal_path.exists():raise ValueError('Preserve next bounded diagnostic proposal')
    models={}
    for name,run,arm,cfg in (('strong_staged_CE',study.cached.RUN,study.cached.ARM,study.cached.CONFIG),
            ('relative_ranking',study.MECHANISM_RUN,study.MECHANISM_ARM,study.base_study.CONFIG),
            ('positive_anchor',study.RUN,study.ARM,study.CONFIG)):
        data=read_json(run/'compare-result.json');record=data['checkpoints'][arm]
        prior=read_json(run/'job.json')
        if prior['status']!='complete' or alive(prior):raise ValueError('All cached scored model processes must be terminal')
        models[name]=dict(run=str(run),arm=arm,config=ref(cfg),result=ref(run/'compare-result.json'),
            checkpoint=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
    proposal=dict(status='one_cached_same_input_decision_span_and_exact_greedy_body_diagnostic_proposed',created_at=now(),
        trigger=dict(completion=ref(complete_path),absolute_likelihood=ref(analysis_path)),models=models,
        source_cases=config['references']['source_cases'],retention_cases=config['references']['retention_cases'],
        scorer_implementation=ref(ROOT/'src/jmicro/japanese_evaluation.py'),
        question='Does whole-candidate preference depend on later teacher-forced tokens while the first different choice token is incorrectly preferred, especially on unseen forms?',
        rationale='Positive anchor improves bridge body gold NLL1.90905->.69749 but structural first-gold NLL3.17460->5.16281; broad greedy80 coherence remains5 and loops28. Need the same-input decision and already saved all-token argmax conjunction before choosing the next learning objective.',
        fixed_scope='All3 completed models, both existing128-family suites, all256 context poles per suite, all3072 cached request records. No family/category/model selection.',
        CPU_ceiling_seconds=10,GPU_seconds=0,forward_requests=0,optimizer_updates=0,new_original_corpus_tokens=0,
        procedure=['Validate bound config/checkpoint/cases/source SHAs and actually terminal processes. Reuse same CUDA BF16/math raw token_nll and is_greedy; no CPU FP32 inference or subtraction.',
            'For each opposed-candidate context, locate the first differing target ID. Prove complete prefix and every prior target ID are identical before comparing its two token NLLs. Report identical/prefix-only unscorable cases explicitly; never add EOS/pad targets.',
            'Report full sum/tokenmean candidate preference, same-input distinguishing-token preference, gold decision NLL, subsequent gold-token NLL and disagreements. Also count cached is_greedy conjunctions for the entire gold body and both context poles.',
            'Aggregate all/lexical/structural/category counts with unchanged denominators, keep ties and all per-family rows. Shared-generator correlated contexts do not become independent samples.',
            'Use result to define one distinct bounded Base learning comparison; preserve existing quality criteria and do not start GPU variants automatically.'],
        limits=['This is a cached teacher-forced decomposition, not independent natural-language quality or unique causal proof.',
            'is_greedy means all target positions are argmax under their preceding target IDs. Its conjunction supports an exact greedy body path; EOS after that body and broader open generation remain unproved.',
            'If differentiating-token preference fails while complete-body ranking passes, later candidate-conditioned scores can conceal initiation errors; this does not license score/decoder/acceptance changes.',
            'No repetition of checkpoint-wide zero-context scoring, source sweeps, first-token departure search or new corpus conversion.'],
        completion_condition='One terminal bound finite CPU report with every model/suite/family accounted, or exact failure/cap record; no cap expansion.',
        protected_test_used=False,Base_complete=False,Chat_started=False,quantization_started=False,quality_criteria_unchanged=True)
    atomic_json(proposal_path,proposal)
    target=ROOT/'reports/phase6/anchored_context_outcome_workspace_completion.json'
    if target.exists():raise ValueError('Preserve terminal workspace observation')
    atomic_json(target,dict(status='rejected_positive_anchor_pilot_all_evidence_recorded_original_UI_restored',created_at=now(),
        completion=ref(complete_path),absolute_likelihood_analysis=ref(analysis_path),next_proposal=ref(proposal_path),
        actual_scientific_process_absent=True,original_UI=ui,original_UI_identity=processes[0],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True))
    portable=read_json(ROOT/'reports/phase6/anchored_context_outcome_comparison_portable.json')
    s=complete['summaries'][study.ARM];b=analysis['summaries']['bridge'];r=analysis['summaries']['retention']
    prefix=f'''正解確率を加えた単一100M比較と全評価を完了・不採用（2026-10-06 JST）。実CUDA58checksと永続開始を45cd1faへ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}はcomplete・実identity不在。main100000000CE教師/maininput{complete['main_input_positions']}/3068更新、CP323503 SHA{complete['checkpoint']['sha256']}。同Webreference{complete['reference_input_positions']}input/{complete['reference_body_positions']}body/親nonEOS mass{complete['reference_non_EOS_teacher_probability_mass']}。同rank6136family presentations/12272relational labels/1022980valid/6283264padded/gold73725・foil73725位置/gold315047・foil315047bytes。positive CEに正解73725 hard教師を別計数しmain込み100073725、combined physical131948544/valid126688260。新corpus/追加input relative to ranking0。全3068main/Web/pair入力・mask digest・親massと全cursor一致、全rank/newhard台帳を再現監査。

train{complete['training_seconds']:.6f}秒、science GPU{complete['science_GPU_seconds']:.6f}+probe{complete['verification_GPU_seconds']:.6f}=新全{complete['current_study_all_GPU_seconds']:.6f}秒<900。旧関連1734.837644秒を消さず累積{complete['cumulative_related_GPU_seconds']:.6f}秒。40検証更新/main1307967/positivehard933/rank160choice labels81920paddedは科学学習へ加算しない。

ranking→anchor: BPB.988409457→{s['BPB']:.9f}悪化、文法2=37→{s['grammar2']}/関連2=41→{s['relevance2']}/一貫性2=2→{s['coherent']}/適切22→{s['appropriate']}/EOS41→{s['rates']['eos']}/自動反復21→{s['rates']['repetition']}、Unicode-role-empty0（各80）。一貫性差+3/paired95%CI[-.0125,.0875]で有意改善の証明なし。強いstagedCE23に対し-18/CI[-.325,-.125]、relative/absolute/歴史Web1% BPB guard未達、不採用。意味59.375→67.1875%/JBLiMP75.227→76.435%/JCQA33.959→34.942%の改善を文章品質/完成Baseへ置換しない。

bridge両極正答86→79/128（語彙63→63/64・構造23→16/64）、retention80→80/128。同256全文472055bytes/122343bodytokens、日本語192-331-1119、全80greedy64を完了。全80を個別に読み78新観察/同id-prefix-raw-stop2件だけ旧notesを再利用し、raw SHA/rationale/TSVとreview/completionを保存。非blind Codex、独立人間なし。新しい人物/幻想/自然な別継続をgold不一致だけで落とさず、数値の誤りは文法とは別に判定した。

全256familyの既存BF16 raw2048requestsだけを実CPU{analysis['CPU_elapsed_seconds']:.6f}秒/上限10、GPU0/新forward0で集計。bridge全gold平均tokenNLL1.909050→.697495・222/256 poles改善、foil4.096298→2.661693。一方、構造gold全body3.061216→1.374313でもfirst-gold3.174599→5.162815悪化。語彙first-gold.306681→.055691改善を隠さず、全体first1.740640→2.609253。retention全gold2.238642→1.257412・215/256改善でも全first3.495138→4.053743、構造first3.858534→5.374053悪化。teacher-forced後続の改善と開始位置/自然文の保持を分ける。唯一因果/全vocab top1成功の証明ではない。

可搬{portable['file_count']}text/{portable['raw_bytes']}rawbytes、gzip{portable['archive_bytes']}/SHA{portable['archive']['sha256']}を保存。モデルtensor/dataarraysはnativeのみ、workspace metadata/次proposalはarchive後の別記録。元10B UI{processes[0]['pid']}/同boot/start{processes[0]['start_ticks']}のlive identityとHTTP元CP410f975d…/10000007168/busy=falseを確認、failed candidateをUIへ置換しない。GPU科学job0。

この単一anchor比較は終了し、係数/温度/normalizer/order/LR/source/batch sweep、cap拡張、自動延長/有利CP探索を行わない。次はdecision_span_diagnostic_proposal.jsonの単一cached CPU診断（上限10秒/GPU0/newforward0）を実装・実行。強いstagedCE/relative ranking/anchorの3実終了model、同bridge128/retention128、全3072保存済scoresを用い、候補が初めて異なる位置まで入力が同一であることを確認してその位置の正解対foil確率と全body選好を比べる。prefix包含等の測れないcaseは除外を隠さず別記、EOS/padを勝手に補わない。保存済is_greedy全target argmaxの連言も集計し、完全gold body経路とEOS後の停止/自然文品質を区別する。全family/両context/3modelを記録し、後続teacher forcingに隠れた開始選択の誤りが実際に支持されるかから次の一つの有限Base学習条件を定義する。CPU FP32再推論/旧zero-context再診断/巨大source再scanなし。pilot品質合格時だけ独立学習seed/full dev/protected testへ進む。旧Phase0–3/数値7失敗/全品質条件/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_positive_anchor100M_fully_reviewed_rejected_decision_span_diagnostic_proposed',updated_at=now(),
        Base_complete=False,Chat_started=False,quantization_started=False,
        anchored_context_outcome_completion=ref(complete_path),anchored_context_outcome_workspace_completion=ref(target),
        anchored_context_outcome_absolute_likelihood=ref(analysis_path),decision_span_diagnostic_proposal=ref(proposal_path),
        next_action='Implement/run one10second cached same-input decision-span and exact-greedy-body diagnostic across all3 completed models/all256 fixed families, then define one distinct bounded Base learning comparison from the result. No new GPU variant automatically.')
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=progress['status'],UI_identity=processes[0],next_proposal=str(proposal_path))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
