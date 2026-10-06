"""Persist the cached diagnosis and one new source-representation comparison proposal."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import json
import tarfile
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity


def ref(path):return dict(path=str(path),sha256=sha256(path))


def main():
    result_path=ROOT/'reports/phase6/decision_span_diagnostic_result.json';r=read_json(result_path)
    p_path=ROOT/'reports/phase6/decision_span_diagnostic_proposal.json';p=read_json(p_path)
    if (r['status']!='all3_cached_same_input_decision_and_exact_greedy_body_diagnostic_complete'
            or r['proposal']!=ref(p_path) or r['CPU_elapsed_seconds']>10 or r['GPU_seconds'] or r['forward_requests']
            or r['raw_requests_reused']!=3072 or len(r['rows'])!=1536):raise ValueError('Actual full finite cached diagnosis required')
    for source,digest in r['source_sha256'].items():
        if sha256(ROOT/source)!=digest:raise ValueError('Actual diagnostic source differs')
    for model in p['models'].values():
        job=read_json(Path(model['run'])/'job.json')
        if job['status']!='complete' or alive(job):raise ValueError('All compared science processes must be absent')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    if ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290' or ui['busy']:
        raise ValueError('Original idle UI required')
    ui_processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode()
        except (OSError,UnicodeDecodeError):continue
        if '/.venv/bin/' in args and 'scripts/webui.py --port 7860' in args:ui_processes.append(identity(int(path.parent.name)))
    if len(ui_processes)!=1 or not alive(ui_processes[0]):raise ValueError('One actual live original UI process required')
    source_dir=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006')
    m=read_json(source_dir/'manifest.json');train=source_dir/'train-source.json'
    if sha256(train)!=m['train_source_sha256']:raise ValueError('Accepted TRAIN fact source differs')
    control=p['models']['strong_staged_CE'];config=read_json(Path(control['config']['path']))
    proposal_path=ROOT/'reports/phase6/narrative_condition_source_proposal.json'
    if proposal_path.exists():raise ValueError('Preserve next distinct source proposal')
    proposal=dict(status='one_TRAIN_grounded_narrative_representation_source_comparison_proposed',created_at=now(),
        trigger=dict(diagnostic=ref(result_path),previous_pilot=p['trigger']['completion']),
        rejected_teacher_and_public_source_evidence=ref(ROOT/'reports/phase6/public_prose_feasibility_completion.json'),
        hypothesis='Direct native learning of short complete progressing narratives, with the same TRAIN facts but more surface realizations, can generalize better than repeatedly restating finite question/record/outcome forms. Existing local probe gains are not broad Base quality.',
        evidence_limits='The diagnostic rejects hidden late-token preference as the dominant anchor bridge failure:0/256 full-sum-correct/decision-wrong. Exact greedy-body improvement27->68/128 coexists with broad coherence2->5/80 and repetition21->28/80. Narrow source/transfer is a motivated hypothesis, not a unique causal proof or a capacity-limit claim.',
        source=dict(manifest=ref(source_dir/'manifest.json'),train_source=ref(train),accepted_review=ref(source_dir/'content-review.json'),
            families=1024,documents=2048,serialized_tokens=m['serialized_tokens'],body_tokens=m['serialized_tokens']-4096,
            body_plus_EOS_teachers=m['serialized_tokens']-2048,train_entity_bank_size=16,
            semantic_categories=['negation','quantity','time','comparison','entity_reference','causality']),
        new_source=dict(kind='locally_authored_TRAIN_grounded_short_narratives_v1',source='local_programmatic_Japanese_not_public_corpus_or_public_teacher',
            data_directory='/home/aihub_ubuntu/jmicro-data/phase6/narrative-condition-source-20261006',
            selected_fact_families_unchanged=1024,opposed_branches=2,surface_realizations_per_branch=8,prospective_documents=16384,
            semantic_state_families_not_increased=True,new_original_corpus_tokens=0,new_surface_tokens_pending=True,
            design='Eight explicitly authored natural complete2-3sentence realizations per category; retain every accepted TRAIN family/state/branch and progress to an action or observable outcome, without record/question/verdict restatement. Plain Base body+EOS, no role tokens or Chat wrappers.',
            grounding=['Negation: declared initial state plus performed/nonperformed TRAIN action; author a consistent remaining object/state or ensuing action.',
                'Quantity/time/comparison: compute existing TRAIN numbers/operation/longer person exactly; present a coherent scene and ensuing action instead of answer fragments.',
                'Entity reference: preserve the actual TRAIN receiver/sender/original-owner/alias role and active person through the next action.',
                'Causality: retain the existing declared switch/button/position/lever mechanism and its state, with consistent lit/unlit consequence.'],
            split_policy='Consume accepted train-source.json only. No evaluation prefixes, probe candidate text, held-out names/actions/items, protected test or public rejected samples may be used to write/generate training text.',
            limitations='Local finite compositional prose with authored fictional details, not independently sampled natural Japanese or8x semantic evidence. Surface amount/style/length/EOS frequency change together; do not call this an isolated data-quantity or style causal effect.'),
        CPU_preparation=dict(ceiling_seconds=60,seed=2026100691,full_input_limit_tokens=1024,whole_documents=True,
            tokenizer=config['tokenizer'] if 'tokenizer' in config else 'artifacts/phase2/4096/tokenizer.model',
            tokenizer_sha256='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318',
            fixed_content_documents=64,content_sampling='Predeclared stratified64: cover48 category/surface cells with one fixed train draw each, then16 additional fixed unique train draws. Both branches represented overall. No reroll/source filtering after viewing.',
            content_gate='All64 individually read and raw SHA bound; weak<=10/64, unresolved grammar/grounding errors0, all training documents complete and EOS terminated. Failed64 rejects the entire source; do not patch grammar/renderer after freezing its actual pilot or accept only favorable cases.',
            coverage_checks='Every1024 accepted TRAIN family and2branches x8realizations; preserve original semantic state/source provenance, native exact bytes/BOS/body/EOS, no truncation, reserved-role/pad IDs0, exact full-text uniqueness, length/EOS/actual surface-body token disclosure.'),
        proposed_comparison=dict(parent=config['parent'],strong_control=control,primary_CE_quotas=config['arms'][control['arm']],
            main_teachers=100000000,source_order=config['source_order'],shape=config['shapes'],actual_LR=.00001,
            full_parent_model_Adam_scheduler_RNG_preserved=True,ordinary_body_plus_EOS_CE_weight1=True,
            change='Replace only conditional-text source with accepted new prose; use the completed same-parent stagedCE as quality control. No auxiliary rank/KL/anchor.',
            unchanged_other_three_source_sequences_counters_cursors=True,conditional_input_and_EOS_frequency_changes_disclosed=True,
            measured_budget_pending=True,new_GPU_ceiling_seconds_including_all_probes=900,
            CUDA_gate='Own actual continuous4vs2+2 full-state/new-source sampler/counters and32 steady combined update timings; preserve all failed probe costs. Same150second reserve/30%margin/50second slack before100M freeze.',
            quality_criteria_unchanged=True,quality_gate='Strong stagedCE23+8 with pairedCI lower>0/EOS>=76/repetition<=2; original absolute grammar>=56/coherence>=27/appropriate>=27/EOS>=37/repetition<=18/noempty-role-Unicode; historical Web BPB<=.9812859519097707 and existing stop guards.',
            evaluation='Same256 full common bytes/Japanese192-331-1119/all80 individually read raw-bound greedy/bridge128/retention128; existing scorers/decoder/suite splits unchanged.'),
        preserved_related_GPU_seconds=read_json(Path(p['trigger']['completion']['path']))['cumulative_related_GPU_seconds'],
        completion_condition='One accepted finite64 source preparation followed, only if actual CUDA/budget gates pass, by one terminal100M comparison and full review. No renderer/filter/teacher/prompt/LR/source/shape sweep, checkpoint scan, automatic extension, cap enlargement or relaxed quality gates.',
        next_action='Implement owned narrative renderer/full TRAIN preparation/native view and meaningful grounding/codec checks; freeze its input/renderer/sampling before actual preparation; read all fixed64 before student GPU.',
        actual_new_source_documents=0,student_scientific_teacher_tokens=0,GPU_training_started=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        after_qualified_pilot='Independent learned seed/full dev/protected test/adoption, then notify and stop at Base.')
    atomic_json(proposal_path,proposal)
    completion_path=ROOT/'reports/phase6/decision_span_diagnostic_completion.json'
    if completion_path.exists():raise ValueError('Preserve completed diagnostic record')
    atomic_json(completion_path,dict(status='cached_all3_full_decision_span_diagnosis_complete_next_source_comparison_defined',created_at=now(),
        proposal=ref(p_path),result=ref(result_path),CPU_elapsed_seconds=r['CPU_elapsed_seconds'],CPU_ceiling_seconds=10,
        raw_requests_reused=3072,all_context_pair_rows=1536,GPU_seconds=0,forward_requests=0,optimizer_updates=0,
        tests=r['CPU_tests'],summaries=r['summaries'],all_original_full_candidate_aggregates_exactly_reproduced=True,
        all_first_distinct_input_prefixes_identical=True,all_poles_scorable=True,
        maximum_shared_target_NLL_difference=max(v['maximum_shared_target_NLL_difference'] for suites in r['summaries'].values() for suite in suites.values() for key,v in suite.items() if key!='categories'),
        primary_hypothesis_result='Late teacher-forced scores hiding wrong first distinct choice are not the dominant anchor bridge issue:0 such cases;17 retention structural cases remain. This does not motivate a new first-distinct-token loss as the sole broad-quality repair.',
        next_source_proposal=ref(proposal_path),original_UI=ui,original_UI_identity=ui_processes[0],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        quality_criteria_unchanged=True))
    files=[p_path,result_path,completion_path,proposal_path,ROOT/'reports/phase6/decision_span_diagnostic_tests.xml',
        ROOT/'scripts/decision_span_diagnostic.py',ROOT/'scripts/run_decision_span_diagnostic.py',Path(__file__),ROOT/'tests/test_decision_span_diagnostic.py']
    archive=ROOT/'reports/phase6/decision_span_diagnostic_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve diagnostic portable evidence')
    manifest={v.relative_to(ROOT).as_posix():dict(bytes=v.stat().st_size,sha256=sha256(v)) for v in files}
    with tarfile.open(archive,'w:gz') as stream:
        for v in files:stream.add(v,arcname=v.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/decision_span_diagnostic_portable.json',dict(status='actual_cached_diagnostic_and_next_proposal_portable',
        files=manifest,file_count=len(files),raw_bytes=sum(v['bytes'] for v in manifest.values()),archive=ref(archive),
        cached_old_raw_scores_retained_in_their_original_portable_archives=True,new_model_tensors_or_arrays=0))
    a=r['summaries']['positive_anchor'];old=r['summaries']['relative_ranking'];control=r['summaries']['strong_staged_CE']
    prefix=f'''同一入力の選択位置・完全greedy本文診断を完了（2026-10-06 JST）。前turnのpositive-anchor100M/全評価不採用を7afe0bfへ保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

decision_span_diagnostic_result/completion.jsonに強いstagedCE/relative ranking/positive anchorの3実終了model×bridge128/retention128×両context/candidateの全3072既存BF16 score requestsを集計。実CPU{r['CPU_elapsed_seconds']:.6f}秒/上限10、GPU0/newforward0/optimizer0。1536pair rows全てに候補の最初の異なるtarget位置があり、そこまでの完全input IDs一致を確認、共有先行token NLL差最大0。全18cohortと全categoryを保持、元のsum/tokenmean/bytemean・全対照aggregate完全再現。prefix包含を明示するhelper、後続NLLで誤った選択が隠れるcounterexample/argmax連言と候補順位の区別にCPU2tests/.03秒成功。新チェックポイント推論/旧zero-context再測定/巨大index再scanなし。

bridge両極正答（全body/最初distinct選択/完全goldbody greedy）はstaged59/57/31、ranking86/84/27、anchor79/79/68（各128）。anchorでfullsum正解だがdistinct位置が誤りは0/256で、当初疑った後続teacher forcingによる開始選択の隠蔽は主bridge失敗を説明しない。retentionはstaged36/35/15、ranking80/72/14、anchor80/77/32、anchor隠蔽17/256は全て構造cohort。語彙/構造の全分解を残し、小局所のgreedy body改善を自然文一貫性5/80・反復28/80の成功へ置換しない。is_greedyの全target argmax連言は候補body経路を支持するが、その後のEOS停止/新文脈/自然文品質は保証しない。Shared generator/相関poles/teacher forcing/一つのseedの限界を保ち、単独のfirst-distinct loss修正へは進まない。

accepted条件TRAIN sourceは2048docs/serialized89446/body85350/本文+EOS87398、1024facts/16人物/24source表現。例は行動の言い直しを同じ出来事で閉じる記録文。main conditional10Mは同じ小poolの反復で、主Web12Bデータ量と条件・自然文の表現幅を混同しない。これは全corpus品質や唯一原因の証明ではない。既不採用Qwen4B teacher64弱37/publicMagpie64弱23・供給4.23Mも再確認し、そのモデル/prompt/filter/sourceを再試行せず不採用を保持。

次はnarrative_condition_source_proposal.jsonの一つのTRAIN由来自然短文source比較。既accepted1024facts/両branchはそのまま、各category8個の完結2-3文/計16384surface docs案。単なる記録/質問/言い直しから、局所条件を保持して行動/観測結果へ進む文章にする。新独立semantic families/public corpus0、surface量/style/length/EOS頻度も変わるので単純な増量効果とはしない。CPU準備60秒/native4096/wholebody1024上限、予め固定した48category×surface＋16追加の64全読解・weak<=10/未解消grammar-grounding0が必要。不合格からrenderer/filter/rerollで同pilotを合格へ変えない。まだactual source0/学生GPU0。

accepted sourceだけをsame10.5B fullparent/Adam/scheduler/RNG/実LR.00001、Web75M→story5M→ordinary10M→newconditional10M、ordinary body+EOS CE weight1の100Mで強いstagedCE対照へ比較する案。aux rank/KL/anchorなし、変更はconditional source、他3source sequence/cursor/counter一致と変更したconditional physical/EOS頻度を別記。own actualCUDA4vs2+2/32timing/同150秒reserve/30%/50秒＋全probe込み900秒を満たしてから科学設定凍結。元256full bytes/日本語192-331-1119/全80個別読解/bridge-ret128・強いcoherence23+8/CI下限正/EOS>=76/反復<=2・absolute・歴史WebBPB<=.981285952を維持する。品質pilot合格時だけ独立学習seed/full dev/protected test/adoption。GPU科学job0、元10B UI{ui_processes[0]['pid']}/boot{ui_processes[0]['boot_id']}/start{ui_processes[0]['start_ticks']}とHTTP親410f975d…/10000007168/busy=falseを確認。旧Phase0–3/数値7失敗/全基準/関連GPU2289.596018秒を保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        path=ROOT/relative;path.write_text(prefix+path.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_cached_decision_span_complete_narrative_TRAIN_source_comparison_proposed',updated_at=now(),
        decision_span_diagnostic_completion=ref(completion_path),narrative_condition_source_proposal=ref(proposal_path),
        next_action=proposal['next_action'],Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=progress['status'],CPU_seconds=r['CPU_elapsed_seconds'],next_source=str(proposal_path))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
