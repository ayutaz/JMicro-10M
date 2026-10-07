"""Create distinct sigsoftmax GPU commands; never change completed study bytes."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]


def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Expected one workflow block: ' + old[:90])
    return text.replace(old, new)


def renamed(path):
    return ((ROOT / path).read_text().replace('base_confidence_penalty', 'base_sigsoftmax')
        .replace('base-confidence-penalty', 'base-sigsoftmax')
        .replace('ConfidencePenaltyTrainer', 'SigSoftmaxTrainer')
        .replace('confidence_penalty', 'sigsoftmax').replace('confidence_positions', 'sigsoftmax_positions')
        .replace('full hybrid', 'full sigsoftmax').replace('native hybrid', 'native sigsoftmax')
        .replace('middle-head', 'sigsoftmax').replace('confidence-loss transition', 'output-link transition'))


def main():
    pending = {}
    probe = renamed('scripts/probe_base_confidence_penalty.py')
    probe = probe.replace(', confidence_losses', '')
    probe = probe.replace('from phase6_performance import identity, alive',
        'from phase6_performance import identity, alive\nfrom base_sigsoftmax_model import LINK, SigSoftmaxModel, sigsoftmax_logits\nfrom jmicro.model import JMicroModel')
    probe = probe.replace('tests/test_base_sigsoftmax_trainer.py', 'tests/test_base_sigsoftmax.py')
    probe = probe.replace("'tests/test_base_sigsoftmax.py',", "'tests/test_base_sigsoftmax.py', 'tests/test_base_sigsoftmax_evaluation.py',")
    probe = probe.replace("'uv.lock')", "'scripts/base_sigsoftmax_model.py', 'scripts/base_sigsoftmax_evaluation.py', 'uv.lock')")
    begin = probe.index('    tests = ROOT/')
    end = probe.index('    atomic_json(CONFIG, plan)', begin)
    probe = probe[:begin] + '''    tests = ROOT/'reports/phase6/base_sigsoftmax_tests_v2.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 14 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Fourteen actual CPU sigsoftmax protocol checks required')
    proposal = read_json(PROPOSAL)
    evaluation_tests = ROOT/'reports/phase6/base_sigsoftmax_evaluation_tests.xml'
    esuites = list(ET.parse(evaluation_tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in esuites) != 5 or any(int(s.attrib[k]) for s in esuites for k in ('failures','errors','skipped')):
        raise ValueError('Five actual typed likelihood/evaluator checks required')
    cpu_path = ROOT/'reports/phase6/base_sigsoftmax_CPU_preparation_v2.json'
    cpu = read_json(cpu_path)
    if not all(cpu['real_parent_checks'].values()) or cpu['proposal']['sha256'] != sha256(PROPOSAL) or cpu['tests']['sha256'] != sha256(tests):
        raise ValueError('Actual14 and native10M CPU proof required')
    for name,digest in cpu['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('CPU-verified source changed')
    parent_stat = Path(old['parent']['path']).stat()
    if proposal['parent']!=old['parent'] or proposal['source_binding']!=old['source_binding'] or proposal['goals']!=old['goals']:
        raise ValueError('Fixed original parent/source/gold proposal differs')
    plan = dict(created_at=now(), kind='sigsoftmax_original100M_probe', proposal=ref(PROPOSAL),
        CPU_tests=ref(tests), CPU_evaluation_tests=ref(evaluation_tests), CPU_preparation=ref(cpu_path), source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        payload=old_probe['payload'], parent=old['parent'], parent_size=parent_stat.st_size,
        parent_mtime_ns=parent_stat.st_mtime_ns, source_binding=old['source_binding'], goals=old['goals'],
        tokenizer=old['tokenizer'],tokenizer_sha256=old['tokenizer_sha256'],
        dev_shards=old['dev_shards'],dev_manifest_sha256=old['dev_manifest_sha256'],suite_sha256=old['suite_sha256'],evaluation=old['evaluation'],
        batch=48, seed=42, probe_GPU_cap_seconds=180, total_GPU_cap_seconds=4800,
        warmup_updates=3,timed_updates=32,control_CE=old['control_CE'],
        control_result=ref(ROOT/'reports/phase6/natural-context-contrast-comparison-20261007/CE/train-result.json'),
        output_probability_link=LINK,Base_complete=False,Chat_started=False,quantization_started=False)
''' + probe[end:]
    probe = probe.replace("('proposal','CPU_tests','payload','control_CE','control_result')", "('proposal','CPU_tests','CPU_evaluation_tests','CPU_preparation','payload','control_CE','control_result')")
    begin = probe.index('            history = []; histories')
    probe = probe[:begin] + '''            linked = SigSoftmaxModel(t.model.config).to('cuda').eval()
            linked.load_state_dict(parent['model'],strict=True)
            raw = JMicroModel(parent['model_config']).to('cuda').eval()
            raw.load_state_dict(parent['model'],strict=True)
            diag = read_json(p['CPU_preparation']['path'])['train_diagnostic_sequences'][0][:32]
            test_ids = torch.tensor([diag],device='cuda')
            with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',dtype=torch.bfloat16):
                a,b = raw(test_ids,use_cache=True),linked(test_ids,use_cache=True)
                initial['typed_BF16_full_link_once'] = torch.equal(b.logits,sigsoftmax_logits(a.logits))
                initial['same_weight_BF16_greedy_order'] = torch.equal(a.logits.argmax(-1),b.logits.argmax(-1))
                cut = len(diag)//2
                a,b = raw(test_ids[:,:cut],use_cache=True),linked(test_ids[:,:cut],use_cache=True)
                a,b = raw(test_ids[:,cut:],cache=a.cache,use_cache=True),linked(test_ids[:,cut:],cache=b.cache,use_cache=True)
                initial['typed_BF16_cache_link_once'] = torch.equal(b.logits,sigsoftmax_logits(a.logits))
            initial['tagged_link'] = t.model.config['output_probability_link']==LINK
            del linked,raw,test_ids,a,b; clear()
''' + probe[begin:]
    begin = probe.index('            before=host(t.model.state_dict())')
    end = probe.index('            states, logs = [], []', begin)
    probe = probe[:begin] + '''            before=host(t.model.state_dict())
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                selected=targets.ne(-100)
                scores=t.model.lm_head(right_padded_hidden(t.model,ids)[selected])
                loss=F.cross_entropy(scores,targets[selected])
            loss.backward()
            gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(targets.ne(-100).sum()),
                peak_VRAM_bytes=torch.cuda.max_memory_allocated(),optimizer_updates=0,
                unchanged_weights=equal_state(before,host(t.model.state_dict())),sigsoftmax_NLL_loss=float(loss.detach()),
                gradient_norm=float(gradient),decoder_forwards=1,output_probability_link=LINK)
            if not capacity['unchanged_weights'] or not all(math.isfinite(capacity[k]) for k in ('sigsoftmax_NLL_loss','gradient_norm')) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite single-forward tagged sigsoftmax worst shape required')
            del t,before,ids,targets,scores,loss; clear()
''' + probe[end:]
    probe = probe.replace("sigsoftmax=states[0]['sigsoftmax']", 'sigsoftmax_recipe=RECIPE')
    probe = probe.replace("verification_sigsoftmax_positions=sum(r.get('sigsoftmax_positions_this_update',0) for h in histories.values() for r in h)",
        "verification_linked_probability_positions=sum(r.get('probability_positions_this_update',0) for h in histories.values() for r in h)")
    pending['scripts/probe_base_sigsoftmax.py'] = probe
    for name in ('probe', 'run'):
        pending[f'scripts/{name}_base_sigsoftmax.ps1'] = renamed(f'scripts/{name}_base_confidence_penalty.ps1')
    run = renamed('scripts/run_base_confidence_penalty.py')
    run = run.replace('import run_complete_text_comparison as evaluation',
        'import base_sigsoftmax_evaluation as evaluation\nfrom base_sigsoftmax_model import LINK')
    run = run.replace("'uv.lock')", "'scripts/base_sigsoftmax_model.py', 'scripts/base_sigsoftmax_evaluation.py', 'tests/test_base_sigsoftmax_evaluation.py', 'uv.lock')")
    run = run.replace("sigsoftmax=state['sigsoftmax']", "sigsoftmax_recipe=RECIPE,model_config=state['model_config'],output_probability_link=LINK")
    run = once(run, "            evaluation.RUN = RUN/'evaluation'\n", '')
    run = once(run, "evaluated = evaluation.evaluate('sigsoftmax',record,dev,tok,c,binding,beat,check,started+c['GPU_budget_seconds']-prior)",
        "evaluated = evaluation.evaluate('sigsoftmax',record,dev,tok,c,binding,beat,check,started+c['GPU_budget_seconds']-prior,RUN/'evaluation')")
    run = run.replace("failure='One fixed confidence condition; no coefficient/temperature/annealing/threshold/LR/source/parent/batch/decoder/cap rescue or automatic extension.",
        "failure='One fixed probability link; no shift/temperature/calibration/variant/LR/source/parent/batch/backend/decoder/cap rescue or automatic extension.")
    pending['scripts/run_base_sigsoftmax.py'] = run
    review = renamed('scripts/review_base_confidence_penalty.py')
    review = review.replace('from phase6_performance import alive', 'from phase6_performance import alive\nfrom base_sigsoftmax_model import LINK')
    review = review.replace("state['sigsoftmax']!=record['sigsoftmax']", "state['spec']['sigsoftmax']!=record['sigsoftmax_recipe'] or state['model_config']!=record['model_config'] or record['output_probability_link']!=LINK")
    begin = review.index('    if any(not all(math.isfinite(r[k])')
    end = review.index('    if template:', begin)
    review = review[:begin] + '''    if any(not all(math.isfinite(r[k]) for k in ('CE_loss','sigsoftmax_NLL_loss','combined_loss','gradient_norm')) or
            r['CE_loss']!=r['sigsoftmax_NLL_loss'] or r['combined_loss']!=r['sigsoftmax_NLL_loss'] or
            r['committed_update'] is not True or r['output_probability_link']!=LINK or
            r['probability_positions_this_update']!=r['CE_targets_this_update']
            for r in history.values()): raise ValueError('Finite committed hard-gold sigsoftmax NLL history required')
    if (ev.get('output_probability_link')!=LINK or not ev.get('linked_head_used_for_full_cache_generation_and_likelihood')):
        raise ValueError('Tagged linked likelihood/generation evaluation required')
''' + review[end:]
    review = review.replace("sigsoftmax=state['sigsoftmax']", 'sigsoftmax_recipe=RECIPE,output_probability_link=LINK')
    review = review.replace('only added native confidence loss differs', 'only normalized output link differs; exact original hard gold; model NLL uses sigsoftmax')
    review = review.replace('prediction entropy regularization differs', 'normalized output probability link differs')
    pending['scripts/review_base_sigsoftmax.py'] = review
    pending['tests/test_base_sigsoftmax_run.py'] = (ROOT / 'tests/test_base_native_hint_run.py').read_text().replace('run_base_native_hint', 'run_base_sigsoftmax')
    for path in pending:
        if (ROOT / path).exists():
            raise ValueError('Preserve separately prepared source: ' + path)
    for path, text in pending.items():
        (ROOT / path).write_text(text, encoding='utf-8', newline='')
    print('Created seven distinct commands/test sources; old studies unchanged')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
