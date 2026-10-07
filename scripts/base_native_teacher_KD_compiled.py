"""Compile the frozen hidden helper, retaining bare model/checkpoint objects.

Training is single-threaded. Dispatch substitution lasts only for one step,
including failures; the original eager trainer and source remain untouched.
"""
import copy
import threading
import torch
import base_native_teacher_KD_trainer as eager

ORIGINAL_HIDDEN = eager.right_padded_hidden
RECIPE = dict(helper='natural_context_contrast_trainer.right_padded_hidden',
              backend='inductor', mode='default', dynamic=True, fullgraph=True)
_compiled_hidden = None
_dispatch_lock = threading.RLock()


def compiled_hidden():
    global _compiled_hidden
    with _dispatch_lock:
        if _compiled_hidden is None:
            _compiled_hidden = torch.compile(ORIGINAL_HIDDEN,
                backend=RECIPE['backend'], mode=RECIPE['mode'],
                dynamic=RECIPE['dynamic'], fullgraph=RECIPE['fullgraph'])
        return _compiled_hidden


class CompiledNativeTeacherKDTrainer(eager.NativeTeacherKDTrainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spec['hidden_execution'] = copy.deepcopy(RECIPE)
        self._hidden = compiled_hidden()

    def step(self):
        with _dispatch_lock:
            previous = eager.right_padded_hidden
            eager.right_padded_hidden = self._hidden
            try:
                return super().step()
            finally:
                eager.right_padded_hidden = previous
