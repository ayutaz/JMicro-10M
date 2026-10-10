"""Dialogue mid-training with optional Base replay and complete-turn windows.

Mid-training learns user/assistant bodies, roles and EOT. SFT's narrower
Assistant-body/EOT mask remains in chat_training.py. No adoption is implied.
"""
import hashlib
import json
import math
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch
from jmicro.experiment import ROOT, sha256
from jmicro.tokenizer import ROLE_IDS
from jmicro.training import Trainer, DocumentSampler, implementation_hashes


class DialogueWindows:
    """Each original message is supervised once per epoch, without pair cuts.

    A long conversation continues in a new window with as much of the previous
    complete pair as fits. Context-only repeated history has no teacher labels.
    Optional system text is taught only in the first window. A source dialogue
    ending with an unanswered user is preserved; no assistant is fabricated.
    """
    def __init__(self, records, tokenizer, context, seed):
        if context < 2 or not records:
            raise ValueError("Nonempty train dialogues and context>=2 required")
        self.context, self.seed = context, seed
        self.windows = []; identities = set()
        for record in records:
            if record.get("split") != "train" or record["doc_id"] in identities:
                raise ValueError("Unique train dialogues required")
            identities.add(record["doc_id"])
            messages = record.get("messages")
            if messages is None: messages = json.loads(record["messages_json"])
            roles = [m["role"] for m in messages]
            offset = int(bool(roles) and roles[0] == "system")
            if len(roles)-offset < 2 or roles[offset:] != [
                    "user" if i%2 == 0 else "assistant" for i in range(len(roles)-offset)]:
                raise ValueError("Alternating dialogue with at least one complete pair required")
            pieces = []
            for message in messages:
                body = tokenizer.encode(message.get("text", message.get("content", "")))
                if not body: raise ValueError("Empty dialogue message")
                role = message["role"]
                pieces.append(([ROLE_IDS[role], *body, 7], ["role", *([role]*len(body)), "EOT"]))
            start = offset
            while start < len(pieces):
                old = pieces[:offset] if offset else []
                previous = pieces[start-2:start] if start > offset else []
                required = sum(len(p[0]) for p in pieces[start:start+2])
                system_length = sum(len(p[0]) for p in old)
                if 1+system_length+required > context+1:
                    raise ValueError("System/current complete pair exceeds context")
                if 1+system_length+sum(len(p[0]) for p in previous)+required > context+1:
                    previous = []
                prefix = [2]; labels = [-100]; kinds = ["context"]
                for ids, types in old+previous:
                    prefix.extend(ids)
                    teach_system = start == offset and not previous
                    labels.extend(ids if teach_system else [-100]*len(ids))
                    kinds.extend(types if teach_system else ["context"]*len(ids))
                end = start
                while end < len(pieces):
                    pair = pieces[end:end+2]
                    if len(prefix)+sum(len(p[0]) for p in pair) > context+1: break
                    for ids, types in pair:
                        prefix.extend(ids); labels.extend(ids); kinds.extend(types)
                    end += len(pair)
                assert end > start and labels[-1] == 7
                self.windows.append(dict(doc_id=record["doc_id"], first_message=start, end_message=end,
                    ids=np.asarray(prefix, dtype=np.int64), labels=np.asarray(labels, dtype=np.int64), kinds=kinds))
                start = end
        digest = hashlib.sha256()
        for window in self.windows:
            digest.update(json.dumps([window["doc_id"], window["first_message"], window["end_message"]], ensure_ascii=False).encode())
            for field in ("ids", "labels"): digest.update(window[field].astype("<i8").tobytes())
        self.binding = digest.hexdigest()
        self.byte_lengths = np.asarray([0 if i < 8 else len(tokenizer.decode_bytes([i])) for i in range(tokenizer.vocab_size)])
        self.epoch = self.position = 0; self._shuffle()

    def _shuffle(self):
        self.order = np.random.default_rng(np.random.SeedSequence([self.seed, self.epoch])).permutation(len(self.windows))

    def state_dict(self):
        return dict(kind="complete-pair-dialogue-v1", binding=self.binding, context=self.context,
            seed=self.seed, windows=len(self.windows), epoch=self.epoch, position=self.position)

    def load_state_dict(self, state):
        current = self.state_dict()
        if any(state[k] != current[k] for k in ("kind", "binding", "context", "seed", "windows")):
            raise ValueError("Dialogue data or configuration differs")
        if type(state["epoch"]) is not int or state["epoch"] < 0 or type(state["position"]) is not int or not 0 <= state["position"] <= len(self.windows):
            raise ValueError("Invalid dialogue cursor")
        self.epoch, self.position = state["epoch"], state["position"]; self._shuffle()

    def next_window(self):
        if self.position == len(self.windows):
            self.epoch += 1; self.position = 0; self._shuffle()
        window = self.windows[int(self.order[self.position])]; self.position += 1
        return window


class DialogueReplaySampler:
    """Frozen separate source series budgets; the final window stays complete."""
    def __init__(self, records, tokenizer, replay, context, seed, budgets):
        if set(budgets) != {"dialogue", "replay"} or any(type(v) is not int or v < 0 for v in budgets.values()) or budgets["dialogue"] <= 0:
            raise ValueError("Positive dialogue and nonnegative replay series budgets required")
        if budgets["replay"] and replay is None: raise ValueError("Replay budget requires train replay data")
        self.context, self.seed, self.budgets = context, seed, dict(budgets)
        self.dialogue = DialogueWindows(records, tokenizer, context, seed)
        self.replay = DocumentSampler(replay, context, seed+1) if budgets["replay"] else None
        replay_manifest = sha256(replay.directory/"manifest.json") if self.replay else None
        self.binding = hashlib.sha256(json.dumps(dict(dialogue=self.dialogue.binding,
            replay_manifest=replay_manifest, context=context, seed=seed, budgets=budgets), sort_keys=True).encode()).hexdigest()
        self.byte_lengths = self.dialogue.byte_lengths
        self.source_series = dict(dialogue=0, replay=0)
        self.source_inputs = dict(dialogue=0, replay=0)
        self.source_teachers = dict(dialogue=0, replay=0)
        self.source_examples = dict(dialogue=0, replay=0)
        self.dialogue_teacher_kinds = dict(user=0, assistant=0, system=0, role=0, EOT=0)
        self.physical_tokens = self.updates = 0

    @property
    def series_tokens(self): return sum(self.source_series.values())

    @property
    def input_tokens(self): return sum(self.source_inputs.values())

    @property
    def teacher_tokens(self): return sum(self.source_teachers.values())

    @property
    def complete(self): return all(self.source_series[k] >= v for k,v in self.budgets.items())

    def state_dict(self):
        return dict(kind="dialogue-replay-budget-v1", binding=self.binding, context=self.context, seed=self.seed,
            budgets=self.budgets, dialogue=self.dialogue.state_dict(), replay=self.replay.state_dict() if self.replay else None,
            source_series=self.source_series.copy(), source_inputs=self.source_inputs.copy(), source_teachers=self.source_teachers.copy(),
            source_examples=self.source_examples.copy(), dialogue_teacher_kinds=self.dialogue_teacher_kinds.copy(),
            physical_tokens=self.physical_tokens, updates=self.updates)

    def load_state_dict(self, state):
        if any(state[k] != self.state_dict()[k] for k in ("kind", "binding", "context", "seed", "budgets")):
            raise ValueError("Frozen mid-training data/recipe differs")
        for field in ("source_series", "source_inputs", "source_teachers", "source_examples"):
            if set(state[field]) != set(self.budgets) or any(type(n) is not int or n < 0 for n in state[field].values()):
                raise ValueError("Invalid source counters")
        if any(type(state[k]) is not int or state[k] < 0 for k in ("physical_tokens", "updates")):
            raise ValueError("Invalid physical/update counters")
        for source in self.budgets:
            if (state["source_series"][source] != state["source_inputs"][source]+state["source_examples"][source]
                    or state["source_teachers"][source] > state["source_inputs"][source]
                    or state["source_series"][source] >= self.budgets[source]+self.context+1):
                raise ValueError("Inconsistent source accounting")
            if not self.budgets[source] and any(state[f][source] for f in ("source_series", "source_inputs", "source_teachers", "source_examples")):
                raise ValueError("Disabled source has exposure")
        kinds = state["dialogue_teacher_kinds"]
        if set(kinds) != set(self.dialogue_teacher_kinds) or any(type(n) is not int or n < 0 for n in kinds.values()) or sum(kinds.values()) != state["source_teachers"]["dialogue"]:
            raise ValueError("Inconsistent dialogue teacher kinds")
        if sum(state["source_inputs"].values()) > state["physical_tokens"]:
            raise ValueError("Physical capacity smaller than input")
        self.dialogue.load_state_dict(state["dialogue"])
        if self.replay: self.replay.load_state_dict(state["replay"])
        for source, sampler in (("dialogue", self.dialogue), ("replay", self.replay)):
            if sampler:
                length = len(sampler.windows) if source == "dialogue" else sampler.blocks
                if state["source_examples"][source] != sampler.epoch*length+sampler.position:
                    raise ValueError("Source cursor and examples differ")
        for field in ("source_series", "source_inputs", "source_teachers", "source_examples", "dialogue_teacher_kinds"):
            setattr(self, field, dict(state[field]))
        self.physical_tokens, self.updates = state["physical_tokens"], state["updates"]

    def batch(self, size):
        if self.complete: raise ValueError("Mid-training series budgets exhausted")
        if type(size) is not int or size <= 0: raise ValueError("Positive batch required")
        x = torch.zeros((size, self.context), dtype=torch.long); y = torch.full_like(x, -100); byte_count = 0
        for row in range(size):
            available = [s for s in self.budgets if self.source_series[s] < self.budgets[s]]
            if not available: break
            source = min(available, key=lambda s:self.source_series[s]/self.budgets[s])
            if source == "dialogue":
                window = self.dialogue.next_window(); count = len(window["ids"])-1
                x[row,:count] = torch.from_numpy(window["ids"][:-1]); y[row,:count] = torch.from_numpy(window["labels"][1:])
                for kind in window["kinds"][1:]:
                    if kind != "context": self.dialogue_teacher_kinds[kind] += 1
            else:
                a,b,_ = self.replay.batch(1); x[row],y[row] = a[0],b[0]; count = int(a.ne(0).sum())
            teachers = y[row][y[row] >= 0].numpy()
            byte_count += int(self.byte_lengths[teachers].sum())
            self.source_series[source] += count+1; self.source_inputs[source] += count
            self.source_teachers[source] += len(teachers); self.source_examples[source] += 1
        self.physical_tokens += size*self.context; self.updates += 1
        return x,y,byte_count


class DialogueTrainer(Trainer):
    """Adopted-Base weights, fresh mid-training optimizer and separate counters."""
    def __init__(self, parent, parent_ref, records, tokenizer, dataset_directory, replay, spec, budgets, device="cpu"):
        if parent["implementation_sha256"] != implementation_hashes(): raise ValueError("Base implementation differs")
        if spec.get("sampler") != "document" or spec.get("training_fast_path") or spec["accumulation"] != 1:
            raise ValueError("Mid-training requires document PAD masks and accumulation1")
        sampler = DialogueReplaySampler(records, tokenizer, replay, spec["context"], spec["seed"], budgets)
        source = SimpleNamespace(directory=Path(dataset_directory), split="train", manifest=dict(vocab_size=tokenizer.vocab_size),
            tokens=np.zeros(spec["context"]+1, dtype="<u2"), index=[dict(offset=0, body_tokens=spec["context"]-1)], byte_lengths=sampler.byte_lengths)
        assert sha256(Path(parent_ref["path"])) == parent_ref["sha256"]
        actual_spec = dict(spec, dialogue_midtraining=dict(budgets=dict(budgets), data_binding=sampler.binding,
            base_checkpoint_sha256=parent_ref["sha256"], trainer_sha256=sha256(Path(__file__)),
            supervision="Dialogue user/assistant/system bodies, role and EOT; replay body/EOS; old overlap/PAD masked",
            minimum_lr_ratio=.1, stable_fraction=.9))
        super().__init__(parent["model_config"], source, actual_spec, device)
        self.model.load_state_dict(parent["model"], strict=True); self.sampler = sampler
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _:1.)
        self.lineage = dict(kind="dialogue-midtraining-fresh-optimizer", parent_update=0, parent_tokens=0,
            base_checkpoint=dict(parent_ref), base_update=parent["update"], base_tokens=parent["tokens"],
            base_supervised_tokens=parent["supervised_tokens"], base_token_digest=parent["token_digest"],
            optimizer_policy="fresh", RNG_policy="new frozen mid-training seed", local_counters_start_at_zero=True)
        assert not self.optimizer.state and self.update == self.tokens == self.supervised_tokens == 0
        self._set_mid_lr()

    def _set_mid_lr(self):
        fraction = max(0., min(1., (self.sampler.series_tokens/sum(self.sampler.budgets.values())-.9)/.1))
        lr = self.spec["lr"]*(.1+.9*(1+math.cos(math.pi*fraction))/2)
        lr *= min(1., (self.update+1)/max(1, self.spec["warmup"]))
        for group in self.optimizer.param_groups: group["lr"] = lr
        self.scheduler._last_lr = [lr]*len(self.optimizer.param_groups)
        return lr

    def step(self):
        self._set_mid_lr(); before_input, before_physical = self.sampler.input_tokens, self.sampler.physical_tokens
        row = super().step()
        self.tokens -= (self.sampler.physical_tokens-before_physical)-(self.sampler.input_tokens-before_input)
        assert self.tokens == self.sampler.input_tokens and self.supervised_tokens == self.sampler.teacher_tokens
        assert self.update == self.sampler.updates
        row.update(tokens_seen=self.tokens, series_tokens=self.sampler.series_tokens,
            source_series=self.sampler.source_series.copy(), source_teachers=self.sampler.source_teachers.copy(),
            dialogue_teacher_kinds=self.sampler.dialogue_teacher_kinds.copy(), valid_input_tokens=self.tokens,
            physical_input_tokens=self.sampler.physical_tokens, padding_input_tokens=self.sampler.physical_tokens-self.tokens)
        self._set_mid_lr(); return row

    def load(self, path, *, decay_branch=False):
        if decay_branch: raise ValueError("Mid-training must resume unchanged")
        lineage = dict(self.lineage); super().load(path)
        if self.lineage != lineage or self.tokens != self.sampler.input_tokens or self.supervised_tokens != self.sampler.teacher_tokens or self.update != self.sampler.updates:
            raise ValueError("Mid-training lineage or accounting differs")
        self._set_mid_lr()
