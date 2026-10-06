"""Portable evidence; field computation is not trained Base completion."""
import argparse
import json
import os
from pathlib import Path
import sys
import tarfile

os.environ['CUDA_VISIBLE_DEVICES'] = ''
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import build_fisher_parameter_field as study


def main(phase):
    config = study.inspect()
    destination = ROOT/f'reports/phase6/fisher_parameter_field_{phase}.json'
    if destination.exists(): raise ValueError('Preserve original field milestone')
    report = dict(status='Fisher_parameter_field_'+phase, created_at=now(),
        config=study.uniform.reference(study.CONFIG), proposal=study.uniform.reference(study.PROPOSAL),
        CPU_preparation_seconds=config['CPU_preparation_seconds'], GPU_seconds=0,
        source_CE_teacher_tokens=0, optimizer_updates=0, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False,
        quality_criteria_unchanged=True, original_UI=original_UI())
    detail = ('一律L2の完了済み不採用対照に対し、同mixed親/継承Adam・LR.00001/同full100M CE・source・mask・lambda.04161064039180984を保ち、'
        'model-sampled conditional diagonal Fisherのglobal unique-coordinate mean1で重み別抑制を行う別案。'
        '同TRAIN32窓/2反復/seed2026100647、行sum NLLをsqrt(全body32638)で割り、行score gradient二乗を和/2するtoken-weighted推定。'
        'GT empirical Fisher/全joint Fisher/Hessian/有限NLL保持の証明ではない。'
        f'関連CPU4tests/1.97秒（独立ラベルの全列挙期待値、tied/一律一致/非有限拒否、private RNG不変、native全state4対2+2と改変拒否）、準備{config["CPU_preparation_seconds"]:.6f}秒。'
        '新GPU/本学習0。次はfield64 gradient/65276model-sampled label（通常source CE0）を120GPU秒内で計算、'
        'own CUDA trainer gate/timing後、field+probe+本科学+評価1800秒予測内のみ100M一候補へ。旧対照再GPU/再全量scanなし。')
    if phase == 'terminal':
        job = read_json(study.RUN/'field/job.json')
        if alive(job) or job['status'] != 'complete': raise ValueError('Actual completed absent field job required')
        result = read_json(study.RUN/'field/result.json')
        if (not result['passed'] or not all(result['checks'].values()) or result['GPU_seconds'] != job['GPU_elapsed_seconds']
                or result['GPU_seconds'] > 120 or result['config_sha256'] != sha256(study.CONFIG)):
            raise ValueError('Actual bounded fixed-field evidence required')
        study.uniform.check_reference(result['field'])
        report.update(actual_job=job, result=study.uniform.reference(study.RUN/'field/result.json'),
                      actual_field=result, GPU_seconds=result['GPU_seconds'])
        detail = (f'固定conditional MC Fisher field実完了、actual{job["pid"]}は実不在。GPU{result["GPU_seconds"]:.6f}秒/120、'
            f'実64score gradient/65276model-sampled label/65536physical、source CE/optimizer0。'
            f'10,001,152 unique119/weights・RNG・Param.grad不変/会計合格、field globalmean{result["normalization"]["normalized_coordinate_mean"]:.8f}、'
            f'max{result["normalized_field_max"]:.6f}、zero{result["normalized_zero_coordinates"]}。'
            'model-sampled conditional Fisherの局所近似で有限保持/日本語品質の証明ではない。field.ptはnative保存/親・memory・source・tensor/rawSHA拘束。'
            '次はown inherited-state CUDA4対2+2/32timing/保存費用を120秒内で測り、field+probe+本科学+評価1800秒予測内のみ'
            '同parent/Adam/source/full100M CE/lambdaの一候補比較を凍結する。旧uniform全80/日本語/dev対照は再実行せず再利用。')
    atomic_json(destination, report)
    files = [destination, study.CONFIG, study.PROPOSAL, Path(__file__),
             ROOT/'reports/phase6/fisher_parameter_anchor_tests.xml', *[ROOT/p for p in study.SOURCES]]
    if phase == 'terminal':
        files += [p for p in sorted((study.RUN/'field').rglob('*')) if p.is_file() and p.suffix in ('.json', '.py', '.ps1', '.xml')]
    files = list(dict.fromkeys(files))
    archive = destination.with_name(destination.stem+'_evidence.tar.gz')
    with tarfile.open(archive, 'w:gz') as output:
        for path in files: output.add(path, arcname=path.relative_to(ROOT).as_posix(), recursive=False)
    atomic_json(destination.with_name(destination.stem+'_portable.json'),
        dict(files={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size, sha256=sha256(p)) for p in files},
             file_count=len(files), archive=study.uniform.reference(archive), tensors_native_only=True))
    prefix = ('Base専用Fisher parameter field: '+phase+'（2026-10-06 JST）。Base未完成・完成時通知して停止、Chat/Dialogue/SFT/量子化なし。\n\n'
        +detail+'\n\n全旧不採用/数値7/Phase0–3/相対・絶対・歴史Web1%品質基準を維持。field/seed/回数/normalization/module/lambda/CP救済sweepなし。'
        '合格recipeのみ独立学習seed/full dev/protected test/採用へ。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。\n\n')
    for relative in ('docs/autonomous_status.md', 'docs/15_project_roadmap.md', 'docs/windows_handoff.md'):
        path = ROOT/relative
        path.write_text(prefix+path.read_text(encoding='utf-8-sig'), encoding='utf-8')
    path = ROOT/'reports/phase6/five_step_progress.json'
    progress = read_json(path)
    progress.update(status=report['status'], updated_at=now(), next_action=detail,
                    Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False)
    progress['fisher_parameter_field_'+phase] = study.uniform.reference(destination)
    atomic_json(path, progress)
    print(json.dumps(dict(status=report['status'], GPU_seconds=report['GPU_seconds'], portable_files=len(files))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=('preparation', 'terminal'))
    main(parser.parse_args().phase)
