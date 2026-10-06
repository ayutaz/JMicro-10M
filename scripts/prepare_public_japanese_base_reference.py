"""Pin and recover one small public Japanese Base for an 80-case reference."""
import os
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from huggingface_hub import HfApi, hf_hub_download
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive, identity

REPOSITORY = 'rinna/japanese-gpt2-xsmall'
RUN = ROOT / 'reports/phase6/public-japanese-base-reference-recovery-20261007'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/public-japanese-base-reference-20261007/model')
FILES = ('README.md', 'config.json', 'tokenizer_config.json', 'special_tokens_map.json', 'spiece.model', 'model.safetensors')


def main():
    started = time.monotonic()
    if (RUN / 'result.json').exists():
        raise ValueError('Preserve completed reference recovery')
    if (RUN / 'job.json').exists():
        raise ValueError('Inspect existing reference recovery process/files before retrying')
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='running', **identity(), started_at=now(), stage='metadata', repository=REPOSITORY,
               source_sha256=sha256(Path(__file__)), optimizer_updates=0, GPU_seconds=0,
               Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(RUN / 'job.json', job)
    def check():
        if time.monotonic() - started > 180:
            raise TimeoutError('Public reference recovery wall budget180s exceeded')
    try:
        references = {}
        for name in ('document_context_ablation_completion.json', 'broad_context_diagnostic_review.json',
                     'teacher_semantic_signal_review.json', 'base_next_two_token_comparison_completion.json'):
            path = ROOT / 'reports/phase6' / name
            references[name] = dict(path=str(path), sha256=sha256(path))
        if (read_json(Path(references['document_context_ablation_completion.json']['path']))['completed_endpoint_history_dependence_marker']
                or read_json(Path(references['teacher_semantic_signal_review.json']['path']))['conservative_context_signal_gate_passed']
                or read_json(Path(references['base_next_two_token_comparison_completion.json']['path']))['eligible_for_final_Base_validation']):
            raise ValueError('Retain actual closed branches; unexpected metadata requires review')
        info = HfApi(token=False).model_info(REPOSITORY, files_metadata=True, token=False)
        check()
        if info.private or info.gated or info.card_data.get('license') != 'mit':
            raise ValueError('Anonymous public MIT reference required')
        available = {row.rfilename: row for row in info.siblings}
        if any(name not in available for name in FILES):
            raise ValueError('Official config/tokenizer and safetensors weights required')
        total = sum(available[name].size for name in FILES)
        if total > 256 * 1024**2:
            raise ValueError('Fixed public reference download ceiling256MiB exceeded')
        declared = [dict(name=name, bytes=available[name].size,
                         lfs_sha256=available[name].lfs.sha256 if available[name].lfs else None) for name in FILES]
        proposal = dict(created_at=now(), repository=REPOSITORY, revision=info.sha, license='MIT',
            primary_source='https://huggingface.co/rinna/japanese-gpt2-xsmall', references=references,
            question='How does a separately trained small Japanese Base perform on the fixed native80 continuation suite?',
            scope='Reference generation only; not a parameter-matched causal comparison, teacher-transfer rescue or adopted10M model.',
            files=declared, download_bytes=total, recovery_wall_limit_seconds=180,
            planned_GPU_limit_seconds=180, generation_cases=80, split='dev', decoding='greedy', max_new_tokens=64,
            content='Read every generated continuation; same grammar/relevance/coherence/completion rubric; reuse native control notes.',
            completion='Pinned recovered public weights/config/codec; full80 actual CUDA generation, raw IDs/text/flags/lengths, all80 individual content review, exited process, original UI restoration and local commit.',
            failure='Stop readiness/codec/finite/budget failure. No model/prompt/token-budget/decoder rescue or repeated reference selection.',
            limitations='Different total parameters, architecture, tokenizer, training data and budget. Same64 foreign tokens do not imply equal bytes or GPU budget. Record tokenizer normalization and UNK coverage. Public pretraining benchmark contamination unknown. No native quality gate is relaxed.',
            student_parameters=10001152, tokenizer_training=False, student_optimizer_updates=0,
            new_student_training_tokens=0, protected_test_scored=False,
            Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
            quality_criteria_unchanged=True)
        atomic_json(RUN / 'proposal.json', proposal)
        DATA.mkdir(parents=True, exist_ok=True)
        recovered = []
        for row in declared:
            check()
            job.update(stage='recover', file=row['name'], heartbeat_at=now())
            atomic_json(RUN / 'job.json', job)
            path = Path(hf_hub_download(REPOSITORY, row['name'], revision=info.sha, token=False, local_dir=DATA))
            digest = sha256(path)
            if path.stat().st_size != row['bytes'] or row['lfs_sha256'] and digest != row['lfs_sha256']:
                raise ValueError('Pinned public model file integrity differs: ' + row['name'])
            recovered.append(dict(path=str(path), bytes=path.stat().st_size, sha256=digest, mtime_ns=path.stat().st_mtime_ns))
        check()
        result = dict(status='public_Japanese_Base_recovered_reference_evaluation_pending', created_at=now(),
                      repository=REPOSITORY, revision=info.sha, files=recovered, proposal_sha256=sha256(RUN / 'proposal.json'),
                      wall_seconds=time.monotonic() - started, GPU_seconds=0, actual_identity=identity(),
                      Base_complete=False, Chat_started=False, quantization_started=False)
        atomic_json(RUN / 'result.json', result)
        job.update(status='complete', stage='complete', ended_at=now(), wall_seconds=result['wall_seconds'])
        atomic_json(RUN / 'job.json', job)
        print(json.dumps(dict(status=result['status'], revision=info.sha, bytes=total, wall_seconds=result['wall_seconds'])))
    except BaseException as error:
        job.update(status='failed', ended_at=now(), error=repr(error))
        atomic_json(RUN / 'job.json', job)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
