"""Record completed CPU evidence and one finite Base-only comparison proposal."""
import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports/phase6'


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def ref(path):
    path = Path(path)
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def write_once(path, value):
    if path.exists():
        raise ValueError(f'Preserve existing record: {path}')
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    stamp = datetime.now(timezone.utc).isoformat()
    diagnostic = read(REPORTS / 'context_prior_diagnostic_completion.json')
    inputs = read(REPORTS / 'context_outcome_ranking_input_preparation.json')
    control = read(ROOT / 'configs/phase6/eos_decoupled_web_kl_comparison.json')
    data = Path(inputs['manifest']['path']).parent
    manifest = read(data / 'manifest.json')
    if ref(data / 'manifest.json') != inputs['manifest']:
        raise ValueError('Prepared train manifest differs')
    for path, digest in inputs['source_sha256'].items():
        if ref(ROOT / path)['sha256'] != digest:
            raise ValueError('Prepared train input source differs')
    if ref(data / 'rows.json') != inputs['rows']:
        raise ValueError('Prepared exact candidate text differs')
    tests = {}
    for name in ('context_prior_analysis_tests.xml', 'context_outcome_ranking_tests.xml',
                 'context_outcome_ranking_trainer_tests.xml'):
        suite = ET.parse(REPORTS / name).getroot().find('testsuite')
        if any(int(suite.attrib[k]) for k in ('errors', 'failures', 'skipped')):
            raise ValueError(f'CPU test did not complete: {name}')
        tests[name] = dict(evidence=ref(REPORTS / name), tests=int(suite.attrib['tests']),
                           seconds=float(suite.attrib['time']), device='CPU', actual_GPU_training=False)
    sources = {p: ref(ROOT / p)['sha256'] for p in (
        'scripts/context_outcome_ranking.py', 'scripts/prepare_context_outcome_ranking_inputs.py',
        'scripts/prepare_context_outcome_ranking_trainer.py', 'scripts/context_outcome_ranking_trainer.py',
        'scripts/context_outcome_ranking_resident_trainer.py', 'tests/test_context_outcome_ranking.py',
        'tests/test_context_outcome_ranking_trainer.py')}
    preparation = dict(status='actual_CPU_inputs_and_three_loss_full_resume_complete_GPU_not_started',
        created_at=stamp, diagnostic=ref(REPORTS / 'context_prior_diagnostic_completion.json'),
        input_preparation=ref(REPORTS / 'context_outcome_ranking_input_preparation.json'),
        manifest=inputs['manifest'], rows=inputs['rows'], source_sha256=sources, CPU_tests=tests,
        actual_train_families=inputs['families'], actual_candidate_rows=inputs['candidate_rows'],
        actual_maximum_input_tokens=inputs['maximum_input_length'],
        actual_valid_input_positions=inputs['valid_input_positions'],
        actual_scored_body_positions=inputs['body_outcome_positions'],
        actual_joint_encoding_equal_rows=inputs['whole_joint_tokenization_equal_rows'],
        categories=inputs['categories'], new_original_corpus_tokens=0,
        CPU_input_preparation_seconds=inputs['CPU_elapsed_seconds'],
        GPU_training_seconds=0, scientific_teacher_tokens=0, scientific_optimizer_updates=0,
        full_resume_CPU='Actual tiny model/Adam/scheduler/RNG/main sampler/Web sampler/ranking sampler, all ledgers and digests: continuous4 equals2+2. One Adam update after all3 backward paths; control primary/reference inputs unchanged. This fixture does not qualify CUDA or10M quality.',
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_used=False, quality_criteria_unchanged=True,
        next_action='Implement owned runner/reviewer/durable launcher and actual CUDA full-state4vs2+2 plus32 measured combined updates; freeze one100M comparison only if finite and total new GPU forecast<=900seconds.')
    prep_path = REPORTS / 'context_outcome_ranking_preparation.json'
    write_once(prep_path, preparation)
    proposal = dict(status='one_train_context_ranking_100M_comparison_proposed_CPU_prepared_not_GPU_frozen',
        created_at=stamp, trigger=preparation['diagnostic'], preparation=ref(prep_path),
        question='Does directly supervising reversal of correct continuation across two TRAIN contexts restore contextual discrimination and generation coherence while conditional parent Web KL retains language quality?',
        diagnostic_limit='BOS-only arithmetic decomposition supports weaker contextual separation rather than prior-only offset; it is not a causal parameter attribution or proof of zero context use.',
        parent=control['parent'], mechanism_control_config=ref(ROOT / 'configs/phase6/eos_decoupled_web_kl_comparison.json'),
        mechanism_control_completion=ref(REPORTS / 'eos_decoupled_web_kl_comparison_completion.json'),
        mandatory_stronger_quality_control_config=ref(ROOT / 'configs/phase6/source_order_condition_comparison_v2.json'),
        pool=control['pool'], original_web=control['original_web'], positive_data=control['positive_data'],
        ranking_inputs=inputs['manifest'], resident_input_preparation=ref(REPORTS / 'web_kl_resident_window_preparation.json'),
        fixed_primary=dict(ordinary_CE_teachers=100000000, input_positions=100532224, updates=3068,
            quotas=dict(web=75000000, story=5000000, ordinary_textbook=10000000, conditional_textbook=10000000),
            order=['web', 'story', 'ordinary_textbook', 'conditional_textbook'],
            parent_state='Same historical10.5B fullstate; inherit model/Adam/scheduler/RNG, actualLR.00001; no reset/reheat.',
            shape=dict(batch=32, context=1024, dtype='bf16', backend='flash', compile_mode='reduce-overhead', accumulation=1)),
        fixed_Web_reference=dict(batch=8, context=1024, input_positions=25133056,
            conditional_non_EOS_parent_KL_coefficient=1,
            original_control_body_positions=25026383,
            retained_probability_mass_is_not_integer_teacher_count=True,
            main_and_Web_reference_positions=125665280,
            immutable_parent=True, separate_cursor=True),
        one_new_auxiliary=dict(kind='train_opposite_context_non_EOS_outcome_ranking_v1',
            families_per_update=2, candidate_rows_per_family=4, context=256,
            coefficient=1, temperature=1, score='mean complete-body conditional nonEOS token log-likelihood',
            loss='mean softplus(foil_score-gold_score) across both opposite contexts',
            labels='Existing accepted TRAIN family labels; correct outcome under the opposite context is the foil.',
            sampler='Independent local seed42 deterministic shuffle of all1024 families; cyclic order, full state/digest saved.',
            implementation='Main CE and Web reference keep compiled flash; padded short ranking batch eager BF16 math attention. All3 gradients combine before one clip/Adam/scheduler update.',
            ordinary_CE_teacher_tokens=0, soft_distribution_target_positions=0,
            proposed_family_presentations=6136, proposed_relational_choice_labels=12272,
            proposed_padded_input_positions=6283264, proposed_combined_student_padded_positions=131948544,
            measured_counts_pending=['valid_input_tokens', 'gold_body_scored_positions', 'foil_body_scored_positions',
                                     'gold_body_scored_bytes', 'foil_body_scored_bytes'],
            disclosure='Extra context/foil exposures and relational supervision differ from control. Equal mainCE and reference windows do not imply equal total input/supervision or GPU cost.',
            EOS_limit='EOS3 excluded from this auxiliary normalization/targets; direct auxiliary EOS-logit gradient zero, shared parameters and ordinaryCE may still change EOS.'),
        data_limits=['No new corpus; reuse all1024 accepted TRAIN families, both contexts and their existing two outcomes.',
                     'No dev/bridge/retention/protected-test inputs or labels for learning; no family selection by evaluation.',
                     'Local generated families share rules and some forms with evaluation probes; probe gains alone do not prove independent language quality.'],
        actual_CUDA_gate_pending=True, proposed_new_GPU_ceiling_seconds=900,
        budget_gate='Measure actual CUDA full resume4vs2+2 and32 combined timings, preserve every failed/exhausted cost; forecast3068updates plus150seconds nontraining reserve,30%margin and50seconds slack plus probes must fit900seconds before scientificfreeze. Do not expand cap after rejection.',
        evaluation=['Same full256 dev472055bytes/122343bodytokens, fixed Japanese192/331/1119',
                    'Same80 greedy max64 completions and all80 individual raw-bound content grading',
                    'Same bridge128 and retention128 families, exact candidate sum/token/byte likelihood reported separately',
                    'All3068 primary/reference input/mask/digest/counter checks against cached conditionalKL; new ranking exposure ledgers separate'],
        quality_gate=dict(relative_to_staged_CE=dict(coherence_minimum=31, coherence_gain_minimum=8,
            paired_CI_lower_strictly_positive=True, EOS_minimum=76, repetition_maximum=2, BPB_maximum=1.1336128657420816*1.01),
            absolute=dict(grammar_minimum=56, coherence_minimum=27, appropriate_completion_minimum=27,
                EOS_minimum=37, repetition_maximum=18, empty_role_Unicode_errors_maximum=0),
            historical_Web_BPB_maximum=.9812859519097707,
            same_quality_criteria_unchanged=True,
            no_easing_to_failed_mechanism_control=True),
        completion_condition='One terminal100M arm, full bounded evaluation/all80 notes/input-ledger audit/adoption review. No coefficient/temperature/margin/source/order/LR/batch sweep, favorable checkpoint search or automatic extension. A rejected arm is useful evidence, not Base completion.',
        adoption_after_pilot='Only an actually qualified quality pilot advances to independent learned seed, full dev and protected-test evidence; notify user and stop after actual adopted Base.',
        deferred=['Chat', 'Dialogue', 'SFT', 'quantization', 'final deployment'],
        Base_complete=False, protected_test_used=False)
    proposal_path = REPORTS / 'context_outcome_ranking_proposal.json'
    write_once(proposal_path, proposal)
    prefix = '''文脈と候補priorの有限CPU診断を完了・train文脈比較損失を準備（2026-10-06 JST）。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止する。Baseは未完了・未採用。Chat/Dialogue/SFT/量子化は開始しない。

context_prior_diagnostic_completion.jsonに実4checkpoint/2suite/全256familyのoriginal4096と同じtargetを保つBOS-only4096、計8192requestsをCPU FP32/math/eval/no-gradで保存。実16.773451秒/上限180、GPU0、全4modelの重み/RNG/grad/eval/device/CUDA未初期化checks合格、actual603932は終了・ps不在。元GPU BF16とCPU FP32を混ぜて引かず、採用値をCPU補正で置換しない。conditionalKL→gold replayのbridgeは両極正答53→40/128、喪失13/獲得0。算術切り分けで文脈側変化だけで喪失10、priorだけ0、どちら単独でも2、両方必要1。retention32→22、喪失13/獲得3、文脈だけ11/priorだけ1/どちらでも1。単純prior offsetだけが主因という仮説は支持せず、文脈分離の弱まりを支持する局所診断。BOS-onlyの位置/文法差、shared generator/形重複、算術交換が実現可能なモデル変更/因果証明ではない限界を保持する。全family/category/3normalizers/raw scoreを保存。

診断可搬547text/17,565,308rawbytes、gzip1,972,432/ SHA3c1091bb513b7093c45b08b79f3e6d9aaf5ae97217ae2d631cd456419cfce27d。Windows raw/archive SHA確認。CPU診断2tests合格。launcherはWindows側にありnative側のcopyはパス不在で中止したが、実診断・archiveは正常完了、再診断/予算追加なし。

context_outcome_ranking_preparation.jsonとproposal.jsonを保存。新corpus0、既存accepted TRAIN1024family/2048positive recordsの反対文脈/共有2outcomesから4096candidate rowsを実CPU.215551秒/60で用意。joint encoding全4096一致、max74tokens、valid170700/body24604、prefix/pad/EOSはaux教師外。固定2family/update、8x256、conditional nonEOS mean-body logPのsoftplus(foil-gold)、係数/温度1。従来main100MCEと同Web参照conditionalKLを保ち、rankは別のrelational supervisionでありCE教師/soft target数へ足さない。計画上6136family presentations/12272choice labels/6283264padded positions、combined131948544を別会計し、valid/gold/foil/bytesは実samplerで測る。

owned context_outcome_ranking_trainer.py/resident adaptorはmain CE→Web KL→短いpad付きrankの3backward後に1回clip/Adam/scheduler。main/ref compiled flashは維持しrankはeager BF16 math案。実CPU loss/直接EOS勾配ゼロ/文脈反転・global候補bias、local shuffle/globalRNG不変、全state連続4対2+2と3samplers/全ledger/digest一致、main/ref control入力一致に3tests合格（rank2/fulltrainer1）。これはfixtureで実10M CUDA/品質の証明ではない。科学GPU0・科学追加教師0・CUDA gate未実施・科学config未凍結。

次はowned runner/reviewer/durable launcherとactual CUDA連続4対2+2＋32combined timings→従来150秒非学習枠/30%/50秒余裕＋全probe costs込み900秒内なら単一100M比較だけ凍結/実施→同256全文/日本語/全80内容/bridge-retention/全3068入力と新rank台帳の採否。control conditionalKLは機序対照、採用は強い元staged CE23+8/CI lower>0/EOS>=76/反復<=2、既存absoluteと歴史Web BPB<=.981285952を維持する。失敗済gold replayのvariant・設定sweep・量だけの延長・有利CP探索なし。品質pilot合格後だけ独立学習seed/full dev/protected test。元10B UI599823/同boot/start15623625とHTTP親410f975d…/10,000,007,168/busy=falseを確認、CPU作業で停止しない。WSL uv3.12.7/local commitのみ/pushなし。旧Phase0–3/数値7失敗・品質基準・過去費用は保持。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md', 'docs/15_project_roadmap.md', 'docs/windows_handoff.md'):
        path = ROOT / relative
        path.write_text(prefix + path.read_text(encoding='utf-8'), encoding='utf-8')
    progress_path = REPORTS / 'five_step_progress.json'
    progress = read(progress_path)
    progress.update(status='Base_only_context_prior_diagnostic_complete_train_outcome_ranking_CPU_prepared_GPU_pending',
        last_updated_at=stamp, context_prior_diagnostic_completion=ref(REPORTS / 'context_prior_diagnostic_completion.json'),
        context_outcome_ranking_preparation=ref(prep_path), context_outcome_ranking_proposal=ref(proposal_path),
        next_action=preparation['next_action'], Base_complete=False, Chat_started=False, quantization_started=False)
    progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Recorded actual CPU diagnostic/prototype, one bounded proposal and Base-only stop boundary; GPU not started.')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
