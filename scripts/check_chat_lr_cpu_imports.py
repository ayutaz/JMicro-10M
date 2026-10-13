"""Import CPU adapters with project src bootstrap; never starts model execution."""
from chat_lr_contract import RUN, reference
from jmicro.training import atomic_json
from jmicro.experiment import now
import analyze_chat_lr_results
import compare_chat_lr_observed
import observe_chat_lr
import bind_chat_lr_authored_scores

if __name__ == '__main__':
    modules = (analyze_chat_lr_results, compare_chat_lr_observed, observe_chat_lr, bind_chat_lr_authored_scores)
    atomic_json(RUN / 'CPU_observer_imports.json', dict(passed=True, observed_at=now(),
        modules={module.__name__: reference(module.__file__) for module in modules}, GPU_updates=0, quality_evidence=False))
    print('CPU observer/reviewer entrypoints import successfully; no GPU work')
