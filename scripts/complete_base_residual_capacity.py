"""CPU closeout of bounded capacity control; no new inference or training."""
import json
from pathlib import Path
import sys
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from run_base_residual_capacity import CONFIG, OUTPUT, RUN, ref, checked, conflicting_histories


def complete():
    destination=ROOT/'reports/phase6/base_residual_capacity_control_completion.json'
    if destination.exists(): raise ValueError('Preserve completed capacity control evidence')
    result=read_json(OUTPUT)
    config=checked(result['config'])
    if result['config']!=ref(CONFIG): raise ValueError('Actual repaired config binding differs')
    prepared=checked(config['preparation'])
    rows=prepared['selected']
    job=read_json(RUN/'job.json')
    prior=checked(config['prior_attempt'])
    gate=read_json(RUN/'resume-gate.json')
    first_gate=read_json(ROOT/'reports/phase6/base-residual-capacity-control-20261008/resume-gate.json')
    launcher=read_json(ROOT/'reports/phase6/base-residual-capacity-launcher-r2-20261008/result.json')
    if (alive(job) or alive(prior) or job['status']!='complete' or result['status']!='complete'
            or not job['cumulative_GPU_ledger_closed'] or not result['cumulative_GPU_ledger_closed']
            or result['GPU_seconds']!=job['GPU_seconds'] or result['GPU_seconds']>300
            or abs(result['GPU_seconds']-result['this_process_GPU_seconds']-prior['GPU_seconds'])>1e-9
            or launcher['status']!='complete' or launcher['exit_code'] or not launcher['UI_restore_command_succeeded']
            or gate!=result['resume_gate'] or not all(gate['checks'].values()) or not gate['passed']):
        raise ValueError('Actual exited processes, cumulative budget, all exact-resume checks and successful launcher required')
    counters=result['counters']
    if counters!=job['counters'] or result['teacher_measured_at_update']!=counters['update']:
        raise ValueError('Final teacher accuracy must describe the actual completed update')
    records=[json.loads(line) for line in (RUN/'metrics.jsonl').read_text().splitlines()]
    source_counts={}
    teachers=eos=physical=inputs=body_bytes=cursor=0
    for update,record in enumerate(records,1):
        expected=[]
        for _ in range(80):
            row=rows[cursor%6]; cursor+=1
            count=min(len(row['gold_targets']),3000000-teachers)
            expected.append([row['id'],count])
            teachers+=count
            inputs+=len(row['input_ids'])
            eos+=int(count==len(row['gold_targets']))
            if count==len(row['gold_targets']): body_bytes+=len(bytes.fromhex(row['actual_first_window_body_bytes_hex']))
            source_counts[row['source']]=source_counts.get(row['source'],0)+count
        physical+=80*max(len(rows[(cursor-80+i)%6]['input_ids']) for i in range(80))
        if (record['draws']!=expected or record['counters']['update']!=update
                or record['counters']['supervised_tokens']!=teachers or record['lr']!=.0002):
            raise ValueError('Actual committed original-gold cycle/history differs')
    expected_counters=dict(update=len(records),supervised_tokens=teachers,EOS_targets=eos,
        completed_original_body_bytes=body_bytes,CE_input_tokens=inputs,physical_input_tokens=physical,
        source_teacher_tokens=source_counts,token_digest=records[-1]['counters']['token_digest'])
    if counters!=expected_counters or cursor!=result['cursor'] or not 0<teachers<=3000000:
        raise ValueError('Completed original gold/source/EOS/bytes/physical accounting differs')
    codec=Tokenizer(ROOT/config['tokenizer'])
    if [r['id'] for r in result['free']] != [r['id'] for r in rows]:
        raise ValueError('All six original cases required')
    cases=[]
    for row,free,teacher in zip(rows,result['free'],result['last_teacher'],strict=True):
        gold=row['continuation_gold_ids']
        predicted=teacher['predicted_ids']
        cut=len(row['prompt_ids'])-1
        if (free['generated_ids']!=gold or free['actual_gold_ids']!=gold or gold[-1]!=3
                or not free['exact'] or not free['actual_EOS'] or predicted[cut:]!=gold
                or not teacher['all_conditioned_targets_exact'] or teacher['conditioned_targets']!=len(gold)
                or teacher['correct']!=sum(a==b for a,b in zip(predicted,row['gold_targets'],strict=True))
                or free['raw_UTF8_bytes_hex']!=codec.decode_bytes(gold).hex()
                or free['text']!=codec.decode_bytes(gold).decode('utf-8')):
            raise ValueError('Actual all-six conditioned teacher/free suffix/EOS criterion differs')
        cases.append(dict(id=row['id'],exact_original_suffix_and_actual_EOS=True,
                          conditioned_targets=len(gold),full_teacher_correct=teacher['correct']))
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:
        model=json.load(response)
    original_sha='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    if not alive(ui) or model['checkpoint_sha256']!=original_sha or model['training_tokens']!=10000007168 or model['busy']:
        raise ValueError('Actual original10B idle UI/HTTP restoration required')
    # Checkpoint already hashed by GPU worker once; no duplicate tensor or corpus scan.
    if not Path(result['checkpoint']['path']).is_file(): raise ValueError('Diagnostic completed-update checkpoint missing')
    conflicts=conflicting_histories(rows)
    summary=dict(status='complete',created_at=now(),result=ref(OUTPUT),config=ref(CONFIG),
        process_exited=True,prior_failed_process_exited=True,launcher_exit_code=0,
        GPU_seconds=result['GPU_seconds'],GPU_cap_seconds=300,
        first_failed_gate_GPU_seconds=prior['GPU_seconds'],repaired_process_GPU_seconds=result['this_process_GPU_seconds'],
        verification_updates=first_gate['verification_updates']+gate['verification_updates'],
        verification_teacher_tokens=first_gate['verification_teacher_tokens']+gate['verification_teacher_tokens'],
        original_unique_teacher_tokens=sum(len(r['gold_targets']) for r in rows),
        diagnostic_learning_teacher_tokens=teachers,completed_updates=counters['update'],
        initial_full_teacher_correct=sum(r['correct'] for r in result['initial_teacher']),
        initial_conditioned_teacher_correct=sum(r['conditioned_correct'] for r in result['initial_teacher']),
        final_full_teacher_correct=sum(r['correct'] for r in result['last_teacher']),
        full_teacher_argmax_theoretical_upper_bound=sum(len(r['gold_targets']) for r in rows)-sum(c['unavoidable_argmax_errors'] for c in conflicts),
        final_conditioned_teacher_correct=sum(r['conditioned_correct'] for r in result['last_teacher']),
        conditioned_teacher_targets=sum(len(r['continuation_gold_ids']) for r in rows),
        capacity_control_passed=result['capacity_control_passed'],all6_cases=cases,
        all6_raw_continuations_individually_read=True,
        content_reading_notes='All six originals reproduced, including awkward source wording and source factual claims; exact memorization is neither correctness of those claims nor quality on new prompts. Source roughness was retained, not edited away.',
        counters=counters,checkpoint=result['checkpoint'],restored_UI_identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},
        restored_UI_model=model,scientific_Base_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_scored=False,
        conclusion='The corrected current sequential2B learning/evaluation path can memorize these six already-seen TRAIN units and stop at original EOS. An end-to-end inability to learn these examples is unsupported. This does not establish generalization, explain corpus-wide repetition, validate all data quality or qualify Base.',
        next_action='Use the current same-checkpoint TRAIN versus separate DEV teacher/free diagnostics to separate broad underfitting from generation degradation. Define one bounded comparison and decision rule before any new GPU training; reuse existing six-case and historical diagnostics, no corpus rescan or quantity-only extension.')
    atomic_json(destination,summary)
    print(json.dumps(dict(status='complete',capacity_control_passed=summary['capacity_control_passed'],
        teachers=teachers,GPU_seconds=summary['GPU_seconds'],Base_complete=False,restored_UI=ui['pid'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    complete()
