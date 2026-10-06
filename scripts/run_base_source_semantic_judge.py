"""One persistent BF16 judge run,64 source cases, no student training."""
import hashlib
import json
import os
from pathlib import Path
import sys
import time
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria, StoppingCriteriaList
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json, gpu_lock
from phase6_performance import identity, alive
from base_source_semantic_judge import parse_prediction, agreement, meets_gate

CONFIG = ROOT/'configs/phase6/base_source_semantic_judge.json'
RUN = ROOT/'reports/phase6/base-source-semantic-judge-20261007'


def read(path):
    return json.loads(Path(path).read_text())


def main():
    torch.set_num_threads(2)
    config = read(CONFIG)
    for relative, expected in config['source_sha256'].items():
        if sha256(ROOT/relative) != expected:
            raise ValueError('Frozen judge code/dependencies changed')
    sample = Path(config['original_sample_path'])
    if sha256(sample) != config['original_sample_sha256'] or sha256(Path(config['gold_path'])) != config['gold_sha256']:
        raise ValueError('Original source and pre-inference gold changed')
    recovery = read(config['recovery_path'])
    if sha256(Path(config['recovery_path'])) != config['recovery_sha256']:
        raise ValueError('Verified public model recovery changed')
    for file in recovery['files']:
        stat = Path(file['path']).stat()
        if stat.st_size != file['bytes'] or stat.st_mtime_ns != file['mtime_ns']:
            raise ValueError('Previously hash-verified model changed')
    if not torch.cuda.is_available():
        raise RuntimeError('Actual CUDA inference required')
    RUN.mkdir(parents=True, exist_ok=True)
    job_path = RUN/'job.json'
    if job_path.exists():
        old = read(job_path)
        if alive(old):
            raise ValueError('Judge process actually live; no duplicate')
        if old['status'] == 'complete':
            print('Completed fixed64 judge retained')
            return
        raise ValueError('Preserve incomplete diagnostic; inspect/version repair instead of identical retry')
    rows = read(sample)['rows']
    # Gold is used only after inference; never put scores/reasons in model prompts.
    gold = read(config['gold_path'])['notes']
    job = dict(status='running', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
        GPU_seconds=0, completed_documents=0, scientific_teacher_tokens=0, optimizer_updates=0,
        Base_complete=False, Chat_started=False, quantization_started=False,
        restart_command='scripts/run_base_source_semantic_judge.ps1 -Worker (inspect saved job first; completed run is never repeated)')
    atomic_json(job_path, job)
    predictions = []
    timings = []
    gpu_start = None

    def heartbeat(stage):
        job.update(stage=stage, heartbeat_at=now(), completed_documents=len(predictions),
            GPU_seconds=time.monotonic()-gpu_start if gpu_start is not None else 0)
        atomic_json(job_path, job)

    def check():
        if gpu_start is not None and time.monotonic()-gpu_start > config['GPU_limit_seconds']:
            raise TimeoutError('Fixed judge GPU180s budget exhausted')

    class Deadline(StoppingCriteria):
        def __call__(self, input_ids, scores, **kwargs):
            check()
            return False

    try:
        with gpu_lock('cuda'):
            gpu_start = time.monotonic()
            torch.manual_seed(config['seed'])
            torch.cuda.manual_seed_all(config['seed'])
            torch.cuda.reset_peak_memory_stats()
            heartbeat('load_local_verified_BF16_judge')
            tokenizer = AutoTokenizer.from_pretrained(config['model_directory'], local_files_only=True,
                trust_remote_code=False, padding_side='left')
            model = AutoModelForCausalLM.from_pretrained(config['model_directory'], local_files_only=True,
                trust_remote_code=False, dtype=torch.bfloat16, attn_implementation='sdpa').to('cuda').eval()
            tokenizer.pad_token_id = tokenizer.eos_token_id
            eos = model.generation_config.eos_token_id
            eos = [eos] if isinstance(eos, int) else list(eos)
            for offset in range(0, 64, config['batch']):
                check()
                batch = rows[offset:offset+config['batch']]
                prompts = [tokenizer.apply_chat_template([
                    dict(role='system', content=config['system_prompt']),
                    dict(role='user', content=json.dumps(dict(article=r['text']), ensure_ascii=False))],
                    tokenize=False, add_generation_prompt=True) for r in batch]
                inputs = tokenizer(prompts, padding=True, truncation=False, return_tensors='pt')
                if inputs['input_ids'].shape[1] > config['maximum_input_tokens']:
                    raise ValueError('Whole article input exceeds frozen context; never truncate')
                input_counts = inputs['attention_mask'].sum(dim=1).tolist()
                inputs = inputs.to('cuda')
                torch.cuda.synchronize()
                begin = time.monotonic()
                with torch.inference_mode():
                    sequences = model.generate(**inputs, max_new_tokens=config['max_new_tokens'],
                        do_sample=False, use_cache=True, pad_token_id=tokenizer.pad_token_id,
                        stopping_criteria=StoppingCriteriaList([Deadline()]))
                torch.cuda.synchronize()
                elapsed = time.monotonic()-begin
                for row, sequence, input_count, prompt in zip(batch, sequences[:, inputs['input_ids'].shape[1]:].tolist(), input_counts, prompts, strict=True):
                    endings = [i for i, token in enumerate(sequence) if token in eos]
                    actual = sequence[:endings[0]+1] if endings else sequence
                    text = tokenizer.decode(actual, skip_special_tokens=True)
                    parsed = parse_prediction(text) if endings else None
                    record = dict(index=row['index'], original_document_sha256=row['original_document_sha256'],
                        original_span_sha256=row['original_span_sha256'], full_article_in_prompt=True,
                        prompt_sha256=hashlib.sha256(prompt.encode()).hexdigest(),
                        input_tokens=input_count, generated_ids=actual, generated_tokens=len(actual),
                        stop='EOS' if endings else 'max_new_tokens', raw_output=text, parsed=parsed)
                    predictions.append(record)
                    atomic_json(RUN/'raw'/f"row-{row['index']:02d}.json", record)
                timings.append(dict(offset=offset, documents=len(batch), seconds=elapsed,
                    input_tokens=sum(input_counts), generated_tokens=sum(p['generated_tokens'] for p in predictions[-len(batch):]),
                    original_body_tokens=sum(r['native_body_tokens'] for r in batch)))
                atomic_json(RUN/'partial.json', dict(predictions=predictions, timings=timings))
                heartbeat('classify_original_article_bodies')
                if torch.cuda.max_memory_allocated() > config['maximum_peak_allocated_bytes']:
                    raise MemoryError('Frozen judge memory budget exceeded')
            check()
            peak = torch.cuda.max_memory_allocated()
            del model
            torch.cuda.empty_cache()
        gpu_seconds = time.monotonic()-gpu_start
        all_stats = agreement(predictions, gold, list(range(64)))
        development = agreement(predictions, gold, config['development_indices'])
        holdout = agreement(predictions, gold, config['holdout_indices'])
        passed = meets_gate(holdout, config['gate'])
        classification_seconds = sum(t['seconds'] for t in timings)
        report = dict(status='fixed64_judge_complete_passed' if passed else 'fixed64_judge_complete_rejected',
            created_at=now(), config_sha256=sha256(CONFIG), model=config['model'], revision=config['revision'],
            actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
            original_sample_sha256=config['original_sample_sha256'], gold_sha256=config['gold_sha256'],
            predictions=predictions, timings=timings, all64=all_stats, development=development, holdout=holdout,
            gate=config['gate'], classifier_feasibility_passed=passed, GPU_seconds=gpu_seconds,
            classification_seconds=classification_seconds, peak_allocated_bytes=peak,
            observed_original_body_tokens=sum(r['native_body_tokens'] for r in rows),
            raw_body_tokens_per_second=sum(r['native_body_tokens'] for r in rows)/classification_seconds,
            input_tokens=sum(p['input_tokens'] for p in predictions), generated_tokens=sum(p['generated_tokens'] for p in predictions),
            scientific_teacher_tokens=0, optimizer_updates=0, prepared_training_tokens=0,
            Base_complete=False, Chat_started=False, quantization_started=False, protected_test_bodies_read=False,
            no_gold_labels_or_reasons_in_prompt=True, no_student_weight_changes=True, model_outputs_not_training_targets=True,
            new_weight_download_bytes=0, no_post_outcome_prompt_model_threshold_tuning=True,
            next_action=config['next_on_pass'] if passed else config['failure_action'], limitations=config['limitations'])
        atomic_json(RUN/'result.json', report)
        job.update(status='complete', ended_at=now(), GPU_seconds=gpu_seconds,
            classifier_feasibility_passed=passed, stage='complete', completed_documents=64)
        atomic_json(job_path, job)
        print({k:report[k] for k in ('status','holdout','GPU_seconds','peak_allocated_bytes','raw_body_tokens_per_second')})
    except BaseException as error:
        job.update(status='failed', ended_at=now(), error_type=type(error).__name__)
        heartbeat('failed_preserved_no_identical_retry')
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
