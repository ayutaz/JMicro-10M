"""Reuse actual process/UI/kernel-lock observer, write only the new run."""
from chat_lr_contract import RUN
import inspect_chat_semantic_environment as observer

observer.RUN = RUN
# Include Base trainers too; future resumption must never race unrelated jobs.
observer.PATTERNS += ('scripts/run_base_', 'scripts/run_chat_lr.py', 'scripts/evaluate_chat_lr.py')

if __name__ == '__main__':
    observer.inspect()
